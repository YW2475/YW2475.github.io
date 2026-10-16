"""Extract the two public-domain marriage notes, excluding modern annotations."""
import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parent
url = "https://www.darwinproject.ac.uk/tags/about-darwin/family-life/darwin-marriage"
response = requests.get(url, timeout=45)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")
first = soup.find("h3", string=lambda s: s and "First note" in s)
if first is None:
    raise ValueError("Marriage-note section not found")
blocks = [{"id": "H001", "type": "heading", "en": "First note", "zh": "第一份札记"}]
for node in first.next_siblings:
    if not getattr(node, "name", None):
        continue
    if node.name == "h3" and node.get_text(strip=True) == "Notes":
        break
    if node.name == "h3":
        blocks.append({"id": "H002", "type": "heading", "en": "Second note", "zh": "第二份札记"})
    elif node.name == "p":
        for sup in node.find_all("sup"):
            sup.decompose()
        en = re.sub(r"\[\d+\]", "", node.get_text(" ", strip=True))
        en = re.sub(r"\s+", " ", en).strip()
        n = sum(b["type"] == "paragraph" for b in blocks) + 1
        blocks.append({"id": f"S{n:03d}", "type": "paragraph", "en": en})
if len(blocks) != 23:
    raise ValueError(f"Unexpected source segmentation: {len(blocks)} blocks")
(root / "darwin-marriage-original-blocks.json").write_text(json.dumps(blocks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
for block in blocks:
    print(block["id"], block["en"])
