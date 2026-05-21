# Conversation: `Otho`

_Inherits: `BaseSlynthMayor`_

_0 start(s), 42 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Welcome to Grit Gate. I am Otho, Barathrum's steward. I apologize for the manner of our introduction, but we must take precautions. Qud is a very unforgiving place.

        You demonstrate tremendous promise to have returned from Golgotha with such inexperience. Take this firearm as your reward. It bears the mark of our finest gunsmith, Sparafucile. Take this bracelet, as well.

        Return when you are ready to discuss the signal.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
- **choice** `?` → `End`
    > Thank you. I will return.
    - _part: `ReceiveItem` (Blueprints=MasterworkCarbine,MasterworkChainPistol Pick=true Identify=All)_
    - _part: `ReceiveItem` (Blueprints=Hologram Bracelet Identify=All)_
    - _part: `GritGateHandler` (Rank=Apprentice)_

### Node `Start`

Welcome to Grit Gate. I am Otho, Barathrum's steward. I apologize for the manner of our introduction, but we must take precautions. Qud is a very unforgiving place.

        I am pleased to see that you've returned with the waydroid, though you still know little of the dangers you bear. Take this firearm as your reward. It bears the mark of our finest gunsmith, Sparafucile.

        Return when you are ready to discuss the signal.

**Choices:**
- **choice** `?` → `End`
    > Thank you. I will return.
    - _part: `ReceiveItem` (Blueprints=MasterworkCarbine,MasterworkChainPistol Pick=true Identify=All)_
    - _part: `GritGateHandler` (Rank=Apprentice)_

### Node `Start`

Welcome to Grit Gate. I am Otho, Barathrum's steward. I apologize for the manner of our introduction, but we must take precautions. Qud is a very unforgiving place.

        You are worthy to study with us. Take these.

        Return when you are ready to discuss the signal.

**Choices:**
- **choice** `?` → `End`
    > Thank you. I will return.
    - _part: `ReceiveItem` (Blueprints=EMPGrenade3,ColdGrenade3,StasisGrenade3 Identify=All)_
    - _part: `GritGateHandler` (Rank=Apprentice)_

### Node `Start`

