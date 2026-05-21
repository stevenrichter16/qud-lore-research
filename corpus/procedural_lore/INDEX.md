# Procedural Lore — How Qud Generates Its Own History

Essays for video-script research. Each essay is grounded in the
decompiled C# code (`/Users/steven/qud-decompiled-project/`) plus the
data files in the Steam install
(`~/Library/Application Support/Steam/.../Base/`).

This is the **lore that doesn't fit in the static XMLs** — the
machinery that builds a fresh mythology every time you boot a world.

## Reading order

1. **[01_history_engine_overview.md](01_history_engine_overview.md)** — the headline synthesis essay; if you watch one video, this is it
2. **[02_sultan_history_generation.md](02_sultan_history_generation.md)** — the 5-sultan, 6000-year-each timeline
3. **[03_spice_grammar_engine.md](03_spice_grammar_engine.md)** — the recursive template engine behind every named thing
4. **[04_historic_relic_generation.md](04_historic_relic_generation.md)** — why each weapon has a biography
5. **[05_settlements_and_zones.md](05_settlements_and_zones.md)** — what's hand-placed and what's procgen
6. **[06_secrets_and_water_ritual.md](06_secrets_and_water_ritual.md)** — gossip as a per-playthrough emergent map

## Key entry-point files (verified 2026-05-20)

| System | File | Lines |
|---|---|---:|
| Sultan history generator | [`XRL.Annals/QudHistoryFactory.cs`](../../qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs) | 643 |
| Single sultan generator | [`XRL.Annals/InitializeSultan.cs`](../../qud-decompiled-project/XRL.Annals/InitializeSultan.cs) | 80 |
| Timeline data structure | [`HistoryKit/History.cs`](../../qud-decompiled-project/HistoryKit/History.cs) | 209 |
| Spice template engine | [`HistoryKit/HistoricStringExpander.cs`](../../qud-decompiled-project/HistoryKit/HistoricStringExpander.cs) | 435 |
| Spice data loader | [`HistoryKit/HistoricSpice.cs`](../../qud-decompiled-project/HistoryKit/HistoricSpice.cs) | 160 |
| Spice data file | `~/Library/.../Base/HistorySpice.json` | 2692 lines |
| Relic name generator | [`XRL.World/RelicGenerator.cs`](../../qud-decompiled-project/XRL.World/RelicGenerator.cs) | 1692 |
| World/settlement placer | [`XRL.World.WorldBuilders/JoppaWorldBuilder.cs`](../../qud-decompiled-project/XRL.World.WorldBuilders/JoppaWorldBuilder.cs) | 3641 |
| Water-ritual secrets | [`XRL.World.Conversations.Parts/WaterRitualSellSecret.cs`](../../qud-decompiled-project/XRL.World.Conversations.Parts/WaterRitualSellSecret.cs) | 145 |
| Secret storage | [`Qud.API/JournalObservation.cs`](../../qud-decompiled-project/Qud.API/JournalObservation.cs) | 136 |
