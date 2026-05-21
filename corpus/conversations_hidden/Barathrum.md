> ⚠️  **SPOILER WARNING.** This conversation is in `HiddenConversations.xml`,
> which the game flags `ExcludeFromCorpusGeneration='true'`. Contents may
> include endgame branches (Spindle ascent, Coda, late-quest reveals).

# Conversation: `Barathrum`

_From HiddenConversations.xml_

_Inherits: (default: BaseConversation)_

_7 start(s), 49 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `AllDone`  _IfTestState=`BaraAllDone`_

*Barathrum mumbles inaudibly.*

**Choices:**
- **choice** `WaterRitualChoice`
- **choice** `Trade`
- **choice** `?` → `End`
    > ...

### Start `Z-Ascended`  _IfHaveState=`(SpindleAscended AND GyreTruthKnown)`_

*Barathrum's countenance suddenly gravens.*
        
        O.. I know it to be arduous for you, meyvn, to see me like this. The imago unstrung...

**Choices:**
- **choice** `WaterRitualChoice`
- **choice** `Trade`
- **choice** `?` → `Z-Ascended2`
    > ...

### Start `Z-Ascended-No-Reveal`  _IfHaveState=`SpindleAscended`_

*Barathrum's countenance suddenly gravens.*

        Child. There is much more I would have liked to share. But... I am a puppet of my shame.

**Choices:**
- **choice** `WaterRitualChoice`
- **choice** `Trade`
- **choice** `?` → `Z-Ascended2`
    > ...

### Start `Z-Silent`  _IfHaveState=`BarathrumDone`_

*Barathrum mumbles inaudibly.*

**Choices:**
- **choice** `WaterRitualChoice`
- **choice** `Trade`
- **choice** `?` → `End`
    > ...

### Start `Z-Hushed`  _IfHaveState=`BarathrumWeeps`_

*Barathrum weeps.*

**Choices:**
- **choice** `WaterRitualChoice`
- **choice** `Trade`
- **choice** `?` → `End`
    > ...

### Start `Z-SteelOurselves`  _IfHaveState=`BarathrumCusp`_

**Choices:**
- **choice** `WaterRitualChoice`
- **choice** `Trade`
- **choice** `?` → `End`
    > ...

### Start `Z-Ascending`  _IfHaveState=`StarfreightAscending`_

We've-

        We've done it, =name=. I-

**Choices:**
- **choice** `WaterRitualChoice`
- **choice** `Trade`
- **choice** `?` → `Dawnstirs`
    > ...

## Nodes

### Node `Z-Ascended2`

I am sorry, =name=. I am so proud of you! I wish... I wish it were I did not peel, like your model.

**Choices:**
- **choice** `?` → `Z-Ascended3`
    > ...

### Node `Z-Ascended3`

