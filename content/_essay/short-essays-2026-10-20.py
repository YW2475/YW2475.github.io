"""Add complete bilingual short essays; track unavailable readers separately."""
import concurrent.futures
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
ORIGINALS = ROOT / 'originals-2026-10-20'
BATCH = ROOT / 'essay-additions-2026-10-20.json'

def record(ident, title, zh, author, year, category, source, rights='Public-domain original text; new Chinese translation.', **extra):
    return dict(id=ident, title=title, zh_title=zh, author=author, year=year,
                category=category, source=source, folder=f'{title.replace("?", "").replace(":", "")} {year}',
                kind='full', scope='complete-essay', rights=rights, visible=True,
                status='source-acquisition-pending', **extra)

RECORDS = [
    record('franklin-whistle', 'The Whistle', '哨子', 'Benjamin Franklin', 1779, '文学与思想',
           'https://en.wikisource.org/wiki/The_Whistle_(Franklin,_1779)'),
    record('twain-youth', 'Advice to Youth', '给青年人的忠告', 'Mark Twain', 1882, '文学与思想',
           'https://readingrooms.org/demo/advice_to_youth.pdf'),
    record('orwell-tea', 'A Nice Cup of Tea', '一杯好茶', 'George Orwell', 1946, '文学与思想',
           'https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/a-nice-cup-of-tea/',
           rights='Original text is public domain in mainland China (author died 1950); not a claim of worldwide public-domain status. Local personal-study use; no modern translation or editorial introduction copied.', rights_jurisdiction='mainland China'),
    record('chesterton-bed', 'On Lying in Bed', '论赖床', 'G. K. Chesterton', 1909, '文学与思想',
           'https://www.gkc.org.uk/gkc/books/On_Lying_In_Bed.html'),
    record('twain-lying', 'On the Decay of the Art of Lying', '论说谎艺术的衰落', 'Mark Twain', 1880, '文学与思想',
           'https://www.gutenberg.org/cache/epub/2572/pg2572.html', citation='Written in 1880; collected in The Stolen White Elephant, Etc. (1882).'),
    record('adams-internet', 'How to Stop Worrying and Learn to Love the Internet', '如何停止担忧并学会爱上互联网', 'Douglas Adams', 1999, '信息与技术',
           'https://www.douglasadams.com/dna/19990901-00-a.html', rights='No full-reproduction/translation licence confirmed.', kind_override='pending'),
    record('medawar-fraud', 'Is the Scientific Paper a Fraud?', '科学论文是骗局吗？', 'Peter Medawar', 1963, '心智与判断',
           'https://wellcomecollection.org/works/sbvjw9wy', rights='Peter Medawar-authored archive works are explicitly licensed CC BY by Wellcome Collection; third-party works excluded.',
           license='CC BY', transcription_source='https://web350b.ipsp.uni-hohenheim.de/scimeth/literature/medawar_paper_fraud.pdf',
           citation='The Listener 70, 377–378 (1963); archive PP/PBM/E.192. University-hosted transcription cross-checked against the archived essay.'),
    record('thomas-cell', 'The Lives of a Cell', '细胞的生命', 'Lewis Thomas', 1971, '自然与演化',
           'https://www.nejm.org/doi/abs/10.1056/NEJM197105132841908', rights='No full-reproduction/translation licence confirmed.', kind_override='pending'),
    record('bacon-gardens', 'Of Gardens', '论园林', 'Francis Bacon', 1625, '自然与演化',
           'https://www.gutenberg.org/cache/epub/46964/pg46964-images.html'),
    record('lamb-roast', 'A Dissertation upon Roast Pig', '烤猪论', 'Charles Lamb', 1822, '文学与思想',
           'https://www.gutenberg.org/cache/epub/43566/pg43566-images.html'),
    record('haldane-rabbit', 'On Being One’s Own Rabbit', '把自己当作实验兔', 'J. B. S. Haldane', 1927, '自然与演化',
           'https://jbshaldane.org/books/1927-Possible-Worlds/haldane-1927-possible-worlds.html',
           folder_override='On Being Ones Own Rabbit 1927', citation='Possible Worlds and Other Essays (1927), pp. 106–119; complete standalone essay.'),
    record('borges-exactitude', 'On Exactitude in Science', '论科学的精确性', 'Jorge Luis Borges', 1946, '文学与思想',
           'https://sites.lsa.umich.edu/mqr/2015/12/on-the-unsaid/', rights='Protected original and modern English translations; no full-reproduction/translation licence confirmed.',
           kind_override='pending', genre='short parable'),
]
for item in RECORDS:
    if 'folder_override' in item: item['folder'] = item.pop('folder_override')
    if item.pop('kind_override', None) == 'pending':
        item.update(kind='pending', visible=False, status='awaiting-licensed-or-user-provided-full-source')

