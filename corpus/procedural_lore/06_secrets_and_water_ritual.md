# The Water Ritual and the Secrets System

> **What this is:** When you complete the water ritual with an NPC,
> you can trade secrets and gossip for reputation. Those secrets
> aren't authored — they're a per-playthrough emergent map of who
> learned what about whom. This essay walks the data structures and
> the event-driven hooks that make it work.

---

## The water ritual in one sentence

You share water with an NPC, you both gain trust, and now they will
trade *information* with you: secrets they know (where a faction's
heirloom is buried, what a sultan did in a specific era, where a
ruin is) and gossip they've overheard.

## The data structure: `JournalObservation`

Every secret or gossip entry is a [`JournalObservation`](../../qud-decompiled-project/Qud.API/JournalObservation.cs)
in the player's journal. Fields:

```csharp
public long Time;          // when the player learned it
public string Category;    // "Gossip" or other category
public string RevealText;  // the text shown when first learned
public bool Rumor;         // true = unconfirmed, false = secret
// inherited from IBaseJournalEntry:
//   ID, History, Text, LearnedFrom, Weight, Revealed, Tradable, Attributes
```

When the player learns one, `Reveal()` ([line 123](../../qud-decompiled-project/Qud.API/JournalObservation.cs))
displays the text and files it under "Observations" in the journal
screen.

## The conversation hook: `WaterRitualSellSecret`

Every conversation that supports secret-trading uses
[`WaterRitualSellSecret`](../../qud-decompiled-project/XRL.World.Conversations.Parts/WaterRitualSellSecret.cs)
as a conversation `<part>`. From [`BaseConversation`](../conversations/BaseConversation.md)
in our corpus, you can see the choices:

```xml
<choice ID="ShareGossipChoice">
  <text>I have some gossip that may interest you.</text>
  <part Name="WaterRitualSellSecret" Gossip="true" />
</choice>
<choice ID="ShareSecretListenerChoice">
  <text>I have a secret to share with you.</text>
  <part Name="WaterRitualSellSecret" />
</choice>
```

The `Gossip="true"` toggle distinguishes the two — they share
machinery but filter different entry categories.

### The `Share()` flow

[`WaterRitualSellSecret.Share()`](../../qud-decompiled-project/XRL.World.Conversations.Parts/WaterRitualSellSecret.cs)
at line 60:

```csharp
public virtual void Share()
{
    List<IBaseJournalEntry> distinctNotes = GetDistinctNotes();
    HistoryAPI.OnWaterRitualSellSecret(WaterRitual.Record, distinctNotes);  // ← event hook
    int num = Popup.PickOption(
        Secret ? "Choose a secret to share:" : "Choose some gossip to share:",
        …,
        GetOptionsFor(distinctNotes),
        …);
    if (num >= 0) { SellEntry(distinctNotes[num]); }
}
```

Note the **event hook**: `HistoryAPI.OnWaterRitualSellSecret` lets
arbitrary subsystems inject custom secrets into the menu at runtime,
filtered by the current `WaterRitual.Record` (which records the
faction context).

### Weight + filter

`GetWeight(entry)` at [line 38](../../qud-decompiled-project/XRL.World.Conversations.Parts/WaterRitualSellSecret.cs)
asks the faction "how much do you care about this kind of secret":

```csharp
int buySecretWeight = WaterRitual.RecordFaction.GetBuySecretWeight(Entry, The.Speaker);
if (Entry is JournalObservation observation) {
    if ((observation.Category != "Gossip") != Secret) return 0;  // category mismatch
    return buySecretWeight;
}
```

Translation: a faction has a per-secret weight (might be 0, might be
100). The menu lists only entries with weight > 0, ordered by
weight. Different factions are interested in different things — what
the Putus Templar will buy isn't what the Mechanimists will.

### Selling an entry

`SellEntry()` at [line 71](../../qud-decompiled-project/XRL.World.Conversations.Parts/WaterRitualSellSecret.cs):

```csharp
public virtual void SellEntry(IBaseJournalEntry Entry) {
    Entry.Tradable = false;                                                       // can only sell once
    Entry.AppendHistory(" {{K|-shared with " + WaterRitual.RecordFaction.GetFormattedName() + "}}");
    Entry.Updated();
    Entry.Reveal(WaterRitual.RecordFaction.GetFormattedName());                   // the faction now also knows
    AwardReputation(Bonus);
}
```

Two interesting beats:
1. `Tradable = false` — you can't double-sell. Each secret is a
   one-shot commodity per playthrough.
