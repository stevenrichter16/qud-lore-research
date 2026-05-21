# The Spice Grammar Engine

> **What this is:** The recursive template-expansion engine that turns
> a string like `<spice.history.gospels.Celebration.LateSultanate.!random>`
> into a sentence like "climbed the burning belfries." Every named
> thing in Qud — relic names, tomb inscriptions, village proverbs,
> quest hagiographs — flows through this engine. Understanding it is
> understanding Qud's worldbuilding instrument.

---

## A worked example

The Watervine quest has this `Gospel` attribute (from [Quests.xml](../quests/What_s_Eating_the_Watervine_.md)):

```
At the bloody Battle of Red Rock, =name= fought the combined girshling
and baboon forces to liberate the villagers of Joppa. In =player.t's=
honor they <spice.history.gospels.Celebration.LateSultanate.!random>.
```

That `<spice...>` token gets resolved at quest-completion time by
[`HistoricStringExpander.ExpandString()`](../../qud-decompiled-project/HistoryKit/HistoricStringExpander.cs).
Concrete output for one playthrough:

> "At the bloody Battle of Red Rock, **Tobias** fought the combined
> girshling and baboon forces to liberate the villagers of Joppa. In
> **his** honor they **climbed the burning belfries**."

The bold tokens are filled in by three different systems:
- `Tobias` ← character creation
- `his` ← grammar substitution from the character's pronouns
- `climbed the burning belfries` ← spice expansion from
  `HistorySpice.json` lookup at path `spice.history.gospels.Celebration.LateSultanate`,
  picked at random from the list at that node

## The data: `HistorySpice.json` (2692 lines)

The Steam install ships a JSON dictionary of mythic raw material at
`~/Library/Application Support/Steam/.../Base/HistorySpice.json`. Its
top-level structure is:

```jsonc
{
  "spice": {
    "elements": {
      "glass": { /* see below */ },
      "jewels": { /* see below */ },
      "stars": { /* see below */ },
      // ...more elements
    },
    "history": {
      "gospels": {
        "Celebration": {
          "LateSultanate": [
            "climbed the burning belfries",
            "threw a <spice.objectNouns.!random> into the trash sea",
            "wrested from the liminal tiers of a shale-toppled spire"
          ],
          // ...other eras
        },
        // ...other gospel types
      },
      "relics": {
        "names": [
          "the <spice.itemTypes.*itemType*.!random> of the <spice.adjectives.!random> <spice.elements.*element*.adjectives.!random>",
          "*personNounPossessive* <spice.elements.*element*.adjectives.!random> <spice.itemTypes.*itemType*.!random>",
          // ...8 total templates
        ]
      }
    },
    "elements", "pronouns", "objectNouns", "itemTypes", /* ...other root namespaces */
  }
}
```

### Elements as the unit of mythic coherence

Each `element` (glass, jewels, stars, sky-bears, etc.) is a rich
node with 14+ properties:

```jsonc
"glass": {
  "professions":      [ "glassblower", "window maker" ],
  "materials":        [ "glass", "sand" ],
  "adjectives":       [ "glazed", "stained", "clear", "prismatic" ],
  "nouns":            [ "prism", "glass", "mirror" ],
  "nounsPlural":      [ "prisms", "glass", "mirrors" ],
  "practices":        [ "staring into mirrors", "staining glass",
                        "glassblowing",
                        "burying prisms under the earth" ],
  "murdermethods":    [ "by trapping <spice.pronouns.object.!random> in a prism",
                        "with a dagger made of <^.materials.!random>" ],
  "inspirationsVerbPhrase": [ "saw <entity.possessivePronoun> own reflection in a river",
                              "had a dream that <entity.subjectPronoun> was <^.practices.!random>" ],
  "quality":          [ "transparent visage", "sandy hair",
                        "mirrored eyes",
                        "reputation for murdering someone <^.murdermethods.!random>" ],
  "babeTrait":        [ "with its mouth full of <^.materials.!random>",
                        "with <^.nounsPlural.!random> on its eyes" ],
  "ravaging":         [ "shattering all the glass in the homes" ],
  "ruinReason":       "devastated by torrential glass storms",
  "ruinDescription":  "glass-swept knolls",
  "mythicalEvent":    [ "a *var* shattered in every home",
                        "a famous <^.professions.!random> completed work on a legendary *var*" ],
  "weddingConditions":[ "in a cathedral of stained glass",
                        "in a hall of mirrors",
                        "inside a colossal prism",
                        "during a torrential glass storm" ],
  "mythicalBattleVista":[ "curtained under a *var* lune" ]
}
```

When a Sultan's `element` is set to `glass`, *every* downstream story
about that Sultan can pull from this single node:
- Their **birth** ("a babe with <^.nounsPlural.!random> on its eyes") →
  "a babe with mirrors on its eyes"
- Their **murder method** in a tomb inscription
- The **conditions of their wedding**
- Their **inspiration verb phrase** before some mythic deed
- The **ruin description** if a city falls to them
- The **mythical battle vista** of one of their wars

