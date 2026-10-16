"""Source-map the licensed 2005 complete reprint, retaining all original notes."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import pymupdf

private = Path(__file__).resolve().parent
reader = private / 'readers/geertz-complete'
reader.mkdir(parents=True, exist_ok=True)
pdf = private / 'originals-2026-10-12/geertz-cockfight/PDFs/Deep_Play_2005_complete.pdf'
doc = pymupdf.open(pdf)
old = json.loads((private / 'geertz-cockfight-source-map.json').read_text(encoding='utf-8'))
backup = reader / 'previous-abridged-source-map.json'
if not backup.exists():
    backup.write_text(json.dumps(old, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def normalize(s):
    s = s.replace('½', 'fi').replace('ﬂ', 'fl').replace('ﬁ', 'fi')
    return re.sub(r'\s+', ' ', s).strip()

def join(a, b):
    # A printed hyphen at a column/line end is retained in genuinely compound words.
    if a.endswith('-') and re.match(r'^[a-z]', b):
        return a[:-1] + b
    return a.rstrip() + ' ' + b.lstrip()

body, notes, skipped = [], [], []
kept_lines = 0
raw_chars = 0
for page_index, page in enumerate(doc):
    number = page_index + 56
    blocks = [b for b in page.get_text('dict')['blocks'] if b['type'] == 0]
    blocks.sort(key=lambda b: (0 if b['bbox'][0] < 250 else 1, b['bbox'][1]))
    for block in blocks:
        x, y, _, _ = block['bbox']
        all_text = normalize(' '.join(''.join(s['text'] for s in l['spans']) for l in block['lines']))
        if x < 60 or x > 443 or y > 655 or (page_index == 0 and (y < 210 or (x < 250 and y > 505))):
            skipped.append({'page': number, 'bbox': block['bbox'], 'text': all_text})
            continue
        lines = block['lines']
        font_weights = Counter()
        for line in lines:
            for span in line['spans']:
                font_weights[round(span['size'])] += len(span['text'])
        size = font_weights.most_common(1)[0][0]
        kind = 'footnote' if size <= 9 else 'paragraph'
        base = 63 if x < 250 else 258
        pieces, current = [], ''
        for line_index, line in enumerate(lines):
            text = normalize(''.join(s['text'] for s in line['spans']))
            if not text:
                continue
            kept_lines += 1
            raw_chars += len(text)
            indent = line['bbox'][0] - base
            dropcap = any(s['size'] >= 20 for s in line['spans'])
            new_note = kind == 'footnote' and bool(re.match(r'^(?:[1-9]|[1-3][0-9]|4[0-3])\s+[A-Z“‘]', text))
            new_para = kind == 'paragraph' and size == 11 and (indent > 5 or dropcap)
            if current and (new_note or new_para):
                pieces.append(current)
                current = ''
            current = join(current, text) if current else text
        if current:
            pieces.append(current)
        dest = notes if kind == 'footnote' else body
        for piece_index, text in enumerate(pieces):
            first = lines[0]
            starts_indented = first['bbox'][0] - base > 5
            dropcap = any(s['size'] >= 20 for s in first['spans'])
            if kind == 'footnote':
                starts_new = bool(re.match(r'^(?:[1-9]|[1-3][0-9]|4[0-3])\s+[A-Z“‘]', text))
            else:
                starts_new = piece_index > 0 or starts_indented or dropcap or size == 10
            if dest and not starts_new:
                dest[-1]['en'] = join(dest[-1]['en'], text)
                dest[-1]['source_pages'].append(number)
                dest[-1]['source_bboxes'].append(block['bbox'])
            else:
                dest.append({'type': kind, 'en': text, 'source_page': number,
                             'source_pages': [number], 'source_bboxes': [block['bbox']]})

def match_key(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())
previous = {match_key(b.get('en', '')): b['zh'] for b in old['blocks'] if b.get('en') and b.get('zh')}
for prefix, blocks in [('S', body), ('N', notes)]:
    for i, block in enumerate(blocks, 1):
        block['id'] = f'{prefix}{i:03d}'
        if match_key(block['en']) in previous:
            block['zh'] = previous[match_key(block['en'])]
            block['translation_method'] = 'retained-previous-translation'
note_numbers = [int(re.match(r'^(\d+)\s', b['en']).group(1)) for b in notes if re.match(r'^(\d+)\s', b['en'])]
assert note_numbers == list(range(1,44)), note_numbers
paper = dict(old['paper'], kind='full', visible=True, status='bilingual-full-licensed-reprint',
             citation='Dædalus 134(4), Fall 2005, pp. 56–86; complete reprint of the 1972 essay.',
             source='https://direct.mit.edu/daed/article/134/4/56/27395/Deep-play-notes-on-the-Balinese-cockfight',
             edition='2005 complete licensed reprint; not the 1973 expanded book chapter.',
             rights='© 2005 American Academy of Arts & Sciences; CC BY-NC 4.0.',
             license='https://creativecommons.org/licenses/by-nc/4.0/',
             scope='complete-2005-reprint', local_source=str(pdf.resolve()))
out = {'paper': paper, 'scope': paper['scope'], 'source_format': 'pdf-text',
       'source_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
       'blocks': body + notes,
       'coverage': {'pdf_pages': len(doc), 'printed_pages': '56–86', 'paragraphs': len(body),
                    'original_notes': len(notes), 'note_numbers': note_numbers,
                    'source_lines_retained': kept_lines, 'source_chars_before_rejoining': raw_chars,
                    'english_words': sum(len(b['en'].split()) for b in body+notes)},
       'omitted_non_content': skipped,
       'glossary': {'deep play':'深层游戏', 'cockfight':'斗鸡', 'status hierarchy':'地位等级',
                    'center bet':'中央赌注', 'side bet':'外围赌注', 'thick description':'深描'}}
(reader / 'source_map.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
print(json.dumps(out['coverage'],ensure_ascii=False))
