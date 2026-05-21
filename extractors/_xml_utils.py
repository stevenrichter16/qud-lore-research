"""Shared XML loader that fixes Qud's CP-1252 numeric refs before parsing.

Qud's XML data files were authored on Windows with non-portable numeric
character references in the 0x80-0x9F range (e.g. `&#148;` for a right
double quote). These are invalid in XML, which expects Unicode codepoints
there. We pre-substitute them with the proper Unicode equivalents.
"""

from __future__ import annotations

import re
from pathlib import Path
from xml.etree import ElementTree as ET

# CP-1252 0x80-0x9F → Unicode codepoint. Codes not in this map are
# unassigned in CP-1252 (0x81, 0x8D, 0x8F, 0x90, 0x9D) and dropped.
_CP1252_TO_UNICODE = {
    0x80: 0x20AC, 0x82: 0x201A, 0x83: 0x0192, 0x84: 0x201E,
    0x85: 0x2026, 0x86: 0x2020, 0x87: 0x2021, 0x88: 0x02C6,
    0x89: 0x2030, 0x8A: 0x0160, 0x8B: 0x2039, 0x8C: 0x0152,
    0x8E: 0x017D, 0x91: 0x2018, 0x92: 0x2019, 0x93: 0x201C,
    0x94: 0x201D, 0x95: 0x2022, 0x96: 0x2013, 0x97: 0x2014,
    0x98: 0x02DC, 0x99: 0x2122, 0x9A: 0x0161, 0x9B: 0x203A,
    0x9C: 0x0153, 0x9E: 0x017E, 0x9F: 0x0178,
}

# CP437 control range 0x00-0x1F + 0x7F → visible glyph. Qud renders via a
# CP437 tilemap, so refs like &#x7; in book pages mean the bullet glyph
# 0x07, not the BEL control char.
_CP437_GLYPHS = {
    0x00: " ", 0x01: "☺", 0x02: "☻", 0x03: "♥", 0x04: "♦",
    0x05: "♣", 0x06: "♠", 0x07: "•", 0x08: "◘", 0x09: "○",
    0x0A: "◙", 0x0B: "♂", 0x0C: "♀", 0x0D: "♪", 0x0E: "♫",
    0x0F: "☼", 0x10: "►", 0x11: "◄", 0x12: "↕", 0x13: "‼",
    0x14: "¶", 0x15: "§", 0x16: "▬", 0x17: "↨", 0x18: "↑",
    0x19: "↓", 0x1A: "→", 0x1B: "←", 0x1C: "∟", 0x1D: "↔",
    0x1E: "▲", 0x1F: "▼", 0x7F: "⌂",
}

_NUMERIC_REF_RE = re.compile(r"&#(x[0-9a-fA-F]+|\d+);")

def _fix_ref(m: re.Match) -> str:
    token = m.group(1)
    n = int(token[1:], 16) if token[0] in ("x", "X") else int(token)
    # XML control-char refs (illegal in XML 1.0) → CP437 glyph
    if n in _CP437_GLYPHS:
        return _CP437_GLYPHS[n]
    if 0x80 <= n <= 0x9F:
        cp = _CP1252_TO_UNICODE.get(n)
        return chr(cp) if cp is not None else ""
    # leave other numeric refs alone (XML allows them)
    return m.group(0)

def load_qud_xml(path: str | Path) -> ET.ElementTree:
    """Read a Qud XML file, fix CP-1252 numeric refs, return parsed tree."""
    raw = Path(path).read_text(encoding="utf-8")
    fixed = _NUMERIC_REF_RE.sub(_fix_ref, raw)
    return ET.ElementTree(ET.fromstring(fixed))


# -- Color-code stripping for Qud's runtime markup --

_COLOR_RE = re.compile(r"\{\{([^|}]+)\|([^}]*)\}\}", re.DOTALL)
_AMP_COLOR_RE = re.compile(r"&[a-zA-Z]")

