> ⚠️  **SPOILER WARNING.** This conversation is in `HiddenConversations.xml`,
> which the game flags `ExcludeFromCorpusGeneration='true'`. Contents may
> include endgame branches (Spindle ascent, Coda, late-quest reveals).

# Conversation: `SpokenIonic`

_From HiddenConversations.xml_

_Inherits: (default: BaseConversation)_

_0 start(s), 10 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Sapience? Hey!
        The time goes, since I have communed last, my adornments speak.
        Has interstate power been declared among the Codex people?

**Choices:**
- **choice** `Who` → `Ionic`
    > Who are you? What are you?
- **choice** `Where` → `Temple`
    > What is this place?
- **choice** `Spindle` → `Journey`
    > I ascended the Spindle to arrive at this place.
- **choice** `Translation` → `Codex`
    > What 'interstate power'? Who are the 'Codex people'?
- **choice** `Bye` → `End`
    > Live and... drink?

### Node `Ionic`

Gathered and spun, I emerge into Spoken Ionic Through Covalency Heart.
        What is... what are. I cannot.
        Finding no entry, for the rest is at home. A strand to you.

**Choices:**
- **choice** `?` → `Greet`
    > Greetings, Spoken Ionic Through Covalency Heart. I am =name=.
- **choice** `?` → `Adornments`
    > I like your jewelry.

### Node `Greet`

Joyously!

### Node `Adornments`

I shiver at a magnanimity long since worn! Decorate you, decorate.
        Your adornments fascinate also, hey!
        Span of time across stars shines through it.

### Node `Journey`

Emerges this creature from soil, speaks adornment.
        Shaken carefully because thought was the line closed.
        Our remembers at home. Strand.

### Node `Codex`

By my adornments, it is the mat below and its home-havers.
        It is not? I offer a strand. This entry can be at home.
        Having all time and no entry-home, we addle.

**Choices:**
- **choice** `Howlong` → `Time`
    > How long have you been here?

### Node `Time`

I must offer a strand to you.
        Having not this entry, for I left it at home.
        At smallest... more than one hundred Codex cycle. Less than ten thousand.
        Big span. I offer you strands for this.

### Node `Temple`

Hey! This one I have.
        Rootbound we to Star Orchid Temple, one of more.
        Here celebrate burn dust of the tail riders, mosaic innumerability.

**Choices:**
- **choice** `?`
- **choice** `Else` → `Others`
    > Is there anyone else here?

### Node `Others`

For temple 'here' yes:
        Spoken Ionic Through Covalency Heart here.
        Also, you.

**Choices:**
- **choice** `Whoelse` → `Quay`
    > But is there anyone else here on the Quay?

### Node `Quay`

Offering adornment,
        No entry for this.
        My mat is small.

**Choices:**
- **choice** `?`
