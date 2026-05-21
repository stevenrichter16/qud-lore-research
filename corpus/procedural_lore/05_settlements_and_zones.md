# Settlements and Zones: What's Fixed, What's Rolled

> **What this is:** Why Joppa is always at the same coordinate, but
> the village of "Mopango Wells" doesn't exist in your friend's
> playthrough. The map's static skeleton vs. its procgen flesh.

---

## The hardcoded backbone

[`JoppaWorldBuilder.cs`](../../qud-decompiled-project/XRL.World.WorldBuilders/JoppaWorldBuilder.cs)
opens with 8 const-string ZoneIDs. These are the fixed
**story-load-bearing** locations:

```csharp
public const string ID_JOPPA       = "JoppaWorld.11.22.1.1.10";
public const string ID_GRIT_GATE   = "JoppaWorld.22.14.1.0.13";
public const string ID_EZRA        = "JoppaWorld.53.4.0.0.10";
public const string ID_SPINDLE     = "JoppaWorld.53.3.1.1.10";
public const string ID_GOLGOTHA    = "JoppaWorld.23.9.1.1.10";
public const string ID_BETHESDA    = "JoppaWorld.25.3.1.1.10";
public const string ID_TEMPLE_ROCK = "JoppaWorld.25.3.1.1.26";
public const string ID_COURT       = "JoppaWorld.53.4.1.1.10";
```

The format is `<world>.<X>.<Y>.<localX>.<localY>.<Z>` — overland tile
coordinate, then a sub-tile coordinate, then a depth-level. So Joppa
is always at overland (11, 22) at the top-most level (Z=10). The
Spindle is at (53, 3) at Z=10. Bethesda Susa is at (25, 3) with the
Temple Rock right next to it at the same coord but Z=26 (deeper down).

This is *why* the Spindle quest works the same way every playthrough,
why Barathrum is always under Grit Gate, why Mehmet is always in
Joppa. Plot-bearing geography is constant. The questline writers
could safely write quest text that says "travel to Bethesda Susa"
because Bethesda Susa is always at the same tile.

## The 16-biome terrain budget

[`QudHistoryFactory.cs`](../../qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs)
defines the percentage of the worldmap that each terrain type gets:

| Biome | % of map | Village modifier |
|---|---:|---:|
| Jungle | 24% | 1.0× |
| Saltdunes | 12% | 0.8× |
| DeepJungle | 10% | 1.0× |
| Mountains | 10% | 0.8× |
| Hills | 9% | 1.0× |
| Water | 8% | 0.8× |
| DesertCanyon | 7% | 1.2× |
| MoonStair | 4% | 1.0× |
| Flowerfields | 3% | 1.2× |
| LakeHinnom | 3% | 1.2× |
| Ruins | 3% | 1.0× |
| Saltmarsh | 2% | 1.4× |
| Fungal | 2% | 1.2× |
| PalladiumReef | 2% | 1.2× |
| BaroqueRuins | 2% | 1.0× |
| BananaGrove | 1% | 1.0× |

These constants are why every Qud world *feels* like the same world:
the salt marsh is always small (~2%), the jungle always huge (~24%),
the Banana Grove always vanishingly rare (~1%). The seed varies the
exact placement but not the macro-budget.

The village modifier biases settlement density per biome — fertile
Saltmarsh gets 1.4× more villages than its 2% share would suggest;
arid Mountains get 0.8× fewer.

## The settlement layers

The worldgen builds settlements in *three distinct passes*:

