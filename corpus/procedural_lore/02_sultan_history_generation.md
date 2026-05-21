# The Sultan History Generator

> **What this is:** A deep dive on the 5-Sultanate, 6000-year-each
> timeline that gets generated at the start of every Qud world. Every
> Sultan's name, their dynasty, their region, their tomb's location,
> and the eight major life-events that fill out their biography are
> rolled here. Then the spice engine fills in the prose.

---

## The 30,000-foot view

A new world begins with `QudHistoryFactory.GenerateNewSultanHistory()`.
The entrypoint creates an empty `History` (a timeline + a bag of
`HistoricEntity` objects) and loops 5 times:

```csharp
// QudHistoryFactory.cs:107-121
public static History GenerateNewSultanHistory()
{
    History history = new History(1L);
    InitializeHistory(history);
    List<int> spreadOfSultanYears = QudHistoryHelpers.GetSpreadOfSultanYears(6000, 5);
    for (int i = 1; i <= 5; i++)
    {
        GenerateNewRegions(history, Stat.Random(2, 3), i);
        GenerateNewSultan(history, i);
        history.currentYear += spreadOfSultanYears[i - 1];
    }
    AddSultanCultNames(history);
    AddResheph(history);
    return history;
}
```

Per loop iteration ("**period**"):
1. Roll 2-3 new regions for the Sultanate.
2. Generate a Sultan for the period.
3. Advance the clock by a random share of 30,000 years (the average
   is 6,000, but the spread varies).

After the loop, `AddSultanCultNames` registers Sultan-cult IDs for the
worship system (the `Mechanimist` faction has sub-cults per Sultan),
and `AddResheph` — the one fixed entity in the whole history — gets
appended.

## One sultan, in detail

`GenerateNewSultan(history, period)` ([QudHistoryFactory.cs:269](../../qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs))
does three things:

1. Create a `HistoricEntity` and run `InitializeSultan` on it.
2. Mark `isCandidate=true` (i.e. "still alive when era begins").
3. Roll an origin event: **20% chance `BornAsHeir`**, **80% chance
   `FoundAsBabe`** (`Stat.Random(0,4) == 0`).
4. Roll **8 life events** from a pool:

```csharp
// (rough transcription from QudHistoryFactory.cs:282-321)
for (int i = 0; i < 8; i++)
{
    int num = Stat.Random(0, 16);    // ← 17-way roll
    if (num == 0) ApplyEvent(new CorruptAdministrator(), …);
    if (num == 1) ApplyEvent(new CapturedByBandits(), …);
    if (num == 2) ApplyEvent(new InspiringExperience(), …);
    if (num == 3) ApplyEvent(new MeetFaction(), …);
    if (num == 4) ApplyEvent(new SecretRitual(), …);
    if (num == 5) ApplyEvent(new ChallengeSultan(), …);
    if (num == 6) ApplyEvent(new ForgeItem(), …);
    if (num == 7) ApplyEvent(new UnderWeirdSky(), …);
    if (num == 8) ApplyEvent(new LiberateCity(), …);
    // ... more (the rest of the 0-16 range)
}
```

Note: rolls 9-16 don't have visible branches in this slice, but the
17-way roll is doing weighted-by-omission — most cases produce *no
event*, so sultans naturally have varied event counts (some lives
quieter than others).

Each event class (`CorruptAdministrator`, `MeetFaction`, etc.) lives
in its own file in `XRL.Annals/` and overrides `Generate()` to set
event-properties (year of occurrence, gospel template, tomb
inscription template, etc.). The gospels and inscriptions are stored
as *unexpanded spice strings* — they only resolve to prose later, when
something needs to render them.

## The InitializeSultan event itself

[InitializeSultan.cs](../../qud-decompiled-project/XRL.Annals/InitializeSultan.cs) (80 lines, full file)
runs in the loop's "ApplyEvent" step and sets the Sultan's
properties:

```csharp
// InitializeSultan.cs:28-66
do
{
    int num = 0;
    bool flag = (parse(GetRegionalizationParameters.successorChance).in100() ? true : false);
    if (entitiesWherePropertyEquals.Count == 0) flag = false;   // no prev sultan to inherit from
    if (flag)
    {
        // Continue existing dynasty as successor: "Resheph II"
        HistoricEntity randomElement = entitiesWherePropertyEquals.GetRandomElement();
        text = randomElement.GetCurrentSnapshot().GetProperty("nameRoot");
        int num2 = int.Parse(randomElement.GetCurrentSnapshot().GetProperty("suffix"));
        if (num2 == 0) { num = 2; /* set the predecessor's name to "X I" */ }
        else { num = num2 + 1; }
    }
    else
    {
        // New dynasty: roll a fresh name from the "Eater" namelist
        do { text = NameMaker.MakeName(null, null, null, null, "Eater"); }
        while (history.GetEntitiesWherePropertyEquals("name", text).Count > 0);
    }
    value = ((num != 0) ? (text + " " + Grammar.GetRomanNumeral(num)) : text);
} while (history.GetEntitiesWherePropertyEquals("name", value).Count != 0);
```

