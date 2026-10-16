"""Extract the complete 1881 book, excluding only covers, folios and adverts."""
import concurrent.futures
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, NavigableString

root = Path(__file__).resolve().parent
reader = root / 'readers' / 'darwin-worms-complete'
assets = reader / 'assets'
assets.mkdir(parents=True, exist_ok=True)
url = 'https://darwin-online.org.uk/converted/published/1881_Worms_F1361/1881_Worms_F1361.html'
r = requests.get(url, timeout=45)
r.raise_for_status()
(reader / 'original.html').write_bytes(r.content)
soup = BeautifulSoup(r.content, 'lxml')
book = soup.body.find('div', recursive=False)
old = json.loads((root / 'darwin-source-map.json').read_text(encoding='utf-8'))
backup = reader / 'previous-chapter-VII-source-map.json'
if not backup.exists():
    backup.write_text(json.dumps(old, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
def norm(text):
    return re.sub(r'\s+', ' ', text).strip()
old_translations = {norm(b['en']): b['zh'] for b in old.get('blocks', []) if b.get('en') and b.get('zh')}
blocks, omitted, figure_urls = [], [], {}
counts = Counter()
page = None
started = False
in_index = False
figure_pending = None
last_body = None
page_changed = False
source_node = 0

def add_text(text, kind='paragraph', heading_level=2):
    global figure_pending, last_body, page_changed
    text = norm(text)
    if not text:
        return
    if kind == 'paragraph' and figure_pending:
        kind = 'caption'
    footnote = bool(re.match(r'^[*†‡]', text))
    if footnote:
        kind = 'footnote'
    # Rejoin paragraphs cut only by a printed page break; retain the footnotes.
    if kind == 'paragraph' and not in_index and page_changed and last_body and not re.search(r'[.!?][\"”’\)]?$', last_body['en']):
        last_body['en'] += ' ' + text
        last_body['source_pages'].append(page)
        last_body['source_nodes'].append(source_node)
        page_changed = False
        return
    prefixes = {'paragraph': 'S', 'footnote': 'N', 'heading': 'H', 'caption': 'C'}
    prefix = prefixes[kind]
    counts[prefix] += 1
    block = {'id': f'{prefix}{counts[prefix]:03d}', 'type': kind, 'en': text,
             'source_page': page, 'source_pages': [page], 'source_nodes': [source_node],
             'order': len(blocks), 'heading_level': heading_level}
    if text in old_translations:
        block['zh'] = old_translations[text]
        block['translation_method'] = 'retained-previous-human-translation'
    if kind == 'caption':
        block['figure_id'] = figure_pending
        # A short "Fig. 2." label is followed by the actual caption paragraph.
        if not re.fullmatch(r'Fig\.\s*\d+\.', text):
            figure_pending = None
    blocks.append(block)
    if kind == 'paragraph':
        last_body = block
        page_changed = False
    elif kind in ('heading', 'caption'):
        last_body = None

def add_image(image):
    global figure_pending, last_body
    src = image.get('src')
    number = int(re.search(r'fig(\d+)', src).group(1))
    fig_id = f'F{number:03d}'
    file = f'{fig_id}.jpg'
    figure_urls[file] = urljoin(url, src)
    blocks.append({'id': fig_id, 'type': 'figure', 'source_page': page,
                   'order': len(blocks), 'path': 'assets/' + file, 'original_source': figure_urls[file]})
    figure_pending = fig_id
    last_body = None

def consume(node):
    global page, started, in_index, figure_pending, source_node, page_changed
    if not getattr(node, 'name', None):
        return
    source_node += 1
    if node.name == 'img':
        add_image(node)
        return
    if node.name == 'table':
        if node.find('img'):
            # These are two layout tables with original figures and adjacent prose.
            for td in node.find_all(['td', 'th']):
                inline = []
                def flush_inline():
                    if norm(''.join(inline)):
                        add_text(''.join(inline))
                    inline.clear()
                for child in td.children:
                    if isinstance(child, NavigableString):
                        inline.append(str(child))
                    elif child.name in ('p', 'h3', 'table', 'img'):
                        flush_inline()
                        consume(child)
                    else:
                        inline.append(child.get_text())
                flush_inline()
        else:
            counts['T'] += 1
            rows = []
            for ri, tr in enumerate(node.find_all('tr')):
                cells = []
                for ci, cell in enumerate(tr.find_all(['td', 'th'], recursive=False)):
                    cells.append({'id': f'T{counts["T"]:03d}-r{ri+1}c{ci+1}', 'en': norm(cell.get_text(' ', strip=True)),
                                  'colspan': int(cell.get('colspan', 1)), 'rowspan': int(cell.get('rowspan', 1))})
                rows.append(cells)
            blocks.append({'id': f'T{counts["T"]:03d}', 'type': 'table', 'source_page': page,
                           'order': len(blocks), 'rows': rows})
        return
    if node.name not in ('p', 'h3'):
        for child in node.children:
            consume(child)
        return
    text = norm(node.get_text(' ', strip=True))
    marker = re.fullmatch(r'\[page\]?\s*\(?\s*([\divxlc]+)\s*\)?\]?', text, re.I)
    if marker:
        page = marker.group(1)
        started = started or page == 'i'
        page_changed = True
        omitted.append({'type': 'folio', 'text': text, 'source_node': source_node})
        return
    if not started or not text and not node.find('img'):
        if text:
            omitted.append({'type': 'cover-furniture', 'text': text, 'source_node': source_node})
        return
    if text.startswith('[page') or text.startswith('[inside') or text.startswith('[front'):
        omitted.append({'type': 'page-furniture', 'text': text, 'source_node': source_node})
        return
    if re.fullmatch(r'[B-X](?:\s+2)?', text) and not in_index and node.get('align') != 'center':
        omitted.append({'type': 'printer-signature', 'text': text, 'source_node': source_node})
        return
    for image in node.find_all('img'):
        add_image(image)
    if text:
        if text == 'INDEX.':
            in_index = True
        is_heading = node.name == 'h3' or (node.get('align') == 'center' and text.isupper() and len(text) < 220)
        if is_heading and not figure_pending:
            level = 2 if re.match(r'CHAPTER|CONTENTS\.|INDEX\.|INTRODUCTION\.', text) else 3
            add_text(text, 'heading', level)
        else:
            add_text(text)

for child in book.children:
    if getattr(child, 'name', None) and norm(child.get_text(' ', strip=True)) == 'BY THE SAME AUTHOR.':
        omitted.append({'type': 'publisher-adverts-after-index', 'starts': 'BY THE SAME AUTHOR.'})
        break
    consume(child)

def download(item):
    file, source = item
    target = assets / file
    if target.exists():
        return
    response = requests.get(source, timeout=45)
    response.raise_for_status()
    if not response.headers.get('Content-Type', '').startswith('image/'):
        raise ValueError('Not an image: ' + source)
    target.write_bytes(response.content)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    list(pool.map(download, figure_urls.items()))

body_chapters = [b for b in blocks if b['type'] == 'heading' and re.fullmatch(r'CHAPTER [IVX]+\.', b['en']) and str(b['source_page']).isdigit()]
assert len(body_chapters) == 7, body_chapters
assert len(figure_urls) == 15
assert counts['T'] == 8
assert in_index
assert any(b.get('en', '').startswith('Zincke, Rev.') for b in blocks)
source_map = {
    'paper': dict(old['paper'], kind='full', source=url,
                  citation='London: John Murray, fifth thousand (corrected), 1881. Full work: title matter, contents, Introduction, Chapters I–VII, Index, pp. i–viii and 1–326.',
                  note='', rights='Public-domain original text and illustrations, newly translated.'),
    'scope': 'full-book', 'edition': '1881 fifth thousand, corrected',
    'source_sha256': hashlib.sha256(r.content).hexdigest(),
    'source_url': url, 'blocks': blocks, 'omitted_non_content': omitted,
    'coverage': {'body_chapters': [b['en'] for b in body_chapters], 'figures': len(figure_urls),
                 'table_fragments': counts['T'], 'includes_index': True,
                 'text_blocks': sum('en' in b for b in blocks),
                 'original_words': sum(len(b.get('en', '').split()) for b in blocks)},
    'glossary': {'vegetable mould': '腐殖土', 'mould': '腐殖土', 'worms': '蚯蚓', 'castings': '蚓粪',
                 'burrows': '洞穴', 'gizzard': '砂囊', 'humus': '腐殖质', 'humus-acids': '腐殖酸',
                 'denudation': '剥蚀', 'calciferous glands': '钙质腺'},
    'translation_status': 'in-progress; not advertised as complete until every block is translated',
}
(reader / 'source_map.json').write_text(json.dumps(source_map, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(source_map['coverage'], ensure_ascii=False))
print('Source map prepared; existing website remains unchanged until full translation is ready')
