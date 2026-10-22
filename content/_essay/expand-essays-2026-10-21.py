"""Acquire verified editions, align whole essays, and publish only completed readers."""
import concurrent.futures
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / 'originals-2026-10-21'
READERS = ROOT / 'readers'
BATCH = ROOT / 'essay-additions-2026-10-21.json'
CANDIDATES = ROOT / 'essay-candidates-2026-10-21.json'

# Number, stable ID, year, source language, edition URL (empty means candidate URL).
PLAN = [
    (1, 'wallace-varieties', 1858, 'en', 'https://people.wku.edu/charles.smith/wallace/S043.htm'),
    (2, 'muir-windstorm', 1894, 'en', 'https://www.gutenberg.org/cache/epub/10012/pg10012-images.html'),
    (3, 'burroughs-seeing', 1899, 'en', 'https://wehd.com/373/245.html'),
    (4, 'leopold-oak', 1949, 'en', ''),
    (7, 'carson-wonder', 1956, 'en', 'https://www.fws.gov/sites/default/files/documents/2024-04/1056.pdf'),
    (8, 'haldane-life', 1929, 'en', ''),
    (9, 'feynman-value', 1955, 'en', 'https://calteches.library.caltech.edu/1575/1/Science.pdf'),
    (13, 'poincare-creation', 1908, 'en', 'https://www.gutenberg.org/cache/epub/39713/pg39713-images.html'),
    (26, 'simmel-stranger', 1908, 'de', 'https://socio.ch/_original/sim/soziologie/soz_9_ex3.htm'),
    (27, 'simmel-bridge', 1909, 'de', ''),
    (28, 'simmel-metropolis', 1903, 'de', ''),
    (36, 'russell-lived', 1967, 'en', ''),
    (37, 'russell-rubbish', 1943, 'en', ''),
    (38, 'james-blindness', 1899, 'en', ''),
    (39, 'clifford-belief', 1877, 'en', 'https://www.gutenberg.org/cache/epub/50189/pg50189-images.html'),
    (42, 'montaigne-thumbs', 1580, 'en', 'https://www.gutenberg.org/cache/epub/3600/pg3600-images.html'),
    (43, 'montaigne-smells', 1580, 'en', 'https://www.gutenberg.org/cache/epub/3600/pg3600-images.html'),
    (44, 'benjamin-library', 1931, 'de', 'https://www.textlog.de/benjamin/kleine-prosa/denkbilder/packe-bibliothek-aus'),
    (50, 'chesterton-nonsense', 1901, 'en', ''),
    (51, 'orwell-bookshop', 1936, 'en', ''),
    (52, 'orwell-books-cigarettes', 1946, 'en', ''),
    (53, 'orwell-sport', 1945, 'en', ''),
    (54, 'orwell-reviewer', 1946, 'en', ''),
    (55, 'lynd-ignorance', 1921, 'en', 'https://www.gutenberg.org/cache/epub/13448/pg13448-images.html'),
    (56, 'lynd-weeds', 1921, 'en', 'https://www.gutenberg.org/cache/epub/13448/pg13448-images.html'),
    (57, 'lynd-insects', 1921, 'en', 'https://www.gutenberg.org/cache/epub/13448/pg13448-images.html'),
    (60, 'stevenson-love', 1877, 'en', ''),
    (61, 'twain-cornpone', 1923, 'en', 'https://www.gutenberg.org/cache/epub/68604/pg68604-images.html'),
    (62, 'twain-telephone', 1880, 'en', 'https://www.gutenberg.org/cache/epub/142/pg142-images.html'),
    (63, 'zhou-vegetables', 1924, 'zh', ''),
    (64, 'zhou-tea', 1924, 'zh', ''),
    (65, 'feng-gradual', 1931, 'zh', ''),
    (66, 'feng-children', 1926, 'zh', ''),
    (69, 'terada-hotwater', 1922, 'ja', ''),
    (70, 'terada-sugar', 1927, 'ja', 'https://www.aozora.gr.jp/cards/000042/files/2455_10268.html'),
    (71, 'terada-scientist', 1933, 'ja', ''),
    (72, 'nakaya-eggs', 1947, 'ja', ''),
    (73, 'nakaya-snow', 1938, 'ja', ''),
    (74, 'luxun-pagoda', 1924, 'zh', ''),
]
DEATHS = {'wallace':1913,'muir':1914,'burroughs':1921,'leopold':1948,'carson':1964,
          'haldane':1964,'poincare':1912,'simmel':1918,'russell':1970,'james':1910,
          'clifford':1879,'montaigne':1592,'benjamin':1940,'chesterton':1936,
          'orwell':1950,'lynd':1949,'stevenson':1894,'twain':1910,'zhou':1967,
          'feng':1975,'terada':1935,'nakaya':1962,'luxun':1936}
