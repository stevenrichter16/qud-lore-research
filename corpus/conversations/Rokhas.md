# Conversation: `Rokhas`

_Inherits: (default: BaseConversation)_

_0 start(s), 7 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Ayuh.

**Choices:**
- **choice** `?` → `Greet`
    > Greetings. I am =name=.
- **choice** `?` → `Ayuh`
    > Ayuh.
- **choice** `?` → `End`
    > Live and drink.

### Node `Ayuh`

*nods*

**Choices:**
- **choice** `?` → `Greet`
    > =name=.
- **choice** `?` → `End`
    > *nod*

### Node `Greet`

Rokhas. I ranch these here beauts.

**Choices:**
- **choice** `RokhasRanch` → `Ranch`
    > This is your ranch?
- **choice** `RokhasSlugs` → `Nudibranchs`
    > Are those... giant slugs?
- **choice** `RokhasFreehold` → `Freehold`
    > What do you think of the Yd Freehold?
- **choice** `RokhasBye` → `End`
    > Live and drink, Rokhas.

### Node `Ranch`

I said I ranch these here beauts.

        The Freeholders en't much for letting a body lay claim to land. En't what I'da wished for, but as the Issachari say: "Should your compass lead you to the Six Day Stilt, throw it in the well."

**Choices:**
- **choice** `?` → `Hometown`
    > Are you from the desert? How did you end up here?
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Hometown`

Lived most of m'life on a desert steppe twixt the flower fields of Qud and the M'ryee's salt pans.

        I ended up here when m'snapbrain cousin played tinker with one of them coiler doodads. The less said about all that, the better.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Nudibranchs`

Kaleidoslugs! Beautiful slugs, they are, lovely crooners. Love em. Big ole slugs. Heh.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Freehold`

Is what it is. Fine enough place. I've a trade, critters, and nowheres else to go.

        I en't much for grand experiments, I just got to live. Ken?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
