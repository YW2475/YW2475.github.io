"""Complete originals whose protection term has expired for mainland-China study."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
essay_dir = root.parent / 'Essay'
q = lambda value: json.dumps(value, ensure_ascii=False)
batch_path = root / 'essay-additions-2026-10-12.json'
batch = json.loads(batch_path.read_text(encoding='utf-8'))
ids = ['leopold-mountain', 'woolf-moth', 'tanizaki-shadows', 'russell-idleness', 'flexner-useless', 'thurber-bed']
death_years = {'leopold-mountain': 1948, 'woolf-moth': 1941, 'tanizaki-shadows': 1965, 'russell-idleness': 1970, 'flexner-useless': 1959, 'thurber-bed': 1961}
term_source = 'https://www.ncac.gov.cn/xxfb/flfg/flfg_532/202103/t20210309_50530.html'

source_updates = {
    'leopold-mountain': ('https://blogs.ubc.ca/lled4492016/files/2016/04/Thinking-Like-a-Mountain_Aldo-Leopold.pdf', 'UBC teaching transcription of the eight original paragraphs; modern title, navigation, photographs and printed browser headers excluded.'),
    'woolf-moth': ('https://gutenberg.net.au/ebooks12/1203811h.html#ch-02', 'Only the first essay, five paragraphs; Leonard Woolf’s editorial note and other essays excluded.'),
    'tanizaki-shadows': ('https://www.aozora.gr.jp/cards/001383/files/56642_59575.html', 'Aozora Japanese original, 16 sections/paragraphs; ruby readings, section ornaments and modern bibliographical colophon excluded. Original Japanese retained; Chinese newly translated, not copied from a modern English or Chinese edition.'),
    'russell-idleness': ('https://humanum.arts.cuhk.edu.hk/humftp/E-text/Russell/praise.htm', 'CUHK English transcription: 28 paragraphs and Russell’s original note; site navigation excluded.'),
    'flexner-useless': ('https://www.ias.edu/ideas/usefulness-useless-knowledge', 'IAS transcription checked against the linked 1939 scan; known joined-word transcription errors corrected and recorded separately.'),
    'thurber-bed': ('https://www.newyorker.com/magazine/1933/07/08/my-life-and-hard-times-i-the-night-the-bed-fell', 'Original New Yorker text; digital timestamp is July 1, print issue July 8, 1933. Library of America PDF consulted as an original-source copy; modern cover and promotional material excluded.'),
}

overrides = json.loads((root / 'tanizaki-shadows-translation-overrides.json').read_text(encoding='utf-8'))
en_overrides = json.loads((root / 'public-domain-translation-overrides-2026-10-12.json').read_text(encoding='utf-8'))
ja_fixes = {'手机': '电话', '娃娃': '人偶', '傀儡师': '操偶师', '蜘蛛瘿': '蛛丝', '我国的大教堂': '我国的佛寺', '日本的大教堂': '日本的佛寺', '朝日堂': '朝日会馆', '安灯': '行灯', 'Waranji-ya': '草鞋屋', 'Musoan Mubayashi': '武林无想庵'}

for paper in batch:
    if paper['id'] not in ids:
        continue
    stem = paper['id']
    blocks = json.loads((root / f'{stem}-original-blocks.json').read_text(encoding='utf-8'))
    translations = json.loads((root / f'{stem}-translations.json').read_text(encoding='utf-8'))
    lang = 'ja' if stem == 'tanizaki-shadows' else 'en'
    for block in blocks:
        zh = translations[block['id']]
        if lang == 'ja':
            for old, new in ja_fixes.items():
                zh = zh.replace(old, new)
            zh = overrides.get(block['id'], zh)
        else:
            zh = en_overrides.get(stem, {}).get(block['id'], zh)
        block['zh'] = zh
        if not zh.strip() or not block[lang].strip():
            raise ValueError(f'Empty text in {stem}: {block["id"]}')
    paper.update({
        'kind': 'full', 'status': 'bilingual-full', 'original_language': lang,
        'source': source_updates[stem][0], 'edition': source_updates[stem][1],
        'author_death_year': death_years[stem],
        'rights': 'Original literary text is out of economic copyright under the mainland-China life-plus-50-year term, for the user’s explicitly local study context. This is not a claim of worldwide public-domain status. Modern editor content and modern translations excluded.',
        'rights_jurisdiction': 'mainland China', 'rights_term_reference': term_source,
        'distribution': 'local-study-only; not published or pushed',
        'translation_status': 'assistant-translated' if stem in ('woolf-moth', 'leopold-mountain') else 'machine-draft-with-selected-manual-retranslation',
    })
    if stem == 'tanizaki-shadows':
        paper['secondary'] = 'https://www.aozora.gr.jp/cards/001383/card56642.html'
        paper['citation'] = '陰翳礼讃, 経済往来, December 1933 and January 1934; Aozora Japanese text, card 56642.'
    paper.pop('source_scope', None)
    lines = [
        '#import "../index.typ": template, tufted',
        '#import "../../_essay/bilingual.typ": zh',
        '#show: template.with(',
        f'  title: {q(paper["title"])},', f'  author: {q(paper["author"])},',
        f'  date: {q(str(paper["year"]))},', f'  lang: {q(lang)},',
        '  css: ("/assets/custom.css", "/assets/essay.css"),', ')', '',
        f'= {paper["title"]} / {paper["zh_title"]}', '',
    ]
    for block in blocks:
        lines += [
            f'#html.p(id: {q(lang + "-" + block["id"])})[#text({q(block[lang])})]', '',
            f'#zh(id: {q(block["id"])})[#text({q(block["zh"])})]', '',
        ]
    folder = essay_dir / paper['folder']
    folder.mkdir(exist_ok=True)
    (folder / 'index.typ').write_text('\n'.join(lines), encoding='utf-8')
    source_map = {'paper': paper, 'scope': 'full', 'original_language': lang, 'blocks': blocks, 'translation_status': paper['translation_status']}
    (root / f'{stem}-source-map.json').write_text(json.dumps(source_map, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(stem, len(blocks), 'aligned paragraphs')

# Register source availability separately from permission to produce a full reader.
source_paths = {
    'dillard-weasels': 'dillard-weasels', 'borges-wilkins': 'borges-wilkins',
    'sacks-colorblind': 'sacks-colorblind', 'boulding-spaceship': 'boulding-spaceship',
}
for paper in batch:
    if paper['id'] in source_paths:
        pdfs = list((root / 'originals-2026-10-12' / source_paths[paper['id']] / 'PDFs').glob('*.pdf'))
        if pdfs:
            paper['local_source'] = str(pdfs[0].resolve())
            paper['source_acquisition'] = 'assistant-downloaded-for-local-reading'
            paper['status'] = 'local-pdf-available-reader-pending'
            paper['rights'] = 'Publicly downloadable source retained for private reading; full-text reproduction or translation permission not inferred from download.'

batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
index_path = essay_dir / 'index.typ'
index = index_path.read_text(encoding='utf-8')
by_title = {paper['title'] + ' / ' + paper['zh_title']: paper for paper in batch}
def update_entry(match):
    entry = match.group(0)
    title = json.loads(re.search(r'title: ("(?:[^"\\]|\\.)*")', entry).group(1))
    paper = by_title.get(title)
    if paper and paper['kind'] == 'full':
        entry = re.sub(r'path: "(?:[^"\\]|\\.)*"', 'path: ' + q(paper['folder'] + '/'), entry)
    return entry
index = re.sub(r'#tufted\.blog-entry\([\s\S]*?\n\)', update_entry, index)
index_path.write_text(index, encoding='utf-8')
catalog_path = root / 'classics-catalog.json'
catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
by_id = {paper['id']: paper for paper in batch}
catalog = [dict(paper, **by_id[paper['id']]) if paper['id'] in by_id else paper for paper in catalog]
catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

pending = [paper for paper in batch if paper['kind'] != 'full']
lines = [
    '# 待补齐站内双语全文的原文清单', '',
    '2026-10-12：Essay目录共58个条目，53篇有站内正文，5篇尚未生成站内双语全文。用户明确为本地个人学习，未发布、未提交或推送。', '',
    '本次自行获取源文件并补入六篇早期原作。按照中国大陆自然人作品作者终身加死亡后50年的期限记录原作状态，不声称这些原作在所有国家都已进入公版。现代英译、现代中译、网站编辑导言和出版机构新增内容不随原作收录。', '',
    '《阴翳礼赞》保留日文原文并附中文译文；《飞蛾之死》《像山一样思考》人工翻译。其余四篇较长译文采用机器初译与部分人工重译，尚未逐句精校。', '',
    '| 文章 | 来源状态 | 原文入口 |', '| --- | --- | --- |',
]
for paper in pending:
    status = 'PDF已下载，保存在本地资料目录；尚未生成全文双语页面' if paper.get('local_source') else '1971年期刊版PDF未成功取得；1969年RAND工作论文为不同版本，未冒充期刊原文'
    lines.append(f'| {paper["zh_title"]} / {paper["title"]} | {status} | [原文]({paper["source"]}) |')
lines += ['', '源文件存于originals-2026-10-12/，已加入Git忽略列表且不进入网站构建输出。下载副本并未被当作用户上传文本。', '', '已有版本差异仍保留：《深层游戏》为用户提供的节选版，《心智、大脑与程序》为预发表稿。', '']
(root / 'pending-originals-2026-10-05.md').write_text('\n'.join(lines), encoding='utf-8')
notes_path = root / 'classics-translation-notes.md'
notes = notes_path.read_text(encoding='utf-8')
marker = '## 2026-10-12 自行下载与本地学习整理'
if marker not in notes:
    notes += '\n' + marker + '\n\n重新按中国大陆保护期限核对原作，补入利奥波德、伍尔夫、谷崎润一郎、罗素、弗莱克斯纳、瑟伯六篇，目录仍58个条目，53篇有站内正文。谷崎采用青空文库日文公版底本，16个原文段落/小节逐段配中文；原版ruby读音及分节圆圈不进入正文，未使用现代英译或中译。谷崎前三个重点段落中的第一、第二、最后段人工重译，其他段落为初稿并校正核心词汇；伍尔夫与利奥波德人工翻译，另外三篇机器初译与选段校正。各篇收录范围与版本只在source-map记录。\n'
    notes_path.write_text(notes, encoding='utf-8')
print('58 entries; 53 local articles; 5 full bilingual readers pending')
