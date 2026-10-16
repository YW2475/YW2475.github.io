"""Render a complete licensed reprint; no editorial notices in the reading body."""
import json
import re
from pathlib import Path

private = Path(__file__).resolve().parent
reader = private / 'readers/geertz-complete'
data = json.loads((reader / 'source_map.json').read_text(encoding='utf-8'))
paper = data['paper']
public = private.parent / 'Essay' / paper['folder']
public.mkdir(exist_ok=True)
quote = lambda s: json.dumps(s, ensure_ascii=False)
typ = ['#import "../index.typ": template, tufted', '#import "../../_essay/bilingual.typ": zh',
       '#show: template.with(', '  title: ' + quote(paper['title']) + ',',
       '  author: "Clifford Geertz", date: "1972", lang: "en",',
       '  description: ' + quote(paper['description']) + ',',
       '  css: ("/assets/custom.css", "/assets/essay.css"),', ')', '',
       '= ' + paper['title'] + ' / ' + paper['zh_title'], '']
md = ['# ' + paper['title'], '', paper['citation'], '',
      'Author: Clifford Geertz. © 2005 American Academy of Arts & Sciences.',
      'Source: ' + paper['source'], 'License: ' + paper['license'],
      'Changes: PDF text extracted and line/column breaks rejoined; Chinese translation added.', '']
notes_started = False
for block in data['blocks']:
    if block['type'] == 'footnote' and not notes_started:
        typ += ['== Notes / 注释', '']
        md += ['## Notes / 注释', '']
        notes_started = True
    assert block.get('zh')
    ident = block['id']
    typ += [f'#html.p(id: "en-{ident}")[#text({quote(block["en"])})]', '',
            f'#zh(id: "{ident}")[#text({quote(block["zh"])})]', '']
    md += [f'<!-- source-id: {ident}; printed-pages: {sorted(set(block["source_pages"]))} -->',
           block['en'], '', block['zh'], '']
(public / 'index.typ').write_text('\n'.join(typ), encoding='utf-8')
(reader / 'paper.md').write_text('\n'.join(md), encoding='utf-8')
(private / 'geertz-cockfight-source-map.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(reader / 'translation_notes.md').write_text('''# Complete licensed reprint

Clifford Geertz, Deep play: notes on the Balinese cockfight.
Dædalus 134(4), Fall 2005, pp. 56–86. Complete 31-page reprint of the 1972 essay.
© 2005 American Academy of Arts & Sciences. CC BY-NC 4.0.
https://direct.mit.edu/daed/article/134/4/56/27395/Deep-play-notes-on-the-Balinese-cockfight
https://creativecommons.org/licenses/by-nc/4.0/

Changes: English text extracted, broken words/column continuations joined,
running headers and publisher author biography omitted, Chinese added.
The original 43 notes are all retained and translated, in numerical order.
The supplied abridged reprint is preserved separately. This is not the expanded
1973 book chapter. Chinese has complete coverage but remains a draft translation.
No figures or tables are present in this complete reprint; the numbered formal
paradigm and quotations are retained as text blocks in their source order.
''', encoding='utf-8')

for filename in ('classics-catalog.json', 'essay-additions-2026-10-05.json'):
    path = private / filename
    records = json.loads(path.read_text(encoding='utf-8'))
    for record in records:
        if record['id'] == paper['id']:
            record.update(paper)
            record['translation_status'] = data['translation_status']
    path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
index = private.parent / 'Essay/index.typ'
text = index.read_text(encoding='utf-8')
if 'path: "Deep Play 1972/"' not in text:
    anchor = '#tufted.blog-entry(\n  date: "1973",\n  path: "The Strength of Weak Ties 1973/",'
    entry = '#tufted.blog-entry(\n  date: "1972",\n  path: "Deep Play 1972/",\n  title: ' + quote(paper['title']+' / '+paper['zh_title']) + ',\n)\n\n'
    assert anchor in text
    text = text.replace(anchor, entry + anchor)
    index.write_text(text, encoding='utf-8')
print(json.dumps({'full_reprint_pages':31,'paragraphs':data['coverage']['paragraphs'],'original_notes':43,'visible_entries':text.count('#tufted.blog-entry(')},ensure_ascii=False))