CATEGORY = {1:'自然与演化',2:'心智与判断',3:'信息与技术',4:'经济与社会',
            5:'心智与判断',6:'文学与思想',7:'文学与思想',8:'文学与思想'}

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def initialize():
    if BATCH.exists(): return
    chosen={x[0]:x for x in PLAN}; records=[]
    for c in json.loads(CANDIDATES.read_text(encoding='utf-8'))['items']:
        n=c['number']; title=c['title'].split(' · ')[-1].split(' / ')[0]
        zh=c['title'].split(' · ')[0]
        author=c['author_and_edition'].split('，')[0]
        r=dict(id=f'candidate-{n:02d}',candidate_number=n,title=title,zh_title=zh,author=author,
               category=CATEGORY[int(c['category'][0])],source=c['source_url'],visible=False,
               status='awaiting-user-provided-original-or-reproduction-permission',kind='pending')
        if n in chosen:
            _,ident,year,lang,url=chosen[n]
            r.update(id=ident,year=year,original_language=lang,source=url or r['source'],
                     folder=re.sub(r'[<>:"/\\|?*]','',title)+f' {year}',
                     status='source-acquisition-pending')
            death=DEATHS.get(ident.split('-')[0])
            r.update(author_death_year=death,rights_jurisdiction='mainland China',
                rights='Original literary work beyond the mainland-China life-plus-50 term as of 2026; no assertion of worldwide public-domain status. Only original author text and newly generated Chinese translation are included.',
                rights_term_reference='https://www.ncac.gov.cn/xxfb/flfg/flfg_532/202103/t20210309_50530.html')
            if n==7:
                r.update(rights='Public Domain explicitly declared by the US Fish & Wildlife Service for this article scan.',rights_jurisdiction='source-declared Public Domain',rights_evidence='https://www.fws.gov/media/help-your-child-wonder')
            if n==9:
                r.update(rights='Caltech expressly permits individual, educational, research and non-commercial reproduction, distribution, display and performance in any format.',rights_jurisdiction='source permission',rights_evidence='https://calteches.library.caltech.edu/1575/')
        records.append(r)
    dump(BATCH,records)

def fetch(r):
    folder=SOURCES/r['id'];folder.mkdir(parents=True,exist_ok=True)
    old=folder/'manifest.json'
    if old.exists():return dict(id=r['id'],cached=True)
    u=r['source'];response=requests.get(u,timeout=(10,35));response.raise_for_status()
    data=response.content;resolved=response.url
    if 'aozora.gr.jp/cards/' in u and '/files/' not in u:
        soup=BeautifulSoup(data,'html.parser')
        a=next(a for a in soup.select('a[href]') if '/files/' in a['href'] and a['href'].endswith('.html'))
        resolved=urljoin(u,a['href']);response=requests.get(resolved,timeout=35);response.raise_for_status();data=response.content
    ext='.pdf' if data.startswith(b'%PDF') else '.html'
    if u.endswith('.pdf'):assert ext=='.pdf','PDF URL returned non-PDF'
    target=folder/('original'+ext);target.write_bytes(data)
    dump(old,dict(id=r['id'],source_url=u,resolved_url=resolved,path=str(target.resolve()),
                  format=ext[1:],bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),si_requested=False))
    return dict(id=r['id'],bytes=len(data),format=ext[1:])

def acquire():
    initialize();records=json.loads(BATCH.read_text(encoding='utf-8'));results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        tasks={pool.submit(fetch,r):r for r in records if r.get('original_language')}
        for f in concurrent.futures.as_completed(tasks):
            r=tasks[f]
            try:result=f.result()
            except Exception as e:result=dict(id=r['id'],error=str(e)[:180]);r['status']='source-acquisition-failed'
            else:r['status']='source-downloaded-not-yet-extracted'
            results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
    dump(SOURCES/'download-results.json',results);dump(BATCH,records)

def clean(node):
    node=BeautifulSoup(str(node),'html.parser')
    for t in node.select('.pagenum,.pageno,.pb,rt,rp,script,style'):
        t.decompose()
    for i in node.select('img'):
        alt=i.get('alt','');i.replace_with(alt if len(alt)==1 else '')
    return re.sub(r'\s+',' ',node.get_text()).strip()

def between(soup, start, end=None, tags=('p',)):
    active=False;result=[]
    for t in soup.find_all(tags):
        text=clean(t)
        if not active and re.search(start,text):active=True
        if not active:continue
        if end and re.search(end,text):break
        if text:result.append(t)
    assert active,'Article start not found: '+start
    return result

def chapter(soup, title, level=None):
    heading=next(t for t in soup.find_all(['h1','h2','h3','h4','h5']) if re.search(title,clean(t),re.I))
    level=level or int(heading.name[1]);nodes=[]
    for t in heading.find_all_next(['h1','h2','h3','h4','h5','p','pre','img']):
        if t.name.startswith('h') and int(t.name[1])<=level:break
        if t.name=='img' and t.find_parent('p'):continue
        if t.name=='p' and t.find_parent('pre'):continue
        if t.get('id')=='pg-footer' or t.find_parent(id='pg-footer'):break
        nodes.append(t)
    # Include author notes referenced by the chapter, even when collected at book end.
    selected={id(t) for t in nodes}
    for t in list(nodes):
        for a in t.select('a[href^="#"]'):
            if not re.search(r'foot|note|fn',a.get('href',''),re.I):continue
            target=soup.find(id=a['href'][1:])
            if target:
                note=target if target.name=='p' else target.find_parent('p')
                if note and id(note) not in selected:
                    nodes.append(note);selected.add(id(note))
    return nodes