This is why Qud's procgen feels *coherent* rather than random:
**one** element-roll constrains a *whole* downstream story to a
unified tonal palette.

## The expander algorithm

[`HistoricStringExpander.cs`](../../qud-decompiled-project/HistoryKit/HistoricStringExpander.cs)
has two main methods:

### `ExpandString(input, …)` — the outer loop

Finds every `<…>` token in the input string, repeatedly. Each match
gets handed to `ExpandQuery` for resolution. Recursion limit: 25
iterations ([line 414](../../qud-decompiled-project/HistoryKit/HistoricStringExpander.cs)).
That cap protects against infinite-loop spice (a template that
references itself, directly or transitively).

```csharp
// ExpandString (simplified):
while (match = Regex.Match(buffer, "<.*?>"); match.Value.NotEmpty;)
{
    string expanded = ExpandQuery(match.Value, entity, history, vars, nodeVars);
    buffer.Replace(match.Value, expanded);
    if (++iterations > 25) { Error("max recursion"); break; }
}
```

### `ExpandQuery(query, …)` — the resolver

Parses one `<…>` token and resolves it. Steps:

1. **Strip post-processors.** Tokens can end with `.capitalize`,
   `.article`, or `.pluralize`. These get noted and stripped:
   `<spice.foo.bar.capitalize>` → resolve `<spice.foo.bar>` then
   capitalize the result.
2. **Split on `.`.** `spice.history.gospels.Celebration.LateSultanate.!random`
   becomes `[spice, history, gospels, Celebration, LateSultanate, !random]`.
3. **Walk the JSON tree.** Starting at `HistoricSpice.root`, descend
   one key at a time. If the next key is `!random`, pick a random
   list element. If it's `entity$property`, look up a property on the
   current `HistoricEntitySnapshot`. If it's just a key, descend
   into the JSON.
4. **Apply post-processors** on the final value (capitalize, article,
   pluralize).
5. **Variable substitution.** `*element*`, `*itemType*`, etc. get
   replaced by values from the `vars` dictionary that the caller
   passed in (so a relic generator can inject `*element* = "glass"`
   before expanding).

### Failure handling

Two escape hatches when a path doesn't resolve:

- `_failureredirect` — a string that gets re-expanded as a fallback
  with the remaining path appended (line 173-183).
- `_staticfailureredirect` — a fixed fallback string (line 183-187).

This is how spice authors can write "if there's no specific entry
for X, fall back to Y" without writing every combination
explicitly.

### Relative paths: the `<^.foo>` syntax

[`HistoricSpice.cs:97`](../../qud-decompiled-project/HistoryKit/HistoricSpice.cs)
has a `ResolveRelativeLinks()` pass that runs at load time. It
rewrites every `<^.x>` (or `<^^.x>`, `<^^^.x>`) into an absolute
path based on the *position in the JSON tree where the token is
written*.

So inside `spice.elements.glass.murdermethods`, a token
`<^.materials.!random>` rewrites to
`<spice.elements.glass.materials.!random>`. This is why an element
can self-reference its own properties without knowing its absolute
path — keeps the data file compact and orthogonal.

### Entity context: `<entity.X>` and `<entity[ID].X>`

Tokens starting with `entity` reach back into the current
`HistoricEntitySnapshot` for properties:
- `<entity.subjectPronoun>` → "she" / "he" / "they"
- `<entity.name>` → "Resheph II"
- `<entity[ID-xyz].region>` → a specific other entity's property

This is how a tomb inscription about Resheph II picks up Resheph
II's actual pronoun and region, not some other Sultan's.

## Recursion in practice

Here's a real fragment that recurses 3 levels deep:

```
"weddingConditions": [
  "in a cathedral of stained glass",
  "in a hall of mirrors",
  "inside a colossal prism",
  "during a torrential glass storm"
]
```

Now if a sultan's `element` is `jewels` instead, the same template
position has:

```
"weddingConditions": [
  "adorned with <^.nounsPlural.!random> and <^.nounsPlural.!random>",
  "inside a colossal <^.nouns.!random>",
  ...
]
```

That second template recursively expands to e.g. "adorned with
emeralds and rubies." The same surface template — *wedding conditions
for a sultan* — yields tonally different output by virtue of which
element won the parent roll.

## Video angles

- **"One JSON file you can read in a coffee."** Show the actual
  HistorySpice.json file. 2700 lines, but mostly lists of evocative
  fragments. You can read through it in 20 minutes. Compare to the
  novel-length lore documents AAA RPGs ship with.
- **"Recursion as worldbuilding."** Walk one expansion step-by-step
  on screen — show the `<spice.foo>` template, show the JSON lookup,
  show the recursive call, show the final string. It's a small
  algorithm doing enormous work.
- **"The element abstraction is the magic."** Most of Qud's tonal
  coherence comes from a sultan rolling *one* element which then
  constrains 14 downstream properties to a single semantic field.
  This is a worldbuilding trick anyone could steal.
