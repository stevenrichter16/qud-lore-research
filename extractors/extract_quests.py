#!/usr/bin/env python3
"""Extract Quests.xml — one .md per quest with Hagiograph + Gospel
templates surfaced (these are the canonical lore templates per quest).
"""

import sys
from pathlib import Path

from _xml_utils import load_qud_xml, sanitize_filename, strip_color

QUD_BASE = Path.home() / "Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base"
SRC = QUD_BASE / "Quests.xml"
DST = Path(__file__).resolve().parent.parent / "corpus" / "quests"


def render_quest(q) -> str:
    name = q.attrib.get("Name", "?")
    out = [f"# Quest: {name}", ""]

    # Header attributes — load-bearing lore metadata
    for key, label in [
        ("Factions", "Factions"),
        ("Reputation", "Reputation"),
        ("Level", "Level"),
        ("Achievement", "Achievement"),
        ("HagiographCategory", "Hagiograph Category"),
    ]:
        if key in q.attrib:
            out.append(f"- **{label}:** {q.attrib[key]}")
    out.append("")

    if "Accomplishment" in q.attrib:
        out.append("## Accomplishment")
        out.append("")
        out.append(f"> {strip_color(q.attrib['Accomplishment'])}")
        out.append("")

    if "Hagiograph" in q.attrib:
        out.append("## Hagiograph _(player legend template)_")
        out.append("")
        out.append(f"> {strip_color(q.attrib['Hagiograph'])}")
        out.append("")

    if "Gospel" in q.attrib:
        out.append("## Gospel _(celebratory narrative template)_")
        out.append("")
        out.append(f"> {strip_color(q.attrib['Gospel'])}")
        out.append("")

    steps = q.findall("step")
    if steps:
        out.append(f"## Steps ({len(steps)})")
        out.append("")
        for i, s in enumerate(steps, 1):
            sname = s.attrib.get("Name", "?")
            xp = s.attrib.get("XP", "?")
            out.append(f"### Step {i}: {sname}")
            out.append("")
            out.append(f"_XP: {xp}_")
            out.append("")
            text_el = s.find("text")
            if text_el is not None and text_el.text:
                out.append(f"> {strip_color(text_el.text.strip())}")
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
    for q in root.findall("quest"):
        name = q.attrib.get("Name", "?")
        md = render_quest(q)
        fname = f"{sanitize_filename(name)}.md"
        (DST / fname).write_text(md, encoding="utf-8")
        rows.append((
            name,
            q.attrib.get("Factions", "—"),
            q.attrib.get("Level", "?"),
            len(q.findall("step")),
            fname,
        ))

    idx = [
        "# Quests — Index",
        "",
        f"_{len(rows)} quests from `Quests.xml`._",
        "",
        "| Quest | Factions | Level | Steps | File |",
        "|---|---|---:|---:|---|",
    ]
    for name, factions, level, nsteps, fname in sorted(rows, key=lambda r: r[0].lower()):
        idx.append(f"| {name} | {factions} | {level} | {nsteps} | [{fname}]({fname}) |")
    (DST / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"OK: wrote {len(rows)} quest files + INDEX.md to {DST}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
