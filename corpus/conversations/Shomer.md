# Conversation: `Shomer`

_Inherits: (default: BaseConversation)_

_0 start(s), 14 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Saad, welcom. Saad, from thyn heres shaken the wet and olde lif. Saad, in-to a smal vessel pouren hit. Saad, to thyn sash attachen the vessel. Saad, crossen nou thrugh the heigh gate and in-to Brightsheol.

**Choices:**
- **choice** `ChoiceDream` → `Dream`
    > Where is Brightsheol in relation to Qud... to Salum?
- **choice** `ChoiceDead` → `Dead`
    > Am I dead?
- **choice** `ChoicePlace` → `Place`
    > What is this place?
- **choice** `ChoiceSaad` → `Saad`
    > Why do you call me Saad?
- **choice** `ChoiceMission` → `Mission`
    > I've come from the Thick World with a mission: to disable the Spindle's magnetic field. Can you do this for me?
- **choice** `?` → `End`
    > ...

### Node `Dead`

Saad, the bodi dien, but the mind romen.

**Choices:**
- **choice** `?`
- **choice** `?` → `Place`
    > What is this place?
- **choice** `?` → `Saad`
    > Why do you call me Saad?
- **choice** `?` → `Mission`
    > I've come from the Thick World with a mission: to disable the Spindle's magnetic field. Can you do this for me?
- **choice** `?` → `End`
    > ...

### Node `Place`

Saad, stonden thu at the heigh gate to Brightsheol. Saad, thyn heres been wet with olde lif. Saad, shaken thyn hed and cross in-to neue lif.

**Choices:**
- **choice** `?`
- **choice** `?` → `Resheph`
    > Is Resheph here?
- **choice** `?` → `Dead`
    > Am I dead?
- **choice** `?` → `Saad`
    > Why do you call me Saad?
- **choice** `?` → `Mission`
    > I've come from the Thick World with a mission: to disable the Spindle's magnetic field. Can you do this for me?
- **choice** `?` → `End`
    > ...

### Node `Resheph`

No Saad Resheph residen her.

**Choices:**
- **choice** `?` → `Dream`
    > Where is Brightsheol in relation to Qud... to Salum?
- **choice** `?` → `Dead`
    > Am I dead?
- **choice** `?` → `Saad`
    > Why do you call me Saad?
- **choice** `?` → `Mission`
    > I've come from the Thick World with a mission: to disable the Spindle's magnetic field. Can you do this for me?
- **choice** `?` → `End`
    > ...

### Node `Dream`

Alofte of Gjaus a cite twinklen. And ther the Seraph dremen. And Brightsheol is the drem.

**Choices:**
- **choice** `?` → `Dead`
    > Am I dead?
- **choice** `?` → `Place`
    > What is this place?
- **choice** `?` → `Saad`
    > Why do you call me Saad?
- **choice** `?` → `Mission`
    > I've come from the Thick World with a mission: to disable the Spindle's magnetic field. Can you do this for me?
- **choice** `?` → `End`
    > ...

### Node `Saad`

Artow a Saad of olde Salum, and nou stonden thu at the heigh gate to Brightsheol.

**Choices:**
- **choice** `?`
- **choice** `?` → `Qud`
    > Salum? Is that another name for Qud?
- **choice** `?` → `Dead`
    > Am I dead?
- **choice** `?` → `Place`
    > What is this place?
- **choice** `?` → `Mission`
    > I've come from the Thick World with a mission: to disable the Spindle's magnetic field. Can you do this for me?
- **choice** `?` → `End`
    > ...

### Node `Qud`

Saad, yis.

**Choices:**
- **choice** `?` → `Dead`
    > Am I dead?
- **choice** `?` → `Place`
    > What is this place?
- **choice** `?` → `Saad`
    > Why do you call me Saad?
- **choice** `?` → `Mission`
    > I've come from the Thick World with a mission: to disable the Spindle's magnetic field. Can you do this for me?
- **choice** `?` → `End`
    > ...

### Node `Mission`

*The clothes shrouding Rainwater Shomer's form are still for many moments.*

        The shomrim connen. Why oghte we?

**Choices:**
- **choice** `?` → `ImSaad`
    > Because... I am a Saad, after all.
- **choice** `?` → `ImSaad`
    > Shomer, you impudent whelp! Saad Resheph stands before you. Do as I say.
- **choice** `?` → `Salum1`
    > Something changed atop the Spindle. If Brightsheol is indeed connected to the city there, then this change may suggest it's in peril...
- **choice** `?` → `Start`
    > Wait. I have more questions to ask.

### Node `ImSaad`

*The clothes shrouding Rainwater Shomer's form are still for many moments.*

        The shomrim remainen unbilefful.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > ...

### Node `Salum1`

*The clothes shrouding Rainwater Shomer's form remain still.*

**Choices:**
- **choice** `?` → `Salum2`
    > One year ago, someone began broadcasting a signal from atop the Spindle. I have a recording of it here...

### Node `Salum2`

*The clothes shrouding Rainwater Shomer's form remain still.*

**Choices:**
- **choice** `?` → `Salum3`
    > I ask you: disable the magnetic field so that the Spindle can be ascended and the signal investigated.

### Node `Salum3`

*The clothes shrouding Rainwater Shomer's form are still for many moments.*

        Saad, the Seraph sprecen. Saad, thu asken, and the shomrim assenten. Saad, wiltou return to Salum or crossen in-to Brightsheol?

**Choices:**
- **choice** `?` → `Return`
    > If it can be done, return me to Qud. I wish to ascend the Spindle myself.
- **choice** `?` → `Cross`
    > ... I've shaken the wet life from my hair. Now I shall cross into Brightsheol.
- **choice** `?` → `End`
    > I need time to consider.

### Node `Return`

Saad, nou-then return.

**Choices:**
- **choice** `?` → `End`
    > I am ready.
- **choice** `?` → `End`
    > I need time to reconsider.

### Node `Cross`

Saad, nou-then crossen in-to Brightsheol.

**Choices:**
- **choice** `?` → `End`
    > I am ready.
    - _part: `CrossIntoBrightsheol`_
- **choice** `?` → `End`
    > I need time to reconsider.
