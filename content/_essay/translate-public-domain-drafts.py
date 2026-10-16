"""Generate aligned translation drafts for locally public-domain originals."""
import concurrent.futures
import hashlib
import json
import re
import time
from pathlib import Path

import requests

root = Path(__file__).resolve().parent
ids = ['flexner-useless', 'russell-idleness', 'thurber-bed']
cache_path = root / 'public-domain-translation-cache-2026-10-12.json'
cache = json.loads(cache_path.read_text(encoding='utf-8')) if cache_path.exists() else {}
jobs, block_keys = {}, {}

def chunks(text):
    result = []
    while len(text) > 1500:
        cut = max(text.rfind('. ', 650, 1500), text.rfind('; ', 650, 1500), text.rfind(' ', 650, 1500))
        cut = cut + 1 if cut > 0 else 1500
        result.append(text[:cut])
        text = text[cut:]
    if text:
        result.append(text)
    return result

for stem in ids:
    blocks = json.loads((root / f'{stem}-original-blocks.json').read_text(encoding='utf-8'))
    for block in blocks:
        texts = chunks(block['en'])
        assert ''.join(texts) == block['en']
        keys = [hashlib.sha256(text.encode('utf-8')).hexdigest() for text in texts]
        block_keys[stem, block['id']] = keys
        jobs.update(zip(keys, texts))

def translate(item):
    key, text = item
    for attempt in range(3):
        try:
            r = requests.get('https://translate.googleapis.com/translate_a/single', params={
                'client': 'gtx', 'sl': 'en', 'tl': 'zh-CN', 'dt': 't', 'q': text,
            }, timeout=35)
            r.raise_for_status()
            zh = ''.join(part[0] for part in r.json()[0] if part[0])
            if not zh.strip():
                raise ValueError('Empty translation')
            return key, zh
        except Exception:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    tasks = [pool.submit(translate, item) for item in jobs.items() if item[0] not in cache]
    for future in concurrent.futures.as_completed(tasks):
        key, zh = future.result()
        cache[key] = zh
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        if len(cache) % 15 == 0 or len(cache) == len(jobs):
            print(f'Translation segments: {len(cache)}/{len(jobs)}', flush=True)
for stem in ids:
    blocks = json.loads((root / f'{stem}-original-blocks.json').read_text(encoding='utf-8'))
    translations = {block['id']: ''.join(cache[key] for key in block_keys[stem, block['id']]) for block in blocks}
    (root / f'{stem}-translations.json').write_text(json.dumps(translations, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(stem, len(translations), 'translated paragraphs')
