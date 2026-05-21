# Conversation: `Tzedech`

_Inherits: (default: BaseConversation)_

_5 start(s), 18 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `KilledTau`  _IfTestState=`TauElse contains KilledByPlayer`_

*The chime rings a bone-shaking alarm.*

        Is this a taunt? A challenge? What cruelty drives you to attempt communication after what you have done?

**Choices:**
- **choice** `?` → `Killed2`
    > How do you feel about Tau's departure?
- **choice** `?` → `End`
    > Live and drink.

### Start `LostInSoft`  _IfHaveState=`TauLostInSoft`_

*The chime rings a knell.*

        O gesticulating hand.

**Choices:**
- **choice** `?` → `Lost2`
    > How do you feel about Tau's departure?

### Start `KilledCompanion`  _IfTestState=`TauCompanion contains KilledByPlayer`_

The chime rings loud and sharp.

        Heavy the hand. Heavy the head.

**Choices:**
- **choice** `?` → `Companion2`
    > Tau has completed her -elseing.

### Start `ElseWelcome`  _IfHaveState=`ElseingComplete`_

You. I roil to see you. I welcome you. I churn.

        Do you know this weight, I wonder? Can you?

**Choices:**
- **choice** `?` → `Else2`
    > Tau has completed the -elseing ritual.

### Start `Declaration`

*the chime rings a sharp, urgent gonging tone*

				Entity! You are given persistent will and agency, twice-hewn architecture of body and strong fiber that pulls. You bolt upright and damp-haired into fullness, your grasp abrading the threads of existence. Your responsibility remains whether acknowledged or not. Have strength, the time is now.

**Choices:**
- **choice** `?` → `What`
    > Sorry?
- **choice** `?` → `Name`
    > I am =name=. Who are you?
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Killed2`

Your mockery disgusts me. You disgust me. I will not be calmed, Tikva!

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Lost2`

We are adrift now. I will seek signs of her, or whatever she becomes. What do you care?

        Do not answer.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Companion2`

I wonder how it must feel to be =name=, so loath to see the pen of fate in another's grasp that you see fit to wrench it away. Does it bring exultation of control, or relief from a gnawing insecurity?

        Do not answer. I will not be calmed. Ask if asking.

**Choices:**
- **choice** `?` → `PostQuestions`
    > I do have questions, still.
- **choice** `?` → `End`
    > Live and drink.

### Node `Else2`

I am torn asunder! This outcome, this outcome, the shear splits me. Why Ptoh? How? Has this always been us? Which of us yet carry this -else to reify under pressure to our extancy?

        Do not answer. There is no word-answer, and perhaps none at all. You have done us a service and I thank you for this -elseing.

**Choices:**
- **choice** `?` → `PostQuestions`
    > You are welcome. I yet have questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `Welcome`

**Choices:**
- **choice** `?` → `Name`
    > I am =name=. Who are you?
- **choice** `?` → `Upset`
    > Is something the matter?
- **choice** `?` → `Gyredream`
    > Is all this about gyredream?
- **choice** `?` → `Tau`
    > I am to carry Tau's chime to Taproot, so she can leave Chavvah.
- **choice** `?` → `End`
    > Live and drink.

### Node `PostQuestions`

I accept. Ask if asking.

### Node `What`

*the chime rings again, echoing louder in the walls of your mind*
        
				Hear me! It is more important than ever to know that you are a driver, reforged and honed. You tool yourself to apply selective atrocity. It cannot be helped. You shape this, your path bloody and blooming. You start in sleep and shake the ground.

				All must, but you most of all. The weight may have been negligent once, but it is terribly heavy now.

				Do you accept responsibilty?

**Choices:**
- **choice** `?` → `Accept`
    > I do.
- **choice** `?` → `Deny`
    > I do not.
- **choice** `?` → `What2`
    > What?

### Node `Deny`

Yet, what you break is broken. -else is not -then regardless of will. This way split me again from Tikva, sundered early the love I knew, the denial. Our cowardice.

				Ignore this digression. Ask, if asking.

**Choices:**
- **choice** `?` → `Lover`
    > You loved another chime?

### Node `What2`

You are encysted as Tikva, just as they! Milky white keratinous thoughts melt to a sick mass, wrapped in a protective membrane. I tremble. So it is.

				Ask, if asking.

**Choices:**
- **choice** `?` → `Cyst`
    > That's disgusting.
- **choice** `?` → `Lover`
    > What's that about Tikva?

### Node `Cyst`

Just as Tikva, you turn away from your self-disgust. Yet, it is you and within you. You contain that you cannot tolerate.

### Node `Accept`

*Tzedech emits a powerful, body-thrumming chime*

				Yes. You understand destroying. You know the weight. We are past time of querulous inquisition, of confessions on lined parchment. Was the whole of this in your weight? It no longer matters. Scale the firmament, smite or soothe what rouses there.

### Node `Name`

*the chime rings clear and loud*

				This called Tzedech. Compass, judgment, motivation. Once lover of Tikva, apart now after gyredream.

**Choices:**
- **choice** `?` → `Lover`
    > You were another chime's lover?

### Node `Upset`

*Tzedech chimes, buzzing with agitation*

Twofirm roils in me with the enormity. Can it contain so much gone and unremunerated? Tau, Tikva, and more to come. Consumed, we, and paralyzed.

### Node `Gyredream`

It consumes me. I witnessed so little from the weave of outcomes. If I could remember them all, could I influence the course? Would I know what safe means? Too many questions with no conceivable answer. Was your rekindling the spark that caught fire? I do not know.
      
      We are adrift.

### Node `Tau`

Tau. We ache in her empty space. Who awaits at taproot? What fate is this?

				This is the path. Be wary.

### Node `Lover`

Tikva. Once lover, now foil, perhaps lover again.
      
      Its light invites and overwhelms, a hope blind and blinding. Cruel frustration at storm-time. When its eyes are needed they turn away. I will not be calmed. I will not be calmed!

**Choices:**
- **choice** `?` → `Lovers`
    > How can chimes in a tree be lovers?
- **choice** `?` → `Cycle`
    > You'll be together again?
- **choice** `?` → `End`
    > I should go. Live and drink.

### Node `Lovers`

You are terribly small. Your love, small. Confined.
      
      I cannot will not uplift your little concept. Do it yourself.

### Node `Cycle`

As seasons cycle, so Chavvah cycles. We are not as you, our love is not as you. But it is come early, this winter. Gyredream shakes us.
    
      This is insufficient and I cannot bridge understanding. Consider questions of greater utility.
