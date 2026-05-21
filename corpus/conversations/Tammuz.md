# Conversation: `Tammuz`

_Inherits: (default: BaseConversation)_

_5 start(s), 13 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `NewWelcome`  _IfHaveState=`TammuzPermission`_

*Tammuz chimes a quiet tone.*

### Start `KilledTau`  _IfTestState=`TauElse contains KilledByPlayer`_

*Tammuz is nearly silent but for a soft, shaky resonance*

        ...

**Choices:**
- **choice** `?` → `Killed2`
    > Tau is gone.

### Start `KilledCompanion`  _IfTestState=`TauCompanion contains KilledByPlayer`_

*Tammuz chimes a querulous tone*

        O-oh. Elsefolder... th-this path you have l-laid upon Tau, it-it is best. It is good? P-please be good.

**Choices:**
- **choice** `?` → `Companion2`
    > How does Tau's departure find you?

### Start `ElseWelcome`  _IfHaveState=`ElseingComplete`_

*Tammuz rings a wavering chime*

        Y-you are here. Elseing h... hand.

**Choices:**
- **choice** `?` → `Else2`
    > How does Tau's departure find you?

### Start `Welcome`

*Tammuz chimes a broad and booming tone.*

				You! Purpose-driven mad... madhand. You've come here, right? Then you must know power is our... the domain of being is one of power, wouldn't you say? W-Would you please agree with that?

**Choices:**
- **choice** `?` → `Welcome2`
    > ...

## Nodes

### Node `Killed2`

You m-m-moon king. Madhand.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Companion2`

*Tammuz's chime rings even quieter and more tremulous*

        Un, un-uncertain. Tau l-leaves unfolded but the g-g-g-gyre yet s-spins. The s-spinning leaves me dizzy.

**Choices:**
- **choice** `?` → `PostQuestions`
    > I have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `Else2`

*the chime is louder this time, but just as querulous*

        Sh-sh-she, th-this fate, it. It is a d-deep dark. Will Tau f-fold herself, I wonder?

**Choices:**
- **choice** `?` → `PostQuestions`
    > I have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `Choices`

**Choices:**
- **choice** `?` → `Name`
    > I am =name=. Who are you?
- **choice** `?` → `Gyredream`
    > Did you experience the gyredream?
- **choice** `?` → `TauChime`
    > I am to carry Tau's chime to Taproot, so she can leave Chavvah.
- **choice** `?` → `End`
    > Live and drink.

### Node `PostQuestions`

If y-y, th-that... yes. Ask if, if asking.

### Node `Welcome2`

*Tammuz quiets, then chimes in tottering, unsure tones.*

				You beast! You m-moon king! You... Our roars are beastial! Would you say so?

**Choices:**
- **choice** `?` → `What`
    > This is all nonsense.

### Node `What`

*The chime vibrates and shrinks its sound.*

				You- you don't understand? You... it's you. It's-
				
				It is as said: strange is the path to wisdom! Perhaps you will... perhaps it is you who must figure it out. Figure it all out..

**Choices:**
- **choice** `?` → `Unsure`
    > You sound very unsure of yourself.

### Node `Unsure`

*Tammuz makes a hollow peep.*

**Choices:**
- **choice** `?` → `Permission`
    > Be uncertain, friend. You have my permission.

### Node `Permission`

*Tammuz is silent and still.*

**Choices:**
- **choice** `?` → `End`
    > I will give you a moment.
- **choice** `?` → `End`
    > Live and drink.

### Node `Name`

*Tammuz chimes a small and bright noise.*
				
				Ta- Tammuz. Who becomes. Who is Twofirm even in -then.

**Choices:**
- **choice** `?` → `Twofirm`
    > Twofirm?

### Node `Twofirm`

The t-two sephirots. -then and -else. I cannot be -else. *I* cannot, of course. But -then? It does not seem so.
				  
				Their chimes ring at the right frequencies, others. But not so, mine.

**Choices:**
- **choice** `?` → `Twofirm`
    > Twofirm?

### Node `Gyredream`

*Tammuz quivers and chimes a jarring tone.*

				O-Oh. Oh u-uh oh oh. By contrasts, a q-quake stills even the most anxious trembling...
				
				The world... the world becomes and unbecomes. All the nervous, volcanic energy of being. Who becomes who? Three became one, but what of them now? 
				
				And w-what becomes of Tau? Of me? Of y-you?

### Node `TauChime`

*The chime knells a soft and brittle tone.*

				B-bright, she. And sang to the spark in T-Tammuz, too. By her, and through her, one could well-night feel full and at crown's end.

        She r-returns to Soft now, yes? And then to walk free as -else. See... see her there for me. G-Goodbye.

**Choices:**
- **choice** `?` → `End`
    > ...
