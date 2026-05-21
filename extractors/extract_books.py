#!/usr/bin/env python3
"""Extract one markdown file per book from Qud's Books.xml.

Reads from the Steam install. Writes to ../corpus/books/.
Idempotent: rerunning overwrites.
"""

import re
import sys
from pathlib import Path

from _xml_utils import load_qud_xml

QUD_BASE = Path.home() / "Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base"
SRC = QUD_BASE / "Books.xml"
DST = Path(__file__).resolve().parent.parent / "corpus" / "books"

# Qud color codes: {{X|text}} renders text in color X. Strip to plain.
COLOR_RE = re.compile(r"\{\{([^|}]+)\|([^}]*)\}\}", re.DOTALL)
# Some legacy color marks like &y, &W, &Rblah are single-char prefixes.
AMP_COLOR_RE = re.compile(r"&[a-zA-Z]")

def strip_color(text: str) -> str:
    if not text:
        return ""
    prev = None
    while prev != text:
        prev = text
        text = COLOR_RE.sub(r"\2", text)
    text = AMP_COLOR_RE.sub("", text)
    return text

def sanitize_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]", "_", name)

def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1
    DST.mkdir(parents=True, exist_ok=True)
    tree = load_qud_xml(SRC)
    root = tree.getroot()

    index_rows: list[tuple[str, str, int, str]] = []
    for book in root.findall("book"):
        bid = book.attrib.get("ID", "Untitled")
        title = strip_color(book.attrib.get("Title", bid))
        pages_text: list[str] = []
        for p in book.findall("page"):
            raw = p.text or ""
            pages_text.append(strip_color(raw).strip())

        out_lines: list[str] = [
            f"# {title}",
            "",
            f"_ID: `{bid}`_",
            "",
            f"_{len(pages_text)} page{'s' if len(pages_text) != 1 else ''}_",
            "",
            "---",
            "",
        ]
        for i, p in enumerate(pages_text, 1):
            if len(pages_text) > 1:
                out_lines.append(f"## Page {i}")
                out_lines.append("")
            out_lines.append(p)
            out_lines.append("")

        fname = f"{sanitize_filename(bid)}.md"
        (DST / fname).write_text("\n".join(out_lines), encoding="utf-8")
        index_rows.append((bid, title, len(pages_text), fname))

    idx = [
        "# Books — Index",
        "",
        f"_{len(index_rows)} books extracted from `Books.xml`._",
        "",
        "| ID | Title | Pages | File |",
        "|---|---|---:|---|",
    ]
    for bid, title, npages, fname in sorted(index_rows, key=lambda r: r[0].lower()):
        idx.append(f"| `{bid}` | {title} | {npages} | [{fname}]({fname}) |")
    (DST / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"OK: wrote {len(index_rows)} book files + INDEX.md to {DST}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