def strip_color(text: str) -> str:
    if not text:
        return ""
    prev = None
    while prev != text:
        prev = text
        text = _COLOR_RE.sub(r"\2", text)
    return _AMP_COLOR_RE.sub("", text)


def sanitize_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]", "_", name)


# -- Shared conversation rendering (for Conversations.xml and HiddenConversations.xml) --

def _collect_text_blocks(elem) -> list[str]:
    """Return text blocks from this element's direct text and <text> children."""
    blocks: list[str] = []
    if elem.text and elem.text.strip():
        blocks.append(strip_color(elem.text.strip()))
    for child in elem.findall("text"):
        t = (child.text or "").strip()
        if t:
            blocks.append(strip_color(t))
    return blocks

def _render_choice_lines(choice) -> list[str]:
    lines: list[str] = []
    cid = choice.attrib.get("ID", "?")
    goto = (choice.attrib.get("Target")
            or choice.attrib.get("Goto")
            or choice.attrib.get("GotoID")
            or "")
    arrow = f" → `{goto}`" if goto else ""
    lines.append(f"- **choice** `{cid}`{arrow}")
    for block in _collect_text_blocks(choice):
        for ln in block.splitlines():
            lines.append(f"    > {ln}")
    for part in choice.findall("part"):
        pname = part.attrib.get("Name", "?")
        attrs = " ".join(f"{k}={v}" for k, v in part.attrib.items() if k != "Name")
        attr_suffix = f" ({attrs})" if attrs else ""
        lines.append(f"    - _part: `{pname}`{attr_suffix}_")
        if part.text and part.text.strip():
            for ln in strip_color(part.text.strip()).splitlines():
                lines.append(f"        > {ln}")
    return lines

def _render_node_lines(node, label: str) -> list[str]:
    lines: list[str] = []
    nid = node.attrib.get("ID", "?")
    # Surface entry conditions if present (for <start> nodes, these are
    # the gating conditions, very lore-relevant)
    cond_attrs = []
    for k in ("IfHaveState", "IfTestState", "IfHaveQuestComplete", "IfQuestActive"):
        if k in node.attrib:
            cond_attrs.append(f"{k}=`{node.attrib[k]}`")
    cond_suffix = "  _" + ", ".join(cond_attrs) + "_" if cond_attrs else ""
    lines.append(f"### {label} `{nid}`{cond_suffix}")
    lines.append("")
    for block in _collect_text_blocks(node):
        lines.append(block)
        lines.append("")
    choices = node.findall("choice")
    if choices:
        lines.append("**Choices:**")
        for c in choices:
            lines.extend(_render_choice_lines(c))
        lines.append("")
    return lines

def render_conversation_md(conv, source_note: str = "") -> str:
    """Render a <conversation> element as markdown."""
    cid = conv.attrib.get("ID", "Untitled")
    inherits = conv.attrib.get("Inherits", None)
    nodes = conv.findall("node")
    starts = conv.findall("start")
    root_choices = conv.findall("choice")

    out: list[str] = [f"# Conversation: `{cid}`", ""]
    if source_note:
        out.append(f"_{source_note}_")
        out.append("")
    if inherits is None:
        out.append("_Inherits: (default: BaseConversation)_")
    elif inherits == "":
        out.append("_Inherits: (none — explicit empty, suppresses default)_")
    else:
        out.append(f"_Inherits: `{inherits}`_")
    out.append("")
    out.append(f"_{len(starts)} start(s), {len(nodes)} node(s), {len(root_choices)} root-level choice(s)_")
    out.append("")
    out.append("---")
    out.append("")

    if root_choices:
        out.append("## Conversation-level choices")
        out.append("")
        for c in root_choices:
            out.extend(_render_choice_lines(c))
        out.append("")

    if starts:
        out.append("## Start nodes (conditional entry points)")
        out.append("")
        for s in starts:
            out.extend(_render_node_lines(s, "Start"))

    if nodes:
        out.append("## Nodes")
        out.append("")
        for n in nodes:
            out.extend(_render_node_lines(n, "Node"))

    return "\n".join(out)
