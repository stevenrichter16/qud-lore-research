# Conversation: `Nima Ruda`

_Inherits: (default: BaseConversation)_

_0 start(s), 4 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Ahh, there is a new face. I am Nima Ruda, town apothecary. If your feet point to Qud, you’ll need some of my wares before you go.~
        Live and drink, wayfarer.~
        Time and rest are the surest way to dress a wound, but my wares can help if you’re in a hurry.~
        The Fates watch you, =player.formalAddressTerm=.~
        Don’t let your nostrums run dry on the road. I have what you need.

**Choices:**
- **choice** `?` → `Wares`
    > What wares do you offer?
- **choice** `?` → `Story`
    > Where are you from?
- **choice** `?` → `End`
    > Live and drink.

### Node `Wares`

Witchwood for pain, bandages for bleeding, yuckwheat and honey for when your guts act up. Coldcaps when I can find them. Why not take a look?

### Node `Story`

I grew up right here in Joppa, daughter of the Elder and all. Spent some years delving, but gave it up after a few near escapes and nearly deadly wounds. I’m better suited to herbalism anyway, and my father worries less.

**Choices:**
- **choice** `?` → `Leadership`
    > Will you inherit leadership of Joppa from your father?

### Node `Leadership`

Fates forfend. I would hardly like to lead a village and run a shop at the same time.

**Choices:**
- **choice** `?` → `End`
    > Fair enough. Live and drink.
