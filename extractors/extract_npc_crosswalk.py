#!/usr/bin/env python3
"""Build a creature/NPC → conversation crosswalk from ObjectBlueprints/Creatures.xml.

Walks the inheritance chain: an object inherits a conversation if any
ancestor declares <part Name="ConversationScript" ConversationID="..."/>.

Writes ../corpus/npc_index/INDEX.md and a per-conversation reverse-index
listing every creature that uses each conversation.
"""

import re
import sys
from pathlib import Path

from _xml_utils import load_qud_xml

QUD_BASE = Path.home() / "Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base"
SRC = QUD_BASE / "ObjectBlueprints" / "Creatures.xml"
DST = Path(__file__).resolve().parent.parent / "corpus" / "npc_index"

def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1
    DST.mkdir(parents=True, exist_ok=True)

    tree = load_qud_xml(SRC)
    root = tree.getroot()

    # Collect every <object> with its Name, Inherits, and any ConversationID part
    objects: dict[str, dict] = {}
    for obj in root.findall(".//object"):
        name = obj.attrib.get("Name", "")
        if not name:
            continue
        inherits = obj.attrib.get("Inherits", "")
        direct_conv = None
        for part in obj.findall("part"):
            if part.attrib.get("Name") == "ConversationScript":
                direct_conv = part.attrib.get("ConversationID", "")
                break
        objects[name] = {"inherits": inherits, "direct_conv": direct_conv}

    # Walk inheritance to resolve effective ConversationID
    def resolve(name: str, seen: set[str] | None = None) -> str | None:
        if seen is None:
            seen = set()
        if name in seen or name not in objects:
            return None
        seen.add(name)
        info = objects[name]
        if info["direct_conv"]:
            return info["direct_conv"]
        if info["inherits"]:
            return resolve(info["inherits"], seen)
        return None

    # Build (creature_name, conversation_id, "direct" or "inherited")
    rows: list[tuple[str, str, str]] = []
    for name, info in objects.items():
        cid = resolve(name)
        if cid:
            origin = "direct" if info["direct_conv"] else "inherited"
            rows.append((name, cid, origin))

    rows.sort(key=lambda r: (r[1].lower(), r[0].lower()))

    # Main creature → conversation table
    main_idx = [
        "# NPC ↔ Conversation Crosswalk",
        "",
        f"_{len(rows)} creature objects resolve to a `ConversationID`._",
        "",
        "_Direct = the object itself has the `ConversationScript` part._",
        "_Inherited = resolved by walking the `Inherits=` chain._",
        "",
        "| Creature | Conversation | Origin |",
        "|---|---|---|",
    ]
    for name, cid, origin in rows:
        main_idx.append(f"| `{name}` | [`{cid}`](../conversations/{cid}.md) | {origin} |")
    (DST / "INDEX.md").write_text("\n".join(main_idx), encoding="utf-8")

    # Reverse: per-conversation list of creatures
    by_conv: dict[str, list[tuple[str, str]]] = {}
    for name, cid, origin in rows:
        by_conv.setdefault(cid, []).append((name, origin))

    rev = [
        "# Conversation → Creatures (reverse index)",
        "",
        "Every conversation, and which creature objects resolve to it.",
        "",
    ]
    for cid in sorted(by_conv.keys(), key=str.lower):
        rev.append(f"## `{cid}`")
        rev.append("")
        for name, origin in by_conv[cid]:
            rev.append(f"- `{name}` ({origin})")
        rev.append("")
    (DST / "BY_CONVERSATION.md").write_text("\n".join(rev), encoding="utf-8")

    print(f"OK: wrote crosswalk ({len(rows)} creatures, {len(by_conv)} conversations) to {DST}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
