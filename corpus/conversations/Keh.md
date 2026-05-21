# Conversation: `Keh`

_Inherits: `BaseSlynthMayor`_

_1 start(s), 34 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `MocksFate`  _IfHaveState=`HindrenQuestFullyResolved`_

You again?

        It is only a matter of time until we are overtaken by hostile kendren. Your presence mocks our fate.

**Choices:**
- **choice** `?` → `KindrishReturnAfter`
    > Hindriarch, I have found Kindrish.
- **choice** `?` → `End`
    > You will find a way. Live and drink.

## Nodes

### Node `SlynthRequestAccept`

### Node `SlynthArrived`

### Node `SlynthSettled`

### Node `SlynthRequest`

Don't be coy, =name=. Emboldened by your incursions into our village, you wish to fill it with your indigent foundlings on the weight of your reputation alone. Am I correct?

**Choices:**
- **choice** `?` → `SlynthRequestReject`
    > I... suppose so, yes.

### Node `SlynthRequestReject`

Then I overestimated your intellect further than I realized. Get out.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `SlynthAbout`

The slynth? What of them?

### Node `Start`

Live and drink, kendren. I am Hindriarch Keh; welcome to Bey Lah.

        It's nearly unprecedented for one such as you to pass by our scouts unaccosted, but these are unprecedented circumstances. I have a task for you. Are you interested?

**Choices:**
- **choice** `?` → `Yes. Go on.`
    > Yes. Go on.
- **choice** `?` → `No.`
    > No.

### Node `Yes. Go on.`

Good.

        We hindren are a close-knit and staid people, and our safety depends on our solidarity. In order to preserve our safety and culture, we ask that any of our number who leave us never come back. Recently, one such exile took the treasure of our village, a bracelet named Kindrish, with her when she left. None of our number can leave to get it back, or it will be a violation of the values that I have guarded, and the Hindriarchs before me, for countless generations.

        Will you help us recover our treasure? We have a small cache of valuables we can offer as a reward.

**Choices:**
- **choice** `?` → `Accept`
    > All right. I'll find your treasure.
- **choice** `?` → `No.`
    > No thank you. I don't care for this job.

### Node `Accept`

Excellent. I will do my best to reward you to your satisfaction.

        Though her name is sand in my mouth now, the exile who stole Kindrish is called Eskhind. She left a few weeks ago, and took her sister and brother with her. I don't know where she's gone, but Warden Neelahind might, as they were close friends as children.

        Find the exile called Eskhind and retrieve Kindrish from her, even... even if the cost is the life of her and her siblings. Kindrish has been handed down over countless generations, and it belongs to my people, not any individual. Go, kendren. Speak to Warden Neelahind, and find out where Eskhind is hidden.

**Choices:**
- **choice** `?` → `End`
    > As you say.

### Node `No.`

Then I will thank you to leave as quickly as possible. I don't want the faundren to become used to our borders being permeable.

**Choices:**
- **choice** `?` → `End`
    > As you say. Live and drink.

### Node `KindrishReturnBefore`

You've found our treasure? I'll admit, kendren, I'm very impressed. Take this as thanks.

        That said, the exile must answer for her crimes. There is further reward for you if you see this case through to the end.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Hindriarch.

### Node `KindrishReturnAfter`

You've found our treasure? I'll admit, kendren, I'm very impressed.

        Take this as thanks, and... well. I suppose you've earned your stay for a while. Just try not to give the faundren any ideas.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Hindriarch.

### Node `Start`

You're back. Have you found the exile and retrieved our treasure?

**Choices:**
- **choice** `?` → `KindrishReturnBefore`
    > I have found Kindrish, but not Eskhind.
- **choice** `?` → `Dead`
    > Eskhind is dead, but Kindrish was not on her body.
- **choice** `?` → `I have not.`
    > I have not.

### Node `I have not.`

Perhaps you should get back to it rather than hanging around my village. Warden Neelahind may be able to help you.

**Choices:**
- **choice** `?` → `End`
    > As you say. Live and drink.

### Node `Dead`

Ayvah. She must have sold it. Tell no one about this. Please understand that I cannot reward you, as you did not complete the task I asked of you.

**Choices:**
- **choice** `?` → `End`
    > Understandable. Live and drink.
- **choice** `?` → `End`
    > Unacceptable. Prepare to die.
    - _part: `StartFight`_

### Node `Start`

Why is an exile standing in my village? Are you trying to play me for a fool?

**Choices:**
- **choice** `?` → `KindrishReturnBefore`
    > Hindriarch, I have found Kindrish, but Eskhind did not have it.
- **choice** `?` → `Accused`
    > Eskhind claims to be wrongfully accused.