def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def acquire(item):
    folder = ORIGINALS / item['id']; folder.mkdir(parents=True, exist_ok=True)
    url = item.get('transcription_source', item['source'])
    ext = '.pdf' if url.lower().endswith('.pdf') else '.html'
    target = folder / ('original' + ext)
    if target.exists():
        return {'id': item['id'], 'cached': True, 'path': str(target), 'bytes': target.stat().st_size}
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    if ext == '.pdf': assert r.content.startswith(b'%PDF'), 'Not a PDF'
    target.write_bytes(r.content)
    manifest = dict(id=item['id'], source_url=url, resolved_url=r.url, file=str(target.resolve()),
                    sha256=hashlib.sha256(r.content).hexdigest(), bytes=len(r.content), si_requested=False,
                    access_mode='public-source', format=ext[1:])
    dump(folder/'manifest.json', manifest)
    return {'id': item['id'], 'path': str(target), 'bytes': len(r.content)}

def clean(node):
    copy = BeautifulSoup(str(node), 'html.parser')
    for tag in copy.select('.pagenum, .pageno, .fnanchor'):
        tag.decompose()
    for image in copy.find_all('img'):
        alt = image.get('alt', '')
        image.replace_with(alt if len(alt) == 1 and alt.isalpha() else '')
    # Join inline tags without inserting spaces into restored drop capitals.
    text = copy.get_text()
    return re.sub(r'\s+', ' ', text).strip()