2. `Entry.Reveal(faction)` — the secret propagates to the faction.
   This is *how* gossip spreads in the simulation: once you sell a
   secret to one Mechanimist, the entire faction "knows" it (in a
   loose sense — it affects which NPCs will then want to *buy* the
   same secret from you).

## Where secrets come from

Secrets are seeded in three ways:

### 1. World-gen (BuildSecrets)

[`JoppaWorldBuilder.BuildMutableEncounters`](../../qud-decompiled-project/XRL.World.WorldBuilders/JoppaWorldBuilder.cs)
line ~411:

```csharp
BuildStep("Placing secrets", BuildSecrets);
BuildStep("Creating gossip", JournalAPI.InitializeGossip);
BuildStep("Creating observations", JournalAPI.InitializeObservations);
```

The world-build pass creates the *initial inventory* of secrets:
faction heirloom locations, historic-site locations, ruin
coordinates, who-killed-whom from the sultan history.

### 2. NPC `Awake` event hooks

[`WaterRitualSellSecret.Awake`](../../qud-decompiled-project/XRL.World.Conversations.Parts/WaterRitualSellSecret.cs)
line 80:

```csharp
GetWaterRitualSellSecretBehaviorEvent.Send(
    The.Player, The.Speaker,
    ref Message, ref Reputation, ref Bonus, Secret, Gossip);
```

This fires an event that any subsystem can listen to. A faction-quest
script might inject a faction-specific secret here. A unique NPC
might inject a one-of-a-kind rumor.

### 3. Player gameplay

Some secrets are generated by player actions: discovering a ruin,
killing a unique NPC, completing a quest. These get added to the
journal as `JournalObservation` entries by the gameplay code that
fires them.

## The emergent map

The interesting consequence: the *graph of who knows what about whom*
is unique to your playthrough. Two Qud players might both have done
the water ritual with Mehmet. One sold him a rumor about a Mopango
ambush; the other sold him a rumor about a Templar patrol. From that
point on, Mehmet behaves slightly differently in each playthrough —
he's primed with different information, his faction-reputation
implications cascade differently.

This isn't "the world reacts to player choice" in a scripted-quest
sense. It's *the gossip simulation reacting to the player as a node
in the network*. Mechanically: which secrets are still `Tradable`
and which factions know which secrets is a per-save state, and it
feeds into per-conversation behavior.

## The `Reveal` chain

When `Entry.Reveal()` fires for a `JournalObservation`:

```csharp
// JournalObservation.cs:123
public override void Reveal(string LearnedFrom = null, bool Silent = false)
{
    if (!Revealed) {
        base.Reveal(LearnedFrom, Silent);
        Updated();
        // ... show popup, file in "Observations" journal section
    }
}
```

The base `Reveal` triggers further events that other subsystems hook
into. A particularly elegant property: revealing a secret to a
faction is symmetric with the player learning it. It's the same
machinery in both directions.

## Video angles

- **"Gossip as a graph."** Diagram the network: NPCs ↔ secrets ↔
  factions. Show how selling one secret to one NPC propagates to a
  faction, which changes what secrets *other* NPCs will buy from
  you. This is the most under-discussed thing in Qud's design.
- **"The water ritual is a UI for a simulation."** Frame the ritual
  itself (the line "Live and drink, kindred") as a *vocabulary* for
  underlying mechanics: what's actually happening is reputation
  exchange + journal-entry tradable-flag flipping. The flavor sells
  it.
- **"Every secret is one-shot."** The `Tradable = false` line is a
  small but meaningful design choice. It forces the player to think
  about *who* to sell each secret to. Compare to RPGs where you can
  re-sell the same info to ten NPCs for ten rewards.
- **"Where the secrets come from."** Three sources: world-gen seed,
  NPC event-injection, player gameplay. Each illustrates a different
  design pattern.

## Where to find examples in the corpus

- [`conversations/BaseConversation.md`](../conversations/BaseConversation.md)
  — the water-ritual scaffolding (every conversation inherits this)
- Any villager conversation: the `WaterRitualChoice` greeting opens
  the ritual flow
- [`Tszappur.md`](../conversations/Tszappur.md), [`Hortensa.md`](../conversations/Hortensa.md),
  [`Yla_Haj.md`](../conversations/Yla_Haj.md) — NPCs that have rich
  secret-trading content
- The `JournalScreen.STR_OBSERVATIONS` constant in the codebase is
  where the observations end up displayed; the journal is the
  player-facing surface of all this machinery
