#!/usr/bin/env python3
"""Extract one markdown file per conversation from Qud's Conversations.xml.

Uses the shared renderer in _xml_utils.render_conversation_md, which
also handles <start> conditional entry nodes.
"""

import sys
from pathlib import Path

from _xml_utils import load_qud_xml, render_conversation_md, sanitize_filename

QUD_BASE = Path.home() / "Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base"
SRC = QUD_BASE / "Conversations.xml"
DST = Path(__file__).resolve().parent.parent / "corpus" / "conversations"


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1
    DST.mkdir(parents=True, exist_ok=True)

    tree = load_qud_xml(SRC)
    root = tree.getroot()

    index_rows: list[tuple[str, str, int, int, int, str]] = []
    for conv in root.findall("conversation"):
        cid = conv.attrib.get("ID", "Untitled")
        inherits = conv.attrib.get("Inherits", "")
        md = render_conversation_md(conv)
        fname = f"{sanitize_filename(cid)}.md"
        (DST / fname).write_text(md, encoding="utf-8")
        index_rows.append((
            cid, inherits,
            len(conv.findall("start")),
            len(conv.findall("node")),
            len(conv.findall("choice")),
            fname,
        ))

    def sort_key(r):
        cid_lc = r[0].lower()
        return (0 if cid_lc.startswith("base") else 1, cid_lc)

    idx = [
        "# Conversations — Index",
        "",
        f"_{len(index_rows)} conversations from `Conversations.xml`._",
        "",
        "| ID | Inherits | Starts | Nodes | Root choices | File |",
        "|---|---|---:|---:|---:|---|",
    ]
    for cid, inherits, ns, nn, nc, fname in sorted(index_rows, key=sort_key):
        inh = inherits if inherits else "_(default)_"
        idx.append(f"| `{cid}` | {inh} | {ns} | {nn} | {nc} | [{fname}]({fname}) |")
    (DST / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"OK: wrote {len(index_rows)} conversation files + INDEX.md to {DST}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
