# Caves of Qud — Lore Compilation for YouTube Video Scripts

**Living planning + implementation doc.** Update in the same commit as any
code or corpus change. Append to the implementation log; do not silently
edit history.

---

## Goal

Produce Elder-Scrolls-style deep-lore video scripts about Caves of Qud
(Freehold Games, 2015–ongoing). Target output: ~20-min YouTube essays
on individual topics (e.g. "The Spindle," "Resheph and Saad Amus,"
"The Mechanimist Faith," "How Qud Generates Its Own History").

To get there, this workspace builds a **searchable, readable corpus**
out of the game's authored data + procedural systems, plus an index
of external sources (wiki, dev commentary, Discord, etc.).

## Non-goals

- **Not** a fan-fiction or extension layer. We are reading what Qud
  already says, not adding to it.
- **Not** in the Caves of Ooo repo. The CoO project has its own original
  worldbuilding ([Palimpsest_Lore_Bible.md](../house_feature/caves_of_ooo/Docs/Lore/Palimpsest_Lore_Bible.md),
  RotChoir, Glassblown, Brine Communion, etc.) and we keep those
  IP-distinct from extracted Qud content.
- **Not** a game-mechanics doc. Mechanics only matter where they
  illuminate worldbuilding (e.g. the historic-relic part, the Sultan
  history generator).

## Why a separate workspace