### Pass 1: hardcoded
The 8 ID-constants above. Placed at fixed (X, Y, Z). Each gets its
own zone-builder class (e.g., `Joppa` is built by a Joppa-specific
ZoneBuilder that places Mehmet, the watervine farm, Argyve's hut).

### Pass 2: village-from-history
~28 villages are rolled by `GenerateVillageEraHistory` (see
[`02_sultan_history_generation.md`](02_sultan_history_generation.md)).
Each village exists in the *history first* — as a `HistoricEntity`
with founding year, founding sultan, biome, proverbs, gospels —
*before* the map exists. When the map gets built, villages get
**placed into matching terrain** by `JoppaWorldBuilder.AddVillages`.

This is the inversion that makes Qud's villages feel real: they have
a backstory before they have a location. The map is the last layer,
not the first.

### Pass 3: lairs, ruins, secrets, dynamic quests
[`JoppaWorldBuilder.BuildMutableEncounters`](../../qud-decompiled-project/XRL.World.WorldBuilders/JoppaWorldBuilder.cs) at line ~400 runs
this sequence:

```
BuildStep("Creating sultan entries",       JournalAPI.InitializeSultanEntries)
BuildStep("Recording sultan aliases",      RecordSultanAliases)
BuildStep("Placing historic sites",        AddSultanHistoryLocations)
BuildStep("Renaming sultan tombs",         RenameSultanTombs)
BuildStep("Placing lairs",                 BuildLairs)
BuildStep("Placing lairs",                 AddNephilimLairs)
BuildStep("Placing villages",              AddVillages)
BuildStep("Placing secrets",               BuildSecrets)
BuildStep("Generating dynamic quests",     BuildDynamicQuests)
BuildStep("Placing clams",                 PlaceClams)
BuildStep("Requiring faction heirlooms",   Factions.RequireCachedHeirlooms)
BuildStep("Creating gossip",               JournalAPI.InitializeGossip)
BuildStep("Creating observations",         JournalAPI.InitializeObservations)
```

Each `BuildStep` is wrapped in `try`/`catch` so a failure in one
step doesn't kill world-gen. The order matters: sultan entries
exist before the lairs that reference them; lairs exist before
villages (so villages can be placed *away* from lairs); villages
exist before secrets (because secrets reference villages).

## The Nephilim Lairs

`AddNephilimLairs` (mentioned in the BuildMutableEncounters list
above) is the wedge of *lore-driven* lair placement. The Nephilim
are the seven plagues / Girsh titans that Resheph drove under the
earth a chiliad ago (see [`Irudad.md`](../conversations/Irudad.md)).
These lairs are placed with story significance — the player can
hunt them as endgame content. Look at the conversations referencing
"nephilim" or "Girsh titan" in the corpus
([`corpus/topic_index/Girsh.md`](../topic_index/Girsh.md))
for the in-fiction framing.

## Where things go wrong: zone-builder failures

`try`/`catch` around each `BuildStep` means a failing builder doesn't
crash the world — it just produces a world *missing* that feature.
Run-to-run variability in Qud sometimes includes missing villages or
absent lairs because of this. Worth noting if your video does a
"weirdness in worldgen" segment.

## The local-map layer

Below the overland (80×25 tile worldmap) is a per-zone local map
(roughly 80×25 character tiles per zone, generated by per-zone
ZoneBuilder classes). Settlements like Joppa have hand-authored
local-map blueprints (in `prototypes/sultan map prototypes/` in the
Steam install). Procgen settlements use parametric local-map
generators. This is mostly outside the scope of "history generation"
but worth mentioning for completeness — it's the other half of
"what makes Qud's worlds unique."

## Video angles

- **"The skeleton and the flesh."** Show the hardcoded 8 locations as
  a fixed map skeleton. Then show villages dropping into matching
  biomes per playthrough. The skeleton is the plot. The flesh is the
  ambiance.
- **"The biome budget."** A single table (the one above) controls
  what every Qud world will *feel* like, because it constrains the
  macro-distribution of terrain. Compare to how Minecraft tunes its
  world.
- **"Lairs after villages."** The build-order matters: lairs first,
  villages placed away from them. Subtle but causes the
  "civilization vs. wilderness" texture of Qud's overland map.
- **"What's missing from `Worlds.xml`."** Earlier-noted gap: named
  settlements aren't in Worlds.xml because they're in *code*. This
  essay closes that gap. Visualize where they live: in the
  `JoppaWorldBuilder.cs` file as constants. That's *the source of
  truth* for what's in the world.

## What this doesn't cover

- **Cave systems & deep-Z generation.** The Z-axis below the overland
  is its own can of worms (Strata builder, depth-dependent encounters).
- **Tzimtzlum, the clam world.** A separate plane with its own
  builder. Worth its own video.
- **The Coda / endgame zones.** Hand-authored, plot-load-bearing.
  Different topic; see [`corpus/conversations_hidden/InheritorGodling.md`](../conversations_hidden/InheritorGodling.md).
