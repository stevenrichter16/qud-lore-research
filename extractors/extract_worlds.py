#!/usr/bin/env python3
"""Extract Worlds.xml — one .md per world, listing cells + zones.

Most lore content here is structural: zone names and name contexts.
The lore-density payoff is the catalog of named locations
(JoppaWorld villages, Tzimtzlum, Interior dungeons, Coda, etc.).
"""

import sys
from pathlib import Path

from _xml_utils import load_qud_xml, sanitize_filename

QUD_BASE = Path.home() / "Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base"
SRC = QUD_BASE / "Worlds.xml"
DST = Path(__file__).resolve().parent.parent / "corpus" / "worlds"


def render_world(w) -> str:
    name = w.attrib.get("Name", "?")
    disp = w.attrib.get("DisplayName", name)

    out = [f"# World: {disp}", ""]
    out.append(f"- ID: `{name}`")
    if "Plane" in w.attrib:
        out.append(f"- Plane: `{w.attrib['Plane']}`")
    if "Protocol" in w.attrib:
        out.append(f"- Protocol: `{w.attrib['Protocol']}`")
    if "ZoneFactory" in w.attrib:
        out.append(f"- ZoneFactory: `{w.attrib['ZoneFactory']}`")
    if "CustomClock" in w.attrib:
        out.append(f"- CustomClock: `{w.attrib['CustomClock']}`")
    out.append("")

    cells = w.findall("cell")
    if cells:
        out.append(f"## Cells ({len(cells)})")
        out.append("")
        for cell in cells:
            cname = cell.attrib.get("Name", "?")
            out.append(f"### Cell: `{cname}`")
            zones = cell.findall("zone")
            if zones:
                out.append("")
                out.append("| x,y | Level | Name | NameContext | Builders |")
                out.append("|---|---:|---|---|---|")
                for z in zones:
                    zx = z.attrib.get("x", "?")
                    zy = z.attrib.get("y", "?")
                    zlvl = z.attrib.get("Level", "?")
                    zname = z.attrib.get("Name", "?")
                    zctx = z.attrib.get("NameContext", "")
                    builders = [b.attrib.get("Class", "?") for b in z.findall("builder")]
                    builder_str = ", ".join(b for b in builders if b != "?") or "—"
                    out.append(f"| {zx},{zy} | {zlvl} | {zname} | {zctx} | {builder_str} |")
                out.append("")

    # Top-level zones (no cell wrapper)
    top_zones = w.findall("zone")
    if top_zones:
        out.append(f"## Top-level zones ({len(top_zones)})")
        out.append("")
        for z in top_zones[:50]:  # cap to keep readable
            zx = z.attrib.get("x", "?")
            zy = z.attrib.get("y", "?")
            zname = z.attrib.get("Name", "?")
            out.append(f"- ({zx},{zy}) **{zname}**")
        if len(top_zones) > 50:
            out.append(f"- _… {len(top_zones) - 50} more zones omitted from preview._")
        out.append("")

    return "\n".join(out)


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1
    DST.mkdir(parents=True, exist_ok=True)

    tree = load_qud_xml(SRC)
    root = tree.getroot()

    rows: list[tuple[str, str, int, int, str]] = []
    for w in root.findall("world"):
        name = w.attrib.get("Name", "?")
        disp = w.attrib.get("DisplayName", name)
        md = render_world(w)
        fname = f"{sanitize_filename(name)}.md"
        (DST / fname).write_text(md, encoding="utf-8")
        rows.append((
            name, disp,
            len(w.findall("cell")),
            len(w.findall("zone")),
            fname,
        ))

    idx = [
        "# Worlds — Index",
        "",
        f"_{len(rows)} worlds from `Worlds.xml`._",
        "",
        "| ID | Display Name | Cells | Top-level Zones | File |",
        "|---|---|---:|---:|---|",
    ]
    for name, disp, nc, nz, fname in sorted(rows, key=lambda r: r[0].lower()):
        idx.append(f"| `{name}` | {disp} | {nc} | {nz} | [{fname}]({fname}) |")
    (DST / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"OK: wrote {len(rows)} world files + INDEX.md to {DST}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
