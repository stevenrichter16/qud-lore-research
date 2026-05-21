# Conversation: `Zothom`

_Inherits: (default: BaseConversation)_

_0 start(s), 13 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Live and drink, wayfarer.

        Cause no strife here and we will have no quarrel.

**Choices:**
- **choice** `?` → `ZothomGreets`
    > I am =name=. Who are you?
- **choice** `?` → `ZothomWarden`
    > You speak like a Warden.
- **choice** `?` → `ZothomWhat`
    > What are you doing here?
- **choice** `?` → `End`
    > Live and drink.

### Node `ZothomGreets`

I am no one of any importance.

        But my name is Zothom, and some call me the Penitent.

**Choices:**
- **choice** `?` → `ZothomThePenitent`
    > Penitent?
- **choice** `?` → `ZothomWarden`
    > You speak like a Warden.
- **choice** `?` → `ZothomWhat`
    > What are you doing here?
- **choice** `?` → `End`
    > Live and drink.

### Node `ZothomWarden`

I am no Warden. My only fellowship is with my own shame.

**Choices:**
- **choice** `?` → `ZothomThePenitent`
    > Why are you ashamed?
- **choice** `?` → `ZothomGreets`
    > My name is =name=. What is yours?
- **choice** `?` → `ZothomWhat`
    > What are you doing here?
- **choice** `?` → `End`
    > Live and drink.

### Node `ZothomWhat`

I watch over the Grave of Rebekah to atone for my deeds, and to find my credo.

**Choices:**
- **choice** `?` → `ZothomKnowsRebekah`
    > Who is Rebekah?
- **choice** `?` → `ZothomThePenitent`
    > Your deeds?
- **choice** `?` → `ZothomCredo`
    > Your credo?
- **choice** `?` → `ZothomWarden`
    > Are you a Warden?
- **choice** `?` → `ZothomGreets`
    > Who are you?
- **choice** `?` → `End`
    > Live and drink.

### Node `ZothomThePenitent`

I was once a vile graverobber, the lowest of the low. Years ago I sought to plunder the Tomb of the Eaters, and set off to do so with a pair of confederates. I watched both of them die, slain by ancient artifice and entombed with the ancient dead.

        I would have shared their fate, but for a coterie of mopango nesting in the catacombs. They kept me safe and fed me while I treated my wounds. It is in their honor that I seek a credo now.

**Choices:**
- **choice** `?` → `ZothomLovesMopango`
    > Mopango?
- **choice** `?` → `ZothomCredo`
    > Credo?
- **choice** `?` → `ZothomTomb`
    > I need to enter the Tomb of the Eaters.
- **choice** `?` → `End`
    > Live and drink, Penitent One.

### Node `ZothomTomb`

Is your motivation just?

**Choices:**
- **choice** `?` → `ZothomJust`
    > Yes.
- **choice** `?` → `ZothomUnjust`
    > No.

### Node `ZothomJust`

Only those who pay their respects to the Grave of Rebekah will know the way into the tomb.

        If you make it inside, the mopango will offer you solace and knowledge, and can tell you more about the Tomb's contents.

**Choices:**
- **choice** `?` → `ZothomKnowsRebekah`
    > Who is Rebekah?
- **choice** `?` → `ZothomLovesMopango`
    > The mopango?
- **choice** `?` → `ZothomHelp`
    > Can't you tell me anything else?
- **choice** `?` → `End`
    > I will. Live and drink.

### Node `ZothomUnjust`

May you share my fate, then.

**Choices:**
- **choice** `?` → `ZothomHelp`
    > Tell me how to get in anyway.
- **choice** `?` → `End`
    > We'll see. Live and drink.

### Node `ZothomHelp`

No.

**Choices:**
- **choice** `?` → `ZothomLovesMopango`
    > Tell me about the mopango, then.
- **choice** `?` → `End`
    > Fine.

### Node `ZothomCredo`

Yes. It is a rite of passage for the mopango people: a statement that inspires contemplation, discussion, and thought. An ideal credo has no single explanation or interpretation and is meant to inspire contemplation in those who hear it. For this reason, it is considered rude among mopango to ask the meaning of a credo.

        Someday I will find mine.

**Choices:**
- **choice** `?` → `ZothomLovesMopango`
    > Who are the mopango?
- **choice** `?` → `ZothomTomb`
    > I need to enter the Tomb of the Eaters.
- **choice** `?` → `End`
    > Live and drink.

### Node `ZothomLovesMopango`

Mopango are plated, digging creatures whose armor scales glow a pale white. They are contemplative, sociable, and mostly peaceful. They commune with ancient objects, which is why a coterie of their kind lives in the Tomb of the Eaters.

        They are patient even with rough-hewn wanderers such as we, but it's still not best to ask one to explain eir credo.

**Choices:**
- **choice** `?` → `PangoQuest`
    > I'd like to meet these mopango.
- **choice** `?` → `ZothomCredo`
    > Credo?
- **choice** `?` → `ZothomTomb`
    > I need to enter the Tomb of the Eaters.
- **choice** `?` → `End`
    > Live and drink, Penitent One.

### Node `PangoQuest`

If you do find =player.reflexive= in the Tomb, the mopango settlement is nestled in the wall of the Northwest Catacombs. The entrance is guarded by a chain turret named Vivira, brightly-painted to distinguish em from eir brethren.

        Resist your reflexive urge to fight or flee, as Vivira is friendly and open to parley. If you meet, tell em I sent you.

**Choices:**
- **choice** `?` → `End`
    > Speak to a... turret? I suppose I will; live and drink.
- **choice** `?` → `End`
    > Speak to a... turret? No thank you; live and drink.

### Node `ZothomKnowsRebekah`

Rebekah was a physician, and an advisor to Resheph until she lost his favor. When, after years of exile, she lost her voice and her life, she was buried here, an outsider unfit to be interred with the honored dead. So she rests here.

        I believe her proximity will help me find my credo.

**Choices:**
- **choice** `?` → `ZothomCredo`
    > Credo?
- **choice** `?` → `ZothomTomb`
    > I need to enter the Tomb of the Eaters.
- **choice** `?` → `End`
    > Live and drink, Penitent One.