def prepare():
    import pymupdf
    records = json.loads(BATCH.read_text(encoding='utf-8'))
    for item in records:
        if item['kind'] != 'full': continue
        ident = item['id']; folder = ORIGINALS/ident
        blocks=[]; omissions=[]; corrections=[]
        def add(en, kind='paragraph', anchor=None, page=None):
            if not en.strip(): return
            blocks.append(dict(type=kind, en=en, source_anchor=anchor, source_page=page))
        if ident in ('twain-youth', 'medawar-fraud'):
            pdf = folder / ('reprint.pdf' if ident=='medawar-fraud' else 'original.pdf')
            doc=pymupdf.open(pdf)
            for page_index,page in enumerate(doc):
                source_blocks=page.get_text('blocks')
                if ident=='medawar-fraud':
                    left_edge,right_edge=(235,410) if page_index==0 else (225,400)
                    source_blocks.sort(key=lambda b: (0 if b[0]<left_edge else 1 if b[0]<right_edge else 2,b[1]))
                for b in source_blocks:
                    x,y,_,bottom,text,*_=b
                    text=re.sub(r'\s+',' ',text).strip()
                    if not text:continue
                    if ident=='twain-youth':
                        if page_index==0:
                            text=re.sub(r'^"Advice to Youth" \(1882\), Mark Twain \(Samuel Clemens\)\s*','',text)
                    else:
                        if y>775 or (page_index==0 and (y<200 and x<410)) or (page_index==1 and x<405 and y>460) or (page_index==1 and x>405 and y>=745):
                            omissions.append({'page':page_index+1,'text':text});continue
                        text=re.sub(r'(?<=[a-z])-\s+(?=[a-z])','',text)
                        fixes={"I'ather":"rather",'generahzation':'generalization','XHIS conception':'THIS conception','A HE theor>':'THE theory','-•-HIS alternative':'THIS alternative',
                               'natiu"e':'nature',"structiu'e":'structure',")'ou":'you',"\\'ou":'you',"discover}.,":'discovery,',"discover}.'":'discovery,',
                               "un\\'arnished":'unvarnished',"underK'ing":'underlying','the\\ make':'they make','lo\\e':'love',"theory' underlying":'theory underlying',
                               'aie two':'are two',"v.'as":'was','fomi part':'form part','Discouery':'Discovery','Wilham':'William','hypotheses nan jingo':'hypotheses non fingo',
                               "sequor'—l":'sequor’—I','T THIS alternative':'THIS alternative'}
                        for before,after in fixes.items():
                            if before in text: text=text.replace(before,after);corrections.append({'from':before,'to':after})
                        text=re.sub(r'N,\s*I\s*OW let','NOW let',text)
                        if not blocks:text='I '+text
                    if blocks and not re.search(r'[.!?][\"”\)]?$',blocks[-1]['en']) and (ident=='medawar-fraud' or blocks[-1]['source_page']!=page_index+1):
                        blocks[-1]['en']+=' '+text
                        blocks[-1].setdefault('source_continuations',[]).append({'page':page_index+1,'bbox':list(b[:4])})
                    else:add(text,anchor=f'PDF block at {tuple(round(v,1) for v in b[:4])}',page=page_index+1)
            if ident=='medawar-fraud':
                item.update(transcription_source='https://gwern.net/doc/philosophy/epistemology/1964-merton.pdf',
                            edition='Complete text of the 1964 Saturday Review reprint (August 1, pp. 42–43) of the BBC talk; original title in reprint: Is the Scientific Paper Fraudulent?',
                            citation='The Listener 70, 377–378 (1963); reprinted in Saturday Review, August 1, 1964, pp. 42–43, credited to The Experimental Method (BBC). Author-text reuse licence recorded by Wellcome Collection, PP/PBM/E.192.')
        else:
            soup=BeautifulSoup((folder/'original.html').read_bytes(),'lxml')
            if ident=='franklin-whistle':
                item['source']='https://www.gutenberg.org/files/35508/35508-h/35508-h.htm#THE_WHISTLE'
                heading=soup.find(id='THE_WHISTLE').parent
                for tag in heading.find_all_next(['p','h2','h3']):
                    if tag.name in ('h2','h3'):break
                    add(clean(tag),anchor='THE_WHISTLE')
                item['edition']='Complete letter to Madame Brillon, Passy, November 10, 1779, including opening paragraphs and signature. Later editorial bibliography omitted.'
            elif ident=='orwell-tea':
                section=soup.select_one('section.entry-content');started=False
                for tag in section.find_all(recursive=False):
                    if not getattr(tag,'name',None):continue
                    text=clean(tag)
                    if text.startswith('If you look up'):started=True
                    if not started:continue
                    if text.startswith('Evening Standard'):break
                    if tag.name=='ul':
                        for li in tag.find_all('li',recursive=False):add(clean(li))
                    elif tag.name=='p':add(text)
                assert len([b for b in blocks if re.match(r'^(First|Secondly|Thirdly|Fourthly|Fifthly|Sixthly|Seventhly|Eighthly|Ninthly|Tenthly|Lastly)',b['en'])])==11
            elif ident=='chesterton-bed':
                started=False
                for p in soup.find_all('p'):
                    text=clean(p)
                    if text.startswith('Lying in bed would'):started=True
                    if text.startswith('--Gilbert') or text.startswith('Up to G.K.') or text.startswith('Last modified:'):break
                    if started and text:add(text)
                assert blocks[0]['en'].startswith('Lying in bed would')
            elif ident=='twain-lying':
                for tag in soup.body.find_all(recursive=False):
                    if tag.get('id')=='pg-header':continue
                    if tag.get('id')=='pg-footer':break
                    if tag.name=='h2':add(clean(tag),'heading',tag.get('id'))
                    elif tag.name=='p' and tag.get('id')!='id00001':add(clean(tag),'footnote' if tag.get('id')=='id00003' else 'paragraph',tag.get('id'))
            elif ident=='bacon-gardens':
                paragraphs=[p for p in soup.find_all('p') if p.find('img') and any(len(i.get('alt',''))==1 and i.get('alt','').isalpha() for i in p.find_all('img'))]
                assert len(paragraphs)==10
                for p in paragraphs:add(clean(p))
                item['edition']='Complete essay; decorative initial letters restored as text. Later illustrated-edition ornaments and printer colophon omitted.'
            elif ident=='lamb-roast':
                h=next(h for h in soup.find_all('h2') if clean(h)=='UPON ROAST PIG')
                for tag in h.find_all_next(['p','section']):
                    if tag.get('id')=='pg-footer':break
                    if tag.name=='p' and not tag.find_parent('div',class_='figure'):add(clean(tag))
                item['edition']='Complete essay text as printed in the 1888 illustrated edition; later illustrations, title matter and colophon omitted.'
            elif ident=='haldane-rabbit':
                h=next(h for h in soup.find_all('h1') if 'OWN RABBIT' in h.get_text().upper())
                for tag in h.find_all_next(['p','h1']):
                    if tag.name=='h1':break
                    add(clean(tag),'heading' if clean(tag).startswith('THE STORY OF A SKIRMISH') else 'paragraph')
                item['edition']='Complete standalone essay in Possible Worlds and Other Essays (1927), pp. 107–119, including subtitle. First drop capital restored; printed folios omitted.'
        assert blocks and len(' '.join(b['en'] for b in blocks))>500,ident
        if ident=='medawar-fraud':
            expanded=[]
            for b in blocks:
                for part in re.split(r'(?=NOW let me go back)',b['en']):
                    if part.strip():expanded.append(dict(b,en=part.strip()))
            blocks=expanded
        for index,b in enumerate(blocks,1):b.update(id=f'S{index:03d}',order=index-1)
        reader=ROOT/'readers'/ident;reader.mkdir(parents=True,exist_ok=True);(reader/'assets').mkdir(exist_ok=True)
        src=folder/('reprint.pdf' if ident=='medawar-fraud' else 'original.pdf' if ident=='twain-youth' else 'original.html')
        data=dict(paper=item,scope='complete-essay',source_format='pdf-text' if src.suffix=='.pdf' else 'html',
                  source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),blocks=blocks,
                  coverage={'blocks':len(blocks),'english_words':sum(len(b['en'].split()) for b in blocks),'source_beginning':blocks[0]['en'][:100],'source_ending':blocks[-1]['en'][-140:]},
                  omitted_non_content=omissions,transcription_corrections=corrections,
                  glossary={'induction':'归纳','deduction':'演绎','hypothesis':'假说','hypothetico-deductive':'假说—演绎'} if ident=='medawar-fraud' else {'tetany':'手足搐搦症','hydrogen ion concentration':'氢离子浓度'} if ident=='haldane-rabbit' else {})
        dump(reader/'source_map.json',data)
        print(json.dumps({'id':ident,**data['coverage']},ensure_ascii=False),flush=True)
    dump(BATCH,records)

