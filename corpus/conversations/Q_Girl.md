# Conversation: `Q Girl`

_Inherits: (default: BaseConversation)_

_0 start(s), 10 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Quetzal! Who are you, stranger?

**Choices:**
- **choice** `?` → `End`
    > I must be going.

### Node `Start`

It's time to fight, =name=. Are you with me?

**Choices:**
- **choice** `?` → `End`
    > I am.

### Node `Start`

Quetzal, quetzal, quetzal! Welcome to the workshop, =player.formalAddressTerm=.

**Choices:**
- **choice** `ClimberChoice` → `Climber`
    > Barathrum asked me to deliver your blueprints to Pax Klanq.
- **choice** `RumblingChoice` → `Rumbling`
    > Did you feel that rumbling, Q Girl?
- **choice** `QuetzalChoice` → `Quetzal`
    > What does 'quetzal' mean?
- **choice** `HairChoice` → `Hair`
    > Your hair is a quasar of red ochre and indigo.
- **choice** `GogglesChoice` → `Goggles`
    > Do you like my goggles?
- **choice** `TinkerChoice` → `Tinker`
    > There must be a hundred gadgets here. What are you working on?
- **choice** `DiskChoice` → `Disk`
    > Otho informs me that you have a method for decoding the signal. Can you encode your instructions for the baetyl onto this disk?
- **choice** `?` → `End`
    > Live and drink, tinker.

### Node `Rumbling`

Yikes! Yes! The intensity was too great to be the result of one of my experiments. What was it, I wonder?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, tinker.

### Node `Quetzal`

It's a word I say out of excitement. Sort of a semantic extension of the feeling I get when I see a quetzal. Oh, a quetzal is a pretty bird in the trogon family. I tend to incorporate things I like into my idiolect.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, tinker.

### Node `Hair`

Quetzal! Thank you, thank you. What a poetic metaphor! You're a regular Shakesprig, aren't you?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, tinker.

### Node `Goggles`

Yes, yes, yes. They are so quetzal!

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, tinker.

### Node `Tinker`

Oh, oh! Quetzal! A wave shortener for the short wave detector, a frustum pully for the ion lathe, a thrice-retrothreaded M-band, a...

        *She continues.*

        ...and a dissertation on the illegitimacy of power. Quetzal!

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, tinker.

### Node `Disk`

I do, brave friend. I'll imprint them now.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Q Girl.

### Node `Climber`

Here they are, brave friend. Good luck!

**Choices:**
- **choice** `?` → `End`
    > Thank you, Q Girl.
