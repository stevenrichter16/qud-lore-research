# Conversation: `ChavvahPrime`

_Inherits: `BaseSlynthMayor`_

_1 start(s), 28 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

## Nodes

### Node `WelcomeNoPhysiology`

We share the bright and now, traveler =name=.

**Choices:**
- **choice** `?` → `Chavvah`
    > What is this place?
- **choice** `?` → `Name`
    > Who are you?
- **choice** `?` → `Chime`
    > The entity I spoke with at Eyn Roj mentioned a chiming rock...
- **choice** `?` → `ActiveQuest`
    > Explain once more what I must do with Tau's chime.
- **choice** `?` → `DoneQuest`
    > I've reunited Tau with her chime.
- **choice** `?` → `DoneQuest`
    > I've destroyed the chime, Dyvvrach.
- **choice** `?` → `BarathrumChavvahDone`
    > I have completed the ritual of -elseing. Will you power Barathrum's starclimb, as you said?
- **choice** `?` → `Barathrum`
    > I come in the name of need. Barathrum asks the strength of your psyche to power our starclimb.
- **choice** `?` → `End`
    > Live and drink.

### Node `Chavvah`

This keter roams above my trunk at Eyn Roj, traveler =name=, and across the Stair I dream. You found me, this keter where I chime in dozens.

### Node `Chime`

Ah, I am in need, and so I turned my chimes trunkward to tune. You struck the chime and now you are here. Are you a waterhand, and free?

**Choices:**
- **choice** `?` → `Work`
    > What do you need?
- **choice** `?` → `Barathrum`

### Node `Work`

My chimeling Tau leaves Chavvah, leaves me. It is her choice.

				Her transit-psyche manifests at the bottom of Taproot, where we cannot consciously go. To finish the ritual of -elseing, to let Tau become -else, I need a traveler such as you, =name=.

**Choices:**
- **choice** `?` → `Work2`
    > What must I do?
- **choice** `?` → `Tau`
    > Who is Tau?
- **choice** `?` → `Chime`
- **choice** `?` → `Barathrum`

### Node `Work2`

Take Tau's chime, silent and still. Carry it to the bottom of Taproot, deep under my trunk, where she will make the chime her transit-body and walk away forever. Finish the ritual of -elseing.

				At the bottom of Taproot, Tau manifests. She tells us, too, that another waits for her there.

**Choices:**
- **choice** `?` → `Accept`
    > I will do as you ask.
- **choice** `?` → `Welcome`
    > I have more to ask, first.

### Node `ActiveQuest`

Take Tau's chime, silent and still. Carry it to the bottom of Taproot, deep under my trunk, where she will make the chime her transit-body and walk away forever. Finish the ritual of -elseing.

				At the bottom of Taproot, Tau manifests. She tells us, too, that another waits for her there.

### Node `DoneQuest`

So you have, and what proceeds, proceeds.

				I felt your coming here, =name=, in Gyredream. I've felt this moment. I feel it now.

				The ritual of -elseing is complete, waterhand. You are done, and with our thanks.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
    - _part: `IfThenElseAchievement`_

### Node `Accept`

Thank you, traveler =name=.

**Choices:**
- **choice** `?` → `Welcome`
    > ...

### Node `Tau`

My chimeling, burning bright, all starlight and right angles in her heart. She leaves Chavvah; it is her choice. I..

**Choices:**
- **choice** `?` → `Work2`
    > What must I do?
- **choice** `?` → `Chime`
- **choice** `?` → `Barathrum`

### Node `Name`

A sophist of the Self spilled ink and called me, long ago, the Tree of Life. To me, I am the many Selves pinched up my taproot from the permeating Soft.

				I am Chavvah, and I am dyvvrach.

**Choices:**
- **choice** `?` → `ManySelves`
    > Many selves? What does this mean?

### Node `ManySelves`

As Chavvah I am many. As dyvvrach I am one. I am one and many. One-selves have called me tree city, the sentient place. You may think of the Selves this way, sprouted in keter from Twofirm.

**Choices:**
- **choice** `?` → `Physiology`
    > Twofirm?

### Node `Physiology`

Deep under earth and permeating our roots is Soft, our feeling substance. Ground pressure pushes it up the taproot to our trunk, where it condenses into Twofirm: the biformal phase that contains the two sefirots, -then and -else.

