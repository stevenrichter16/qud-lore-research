# Conversation: `PaxKlanq`

_Inherits: (default: BaseConversation)_

_1 start(s), 12 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

Klanq puff at you?

**Choices:**
- **choice** `?` → `Die`
    > Didn't you die?
- **choice** `?` → `BarathrumStudy`
    > Aren't you supposed to be helping Barathrum in his study?
- **choice** `ChoiceWhat` → `What`
    > Excuse me?
- **choice** `ChoicePlace` → `Place`
    > Why are you the color of coral? And why did the brick road outside only appear after I ate the Eater's fleshcap?
- **choice** `ChoicePresume` → `Presume`
    > I'm here to collect a debt for the Barathrumites.
- **choice** `?` → `End`
    > Fine. Puff away.
    - _part: `PaxInfectLimb` (IfQuestActive=true)_
- **choice** `?` → `End`
    > No, thanks. Live and drink.

## Nodes

### Node `Die`

Klanq distribute! Cannot kill Klanq in a way that matters.

### Node `BarathrumStudy`

Klanq distribute! Here, there.

### Node `What`

Klanq puff at you.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, mushroom.

### Node `Place`

Klanq want no visitors, so Klanq relocate workshop. Half dimension away. Tasties alter viewing plane.

**Choices:**
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, mushroom.

### Node `Presume`

Prickles? Klanq miss prickles.

**Choices:**
- **choice** `ChoicePrickles` → `Light`
    > Why do you owe... "prickles"... a debt?
- **choice** `ChoiceQuest` → `Quest`
    > Well, you can repay the debt now. Barathrum wants you to build something. A climber. He says only you can do it.

### Node `Light`

Klanq puff on prickles during lecture on light refraction. Prickles angry.

**Choices:**
- **choice** `?`

### Node `Quest`

Klanq care little for debt.

**Choices:**
- **choice** `?` → `Quest2`
    > But you owe Barathrum. He needs your help.

### Node `Quest2`

Klanq puff on debt.

**Choices:**
- **choice** `?` → `Quest3`
    > Is there anything I can do change your mind?

### Node `Quest3`

Klanq think...

**Choices:**
- **choice** `?` → `Quest4`
    > ...

### Node `Quest4`

Klanq got it! Klanq puff on you.

**Choices:**
- **choice** `?` → `Quest5`
    > Excuse me?
- **choice** `?` → `End`
    > Puff on yourself, mushroom. I'm leaving.

### Node `Quest5`

Klanq puff on you. You host Klanq. You spread Klanq for Klanq. Then your Klanq shrivels away.

        Klanq puff on you, then Klanq build jalopy.

**Choices:**
- **choice** `?` → `Quest6`
    > Fine. Puff away.
    - _part: `PaxInfectLimb`_
- **choice** `?` → `End`
    > Puff off. Bye.

### Node `Quest6`

Klanq puff on you! Klanq build jalopy.

**Choices:**
- **choice** `?` → `End`
    > Ugh.
    - _part: `TakeItem` (Require=false Blueprints=ClimberBlueprints)_
    - _part: `QuestHandler` (Action=Step QuestID=Pax Klanq, I Presume? StepID=Convince Pax Klanq to Construct the Climber)_
