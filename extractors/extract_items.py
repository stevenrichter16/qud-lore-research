#!/usr/bin/env python3
"""Extract ObjectBlueprints/Items.xml — every object with a
Description part. Emits a single consolidated `Items.md` for easy
greppability rather than 800+ micro-files. Also writes companion
files for high-density subsets (books-as-items, cybernetics, etc.).
"""

import re
import sys
from pathlib import Path

from _xml_utils import load_qud_xml, strip_color

QUD_BASE = Path.home() / "Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base"
SRC = QUD_BASE / "ObjectBlueprints" / "Items.xml"
DST = Path(__file__).resolve().parent.parent / "corpus" / "items"


def get_part(obj, name: str):
    for p in obj.findall("part"):
        if p.attrib.get("Name") == name:
            return p
    return None


def get_tag_value(obj, name: str) -> str | None:
    for t in obj.findall("tag"):
        if t.attrib.get("Name") == name:
            return t.attrib.get("Value", "")
    return None


def get_render_name(obj) -> str:
    r = get_part(obj, "Render")
    if r is not None:
        dn = r.attrib.get("DisplayName")
        if dn:
            return strip_color(dn)
    return obj.attrib.get("Name", "?")


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1
    DST.mkdir(parents=True, exist_ok=True)

    tree = load_qud_xml(SRC)
    root = tree.getroot()

    # Collect: (object_id, display_name, description, tier, inherits, is_book, is_quest)
    items: list[dict] = []
    for obj in root.findall(".//object"):
        oid = obj.attrib.get("Name", "")
        if not oid:
            continue
        desc_part = get_part(obj, "Description")
        if desc_part is None:
            continue
        desc = desc_part.attrib.get("Short", "")
        if not desc.strip():
            continue
        display = get_render_name(obj)
        tier = get_tag_value(obj, "Tier") or "—"
        inherits = obj.attrib.get("Inherits", "")
        is_book = get_part(obj, "Book") is not None
        is_quest = (get_tag_value(obj, "QuestItem") is not None
                    or get_tag_value(obj, "QuestStarter") is not None
                    or get_tag_value(obj, "Quest") is not None)
        # Pull out the linked BookID if it's a book-as-item
        book_id = None
        if is_book:
            bp = get_part(obj, "Book")
            if bp is not None:
                book_id = bp.attrib.get("ID", "")
        items.append({
            "id": oid,
            "display": display,
            "description": strip_color(desc),
            "tier": tier,
            "inherits": inherits,
            "is_book": is_book,
            "is_quest": is_quest,
            "book_id": book_id,
        })

    items.sort(key=lambda r: r["display"].lower())

    # Main consolidated file — every item with a description
    main_lines = [
        "# Items — All (descriptions only)",
        "",
        f"_{len(items)} items with a `<part Name=\"Description\">` extracted from `ObjectBlueprints/Items.xml`._",
        "",
        "Sorted alphabetically by display name.",
        "",
        "---",
        "",
    ]
    for it in items:
        tags = []
        if it["is_book"]:
            tags.append("📖 book")
        if it["is_quest"]:
            tags.append("⚑ quest")
        tag_str = "  _" + ", ".join(tags) + "_" if tags else ""
        main_lines.append(f"### {it['display']}{tag_str}")
        main_lines.append("")
        main_lines.append(f"_ID: `{it['id']}` · Tier: {it['tier']} · Inherits: `{it['inherits'] or '—'}`_")
        if it["book_id"]:
            main_lines.append(f"_Book content: see [`books/{it['book_id']}.md`](../books/{it['book_id']}.md)_")
        main_lines.append("")
        main_lines.append(f"> {it['description']}")
        main_lines.append("")
    (DST / "Items.md").write_text("\n".join(main_lines), encoding="utf-8")

    # Subset: books-as-items
    book_items = [it for it in items if it["is_book"]]
    if book_items:
        book_lines = [
            f"# Items: Books ({len(book_items)})",
            "",
            "Items that the player picks up as books. Each links to the book's page contents.",
            "",
            "| Item display name | Item ID | Book ID | File |",
            "|---|---|---|---|",
        ]
        for it in sorted(book_items, key=lambda r: r["display"].lower()):
            bid = it["book_id"] or "?"
            book_lines.append(f"| {it['display']} | `{it['id']}` | `{bid}` | [`books/{bid}.md`](../books/{bid}.md) |")
        (DST / "Items_Books.md").write_text("\n".join(book_lines), encoding="utf-8")

    # Subset: quest items
    quest_items = [it for it in items if it["is_quest"]]
    if quest_items:
        q_lines = [
            f"# Items: Quest items ({len(quest_items)})",
            "",
            "Items tagged `Quest` — recovered, delivered, or examined as part of a quest.",
            "",
        ]
        for it in sorted(quest_items, key=lambda r: r["display"].lower()):
            q_lines.append(f"### {it['display']}")
            q_lines.append("")
            q_lines.append(f"_ID: `{it['id']}` · Tier: {it['tier']}_")
            q_lines.append("")
            q_lines.append(f"> {it['description']}")
            q_lines.append("")
        (DST / "Items_Quest.md").write_text("\n".join(q_lines), encoding="utf-8")

    # Compact INDEX
    idx = [
        "# Items — Index",
        "",
        f"_{len(items)} items with descriptions._",
        "",
        f"- [Items.md](Items.md) — every described item, alphabetical",
        f"- [Items_Books.md](Items_Books.md) — {len(book_items)} book-items (cross-linked to corpus/books/)",
        f"- [Items_Quest.md](Items_Quest.md) — {len(quest_items)} quest items",
        "",
    ]
    (DST / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"OK: wrote items corpus ({len(items)} total, {len(book_items)} books, {len(quest_items)} quest) to {DST}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
