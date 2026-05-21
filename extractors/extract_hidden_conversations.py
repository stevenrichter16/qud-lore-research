#!/usr/bin/env python3
"""Extract HiddenConversations.xml — the same shape as Conversations.xml
but flagged ExcludeFromCorpusGeneration='true' by the game itself.
Output is segregated into corpus/conversations_hidden/ and each file
gets a SPOILER banner so endgame content (Barathrum Z-Ascended, Coda,
Spindle) doesn't bleed into beginner-level video scripts.
"""

import sys
from pathlib import Path

from _xml_utils import load_qud_xml, render_conversation_md, sanitize_filename

QUD_BASE = Path.home() / "Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base"
SRC = QUD_BASE / "HiddenConversations.xml"
DST = Path(__file__).resolve().parent.parent / "corpus" / "conversations_hidden"

SPOILER_BANNER = (
    "> ⚠️  **SPOILER WARNING.** This conversation is in `HiddenConversations.xml`,\n"
    "> which the game flags `ExcludeFromCorpusGeneration='true'`. Contents may\n"
    "> include endgame branches (Spindle ascent, Coda, late-quest reveals).\n"
)


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1
    DST.mkdir(parents=True, exist_ok=True)

    tree = load_qud_xml(SRC)
    root = tree.getroot()

    index_rows: list[tuple[str, int, int, int, str]] = []
    for conv in root.findall("conversation"):
        cid = conv.attrib.get("ID", "Untitled")
        md = render_conversation_md(conv, source_note="From HiddenConversations.xml")
        out = SPOILER_BANNER + "\n" + md
        fname = f"{sanitize_filename(cid)}.md"
        (DST / fname).write_text(out, encoding="utf-8")
        index_rows.append((
            cid,
            len(conv.findall("start")),
            len(conv.findall("node")),
            len(conv.findall("choice")),
            fname,
        ))

    idx = [
        "# Hidden Conversations — Index",
        "",
        SPOILER_BANNER,
        "",
        f"_{len(index_rows)} hidden conversations from `HiddenConversations.xml`._",
        "",
        "| ID | Starts | Nodes | Root choices | File |",
        "|---|---:|---:|---:|---|",
    ]
    for cid, ns, nn, nc, fname in sorted(index_rows, key=lambda r: r[0].lower()):
        idx.append(f"| `{cid}` | {ns} | {nn} | {nc} | [{fname}]({fname}) |")
    (DST / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"OK: wrote {len(index_rows)} hidden conversation files + INDEX.md to {DST}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