def prepare_one(r):
    ident=r['id'];reader=READERS/ident;reader.mkdir(parents=True,exist_ok=True)
    if (reader/'source_map.json').exists():return {'id':ident,'cached':True}
    manifest=json.loads((SOURCES/ident/'manifest.json').read_text(encoding='utf-8'))
    original=Path(manifest['path']);blocks=[]
    def add(text,kind='paragraph',**extra):
        text=re.sub(r'\s+',' ',text).strip()
        if text:blocks.append(dict(type=kind,en=text,**extra))
    if original.suffix=='.pdf':
        import pymupdf
        d=pymupdf.open(original)
        if ident=='russell-lived':
            page=next(p for p in d if 'Three passions' in p.get_text())
            text=page.get_text();text=text[text.index('Three passions'):]
            for b in page.get_text('blocks',sort=True):
                t=b[4]
                if not blocks:
                    if 'Three passions' not in t:continue
                    t=t[t.index('Three passions'):]
                t=re.sub(r'(?<=\w)-\s*\n\s*(?=\w)','',t);add(t,source_page=page.number+1)
            r['edition']='Complete five-paragraph prologue from the publisher facsimile of Autobiography, Volume 1 (1967).'
        elif ident=='zhou-tea':
            current='';started=False;stopped=False
            for page in list(d)[2:5]:
                for b in page.get_text('dict')['blocks']:
                    for line in b.get('lines',[]):
                        text=''.join(s['text'] for s in line['spans']).strip()
                        if not text or re.fullmatch(r'\d+',text) or text in ('喝茶','周作人','閒情樂事') or text.startswith('©'):continue
                        if not started:
                            if not text.startswith('前回徐志摩'):continue
                            started=True
                        if text.startswith('（選自'):stopped=True;break
                        if stopped:break
                        if line['bbox'][0]>85 and current:
                            add(current,source_page=page.number+1);current=''
                        current+=text
                    if stopped:break
                if stopped:break
            if current:add(current,source_page=5)
            assert started and stopped
            r['edition']='Complete 喝茶 including author dateline, pp. 3–5 in the City University of Hong Kong Press preview; page furniture and later edition note excluded.'
        elif ident=='leopold-oak':
            started=False;stopped=False;current='';last_y=None
            for page in d:
                lines=[line for b in page.get_text('dict')['blocks'] for line in b.get('lines',[])]
                lines.sort(key=lambda line:(int(line['bbox'][0]>=400),line['bbox'][1],line['bbox'][0]));last_y=None;last_column=None
                for line in lines:
                    text=''.join(s['text'] for s in line['spans']).strip();x,y=line['bbox'][:2]
                    if y>535:continue
                    column=int(x>=400);base_x=432 if column else 72
                    if column!=last_column:last_y=None;last_column=column
                    if not started:
                        if 'There are two spiritual dangers' not in text:continue
                        text=text[text.index('There are two spiritual dangers'):];started=True
                    if re.search(r'Thinking\s+Like\s+a\s+Mountain',text,re.I):
                        stopped=True;break
                    if not text or re.fullmatch(r'[\d\s*–—-]+',text):continue
                    if current and (x>=base_x+32 or (last_y is not None and y-last_y>23)):
                        add(current,source_page=page.number+1);current=''
                    current+=('' if not current or current.endswith('-') else ' ')+text;last_y=y
                if stopped:break
            if current:add(current,source_page=page.number+1)
            assert started and stopped
            r['edition']='Complete February—Good Oak chapter in the A Sand County Almanac teaching transcription, source PDF pp. 2–9; adjacent essays excluded.'
        elif ident!='haldane-life':raise ValueError('PDF needs explicit extraction/OCR before completion')
        for page_no,page in enumerate(d if ident=='haldane-life' else [],1):
            for bbox in page.get_text('blocks',sort=True):
                text=bbox[4].strip()
                if not text or re.fullmatch(r'\d+',text) or re.search(r'www\.|https?://',text):continue
                if page_no==1 and not blocks:
                    if 'UNTIL' not in text:continue
                    text=text[text.index('UNTIL'):]
                text=re.sub(r'(?<=\w)-\s*\n\s*(?=\w)','',text)
                text=re.sub(r'\s+',' ',text)
                if blocks and not re.search(r'[.!?][”\"\)]?$',blocks[-1]['en']):
                    blocks[-1]['en']+=' '+text
                else:add(text,source_page=page_no)
        if ident=='haldane-life':
            assert blocks[0]['en'].startswith('UNTIL')
            r['edition']='Complete 12-page reprint of the 1929 essay; title, author line and folios omitted.'
    else:
        soup=BeautifulSoup(original.read_bytes(),'html.parser');nodes=[]
        if ident=='wallace-varieties':
            nodes=between(soup,r'^\[\[p\. 53\]\]',r'^\*|^Editor');r['edition']='Complete 1858 essay including Ternate dateline; later editor commentary excluded.'
        elif ident=='muir-windstorm':nodes=chapter(soup,r'A WIND-STORM IN THE FORESTS')
        elif ident=='burroughs-seeing':nodes=between(soup,r'^I\s+DO not purpose')
        elif ident=='poincare-creation':
            nodes=chapter(soup,r'^Mathematical Creation$');r['edition']='Complete Science and Method, Book I, Chapter III; G. B. Halsted translation, The Foundations of Science (1913).'
        elif ident=='feynman-value':
            nodes=between(soup,r'^From time to time',tags=('p','h2','h3','pre'))
            r['edition']='Complete 1955 address, text transcription checked against the Caltech-authorized three-page original scan; all subheadings and the seashore passage retained.'
        elif ident in ('simmel-stranger','simmel-bridge','simmel-metropolis'):
            nodes=[p for p in soup.select('p.normalschrift') if not p.find('p') and not re.search(r'Prof\.|Hans Geser|Soziologisches Institut',clean(p))]
            assert len(nodes)>8,'German edition not acquired'
            r['edition']='Complete German author text; site navigation, bibliographic header and modern editorial material excluded.'
        elif ident=='benjamin-library':
            nodes=[p for p in soup.find_all('p') if not p.get('class')]
            assert clean(nodes[0]).startswith('Ich packe meine Bibliothek aus.')
            r['edition']='Complete German original, Ich packe meine Bibliothek aus. Eine Rede über das Sammeln (1931); not a modern English translation.'
        elif ident=='russell-lived':nodes=between(soup,r'^Three passions',r'^\*|^About|^Note:')
        elif ident=='russell-rubbish':nodes=between(soup,r'^Man is a rational animal',r'^Back|^Home|^\[Back')
        elif ident=='james-blindness':nodes=between(soup,r'^Our judgments',r'^Monadnock Valley Press')
        elif ident=='clifford-belief':nodes=chapter(soup,r'^III\. THE ETHICS OF BELIEF\.')
        elif ident=='montaigne-thumbs':nodes=chapter(soup,r'OF THUMBS')
        elif ident=='montaigne-smells':nodes=chapter(soup,r'OF SMELLS')
        elif ident=='chesterton-nonsense':nodes=chapter(soup,r'^A DEFENCE OF NONSENSE$')
        elif ident=='orwell-bookshop':nodes=between(soup,r'^When I worked',r'^1936|^November|^Notes|^____|^©')
        elif ident in ('orwell-sport','orwell-reviewer','orwell-books-cigarettes'):
            if ident=='orwell-books-cigarettes':nodes=chapter(soup,r'^BOOKS VS\. CIGARETTES$')
            else:
                section=soup.select_one('section.entry-content') or soup
                starts={'orwell-sport':r'^Now that the brief','orwell-reviewer':r'^In a cold but stuffy'}
                nodes=between(section,starts[ident],r'^Tribune|^Published|^©|^Copyright')
        elif ident.startswith('lynd-'):
            titles={'lynd-ignorance':r'^THE PLEASURES OF IGNORANCE$','lynd-weeds':r'^WEEDS: AN APPRECIATION$','lynd-insects':r'^THE HUM OF INSECTS$'}
            nodes=chapter(soup,titles[ident])
        elif ident=='stevenson-love':
            h=next(p for p in soup.find_all('p') if clean(p)=='ON FALLING IN LOVE')
            for p in h.find_all_next(['p','pre','h2','h3','h4']):
                if re.search(r'^IV$|^TRUTH OF INTERCOURSE',clean(p)):break
                if p.name.startswith('h'):break
                nodes.append(p)
        elif ident=='twain-cornpone':nodes=chapter(soup,r'^CORN-PONE OPINIONS')
        elif ident=='twain-telephone':nodes=chapter(soup,r'^A TELEPHONIC CONVERSATION$')
        elif ident=='zhou-vegetables':
            for p in between(soup,r'^我的故乡不止一个'):
                nodes.append(p)
                if clean(p)=='十三年二月':break
            assert clean(nodes[-1])=='十三年二月'
        elif ident=='feng-children':
            for p in between(soup,r'^我的孩子们！我憧憬'):
                nodes.append(p)
                if '我的画在世间已无可印证了' in clean(p):break
            assert '我的画在世间已无可印证了' in clean(nodes[-1])
        elif ident=='feng-gradual':
            for p in between(soup,r'^使人生圆滑进行'):
                text=clean(p)
                if re.search(r'^【.*赏析|^【.*賞析|^赏析|^一九|^——',text):break
                nodes.append(p)
                if '一刹那便是永劫' in text:break
            assert '一刹那便是永劫' in clean(nodes[-1])
            r['edition']='Complete 渐 as collected in 缘缘堂随笔 (1931); later criticism and teaching commentary excluded. Collection year retained; first-publication year not asserted.'
        elif ident=='luxun-pagoda':nodes=soup.select('article p')
        elif ident.startswith(('terada-','nakaya-')):
            content=soup.select_one('.main_text');assert content
            for image in content.select('img.gaiji'):
                if '1-87-29' in image.get('src',''):image.replace_with('瀆')
                else:raise ValueError('Unknown gaiji: '+image.get('alt',''))
            for t in content.select('rt,rp'):t.decompose()
            text=content.get_text('\n',strip=False)
            # Ruby has been removed; retain the printed paragraph breaks (br), not tag boundaries.
            for br in content.select('br'):br.replace_with('\n')
            text=content.get_text()
            if ident=='terada-sugar':
                # Complete titled entry inside 備忘録, not a replacement by the whole collection.
                lines=text.splitlines();begin=next(i for i,s in enumerate(lines) if s.strip()=='金米糖')+1
                stop=next(i for i,s in enumerate(lines[begin:],begin) if s.strip()=='風呂の流し')
                text='\n'.join(lines[begin:stop]);r['year']=1927;r['folder']='金米糖 1927'
                r['edition']='Complete titled 金米糖 entry of 備忘録, 思想, September 1927. Other entries in the collection excluded; not the separate 1920 romanized KONPEITOO version.'
            for line in text.splitlines():
                if line.strip():add(line)
            # Aozora figure images are author illustrations, kept separately below.
            for image in content.select('img[src]'):
                url=urljoin(manifest['resolved_url'],image['src']);response=requests.get(url,timeout=20);response.raise_for_status()
                asset='assets/F001'+Path(image['src']).suffix;(reader/'assets').mkdir(exist_ok=True);(reader/asset).write_bytes(response.content)
                add(image.get('alt','Figure'),'figure',asset=asset,source_image_url=url)
        else:raise ValueError('Source boundary still requires verification')
        used_captions=set()
        for node in nodes:
            if id(node) in used_captions:continue
            if node.name=='img':
                url=urljoin(manifest['resolved_url'],node['src']);response=requests.get(url,timeout=20);response.raise_for_status()
                num=sum(b['type']=='figure' for b in blocks)+1;asset=f'assets/F{num:03d}'+Path(node['src']).suffix
                (reader/'assets').mkdir(exist_ok=True);(reader/asset).write_bytes(response.content)
                container=node.find_parent('div',class_=re.compile('fig')) or node.parent
                captions=container.select('p.caption') if container else []
                caption=' '.join(clean(c) for c in captions) or node.get('alt','')
                used_captions.update(id(c) for c in captions)
                add(caption or f'Figure {num}','figure',asset=asset,source_image_url=url)
                continue
            if node.find('img') and not all(len(i.get('alt',''))==1 for i in node.find_all('img')):
                if ident!='feng-children':raise ValueError('Source illustration needs extraction inside paragraph')
            text=clean(node)
            if node.name=='pre' and ident=='orwell-books-cigarettes':
                raw=node.get_text().strip();rows=[re.split(r'\s{2,}',s.strip()) for s in raw.splitlines() if s.strip()]
                rows=[re.split(r'\s+(?=\d+$)',row[0]) if len(row)==1 and re.search(r'\s\d+$',row[0]) else row for row in rows]
                cols=max(len(row) for row in rows)
                if len(rows[0])<cols:rows[0]=['']*(cols-len(rows[0]))+rows[0]
                assert all(len(row)==cols for row in rows)
                translations={'Bought (mostly second-hand)':'购入（多为旧书）','Given to me or bought with book tokens':'获赠或用购书券购入',
                    'Review copies and complimentary copies':'书评样书及赠阅本','Borrowed and not returned':'借来未还','Temporarily on loan':'暂借',
                    'Total':'合计','Bought':'购入','Gifts':'获赠','Review copies, etc':'书评样书等','On loan':'暂借','Shelves':'书架'}
                zh_rows=[[translations.get(cell,cell) for cell in row] for row in rows]
                blocks.append(dict(type='table',en=raw,zh='\n'.join(' | '.join(row) for row in zh_rows),rows=rows,zh_rows=zh_rows));continue
            if ident=='wallace-varieties':text=re.sub(r'\[\[p\. \d+\]\]','',text)
            if ident=='burroughs-seeing':text=re.sub(r'^I\s+DO\b','I do',text)
            add(text,'heading' if node.name.startswith('h') else 'paragraph',source_anchor=node.get('id'))
    assert blocks and sum(len(b['en']) for b in blocks)>500,'Body too small or absent'
    for i,b in enumerate(blocks,1):b.update(id=f'S{i:03d}',order=i-1)
    data=dict(paper=r,scope='complete-essay',original_language=r['original_language'],source_format=manifest['format'],
              source_sha256=manifest['sha256'],source_url=manifest['resolved_url'],blocks=blocks,glossary={},
              coverage={'blocks':len(blocks),'source_characters':sum(len(b['en']) for b in blocks),
                        'source_beginning':blocks[0]['en'][:150],'source_ending':blocks[-1]['en'][-200:]},
              omitted_non_content=['Source website navigation, catalogues, later editorial commentary, folios and publisher boilerplate.'],
              extraction_status='complete source boundaries identified; limited spot review')
    dump(reader/'source_map.json',data);r['status']='source-extracted-awaiting-translation'
    return dict(id=ident,**data['coverage'])

