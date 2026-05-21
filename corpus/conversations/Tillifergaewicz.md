# Conversation: `Tillifergaewicz`

_Inherits: (default: BaseConversation)_

_0 start(s), 4 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

*aloud, in a high-pitched buzzing voice*

        A customer? A customer! Enter, =player.formalAddressTerm=, browse, buy. The Consortium's finest, stocked and sold by Tillifergaewicz! Tilli will do, but what will Tilli do... for you?

**Choices:**
- **choice** `TilliTalks` → `Talking`
    > You speak aloud. You're not telepathic?
- **choice** `TilliGreets` → `Greeting`
    > Greetings, Tilli. I am =name=.
- **choice** `TilliFreehold` → `Freehold`
    > What can you tell me about the Freehold?
- **choice** `TilliBye` → `End`
    > I'm fine, thank you. Live and drink.

### Node `Talking`

Ugh, ever telepathy. No requirement exists that Consortium merchants be mind-speakers, as swollen with their numbers as we are. I cannot blame you for your surprise, mind, I am simply frustrated.

        Over years, I shaped something akin to a voice-box, which you hear now. I "made do", as Rokhas might say. Now what may I "make do" for you?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Greeting`

Greetings, =name=, and welcome! In what wares may I interest you this day?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Freehold`

Oh, I am joyous to reside here.

        Yd could do, mind, with some measure of hierarchy, and more infrastructure, to attract wayfarers less adventuresome than yourself. Also, Mak absolutely must cease advising that anyone enter the clam; it is not funny and someone could die.

        But... the structure of friendships here is true, and sturdy! Kindly keep this exchange between us. I was mostly kidding. Somewhat kidding.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
