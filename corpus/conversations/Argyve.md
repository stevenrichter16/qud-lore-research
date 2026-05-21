# Conversation: `Argyve`

_Inherits: (default: BaseConversation)_

_9 start(s), 18 node(s), 1 root-level choice(s)_

---

## Conversation-level choices

- **choice** `Trade`

## Start nodes (conditional entry points)

### Start `MumblingWelcome`

*mumbling* ...exceeding mass thresholds, perhaps a ganglionic teleprojector fitted with suspensors...

**Choices:**
- **choice** `?` → `MumblingWelcome2`
    > ...

### Start `StartHasFetch1`

You're standing in my light! What do you want?

**Choices:**
- **choice** `?` → `GiveKnickknack`
    > Here is your knickknack.
    - _part: `GiveArtifact`_
- **choice** `?` → `End`
    > Nothing. I will return with your knickknack.

### Start `GiveKnickknack`

Ah, mmm, hmmm. Are you a useful one, after all? Go fetch me another!

**Choices:**
- **choice** `?` → `End`
    > If I must.

### Start `StartHasFetch2`

Ah, mmm, hmmm. Are you a useful one, after all? Go fetch me another!

**Choices:**
- **choice** `?` → `Impressive`
    > Here is your knickknack.
    - _part: `GiveArtifact`_
- **choice** `?` → `End`
    > If I must.

### Start `StartBeforeWeirwire`

### Start `TheWire`

The wire! Give it to me!

**Choices:**
- **choice** `?` → `GiveWire`
    > Take the wire.
    - _part: `HaveItem` (Blueprints=Wire Strand Amount=200 Require=true)_
- **choice** `?` → `End`
    > I don't have enough yet.

### Start `ConduitWorking`

It's working! Genius! Genius! Noise in the static- I hear it! I hear!... what's this? What *is* that? Wait...

**Choices:**
- **choice** `?` → `Signal1`
    > ...

### Start `StartFinishedCanticle`

*Argyve gives a curt nod and extended cock of an eyebrow.*

      Apprentice.

      *Argyve returns to his tasks.*

**Choices:**
- **choice** `?` → `Golgotha`
    > The Barathrumites say I must plumb a cave called Golgotha before joining them.
- **choice** `?` → `RankUp`
    > Argyve, I am no apprentice. The Barathrumites call me =factionaddress:Barathrumites= now.
- **choice** `?` → `AskAfter`
    > Need anything, Argyve?
- **choice** `?` → `End`
    > Farewell, Argyve.

### Start `StartCanticleActive`

My apprentice! What?

**Choices:**
- **choice** `?` → `WhoBarathrumites`
    > Who are the Barathrumites again?
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `MumblingWelcome2`

Oh, I didn't notice you there. That's because I was ignoring you.

**Choices:**
- **choice** `?` → `MumblingWelcome3`
    > ...

### Node `MumblingWelcome3`

*mumbling* ...waste heat from the thermo cask? Or centrifugal extraction to the p-density of sunslag...

**Choices:**
- **choice** `?` → `Knickknack`
    > ...

### Node `Knickknack`

*mumbling* ...unexpected deviation from the Klanq constant.

				*Argyve coughs.*

				Must you bother me? What are you, some sort of waterfreak? Faundren-eyed pilgrim? Arconaut? Make =player.reflexive= useful and fetch me a knickknack from one of the caves, then. I may "reward" you.

**Choices:**
- **choice** `?` → `Cave`
    > Where can I find a cave?
- **choice** `?` → `End`
    > I'm not interested.

### Node `Cave`

There are caves everywhere, you dolt! Scoop the surface of the marsh, or head on east to the rust wells, or wander into the Desert for all I care...

**Choices:**
- **choice** `?` → `End`
    > I will return with your knickknack.
- **choice** `?` → `End`
    > I'm not interested.

### Node `Impressive`

*Argyve whistles.*
				
				Impressive, you! Maybe you're fit to poke around my workshop and swap scrap with me. I have been wanting another apprentice. So unfortunate about Skref, what with the disembowelment and all. Take a seat, there.

**Choices:**
- **choice** `?` → `Weirdwire`
    > ...

### Node `Weirdwire`

