"""Integrate this essay batch without generating placeholder article pages."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
essay_dir = root.parent / "Essay"
batch = json.loads((root / "essay-additions-2026-10-12.json").read_text(encoding="utf-8"))
q = lambda value: json.dumps(value, ensure_ascii=False)

for stem, entry_id in (("pencil", "read-pencil"), ("darwin-marriage", "darwin-marriage")):
    paper = next(entry for entry in batch if entry["id"] == entry_id)
    blocks = json.loads((root / f"{stem}-original-blocks.json").read_text(encoding="utf-8"))
    translations = json.loads((root / f"{stem}-translations.json").read_text(encoding="utf-8"))
    for block in blocks:
        if "zh" not in block:
            block["zh"] = translations[block["id"]]
        if not block["en"].strip() or not block["zh"].strip():
            raise ValueError(f"Empty block: {entry_id} {block['id']}")
    if stem == "pencil":
        # The web renderer places the original author note inside a blockquote.
        blocks[-1]["en"] = re.sub(r"^>\s*\*\s*", "* ", blocks[-1]["en"])
    lines = [
        '#import "../index.typ": template, tufted',
        '#import "../../_essay/bilingual.typ": zh',
        '#show: template.with(',
        f'  title: {q(paper["title"])},',
        f'  author: {q(paper["author"])},',
        f'  date: {q(str(paper["year"]))},',
        '  lang: "en",',
        '  css: ("/assets/custom.css", "/assets/essay.css"),',
    ]
    if stem == "pencil":
        # Required CC attribution sits outside the article, in the existing footer.
        lines.append('  footer-elements: ([#link("https://fee.org/articles/i-pencil/")[FEE] · #link("https://creativecommons.org/licenses/by/4.0/")[CC BY 4.0] · 中文译文],),')
    lines += [')', '', f'= {paper["title"]} / {paper["zh_title"]}', '']
    for block in blocks:
        if block["type"] == "heading":
            lines += [f'== {block["en"]} / {block["zh"]}', '']
        else:
            lines += [
                f'#html.p(id: {q("en-" + block["id"])})[#text({q(block["en"])})]', '',
                f'#zh(id: {q(block["id"])})[#text({q(block["zh"])})]', '',
            ]
    folder = essay_dir / paper["folder"]
    folder.mkdir(exist_ok=True)
    (folder / "index.typ").write_text("\n".join(lines), encoding="utf-8")
    source_map = {
        "paper": paper, "scope": "full", "translation_method": "assistant-translated",
        "blocks": blocks,
        "excluded": "Modern website introductions, navigation, editorial annotations and subsequent commentary.",
    }
    (root / f"{entry_id}-source-map.json").write_text(json.dumps(source_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

index_path = essay_dir / "index.typ"
index = index_path.read_text(encoding="utf-8")
chunks = re.split(r"(?m)(^== .+\n)", index)
categories = {
    "Nature and Evolution / 自然与演化": "自然与演化",
    "Mind and Judgment / 心智与判断": "心智与判断",
    "Mathematics and Physics / 数学与物理": "数学与物理",
    "Information and Technology / 信息与技术": "信息与技术",
    "Economy and Society / 经济与社会": "经济与社会",
    "Literature and Ideas / 文学与思想": "文学与思想",
}
for i in range(1, len(chunks), 2):
    category = categories[chunks[i].strip().removeprefix("== ")]
    entries = re.findall(r"#tufted\.blog-entry\([\s\S]*?\n\)", chunks[i + 1])
    for paper in batch:
        if paper["category"] != category:
            continue
        path = paper["folder"] + "/" if paper["kind"] == "full" else paper["source"]
        if any(f'title: {q(paper["title"] + " / " + paper["zh_title"])}' in entry for entry in entries):
            continue
        entries.append("\n".join([
            '#tufted.blog-entry(', f'  date: {q(str(paper["year"]))},',
            f'  path: {q(path)},', f'  title: {q(paper["title"] + " / " + paper["zh_title"])},', ')',
        ]))
    entries.sort(key=lambda entry: int(re.search(r'date: "(\d+)"', entry).group(1)))
    chunks[i + 1] = "\n" + "\n\n".join(entries) + "\n\n"
index_path.write_text("".join(chunks).rstrip() + "\n", encoding="utf-8")

catalog_path = root / "classics-catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
existing_ids = {entry["id"] for entry in catalog}
catalog.extend(paper for paper in batch if paper["id"] not in existing_ids)
catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

pending = [paper for paper in batch if paper["kind"] == "external"]
pending_lines = [
    '# 待补齐双语全文的原文清单', '',
    '2026-10-12：新增13个条目，目录共58篇；47篇有站内正文，11篇等待用户提供原文。', '',
    '新加入《我，铅笔》采用FEE明确标注CC BY 4.0的版本，《结婚札记》收录达尔文的两份公版手稿。其余新增条目链接至原文或出版页面，不生成摘要、导读或占位正文。', '',
    '| 文章 | 作者 | 年份 | 原文或版本入口 |',
    '| --- | --- | --- | --- |',
]
pending_lines.extend(f'| {paper["zh_title"]} / {paper["title"]} | {paper["author"]} | {paper["year"]} | [链接]({paper["source"]}) |' for paper in pending)
pending_lines += ['', '《阴翳礼赞》的链接为出版介绍；可以提供日文原作或英文译本。《色盲画家的病例》可以提供1987年文章或1995年收入书中的版本，收录时按实际提供的版本记录。', '', '已有版本差异仍保留：《深层游戏》为用户提供的节选版，《心智、大脑与程序》为预发表稿。', '']
(root / "pending-originals-2026-10-05.md").write_text("\n".join(pending_lines), encoding="utf-8")
notes_path = root / "classics-translation-notes.md"
notes = notes_path.read_text(encoding="utf-8")
marker = '## 2026-10-12 新增十三篇'
if marker not in notes:
    notes += '\n' + marker + '\n\n新增十二篇推荐文章与达尔文《结婚札记》，目录共58个条目。两篇新增站内全文采用人工逐段翻译：《我，铅笔》44个段落/标题/原注块，《结婚札记》两份手稿、21段。其余11篇为原文或版本直达链接，待用户提供文本后补入站内双语全文。页面不加导读、版本说明或占位正文。《我，铅笔》依据FEE明确的CC BY 4.0许可转载，署名与标题保留，来源、许可及新增中文译文标识放在正文之外的页脚。\n'
    notes_path.write_text(notes, encoding="utf-8")

print(f"Essay entries: {len(re.findall(r'#tufted.blog-entry', index_path.read_text(encoding='utf-8')))}")
print(f"Added: {len(batch)}; local bilingual originals: 2; pending originals: {len(pending)}")
