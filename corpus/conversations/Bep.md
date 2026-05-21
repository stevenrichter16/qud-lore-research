# Conversation: `Bep`

_Inherits: (default: BaseConversation)_

_0 start(s), 6 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

bep see widget? Or bep see widget.

**Choices:**
- **choice** `BepChoice` → `Bep`
    > bep?
- **choice** `SvardymChoice` → `Svardym`
    > Are you svardym?
- **choice** `TrashChoice` → `Trash`
    > So much trash! Did a goatfolk bully crash through your workshop?
- **choice** `FreeholdChoice` → `Freehold`
    > Tell me about the Yd Freehold.
- **choice** `?` → `End`
    > Live and drink.

### Node `Bep`

bep is bep. good meet!

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Svardym`

bep varrrdym from the egg, once.

**Choices:**
- **choice** `GyreChoice` → `Gyre`
    > What do you know of the Gyre?
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Gyre`

grre? bep flame and bend brass to make ring ball grre for librrry.

**Choices:**
- **choice** `?` → `Start`
    > ...
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Trash`

tink mess. flame bits for tink and onto floor! rrcuit snap, glass smatter, core fries and lekky spill.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Freehold`

bep make all and anys. bep too lounge in green-gold cubby, smoke pillow and Krka and Tilli.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.