`/Users/steven/qud-lore-research/` sits outside the CoO worktree.
Two reasons:
1. Keeps extracted Qud text (Freehold Games' copyright) out of the
   CoO repo. Even if all our usage is fair-use research, mixing
   them invites confusion later.
2. Allows the corpus to grow large (`Books.xml` alone produces ~50
   files; conversations will produce ~250+) without bloating CoO
   git history.

## Source data

| Source | Path | Status |
|---|---|---|
| Steam install (canonical XML) | `~/Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base/` | confirmed exists 2026-05-20 |
| Full decompile (C#, behavior) | `/Users/steven/qud-decompiled-project/` | code-only; useful for understanding history-generator + secrets + Markov systems |
| In-repo Qud subset | `caves_of_ooo/qud_decompiled_project/` | symlink, code-only, no XML data |

## Lore source map (read-priority order)

| File | Density | What's in it |
|---|---|---|
| `Books.xml` | ★★★★★ | 53 in-game books — myths, manuals, poetry, fragments |
| `Conversations.xml` | ★★★★★ | NPC dialogue trees, ~250 conversations |
| `HiddenConversations.xml` | ★★★★ | secret/late-game dialogue |
| `Quests.xml` | ★★★★ | hagiographs, gospels, quest narrative |
| `Factions.xml` | ★★★★ | faction descriptions + relations |
| `ObjectBlueprints/Items.xml` | ★★★ | flavor text on relics, weapons, books-as-items |
| `ObjectBlueprints/Creatures.xml` | ★★★ | creature flavor + culture tags + conversation refs |
| `Worlds.xml` | ★★★ | regions: JoppaWorld, Tzimtzlum, Interior, Coda |
| `Mutations.xml` | ★★ | mutation flavor / bearer descriptions |
| `Relics.xml` | ★★ | legendary items + linked descriptions |
| `ZoneTemplates.xml` | ★★ | procedural zone descriptions, semantic tags |
| `PopulationTables.xml` | ★ | named populations / cultural groupings |
| `Corpus/*.txt` | ★★ | real-world scholarly excerpts cited as in-world texts |
| `HistorySpice.json` | ★★★★★ | **2692-line mythic-grammar dictionary** organized by element (glass, jewels, stars, etc.) with 14+ properties each — the data side of [[03_spice_grammar_engine]] |
| `Naming.xml`, `Genotypes.xml`, `Bodies.xml`, `Skills.xml` | ★ | tertiary flavor; naming conventions reveal culture |
| `HiddenMutations.xml` | ★ | secret mutations |
| `SparkingBaetyls.xml` | ★ | baetyl chrysalis / sparking content |
| `ChiliadFactions.xml` | ? | unknown — investigate |

**Procedural lore** lives in C# under `XRL.World.WorldBuilders`,
`XRL.World.Parts.History*`, `HistoryKit.cs`. Worth a whole video on
*how* Qud authors its own mythology per-playthrough.

## External sources (need to gather separately)

- **Official wiki** — `wiki.cavesofqud.com` (most consolidated reference)
- **Dev commentary** — Brian Bucklew + Jason Grinblat: Roguelike
  Celebration talks, dev streams, podcast interviews, Patreon posts
- **Official Discord** — `#lore` channel + dev Q&A
- **Reddit** — `r/cavesofqud` lore threads
- **Playthrough-generated lore** — `secrets.json` exports from actual
  runs (Markov-rendered, not template form)

---

## Phases

### M1 — Workspace + Books extractor _✅ done 2026-05-20_

- [x] `/Users/steven/qud-lore-research/` scaffolded
- [x] PLAN.md committed (this file)
- [x] `extract_books.py` → **53 books** to `corpus/books/*.md` + INDEX
- [x] Sanity-checked `Skybear.md` (Song of the Sky-Bear, Middle-English
  pastiche) — prose intact, color codes stripped cleanly

### M2 — Conversations extractor _✅ done 2026-05-20_

- [x] `extract_conversations.py` → **203 conversations** to
  `corpus/conversations/*.md` + INDEX (201 unique files — see note below)
- [x] Inheritance policy: shallow (do not expand `Inherits=`); each file
  shows the parent ID so a reader can follow chains manually
- [x] Sanity-checked Mehmet (Joppa elder, 7 nodes), Barathrum (44 nodes —
  rich), Q_Girl, ConsortiumGlowpad
- [x] **Known issue**: 3 `<conversation>` elements share ID
  `BaseConversation` (Qud's XML-mod merge pattern). Current extractor
  emits last-write-wins. Acceptable: BaseConversation is the
  water-ritual scaffolding, useful but not lore-critical. Defer
  merge-on-collision for M5.

### M3 — NPC ↔ Conversation crosswalk _✅ done 2026-05-20_

- [x] `extract_npc_crosswalk.py` walks the `Inherits=` chain across
  `ObjectBlueprints/Creatures.xml`
- [x] Produced `corpus/npc_index/INDEX.md` (creature → conversation,
  sorted by conversation) and `BY_CONVERSATION.md` (reverse index)
- [x] **895 creatures** resolve to **176 distinct conversations** through
  the inheritance graph. The headline "221 direct ConversationID refs"
  from initial inspection was a floor — most creature objects pick up
  their conversation via `BaseAnimal`, `BaseHumanoid`, etc.

### M4 — HiddenConversations + Factions + Worlds + Quests + Items _✅ done 2026-05-20_

- [x] `extract_hidden_conversations.py` → **9 hidden conversations** with
  SPOILER banner per file. **Major finds:** Resheph (102 nodes!),
  Barathrum endgame Spindle-ascension (49 nodes + 7 conditional
  starts), InheritorGodling + PartialGodling (29 nodes each — the Coda
  ending content), Fool, Archon/Barathrum/Rebekah holograms, SpokenIonic.
- [x] **Refactored conversation rendering** into
  `_xml_utils.render_conversation_md()` — now handles `<start>`
  conditional entry points (which the M2 extractor missed). Re-ran
  M2; some files gained content from `<start>` nodes that were
  previously dropped (e.g. visible NPCs with state-gated greetings).
- [x] `extract_factions.py` → **83 factions** (relations data only;
  Factions.xml has no description prose — prose lives in Books,
  Conversations, Quests). Each file notes the cross-search hint.
- [x] `extract_worlds.py` → **5 worlds**: JoppaWorld (234 cells —
  the main map), NorthSheva (11 cells), Interior (7 cells — Golem,
  TempleMechaMkI/II, Mover, etc.), Tzimtzlum (clam-clock world),
  ThinWorld. Output is structural (cell + zone catalogs); see
  caveat below.
- [x] `extract_quests.py` → **28 quests** with Hagiograph + Gospel
  templates surfaced as headed sections (these are the canonical
  per-quest lore templates, e.g. Watervine quest's
  "In the month of =month= of =year=, =name= walked below the chrome
  arches…").
- [x] `extract_items.py` → **823 items** with descriptions, consolidated
  into `Items.md`, plus `Items_Books.md` (19 book-items cross-linked
  to `corpus/books/`) and `Items_Quest.md` (1 — see caveat).

**M4 caveats / structural limits discovered:**
- **Named settlements not in `Worlds.xml`.** JoppaWorld lists 17
  distinct cell types (EynRoj, LakeHinnom, MoonStair, OpalDuskwaters,
  PalladiumReef, YdFreehold, BaroqueRuins, Flowerfield, etc.) but the
  named *settlements* (Joppa village, Grit Gate, Six Day Stilt,
  Kyakukya, Bey Lah, Omonporch, Bethesda Susa) are placed by C#
  world-builder code, not XML. Need to read
  `XRL.World.WorldBuilders.*` in the decompile for that (slated for M6).
- **Quest items barely tagged.** Only 1 item in the corpus carries a
  `QuestItem` / `QuestStarter` tag (the Repulsive Device — Sheba's
  Hagadias's quest object). Other quest-relevant items (amaranthine
  prism, etc.) are referenced from quest scripts but not statically
  flagged. M5 cross-cutting index will resolve these by name.

### M5 — Topic index (cross-cutting) _✅ done 2026-05-20_

- [x] `extract_topic_index.py` — walks every corpus file once, scans
  each line against a compiled regex set of ~290 entities, emits one
  `corpus/topic_index/<entity>.md` per entity with mentions grouped by
  source category and short excerpts.
- [x] Entity set: hand-curated `SEED_ENTITIES` (~85 canon names with
  alias lists) ∪ auto-derived faction + conversation IDs, minus an
  `AUTO_DERIVE_BLACKLIST` (Player, Inanimate, Mean, base/farmer/herder
  scaffolding IDs).
- [x] **Results:** 292 entities with ≥1 mention, 3644 total mentions
  across 382 corpus files.
- [x] **Top 10 by mention count:** Barathrum (153), Spindle (115),
  Eskhind (106), Bey Lah (105), Slynth (89), Gyre (82), Grit Gate (81),
  Girsh (67), Joppa (67), Resheph (67).
- [x] **Master index:** `corpus/topic_index/INDEX.md` sorted by count
  desc → per-entity .md is the research dossier for that name.
- [x] Per-category mention list within each entity file capped at 50
  (the file itself directs reader to the source if more).

**M5 caveats:**
- **Idempotency.** Re-run wipes and regenerates all topic files. If
  any base extractor re-runs and changes content, re-run this too.
- **Remaining noise.** "Water" (59 — water-ritual + water-baron is
  real lore, but "water" matches everywhere) and "tinker" (32 — mostly
  real but lowercase noun is broad). Both kept because they're not
  blacklist-worthy yet; their topic files are still useful, just denser
  than a tighter-named entity.
- **Seed completeness.** Some seed entities returned 1 mention because
  the in-game spelling uses a variant we didn't list (e.g. Saad Amus
  is actually `Saad Amus-an` and the Sky-Bear is mostly called by his
  Middle-English name in `Skybear.md`). Future polish: add a "seeds
  with <2 mentions" report to surface coverage gaps.

### M6 — Procedural lore writeup _✅ done 2026-05-20_

- [x] Explore agent inventoried the 5 key systems in
  `/Users/steven/qud-decompiled-project/` and returned entry-point
  classes + methods. Verified ~6 of its claims directly against
  source.
- [x] Read entry-point files (full or substantial slices):
  `QudHistoryFactory.cs`, `InitializeSultan.cs`,
  `HistoricStringExpander.cs`, `HistoricSpice.cs`, `History.cs`,
  `RelicGenerator.cs` (top 220 lines), `JoppaWorldBuilder.cs`
  (top + lines 400-500), `WaterRitualSellSecret.cs`,
  `JournalObservation.cs`.
- [x] Confirmed a **major lore-data file** missed in earlier inventory:
  `HistorySpice.json` (2692 lines, 183KB) in the Steam install. This
  is the spice grammar's mythic raw material — organized by
  "element" (glass, jewels, stars, sky-bears, etc.) with 14+
  properties each (professions, ruinReason, weddingConditions,
  mythicalBattleVista, etc.).
- [x] Wrote 6 essays + INDEX in `corpus/procedural_lore/`:
  - `01_history_engine_overview.md` — synthesis/headline video
  - `02_sultan_history_generation.md` — 5-Sultanate, 6000-yr-each, 8-event biographies
  - `03_spice_grammar_engine.md` — the recursive template engine
  - `04_historic_relic_generation.md` — 8 templates × element abstraction
  - `05_settlements_and_zones.md` — fixed skeleton + procgen flesh
  - `06_secrets_and_water_ritual.md` — gossip-as-graph event system

**M6 headline findings:**
- **Resheph is hardcoded.** `AddResheph(history)` runs at
  [QudHistoryFactory.cs:119](../../qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs)
  after the 5 procgen Sultans are created. He's the one named figure
  who survives across playthroughs. Major narrative implication: the
  Spindle questline depends on him existing, so he had to be hand-placed.
- **Sultans are named via the "Eater" namelist** (`NameMaker.MakeName(..., "Eater")`).
  Subtle cosmology: the Sultanate is tonally tied to the Eaters of
  the People (cannibal faction). Probably worth a callout in a
  "naming-as-worldbuilding" video angle.
- **Every Sultan rolls an "element"** from `<spice.elements.!random>`
  which then constrains 14 downstream properties (their wedding
  conditions, their murder methods, their tomb inscriptions, etc.)
  to a single semantic field. This is the trick that makes Qud's
  procgen feel *coherent* rather than random.
- **The fixed-coordinate IDs reveal the plot.** Joppa (11,22), Spindle
  (53,3), Bethesda (25,3), Grit Gate (22,14), Golgotha (23,9) and
  others are hard-wired in
  [JoppaWorldBuilder.cs:26-40](../../qud-decompiled-project/XRL.World.WorldBuilders/JoppaWorldBuilder.cs).
  Story-load-bearing geography is canon; ambient settlements roll.
- **The biome budget is fixed.** Saltdunes always 12%, Jungle always
  24%, Banana Grove always 1%. Every Qud world feels like the same
  world at the macro level for this reason.

### M7 — External-source gathering

- [ ] Wiki scrape or local mirror (legal: structured for personal
  research only)
- [ ] Dev-talk transcript collection (Roguelike Celebration, GDC)
- [ ] Discord lore-channel export (if accessible)

### M8 — Video script drafts _🟡 in progress 2026-05-20_

- [x] **Episode 1: Resheph and the Plagues** — written + revised after
  two review passes. ~3500 words, ~24 min runtime. Saved to
  [`scripts/01_resheph_and_the_plagues.md`](scripts/01_resheph_and_the_plagues.md).
  Eight-section structure. Every quote sourced; closing beat cites
  `AddResheph(history)` at `QudHistoryFactory.cs:119`.
- [x] **Episode 2: Barathrum the Old — The Bear Who Failed** — written
  + strict-evidence revision applied. ~4000 words, ~24-25 min target
  runtime. Saved to
  [`scripts/02_barathrum_the_bear_who_failed.md`](scripts/02_barathrum_the_bear_who_failed.md).
  Eight-section structure. Teed up Rebekah as Episode 3.
- [x] **Episode 3: Rebekah and the Daughters of Exile** — written,
  two review passes applied under the strict-evidence rule. ~3900
  words, ~25 min target runtime. Saved to
  [`scripts/03_rebekah_and_the_daughters_of_exile.md`](scripts/03_rebekah_and_the_daughters_of_exile.md).
  Ten-section structure (Cold Open → What the World Was Told →
  What Barathrum Called Her → What She Served → The Betrayal →
  The Rotting Tongue → Where They Buried Her → The Daughters Who
  Tinker → Zothom and the Question of Grief → A Hologram at the
  End → The Question). Major discovery embedded: Ezra is the
  Eaters' funerary site (per Haddas the tree-mayor) and the
  Spindle was called "Gjaus" by the Eaters and "Star-Tree" /
  "Blue Mother" — context that reframes Rebekah's burial at Ezra.
  Teed up the Spindle itself as Episode 4.
- [ ] Episode 4 candidate: **The Spindle** — the artifact, the Star-Tree
  the Eaters called Gjaus, the Mark of Death, Brightsheol ascent.
  Material in [`corpus/topic_index/Spindle.md`](corpus/topic_index/Spindle.md).
- [ ] Future candidates: The Mechanimist Faith (75-page scripture
  deep-dive), The Coven & Folk Clock, The Coda (Inheritor Godling),
  How Qud Generates Its Own History (M6 synthesis as a script),
  Haddas the tree-mayor of Ezra (technically an Eater).

---

## Implementation log

Append each session. Newest at top. Date in absolute form.

### 2026-05-20 (cont.) — Independent fact-check of all 3 scripts (3 cold-eye agents)

Spawned three parallel verification agents — one per script — each
tasked with grepping the corpus to confirm EVERY quote verbatim and
flag any strict-evidence violation. Cross-checked the critical
findings against source myself before accepting. All three came back
NEEDS-EDITS. 14 corrections applied total.

**Script 1 (Resheph) — 5 fixes, incl. 2 critical:**
- 🔴 **Imperial Biographer beat was backwards.** The lines "The
  sultanate is dissolved / Resheph is dead" are PLAYER choices, not
  the biographer's. The biographer (Herododicus) actually *refuses*
  to believe the reign ended — "What a prodigious reign! Bless that
  Coiled Lamb!" Rewrote the beat to use him correctly (a deluded
  loyalist still waiting to canonize a Godhead who may be dead or may
  be atop the Spindle). NB: this error was introduced during the
  *previous* review pass — a good argument for fresh-eyes review.
- 🔴 **"Every Sultan including Resheph" namegen claim was wrong.**
  Resheph's name is hardcoded (`InitializeResheph.cs:24 string value
  = "Resheph"`), NOT rolled from the Eater list. Fixed to "every
  *other* Sultan"; this actually strengthens the §VI fixed-star point.
- 🟡 Mechanimist passage overclaimed: dropped "dominant religion of
  Qud, 70+ pages of canonical text." The books never say "Mechanimist"
  and name Resheph only ~twice across 76 pages. Reframed as
  preacher-sermons that invoke him + the sourced faction-worship fact.
- 🟡 SnailFarmer "didn't know the meaning" → "leaves as an open
  question" (the NPC only poses a rhetorical prompt).
- 🟡/🔵 "Healer of the seven plagues" → "Healer of the plagues of the
  Gyre"; "Eaters of the People" → corpus calls it `Cannibals`.

**Script 2 (Barathrum) — 4 fixes, 1 critical:**
- 🔴 **`Barathrum:Dead`/`Launched` states misattributed** to the
  Barathrum hidden file; they're actually in `Resheph.md:212,380,975`.
  The fate-is-open claim is true but the citation pointed at the wrong
  file. Re-attributed.
- 🟡 "He sheltered the Daughters of Exile" — unsourced; dropped.
- 🔵 Pax Klanq listed as apprentice — he's an outside contractor on a
  debt, not a disciple. Moved out of the apprentice list.

**Script 3 (Rebekah) — 5 fixes (quotes were 100% accurate):**
- 🟡 "Mechanimist faith" attribution — the word appears in none of
  script 3's cited sources. Re-grounded via the `factions:Mechanimists`
  +50 worship attitude with explicit citation.
- 🟡 Brightsheol→control-unit geographic chain stated as fixed fact;
  only "grave is the key into the tomb" is sourced (Zothom). Relabeled
  the rest as Episode 4 forward-reference.
- 🔵 "technically an Eater / by his own admission" — it's player-
  proposed; Haddas only concedes "I suppose so." Softened.

Both verification agents that checked quote-fidelity confirmed every
blockquote in all three scripts is verbatim. The problems were all in
the connective prose, not the quotations.

### 2026-05-20 (cont.) — Script 3 written + reviewed under strict-evidence rule

- Investigated Rebekah lore in corpus *before* drafting, per the
  rule. Primary sources: YlaHaj (Daughter of Exile at Ezra), Zothom
  (the Penitent at the gravesite), Barathrum hidden conversation
  (where the betrayal is recounted), and — a major find I almost
  missed — Haddas the tree-mayor of Ezra, who reveals Ezra is the
  Eaters' funerary site and that the Spindle was called *Gjaus*
  and *Star-Tree* by the Eaters. Also: a one-node `RebekahHologram`
  conversation in `HiddenConversations.xml`.
- Drafted with strict-evidence discipline from the start. Then ran
  two review passes (gap-coverage + cold-eye adversarial) before
  commit. 11 edits applied, including:
  - 🔴 "Rebekah told the orphic truth to a Seraph, then to a young
    bear" — she SERVED the Seraph, she TOLD the orphic truth to
    her apprentice. Fixed.
  - 🔴 "Sultanate's chroniclers — Resheph's own annal-keepers" —
    invented. Replaced with the passive construction the source
    actually uses.
  - 🔴 "Daughters are not at the grave because Rebekah's bones are
    sacred relics" — directly contradicts Yla Haj, who calls the
    gravesite sacred. Forced false contrast removed.
  - 🟡 "Two villagers do not agree on much" — they tell compatible
    stories with different emphases. Softened.
  - 🟡 Faction-file claim about Daughters' negative attitude toward
    Templar mixed up the feelings table and worship-attitudes table.
    Precision restored.
  - 🟡 "Stitch back together" misquotes Barathrum, who says "stitch
    something new." Fixed.
  - 🟡 Hologram-section: "more fragmented than Resheph's lines"
    overclaim — both are archaic compound-word register. Cut.
  - 🟡 Hologram-section: silently implied the hologram came from
    Resheph's thin-scan. Now: "the script will not connect this
    hologram to Resheph's triumvirate thin-scan or to any other
    origin point; the source does not establish that connection."
  - 🟡 "Resheph's people's grave-soil" — kinship inference removed;
    softened to "Eaters' grave-soil" with attribution.
- Final script ~3900 words, ~25 min runtime. Open-ended on
  Daughters-worship-Resheph-+50 question (declined to speculate
  why; flagged as a corpus open question).

### 2026-05-20 (cont.) — Script 2 strict-evidence revision

User called out a critical methodology failure: the draft of Script 2
re-committed the exact class of overclaim that Script 1's review pass
had just corrected — asserting a specific mapping from the triumvirate
(original archon + Rebekah + Barathrum) to the three Resheph personas
(Healer + Coiled Lamb + Above) as if the game text had stated it,
when in fact the source declines to specify which mind became which
persona.

**New standing rule** (saved to user memory as
`feedback_qud_script_strict_evidence`): for Qud lore scripts, nothing
goes into a script unless it comes directly from investigation of the
extracted corpus or decompiled code. No invented detail. No
identifications/mappings the source doesn't make. No fixed claims
about player-determined fates. Inference is permitted only when
labeled as inference.

**Edits applied to Script 2 under the new rule:**
- Cold Open: dropped "lit by lamps that have been burning for a
  thousand years" (source says "candle-dim," not "lamps"); dropped
  "Last alive of the bears who crossed the Homs Delta" (not in source);
  surfaced the prattleplant + codex + Signal as direct verbatim quotes
  rather than narrative reconstruction.
- Section II: removed "for both cultural and biological reasons; bears
  with paws like his are made for delicate work" (invented). Replaced
  with Barathrum's own first-person account of his arrival.
- Section III: removed dramatized "She included him" / "He said yes"
  reconstruction. Quoted the verbatim "Together we beseeched
  Resheph..." line instead.
- Section IV: rewrote the triumvirate-to-personas mapping. Now reads:
  "The game text does not tell you which of the three personae the
  Barathrum-scan ended up wearing. The inference is tempting,
  especially for the Coiled Lamb, but the source declines to spell it
  out." Removed "The Coiled Lamb sacrifices itself voluntarily. The
  image is exactly right" (interpretive overreach).
- Section V: removed "He carried the deceit because the deceit was
  load-bearing" reasoning. Replaced with: "The source does not say in
  so many words that this concealment was deliberate strategy versus
  simple exhaustion — only that it happened."
- Section VII: removed "left behind by the Eaters" attribution
  (source says functioning starship exists; doesn't specify origin).
- Section VIII: 🔴 rewrote "He died in a chrome grotto..." — Barathrum's
  fate is player-determined (`Barathrum:Dead` AND `Barathrum:Launched`
  are both branches in the hidden conversation file's state checks).
  New text acknowledges all branches.
- Production notes: added a strict-evidence reminder pointing to the
  user-memory rule.

Final script is ~4035 words, ~24-25 min runtime. Tonally tighter
than v1 because much of what was "atmospheric" was unsourced
embellishment and got cut.

### 2026-05-20 (cont.) — Script 2 written

- Wrote `scripts/02_barathrum_the_bear_who_failed.md`. ~3500 words,
  ~26 min target runtime (slightly long for the genre but the
  material is dense enough to warrant it; production notes flag
  tightening options).
- Eight-section structure mirroring Episode 1's shape: Cold Open →
  The Bear at the Arch → The Cub Who Crossed → The Orphic Truth →
  The Bargain → A Thousand Years of Shim and Solder → The
  Breakdown → The Starshiib → The Question.
- Tonal targets: don't make Barathrum a villain; treat him as the
  best person who could have been put in this position. The
  Starshiib chant (16 repetitions in the source file) lands as
  comic-tragic, not just comic.
- Teed up Rebekah as Episode 3 in the closing beat.

### 2026-05-20 (cont.) — Script 1 reviewed and corrected

Two review passes applied to `scripts/01_resheph_and_the_plagues.md`
before declaring it ready to record:

- **Pass 1 (self, gap-coverage):** found 5 issues. Most-significant:
  the script presented the *triumvirate → three personas* mapping
  (Healer=Rebekah, Lamb=Barathrum, Above=archon) as gospel when the
  game text never explicitly states it — it's a defensible inference
  but had to be marked as such. Also: missing Resheph's own
  first-person plague-engineering confession (`Resheph.md:1083` had
  it sitting right there); thin Section II that should include the
  Imperial Biographer's "Resheph is dead" crack; SIACH etymology
  overreached toward Kabbalistic *sefirot* when it should stick to
  *siyaḥ ha-saddeh*; Section IV closer was rhetorically weak.
- **Pass 2 (self, cold-eye adversarial):** found 5 more issues. The
  largest: 🔴 *Eaters conflation* — the script collapsed "Eaters of
  Earth" (the precursor civilization, of whom Resheph the Seraph is
  one) with "Eaters of the People" (a contemporary cannibal faction).
  These are distinct entities; the Sultanate's `"Eater"` namelist
  ties to the precursor, not the cannibals. Also: 🟡 "not ancient"
  overclaimed plague-engineering when Resheph admits some pre-existing
  afflictions were folded into the Gyre narrative after the fact; 🔵
  "only named figure in Qud's history" needed to specify "in the
  Sultanate history" since Barathrum + Mehmet are also canon across
  playthroughs.
- **8 edits applied** (some review items collapsed into one edit
  where they overlapped). Script is now ~24 min runtime, citations
  audit-clean. Production notes updated.

### 2026-05-20 (cont.) — First script written

- Picked Resheph as the first episode (Elder-Scrolls-archetype
  single-figure deep-dive, dense topic file ready, clean
  public-vs-hidden narrative arc with a real twist).
- Wrote `scripts/01_resheph_and_the_plagues.md` — 22-min runtime,
  six sections, every quote sourced. Production notes + visual
  wishlist + tone reminders included for the recording pass.
- The script naturally teases a Barathrum follow-up (episode 2)
  and Spindle / Rebekah / Mechanimist Faith / Coven / Coda as
  future episodes.

### 2026-05-20 (cont.) — M6 complete

- Explore-agent inventory of `/Users/steven/qud-decompiled-project/`
  for: Sultan history, historic relics, spice grammar, world
  builders, secrets system. Returned 5 systems with entry-point
  files + methods.
- Verified 6 of the agent's claims directly by reading the source
  files myself (per CLAUDE.md cross-check policy).
- Major discovery: `HistorySpice.json` (2692 lines) in Steam install
  is a lore-data file we missed in the M1 inventory. It's the
  mythic raw material the spice engine expands.
- Other discovery: `AddResheph()` is called from
  `GenerateNewSultanHistory()` after the 5-Sultan loop. Resheph is
  the **one** canon figure across all playthroughs. Every other
  Sultan rolls.
- Wrote 6 essays in `corpus/procedural_lore/`:
  - Headline synthesis essay (the "How Qud Generates Its Own
    History" video)
  - Deep-dives on Sultan history, spice grammar, historic relics,
    settlements, secrets+water-ritual
- Each essay cross-links to the C# source files and the relevant
  corpus categories. Each ends with explicit "video angles."

### 2026-05-20 (cont.) — M5 complete

- Wrote `extract_topic_index.py`: scan-and-index across all corpus
  categories. ~290 entities × 60k lines = 3644 mentions assembled
  into per-entity research dossiers in seconds.
- Curated seed list of ~85 canon names with alias variants (Sky-Bear
  has 3 spellings, Q Girl has 3, etc.).
- Auto-derive blacklist iteration: removed `Player` (matches every
  `=player.foo=` template), `BaseConversation` (Inherits references),
  `Mean` (faction whose name matches every English "mean"), and the
  templated farmer/herder/trader generic ConvoIDs.
- **Highest-value topic files for video research:** Barathrum,
  Spindle, Resheph, Eskhind, Bey Lah, Slynth, Gyre, Grit Gate, Joppa,
  Girsh, Barathrumites, Omonporch, Bethesda Susa, Q Girl, Otho,
  Argyve, Mehmet, Mopango.
- **Discovery enabled by the index:** Resheph's topic file alone
  reveals the full Spindle/plagues narrative arc: he's the Seraph who
  seeded the plagues to ready the world for the Coven's return;
  Rebekah was his tutor who betrayed his plan to help Barathrum; the
  Tomb of the Eaters has a flawed seal Resheph placed a thousand
  years ago. Complete 20-minute video script possible from
  `corpus/topic_index/Resheph.md` + the Hidden Conversations files
  it links to.

### 2026-05-20 (cont.) — M4 complete

- Refactored shared conversation rendering into
  `_xml_utils.render_conversation_md()`. Now handles `<start>`
  conditional entry nodes (Qud's pattern for state-gated greetings,
  e.g. Barathrum's Z-Ascended dialogue when `SpindleAscended` flag
  is set).
- Re-ran `extract_conversations.py` against `Conversations.xml`; some
  files now show `<start>` nodes that the M2 version was silently
  dropping. (BaseConversation triple-merge still last-write-wins.)
- New extractors: `extract_hidden_conversations.py`,
  `extract_factions.py`, `extract_worlds.py`, `extract_quests.py`,
  `extract_items.py`. All idempotent.
- Six output directories now: `books/` (53), `conversations/` (201
  unique files for 203 entries), `conversations_hidden/` (9),
  `factions/` (83), `worlds/` (5), `quests/` (28),
  `items/` (3 consolidated files for 823 items),
  `npc_index/` (2 files for 895 creatures → 176 conversations).
- **Top finds in HiddenConversations.xml:** Resheph (102 nodes,
  archaic majestic-2nd-person dialogue: "THOU ART SAT IN THE
  MOVEMENTS OF THE GREAT SIACH"); InheritorGodling + PartialGodling
  (the Coda endgame content, 29 nodes each); Barathrum's full
  Spindle-ascended farewell chain.
- **Structural limits noted:** named settlements aren't in
  Worlds.xml (they're placed by C# WorldBuilder code — defer to M6);
  quest items aren't reliably tagged — only 1 found via QuestItem
  tag (the Repulsive Device, Sheba Hagadias's quest object).

### 2026-05-20 — M1+M2+M3 complete

- Created `/Users/steven/qud-lore-research/` with `extractors/`,
  `corpus/{books,conversations,npc_index}/`, `scripts/`.
- Wrote PLAN.md, README.md.
- Confirmed Steam install path resolves; inventoried 30 top-level XML
  manifests in `StreamingAssets/Base/`.
- Wrote `_xml_utils.load_qud_xml()` shared loader. Qud XML files use
  two invalid-XML conventions that need preprocessing:
  - **CP-1252 numeric refs in the 0x80-0x9F range** (e.g. `&#148;`)
    used for curly quotes etc. on Windows. Mapped to proper Unicode.
  - **CP437 control-glyph refs** (e.g. `&#x7;` = the bullet `•`).
    These are illegal in XML 1.0 but Qud uses them to render CP437
    glyphs on its tilemap. Mapped to Unicode equivalents.
  Without this, ElementTree fails on `Books.xml` line 1091 col 6.
- `extract_books.py`: emitted 53 book files + INDEX.md. Densest:
  `Quotes` (34 pages), `HighSermon` (30 pages — Mechanimist
  scripture), `Preacher1-4` (8-11 pages each — sermons),
  `Across1-3` (the Sunderlies / Athenreach / Oth travelogue),
  `Canticles3`, `Lives1`, `EtaandtheEarthling1`.
- `extract_conversations.py`: emitted 201 unique conversation files
  (203 elements; 3 share BaseConversation as Qud's XML-merge pattern).
  Mehmet, Barathrum (44 nodes), Q_Girl, Hortensa, Jacobo, Neek all
  present and well-formed.
- `extract_npc_crosswalk.py`: walked Creatures.xml inheritance chain.
  895 creatures → 176 conversations. Wrote `INDEX.md` (creature view)
  + `BY_CONVERSATION.md` (reverse index — every creature that uses a
  given conversation, useful for "which speakers share dialogue").
- **Next**: HiddenConversations.xml (Sheba, Coda, Spindle endgame).
  Then Quests.xml — Spindle questline lives there as well.

---

## Open questions

- **Color-code stripping.** Qud uses `{{X|text}}` for inline color and
  `&y` style markers. Stripping to plain text loses emphasis but keeps
  prose readable. Current plan: strip, accept loss. Revisit if a
  specific video needs the formatting back.
- **`Inherits=""` resolution.** Most conversations inherit from
  `BaseConversation` (the water-ritual scaffolding). We will not
  expand inheritance in the per-conversation .md files — that would
  duplicate the same 50 lines into every NPC. Instead, dump base
  once at `corpus/conversations/_BaseConversation.md` and reference.
- **Procedural text fragments.** Conversations include placeholders
  like `=subject.T=`, `=verb:grab=`, `=mutation.name=`. These are
  rendered at runtime. For lore reading, leave them in — they're
  informative about the templating system.
- **Hidden content spoilers.** `HiddenConversations.xml` and the
  Coda content contain endgame spoilers. Mark those clearly in
  extracted files so they don't accidentally land in a beginner-level
  video.
- **BaseConversation merge.** Three `<conversation
  ID="BaseConversation">` elements exist (Qud's mod-style additive
  patching). M5 should merge them rather than last-write-wins, so
  the corpus file shows the full water-ritual scaffolding.

---

## Surprising findings (worth their own video each)

- **Middle-English pastiche.** `Skybear.md` ("Song of the Sky-Bear")
  is written in deliberate Chaucerian Middle English, telling the
  story of Saad Amus the Sky-Bear conquering Aldersesse and binding
  "starry Ptoh" in a tomb. This is canonical Qud lore in a chosen
  poetic register — Freehold is doing what Tolkien did with
  Anglo-Saxon. There's a whole video in: register choice as
  worldbuilding.
- **Mechanimist scripture is enormous.** Combined `HighSermon` (30
  pages) + `Preacher1-4` (~30 pages) + `Canticles*` ≈ 75 pages of
  in-universe religious text. This is roughly the volume of the
  shorter Pauline epistles. A "doctrine of the Mechanimist faith"
  video could be very deep on this material alone.
- **`Quotes.xml` is 34 pages of one-liners** — likely the source for
  the random-quote attributions you see at character-creation. These
  attribute lines like "— Q Girl" or "— from the Lost Histories of
  the Twin Hooks" are themselves world-building: implied books and
  named figures with no other appearance.
- **Resheph speaks in majestic-second-person archaic English.** The
  hidden conversation is 102 nodes of e.g. "THOU ART SAT IN THE
  MOVEMENTS OF THE GREAT SIACH, AND I BEFORE THEE. WHEREFORE ART
  THOU?" The choice of "SIACH" (Hebrew: meditation, discourse,
  reed/grove — also a mystical-network term in Kabbalah) is
  deliberate. Resheph is doing what an ancient unstrung mind would
  do: speaking in a register that the player's language barely
  contains. A whole video in: how Qud uses register-shifts to
  signal cosmic perspective.
- **Quest templates use a `<spice.history.gospels.*>` syntax** for
  procedural celebratory narratives. Cross-reference with Qud's
  procgen text builder (XRL.World.Text.HistoryGen) for the
  "How Qud Generates Its Own History" video.