def prepare():
    records=json.loads(BATCH.read_text(encoding='utf-8'));result=[]
    for r in records:
        if not (SOURCES/r['id']/'manifest.json').exists():continue
        try:res=prepare_one(r)
        except Exception as e:
            res=dict(id=r['id'],error=str(e));r['status']='source-boundary-or-asset-work-pending'
        result.append(res);print(json.dumps({k:v for k,v in res.items() if k not in ('source_beginning','source_ending')},ensure_ascii=True),flush=True)
    dump(BATCH,records);dump(SOURCES/'extraction-results.json',result)

def translate():
    provider='alibaba' if '--provider=alibaba' in sys.argv else 'google'
    if provider=='alibaba':
        import os
        os.environ['translators_default_region']='CN'
        import translators as translation_client
    records=json.loads(BATCH.read_text(encoding='utf-8'))
    cache_path=ROOT/'expansion-translation-cache-2026-10-21.json'
    cache=json.loads(cache_path.read_text(encoding='utf-8')) if cache_path.exists() else {}
    manual_path=ROOT/'manual-translation-overrides-2026-10-21.json'
    manual=json.loads(manual_path.read_text(encoding='utf-8')) if manual_path.exists() else {}
    cache.update(manual)
    sources={};jobs={};targets=[]
    for r in records:
        p=READERS/r['id']/'source_map.json'
        if not p.exists():continue
        data=json.loads(p.read_text(encoding='utf-8'));sources[r['id']]=(p,data)
        lang=r['original_language']
        for b in data['blocks']:
            if b.get('zh'):continue
            if b['type']=='figure' and not b['en']:b['zh']='';continue
            if lang=='zh':b['zh']=b['en'];continue
            parts=[];rest=b['en'];limit=250 if provider=='alibaba' and lang in ('ja','de') else 800 if lang=='ja' else 1600
            while len(rest)>limit:
                cut=max(rest.rfind('. ',limit//2,limit),rest.rfind('。',limit//2,limit),rest.rfind(' ',limit//2,limit))
                cut=cut+1 if cut>=0 else limit;parts.append(rest[:cut]);rest=rest[cut:]
            if rest:parts.append(rest)
            assert ''.join(parts)==b['en']
            keys=[]
            for text in parts:
                key=hashlib.sha256((lang+'\0'+text).encode()).hexdigest()[:16].upper()
                keys.append(key);jobs[key]=(lang,text)
            targets.append((b,keys))
    grouped={}
    for key,(lang,text) in jobs.items():
        if key not in cache:grouped.setdefault(lang,[]).append((key,text))
    batches=[]
    for lang,items in grouped.items():
        current=[];length=0;limit=280 if provider=='alibaba' and lang in ('ja','de') else 1000 if lang=='ja' else 2500 if provider=='alibaba' else 3200
        for item in items:
            if current and length+len(item[1])+32>limit:
                batches.append((lang,current));current=[];length=0
            current.append(item);length+=len(item[1])+32
        if current:batches.append((lang,current))
    def request(lang,text):
        if provider=='alibaba':
            data=translation_client.translate_text(text,translator='alibaba',from_language=lang,to_language='zh',
                timeout=20,sleep_seconds=0.7,is_detail_result=True)
            result=(data.get('data') or {}).get('translateText')
            if not result:raise RuntimeError('Alibaba response: '+str({k:data.get(k) for k in ('code','message','msg')})+'; language='+lang+'; characters='+str(len(text)))
            return result
        for attempt in range(3):
            try:
                response=requests.get('https://translate.googleapis.com/translate_a/single',params={
                    'client':'gtx','sl':lang,'tl':'zh-CN','dt':'t','q':text},timeout=40)
                if response.status_code==429:raise RuntimeError('Translation service rate limit; stop and retain cache')
                response.raise_for_status()
                result=''.join(x[0] for x in response.json()[0] if x[0]);assert result.strip()
                return result
            except Exception:
                if attempt==2 or ('response' in locals() and response.status_code==429):raise
                time.sleep(attempt+1)
    def work(batch):
        lang,items=batch;text='\n'.join('[[TX'+k+']]\n'+t for k,t in items)
        result=request(lang,text).replace('［','[').replace('］',']')
        matches=list(re.finditer(r'\[\[\s*TX\s*([A-F0-9]{16})\s*\]\]',result,re.I))
        if [m[1].upper() for m in matches]==[k for k,_ in items]:
            output={m[1].upper():result[m.end():matches[i+1].start() if i+1<len(matches) else len(result)].strip() for i,m in enumerate(matches)}
            if all(output.values()):return output
        return {k:request(lang,t).strip() for k,t in items}
    print(f'Translating {len(sources)} complete source readers: {len(batches)} remaining batches',flush=True)
    pool=concurrent.futures.ThreadPoolExecutor(max_workers=1 if provider=='alibaba' else 3)
    deferred=[]
    try:
        futures=[pool.submit(work,b) for b in batches]
        for i,f in enumerate(concurrent.futures.as_completed(futures),1):
            try:cache.update(f.result())
            except Exception as e:
                if 'CsiError' in str(e):
                    lang,items=batches[futures.index(f)]
                    deferred.extend(dict(key=k,source_language=lang,text=t,reason='Provider declined this batch; requires direct translation') for k,t in items)
                    print(f'Deferred one {lang} batch for direct translation',flush=True);continue
                dump(cache_path,cache);dump(SOURCES/'deferred-translations.json',deferred);pool.shutdown(wait=False,cancel_futures=True)
                raise RuntimeError('Translation failed; completed batches cached: '+str(e)) from e
            if i%10==0 or i==len(batches):
                dump(cache_path,cache);print(f'Translation batches {i}/{len(batches)}',flush=True)
    finally:
        pool.shutdown(wait=False,cancel_futures=True)
    dump(cache_path,cache);dump(SOURCES/'deferred-translations.json',deferred)
    for b,keys in targets:
        if not all(k in cache for k in keys):continue
        b['zh']=''.join(cache[k] for k in keys)
        b['translation_method']='assistant translation' if all(k in manual for k in keys) else 'machine draft with validated paragraph alignment'
    for ident,(p,data) in sources.items():
        if all(b.get('zh','').strip() or (b['type']=='figure' and not b['en']) for b in data['blocks']):
            data['translation_status']='complete paragraph coverage; machine draft, limited spot review'
        else:data.pop('translation_status',None)
        dump(p,data)
    print(f'Aligned translations saved; {len(deferred)} segments require direct translation',flush=True)

def render():
    records=json.loads(BATCH.read_text(encoding='utf-8'));completed=[]
    for r in records:
        folder=READERS/r['id'];p=folder/'source_map.json'
        if not p.exists():continue
        data=json.loads(p.read_text(encoding='utf-8'))
        if not data.get('translation_status'):continue
        r.update({k:v for k,v in data['paper'].items() if k not in ('category','source')});r.update(visible=True,kind='full',scope=data.get('scope','complete-essay'),
                   status='bilingual-complete-draft' if r['original_language']!='zh' else 'complete-original',
                   translation_status=data['translation_status'],source_acquisition='assistant-retrieved-original',
                   completeness='all source body blocks retained; source boundaries and paragraph coverage checked')
        r.pop('pending_reason',None)
        q=lambda x:json.dumps(x,ensure_ascii=False)
        public=ROOT.parent/'Essay'/r['folder'];public.mkdir(exist_ok=True)
        title=r['title'] if r['title']==r['zh_title'] else r['title']+' / '+r['zh_title']
        typ=['#import "../index.typ": template, tufted','#import "../../_essay/bilingual.typ": zh, zh-caption',
             '#show: template.with(',f'  title: {q(r["title"])},',f'  author: {q(r["author"])}, date: {q(str(r["year"]))}, lang: {q(r["original_language"])},',
             '  css: ("/assets/custom.css", "/assets/essay.css"),',')','',f'= #text({q(title)})','']
        md=['# '+title,'','Author: '+r['author'],'Source: '+r['source'],
            'Edition: '+r.get('edition','Complete standalone essay or complete titled entry in its source collection.'),
            'Translation: complete paragraph coverage; machine draft with limited spot review.','']
        for b in data['blocks']:
            assert (b['en'].strip() and b['zh'].strip()) or (b['type']=='figure' and not b['en'])
            if b['type']=='figure':
                import shutil
                (public/'assets').mkdir(exist_ok=True);shutil.copy2(folder/b['asset'],public/b['asset'])
                caption=f', caption: [#text({q(b["en"])}) #zh-caption[#text({q(b["zh"])})]]' if b['en'] else ''
                typ += [f'#figure(image({q(b["asset"])}, width: 85%){caption})','']
                md += [f'![{b["en"]}]({b["asset"]})','']
            elif b['type']=='table':
                cols=len(b['rows'][0])
                def tab(rows):return '#table(columns: '+str(cols)+', align: left, inset: 6pt, '+', '.join('[#text('+q(cell)+')]' for row in rows for cell in row)+')'
                typ += [tab(b['rows']),'','#zh(id: "'+b['id']+'")[\n'+tab(b['zh_rows'])+'\n]','']
                md += ['| '+' | '.join(row)+' |' for row in b['rows']]
            elif b['type']=='heading':typ+=['== #text('+q(b['en'] if r['original_language']=='zh' else b['en']+' / '+b['zh'])+')','']
            else:
                typ += [f'#html.p(id: "en-{b["id"]}")[#text({q(b["en"])})]','']
                if r['original_language']!='zh':typ += [f'#zh(id: "{b["id"]}")[#text({q(b["zh"])})]','']
            md += [f'<a id="{b["id"]}"></a>','**Source:** '+(str(b.get('source_page')) if b.get('source_page') else str(b.get('source_anchor') or data['source_url'])),
                   '','**Original:** '+b['en'].replace('$',r'\$'),'','**中文:** '+b['zh'].replace('$',r'\$'),'']
        (public/'index.typ').write_text('\n'.join(typ).rstrip()+'\n',encoding='utf-8')
        (folder/'paper.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
        (folder/'translation_notes.md').write_text('Complete author text with aligned Chinese draft; no summary substitution.\nSource metadata, edition and omissions are in source_map.json.\nMachine translation with limited spot review; not a sentence-by-sentence polished translation.\nNative Chinese essays retain the original once, without artificial duplication.\n',encoding='utf-8')
        data['paper']=r;dump(p,data)
        dump(ROOT/(r['id']+'-source-map.json'),data)
        completed.append(r)
    index=ROOT.parent/'Essay/index.typ';text=index.read_text(encoding='utf-8')
    for r in completed:
        if f'path: "{r["folder"]}/"' in text:continue
        heading=re.search(r'(?m)^== [^\n]* / '+re.escape(r['category'])+r'\s*\n',text);assert heading
        next_heading=re.search(r'(?m)^== ',text[heading.end():]);end=heading.end()+next_heading.start() if next_heading else len(text)
        entries=list(re.finditer(r'#tufted\.blog-entry\([\s\S]*?\n\)',text[heading.end():end]))
        before=next((heading.end()+e.start() for e in entries if int(re.search(r'date: "(\d+)"',e[0])[1])>r['year']),end)
        label=r['title'] if r['title']==r['zh_title'] else r['title']+' / '+r['zh_title']
        entry=f'#tufted.blog-entry(\n  date: {q(str(r["year"]))},\n  path: {q(r["folder"]+"/")},\n  title: {q(label)},\n)\n\n'
        text=text[:before]+entry+text[before:]
    index.write_text(text,encoding='utf-8')
    catalog=ROOT/'classics-catalog.json';items=json.loads(catalog.read_text(encoding='utf-8'))
    updates={r['id']:r for r in completed};items=[dict(r,**updates.pop(r['id'])) if r['id'] in updates else r for r in items];items.extend(updates.values())
    dump(catalog,items);dump(BATCH,records)
    for r in records:
        if r['id']=='russell-rubbish' and not r['visible'] and r.get('source_availability')!='body-source-acquired':
            r['status']='awaiting-complete-readable-source'
            r['pending_reason']='常见网页只有节选；馆藏扫描本尚未取得完整可读正文。'
    dump(BATCH,records)
    candidates=json.loads(CANDIDATES.read_text(encoding='utf-8'))
    by_number={r['candidate_number']:r for r in records}
    for c in candidates['items']:
        r=by_number[c['number']]
        c.update(visible=r['visible'],status=r['status'],essay_id=r['id'])
    candidates['scope']='Discovery catalogue with current completion status; only complete readers are published.'
    dump(CANDIDATES,candidates)
    pending=[r for r in records if not r['visible']]
    status=['# Essay 收录状态 · 2026-10-21','',f'本批候选75篇；完整收录{len(completed)}篇，待补{len(pending)}篇。目录只列已完成正文的文章。','',
            '新增外文正文逐段配中文初译；中文原作保留原文一次。没有用节选、书目或摘要充当全文。','',
            '| 编号 | 文章 | 状态 |','| --- | --- | --- |']
    for r in records:
        label='已保存完整正文和逐段中文初译' if r['visible'] else r.get('pending_reason','待提供完整原文或可用的转载授权')
        status.append(f'| {r["candidate_number"]:02d} | {r["zh_title"]} / {r["title"]} | {label} |')
    (ROOT/'essay-status-2026-10-21.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
    dump(ROOT/'essay-completeness-2026-10-21.json',dict(requested=75,completed=len(completed),pending=len(pending),
         visible_local_entries=text.count('#tufted.blog-entry('),coverage=[dict(id=r['id'],**json.loads((READERS/r['id']/'source_map.json').read_text(encoding='utf-8'))['coverage']) for r in completed]))
    print(f'Rendered {len(completed)} completed essays; {len(pending)} pending; {text.count("#tufted.blog-entry(")} visible entries',flush=True)

if __name__=='__main__':
    if sys.argv[1]=='acquire':acquire()
    elif sys.argv[1]=='prepare':prepare()
    elif sys.argv[1]=='translate':translate()
    elif sys.argv[1]=='render':render()
