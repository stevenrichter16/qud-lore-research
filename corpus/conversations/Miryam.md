# Conversation: `Miryam`

_Inherits: (default: BaseConversation)_

_5 start(s), 12 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `KilledTau`  _IfTestState=`TauElse contains KilledByPlayer`_

Strange creatures can be so cruel and arbitrary, I say in greeting.

**Choices:**
- **choice** `?` → `Killed2`
    > Tau has departed.

### Start `LostInSoft`  _IfHaveState=`TauLostInSoft`_

I see you.

**Choices:**
- **choice** `?` → `Lost2`
    > Tau has departed.

### Start `KilledCompanion`  _IfTestState=`TauCompanion contains KilledByPlayer`_

No parting is simple. I see you, -elser.

**Choices:**
- **choice** `?` → `Companion2`
    > Tau has completed the -elseing ritual.

### Start `ElseWelcome`  _IfHaveState=`ElseingComplete`_

No parting is simple. I see you, fair -elser.

**Choices:**
- **choice** `?` → `Else2`
    > Tau has completed the -elseing ritual.

### Start `Welcome`

Oh? A traveler? I see you, then. Live... and drink.

**Choices:**
- **choice** `?` → `Name`
    > I am =name=. Who are you?
- **choice** `?` → `Black`
    > Your chime is cracked and ribboned on inside with starless clouds. Why?
- **choice** `?` → `Gyredream`
    > Were you affected by gyredream?
- **choice** `?` → `TauChime`
    > I am to carry Tau's chime to Taproot, so she can leave Chavvah.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Killed2`

*Miryam chimes low.*

        I cannot properly remember her with you here.

        Leave, I beg you.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Lost2`

I do not know how to remember beloved Tau, struggling like a minnow in Soft. In a place between death and living.

        Leave me, please.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Companion2`

And the sole tether she reached for severed. I mourn for the future she built for herself, now, and worry for Tau herself.

        Thank you, all the same, for taking part in this. May you find your comfort.

**Choices:**
- **choice** `?` → `PostQuestions`
    > You are welcome. I yet have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `Else2`

*Miryam tolls.*

        And the gyre tide carries her a darkling way, perhaps never for us to see again. I will carry with me memory of her -then.

        Thank you for taking part in this. May you find your comfort.

**Choices:**
- **choice** `?` → `PostQuestions`
    > You are welcome. I yet have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `PostQuestions`

Oh? Please, then, friend, ask.

### Node `Name`

*Miryam chimes in deep tones.*
				
				I am Miryam, friend.

### Node `Black`

*Miryam chimes in long tones.*

				It's the kriah, traveler. I am in mourning, and I chime in low tones.

**Choices:**
- **choice** `?` → `Loss`
    > I am sorry, Miryam. Did you lose someone close to you?

### Node `Loss`

*Miryam chimes in deep tones.*

				I swim in cool and dark waters, traveler. For me, it is Shiva, the lament of seven thousand years.

				I mourn the passing of all life, and all the necessity of death life must bring. For you, traveler, to come here, how many had to die? I mourn them.

				Or are you the rarest one, who walks below the bright arches and claims no such cost? Even then, what losses did you suffer to come, traveler? What selves of yours had you to shed? Those are -else to us, and I mourn them as well.

**Choices:**
- **choice** `?` → `Loss2`
    > *continue listening*

### Node `Loss2`

*Miryam chimes in aching tones.*

				...but, too, someone close. Tau. Bright tau. She is gone.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Gyredream`

*Miryam chimes in woeful tones.*

				Oh? You know of our pain. Our felt dream?

				The aching, traveler. =name=, I feel the slump of a Great Dying, the spinning out of all life on Earth, and I, drowning in grief. Or... do I? Is it but a new spring flowering, the slump having landed us in a meadow, and they, the gods, who are dead?

**Choices:**
- **choice** `?` → `Aching`
    > *continue listening*

### Node `Aching`

*Miryam chimes in aching tones.*

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `TauChime`

*Miryam chimes in melodic tones.*

				Oh? You would finish the -elseing act?
				
				I am your debtor, =name=. The ritual is how we organize the anguished practice of being. Now my grieving can begin.
				
				Bright Tau shines always, here or there.