It takes more than a willing spirit to be trusted here, wayfarer.

        Prove your worth and bring us a waydroid, and we will have more to speak of.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Start`

Are you ready to discuss the signal?

**Choices:**
- **choice** `?` → `Signal`
    > Yes.
- **choice** `?` → `End`
    > No.

### Node `Signal`

The signal is a repeat transmission being broadcast from an unknown source.=V0tinkeraddendum= One of our tinkers, Q Girl, discovered it while rigging a long wave detector. Unfortunately, it's encrypted, and we do not have the means here to decrypt it. You may be of some help in this matter, however.

        We've long known the location of a fully functioning baetyl within the bowels of the great hall Bethesda Susa. The Mechanimists have consecrated the site around it and built a temple there. Q Girl claims to have developed a means to decrypt the signal, but she needs the computing power of the baetyl. If you can infiltrate the Mechanimist compound, you may be able to engage the baetyl and decode the signal.

**Choices:**
- **choice** `?` → `Baetyl?`
    > What is a baetyl?

### Node `Baetyl?`

They are antique stones located in certain places deep within the caverns of Qud. We believe they are some sort of hyper-advanced machines built by the Eaters. Often one claims to possess a sentience of its own. However, most of them have gone haywire in the eons since their creation; it is rare indeed to discover one whose circuitry is wholly uncorroded.

        The Mechanimists worship this one as an idol, and they will protect it at all costs. You will need to find a way through their host to the baetyl itself.

        Do you believe you can accomplish this task?

**Choices:**
- **choice** `?` → `Bethesda1`
    > Yes, I do.
- **choice** `?` → `End`
    > I must think on this task.

### Node `Bethesda1`

Good, =factionaddress:Barathrumites=. Speak to Q Girl in the workshop. She'll encode her instructions for the baetyl onto a copy of the disk.

        There's one more thing. The baetyl is located beneath the ancient cryobarrios of the Eaters. Time has worked to erode the mechanisms that contain their cryogenic mist. That freezing vapor billows out of the chambers freely now, cooling the entire cavern. You will want to procure warm clothing to protect =player.reflexive=.

        The spoils of the Mechanimists are yours to keep. Remember, =factionaddress:Barathrumites=, Barathrum will look kindly upon your service.

**Choices:**
- **choice** `?` → `End`
    > I will return with the data, Steward.

### Node `Start`

Luck be with you in the lair of Bethsaida, =factionaddress:Barathrumites=.

**Choices:**
- **choice** `?` → `End`
    > I will return with the data, Steward.

### Node `Start`

You return. Have you succeeded in decoding the signal?

**Choices:**
- **choice** `?` → `PresentTheDisk`
    > Yes.

### Node `PresentTheDisk`

Well done, =factionaddress:Barathrumites=. Present the disk.

**Choices:**
- **choice** `?` → `InterpretSignal`
    > [Give Otho the disk]
    - _part: `GritGateHandler` (Rank=Journeyfriend)_

### Node `InterpretSignal`

I must bring the decoded signal to Barathrum immediately. Return in a few hours. By then I'll have discussed our next course of action with Barathrum and will have further instructions for you.

**Choices:**
- **choice** `?` → `End`
    > As you say, steward.

### Node `Start`

=factionaddress:Barathrumites|capitalize=, I have no further instructions for you yet. Return soon.

**Choices:**
- **choice** `?` → `End`
    > As you say, steward.

### Node `Start`

=name=, I've brought the decoded signal to Barathrum, and he's finished musing on it. We have fresh instructions for you, =factionaddress:Barathrumites=. Are you ready to hear them?

**Choices:**
- **choice** `?` → `Overripe`
    > Yes.

### Node `Overripe`

Barathrum needs you for an undertaking of great importance. You must journey to Omonporch far to the north. There the Spindle stretches from earth to sky. Unfortunately, a troublesome merchant from the Consortium of Phyta has relocated there and declared xerself Earl of Omonporch. We need you to broker a deal so that we may lease control of the Spindle. Failing that, you'll need to dispose of the self-appointed Earl.

        Be careful on your approach to Omonporch, =factionaddress:Barathrumites=. So far east into the reaches of Qud, the Putus Templar lie in wait.

**Choices:**
- **choice** `?` → `Ripe1`
    > Who are the Putus Templar?
- **choice** `?` → `Ripe2`
    > What is the purpose of this?
- **choice** `?` → `End`
    > I will secure the Spindle for Barathrum.
- **choice** `?` → `End`
    > I must think on this task.

### Node `Ripe1`

The Putus Templar, or the Sons and Daughters, as they call themselves, are an order of knights who claim descendancy from the Eaters, the ancient folk who wrought the chrome halls of Qud. Beware them, for while they despise all mutants, they harbor a special malice for Barathrum.

        Take care that you do not find =player.reflexive= inside one of their slave pens.

**Choices:**
- **choice** `?` → `Ripe2`
    > What is the purpose of this?
- **choice** `?` → `End`
    > I will secure the Spindle for Barathrum.
- **choice** `?` → `End`
    > I must think on this task.

### Node `Ripe2`

That will be revealed to you in due time.

        Do not forget your place, =factionaddress:Barathrumites=.

**Choices:**
- **choice** `?` → `Ripe1`
    > Who are the Putus Templar?
- **choice** `?` → `End`
    > I will secure the Spindle for Barathrum.
- **choice** `?` → `End`
    > I must think on this task.

### Node `Start`

It's as I feared, =name=. Grit Gate is being assailed. The Putus Templar must have followed you back from Omonporch.

        Let us use the precious little time we have before they arrive to prepare our defenses.

**Choices:**
- **choice** `?` → `BeginCallToArms`
    > What can I do?

### Node `Start`

Go to the mainframe room and scan the shale surrounding Grit Gate for anomalies. Now, =name=!

**Choices:**
- **choice** `?` → `End`
    > I'll go now.

### Node `BeginCallToArms`

With the chrome key card I gave you, you now have access to our power grid. There are chain laser emplacements and force projectors across the enclave. Use Ereshkigal's reconnaissance to decide which defenses to enable. You can also broadcast an overclock command or activate Rodanis Y by interfacing with Ereshkigal.

        Be mindful of the amperage draw, though. If you overdraw the grid, you could cause brownouts.

        Act quickly, =name=! The Templar near us even as we speak.

**Choices:**
- **choice** `?` → `End`
    > I'll do my best to defend Grit Gate.

### Node `Start`  _IfHaveState=`CallToArmsStarted`_

That rumbling... what was it? An explosion? Hmm...

**Choices:**
- **choice** `?` → `BeginGraveTidings`
    > What are you thinking, Otho?

### Node `BeginGraveTidings`

Grave thoughts, =name=. Listen to me now. Take this key card, go to Ereshkigal's room, and-- oh, that's the mainframe. It's what she prefers to be called.

        Go to her room, access Ereshkigal, and scan the shale surrounding the enclave for anomalies. I've asked her to ready her sensors.

        Update me with what you learn. You may use the intercom in the northeast corner of Ereshkigal's room to deliver your update.

        Go, quickly! I'd soon be disabused of my fears.

**Choices:**
- **choice** `?` → `End`
    > I'll go now.

### Node `Start`

You can still activate our defenses, =name=. There are chain laser emplacements and force projectors across the enclave. Use Ereshkigal's reconnaissance to decide which defenses to enable. You can also broadcast an overclock command or activate Rodanis Y by interfacing with Ereshkigal.

        Be mindful of the amperage draw, though. If you overdraw the grid, you could cause brownouts.

**Choices:**
- **choice** `?` → `End`
    > I'll do my best to defend Grit Gate.

### Node `Start`

Have you secured the Spindle yet?

**Choices:**
- **choice** `?` → `CompleteSpindle`
    > Yes, the Spindle is ours.
- **choice** `?` → `End`
    > No, not yet.

### Node `Start`

Leave me alone for a moment, =factionaddress:Barathrumites=. I have duties to attend.

**Choices:**
- **choice** `?` → `End`
    > I will return later, Otho.

### Node `CompleteSpindle`

That is sterling news, =factionaddress:Barathrumites=. I'll go inform Barathrum straightaway.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
    - _part: `GritGateHandler` (Invasion=true)_

### Node `IntroduceBarathrum`

Furthermore, I spoke with Barathrum. He praised your handling of the Earl of Omonporch, and he thanks you for the bravery you exhibited in defending Grit Gate.

        The attack today reminds us: for too long have we put our faith in the isolation of our guild and the preoccupations of the Putus Templar. The looming threat of another attack impels Barathrum to accelerate his plans, and with them, your position in our guild.

        You are raised to Disciple, =player.formalAddressTerm=. Barathrum wishes to speak with you immediately.

**Choices:**
- **choice** `?` → `Barathrum`
    > He wishes to speak to me? Barathrum himself?
    - _part: `GritGateHandler` (Rank=Disciple)_

### Node `Start`

I spoke with Barathrum. He praised your handling of the Earl of Omonporch, and he thanks you for the bravery you exhibited in defending Grit Gate.

        The attack today reminds us: for too long have we put our faith in the isolation of our guild and the preoccupations of the Putus Templar. The looming threat of another attack impels Barathrum to accelerate his plans, and with them, your position in our guild.

        You are raised to Disciple, =player.formalAddressTerm=. Barathrum wishes to speak with you immediately.

**Choices:**
- **choice** `?` → `BarathrumHaveKey`
    > He wishes to speak to me? Barathrum himself?
    - _part: `GritGateHandler` (Rank=Disciple)_
- **choice** `?` → `Barathrum`
    > He wishes to speak to me? Barathrum himself?
    - _part: `GritGateHandler` (Rank=Disciple)_

### Node `Barathrum`

Yes, =factionaddress:Barathrumites=. Take this key and follow the stairs down to his study. He awaits.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Otho.

### Node `BarathrumHaveKey`

Yes, =factionaddress:Barathrumites=. Follow the stairs down to his study. He awaits.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Otho.

### Node `Start`

I am busy, wayfarer. Please talk to Mafeo in the trade square if you need something.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Start`

