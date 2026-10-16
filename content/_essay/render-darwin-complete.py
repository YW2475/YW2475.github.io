"""Render the complete source-aligned book; keep editorial notes private."""
import json
import shutil
from pathlib import Path

private = Path(__file__).resolve().parent
reader = private / 'readers/darwin-worms-complete'
data = json.loads((reader / 'source_map.json').read_text(encoding='utf-8'))
paper = data['paper']
public = private.parent / 'Essay' / paper['folder']
(public / 'assets').mkdir(exist_ok=True)
for asset in (reader / 'assets').glob('*.jpg'):
    shutil.copy2(asset, public / 'assets' / asset.name)

def quote(value):
    return json.dumps(value, ensure_ascii=False)

def table(block, language):
    rows = []
    for row in block['rows']:
        cells = []
        for cell in row:
            attrs = f'colspan: {cell["colspan"]}, rowspan: {cell["rowspan"]}'
            cells.append('#html.td(' + attrs + ')[#text(' + quote(cell.get(language, '')) + ')]')
        rows.append('  #html.tr[' + ' '.join(cells) + ']')
    return '#html.table(id: "' + language + '-' + block['id'] + '", class: "essay-book-table")[\n' + '\n'.join(rows) + '\n]'

typ = ['#import "../index.typ": template, tufted',
       '#import "../../_essay/bilingual.typ": zh',
       '#show: template.with(',
       '  title: ' + quote(paper['title']) + ',',
       '  author: "Charles Darwin", date: "1881", lang: "en",',
       '  description: ' + quote(paper['description']) + ',',
       '  css: ("/assets/custom.css", "/assets/essay.css", "/assets/essay-book.css"),',
       ')', '', '= ' + paper['title'] + ' / ' + paper['zh_title'], '']
md = ['# ' + paper['title'], '', paper['citation'], '', 'Source: ' + data['source_url'], '']
for block in data['blocks']:
    ident = block['id']
    kind = block['type']
    md += [f'<!-- source-id: {ident}; original-page: {block.get("source_page")} -->']
    if kind == 'figure':
        typ += [f'#html.figure(id: "{ident}", class: "essay-paper-figure")[#image({quote(block["path"])})]', '']
        md += [f'![{ident}]({block["path"]})', '']
    elif kind == 'table':
        typ += [table(block, 'en'), '', table(block, 'zh'), '']
        for language in ('en', 'zh'):
            md.append('<table>')
            import html
            for row in block['rows']:
                md.append('<tr>' + ''.join(f'<td colspan="{c["colspan"]}" rowspan="{c["rowspan"]}">{html.escape(c.get(language, ""))}</td>' for c in row) + '</tr>')
            md += ['</table>', '']
    elif kind == 'heading':
        level = block.get('heading_level', 2)
        # Plain text prevents original punctuation from becoming Typst markup.
        typ += ['=' * level + ' #text(' + quote(block['en'] + ' / ' + block['zh']) + ')', '']
        md += ['#' * level + ' ' + block['en'], '', block['zh'], '']
    else:
        cls = ', class: "essay-original-caption"' if kind == 'caption' else ''
        typ += [f'#html.p(id: "en-{ident}"{cls})[#text({quote(block["en"])})]', '',
                f'#zh(id: "{ident}")[#text({quote(block["zh"])})]', '']
        md += [block['en'], '', block['zh'], '']

(public / 'index.typ').write_text('\n'.join(typ), encoding='utf-8')
(reader / 'paper.md').write_text('\n'.join(md), encoding='utf-8')
(private / 'darwin-source-map.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(reader / 'translation_notes.md').write_text('''# Full-book coverage

The 1881 fifth thousand (corrected) contains the title matter, contents,
Introduction, Chapters I–VII and Index. The final entry is Zincke, p. 326.
All 802 text blocks, 15 original figures and 8 table fragments are retained.
Each original paragraph, heading, caption, footnote and table cell has Chinese.
Only cover/spine repeats, printed folios/signatures and publisher advertisements
after the Index are excluded. Original paragraphs split by page breaks are joined.
Translations have complete coverage, but are draft translations rather than a
sentence-by-sentence proofread edition. Exact matching old translations were kept.

## Terminology

vegetable mould / mould: 腐殖土
worms: 蚯蚓
castings: 蚓粪
burrows: 洞穴
gizzard: 砂囊
denudation: 剥蚀
calciferous glands: 钙质腺

The former Chapter VII-only source map is backed up alongside this reader.
''', encoding='utf-8')
print('Full-book page and private aligned reader generated.')