In English:
- Roll a probability called `successorChance` (set per world).
- If it succeeds AND there's a previous Sultan: take their name root
  and increment the Roman numeral. Predecessor becomes "X I", new
  Sultan is "X II".
- Otherwise: roll a fresh name using the **"Eater"** naming context
  (so all Sultans are stylistically "Eater-named" — a tonal choice
  that ties the Sultanate to the Eaters of the People, the cannibal
  faction). The cosmology hint is subtle but real.

Then attributes get set:
- `type=sultan`
- `nameRoot`, `suffix`, `name`
- `period` (1-5)
- `isAlive=true`
- An **element**: `ExpandString("<spice.elements.!random>")` — picks
  glass, jewels, stars, sky-bears, etc. from `HistorySpice.json`.
  This element will *thematically* color all of this Sultan's later
  events, items, and tomb inscriptions.
- A **region** from the regions generated for this period.
- A **location** within that region (where the tomb will end up).
- Pronouns: `Grammar.RandomShePronoun()` — selects from she/he/they
  with whatever distribution Qud uses.

## After all 5 Sultans: Resheph

```csharp
// QudHistoryFactory.cs:119
AddResheph(history);
```

Resheph is the cosmologically significant exception. He's added by
hand to every world's history, AFTER the procedural Sultans. The
spice engine *will* still fill in some of his text (his tomb
inscription, for instance), but his existence, his role as the
"Seraph atop the Spindle," and the plagues he engineered are *plot*
— see [`corpus/conversations_hidden/Resheph.md`](../conversations_hidden/Resheph.md)
and [`corpus/topic_index/Resheph.md`](../topic_index/Resheph.md).

## The village layer (era 6)

`GenerateVillageEraHistory(history)` ([QudHistoryFactory.cs:123](../../qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs))
runs after the Sultanate timeline is complete. It:

1. Picks a "flipYear" from Resheph's properties (the year the
   Sultanate dissolved).
2. Walks every existing event and converts any embedded `gospel` or
   `tombInscription` to "sultanate calendar" formatting (so events
   say "In the 4th year of Resheph II's reign…" not raw years).
3. Generates 4 **Village Zero** entries (one per major founding
   biome: DesertCanyon, Saltdunes, Saltmarsh, Hills).
4. Generates the remainder of the ~28 villages, distributed across
   16 biomes by the percentage-of-worldmap constants (Saltdunes
   12%, Jungle 24%, etc.) with per-biome `villageModifier_*`
   multipliers.

Each village is a `HistoricEntity` with its own event chain:
- `InitializeVillage(Region, BaseFaction, ...)`
- 2 random "village events" from a pool of 7:
  `BecomesKnownFor`, `PopulationInflux`, `Worships`, `Despises`,
  `SharedMutation`, `NewGovernment`, `ImportedFoodorDrink`
- One `VillageProverb` event at the end (this is what gives every
  village a saying — see real examples in any village's NPC dialogue)
- 1-in-20 chance the village starts `Abandoned` (`ruinedVillagesOneIn = 20`)

## Where the output shows up in the corpus

- **Sultan tomb inscriptions** → at the Tomb of the Eaters (Omonporch)
  and the per-Sultan tombs placed by `AddSultanHistoryLocations`
- **Gospels in quest text** → see any [Quests/](../quests/) file with a
  `Gospel` section
- **Village proverbs** → spoken by villagers during conversations;
  see e.g. [`conversations/Mehmet.md`](../conversations/Mehmet.md)
- **Sultan cult names** → the Mechanimist faction's sub-cult worship
  attitudes
- **Historic relics** → see [`04_historic_relic_generation.md`](04_historic_relic_generation.md)

## Video angles

- **"The 8-event biography."** Every Sultan's life is 8 dice rolls
  from a fixed event vocabulary, then prose-skinned. This is a clean
  visualization: show the dice, show the events, then show the final
  rendered biography.
- **"Resheph is the exception."** Every other Sultan is rolled. The
  fact that Resheph is hardcoded — by name, by role, by mythic
  significance — tells you the entire game's plot in one technical
  detail.
- **"Naming by tone."** Sultans are named with the "Eater" namelist.
  Joppa villagers are named differently. The naming systems carry
  cultural signal.