def render():
    records=json.loads(BATCH.read_text(encoding='utf-8'))
    override_path=ROOT/'short-essays-translation-overrides-2026-10-20.json'
    overrides=json.loads(override_path.read_text(encoding='utf-8')) if override_path.exists() else {}
    quote=lambda value:json.dumps(value,ensure_ascii=False)
    for record in records:
        if record['kind']!='full':continue
        reader=ROOT/'readers'/record['id'];data=json.loads((reader/'source_map.json').read_text(encoding='utf-8'))
        assert all(b.get('zh','').strip() for b in data['blocks']),record['id']
        for b in data['blocks']:
            if b['id'] in overrides.get(record['id'],{}):
                b['zh']=overrides[record['id']][b['id']]
                b['translation_method']='human-translated spot correction'
            if record['id']=='medawar-fraud':
                b['en']=b['en'].replace('Hypotheses nan jingo','Hypotheses non fingo').replace('hypotheses non sequor’—I','hypotheses non sequor"—I')
                b['zh']=b['zh'].replace('这篇科学论文','科学论文').replace('假设演绎','假说—演绎').replace('假说演绎','假说—演绎')
            if record['id']=='haldane-rabbit':
                b['zh']=b['zh'].replace('手足抽搐症','手足搐搦症').replace('手足抽搐','手足搐搦症')
        record.update(data['paper'])
        if record['id']=='medawar-fraud':record['title']='Is the Scientific Paper a Fraud?'
        record.update(status='bilingual-complete-draft',translation_status='complete paragraph coverage; draft Chinese translation with spot corrections',
                      completeness='complete source essay, including author subtitle and original notes where present',
                      visible=True,source_acquisition='assistant-retrieved-public-source')
        source_file=ORIGINALS/record['id']/('reprint.pdf' if record['id']=='medawar-fraud' else 'original.pdf' if record['id']=='twain-youth' else 'original.html')
        record['local_source']=str(source_file.resolve())
        dump(source_file.parent/'manifest.json',{'id':record['id'],'file':str(source_file.resolve()),'source_url':record.get('transcription_source',record['source']),
              'sha256':hashlib.sha256(source_file.read_bytes()).hexdigest(),'format':source_file.suffix[1:],
              'status':'downloaded-and-complete-reader-generated','si_requested':False,'rights':record['rights']})
        data['paper']=record
        dump(reader/'source_map.json',data)
        public=ROOT.parent/'Essay'/record['folder'];public.mkdir(exist_ok=True)
        typ=['#import "../index.typ": template, tufted','#import "../../_essay/bilingual.typ": zh',
             '#show: template.with(', '  title: '+quote(record['title'])+',',
             '  author: '+quote(record['author'])+', date: '+quote(str(record['year']))+', lang: "en",',
             '  css: ("/assets/custom.css", "/assets/essay.css"),',')','',
             '= '+record['title']+' / '+record['zh_title'],'']
        md=['# '+record['title'],'','Author: '+record['author'],
            'Source: '+record['source'],'Edition: '+record.get('edition','Complete source essay.'),
            'Rights: '+record['rights'],'Changes: paragraph text extracted and Chinese translation added.','']
        if record.get('license'):md += ['License: '+record['license'],'']
        for b in data['blocks']:
            if b['type']=='heading':
                typ+=['== #text('+quote(b['en']+' / '+b['zh'])+')','']
            else:
                typ += [f'#html.p(id: "en-{b["id"]}")[#text({quote(b["en"])})]','',
                        f'#zh(id: "{b["id"]}")[#text({quote(b["zh"])})]','']
            md += [f'<a id="{b["id"]}"></a>',f'**Source:** {b.get("source_page") or b.get("source_anchor") or record["source"]}',
                   '', '**Original:** '+b['en'],'','**中文:** '+b['zh'],'']
        if data['glossary']:
            md+=['## Terminology / 术语','', '| English | 中文 |', '| --- | --- |']
            md += ['| '+k+' | '+v+' |' for k,v in data['glossary'].items()]
        (public/'index.typ').write_text('\n'.join(typ),encoding='utf-8')
        (reader/'paper.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
        notes=['# Translation and source notes','',record.get('edition','Complete essay text from linked source.'),'',
               'English paragraphs, author headings and original notes retained in order. Each text block has Chinese directly beneath it.',
               'Source website navigation, donation requests, reading guides, publisher title matter, later decorative illustrations and licence boilerplate are excluded from the reading body.',
               'Chinese coverage is complete, but this is a draft translation with limited spot review, not a sentence-by-sentence proofread edition.',
               'Source licence, edition, omitted page furniture and OCR corrections are recorded in source_map.json; they are not displayed as article guide text.','']
        (reader/'translation_notes.md').write_text('\n'.join(notes),encoding='utf-8')

    # Keep the existing page layout and categories, inserting only completed readers.
    index=ROOT.parent/'Essay/index.typ'
    text=index.read_text(encoding='utf-8')
    entry_re=re.compile(r'#tufted\.blog-entry\([\s\S]*?\n\)')
    for record in records:
        if record['kind']!='full' or f'path: "{record["folder"]}/"' in text:continue
        section_re=re.compile(r'(?m)^== [^\n]* / '+re.escape(record['category'])+r'\s*\n')
        heading=section_re.search(text);assert heading,record['category']
        next_heading=re.search(r'(?m)^== ',text[heading.end():])
        end=heading.end()+next_heading.start() if next_heading else len(text)
        entries=list(entry_re.finditer(text,heading.end(),end))
        before=next((e.start() for e in entries if int(re.search(r'date: "(\d+)"',e.group()).group(1))>record['year']),end)
        entry='#tufted.blog-entry(\n  date: '+quote(str(record['year']))+',\n  path: '+quote(record['folder']+'/')+',\n  title: '+quote(record['title']+' / '+record['zh_title'])+',\n)\n\n'
        text=text[:before]+entry+text[before:]
    index.write_text(text,encoding='utf-8')
    catalog_path=ROOT/'classics-catalog.json';catalog=json.loads(catalog_path.read_text(encoding='utf-8'))
    additions={r['id']:r for r in records}
    catalog=[dict(r,**additions.pop(r['id'])) if r['id'] in additions else r for r in catalog]
    catalog.extend(additions.values());dump(catalog_path,catalog);dump(BATCH,records)
    completed=[r for r in records if r['kind']=='full'];pending=[r for r in records if r['kind']!='full']
    lines=['# 短篇 Essay 新增记录（2026-10-20）','',
           f'本批计划12篇，{len(completed)}篇已生成完整逐段双语页；{len(pending)}篇尚未生成全文页，未出现在阅读目录中。',
           '新增文章正文只保留题名、原文与中文，不显示导读、来源与版本说明等栏目。','',
           '| 文章 | 状态 |','| --- | --- |']
    for r in records:lines.append('| '+r['zh_title']+' / '+r['title']+' | '+('完整原文及逐段中文译稿已生成' if r['kind']=='full' else '尚未确认允许全文转载/翻译的许可，等待有许可或用户提供的完整原文')+' |')
    lines += ['','梅达沃采用完整的1964年重印文本，原始讲话/发表年份保留1963，具体来源和CC BY条件记录在内部源映射。',
              '《哨子》保留完整书信开头与署名；《论园林》恢复装饰首字母；《给青年人的忠告》合并跨页段落。',
              '中文为完整覆盖的初译和少量修订，未逐句精校。没有提交、推送或发布。','']
    (ROOT/'short-essays-status-2026-10-20.md').write_text('\n'.join(lines),encoding='utf-8')
    audit={'date':'2026-10-20','requested':12,'added_complete':len(completed),'pending':[{k:r[k] for k in ('id','title','zh_title','source','status')} for r in pending],
           'visible_local_entries':text.count('#tufted.blog-entry('),
           'coverage':[dict(id=r['id'],**json.loads((ROOT/'readers'/r['id']/'source_map.json').read_text(encoding='utf-8'))['coverage']) for r in completed]}
    dump(ROOT/'short-essays-audit-2026-10-20.json',audit)
    print(json.dumps({'added':len(completed),'pending':len(pending),'visible_entries':audit['visible_local_entries']},ensure_ascii=False))

if __name__ == '__main__':
    if sys.argv[1] == 'prepare':
        prepare()
        sys.exit(0)
    if sys.argv[1] == 'render':
        render()
        sys.exit(0)
    if sys.argv[1] == 'acquire':
        ORIGINALS.mkdir(exist_ok=True)
        dump(BATCH, RECORDS)
        results=[]
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            tasks={pool.submit(acquire,item):item for item in RECORDS if item['kind']=='full' or item['id']=='adams-internet'}
            for future in concurrent.futures.as_completed(tasks):
                try: result=future.result()
                except Exception as e: result={'id':tasks[future]['id'],'error':str(e)[:180]}
                results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
        dump(ORIGINALS/'download-results.json',results)
