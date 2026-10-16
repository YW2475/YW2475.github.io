"""Translate every source block and table cell; validated batch markers prevent loss."""
import concurrent.futures
import hashlib
import json
import re
import threading
import time
import sys
from pathlib import Path

import requests

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / 'readers' / 'darwin-worms-complete'
source_path = root / 'source_map.json'
source = json.loads(source_path.read_text(encoding='utf-8'))
cache_path = root / 'translation-cache.json'
cache = json.loads(cache_path.read_text(encoding='utf-8')) if cache_path.exists() else {}
jobs, targets = {}, []
manual = {'CONTENTS.': '目录', 'INDEX.': '索引', 'INTRODUCTION.': '引言',
          'CONCLUSION.': '结论', 'HABITS OF WORMS.': '蚯蚓的习性',
          'HABITS OF WORMS— continued.': '蚯蚓的习性（续）',
          'Ounces.': '盎司', 'Nature of Object.': '物体种类',
          'Thickness of mould in inches.': '腐殖土厚度（英寸）'}
roman = {'I': '一', 'II': '二', 'III': '三', 'IV': '四', 'V': '五', 'VI': '六', 'VII': '七'}

def normalize_input(text):
    if root.name != 'darwin-worms-complete':
        return text
    text = re.sub(r'\bvegetable mould\b', 'humus soil', text, flags=re.I)
    text = re.sub(r'\bmould\b', 'humus soil', text, flags=re.I)
    text = re.sub(r'\bearth-worms?\b', lambda m: 'earthworms' if m.group().lower().endswith('s') else 'earthworm', text, flags=re.I)
    text = re.sub(r'\bworms\b', 'earthworms', text, flags=re.I)
    text = re.sub(r'\bworm\b', 'earthworm', text, flags=re.I)
    text = re.sub(r'\bcastings\b', 'earthworm faecal casts', text, flags=re.I)
    text = re.sub(r'\bcasting\b', 'earthworm faecal cast', text, flags=re.I)
    return text

def term_fix(text):
    if root.name != 'darwin-worms-complete':
        return text.strip()
    for old, new in {'腐殖质土壤': '腐殖土', '腐殖质土': '腐殖土', '腐殖质泥土': '腐殖土',
                     '蚯蚓粪便铸件': '蚓粪', '蚯蚓粪便堆': '蚓粪', '蚯蚓粪便': '蚓粪',
                     '鸡胗': '砂囊', '钙腺': '钙质腺'}.items():
        text = text.replace(old, new)
    return text.strip()

def split_text(text):
    parts = []
    rest = text
    while len(rest) > 1800:
        cut = max(rest.rfind('. ', 850, 1800), rest.rfind('; ', 850, 1800), rest.rfind(' ', 850, 1800))
        cut = cut + 1 if cut > 0 else 1800
        parts.append(rest[:cut])
        rest = rest[cut:]
    if rest:
        parts.append(rest)
    assert ''.join(parts) == text
    return parts

def register(target):
    en = target['en']
    if 'zh' in target:
        return
    chapter = re.fullmatch(r'CHAPTER ([IVX]+)\.', en)
    if chapter:
        target['zh'] = '第' + roman[chapter.group(1)] + '章'
        return
    if en in manual:
        target['zh'] = manual[en]
        return
    if not en.strip() or not re.search(r'[A-Za-z]', en):
        target['zh'] = en
        return
    figure = re.fullmatch(r'Fig\.\s*(\d+)\.', en)
    if figure:
        target['zh'] = '图 ' + figure.group(1) + '。'
        return
    parts = split_text(en)
    keys = []
    for part in parts:
        key = hashlib.sha256(part.encode('utf-8')).hexdigest()[:16].upper()
        keys.append(key)
        jobs[key] = normalize_input(part)
    targets.append((target, keys))

for block in source['blocks']:
    if block['type'] == 'table':
        for row in block['rows']:
            for cell in row:
                register(cell)
    elif 'en' in block:
        register(block)

missing = [(key, text) for key, text in jobs.items() if key not in cache]
batches, current, length = [], [], 0
for item in missing:
    if current and (length + len(item[1]) + 40 > 3300 or len(current) == 12):
        batches.append(current)
        current, length = [], 0
    current.append(item)
    length += len(item[1]) + 40
if current:
    batches.append(current)

local = threading.local()
def request(text):
    if not hasattr(local, 'session'):
        local.session = requests.Session()
    for attempt in range(3):
        try:
            response = local.session.get('https://translate.googleapis.com/translate_a/single', params={
                'client': 'gtx', 'sl': 'en', 'tl': 'zh-CN', 'dt': 't', 'q': text,
            }, timeout=45)
            response.raise_for_status()
            result = ''.join(item[0] for item in response.json()[0] if item[0])
            if not result.strip():
                raise ValueError('Empty translation')
            return result
        except Exception:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)

def translate_batch(items):
    q = '\n'.join(f'[[TX{key}]]\n{text}' for key, text in items)
    translated = request(q).replace('［', '[').replace('］', ']')
    matches = list(re.finditer(r'\[\[\s*TX\s*([A-F0-9]{16})\s*\]\]', translated, re.I))
    if [m.group(1).upper() for m in matches] == [key for key, _ in items]:
        result = {}
        for i, match in enumerate(matches):
            end = matches[i+1].start() if i+1 < len(matches) else len(translated)
            result[match.group(1).upper()] = term_fix(translated[match.end():end])
        if all(result.values()):
            return result
    # A changed/missing marker is never accepted as an aligned translation.
    return {key: term_fix(request(text)) for key, text in items}

print(f'Translating {len(missing)} segments in {len(batches)} validated batches', flush=True)
done = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    futures = [pool.submit(translate_batch, batch) for batch in batches]
    for future in concurrent.futures.as_completed(futures):
        cache.update(future.result())
        done += 1
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        if done % 10 == 0 or done == len(batches):
            print(f'Completed batches: {done}/{len(batches)}; translated segments: {len(cache)}/{len(jobs)}', flush=True)

for target, keys in targets:
    target['zh'] = ''.join(cache[key] for key in keys)
    target['translation_method'] = 'machine-draft; source order and terminology checked'
for block in source['blocks']:
    if block['type'] == 'table':
        for row in block['rows']:
            for cell in row:
                assert 'zh' in cell
    elif 'en' in block:
        assert block.get('zh', '').strip()
source['translation_status'] = 'complete-coverage; draft translation, not sentence-by-sentence proofread'
source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Every source paragraph, heading, caption, original note and table cell now has a paired translation', flush=True)