*Argyve raises both eyebrows.*
				
				Now, to screw the nut on the bolt with an explanation! I'm on the cusp, you see. A grand discovery. The Weirdwire Conduit is near assembled, and once it is, we'll be able to chat with anyone... in instant time! from here to the Yd Freehold. But before I can finish, I need wire. As much as you can find... at least two hundred feet. You should be able to scavenge it from the rust wells.

**Choices:**
- **choice** `?` → `End`
    > I'll fetch you your wire.
- **choice** `?` → `End`
    > I'm not interested.

### Node `GiveWire`

*Argyve hoots*
				
				Yes, yes! Beautiful wire! -oh, before I forget, I repaired an old recoiler for you. Use it whenever you wish to hop back to Joppa quickly. Now, give me a few moments to attach the wire...

**Choices:**
- **choice** `?` → `End`
    > I will return.
    - _part: `ReceiveItem` (Blueprints=Joppa Recoiler Identify=*)_
    - _part: `TakeItem` (Blueprints=Wire Strand Amount=200)_

### Node `Signal1`

It's repeating itself...

**Choices:**
- **choice** `?` → `Signal2`
    > ...

### Node `Signal2`

*Argyve mumbles to himself for several minutes.*

**Choices:**
- **choice** `?` → `Signal3`
    > ...

### Node `Signal3`

Apprentice! Come, here! Something strange is occurring. The Conduit is picking up a signal, some sort of repeating transmission. I cannot decipher it, however. I lack cryptogull eggs and, well, never you mind! I have a great task for you, my apprentice. Do you accept it?

**Choices:**
- **choice** `?` → `Canticle1`
    > Can I know what it is?

### Node `Canticle1`

-yes. You must seek out Barathrum the Old, the eldest and wisest tinker alive. He lives with his followers the Barathrumites under the arch of Grit Gate to the northeast, in the jungle-strangled ruins of Qud. He will know what to make of the signal.

**Choices:**
- **choice** `?` → `WhoBarathrumites`
    > Who are these Barathrumites?
- **choice** `?` → `CanticleAccept1`
    > I require no further information. I will go.

### Node `WhoBarathrumites`

Disciples of Barathrum. Mostly urshiib, like their mentor- quilled albino bears who prefer their candle-dim caves to the sun-salted surface of the jungle. A thousand years ago Barathrum and his kin crossed the Homs Delta into the rusting heart of Qud. He has spent centuries peeling the chrome shells off time's artifacts in his workshop. If he cannot decipher the signal, no one can.

**Choices:**
- **choice** `?` → `CanticleAccept1`
    > I accept the task, Argyve.
- **choice** `?` → `End`
    > I must think on this.
- **choice** `?` → `End`
    > Farewell, Argyve.

### Node `CanticleAccept1`

Splendid! Perfect! Let me record the signal to disk, which you'll need to guard with your life, I'm afraid.

				I'll rig up a droid scrambler for you, too. You see, the Barathrumites have programmed a troupe of waydroids to guard the approach to Grit Gate. With the scrambler, you'll needn't worry about them. Wait there.

**Choices:**
- **choice** `?` → `CanticleAccept2`
    > ...

### Node `CanticleAccept2`

*Argyve mumbles to himself for several minutes.*

**Choices:**
- **choice** `?` → `CanticleAccept3`
    > ...

### Node `CanticleAccept3`

Here you are. Now, go! Off with you! May you live long enough to do my bidding. Away, away!

**Choices:**
- **choice** `?` → `End`
    > Farewell, Argyve.
    - _part: `ReceiveItem` (Blueprints=Droid Scrambler,Argyve's Data Disk Identify=All)_

### Node `Golgotha`

Do they? Yes, yes, Otho might. Hmm.

        *Argyve pauses for an uncomfortably long time.*

        Well.
      
        *Another pause, this one even more long and uncomfortable than the last*

        Good luck!

### Node `RankUp`

Did they, now? Well you're not MY =factionaddress:Barathrumites=!

      Grit Gate is not Joppa, you pridesome solder-nail, and in this house you are apprentice still.

      Now, what did you want? Be quick!

### Node `AskAfter`

-what?

      No, no, I'm far too engrossed to see to your curiosity. I'm sure the Barathrumites have something for you to do.
