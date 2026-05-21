# How Qud Generates Its Own History

> **Video angle:** Most procgen games generate a *map*. Qud generates a
> *history* — five named Sultans, their reigns, their tombs, the
> villages founded under each, the proverbs those villages tell, the
> relics buried in their tombs. The map is downstream of the history.
> When an NPC tells you a rumor, that rumor was *invented* for your
> playthrough by a recursive grammar engine running over a per-world
> JSON of mythic raw material. This video walks the pipeline end-to-end,
> from boot to "an old man tells you a secret."

---

## The one-paragraph version

When you start a new game of Qud, the engine runs a function called
[`QudHistoryFactory.GenerateNewSultanHistory()`](../../qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs).
It creates an empty timeline, then loops five times — once per
**Sultanate** — generating a Sultan, their region, and an ~6000-year
reign. Each Sultan is a `HistoricEntity` (a serializable bag of
properties: name, dynasty, region, elements, pronouns, location of
their tomb). The Sultans then accumulate eight **random life events**
each — `BornAsHeir`, `CorruptAdministrator`, `MeetFaction`,
`SecretRitual`, `ForgeItem`, `UnderWeirdSky`, `LiberateCity`, and
others — that fill out their biography. Every text fragment those
events produce (a sultan's epithet, a tomb inscription, a relic name,
a village proverb) is composed at runtime by recursively expanding
templates from `HistorySpice.json`, a 2692-line dictionary of mythic
raw material organized by **element** (glass, jewels, stars, sky-bears,
etc.). At the end of the era, villages are placed in each region, and
their proverbs and gospels are likewise composed from spice. The
finished history is then handed to [`JoppaWorldBuilder`](../../qud-decompiled-project/XRL.World.WorldBuilders/JoppaWorldBuilder.cs)
which places hand-authored settlements (Joppa, Grit Gate, Six Day
Stilt, Bethesda Susa, the Spindle) at fixed coordinates, lays roads,
seeds villages from the history into matching terrain, and finally
runs `BuildSecrets` and `BuildDynamicQuests` to populate the world
with the rumors NPCs will trade you. From this point on, when an NPC
says "Sultan Resheph drove them back a chiliad ago," that's not a
hand-authored line — Resheph is the one exception, hardcoded into
every history; but the *chiliad ago* and the verb *drove back* and the
implied era come from the history that just got rolled.

## The pipeline, step by step

```
QudHistoryFactory.GenerateNewSultanHistory()
  ├── new History(year=1)
  ├── InitializeHistory() — adds initial Regionalize entity
  ├── loop 5 times:
  │     ├── GenerateNewRegions(2-3 per period)
  │     ├── GenerateNewSultan(period)
  │     │     ├── new HistoricEntity
  │     │     ├── ApplyEvent(InitializeSultan)
  │     │     │     ├── 30% chance: continue prev dynasty → "Resheph II"
  │     │     │     ├── else: NameMaker.MakeName(..., "Eater") → fresh name
  │     │     │     ├── pick random element ← <spice.elements.!random>
  │     │     │     └── place in random region
  │     │     ├── 20% chance: BornAsHeir, else FoundAsBabe
  │     │     └── 8x random events from {CorruptAdministrator,
  │     │         CapturedByBandits, InspiringExperience,
  │     │         MeetFaction, SecretRitual, ChallengeSultan,
  │     │         ForgeItem, UnderWeirdSky, LiberateCity, ...}
  │     └── currentYear += ~6000
  ├── AddSultanCultNames() — registers SultanCult1..5 for the religion system
  └── AddResheph()  ◀── HARDCODED. Resheph is canon in every world.

JoppaWorldBuilder.BuildMutableEncounters()
  ├── BuildStep("Creating sultan entries")
  ├── BuildStep("Recording sultan aliases")
  ├── BuildStep("Placing historic sites")
  ├── BuildStep("Renaming sultan tombs")
  ├── BuildStep("Placing lairs") + AddNephilimLairs
  ├── BuildStep("Placing villages")
  ├── BuildStep("Placing secrets")    ◀── per-world gossip seed
  ├── BuildStep("Generating dynamic quests")
  ├── BuildStep("Placing clams")
  ├── BuildStep("Requiring faction heirlooms")
  └── BuildStep("Creating gossip") + InitializeObservations
```

