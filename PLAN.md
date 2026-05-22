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
- [x] **Episode 4: The Spindle — Gjaus, the Star-Tree** — written,
  ~3600 words, ~25 min runtime, ten sections. Saved to
  [`scripts/04_the_spindle.md`](scripts/04_the_spindle.md). First
  script with a **per-section visual-assets table** (wiki page links
  + YouTube footage URLs), per user request. Structure: Cold Open →
  Omonporch & Asphodel → The Names (Gjaus/Star-Tree/Blue Mother) →
  What It Is (Eater elevator to the vault of heaven) → What It Means
  (Templar metaphor / the Aphir "Girl in the Sky" story / the Sonnet)
  → The Barrier (magnetic field) → The Ascent (Mark of Death → Tomb →
  Herododicus entombs you → the golem creature) → Brightsheol & the
  Shomer (Middle-English gatekeeper; "Brightsheol is the dream") →
  What's at the Top (signal, Seraph, starship) → The Question
  (Iseppa). Teed up Brightsheol's interior + the final choice as Ep5.
- [x] **Episode 5: Brightsheol and the Coda — The Four Fates of Qud**
  — written, ~3800 words, ~26 min runtime, the series finale. Saved
  to [`scripts/05_brightsheol_and_the_coda.md`](scripts/05_brightsheol_and_the_coda.md).
  Per-section visual table points at the **downloaded** local assets
  in `corpus/visual_assets/05_brightsheol/`. Structure: Cold Open
  (crossing into Brightsheol) → The Dream-City → The Seraph Speaks
  (the confession) → The Arguments → "I Subsumed Them" (the payoff:
  Resheph admits he overrode the Rebekah + Barathrum scans) → The
  Four Fates (Covenant/Return/Accession/Starfarer) → The Coda (the
  Inheritor Godling + Fool of the Gyre, four variants) → What Became
  of the Nephilim → The Question (series close).
- [x] **Standalone one-off: The Hindren of Bey Lah — A Village Built
  on Fear** — written, ~3500 words, ~24 min, fully self-contained
  (deliberately NO Resheph/Spindle/series references). Saved to
  [`scripts/standalone_hindren_of_bey_lah.md`](scripts/standalone_hindren_of_bey_lah.md).
  Thesis: fear as a functioning social technology. Self-contained
  quest cluster (Petals on the Wind → Kith and Kin → Find Eskhind →
  Love and Fear). Cast: Hindriarch Keh (the fearful tyrant who
  weaponizes the exile system), Eskhind (the framed exile), Angohind
  (the aspiring detective), Warden Neelahind (arbiter + Eskhind's
  love). Visuals: 16 downloaded `06_bey_lah/` assets mapped per
  section.
