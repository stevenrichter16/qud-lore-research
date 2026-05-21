# Conversation: `DromadTrader`

_Inherits: (default: BaseConversation)_

_0 start(s), 2 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

=player.apparentSpecies=? We are greeted! What do you desire?

**Choices:**
- **choice** `?` → `AboutTheDromad`
    > What kind of creature are you?
- **choice** `?` → `End`
    > I desire nothing. Live and drink.

### Node `AboutTheDromad`

I am dromad, =player.apparentSpecies= =player.formalAddressTerm=. Some say saltstrider. Do you know this?

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
