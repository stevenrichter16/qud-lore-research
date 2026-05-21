# Conversation: `Tikva`

_Inherits: (default: BaseConversation)_

_5 start(s), 10 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `KilledTau`  _IfTestState=`TauElse contains KilledByPlayer`_

*the sound of the chime rings querulous and faint, its light flickering.*

        Please… no…

**Choices:**
- **choice** `?` → `Killed2`
    > Tau has departed.

### Start `LostInSoft`  _IfHaveState=`TauLostInSoft`_

*the sound of the chime rings querulous.*

        The light shines upon you but illuminates nothing. It quails.

**Choices:**
- **choice** `?` → `Lost2`
    > Tau has departed.

### Start `KilledCompanion`  _IfTestState=`TauCompanion contains KilledByPlayer`_

Relief, relief. Relief from the void, safety from its creases.

**Choices:**
- **choice** `?` → `Companion2`
    > How do you feel about Tau's departure?

### Start `ElseWelcome`  _IfHaveState=`ElseingComplete`_

It is happy, it lies. It swells to witness Tau's choice, in pantomime of shared joy.

**Choices:**
- **choice** `?` → `Else2`
    > How do you feel about Tau's departure?

### Start `Welcome`

*the chime rings a long, clarion tone.*
      
      You are as beautiful as imagined. You ring with a shining purpose. This chime is awed to bask in your presence.

**Choices:**
- **choice** `?` → `Name`
    > I am =name=. Who are you?
- **choice** `?` → `Light`
    > Your chime shines with such painful light.
- **choice** `?` → `Gyredream`
    > Were you affected by gyredream?
- **choice** `?` → `TauChime`
    > I am to carry Tau's chime to Taproot, so she can leave Chavvah.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Killed2`

It ignores the monster. It ignores it. It ignores it.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Lost2`

It stares into the light and wishes away the monster.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Companion2`

The light shines so bright, the voidshadow folds not upon it. It exults. It relaxes. It wills this troubled feeling away.

        Thank you for clearing Tau's path, =name=. This is better.

**Choices:**
- **choice** `?` → `PostQuestions`
    > You are welcome. I yet have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `Else2`

It wills this troubled feeling away. It looks to the light with something in its eyes. It tries to blink the something away, but it cannot. The light is dim through the something in its eyes.

        But the light yet shines. It will blink and it will see the light in searing glory. I thank you, I thank you, I thank you.

**Choices:**
- **choice** `?` → `PostQuestions`
    > You are welcome. I yet have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `PostQuestions`

Yes. It looks into the light with you.

### Node `Name`

*the chime rings again*
      
      It is called Tikva, low and humble. The chime rests in a web of strong love, a little piece of something greater and so much more beautiful. As are you, but a gestalt unto yourself. A world to be orbited.

### Node `Light`

It channels the breathtaking things seen and heard and known. Bathe your senses in it until they grow accustomed. You will see nothing else.

### Node `Gyredream`

*the chime rings, a querulous and tinny sound*
        
        It... can scarce find the dream in this light. It thinks of Tzedech and weeps. It was not here, last time the static was in high pitch, but it remembers the pain and fear. It is not ready to feel these, it cannot. Gaze into its light and speak not of nightmares.

**Choices:**
- **choice** `?` → `Lover`
    > Tzedech?

### Node `TauChime`

*the chime goes silent, and its voice in your mind is small and subdued*
        
        It begs. Speak not of Tau. She shone so bright, with none of the heat from my -- from Tzedech.
        
        To remember her departure harms it. This and gyredream are too much for it to bear.

**Choices:**
- **choice** `?` → `Lover`
    > 'Your' Tzedech?

### Node `Lover`

*the deathbell tolls.*
        
      No, it cannot, it cannot, it cannot. It misses it, it misses it, it misses it, it cannot it cannot it cannot.
      
      Look into the light. It burns away the sorrow, it burns away. Please, please, please.