=factionaddress:Barathrumites|capitalize=! You have my deepest gratitude. Few =player.personTerm|pluralize= could have defended Grit Gate so deftly.

        Now, give me time to assess our losses and consult with Barathrum. Return soon.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Otho.

### Node `Start`  _IfHaveState=`ACallToArms_TopScore`_

Given the circumstances, this is a remarkable lack of destruction. Your defense of Grit Gate was first-class, =name=.

**Choices:**
- **choice** `?` → `IntroduceBarathrum`
    > Thank you for the update, Otho.

### Node `Start`  _IfHaveState=`ACallToArms_MidScore`_

Much was lost, but such is what I expected. Once again, thank you for efforts, =name=.

**Choices:**
- **choice** `?` → `IntroduceBarathrum`
    > Thank you for the update, Otho.

### Node `Start`  _IfHaveState=`ACallToArms_BottomScore`_

Such tremendous loss. I wonder if more could have been done to prevent it.

**Choices:**
- **choice** `?` → `IntroduceBarathrum`
    > Thank you for the update, Otho.

### Node `Start`

Yes, =name=?

**Choices:**
- **choice** `?` → `End`
    > Live and drink, steward.

### Node `SlynthRequest`

Be straightforward, disciple. You mean to ask if we will house them.

### Node `SlynthRequestAccept`

I am uncertain that you know the enormity of what you ask me, =name=. Nonetheless, I cannot deny what you have done for our order. These slynth must be tested as you were, but should they show the mettle and drive set by your example, we will accept them as apprentices.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, Otho.

### Node `SlynthRequestReject`

You have grown bold beyond your station. What you have asked of us you have not earned. If you must ask again, become worthier first.

### Node `SlynthAbout`

Has this slynth situation been settled yet?

### Node `SlynthArrived`

I did not expect to admit this, disciple, but the refugees have met my expectations. Like you, they have shown more than a willing spirit in work and curiosity both.

        The slynth have promise, and you may have been right to bring them to us.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, Otho.

### Node `SlynthSettled`

Live and drink, disciple.

        You will be pleased to know that the slynth have proven themselves worthy of apprentice status. They will reside here for as long as they uphold and serve the tenets of our order.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, Otho
