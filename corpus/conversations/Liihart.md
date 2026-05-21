# Conversation: `Liihart`

_Inherits: (default: BaseConversation)_

_0 start(s), 15 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`HindrenVillageRavaged`_

................................

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageDoomed`_

....

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Hey, =name=. Live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

This sucks.

        ...but you're not so bad.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

..................

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

... what a waste.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Oh! =name=.

        It makes me happy to see you.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Um... thank you.

        Live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

*Liihart stares at you for several quiet seconds.*

        Live and drink.

**Choices:**
- **choice** `?` → `ShowSonnet`
    > Does this poem belong to you?
- **choice** `?` → `StoneQuery`
    > May I ask you some questions?
- **choice** `?` → `End`
    > Live and drink, reticent one.

### Node `StoneQuery`

.....

**Choices:**
- **choice** `?` → `StonePush`
    > I said, may I ask you some questions?
- **choice** `?` → `StoneSilence`
    > You are not partial to talking.
- **choice** `?` → `End`
    > Well then. Live and drink.

### Node `StonePush`

*she glares in silence*

**Choices:**
- **choice** `?` → `StonePush`
    > Answer me.
- **choice** `?` → `StoneSilence`
    > You are not partial to talking.
- **choice** `?` → `End`
    > Never mind. Live and drink.

### Node `StoneSilence`

... correct.

**Choices:**
- **choice** `?` → `GentlePush`
    > I'm trying to exonerate your sister. Can you help?
- **choice** `?` → `StonePush`
    > So you can answer my questions. You just don't want to.
- **choice** `?` → `End`
    > Never mind. Live and drink.

### Node `GentlePush`

Eskhind didn't do it. It was probably Keh.

        That's all I know. I mind my business.

        Wish you would too.

**Choices:**
- **choice** `?` → `End`
    > Fair enough. Live and drink.

### Node `ShowSonnet`

Oh! Eskhind wrote that.

        You should give that to Neelahind. It was supposed to go to Neelahind.

**Choices:**
- **choice** `?` → `NotEsk`
    > Not Eskhind?
- **choice** `?` → `End`
    > Thank you. Live and drink.

### Node `NotEsk`

No, no, give it to Neelahind.

        Esk will thank you later.

**Choices:**
- **choice** `?` → `End`
    > I see, thank you. Live and drink.