Each `BuildStep` is wrapped with `try`/`catch` so a single failure
doesn't kill world-gen ([JoppaWorldBuilder.cs:436](../../qud-decompiled-project/XRL.World.WorldBuilders/JoppaWorldBuilder.cs)).

## The four invariants (canon across all playthroughs)

Everything else is rolled per-world, but these are fixed:

1. **Resheph exists.** `AddResheph(history)` runs in
   [QudHistoryFactory:119](../../qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs).
   He is *the* one named figure who survives across playthroughs. The
   `<spice>` engine still generates his epithets and the specific text
   of his myths, but the entity is hardcoded.
2. **Five Sultanates.** `numSultans = 5`. Always.
3. **~6000 years per Sultanate.** `avgYearsInSultanate = 6000`. (The
   actual spread per Sultanate uses `QudHistoryHelpers.GetSpreadOfSultanYears`.)
4. **The hardcoded settlements.** Joppa, Grit Gate, Ezra, the Spindle,
   Golgotha, Bethesda, Temple Rock, and the Court are at fixed
   coordinates ([JoppaWorldBuilder.cs:26-40](../../qud-decompiled-project/XRL.World.WorldBuilders/JoppaWorldBuilder.cs)).
   Their existence and location are canon. *What's in them* mostly is too.

Villages (about 28 of them — `avgNumVillages = 28f`) are placed
dynamically, in terrain types matching biome percentages (Saltdunes
12%, Jungle 24%, etc.) that are themselves constants on
`QudHistoryFactory`.

## Why this matters for video scripts

Three angles:

1. **Qud's worldbuilding scales because it's combinatorial.** A
   hand-authored game has, say, 50 unique relics. Qud has *infinite*
   relics, all internally coherent: an item from Sultanate 3 will use
   adjectives, professions, and mythic events appropriate to *that
   Sultanate's element* (which might be "glass" or "jewels" or
   "stars"). The combinatorial space is enormous but every output
   sounds like it belongs.
2. **The fixed nodes are deliberate.** The fact that Resheph is
   hardcoded — and that the Spindle, Bethesda, Grit Gate sit at fixed
   coordinates — tells you what the *story* is. The procgen handles
   ambient texture; the fixed nodes carry the plot. The Spindle quest
   wouldn't work if the Spindle were placed randomly each playthrough.
3. **History generation is independent of map generation.** The five
   Sultans, their reigns, their relics, their gospels — all exist
   before the map exists. The map then *inherits* the history (their
   tombs go in matching biomes, their villages get placed in their
   regions). This inversion is the trick.

## Where the output shows up in the corpus

- **Hagiograph + Gospel templates** in [Quests.xml](../quests/INDEX.md)
  contain `<spice.history.gospels.Celebration.LateSultanate.!random>`
  syntax. Those get expanded at runtime.
- **Relic biographies** on every relic-tier item — the user never
  sees a relic without one.
- **Tomb inscriptions** for every Sultanate Tomb — these are
  attached to events on each sultan's `HistoricEntity` and surfaced
  when you read the tomb.
- **Village proverbs**, the one-line aphorisms attached to every
  procgen settlement, are generated by
  [`QudHistoryFactory.GenerateVillageEvent → VillageProverb`](../../qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs).

## What this video should NOT try to cover

- Combat math, mutations, ability trees — irrelevant to "how the
  world's history is built."
- The specific lore of Resheph and the Spindle — that's a separate
  video (see [`corpus/topic_index/Resheph.md`](../topic_index/Resheph.md)
  and [`Spindle.md`](../topic_index/Spindle.md)).
- Modding. Qud's spice-engine is moddable (HistoricSpice.cs:48-78
  loads mod overrides via JSON merge), but that's a developer angle.
