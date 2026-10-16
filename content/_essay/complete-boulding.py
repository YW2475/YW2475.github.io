"""Prepare the full CC BY-SA Encyclopedia of Earth transcription."""
import hashlib
import json
import re
import sys
from pathlib import Path

import pymupdf

private = Path(__file__).resolve().parent
reader = private / 'readers/boulding-complete'
reader.mkdir(parents=True,exist_ok=True)
source = private / 'originals-2026-10-12/boulding-spaceship/PDFs/The_Economics_of_the_Coming_Spaceship_Earth.pdf'
source_map = reader / 'source_map.json'
if len(sys.argv) == 1 or sys.argv[1] == 'prepare':
    record = next(x for x in json.loads((private/'classics-catalog.json').read_text(encoding='utf-8')) if x['id']=='boulding-spaceship')
    doc = pymupdf.open(source)
    blocks, omitted = [], []
    in_notes = False
    for page_index,page in enumerate(doc):
        for b in page.get_text('blocks',sort=True):
            text = re.sub(r'\s+',' ',b[4]).strip()
            if not text: continue
            if b[1]<60 or (page_index==0 and b[1]<250) or (page_index==13 and b[1]>=470):
                omitted.append({'page':page_index+1,'text':text});continue
            if text=='Notes':in_notes=True;continue
            pieces = re.split(r'(?<=\S)\s+(?=[1-4]\.\s+[A-Z"])',text) if in_notes else [text]
            for piece in pieces:
                kind='footnote' if in_notes else 'paragraph'
                if not in_notes and blocks and not re.search(r'[.!?][\"”)]?$',blocks[-1]['en']) and blocks[-1]['source_page']!=page_index+1:
                    blocks[-1]['en']+=' '+piece
                    blocks[-1]['source_pages'].append(page_index+1)
                else:
                    blocks.append({'type':kind,'en':piece,'source_page':page_index+1,'source_pages':[page_index+1],'source_bbox':list(b[:4])})
    counts={'paragraph':0,'footnote':0}
    for b in blocks:
        counts[b['type']]+=1
        b['id']=('N' if b['type']=='footnote' else 'S')+f'{counts[b["type"]]:03d}'
    assert counts['footnote']==4
    record.update(kind='full',visible=True,status='bilingual-full-licensed-transcription',scope='full-essay',
                  edition='Complete Encyclopedia of Earth transcription of the 1966 essay, including four original notes.',
                  rights='Local source explicitly states: All text is available under Creative Commons Attribution-Share Alike.',
                  license='CC BY-SA (version unspecified in source)',
                  citation='Environmental Quality in a Growing Economy, H. Jarrett (ed.), 1966, pp. 3–14. Complete CC BY-SA transcription by Encyclopedia of Earth.',
                  local_source=str(source.resolve()))
    data={'paper':record,'scope':'full-essay','source_format':'pdf-text','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
          'blocks':blocks,'coverage':{'pdf_pages':14,'paragraphs':counts['paragraph'],'original_notes':4,
             'english_words':sum(len(b['en'].split()) for b in blocks)},'omitted_non_content':omitted,
          'glossary':{'cowboy economy':'牛仔经济','spaceman economy':'宇航员经济','throughput':'吞吐量','entropy':'熵'}}
    source_map.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data['coverage'],ensure_ascii=False))
else:
    data=json.loads(source_map.read_text(encoding='utf-8'));paper=data['paper']
    public=private.parent/'Essay'/paper['folder'];public.mkdir(exist_ok=True)
    q=lambda s:json.dumps(s,ensure_ascii=False)
    typ=['#import "../index.typ": template, tufted','#import "../../_essay/bilingual.typ": zh',
         '#show: template.with(title: '+q(paper['title'])+', author: "Kenneth E. Boulding", date: "1966", lang: "en", css: ("/assets/custom.css", "/assets/essay.css"))',
         '', '= '+paper['title']+' / '+paper['zh_title'],'']
    md=['# '+paper['title'],'',paper['citation'],'','Author: Kenneth E. Boulding. Source transcription: Encyclopedia of Earth / NCSE.',
        'License: Creative Commons Attribution-Share Alike (version unspecified in source). Changes: line breaks rejoined and draft Chinese added.',
        'Source PDF: https://arachnid.biosci.utexas.edu/courses/THOC/Readings/Boulding_SpaceshipEarth.pdf','']
    notes_started=False
    for b in data['blocks']:
        assert b.get('zh')
        if b['type']=='footnote' and not notes_started:
            typ+=['== Notes / 注释',''];md+=['## Notes / 注释',''];notes_started=True
        typ+=[f'#html.p(id: "en-{b["id"]}")[#text({q(b["en"])})]','',f'#zh(id: "{b["id"]}")[#text({q(b["zh"])})]','']
        md+=[f'<!-- source-id: {b["id"]}; PDF page: {b["source_page"]} -->',b['en'],'',b['zh'],'']
    (public/'index.typ').write_text('\n'.join(typ),encoding='utf-8')
    (reader/'paper.md').write_text('\n'.join(md),encoding='utf-8')
    (reader/'translation_notes.md').write_text('\n'.join(md[:8])+ '\n\nAll 14 source pages processed; four original notes retained. Source site boilerplate omitted. Chinese coverage complete, draft only.\n',encoding='utf-8')
    (private/'boulding-spaceship-source-map.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for filename in ['classics-catalog.json','essay-additions-2026-10-12.json']:
        path=private/filename;records=json.loads(path.read_text(encoding='utf-8'))
        for r in records:
            if r['id']=='boulding-spaceship':r.update(paper);r['translation_status']=data['translation_status']
        path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    index=private.parent/'Essay/index.typ';text=index.read_text(encoding='utf-8')
    if f'path: "{paper["folder"]}/"' not in text:
        anchor='#tufted.blog-entry(\n  date: "1970",\n  path: "The Market for Lemons 1970/",'
        assert anchor in text
        entry='#tufted.blog-entry(\n  date: "1966",\n  path: '+q(paper['folder']+'/')+',\n  title: '+q(paper['title']+' / '+paper['zh_title'])+',\n)\n\n'
        index.write_text(text.replace(anchor,entry+anchor),encoding='utf-8')
    print('Full licensed Boulding page generated.')