Farewell, now, meyvn. =name=. Live and drink.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Dawnstirs`

Only in the Shallows' dawnstirs did I let myself think it possible. And now...

**Choices:**
- **choice** `?` → `SortFaculties`
    > ...

### Node `SortFaculties`

*Barathrum exhales with effort.*

        Let us sort our faculties before we reach the rim of our ascent. There is the edge of our journey still to lathe.

**Choices:**
- **choice** `?` → `BarathrumCusp`
    > Barathrum, let us again talk about the past.
- **choice** `?` → `TemplarDefeated`
    > The Templar are defeated, but will they return in force?
- **choice** `?` → `Well`
    > Barathrum, you look pained. Are you well?
- **choice** `?` → `Awaits`
    > By your guess, what awaits us where the Spindle breaks?
- **choice** `?` → `End`
    > I would like a moment, Barathrum.

### Node `TemplarDefeated`

I cannot say, =name=. But I know it's facile to believe a living heritage can be evanesced in one stroke. We are always downstream of a past violence.

### Node `Well`

*Barathrum shifts his weight, pauses, and flexes an arthritic paw.*

        I am sorry. Tis the acceleration, =name=. I am whirling and empty of breath. Steel yourself, and so shall I.

### Node `Awaits`

*Barathrum pauses.*

        O, =name=, our cursors draw together on Fate's phenomenic slide rule! You burn with speculation, and I- I molder in the coolness of knowing. I enter my dwarf phase.

**Choices:**
- **choice** `?` → `Awaits2`
    > ...

### Node `Awaits2`

*Barathrum takes in a long breath.*

**Choices:**
- **choice** `?` → `Awaits3`
    > ...

### Node `Awaits3`

O, deceit! The grueling gate I crossed on every tilt of glittering dusk. I slept in my crimeclothes and wept, did you hear?

        Or could you hear only the damnable static, like me, and speak naught to the machine that belches it out. Heal none of the wounds of its grievous heart, or mine own...

        O, oh... So much to bear.

**Choices:**
- **choice** `?` → `NoMask`
    > I found a torn sheet of graph paper with a note about deceit. Was it yours?
- **choice** `?` → `NoMask`
    > Your crimeclothes? There was a codex about crimes and punishments near the bedroll in your study. What was it?
- **choice** `?` → `NoMask`
    > The svardym Mak said he was born to a cacophony of static ringing his ears raw. Could it have been the signal?
- **choice** `?` → `NoMask`
    > The Svardym Geeub mentioned a machine speaker and her ursine apprentice. Was that you?
- **choice** `?` → `NoMask`
    > Rebekah was a healer. But the daughters of Exile, her acolytes, are tinkers. Why?
- **choice** `?` → `BarathrumRecovers`
    > Barathrum, I don't understand.
- **choice** `?` → `End`
    > Live and drink.

### Node `NoMask`

I-

        *Barathrum pauses, and then he laughs.*

        Ho, ho! Still! The brow narrows in performance even as the play ends! The mask must peel off... What? No mask??

        *Barathrum gravens suddenly.*

        I am sorry, =name=. I wish not to unnerve you with uncharacteristic lightness. You nor the rest deserve this.

**Choices:**
- **choice** `?` → `Graph2`
    > ...
- **choice** `?` → `CrimePunishment`
    > ...
- **choice** `?` → `MakStatic`
    > ...
- **choice** `?` → `GeeubSpeaker`
    > ...
- **choice** `?` → `DaughtersTinkers`
    > ...

### Node `Graph2`

Yes, that paper, twas mine. This racket of a Signal is mine, too, of sorts.

        It is my tolling bell.

**Choices:**
- **choice** `?` → `BarathrumCusp`
    > Your tolling bell?

### Node `CrimePunishment`

That codex? A comfort, a guidebook, a ledger. My crimes have no signatories, but the heart is its own document.

**Choices:**
- **choice** `?` → `BarathrumCusp`
    > What crimes, Barathrum?

### Node `MakStatic`

Svardym Mak's static? Yes, twas the Signal. My signal. My tolling bell.

**Choices:**
- **choice** `?` → `BarathrumCusp`
    > Your tolling bell?

### Node `GeeubSpeaker`

Apprentice. So long since I've worn that title, but it feels right still.
        
        Yes, twas me at the machine speaker's side.

**Choices:**
- **choice** `?` → `BarathrumCusp`
    > Who was the machine speaker?

### Node `DaughtersTinkers`

She was a healer, yes. The wire cutter can perform the work of a scalpel; and the soldering iron, a suture.
        
        To take apart a history, and stitch something new...

**Choices:**
- **choice** `?` → `BarathrumCusp`
    > What did she take apart?

### Node `BarathrumRecovers`

*Barathrum pauses.*
        
        Forgive me, =name=. The ascent strains the mind as well as the body. My flight of fancy is done; I am regrounded.

**Choices:**
- **choice** `?` → `Z-SteelOurselves`
    > ...

### Node `BarathrumCusp`

*Barathrum pauses and frowns.*

        Do you know, =name=, the engine types that ask us to loose every pin and unhinge every cam to know them? Such an engine of culture we are encased in now, and I cannot speak to the workings of one gearset without disassembling them all. I meant not to tease, and soon, I promise, you will spy the next arc of our journey.

**Choices:**
- **choice** `?` → `End`
    > I will wait, Barathrum.
- **choice** `?` → `Z-Reveal0`
    > Barathrum, if the past has some relevance to this moment, I would ask you to share what you know.

### Node `Z-Reveal0`

*Barathrum sighs.*

**Choices:**
- **choice** `?` → `Z-Reveal1`
    > ...

### Node `Z-Reveal1`

It is done, then. Have the explication you are owed.

**Choices:**
- **choice** `?` → `Z-Reveal1a`
    > ...

### Node `Z-Reveal1a`

You see, =name=, when I, a young bruin, crossed the Homs Delta with my flood-fleeing clan and into the western reach of Qud, the plagues of the Gyre were already ascendant. We took root at our new hearth, in the chrome grottos where we urshiib find natural peace, and by the providence of my elders, I was able to study the tinkering craft.

**Choices:**
- **choice** `?` → `Z-Reveal2`
    > ...

### Node `Z-Reveal2`

Through my work I caught the attention of a master machinist, unconventional of method, who took me under her wing and, in time, availed me of the orphic truth.

        She explained, as I've shared with you and the rest of the acolytes, that the world we know once belonged to a grand Coven of beings who spanned the stars. And that, acting on some inscrutable logic, they disappeared. That an injunction was placed on our world.

        This, you know. It is the truth I told, if only half. But Rebekah taught me more.

**Choices:**
- **choice** `?` → `Z-Reveal3`
    > ...

### Node `Z-Reveal3`

Atop the implausible rise of the Spindle roosted a Seraph, one of the great machinic archons of the Eaters, and this being Rebekah served.

        In the short years before I arrived in Qud, the Seraph became convinced that something had changed in the cosmic order. That along the ecliptic of the Folk Clock, some uncounted peg had slid to a priming position, and that the Coven was set to imminently return.

**Choices:**
- **choice** `?` → `FolkClock`
    > The Folk Clock?

### Node `FolkClock`

The Seraph spoke of a Great Machine that spanned galaxies, the motion of whose sails and gear trains directed the fluidic shifting of stars and cultures. But they spoke little of it, and little I know.

**Choices:**
- **choice** `?` → `Z-Reveal4`
    > ...

### Node `Z-Reveal4`

*Barathrum coughs and swallows.*

        To ready our world for the Coven's return, the Seraph, who would be called Resheph, became convinced that all higher life on the planet must... be purged. That it was our life and way of living that moved the Coven to set the injunction. The only way through was for a new life to obtain.

**Choices:**
- **choice** `?` → `Z-Reveal5`
    > ...

### Node `Z-Reveal5`

And so, Resheph seeded the plagues and whorled them via waveform to a breathing gyre. Blights engineered to attack life whilst preserving the planet's artifacts of glass and chrome.

        Rebekah, dear tutor, betrayed Resheph's confidences and apprised me of the plan, so that I might help her dash it apart and save the peoples of our world.

**Choices:**
- **choice** `?` → `Z-Reveal6`
    > ...

### Node `Z-Reveal6`

*Barathrum coughs and exhales a pained whistle.*

        Together we beseeched Resheph, begged them to reverse the Gyre. I pleaded.. I-

        *Barathrum wheezes.*

**Choices:**
- **choice** `?` → `Z-Reveal7`
    > ...

### Node `Z-Reveal7`

I asked for time. Give me time. To reform Qud, extinguish the hatefulness and needless warmaking, to lift our world across the eschaton and prepare it for the Coven's return...

**Choices:**
- **choice** `?` → `Z-Reveal8`
    > ...

### Node `Z-Reveal8`

After a storm of shrapnel words, the Seraph acceded to ten centuries.

        Ten centuries! An eyeblink on the scales of the Folk Clock but an eternity for us. So I believed.

        The rousing Signal would cease, the plagues of the Gyre would be reversed, to the extent they could; for even the potent archon had not full governance over what they had worked into being.

**Choices:**
- **choice** `?` → `Z-Purge`
    > What would there be for the Coven to return to, if life on our world was purged?
- **choice** `?` → `Z-Sultan`
    > Why had Resheph become sultan?
- **choice** `?` → `Z-Healer`
    > Resheph is remembered as a healer.
- **choice** `?` → `Z-Agreement`
    > How did the agreement play out?
- **choice** `?` → `Z-Failed`
    > Then you did not succeed, by Resheph's measure?

### Node `Z-Purge`

I asked Resheph that very question. But the seraphim transit an ethical manifold much different than our own.

### Node `Z-Sultan`

Once the Seraph had become convinced of the Coven's return, they reified their authority and assumed a more material role in onworld matters. The decaying sultanate was a convenient tool.

### Node `Z-Healer`

And he was, of a sort. The cure for a plague is often too its cause. With one's paws on the dials and drum of power, history is a cloth to be loomspun.

### Node `Z-Agreement`

We allied on the notion that the sultanate must be abolished for the future to flower. I was to execute the earthly plan, while Resheph continued preparations at the astronomical tier. To achieve a sort of bicameralism of action, Resheph insisted on reformatting their personality as a triumvirate, seeded from thin scans of the original archon, Rebekah, and myself.

        The art of mythmaking was employed to enshrine the Resheph persona. Thus- the healer, the Coiled Lamb, and perhaps unexpectedly, the Above.

**Choices:**
- **choice** `?` → `Z-Rebekah`
    > What happened to Rebekah?

### Node `Z-Rebekah`

*Barathrum inhales and stutters.* She-

        Resheph would not forgive her trespass. She contracted the rotting tongue while abetting the lepers of =RebekahRegion=. When her time came, she-

**Choices:**
- **choice** `?` → `Z-Rebekah2`
    > ...

### Node `Z-Rebekah`

Resheph would not let her return home. O..

        *Barathrum expels a hushed whimper.*

**Choices:**
- **choice** `?` → `Z-Hushed`
    > ...

### Node `Z-Failed`

*Barathrum whimpers.*

        -what? Who's there?

**Choices:**
- **choice** `?` → `Z-Name`
    > It is me, Barathrum. =name=.
- **choice** `?` → `Z-Failed2`
    > If the signal sounds and the Gyre widens again, then you did not reach whatever watermark Resheph set?

### Node `Z-Name`

Oh. Good, =name=, good...

### Node `Z-Failed2`

No... Qud is fractious, and no lasting peace has obtained. I tried... for decades on decades I tried our paws on the tiller, to shim together what blossomed in the wild...

        The restoration of machines, the federation of free sovranties, the nourishing rituals of salt and star, the sacred, the profane...

**Choices:**
- **choice** `?` → `Z-Failed3`
    > ...

### Node `Z-Failed3`

In the late years I saw the writing on the wall. I turned us inward, retreated to my candle-dim study to angle at the project alone. A new plan... *eeehw* was-

        *Barathrum starts panting.*

**Choices:**
- **choice** `?` → `Z-Failed4`
    > ...

### Node `Z-Failed4`

*Barathrum heaves a great sigh upon the moist air of the control pit.*
        *Barathrum stumbles to the floor with paws to his face.*

**Choices:**
- **choice** `?` → `Z-Failed5`
    > ...

### Node `Z-Failed5`

I failed it! I have failed! A thousand years too short, and- MORE TIME

        *Barathrum weeps.*

**Choices:**
- **choice** `?` → `Z-Failed6`
    > ...

### Node `Z-Failed6`

I am debased on the plank across the light of God! d- do I have a rightful claim to pity? Blindness! This darkling room abjures the light. Is this the House of Judgement, Hortensa? Or mere penumbra, the child's playcave, and law and language (not yet invented) cast their forcing functions back through time to puppet the unblossomed mind to civilized shape...

**Choices:**
- **choice** `?` → `Z-Failed7`
    > ...

### Node `Z-Failed7`

Each of us is a sick animal in a darkling thicket. Each cursed with machinery to compress the clamber of echoes into bees, mothers, mountains, country. How many millions of snowsick years to sew a feeling substance into an agent of the world! A felt and machine animal, and in so doing, to stuff the whole of the world inside the agent (an inarguable document of its falsity), for agency is in its very definition the world in containment acting on itself...

**Choices:**
- **choice** `?` → `Z-Failed8`
    > ...

### Node `Z-Failed8`

Then? Perhaps.. Perhaps the greater bodies whose agency I share the smaller cut from might share too the greater portion of my meal in blame.

        Winding Svy? Thou art devious in symbol shape like serpent Ba'al!
        Hinnom? For blooming alga thou crossed thy perch's back!
        Shiftless moon?
        Sun! Proud and idle, Sun! Silver father of the protoplanets! Claim mine selfhood and be done with it.

        *Barathrum weeps.*

**Choices:**
- **choice** `?` → `Z-Failed9`
    > ...

### Node `Z-Failed9`

*Barathrum weeps.*

**Choices:**
- **choice** `?` → `Z-DotDotDot`
    > ...

### Node `Z-DotDotDot`

*Barathrum weeps.*

**Choices:**
- **choice** `?` → `Z-WhyAscend`
    > Why ascend the Spindle then? For what purpose?
- **choice** `?` → `End`
    > ...

### Node `Z-WhyAscend`

*Barathrum's countenance suddenly burns bright.*

        Did you know, =name=, I harbor a memory older than even the flooding of my hearth cave. A gleaming ancient tale, told by my elders to the nippy cub I once was...

**Choices:**
- **choice** `?` → `Z-WhyAscend2`
    > ...

### Node `Z-WhyAscend2`

In the age of the covenate, a coterie of our urshiib ancestors took to the stars to ply their burning cores! Can you envision it??

        Ho, ho! I know a secret! Heh, heh! I know... there is a functioning starship atop the Spindle. We can take it, =name=! We launch ourselves into the deepness of the dusted cosmos and find the starshiib! You and I, ho ho!

        Starshiib!

**Choices:**
- **choice** `?` → `Z-Starshiib1`
    > Barathrum, we're to rest the fate of Qud on a mere cub's tale?
- **choice** `?` → `Z-Starshiib1`
    > Starshiib?

### Node `Z-Starshiib1`

Starshiib! Starshiib! Starshiib!

**Choices:**
- **choice** `?` → `Z-Starshiib2`
    > ...
- **choice** `?` → `Z-Starshiib2`
    > Barathrum.
- **choice** `?` → `Z-Starshiib2`
    > Starshiib!

### Node `Z-Starshiib2`

Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib! Starshiib!

**Choices:**
- **choice** `?` → `End`
    > ...
