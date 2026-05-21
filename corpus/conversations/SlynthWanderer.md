# Conversation: `SlynthWanderer`

_Inherits: (default: BaseConversation)_

_0 start(s), 5 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Care you to trade?~
        I aggress not.~
        You peaceful, =player.formalAddressTerm=?~
        Wish trade?~
        Good scavenge?~
        Ah! You seem wanderer. How fare?~
        Live and grow, =player.formalAddressTerm=.~
        =player.FormalAddressTerm=, I greet in peace.~
        Live and drink.~
        Ah?~
        Greet, =player.formalAddressTerm=.

**Choices:**
- **choice** `?` → `Who`
    > Who are you?
- **choice** `?` → `End`
    > Live and drink.

### Node `Who`

I am of slynth, a people grown by hydropon.

**Choices:**
- **choice** `?` → `Slynth`
    > What are slynth?
- **choice** `?` → `Hydropon`
    > What is a hydropon?
- **choice** `Iseebye` → `End`
    > I see. Live and drink.

### Node `Slynth`

What see. Leg plant, glow crest.

        Grow from sun-crungled hydropon and depart siblings.

**Choices:**
- **choice** `?` → `Hydropon`
    > What is a hydropon?
- **choice** `?`

### Node `Hydropon`

Cradle glaze in sun-melt. Plant stuff molded to man-shape.

        Within grow slynth. Only slynth, now.

**Choices:**
- **choice** `?` → `Location`
    > Where is the hydropon?
- **choice** `?` → `Slynth`
    > What are slynth?
- **choice** `?`

### Node `Location`

The cracked egg from we crawl yet rest, in the Reef.

        Siblings there. One speak very well: Thah.

**Choices:**
- **choice** `?` → `End`
    > Perhaps I shall visit. Live and drink.