**Choices:**
- **choice** `?` → `Physiology2`
    > *continue listening*

### Node `Physiology2`

This is the genesis my distinct Self, an awareness that contains both -then, what I will become, and -else, what I will not. Twofirm flows up my sapwood to the keter, where -then manifests as an entity and I chime: I speak and hear the world.

### Node `BarathrumChavvahDone`

*Dyvvrach chimes*

**Choices:**
- **choice** `?` → `BarathrumChavvahDone2`
    > ...

### Node `BarathrumChavvahDone2`

You have completed the ritual of -elseing. You have set bright Tau free.

				Yes, =name=. I will turn my chimes Spindleward to tune, then vibrate at our verve frequency. I will power your starclimb.

				Be vested to tell whoever you must that Chavvah has made this commitment.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Dyvvrach. Live and drink.

### Node `Barathrum`

I start at this but Tikva settles me. I remember now: from a cub I've known Barathrum to be weak in telling but bold in asking. A starclimb? You mean, an ascent to the long chiming rock?

**Choices:**
- **choice** `?` → `Ascent`
    > Barathrum intends to ascend the Spindle to discover the source of the Signal, yes. He needs a power source for the climber, one shielded from electromagnetic disturbance.

### Node `Ascent`

oh. This. Was this felt in gyredream? Your coming to keter? I ask, do not answer.

**Choices:**
- **choice** `?` → `Gyredream`
    > What is gyredream?

### Node `Gyredream`

A future shock. My chimeling _ is vision-gifted, a lichen who clings to shorerock on the straits of Tomorrow. Just a short time ago a sea wave crested and broke beneath her, and she saw in its recession all the bright and violent channel paths.

				We all felt it. A recoming, and the gyre in final tension. I felt...

**Choices:**
- **choice** `?` → `GyredreamMore`
    > *continue listening*

### Node `GyredreamMore`

It was too much for my chimeling Tau. She gasped for air and her chime stilled. She leaves us now, to become -else. It is her choice.

**Choices:**
- **choice** `?` → `WillYouHelp`
    > I am sorry. But will you help Barathrum do as he asks?
- **choice** `?` → `WillYouHelp_ChavvahFinished`
    > I am sorry. But will you help Barathrum do as he asks?

### Node `WillYouHelp`

*Dyvvrach chimes*

**Choices:**
- **choice** `?` → `WillYouHelp2`
    > ...

### Node `WillYouHelp2`

I will power his starclimb. If you take Tau's chime to taproot, for her to walk away. If you finish the ritual of -elseing.

**Choices:**
- **choice** `?` → `Work`
    > The ritual of -elseing?
- **choice** `?` → `Welcome`
    > I see.

### Node `WillYouHelp_ChavvahFinished`

*Dyvvrach chimes*

**Choices:**
- **choice** `?` → `BarathrumChavvahDone2`
    > ...

### Node `SlynthRequest`

Again I must be calmed, but the startling gives way to a curiosity. You speak of the glowfolk, belimbed and free. You asking that they join us, like our Sant?

### Node `SlynthRequestAccept`

We find no precedent for this, yet is there space upon our crystal arms and an openness within us. It is agreed: if these slynth will be of us, we will have them here.

**Choices:**
- **choice** `?` → `End`
    > You all have my thanks.
    - _part: `AddSlynthCandidate` (Sanctuary=the roaming keter of Chavvah)_

### Node `SlynthRequestReject`

I startle, and the roiling is felt before the calm. I cannot find a consensus for the housing of these beings, =name=. I am sorry.

### Node `SlynthAbout`

We await the decision of the glowfolk. Our imaginations run with the possibilities.

### Node `SlynthArrived`

How this keter rustles! The slynth are among us and we adapt, our impressions a melange of excitement, apprehension, and wonder.
        
        Though I have no single sentiment to express, we nonetheless approach -then with our new companions.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, dyvvrach.

### Node `SlynthSettled`

You are well-found, =name=. Though several have chosen their -else, the first of the slynth have joined to us like our Sant, mobile and apart but shared and together. This is a strange -then, but what branches may spill forth from it? I anticipate the witnessing.

**Choices:**
- **choice** `?` → `Start`
    > Live and drink together, Chavvah.
