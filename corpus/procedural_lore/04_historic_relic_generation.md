# Historic Relic Generation

> **What this is:** How Qud generates a unique, biography-bearing name
> for every relic-tier item in the world. Names like *"the prismatic
> cudgel of the brittle glassblower"* or *"Tobias's stardust-mantled
> longblade"* are composed at item-generation time from a tiny set of
> templates and the sultan history. Every relic is tied to a specific
> sultan, region, and element.

---

## The 8 name templates

[`HistorySpice.json`](../../qud-decompiled-project/) at
`spice.history.relics.names` is a list of just 8 templates:

```jsonc
"names": [
  "the <spice.itemTypes.*itemType*.!random> of the <spice.adjectives.!random> <spice.elements.*element*.adjectives.!random> <spice.elements.*element*.nouns.!random>",
  "the <spice.itemTypes.*itemType*.!random> of the <spice.elements.*element*.adjectives.!random> <spice.elements.*element*.nouns.!random>",
  // ...
  "*personNounPossessive* <spice.elements.*element*.adjectives.!random> <spice.itemTypes.*itemType*.!random>",
  "*creatureNamePossessive* <spice.elements.*element*.adjectives.!random> <spice.itemTypes.*itemType*.!random>",
  "*creatureNamePossessive* <spice.itemTypes.*itemType*.!random>"
]
```

8 templates × thousands of combinations of element/adjective/noun =
effectively infinite, all stylistically coherent.

## The name-generation pipeline

[`RelicGenerator.GenerateRelicName()`](../../qud-decompiled-project/XRL.World/RelicGenerator.cs)
at line 131 is the dispatcher. The flow:

```csharp
public static string GenerateRelicName(string Type, HistoricEntitySnapshot SnapRegion, string Element, out string Article)
{
    if (SnapRegion != null)
        return GenerateRelicNameByRegion(Type, SnapRegion, Element, out Article);

    RelicNameContext["*element*"] = Element;
    RelicNameContext["*itemType*"] = Type;
    string Name = HistoricStringExpander.ExpandString("<spice.history.relics.names.!random>", null, null, RelicNameContext);

    // Resolve *personNounPossessive* — a possessive form of a generic person noun
    if (Name.Contains("*personNounPossessive*")) {
        string raw = HistoricStringExpander.ExpandString("<spice.personNouns.!random>");
        Name = (raw != "<spice.personNouns.!random>")
            ? Name.Replace("*personNounPossessive*", Grammar.MakePossessive(raw))
            : Name.Replace("*personNounPossessive*", "*creatureNamePossessive*");
    }
    // Resolve *creatureNamePossessive* — possessive of a generated creature name
    if (Name.Contains("*creatureNamePossessive*")) {
        Name = Name.Replace("*creatureNamePossessive*",
            Grammar.MakePossessive(
                NameMaker.MakeName(EncountersAPI.GetACreature(), ..., "Relic", ...)
            ));
    }
    QudHistoryHelpers.ExtractArticle(ref Name, out Article);
    return QudHistoryHelpers.Ansify(Grammar.MakeTitleCase(Name));
}
```

Three things to notice:
1. **Two paths**: with-region or without. The with-region path
   ([line 155](../../qud-decompiled-project/XRL.World/RelicGenerator.cs))
   appends `of <regionName>` to anchor the relic to a place.
2. **The `*var*` substitution pattern** — `*element*`, `*itemType*`,
   `*personNounPossessive*`, `*creatureNamePossessive*` are
   placeholders the relic generator fills in *before* spice
   expansion. This lets the templates be reusable across item types.
3. **`Grammar.MakeTitleCase`** — Title-cases the final string ("The
   Prismatic Cudgel" not "the prismatic cudgel"). Sets the visual
   register.

## Where the element comes from

The Element parameter isn't random in normal play — it comes from
the `HistoricEntitySnapshot` of a Sultan or region. So if your
playthrough's Sultanate 3 has element `stars`, all Sultanate-3-era
relics in your world will use star-themed adjectives and nouns. This
is **history → items** dataflow: items inherit their tonal palette
from when and where they were forged.

The exception is the bargain-bin generic path
(`GenerateRelic(int Tier, bool RandomName = false)` at
[line 180](../../qud-decompiled-project/XRL.World/RelicGenerator.cs)) which
just grabs a random entity's snapshot, then runs the with-snapshot
path.

## Special relic generators

Beyond the base name generator, RelicGenerator has hand-written
methods for specific lore situations:

- **`GenerateSpindleNegotiationRelic`** ([line 163](../../qud-decompiled-project/XRL.World/RelicGenerator.cs))
  — generates a relic with `likedFactions` and `hatedFactions`
  list-properties baked in, parameterized by spared/betrayed factions
  and the player's name. Used at the Spindle endgame: the relic
  *records* which faction the player favored. This is one of the few
  cases where a procgen item carries player-specific narrative
  consequence.

## Relic vs. unique item

Qud has both:
- **Unique items** (hand-authored in `ObjectBlueprints/Items.xml`,
  with fixed descriptions — see [`Items.md`](../items/Items.md))
- **Procgen relics** (no static blueprint; generated at runtime per
  this pipeline)

The unique items are story-load-bearing (Hortensa's mirror, the
amaranthine prism, the Repulsive Device). The procgen relics fill
in *ambient* world-density — every random tomb, every random
treasure pile, has a relic with a believable name and biography.

## What the player actually sees

The end result: examine any relic-tier weapon in your inventory and
you see something like:

> *The vitric blade of the brittle glassblower*  
> *A longblade, scratched glass curls along its haft.*  
> *Forged in the era of Resheph IV, in the Salt Marsh of the West.*

The first line is from the templates above. The second is the static
item description. The third is a tomb-line generated by walking the
relic's tied sultan-entity and rendering one of that sultan's life
events.

## Video angles

- **"Every relic carries the war it was forged in."** The element
  abstraction means a glass-era sultan's relics use *glass* words. A
  star-era sultan's relics use *star* words. Show the same item
  type — say, a longblade — generated against three different sultan
  contexts and watch the name shift palette.
- **"8 templates, infinite output."** Three lines of JSON ×
  combinatorial element vocabulary = the entire relic-naming layer.
  Compare to how a hand-authored RPG names items.
- **"The Spindle negotiation relic."** One special case where a
  procgen item *remembers* a player decision (faction spared/
  betrayed). Worth mentioning for completeness — it's the place
  procgen and narrative branching most explicitly intersect.

## Where to find examples in the corpus

There's no easy way to see *rendered* relic names in the corpus —
the corpus has the *templates* (`Items.md`) and the *static
descriptions*, but the runtime renders happen per-playthrough. To
gather concrete examples, do a real playthrough and grep the save
file's relic entries. The decompile path for that:
`The.Game.sultanHistory` → walk entities → call `GenerateRelic` on
each.
