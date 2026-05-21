# Conversation: `Thicksalt`

_Inherits: (default: BaseConversation)_

_5 start(s), 10 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `KilledTau`  _IfTestState=`TauElse contains KilledByPlayer`_

Shivering stillness, coldbark pricking with each thump.

        It comes.

**Choices:**
- **choice** `?` → `Killed2`
    > Tau has departed.

### Start `LostInSoft`  _IfHaveState=`TauLostInSoft`_

*the chime rings a long and pensive tone.*

        How something stirs, deep in Soft.

**Choices:**
- **choice** `?` → `Lost2`
    > Tau has departed.

### Start `KilledCompanion`  _IfTestState=`TauCompanion contains KilledByPlayer`_

*through the chime you hear an echoing cacophony, muted by distance and matter.*

        How we ring with it. Your kicksoft drowns under the beat of our selfcries.

**Choices:**
- **choice** `?` → `Companion2`
    > Tau has completed the -elseing ritual.

### Start `ElseWelcome`  _IfHaveState=`ElseingComplete`_

*through the chime you hear an echoing cacophony, muted by distance and matter.*

        How we ring with it. Your kicksoft drowns under the beat of our selfcries.

**Choices:**
- **choice** `?` → `Else2`
    > How does Tau's departure find you?

### Start `Welcome`

Who thumps my crystal arms, and kicksofts me at windfall? I feel you here, friend.

**Choices:**
- **choice** `?` → `Name`
    > I am =name=. Who are you?
- **choice** `?` → `Feel`
    > You... feel me?
- **choice** `?` → `Gyredream`
    > Did you experience the gyredream?
- **choice** `?` → `TauChime`
    > I am to carry Tau's chime to Taproot, so she can leave Chavvah.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Killed2`

Can you feel the stillness? The drycrackle of space between as you thump my crystal arms.

        Life flees you. Motion flees you.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Lost2`

Soft churns Tau in beingstuff. She will -then, but perhaps not Taulike.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Companion2`

*the chime is hard to distinguish from the rising cacophony.*

        Crungled allway. Soft reaches through the bounds of everyshape and afflicts us with fireless hotbark. It resonates through Tau's cavernous absence. Arid tearsalt dries between the Lovers.

**Choices:**
- **choice** `?` → `PostQuestions`
    > I have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `Else2`

*the chime is hard to distinguish from the rising cacophony.*

        Crungled allway. Soft reaches through the bounds of everyshape and afflicts us with fireless hotbark. It resonates through Tau's cavernous absence. Touchloss blooms, each facet trembling for shearpull.

**Choices:**
- **choice** `?` → `PostQuestions`
    > I have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `PostQuestions`

*there is an agitation in Thicksalt's accepting chime.*
        
        Pluck the air, then, with your mouth sounds.

### Node `Name`

*Thicksalt chimes a single, outstretched tone.*

				The naming act is imponderable. So Tau called me Thicksalt, one brickword in a towerful poem whose everyshape I forget, but whose flushing of Soft in afterfeel I am in allway.

### Node `Feel`

*Thicksalt chimes in bright tones.*

				All presence is gesture, and all gesture is felt. Bat the air with your wildlimbs, press on the hardflats of my crystal arms... I feel it.

				You must feel it, too. Or are you touchlost? When Dyvvrach is touchlost, when Dyvvrach speaks the millionth word and forgets all speech is gesture, a cord flicked somewhere. Then I feel the bending rush of grass on my crystal fingers, and Dyvvrach is touchkept again.

### Node `Gyredream`

*Thicksalt chimes in sharpened tones, then stills.*

				You thump my crystal arms, you kicksoft me at windfall. Our feltdream did not end. I feel you here, now.
				
				Before, when Soft flushed so suddenly, I felt the stones of war smash against my western roots, and the kicksoft of air unthicken into stillness. In the quiet black, I felt the so-hot burning of star exhaust and thrum of roaring vessel. Then... too much was felt. Threadcount too high for my edgesense.

**Choices:**
- **choice** `?` → `Gyredream2`
    > *continue listening*

### Node `Gyredream2`

...


				*Thicksalt chimes in gentle tones.*

**Choices:**
- **choice** `?` → `Start`
    > ...

### Node `TauChime`

*Thicksalt chimes in soft and rhythmic tones.*

				I stir now, windwept.
				
				Safesight at your passage, =name=. Thump my crystal arms, hardlift and backbear the chime of bright Tau. The downroot will tickle, but I am blessed in allway.
