#!/usr/bin/env python3
"""Build a cross-cutting topic index across the entire corpus.

For each entity (canon name), emits `corpus/topic_index/<name>.md`
listing every file:line in the corpus where it's mentioned, grouped
by source category, with a short excerpt per mention. The master
`INDEX.md` lists every entity sorted by mention count.

Entity set = hand-curated SEED_ENTITIES ∪ auto-derived names from
faction / conversation / quest IDs (filtered for noise).
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

CORPUS = Path(__file__).resolve().parent.parent / "corpus"
DST = CORPUS / "topic_index"

# Sources to scan, in display order. (subdir, category_label)
CATEGORIES = [
    ("books", "Books"),
    ("conversations", "Conversations"),
    ("conversations_hidden", "Hidden Conversations (spoilers)"),
    ("factions", "Factions"),
    ("worlds", "Worlds"),
    ("quests", "Quests"),
    ("items", "Items"),
    ("npc_index", "NPC index"),
]

# Curated canon names + aliases. Keep entries distinctive (no English words).
SEED_ENTITIES: dict[str, list[str]] = {
    # Cosmology / metaphysics
    "Spindle": ["Spindle"],
    "Gyre": ["Gyre"],
    "Coda": ["Coda"],
    "Siach": ["Siach"],  # mystical-sphere term used by Resheph
    "Imago": ["imago"],
    # Mythic figures
    "Sky-Bear": ["Sky-Bear", "Sky Bear", "Skybear"],
    "Saad Amus": ["Saad Amus", "Amus-an"],
    "Resheph": ["Resheph"],
    "Sheba Hagadias": ["Sheba Hagadias", "Hagadias"],
    "Caiafas": ["Caiafas"],
    "Ptoh": ["Ptoh"],
    "Aldersesse": ["Aldersesse"],
    # Locations — settlements
    "Joppa": ["Joppa"],
    "Grit Gate": ["Grit Gate"],
    "Six Day Stilt": ["Six Day Stilt", "the Stilt"],
    "Kyakukya": ["Kyakukya"],
    "Bey Lah": ["Bey Lah"],
    "Bethesda Susa": ["Bethesda Susa"],
    "Omonporch": ["Omonporch"],
    "Ezra": ["Ezra"],
    # Locations — regions and ruins
    "Brightsheol": ["Brightsheol"],
    "Golgotha": ["Golgotha"],
    "Tzimtzlum": ["Tzimtzlum"],
    "Sheva": ["Sheva"],
    "Moghra'yi": ["Moghra'yi", "Moghra'ji"],
    "Sunderlies": ["Sunderlies"],
    "Athenreach": ["Athenreach"],
    "Great Salt Desert": ["Great Salt Desert", "Salt Desert"],
    "Moon Stair": ["Moon Stair"],
    "Lake Hinnom": ["Lake Hinnom"],
    "Red Rock": ["Red Rock"],
    "Palladium Reef": ["Palladium Reef"],
    # Major NPCs
    "Barathrum": ["Barathrum"],
    "Mehmet": ["Mehmet"],
    "Argyve": ["Argyve"],
    "Q Girl": ["Q Girl", "Q-Girl", "QGirl"],
    "Yla Haj": ["Yla Haj"],
    "Asphodel": ["Asphodel"],
    "Indrix": ["Indrix"],
    "Otho": ["Otho"],
    "Eskhind": ["Eskhind"],
    "Hortensa": ["Hortensa"],
    "Neek": ["Neek"],
    "the Earl": ["the Earl"],
    "Irudad": ["Irudad"],
    "Warden Yrame": ["Warden Yrame", "Yrame"],
    "Warden Indrix": ["Warden Indrix"],
    "Mamon Souldrinker": ["Mamon Souldrinker", "Mamon"],
    "Rebekah": ["Rebekah"],
    "Tam": ["Tam"],
    # Factions / cults
    "Mechanimist": ["Mechanimist"],
    "Putus Templar": ["Putus Templar"],
    "Barathrumite": ["Barathrumite"],
    "Consortium": ["Consortium"],
    "Wardens": ["Wardens"],
    "Daughters of Exile": ["Daughters of Exile"],
    "Eaters of the People": ["Eaters of the People"],
    "Issachari": ["Issachari"],
    "Mopango": ["Mopango"],
    "Slynth": ["Slynth"],
    # Religion / pantheon
    "Girsh": ["Girsh", "girshling"],
    "Cherubim": ["Cherub"],
    "Seraph": ["Seraph"],
    "Templar": ["Templar"],
    # Ecology / canon objects
    "watervine": ["watervine"],
    "salt sun": ["salt sun"],
    "amaranthine prism": ["amaranthine prism", "AmaranthinePrism"],
    "black glass": ["black glass"],
    "Repulsive Device": ["repulsive device"],
    "vinewafer": ["vinewafer"],
    "dromad": ["dromad"],
    "snapjaw": ["snapjaw"],
    "baboon": ["baboon"],
    "baetyl": ["baetyl"],
    # Books-as-entities (the work, referenced from other texts)
    "Canticles": ["Canticles"],
    "Quotes": ["Lost Histories"],
    # Calendar / time
    "Year of the Tortoise": ["Year of the Tortoise"],
    "Beetle Moon": ["Beetle Moon"],
}

STOPWORDS = {
    "true", "false", "none", "default", "base", "test", "simple",
    "generic", "item", "object", "name", "value", "type", "tag",
    "convert", "farmer", "trader", "herder", "merchant", "pilgrim",
}

# Auto-derive blacklist: structural IDs that aren't lore entities.
# Names starting with "Base" are also auto-skipped (conversation scaffolding).
AUTO_DERIVE_BLACKLIST = {
    "Player",
    "Inanimate",
    "Mean",  # is a Faction (hostile temperament) but matches every English "mean"
    "SimpleGeneric",
    "WatervineFarmerConvert",
    "CannibalConvert",
    "IssachariConvert",
    "PigFarmerConvert",
    "JoppaFarmerConvert",
    "MechanimistPilgrim",
    "DromadTrader",
    "ConsortiumGlowpad",
    "StarappleFarmer",
    "PigFarmer",
    "CrabFarmer",
    "LeechFarmer",
    "CatHerder",
    "AmoebaFarmer",
    "SnailFarmer",
    "GoatHerder",
    "BeetleFarmer",
}


def _is_dup(name: str, entities: dict[str, list[str]]) -> bool:
    nl = name.lower()
    if name in entities:
        return True
    for pats in entities.values():
        for p in pats:
            if p.lower() == nl:
                return True
    return False


def build_entity_patterns() -> dict[str, list[str]]:
    entities: dict[str, list[str]] = {k: list(v) for k, v in SEED_ENTITIES.items()}

    def maybe_add(name: str):
        n = name.strip()
        if not n or len(n) < 4:
            return
        if n.lower() in STOPWORDS:
            return
        if n in AUTO_DERIVE_BLACKLIST:
            return
        if n.startswith("Base"):
            return
        if _is_dup(n, entities):
            return
        entities[n] = [n]

    # Faction names from INDEX
    fi = CORPUS / "factions" / "INDEX.md"
    if fi.exists():
        for m in re.finditer(r"^\| `([^`]+)` \|", fi.read_text(), re.MULTILINE):
            maybe_add(m.group(1))

    # Conversation IDs (both regular and hidden)
    for idx_path in [
        CORPUS / "conversations" / "INDEX.md",
        CORPUS / "conversations_hidden" / "INDEX.md",
    ]:
        if idx_path.exists():
            for m in re.finditer(r"^\| `([^`]+)` \|", idx_path.read_text(), re.MULTILINE):
                maybe_add(m.group(1))

    return entities


def make_match_regex(patterns: list[str]) -> re.Pattern:
    escaped = [re.escape(p) for p in patterns]
    return re.compile(r"\b(?:" + "|".join(escaped) + r")\b", re.IGNORECASE)


def safe_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]", "_", name)


def main() -> int:
    DST.mkdir(parents=True, exist_ok=True)
    # Wipe stale topic files (entity set may shrink between runs)
    for old in DST.glob("*.md"):
        old.unlink()

    entities = build_entity_patterns()
    print(f"Scanning corpus for {len(entities)} entities...")

    compiled = {name: make_match_regex(pats) for name, pats in entities.items()}

    # mentions[entity][category] -> list[(relpath, lineno, excerpt)]
    mentions: dict[str, dict[str, list[tuple[str, int, str]]]] = defaultdict(lambda: defaultdict(list))

    skip_filenames = {"INDEX.md", "BY_CONVERSATION.md"}
    total_files_scanned = 0
    total_matches = 0

    for subdir, category in CATEGORIES:
        d = CORPUS / subdir
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name in skip_filenames:
                continue
            total_files_scanned += 1
            relpath = f.relative_to(CORPUS).as_posix()
            with open(f, encoding="utf-8") as fh:
                for lineno, line in enumerate(fh, 1):
                    if not line.strip():
                        continue
                    for name, regex in compiled.items():
                        if regex.search(line):
                            excerpt = line.strip()
                            if len(excerpt) > 220:
                                excerpt = excerpt[:220] + "…"
                            mentions[name][category].append((relpath, lineno, excerpt))
                            total_matches += 1

    # Per-entity files
    index_rows: list[tuple[str, int, str]] = []
    for name in sorted(entities.keys()):
        ent_mentions = mentions[name]
        total = sum(len(v) for v in ent_mentions.values())
        if total == 0:
            continue
        fname = f"{safe_filename(name)}.md"
        out = [
            f"# Topic: {name}",
            "",
            f"_Aliases: {', '.join(repr(p) for p in entities[name])}_",
            "",
            f"_{total} mention(s) across {len(ent_mentions)} categor{'ies' if len(ent_mentions) != 1 else 'y'}._",
            "",
            "---",
            "",
        ]
        for subdir, category in CATEGORIES:
            mlist = ent_mentions.get(category, [])
            if not mlist:
                continue
            out.append(f"## {category} ({len(mlist)})")
            out.append("")
            for relpath, lineno, excerpt in mlist[:50]:
                out.append(f"- `{relpath}:{lineno}` — {excerpt}")
            if len(mlist) > 50:
                out.append(f"- _… {len(mlist) - 50} more mentions in this category, see file directly._")
            out.append("")
        (DST / fname).write_text("\n".join(out), encoding="utf-8")
        index_rows.append((name, total, fname))

    # Master index — sorted by count desc, then by name
    index_rows.sort(key=lambda r: (-r[1], r[0].lower()))

    idx = [
        "# Topic Index — Master",
        "",
        f"_{len(index_rows)} entities with ≥1 mention. {total_matches} total mentions across {total_files_scanned} corpus files._",
        "",
        "_Sorted by mention count, descending. Per-entity files cap each source-category list at 50 entries (see file directly for the rest)._",
        "",
        "| Entity | Mentions | File |",
        "|---|---:|---|",
    ]
    for name, count, fname in index_rows:
        idx.append(f"| {name} | {count} | [{fname}]({fname}) |")
    (DST / "INDEX.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"OK: wrote {len(index_rows)} entity files + master INDEX to {DST}")
    print(f"     ({total_matches} total mentions across {total_files_scanned} files scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