- [x] **Standalone one-off #2: The Mopango — The Buried Watchers** —
  written, ~3500 words, ~23 min, fully self-contained, a DIFFERENT
  faction from Bey Lah. Saved to
  [`scripts/standalone_the_mopango.md`](scripts/standalone_the_mopango.md).
  Thesis: a society built on humility, inquiry, and care — the exact
  inverse of Bey Lah's fear. The mopango are consensus-governed
  archivist-contemplatives who worship a latent inner light (the
  Kasaphescence), abolished gender (ey/em/eir), build mobility aids
  for disabled members, adopt outsiders, "watch the past" by communing
  with relics, care for ancient confined beings they call "the
  children," and each live by a personal *credo* it is taboo to ask
  them to explain. Signature move: the script quotes three credos
  (Vivira's "Form needeth not follow function," Agyra's "Malice alone
  staineth the sanctity of questioning," Doyoba's "Suffering breedeth
  in still water") and obeys the taboo by refusing to explain them.
  18 downloaded `07_mopango/` assets mapped per section.
- [x] **Standalone one-off #4: Chavvah, the Tree of Life — One and
  Many** — written, ~3500 words, ~23 min, fully self-contained; a
  single ENTITY profile (not a faction). Saved to
  [`scripts/standalone_chavvah.md`](scripts/standalone_chavvah.md).
  Thesis: the rare collective consciousness whose deepest act of love
  is letting a member LEAVE. Chavvah is a sentient crystalline
  tree-city, "one and many" (Chavvah the many / dyvvrach the one),
  whose Selves are born holding two *sefirots* — *-then* (what it will
  become) and *-else* (what it will not). Its chimeling Tau, broken
  loose by a vision, chooses to "become -else" via the ritual of
  -elseing; a rootclimber carries her stilled chime down the taproot
  so she can secede into a waiting "greater mind-haven" — or sever
  that liaison (player fork, presented as a fork, never single canon).
  Built strictly on ChavvahPrime / ChavvahFrontChime / Tzedech /
  Santalalotze / TauNoLonger + the If,Then,Else quest. The Kabbalah
  reading (keter / sefirot / Tree of Life, Chavvah = Eve) framed as
  the script's reading of real in-game terms. Visuals: 15 `09_chavvah/`
  assets mapped per section.
- [x] **Standalone one-off #5: Joppa — The People of the Vine** —
  written, ~3500 words, ~23 min, fully self-contained; a PLACE/community
  profile (the starting village). Saved to
  [`scripts/standalone_joppa.md`](scripts/standalone_joppa.md). Thesis:
  the ordinary place is what all the cosmic struggle is *for* — a
  watervine-farming hamlet in the crack between the Great Salt Desert
  (Moghra'yi) and the rotting jungle, "the people of the vine," surviving
  on *just enough* water. Cast: Elder Irudad (host/memory-keeper), Mehmet
  (the wind-tasting dreamer), Nima Ruda (the elder's apothecary daughter
  who refuses to inherit leadership), Tam (the dromad who stopped
  walking), Warden Yrame ("I kill trouble"). Two player-determined forks
  handled as forks: the watervine crisis / Battle of Red Rock, and
  whether Joppa takes in the slynth refugees. STANDALONE: Argyve / the
  Barathrumites, the Six Day Stilt, and Irudad's Gyre/nephilim/
  Resheph-plague lore deliberately omitted; the watervine-eaters kept
  local ("girshlings," "a creature of plague"). Built on Irudad / Mehmet
  / Nima_Ruda / Tam / WardenYrame + HistoryofJoppa Vol 1-2 + the What's
  Eating the Watervine? quest. Visuals: 21 `10_joppa/` assets mapped per
  section.
- [x] **Standalone one-off #6: Golgotha — The Cloaca of the World** —
  written, ~3000 words, ~20 min, fully self-contained; a PLACE/horror
  profile (the trash-cavern and the disease it breeds). Saved to
  [`scripts/standalone_golgotha.md`](scripts/standalone_golgotha.md).
  Thesis: in a world obsessed with height and ascent, Golgotha is the
  counterweight — the cloaca, the place where everything the world
  discards ends up, and the death it offers (glotrot — tongue necrosis)
  is one of the quietest horrors in the game. 5 sections: Cold Open →
  The Descent → The Rotting Tongue → The Cradle of Agolgot → The
  Execrable Pilgrimage → The Cloaca of the World. Built on Mafeo
  (advice quote) + Corpus Choliys (glotrot book) + Irudad (Agolgot
  line) + JoppaWorld map data + More Than a Willing Spirit quest +
  decompile (Glotrot.cs effect strings; AgolgotColumn.cs zone-builder
  "cradle" display name). STANDALONE: Barathrumites / Grit Gate /
  waydroids kept generic ("a proving ground / travelers make to test
  themselves"); Agolgot's nephil/Gyre/chord nature omitted; glotrot ↔
  Rebekah connection omitted; kept "a sleeper" (not "vast sleeper" —
  unsourced). Visuals: 17 `11_golgotha/` assets mapped per section.
  Two review passes (self + cold-eye agent) applied 4 fixes: Mafeo
  ellipsis (restored omitted sentence), Irudad leading ellipsis (added
  `...`), cure-paraphrase boundary (blockquoted cleanly from corpus
  text), "vast sleeper" → "a sleeper."
- [ ] **Standalone one-off #7: Sparafucile** — pending (character study
  of the mute masked assassin/gunsmith).
- [ ] Future / bonus candidates: The Mechanimist Faith (scripture
  deep-dive), The Coven & Folk Clock, "How Qud Generates Its Own
  History" (M6 synthesis as a script), Haddas the tree-mayor of Ezra,
  character studies (Q Girl, Hortensa, Otho), Kyakukya/Oboroqoru.

---

## Implementation log

Append each session. Newest at top. Date in absolute form.

### 2026-05-21 (cont.) — Standalone place profile: Golgotha, the Cloaca of the World

User directed: write Golgotha + Sparafucile episodes (both with reviews),
then push all to remote.

- Corpus investigation: Golgotha's lore is deliberately thin in the corpus
  (it's a main-quest proving-ground, not a society or character study).
  Key sources: Mafeo (advice on visiting Golgotha), Corpus Choliys
  (physician's book with the glotrot disease entry — origin, progression,
  cure), Irudad (the "bilge hose of sleeping Agolgot" image), JoppaWorld
  map data (trash-chute levels + the Cloaca floor label), the More Than a
  Willing Spirit quest legend-template ("victorious and bathed in slime").
  Decompile supplements: Glotrot.cs (the three effect strings — contracted,
  rotting, rotted), AgolgotColumn.cs ("The cradle of Agolgot" display name
  + lair structure below the Cloaca).
- STANDALONE discipline: Golgotha is deeply entangled with the main quest
  (Barathrumites send the player there to retrieve waydroids for Grit Gate)
  and with the Gyre cosmology (Agolgot is a Girsh nephil with a "chord").
  Both threads are deliberately omitted. The proving-ground role is kept
  generic; Agolgot is "a sleeper" only. Glotrot's connection to Rebekah
  ("the rotting tongue" killed her in ep 3) is also omitted.
- Thesis: the dungeon that is a sewer; the death that takes your voice.
  Where other one-offs are about how people live, Golgotha is about where
  the world puts what it can't keep. Mood-piece and atmospheric place-horror
  by design — Golgotha's sourced lore is sparse, so it trades breadth for
  intensity.
- Two review passes:
  - Self pass: fixed "ungLorious" capitalization typo.
  - Background cold-eye agent (corpus + wiki canon-check): found 4 issues.
    Applied all 4: (1) Mafeo ellipsis restored full omitted sentence ("If
    you can cook..."); (2) Irudad quote given leading `...` (the sentence
    begins "This one covered in slick and..."); (3) cure-passage paraphrase
    boundary restructured — ubernostrum block-quote now starts cleanly from
    corpus text ("only the scarce ubernostrum tonic will cause it to
    regrow..."); (4) "vast sleeper" → "a sleeper" (no corpus/decompile
    source for Agolgot's size).
- Downloaded 17 Golgotha tiles into `corpus/visual_assets/11_golgotha/`
  (overworld + surface + trash chutes + Cloaca + shaft, Corpus Choliys,
  yuckwheat + honey + ubernostrum, brown sludge, girsh agolgot +
  girshling + agolmaggot, girshling corpse + sewage eel + slog of the
  cloaca, fuming vents). 162 total assets now across 11 episode folders.

### 2026-05-21 (cont.) — Standalone place profile: Joppa, the People of the Vine

User picked "Joppa" from a data-ranked shortlist of 3 candidate one-offs
(the recommendation was grounded in corpus mention-counts: Joppa topic
index = 92 lines + 2 dedicated History of Joppa books).

- Investigated the corpus: topic_index/Joppa (the full map), the two
  History of Joppa books (Vol 1 "the people of the vine" founding myth;
  Vol 2 the Ut yara Ux festival + warm apple matz), and the resident
  conversations — Irudad (the elder), Mehmet (the wind-tasting farmer),
  Nima Ruda (the elder's apothecary daughter), Tam (the dromad
  saltstrider), Warden Yrame — plus the What's Eating the Watervine?
  quest and the Joppa faction file.
- Thesis: in a game of god-machines and apocalypses, Joppa is the
  smallest thing — a watervine farm in the crack between the Great Salt
  Desert (Moghra'yi) and the rotting jungle — and it is what all the
  cosmic struggle is FOR. A humane "place & its people" portrait; the
  deliberate ordinary counterweight to the extraordinary societies of
  Bey Lah / mopango / Putus Templar / Chavvah.
- 7 sections: Cold Open → The Crack Between the Salt and the Jungle →
  The People of the Vine → The Elder and His Daughter → The Warden and
  the Wanderer → The Battle of the Vegetable → The Open Door → The Place
  Worth Saving.
- STANDALONE discipline: omitted Argyve / the Barathrumites (the
  main-quest gateway), the Six Day Stilt (a named destination), and
  Irudad's longer Gyre / Girsh-nephilim / Resheph-plague nodes; trimmed
  his "in the shadow of the Spindle" line so the Spindle isn't named;
  kept the watervine-eaters local ("girshling," "a creature of plague").
  The slynth appear only as displaced refugees seeking a home (no
  Chavvah / other options named). Two player forks (the Red Rock battle;
  accepting the slynth) presented as forks, never single canon.
- Review pass 1 (self, line-by-line vs. corpus): one quote-fidelity fix
  — "a creature of plague" → a *"creature of plague"* (Irudad.md:110 is
  "Creature of plague," no "a"). Everything else verbatim.
- Review pass 2 (background cold-eye agent, corpus + live-wiki canon):
  0 CRITICAL — no fabricated quotes, no canon errors, no
  player-outcome-as-canon, no self-containment leak, spelling clean,
  wiki consistent (it confirmed apple matz is Joppa's signature dish and
  the Ut yara Ux festival framing). One minor fix applied: softened the
  "lime and gallium" paraphrase to "lime, and maybe gallium" (Mehmet's
  corpus line hedges gallium with "mayhaps"). The cold-open
  two-paragraph join was verified as same-node contiguous text (not a
  splice) and left as-is.
- Downloaded 21 Joppa tiles into `corpus/visual_assets/10_joppa/` (the
  overworld + town, Irudad / Mehmet / Nima Ruda / Tam / Yrame, watervine
  / vinewafer / vinereaper / farmer, gnawed watervine, Red Rock,
  girshling + corpse, baboon, slynth, salt marsh, witchwood, starapple,
  the graveyard). 145 total assets now across 10 episode folders.

- **Standalone library now: 5 one-offs** (Bey Lah / fear, Mopango /
  care, Putus Templar / codified cruelty, Chavvah / the collective that
  lets a self go, Joppa / the ordinary place worth saving) + the 5-part
  Resheph series. **145 visual assets across 10 episode folders.**

### 2026-05-21 (cont.) — QC review round 3: cross-series consistency + edit validation + noun/number audit

User: "do another quality control review of the scripts you've written
so far" (third pass).

Since rounds 1-2 already hit per-script quote-fidelity/canon twice, this
round used three COMPLEMENTARY lenses the prior passes structurally
could not cover, spawned as 3 parallel agents:
- (A) CROSS-SERIES CONSISTENCY — read all 5 series scripts together and
  checked for inter-episode contradictions (every prior agent saw only
  one script in isolation).
- (B) EDIT VALIDATION + UNSOURCED-NARRATION SWEEP — confirmed the 19
  round-2 edits landed correctly, then swept the connective prose of all
  9 scripts for asserted-but-unsourced lore.
- (C) PROPER-NOUN + NUMBER AUDIT — spelling/capitalization consistency +
  every numeric lore claim vs corpus.

VERDICT: the 5-part series is internally consistent — no cross-episode
contradictions (triumvirate membership, Rebekah's death across eps 2↔3,
the Spindle's nature, the four Fates' Nephilim compact all agree). All
19 round-2 edits validated PASS (no regressions). Proper nouns and
numbers clean.

ONE real fix — an unsourced detail hiding in NARRATION (the kind a
quote-fidelity pass can't catch): **"ten thousand years"** (the span the
Seraph/Spindle has waited) appeared in eps 1, 4, 5 but is NOT in the
corpus. The corpus's term for this span is "THE SIDEREAL EON"
(Resheph.md:141: "THE SIDEREAL EON DRAWTH DONE, AND THE COVEN DOTH
RETURN"). Replaced "ten thousand years" → "a sidereal eon" in all three
(consistent + corpus-grounded). It was internally consistent across the
three episodes, so no prior pass flagged it — but it was an invented
figure stated as fact, a strict-evidence violation.

Agent findings VERIFIED AND REJECTED as false positives (cross-checked
against source before acting):
- "102 nodes of dialogue" (ep 5) — CORRECT; Resheph.md:11 declares "102
  node(s)" (agent A's raw count of 104 had included the 2 Start headers).
- "banana groves of the north" (ep 4) — CORRECT; the Spindle/Omonporch
  is canonically northerly (Otho.md:163 "journey to Omonporch far to the
  north"; The_Earl_of_Omonporch.md:27 "Travel north to the Spindle").
- "Grand-doe"/"Grand-Doe" and "Covenate"/"covenate" variants — NOT
  errors; each instance faithfully matches the speaker/source it quotes
  (the lowercase forms are verbatim book text).

Net: 3 edits across eps 1/4/5; all 9 scripts now triple-reviewed and
strict-evidence clean. Committed + pushed.

### 2026-05-21 (cont.) — QC review round 2: all 8 prior scripts (corpus + live-wiki)

User: "do another quality control review of the scripts you've written
so far."

Method: spawned 8 parallel cold-eye general-purpose agents (one per
script — Resheph series 1-5 + Bey Lah, Mopango, Putus Templar), each
doing line-by-line quote-fidelity vs. the corpus AND a live-wiki canon
cross-check, with the known prior-error spots flagged for regression
testing. Chavvah was excluded (just double-reviewed). Cross-checked the
agents' CRITICAL/MODERATE claims against source before accepting — 3
were downgraded on inspection (script 4's injunction "splice" is
contiguous source text, nothing omitted; script 8's cold-open "splice"
is identical verbatim text in both a book and a conversation file).

VERDICT: 0 fabricated/misattributed quotes across all 8 scripts. Both
prior known-fixed canon errors confirmed NOT regressed — the Eaters-of-
Earth vs. Cannibals distinction (scripts 1, 4) and Kasaphescence =
Mechanimist goddess of metal/order, not a mopango inner-light (script
7). The four Coda Fates remain a player menu, not single canon (5).
Self-containment holds on all three standalones.

Corrections applied — 19 edits across 7 scripts:
- **Script 1 (Resheph):** [CRITICAL] the InheritorGodling "yet lives…"
  beat was built on a topic-index TRUNCATION ARTIFACT — the in-game
  sentence is complete ("…yet lives within or outside of the boundaries
  of the Limen, but no word escapes its borders," InheritorGodling.md:81).
  The script had reframed it as a dramatic "the line trails off / the
  Coda will not finish the sentence." Rewrote to quote the full line and
  drop the false trail-off. [MOD] bracket-misquote "incise the mark on
  yo[urself…]" → "your body…" (Barathrum.md:324).
- **Script 2 (Barathrum):** [MOD] "killed by the Seraph for betraying
  his plan" overstated the corpus — rephrased to the corpus account
  (died of the rotting tongue; Resheph would not forgive her trespass
  nor let her return home; Barathrum.md:419,427). [MIN] Euclid quote now
  starts at the faithful sentence boundary ("It's a prattleplant…").
- **Script 4 (Spindle):** [MOD] restored the dropped third Putus Templar
  value to the Murmur's Prayer quote ("…and the total eradication of
  mutant sapience," MurmursPrayer.md:11). [MIN] restored the dropped
  "Welcome" to Asphodel's line; [MIN] leading ellipsis on the
  mid-sentence Barathrum injunction quote.
- **Script 5 (Brightsheol/Coda):** [MOD] reframed "two figures recount
  your story" → "one of two figures, which one depending on the path you
  walked" (the Godling and the Fool are a kill-vs-pacify FORK per wiki
  canon, not a duo; reframed without importing the precise wiki
  mechanic). [MOD] scoped the Nephilim "They lived…" quote to its actual
  source — the Covenant ending (InheritorGodling.md:119-121) — not the
  universal peace outcome.
- **Script 6 (Bey Lah):** [MOD] hedged "built more like deer-centaurs"
  → "they read more like deer-centaurs" (the centaur body-plan is
  inferred, not stated, in the cited corpus lines; wiki confirms it).
- **Script 7 (Mopango):** [MOD] "abolished gender" → "set gender aside"
  in two places (corpus: "a societal relic in which we see no current
  utility," Agyra.md:248); [MOD] hedged the scale-glow-as-inner-Light
  claim as the writer's read; [MIN] cold-open "each lives by a motto" →
  "each seeks" (corpus: "Some of our coterie yet seeketh theirs").
- **Script 8 (Putus Templar):** [CRITICAL→MIN] dual-attributed
  "(book/conversation: Templar Domesticant)" → single "(book: …)" (the
  four Newfather lines are identical verbatim in both sources — not a
  harmful splice). [CRITICAL→MOD] removed the unsourced gloss "the word
  means a domesticated servant" → "a name that suggests…". [MOD] §I "one
  former associate" (pre-asserted Une's §VI ex-Templar reveal) → "one
  masked warden." [MOD] Oudin "elsewhere as the holder of the outposts"
  → "in the same prayer" (both possessives are in the one Murmur's
  Prayer file). [MIN] softened the "reclamation = turning a captive into
  a Domesticant" causal claim to "a vocabulary of the reclaimed."

Deliberately NOT changed (rationale):
- **Script 3 (Rebekah):** the "Resheph would not forgive her" account is
  a properly-attributed Barathrum quote (named speaker + "(hidden
  conversation: Barathrum)" + disclosed node-split) — corpus-faithful.
  NOTE a real corpus-vs-wiki divergence: the wiki's published canon says
  Resheph FORGAVE Rebekah on her deathbed and her offense was theft of
  the Mark of Death — neither is in our corpus extract. Per strict
  evidence the script narrates Barathrum's account and does NOT import
  the wiki version. Left as-is, documented here.
- Minor paraphrase/style left as acceptable: "young bear" for "bruin"
  (narration paraphrase), "Grand-Doe" capitalization, the faundren-rhyme
  final-stanza framing.

Net: all 9 scripts now strict-evidence clean. Committed + pushed.

### 2026-05-21 — Standalone entity profile: Chavvah, the Tree of Life

User: "plan and implement the script for Chavvah the living city."

- Investigated the corpus first: ChavvahPrime (the main dialogue —
  physiology, Tau, the slynth, the -elseing ritual), ChavvahFrontChime
  (the chiming rock you touch to attune), Tzedech (the alien chime),
  Santalalotze (the symbiote — "economic symbiosis"), TauNoLonger (Tau
  after severance, five branches), and the If,Then,Else quest.
- Thesis: a collective consciousness whose deepest act of love is
  letting a member LEAVE — the inverse of the usual hive-mind horror.
  Completes a four-part thematic set on the individual vs. the
  collective: Bey Lah erases the one who leaves (fear), the Putus
  Templar erase the self into devotion (codified cruelty), the mopango
  let each self keep its own credo (care), and Chavvah — most radically
  — lets a self secede.
- Wrote a self-contained 7-section profile (~3500 words, ~23 min):
  Cold Open → The Sentient Place → Soft/Twofirm/Keter (the physiology)
  → The Chimes → Joining → The One Who Leaves (Tau) → The Ritual of
  -Elseing → The Question. The Kabbalah reading (keter / sefirot / Tree
  of Life; Chavvah = Hebrew Eve) is presented as the script's reading
  of real in-game terms, hedged — same handling as Episode 1's "Siach."
- STANDALONE discipline: the corpus's Barathrum/starclimb branch and
  the Gyredream/Gyre node are deliberately omitted; the "future shock"
  that breaks Tau loose is conveyed generically (no proper nouns). The
  collective Tau leaves FOR (canonically tied to Ptoh) is kept generic
  as "a greater mind-haven"; Ptoh is never named. Tau's fate is a
  player FORK (free her liaison vs. sever it), never a single canon.
- Review pass 1 (self, gap-coverage, line-by-line vs. corpus): caught
  and fixed TWO node-splices before they shipped — the cold-open quote
  (had joined `Name`:119 + `ManySelves`:127) and the §II Twofirm quote
  (had joined `Physiology`:135 tail + `Physiology2`:143). Re-cut both
  to single-node boundaries. Softened a §I overclaim (an invented
  prescriptive rule about which name to use) to the corpus-observable
  fact that the player addresses it both ways. Added a sourced capstone
  — the quest's Hagiograph "Beauty in subtraction! Pruner =name= cut
  the Tree of Life to a more aesthetic form" (If__Then__Else.md:13),
  attributed as the player-legend template.
- Review pass 2 (background cold-eye general-purpose agent, corpus +
  live-wiki canon cross-check — same review type that caught the
  Kasaphescence error on the mopango): verdict 0 CRITICAL / 0 MODERATE,
  NO EDITS REQUIRED. Independently confirmed every block quote is
  verbatim from a single corpus node (validating the pass-1 splice
  fixes), the physiology is faithful, the player-fork is a fork, the
  body leaks no Resheph/Spindle/Barathrum/Gyre/Ptoh, the Dyvvrach
  framing is consistent with wiki canon ("one of the chimes… mayor…
  questgiver" — the script's one-and-many framing does not contradict
  it), and the Kabbalah reading is properly hedged as interpretation.
- Downloaded 15 Chavvah assets into `corpus/visual_assets/09_chavvah/`
  (Dyvvrach, Eyn roj, the chiming rock, glowing soft, the crystalline
  root/taproot, Moon Stair, Tzedech, Tikva, Wandering tau, Taunolonger,
  the still crystal chime, Santalalotze, slynth, hexagonal crystal,
  crystalline halo). All 15 confirmed via the MediaWiki API before
  download. Visual table mapped per section.

- **Standalone library now: 4 one-offs** (Bey Lah / fear, Mopango /
  care, Putus Templar / codified cruelty, Chavvah / the collective that
  lets a self go) + the 5-part Resheph series. **124 visual assets
  across 9 episode folders.**

### 2026-05-20 (cont.) — Standalone faction profile: the Putus Templar

- Investigated first: Otho (the "Sons and Daughters," Eater-descent
  claim, slave pens), Murmur's Prayer (the three core values + the
  Murmurs' Festival + the diptych + Oudin), From Entropy to Hierarchy
  (Q Girl's ordered-vs-chaotic-violence thesis, the slave caste,
  "baptism in the blood of the reclaimed"), the Templar Domesticant
  ("Newfather!"), Une (the apparent escapee — blank Aegis, hurdy-gurdy),
  the two quests, the faction file.
- Thesis: cruelty CODIFIED into orthodoxy — ordered violence that
  reproduces, vs. the chaotic violence of the Gyre wights. A third
  distinct society-type after Bey Lah (fear) and the mopango (care):
  the Templar are PURITY + HIERARCHY enforced by ritualized cruelty.
- Wrote a self-contained 7-section profile. Bookended by the
  Domesticant ("Did I do well, Newfather?") and Une (the one who got
  out). Q Girl cited only as "a Qud scholar," Otho as "an observer";
  the main-quest siege role deliberately omitted to keep it standalone
  and unspoiled.
- Downloaded 14 Templar assets into `corpus/visual_assets/08_putus_templar/`
  (the holy rhombus banner, knight types, squires, the Fullerite Aegis,
  Warden Une, the Murmur's Prayer book). 109 total assets now. NB: no
  Domesticant or Murmur tile exists on the wiki — the visual table uses
  text overlays + squire tiles for those beats.
- Review pass 1 (self gap-coverage): quotes clean; the two big
  inferences (reclamation-as-capture-and-remake; Une-as-ex-Templar)
  are hedged as the game leaves them. Flagged for the agent: whether
  "Oudin" is the supreme Templar leader or a regional commander (§V
  currently says "the figure they all serve"). Review pass 2: cold-eye
  agent with wiki canon-check — verdict NEEDS-EDITS (minor), no
  misquotes, no canon contradictions. The agent CONFIRMED both big
  inferences against the wiki: Une *is* canonically an ex-Putus-Templar
  Murmur, and the hurdy-gurdy/Murmur's-instrument link is real — so the
  script was over-cautious. 3 fixes applied: softened §IV's
  "reclamation = capture-and-remake" overclaim to corpus-grounded
  language (the canonical newfather/newchild/gentling-mask mechanic is
  wiki-only, NOT in our corpus, so per the strict rule it stayed OUT of
  the body); scoped §V's "Oudin" to what the corpus actually says (a
  distant authority, nature unspecified); removed a leftover visual-cue
  placeholder. Result: READY. Committed + pushed (`3664659`).

- **Standalone library now: 3 faction one-offs** (Bey Lah / fear,
  Mopango / care, Putus Templar / codified cruelty) + the 5-part
  Resheph series. 109 visual assets across 8 episode folders.

### 2026-05-20 (cont.) — Comprehensive corpus+WIKI canon review of both one-offs

User asked for a comprehensive correctness review of the two one-offs
against the REAL lore (not just the corpus). Spawned two agents that
cross-checked each script against the live Caves of Qud wiki (via the
MediaWiki API with a browser UA). This caught a real canon error the
corpus-only passes had missed.

**Mopango — NEEDS-EDITS (1 hard canon contradiction):**
- 🔴 **Kasaphescence.** The script framed it as a mopango-private
  inner-light divinity ("no chosen people," "not in a temple/relic").
  WRONG: the Kasaphescence is one of Qud's most widely-worshipped
  deities — the Mechanimist goddess of metal and order ("the being
  from whom all metal was birthed... Anything that's ordered, She
  infuses" — Jacobo.md:167, verified). Rewrote §II to situate Her
  correctly (Qud-wide goddess of metal/order) and frame the mopango's
  distinctive *inner-light-through-knowledge* reading as their own
  way of seeking Her. Cited Jacobo as "one of Her faithful elsewhere"
  (no arc-leakage).
- 🔴 "like every mopango, immediately forgives" — false; Yona ("simply
  making thee aware of thy foolishness") and Dadogom are sharp, and
  Vivira refuses if you call the taboo "ridiculous." Rewrote to quote
  Doyoba's actual forgiveness ("I was too harsh... I am not wroth")
  and note it's "the norm, if not quite universal," with Yona's cool
  counter (verified Yona.md:86,96).
- 🔵 restored "Nacham's past" (pointless redaction); 🔵 Vivira is a
  laser emplacement ("Lightspitter"), not a gun — fixed, harmonizes
  with "By Her Light."

**Bey Lah — READY (canon-accurate).** The agent verified Keh/Kindrish/
exile system, the Eskhind↔Neelahind romance, the misgendered sibling,
the lah lifecycle, and the multi-ending design all against the wiki —
all correct. Applied the two optional 🔵 polish items: added a
corpus-grounded deer-centaur silhouette clause (Eskhind: "canters,"
"hooves stamp the packed earth") so viewers don't picture a biped;
and "two hindren" → "two faundren" (the rhyme's own word).

Lesson logged: corpus-fidelity ≠ canon-fidelity. The wiki cross-check
is now part of the comprehensive-review step.

### 2026-05-20 (cont.) — Re-review of Bey Lah (READY) + standalone #2: the Mopango

- Re-reviewed the final Bey Lah script with a fresh cold-eye agent at
  the user's request: verdict **READY** — all four prior corrections
  confirmed correct, every blockquote verbatim, outcomes a menu, fully
  self-contained. No further edits.
- Picked a DIFFERENT faction for a second standalone: **the mopango**
  (19 source files, two own quests, dedicated NPCs). Deliberately the
  thematic inverse of Bey Lah — humility/inquiry/care vs.
  fear/isolation; consensus vs. gerontocracy; gender abolished vs.
  gender-policed; adoption vs. erasure.
- Investigated first: Vivira (the gentle chain-turret guard), Agyra
  (the hospitable spokesperson), Doyoba (keeper of the "child" Nacham),
  Zothom (the outsider's description), and the two quests.
- Wrote a self-contained 7-section essay. The Tomb of the Eaters is
  named only as the mopango's home; the Eaters/Sultans/Resheph plot is
  NOT explained, keeping it standalone and distinct from the series.
- Downloaded 18 mopango assets into `corpus/visual_assets/07_mopango/`
  (added the topic to `download_wiki_assets.py`; 95 total assets now).
- Review pass 1 (self gap-coverage): 4 fixes — preserved the in-game
  spelling "acquaintence"; corrected "granteth"→"grants" (Agyra
  relaying Lebah); 🔴 fixed a misattribution (the "An thou sendest void
  away..." line is Doyoba's, not Agyra's); fixed a visual-table
  filename (Kgoninon.png). Review pass 2: cold-eye verification agent
  — verdict NEEDS-EDITS, all minor: two verbatim quotes silently
  dropped the word "me" ("kept [me] safe and fed [me]"; "uplifted
  [me]... cared for [me]"), restored; and "they describe themselves as
  glowing" overstated a stage direction, softened to "described... as
  glowing softly." Agent confirmed everything else clean: all three
  credos + correct speakers, the corrected Doyoba attribution, the
  "grants freedom" relayed-claim framing, the credo-taboo restraint,
  player-choice neutrality, ey/em pronoun usage, and full
  self-containment (no Resheph/Spindle/Bey-Lah leakage). Result: READY.

### 2026-05-20 (cont.) — Standalone one-off: the hindren of Bey Lah

- User asked for a one-off episode unrelated to the Resheph arc,
  watchable on its own — suggested an interesting faction. Surveyed
  candidates; picked the **hindren of Bey Lah** (105 Bey Lah mentions,
  rich + clearly standalone: its own quest cluster, zero main-quest
  connection).
- Investigated first: the two culture books (Fauns of the Meadow, by
  the hunter-scholar Kaylenn Sand-Shell; Blood and Fear, by Chef Agate
  Severance Star), the four quests, and the key NPCs (Hindriarch Keh,
  Eskhind, Angohind). Core finding: hindren culture is built on
  *cultivated* fear — they fear outsiders ("kendren"), fear each
  other, and their staple crop (the lah plant) is itself a
  fear-weapon grown from "blood and fear." Plus a brutal exile system
  (leavers are erased, called "the dead") and a corrupt Grand-Doe who
  frames an exile for stealing the heirloom Kindrish.
- Wrote a self-contained 9-section essay. Deliberately omitted the
  incidental "Resheph"-oath and "shadow of the spindle" lines that
  appear in Bey Lah texts, to keep the episode standalone.
- Downloaded 16 Bey Lah wiki tiles into `corpus/visual_assets/06_bey_lah/`
  (added the topic to `download_wiki_assets.py`; 77 total assets now).
- Review pass 1 (self gap-coverage): every quote verified against the
  sources; clean. Review pass 2: cold-eye verification agent — verdict
  NEEDS-EDITS, one 🔴 + two 🟡, standalone-ness confirmed intact, all
  other quotes verbatim. 4 fixes applied:
  - 🔴 §VII spliced Eskhind's "ideal patsies" line (node `What are you
    saying?`, :112) with the "gerontocracy ensures..." line (node
    `You claim innocence?`, :124-126) — two mutually-exclusive
    branches — into one quote. Separated into two sourced exchanges.
  - 🟡 §VIII "close friends as children" is Keh's minimizing phrase
    (Keh.md:81), not the lovers' own. Re-attributed to Keh and
    contrasted with Eskhind's verified "We were close. More than
    close..." (Eskhind.md:341).
  - 🟡 §II fable paraphrase corrected (they ate from the field, then
    forgot to tend it).
  - bonus: strengthened §VI's gender-denial beat with Eskhind's now-
    verified counter, "I have no brother. My two sisters are all the
    blood family I can claim" (Eskhind.md:359).
  - Agent confirmed: no Resheph/Spindle/Barathrum/Rebekah/Coda
    reference anywhere in the body — fully self-contained.

### 2026-05-20 (cont.) — Visual assets DOWNLOADED + Episode 5 (finale)

- **Downloaded 61 wiki images** (the user asked for actual downloads,
  not links). The wiki blocks the WebFetch tool's UA, but curl/urllib
  with a browser UA over the MediaWiki `Special:FilePath` endpoint
  works (HTTP 200). Wrote `extractors/download_wiki_assets.py` — a
  curated per-episode downloader — and pulled tiles + screenshots
  into `corpus/visual_assets/{00_common_locations,01_resheph,
  02_barathrum,03_rebekah,04_spindle,05_brightsheol}/`. 736 KB total,
  all verified as real PNGs (visually spot-checked the Resheph statue
  and the Brightsheol gate). MANIFEST.md maps each file to its wiki
  source page. Updated Episode 4's visual note to point at the local
  files. Committed `3b4ebb1`.
- **Episode 5 (finale) written + reviewed.** Investigated the endgame
  hidden conversations first: Resheph (102 nodes — the full
  confrontation, the four decision branches, "I SUBSUMED THEM",
  "REMAIN AT THE SHEVA"), InheritorGodling + Fool (the Coda, four
  ending-variants each), Shomer (Brightsheol), Iseppa (close).
  - Review pass 1 (self): 3 fixes — softened a reconstructed
    "five Sultans/sixth" count; clarified the Starfarer fate comes
    via Barathrum's ship (not a Resheph decision-node option); and
    🔴 un-spliced a §VIII Fool quote that had combined two lines from
    DIFFERENT ending-variants (CovenantPC + ReturnPC) into one
    attributed string — a strict-evidence violation. Now presented
    as separate variant lines.
  - Review pass 2: cold-eye verification agent — verdict NEEDS-EDITS
    with only ONE 🔴 (the rest clean: all blockquotes verbatim, four
    endings presented as a player menu, Fool quotes correctly
    separated by variant, Starfarer correctly attributed to
    Barathrum's ship, no save-mechanics narrated). 3 fixes applied:
    - 🔴 §VII attached the verbatim "never vex the creatures of Qud
      again" compact to "three of four endings," but that exact
      pledge is only in Covenant + Starfarer (two). Return has a
      different compact (ally to banish Resheph); Accession is an
      alliance to doom the world. Corrected to "two," with a note on
      the others. (Cross-checked against InheritorGodling.md:73, 137,
      199, 259 myself.)
    - 🔵 cold-open clipped "the Seraph dremen." — dropped the
      sentence-final period on the mid-sentence fragment.
    - 🔵 restored "of the Spindle" inside the Iseppa quotation
      (verbatim fidelity) while keeping the generalizing gloss.
  - Result: the finale is citation-clean. Series complete (5 of 5).

- Investigated the Spindle corpus before drafting (concordance: 115
  mentions). Read the key new sources: Asphodel (the self-proclaimed
  Earl), Shomer (the Middle-English Brightsheol gatekeeper),
  GolemOperatingManual, TeleporterOrbs ("The Girl in the Sky"),
  Iseppa (the philosophical reflection), the Tomb-of-the-Eaters and
  Earl-of-Omonporch quests. Reused Barathrum + Haddas from Eps 2-3.
- **Key lore consolidated:** the Spindle = an Eater-built elevator
  "to convey freight to and from the vault of heaven" (Barathrum);
  its names are Gjaus (Eaters) / Star-Tree / Blue Mother / Spindle
  (Haddas); it self-locks with a magnetic field; the ascent runs
  *down* through the Tomb of the Eaters and Brightsheol first;
  Brightsheol is "the dream" of the Seraph who dreams atop Gjaus
  (Shomer); a functioning starship sits at the top (Barathrum hidden).
- **Visual-assets request fulfilled:** added a per-section table
  mapping each of the 10 sections to wiki pages (Spindle, Omonporch,
  Asphodel, Tomb of the Eaters, Brightsheol, etc.) and YouTube
  playthrough footage. NB the wiki blocks automated fetch (403), so
  the table points at pages (which host the tile art) rather than raw
  image URLs; flagged for the editor to grab by hand. Wiki/YouTube
  used for B-roll ONLY, never as a lore source — narration is 100%
  corpus-sourced.
- Review pass 1 (self gap-coverage): one fix — removed an unsourced
  claim that Herododicus stands "at the top of the Tomb" (corpus only
  supports the "Entomb me → Brightsheol" dialogue, not his location).
- Review pass 2: cold-eye verification agent — verdict NEEDS-EDITS,
  no critical, all 8 blockquotes confirmed verbatim. 4 fixes applied:
  - 🟡 §VII conflated TWO separate Brightsheol routes (Herododicus's
    sarcophagus-entombment vs the Shomer's "heigh gate" via Resheph's
    burial chamber) into one false sequence. Decoupled; now presents
    them as the corpus does — two distinct routes sharing the
    "you must be dead" precondition. (Verified against
    `ImperialBiographer.md:104-157` myself.)
  - 🟡 §VII "the title Resheph is given elsewhere" (Saad) overclaimed
    — the only corpus instances are the *player* bluffing "Saad
    Resheph stands before you" and the Shomer denying it. Reframed.
  - 🔵 §IV Aphir quote bracket-edit reattached a pronoun ("them" =
    her eyes, not the people). Restored the full verbatim quote.
  - 🔵 §IV "vanished beneath it" softened to "disappeared from a
    grove in the Spindle's shadow" + attributed the star-belonging
    to the father.

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
