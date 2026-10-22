"""Prepare complete author text from the newly recovered Russell/Langmuir sources."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urljoin

import pymupdf
import requests
from bs4 import BeautifulSoup, NavigableString
from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parent
RAW = ROOT / 'originals-2026-10-22'
READERS = ROOT / 'readers'
BATCH = ROOT / 'essay-additions-2026-10-21.json'


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def normalize(text):
    return re.sub('[^a-z]', '', text.lower())


def clean(node):
    copy = BeautifulSoup(str(node), 'lxml')
    for tag in copy.select('script,style,img'):
        tag.decompose()
    for tag in copy.select('font[color]'):
        if tag.get('color', '').lower() in ('#008000', 'green'):
            tag.decompose()
    for tag in copy.select('sup,sub'):
        table = str.maketrans('0123456789+-=()', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾' if tag.name == 'sup' else '₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎')
        tag.replace_with(tag.get_text().translate(table))
    return re.sub(r'\s+', ' ', copy.get_text()).strip()


records = json.loads(BATCH.read_text(encoding='utf-8'))
for r in records:
    number = r['candidate_number']
    if number not in (15, 37):
        continue
    if number == 37:
        ident = 'russell-rubbish'
        r.update(source='https://dai.mun.ca/PDFs/radical/548943.pdf', year=1943,
                 original_language='en', folder='An Outline of Intellectual Rubbish 1943',
                 secondary='https://www.russell-j.com/0811OIR.HTM',
                 edition='Complete 1943 essay: author text on PDF pages 7–28 of the Memorial University scan; English transcription checked against all 22 author-text pages. Covers, advertisements and modern website furniture excluded.')
        original = RAW / 'russell-mun.pdf'
        html = (RAW / 'russell-j.html').read_bytes().decode('utf-8')
        start = html.index('Man is a rational animal')
        ending = 'in our own age as in every other.'
        stop = html.index(ending, start) + len(ending)
        fragment = BeautifulSoup(html[start:stop], 'lxml')
        for tag in fragment.select('br'):
            tag.replace_with('\n')
        paragraphs = [re.sub(r'\s+', ' ', p).strip() for p in re.split(r'\n\s*\n', fragment.get_text())]
        paragraphs = [p for p in paragraphs if p]
        assert paragraphs[0].startswith('Man is a rational animal') and paragraphs[-1].endswith(ending)
        doc = pymupdf.open(original)
        pages = [(i + 1, normalize(doc[i].get_text())) for i in range(6, 28)]
        text = ' '.join(paragraphs)
        similarity = fuzz.ratio(normalize(text), ''.join(t for _, t in pages))
        assert similarity > 98, 'Transcription and original edition differ materially'
        blocks = []
        for paragraph in paragraphs:
            anchor = normalize(paragraph)[:190]
            page, score = max(((p, fuzz.partial_ratio(anchor, t)) for p, t in pages), key=lambda x: x[1])
            blocks.append(dict(type='paragraph', en=paragraph, source_page=page,
                               source_anchor_match=round(score, 2)))
        extra = dict(source_scan_pages=list(range(7, 29)),
                     transcription_url=r['secondary'],
                     transcription_sha256=hashlib.sha256((RAW / 'russell-j.html').read_bytes()).hexdigest(),
                     normalized_transcription_scan_similarity=round(similarity, 3),
                     comparison_note='Whole-text similarity measures transcription agreement with the noisy scan text layer; it is not a translation-quality score or a line-by-line proofread.')
        glossary = {'intellectual rubbish': '智识垃圾', 'rationality': '理性', 'superstition': '迷信'}
    else:
        ident = 'langmuir-pathological'
        r.update(id=ident, source='https://www.cs.princeton.edu/~ken/Langmuir/langmuir.htm',
                 year=1953, original_language='en', folder='Pathological Science 1953',
                 category='数学与物理', author_death_year=1957,
                 rights_jurisdiction='mainland China',
                 rights='Original 1953 Langmuir speech, author died 1957; beyond the mainland-China life-plus-50 term. No worldwide public-domain assertion. Modern introductions, Hall epilogue and modern editorial comments excluded.',
                 rights_term_reference='https://www.ncac.gov.cn/xxfb/flfg/flfg_532/202103/t20210309_50530.html',
                 edition='Complete author speech and question period, as transcribed in GE report 68-C-035 (1968) and restored by Princeton (2002). Includes the three report figures and six numbered symptoms. Excludes R. N. Hall’s preface/epilogue, later webmaster introduction, added bibliography and page markers.')
        original = RAW / 'candidate-15/source-01.html'
        folder = READERS / ident
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'assets').mkdir(exist_ok=True)
        opening = ('This is recorded by Irving Langmuir on March 8, 1954. It is transcribed from a tape recording, '
                   'section number three, of the lecture on "Pathological Science" that I gave on December 18, 1953.')
        blocks = [dict(type='paragraph', en=opening, source_part='introductory-recording-note')]
        image_count = 0
        source_parts = []
        for part, letter in enumerate('ABC', 2):
            path = RAW / 'candidate-15' / f'source-0{part}.html'
            url = urljoin(r['source'], f'lang{letter}.htm')
            source_parts.append(dict(url=url, sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
            soup = BeautifulSoup(path.read_bytes(), 'lxml')
            for node in list(soup.body.children):
                if isinstance(node, NavigableString):
                    value = re.sub(r'\s+', ' ', str(node)).strip()
                    if value:
                        blocks.append(dict(type='paragraph', en=value, source_part=letter))
                    continue
                if node.name in ('script', 'style', 'a', 'hr', 'br'):
                    continue
                if node.name in ('h4', 'h5'):
                    title = clean(node)
                    if title.startswith('EPILOGUE'):
                        break
                    blocks.append(dict(type='heading', en=title, source_part=letter))
                elif node.name == 'ol':
                    for i, item in enumerate(node.select(':scope > li'), 1):
                        blocks.append(dict(type='paragraph', en=f'{i}. {clean(item)}', source_part=letter))
                elif node.name == 'p':
                    # In this source figures occur inside paragraphs, at paragraph ends.
                    value = clean(node)
                    if value:
                        blocks.append(dict(type='paragraph', en=value, source_part=letter))
                    for img in node.select('img[src]'):
                        image_count += 1
                        image_url = urljoin(url, img['src'])
                        asset = f'assets/F{image_count:03d}.png'
                        target = folder / asset
                        if not target.exists():
                            response = requests.get(image_url, timeout=25)
                            response.raise_for_status()
                            assert response.content.startswith(b'\x89PNG'), 'Not an original PNG diagram'
                            target.write_bytes(response.content)
                        blocks.append(dict(type='figure', en='', zh='', asset=asset,
                                           source_part=letter, source_image_url=image_url))
                else:
                    value = clean(node)
                    if value:
                        blocks.append(dict(type='paragraph', en=value, source_part=letter))
        assert image_count == 3
        assert any(b['en'].startswith('Question Period') for b in blocks)
        assert not any('Pathological science is by no means a thing of the past' in b['en'] for b in blocks)
        # HTML has a loose paragraph containing two underlined inline phrases.
        # Keep the whole paragraph together rather than treating each phrase as a block.
        first = next(i for i, b in enumerate(blocks)
                     if b['en'] == 'The maximum effect that is observed is produced by a causative agent of barely detectable intensity')
        last = first + 1
        while last < len(blocks) and blocks[last].get('type') == 'paragraph' and (
                blocks[last]['en'].startswith('.') or blocks[last]['en'] == 'the effect is independent of the intensity of the cause'):
            last += 1
        merged = ' '.join(b['en'] for b in blocks[first:last]).replace(' .', '.')
        blocks[first:last] = [dict(type='paragraph', en=merged, source_part='B')]
        extra = dict(source_parts=source_parts, source_figures=image_count,
                     bibliography_note='Numbered scholarly citation markers in the restored transcript are retained. The later editor’s reference notes are not part of Langmuir’s spoken author text.')
        glossary = {'pathological science': '病态科学', 'Davis-Barnes effect': '戴维斯–巴恩斯效应',
                    'N-rays': 'N射线', 'mitogenetic rays': '有丝分裂辐射',
                    'Allison effect': '阿利森效应', 'extrasensory perception': '超感官知觉'}
    r.update(status='source-extracted-awaiting-translation', kind='pending', visible=False)
    reader = READERS / ident
    if (reader / 'source_map.json').exists():
        print(f'{ident}: already prepared; preserved existing translations')
        continue
    for i, b in enumerate(blocks, 1):
        b.update(id=f'S{i:03d}', order=i - 1)
    coverage = dict(blocks=len(blocks), source_characters=sum(len(b['en']) for b in blocks),
                    source_beginning=blocks[0]['en'][:150], source_ending=blocks[-1]['en'][-250:])
    data = dict(paper=r.copy(), scope='complete-author-essay' if number == 37 else 'complete-author-talk',
                original_language='en', source_format='html-collated-with-original-report',
                source_url=r['source'], source_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),
                blocks=blocks, coverage=coverage, glossary=glossary,
                extraction_status='Author-text boundaries identified; limited source review', **extra)
    dump(reader / 'source_map.json', data)
    print(f'{ident}: {len(blocks)} blocks, {coverage["source_characters"]} source characters')
dump(BATCH, records)
