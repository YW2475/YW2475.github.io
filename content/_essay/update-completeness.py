"""Keep the reading directory free of entries missing the original work."""
import json
import re
import shutil
from pathlib import Path

private = Path(__file__).resolve().parent
project = private.parents[1]
essay = private.parent / 'Essay'
pending_ids = {'dillard-weasels', 'borges-wilkins', 'sacks-colorblind',
               'schelling-segregation', 'boulding-spaceship', 'geertz-cockfight'}
darwin = json.loads((private / 'darwin-source-map.json').read_text(encoding='utf-8'))
catalog_path = private / 'classics-catalog.json'
catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
for entry in catalog:
    if entry.get('status', '').startswith('bilingual-full-licensed-'):
        pending_ids.discard(entry['id'])
for filename in ('classics-catalog.json', 'essay-additions-2026-10-05.json', 'essay-additions-2026-10-12.json'):
    path = private / filename
    records = json.loads(path.read_text(encoding='utf-8'))
    for entry in records:
        if entry['id'] == 'darwin':
            entry.update(darwin['paper'])
            entry.update(scope='full-book', status='bilingual-full-book', visible=True,
                         translation_status=darwin['translation_status'])
        elif entry['id'] in pending_ids:
            entry['visible'] = False
            if entry['id'] == 'geertz-cockfight':
                entry['kind'] = 'abridged'
                entry['status'] = 'incomplete-original'
                entry['scope'] = 'complete-supplied-abridged-reprint'
            else:
                entry['status'] = 'awaiting-user-provided-complete-source'
        elif entry['id'] == 'searle-programs':
            entry['scope'] = 'complete-supplied-penultimate-draft'
            entry['status'] = 'bilingual-complete-supplied-draft'
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

index = essay / 'index.typ'
text = index.read_text(encoding='utf-8')
entry_pattern = re.compile(r'#tufted\.blog-entry\(\s*date:.*?\n\)\s*', re.S)
def retain(match):
    block = match.group(0)
    if 'path: "https://' in block or 'path: "http://' in block or ('geertz-cockfight' in pending_ids and 'path: "Deep Play 1972/' in block):
        return ''
    return block
index.write_text(entry_pattern.sub(retain, text), encoding='utf-8')

# Preserve the complete existing abridged page before removing its public entry.
old = essay / 'Deep Play 1972'
backup = private / 'unfinished/Deep Play 1972'
if 'geertz-cockfight' in pending_ids and (old / 'index.typ').exists():
    shutil.copytree(old, backup, dirs_exist_ok=True)
    (old / 'index.typ').unlink()
stale = project / '_site/Essay/Deep Play 1972/index.html'
assert stale.resolve().is_relative_to((project / '_site').resolve())
if 'geertz-cockfight' in pending_ids and stale.exists():
    stale.unlink()

catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
for ident, filename in [('geertz-cockfight', 'geertz-cockfight-source-map.json'),
                        ('searle-programs', 'searle-programs-source-map.json')]:
    path = private / filename
    mapped = json.loads(path.read_text(encoding='utf-8'))
    record = next(x for x in catalog if x['id'] == ident)
    mapped['paper'].update(record)
    mapped['scope'] = record['scope']
    path.write_text(json.dumps(mapped, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
pending = [x for x in catalog if x['id'] in pending_ids]
visible_count = index.read_text(encoding='utf-8').count('#tufted.blog-entry(')
lines = [f'# 待补齐双语全文：{len(pending)}篇', '',
         f'2026-10-12。阅读目录保留{visible_count}个站内条目；以下{len(pending)}篇尚未生成完整站内双语页，不能算作完成。', '',
         '《蚯蚓》已经从第七章选章扩展为1881年修订版全书：引言、七章、索引、15幅原图、8个表格片段及原注，逐段附中文。中文覆盖完整，仍为未逐句精校的译稿。', '',
         '《巴厘岛斗鸡札记》已补成MIT Press的2005年完整重刊版（31页、43条原注），原文标有CC BY-NC 4.0许可，全部附中文。', '',
         '《宇宙飞船地球》已按Encyclopedia of Earth明确标注CC BY-SA的全文转录补齐，包括4条原注，全部附中文。6篇的本地PDF现在均已取得；下载完成与站内双语全文完成分别记录。', '',
         '| 文章 | 还缺什么 |', '| --- | --- |']
for item in pending:
    if item['id'] == 'geertz-cockfight':
        missing = '用户所提供PDF为节选重印本，现有内容已全部转录；仍缺1972年原刊全文（第1–37页）。已有节选页保留在 unfinished/Deep Play 1972/。'
    elif item['id'] == 'schelling-segregation':
        missing = '1971年期刊版完整PDF已自行下载并核对首尾页143–186，另附出版商声明页；尚未生成站内全文双语页。'
    else:
        missing = '已有自行下载副本，但尚无用户提供的完整文本；尚未生成站内全文双语页。'
    lines.append('| ' + item['zh_title'] + ' / ' + item['title'] + ' | ' + missing + ' |')
lines += ['', '## 版本范围与检查限度', '',
          '《心智、大脑与程序》保留用户提供的完整预发表稿，不称为1980年正式发表版。',
          f'{visible_count}个站内条目不等于{visible_count}篇均已与各自原刊逐字核对；其余条目沿用既有全文转录。本次对《蚯蚓》检查了章节、段落译文、图表、索引结尾及页面生成，并对《斗鸡札记》检查了全部31页和43条原注。',
          '待补篇目仍受版权保护。私用不改变整篇转载/全译非用户提供文本的限制；取得用户提供的完整原文后可继续做逐段双语转换。',
          '源文件保留在私有资料目录，不进入网站输出；没有发布、提交或推送。', '']
(private / 'pending-originals-2026-10-05.md').write_text('\n'.join(lines), encoding='utf-8')
audit = {'date': '2026-10-12', 'visible_local_entries': len(re.findall(r'#tufted\.blog-entry\(', index.read_text(encoding='utf-8'))),
         'unfinished': [{'id': x['id'], 'title': x['title'], 'status': 'incomplete'} for x in pending],
         'darwin_coverage': darwin['coverage'], 'verification_scope': 'Darwin structure, translation coverage and build; prior entries not re-collated word-for-word.',
         'searle_edition': 'Complete supplied penultimate draft; final published edition unverified.'}
(private / 'completeness-audit-2026-10-12.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'reading_entries': audit['visible_local_entries'], 'unfinished': len(pending)}, ensure_ascii=False))
