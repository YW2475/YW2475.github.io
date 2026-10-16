"""Translate the public-domain Japanese source; preserve paragraph alignment."""
import concurrent.futures
import hashlib
import json
import re
import time
from pathlib import Path

import requests

root = Path(__file__).resolve().parent
blocks = json.loads((root / 'tanizaki-shadows-original-blocks.json').read_text(encoding='utf-8'))
cache_path = root / 'tanizaki-shadows-translation-cache-normalized.json'
cache = json.loads(cache_path.read_text(encoding='utf-8')) if cache_path.exists() else {}

def segments(text):
    result, current = [], ''
    for sentence in re.findall(r'.*?[。！？]|.+$', text):
        if len(current + sentence) > 1100 and current:
            result.append(current)
            current = ''
        if len(sentence) > 1100:
            if current:
                result.append(current)
                current = ''
            result.extend(sentence[i:i + 1100] for i in range(0, len(sentence), 1100))
        else:
            current += sentence
    if current:
        result.append(current)
    assert ''.join(result) == text
    return result

jobs = {}
block_keys = {}
for block in blocks:
    texts = segments(block['ja'])
    keys = [hashlib.sha256(t.encode('utf-8')).hexdigest() for t in texts]
    block_keys[block['id']] = keys
    jobs.update(zip(keys, texts))

def translate(item):
    key, text = item
    # Modernize only a few repeated orthographic forms in the translation input.
    replacements = {
        'われ／＼': '我々', 'いろ／＼': '色々', 'こゝ': 'ここ',
        '煖房': '暖房', '普請道楽': '建築好き', '茶人': '茶道の愛好家',
        '凝り性': 'こだわりの強い', '梯子段': '階段', '煽風器': '扇風機',
        '地袋': '低い収納棚', '厠': 'トイレ', '朝顔': '男性用小便器',
        '数寄屋': '伝統的な茶室風建築', '行燈': '行灯',
        '吸い物椀': '澄まし汁を入れる漆塗りの椀',
        '英吉利': 'イギリス', '巴里': 'パリ', '亜米利加': 'アメリカ',
        '支那': '中国', '云う': '言う', 'ゐ': 'い', 'ゑ': 'え', 'たゞ': 'ただ',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    for attempt in range(3):
        try:
            response = requests.get('https://translate.googleapis.com/translate_a/single', params={
                'client': 'gtx', 'sl': 'ja', 'tl': 'zh-CN', 'dt': 't', 'q': text,
            }, timeout=35)
            response.raise_for_status()
            zh = ''.join(part[0] for part in response.json()[0] if part[0])
            if not zh.strip():
                raise ValueError('Empty translation')
            return key, zh
        except Exception:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    futures = [pool.submit(translate, item) for item in jobs.items() if item[0] not in cache]
    for future in concurrent.futures.as_completed(futures):
        key, zh = future.result()
        cache[key] = zh
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'Translation segments: {len(cache)}/{len(jobs)}', flush=True)
translations = {block['id']: ''.join(cache[key] for key in block_keys[block['id']]) for block in blocks}
(root / 'tanizaki-shadows-translations.json').write_text(json.dumps(translations, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Completed {len(translations)} aligned Japanese-Chinese paragraphs')