### Node `Accused`

The pariah claims to be wrongfully accused, and you believe her?

        She is obviously lying. Are all kendren so gullible?

**Choices:**
- **choice** `?` → `Proof`
    > There is no proof that she is lying.

### Node `Proof`

Fine! Go to the Warden, then, and have her solve this mystery.

        But know this: until a thief is found and Kindrish is recovered, I cannot reward you. You get nothing. Live and drink, =player.formalAddressTerm=.

**Choices:**
- **choice** `?` → `End`
    > ...live and drink.

### Node `Start`

Why are you speaking to me? You have work to do.

**Choices:**
- **choice** `?` → `ShowSonnet`
    > Does this poem belong to you?
- **choice** `?` → `Kehstions`
    > I have questions for you.
- **choice** `?` → `End`
    > Live and drink.

### Node `Kehstions`

Fine. What are they?

**Choices:**
- **choice** `?` → `ShowSonnet`
    > Does this poem belong to you?
- **choice** `?` → `Eskxile`
    > Why was Eskhind exiled?
- **choice** `?` → `Kesehind you`
    > Who is your bodyguard?
- **choice** `?` → `Neel before me`
    > Is Neelahind a good warden?
- **choice** `?` → `No brother`
    > Why did you tell me Eskhind had a brother?
- **choice** `?` → `End`
    > That's all. Live and drink.

### Node `Eskxile`

She exiled herself by leaving Bey Lah. Our codes demand that no hindren who leaves us ever return.

        She knew this, and still she chose to leave.

**Choices:**
- **choice** `?` → `Kehstions`
    > I have further questions.
- **choice** `?` → `End`
    > I see. Live and drink.

### Node `Kesehind you`

Kesehind is a good boy. He lost his parents long ago, but has been like a son to me.

        Now his axe-arm is strong where mine is not, and so he lends it.

**Choices:**
- **choice** `?` → `Kehstions`
    > I have further questions.
- **choice** `?` → `End`
    > I see. Live and drink.

### Node `Neel before me`

Warden Neelahind attends to her duties admirably. She is not terribly assertive, but she need not be.

        I'm surprised she's going along with this outsider-led investigation, but she always had a soft spot for the exile.

**Choices:**
- **choice** `?` → `Kehstions`
    > I have further questions.
- **choice** `?` → `End`
    > I see. Live and drink.

### Node `No brother`

If you ask the exile, I'm sure she'll spin some kind of accusation that I believe gender to be an immutable prison, that I impose it on others.

        She's lying. Our people have a long history of two-gender hindren called hartind, respected and consecrated. There is a proper path to gender variance in our society, of which the male exile could have availed himself years ago.

        He never did, so I do not recognize him.

**Choices:**
- **choice** `?` → `Kehstions`
    > I have further questions.
- **choice** `?` → `End`
    > I... see. Live and drink.

### Node `ShowSonnet`

Poem? I detest poetry. Why would one go about learning to write only to use purposefully unclear language, choosing rhyme scheme over clarity?

        Of course it's not mine. Take it back.

**Choices:**
- **choice** `?` → `End`
    > I see. Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageRavaged`_

Gone...

        All gone...

**Choices:**
- **choice** `?` → `End`
    > My condolences.

### Node `Start`  _IfHaveState=`HindrenVillageDoomed`_

I have a terrible feeling that I've brought ill fortune to my village.

        Perhaps it was a mistake to have hired you.

**Choices:**
- **choice** `?` → `End`
    > If you say so. Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

They conspired against me. It is the only explanation.

        You! Leave me alone.

**Choices:**
- **choice** `?` → `End`
    > You will find a way. Live and drink.

### Node `Start`

I should have kept them apart.

        I should have kept all of you apart.

**Choices:**
- **choice** `?` → `End`
    > You will find a way. Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Ah, you again. I'd been doing so well at forgetting your countenance.

        Leave me be.

**Choices:**
- **choice** `?` → `End`
    > Fine. Live and drink.

### Node `Start`

You have a great deal of nerve to speak to me after what you've done.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Some help you are! Now our village lacks a warden.

        How are we to protect ourselves?

**Choices:**
- **choice** `?`
- **choice** `?` → `End`
    > You will find a way. Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Ah, welcome back to the village, =name=. You won't be staying long, will you?

**Choices:**
- **choice** `?`
- **choice** `?` → `End`
    > No. Live and drink.

### Node `Start`

While I appreciate your help, kendren, I would prefer that you not stay longer than you must.

        The faundren might get ideas.

**Choices:**
- **choice** `?`
- **choice** `?` → `End`
    > Fine. Live and drink.
