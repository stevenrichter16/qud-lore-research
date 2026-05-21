#!/usr/bin/env python3
"""Extract Factions.xml — relations data only (Qud's Factions.xml has no
description prose; faction worldbuilding lives in Conversations.xml,
Books.xml, and Quests.xml instead — see PLAN.md).

Emits one .md per faction with: reputation, feelings about other
factions, worship attitudes, and a 'see also' pointer for prose lore.
"""

import sys
from pathlib import Path

from _xml_utils import load_qud_xml, sanitize_filename, strip_color

QUD_BASE = Path.home() / "Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base"
SRC = QUD_BASE / "Factions.xml"
DST = Path(__file__).resolve().parent.parent / "corpus" / "factions"


def render_faction(f) -> str:
    name = f.attrib.get("Name", "?")
    visible = f.attrib.get("Visible", "true")
    init_rep = f.attrib.get("InitialPlayerReputation", "0")

    out = [f"# Faction: `{name}`", ""]
    out.append(f"- Visible: `{visible}`")
    out.append(f"- Initial player reputation: `{init_rep}`")
    if "Old" in f.attrib:
        out.append(f"- Old: `{f.attrib['Old']}`")
    if "Tag" in f.attrib:
        out.append(f"- Tag: `{f.attrib['Tag']}`")
    if "Worshipable" in f.attrib:
        out.append(f"- Worshipable: `{f.attrib['Worshipable']}`")
    out.append("")

    feelings = f.findall("feeling")
    if feelings:
        out.append("## Feelings (about other factions)")
        out.append("")
        out.append("| About | Value |")
        out.append("|---|---:|")
        for fe in feelings:
            about = fe.attrib.get("About", "?")
            value = fe.attrib.get("Value", "0")
            out.append(f"| `{about}` | {value} |")
        out.append("")

    worships = f.findall("factionworshipattitudes")
    if worships:
        out.append("## Worship attitudes")
        out.append("")
        for w in worships:
            default = w.attrib.get("Default", "")
            apply = w.attrib.get("ApplyDefaultAfterSpecificFeelings", "")
            out.append(f"- Default: `{default}`, ApplyDefaultAfterSpecificFeelings: `{apply}`")
            attitudes = w.findall("factionworshipattitude")
            if attitudes:
                out.append("")
                out.append("  | Toward | Attitude |")
                out.append("  |---|---:|")
                for a in attitudes:
                    aname = a.attrib.get("Name", "?")
                    avalue = a.attrib.get("Attitude", "0")
                    out.append(f"  | `{aname}` | {avalue} |")
                out.append("")

    members = f.findall("member")
    if members:
        out.append("## Member entries")
        out.append("")
        for m in members:
            out.append(f"- `{m.attrib}`")
        out.append("")

    out.append("---")
    out.append("")
    out.append("_Note: `Factions.xml` carries no description prose. For prose lore on this faction, search `corpus/books/`, `corpus/conversations/`, and `corpus/quests/` for the faction name._")
    out.append("")
    return "\n".join(out)


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1
    DST.mkdir(parents=True, exist_ok=True)

    tree = load_qud_xml(SRC)
    root = tree.getroot()

    rows: list[tuple[str, str, str, int, str]] = []
    for f in root.findall("faction"):
        name = f.attrib.get("Name", "?")
        md = render_faction(f)
        fname = f"{sanitize_filename(name)}.md"
        (DST / fname).write_text(md, encoding="utf-8")
        rows.append((
            name,
            f.attrib.get("Visible", "true"),
            f.attrib.get("InitialPlayerReputation", "0"),
            len(f.findall("feeling")),
            fname,
        ))

    idx = [
        "# Factions — Index",
        "",
        f"_{len(rows)} factions from `Factions.xml`._",
        "",
        "_NB: `Factions.xml` carries no description prose. This index is relational data only._",
        "_For prose lore, grep `corpus/books/` `corpus/conversations/` `corpus/quests/` for the faction name._",
        "",
        "| Name | Visible | Init Rep | Feelings | File |",
        "|---|---|---:|---:|---|",
    ]
    for name, visible, rep, nfeel, fname in sorted(rows, key=lambda r: r[0].lower()):
        idx.append(f"| `{name}` | {visible} | {rep} | {nfeel} | [{fname}]({fname}) |")
    (DST / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"OK: wrote {len(rows)} faction files + INDEX.md to {DST}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
