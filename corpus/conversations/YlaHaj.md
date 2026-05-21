# Conversation: `YlaHaj`

_Inherits: (default: BaseConversation)_

_0 start(s), 7 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Traveler. Put down your mangled trinkets and I'll repair them.

**Choices:**
- **choice** `GreetChoice` → `Greet`
    > Who are you?
- **choice** `EzraChoice` → `Ezra`
    > Tell me about this ancient village.
- **choice** `ZothomChoice` → `Zothom`
    > Who is the man camped near the graveyard?
- **choice** `SixshrewChoice` → `Sixshrew`
    > What do you think of the plant you share this building with?
- **choice** `EndChoice` → `End`
    > Live and drink, tinker.

### Node `Greet`

*She gives you a hard stare.*

        I am a Daughter of Exile, but you should call me Yla Haj.

**Choices:**
- **choice** `DaughterChoice` → `Daughter`
    > Daughter of Exile?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Daughter`

Tinker-nuns. The world sees fit to call us that, my sisters and me.

        Do you know the story told of Rebekah the Exile? She was a teacher to Resheph, but he excommunicated her from the sultanate and banished her from the realm.

        To know her, I've chosen a life of unbelonging. And among my sisters, I have the honor of permanent residence by her gravesite.

        I'll tell you this, traveler: the shape of a society is visible only from the outside, and there is peace beyond a boundary.

**Choices:**
- **choice** `RebekahChoice` → `Rebekah`
    > Wasn't Rebekah a healer? Why are you an order of tinkers?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Rebekah`

*Yla Haj pauses.*

        You presume too narrow a meaning of "health".

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Ezra`

Ezra sits in the shadow of history, where small things grow. It's the moss beneath the statue, quite literally. For centuries monarchs concerned themselves with felling trees, and now of the Covenate only Ezra remains.

        It's home to Rebekah's gravesite, so for the Daughters, it is a sacred place. You may notice more of us on pilgrimage.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Zothom`

Zothom. I don't see utility in unkindness, but he's a fool. Were it that proximity to meekness made one meek...

        I have no use for a man who seeks salvation in the body of a dead woman.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Sixshrew`

I don't.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
