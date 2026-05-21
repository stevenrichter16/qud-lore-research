# Conversation: `OmonporchBarathrumites`

_Inherits: (default: BaseConversation)_

_0 start(s), 2 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Live and drink.~
        What is it?~
        Live and drink, =player.formalAddressTerm=.

**Choices:**
- **choice** `?` → `Spindle`
    > Why did you come to Omonporch?
- **choice** `?` → `End`
    > Live and drink.

### Node `Spindle`

To make preparations, =player.formalAddressTerm=. Barathrum instructed us here after you secured the grounds.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, friend.
