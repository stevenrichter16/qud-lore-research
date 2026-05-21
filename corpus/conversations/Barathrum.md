# Conversation: `Barathrum`

_Inherits: (default: BaseConversation)_

_3 start(s), 44 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Early`

Should you be here, =player.offspringTerm=?

**Choices:**
- **choice** `?` → `End`
    > My apologies, Barathrum.

### Start `Recame`

Is that you, nestling =name=? Are you returned from gate and Tomb? Come closer, I say.

**Choices:**
- **choice** `?` → `RecameMe`
    > It is, Barathrum. I've returned.

### Start `Welcome`

Come closer, nestling. Let me look upon your countenance.

**Choices:**
- **choice** `?` → `Old`
    > You are so... old.
- **choice** `?` → `Quest`
    > Otho said you wished to speak with me.
- **choice** `?` → `Euclid`
    > What's with the houseplant over there?
- **choice** `?` → `Signal`
    > Please tell me about the signal again.
- **choice** `?` → `Signal`
    > Please tell me about the signal again.
- **choice** `?` → `PaxComplete`
    > I convinced Pax Klanq to construct the climber.
- **choice** `?` → `TombIntro`
    > Pax Klanq has agreed to build the climber. What now?
- **choice** `?` → `TombExplain1`
    > Could you tell me again about the Tomb of the Eaters?
- **choice** `?` → `Golem`
    > The magnetic field has been disable and the Spindle is free to ascend. What now?
- **choice** `?` → `Golem4`
    > Tell me again of the plan to mold a giant creature to ascend the Spindle.
- **choice** `?` → `GolemQuestDone`
    > The creature has been made. What now?
- **choice** `?` → `GolemInfo`
    > Tell me again how the giant creature functions.
- **choice** `?` → `Ascend`
    > I am ready to ascend the Spindle, Barathrum.
- **choice** `?` → `End`
    > Live and drink, eldest Barathrum.

## Nodes

### Node `RecameMe`

You appear... refreshed. My old eyes spy the swim lines of the waking world and to you they cede precedence. A newness obtains.

**Choices:**
- **choice** `?` → `Brightsheol1`
    > Outside of time I found myself in a place of light. I chose to return and was made new.
- **choice** `?` → `Brightsheol2`
    > I found Brightsheol, where it lies beyond the Tomb. I spoke to the Shomer there and arranged for the disablement of the Spindle's magnets.
- **choice** `?` → `PreKlanq`
    > Over there, by your workbench. Is that... Pax Klanq?
- **choice** `?` → `PreJunk`
    > There is junk about.

### Node `PreKlanq`

*Barathrum pauses.*

				It is. For reasons I will explain shortly, for reasons beyond any of our remits, Klanq has returned to Grit Gate.

**Choices:**
- **choice** `?` → `Brightsheol1`
- **choice** `?` → `RecameMe`
    > I've something else to say.

### Node `PreJunk`

*Barathrum pauses.*

				Unusual circumstances have put my study in disarray. Lamentable, this is, but necessary.

**Choices:**
- **choice** `?` → `Brightsheol1`
- **choice** `?` → `RecameMe`
    > I've something else to say.

### Node `Brightsheol1`

*Barathrum pauses.*
				
				I am confident there is a richness of wisdom in the poetry of that statement. One day, I will be eager to discover it. For now, what of the Spindle?

### Node `Brightsheol2`

*Barathrum breathes a deep and relieved sigh.*
				
				You are ever a courier of bright tidings, =name=. I am fond of this fact.
				
			  Categories and types are decohering in these historic times. Nonetheless, the ritual nourishes us. You are raised to Meyvn, =name=. The one who understands.

**Choices:**
- **choice** `?` → `TombReward`
    > *continue listening*
    - _part: `GritGateHandler` (Rank=Meyvn)_

### Node `TombReward`

Take this, too. A chute of morphing gel from my personal collection. You've arrayed yourself in the artifacts of time, and so we have little left to give you. But still, this may be useful.

**Choices:**
- **choice** `?` → `GolemPreface`
    > *continue listening*

### Node `GolemPreface`

Now, matters have... evolved... in your absence. Do you choose now to learn more?

**Choices:**
- **choice** `?` → `Golem`
    > I do.
- **choice** `?` → `End`
    > First, I need rest.

### Node `Golem`

High on the mount above Omonporch, the Putus Templar watch us through their war lenses and prepare an attack. The nephilim, too, stir from their cradles on the Moon Stair and slump with infernal purpose. The short of this is, due to a dearth of prep time and inadequate armament, Pax Klanq no longer believes in the viability of Q Girl's climber design. We must take Klanq at their word, here...

**Choices:**
- **choice** `?` → `Golem2`
    > *continue listening*

### Node `Golem2`

This disheartens us, but there is another hope. Klanq has offered up a new design, something unconventional at all angles. And, despite our early misgivings, Q Girl and I now work in assistance to the project...

**Choices:**
- **choice** `?` → `Golem3`
    > *continue listening*

### Node `Golem3`

A new creature struggles to be born, =name=, and you will help birth it. Then, it will carry us, you and I, to the top of the Spindle.

**Choices:**
- **choice** `?` → `Golem4`
    > ...

### Node `Golem4`

Pax Klanq will mold the creature from raw bioelectrical materials. You must gather these entrails: the body as a model, the catalyst to charge the sanguine fluid, the atzmus as deistic direction, the armament for protection, and the hamsa for personality. You will bond with the creature, too, and act as its pilot. So you must speak an incantation to inscribe the connection.
				
				You'll also need to procure the sanguine fluid itself. And, too, a power source shielded from electromagnetic attacks.

**Choices:**
- **choice** `?` → `Entrails`
    > These entrails, what are they? Where do I find them?
- **choice** `?` → `EntrailsAlternate`
    > These entrails, what are they? Where do I find them?
- **choice** `?` → `Pilot`
    > I'm to pilot the creature? And bond with it?
- **choice** `?` → `Fluid`
    > Sanguine fluid?
- **choice** `?` → `Power`
    > A power source?
- **choice** `?` → `AcceptGolem`
    > Let us begin, then.
- **choice** `?` → `End`
    > I need time and space from this.
- **choice** `?` → `Start`
    > I wish to ask about something else.

### Node `Entrails`

They are the components that we will grow, shape, and solder into the ascendant being. We can delve into specifics once you begin, at which point Pax Klanq can also serve as a source of knowledge.

				As you acquire components, bring them to the mound of scrap and clay over by Klanq.

### Node `EntrailsAlternate`

They are the components that we will grow, shape, and solder into the ascendant being. Ask Pax Klanq for details.

				As you acquire components, bring them to the mound of scrap and clay over by Klanq.

### Node `Pilot`

Correct. The creature will be shaped broad enough to contain two, but only you will be bonded to it. Only you will pilot.
				
				Don't fear over an inescapable tether, though. The creature will be mobile unpiloted, if slower to act.

### Node `Fluid`

Primordial soup, to be catalyzed and ran through its arteries as the animating substance.

### Node `Power`

Yes, the question of power is a trickier one. Our standard power sources might suffice, but they would be vulnerable to electromagnetic attacks on the ascent, and we believe it within the competency of the Putus Templar to execute such an attack.
				
				This leaves us two options. Klanq and Q Girl have worked out a design for a neutronic battery, free from vulnerabilities on the EM spectrum. But it requires 3 drams of neutron flux. The alternative is remote power, but to carry us across the Spindle's length the source would have to be extraordinary. I would look to Chavvah, the Tree of Life, for a psychic quickening. Reports tell of the resumption of their roaming across the Moon Stair. Seek the trunk at Eyn Roj to begin your investigation, if that's the path you choose.

### Node `AcceptGolem`

Yes, =name=! Begin the gathering, and the molding will follow. The materials you choose will influence the being we create, but any such being will be suitable for ascent.
				
				This is our last task before we make our historic climb, =name=. Be safe and well in doing it. If you have more questions, return here. Klanq and I will be available.

**Choices:**
- **choice** `?` → `End`
    > OK.

### Node `GolemQuestDone`

The creature is born, and you are bonded? What work! You are a sterling shaper of world, =name=, and I've nothing left to give you but my praise.

**Choices:**
- **choice** `?` → `GolemAcquaint`
    > ...

### Node `GolemAcquaint`

Now, our operators at Omonporch confirm that a clash with the Templar is inevitable.
				
				This is a grim fact, but it does give space for your bond to flower. Go, become familiar with leading and piloting your creature. Return when you are ready, and we will finally go starward.

**Choices:**
- **choice** `?` → `End`
    > I will, Barathrum. Live and drink.

### Node `Ascend`

Are you sure, Meyvn =name=? Our fates are not reversible past the next event horizon.

**Choices:**
- **choice** `?` → `Start`
    > Let me consider.
- **choice** `?` → `AscendConfirm`
    > We go.

### Node `AscendConfirm`

We go. I-

**Choices:**
- **choice** `?` → `AscendConfirm2`
    > ...

### Node `AscendConfirm2`

O! What is it? I heave... I heave the weight of ass across my crutch, but the bones are pullproof. My bones inosculate to this grotto, or rather- this grotto, this world is what my bones *are*. Can an old bear divest of his spine, leave it to mosses and the sunstrung birds?

**Choices:**
- **choice** `?` → `AscendConfirm3`
    > ...

### Node `AscendConfirm3`

I... 
				
				No matter. The will can break the wheel, too. We go. Pray, the weightloss of the rise might do good for me. Past the shell of the world, I'm to understand one's burdens can no longer pull them down...

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `GolemInfo`

Klanq is able to answer your questions. You received an operating manual, too, no? Perhaps you could reference it.

### Node `Questions`

What can I offer, nestling?

### Node `TombComplete`

You look... refreshed. Thank you, =name=. Take this polygel we recently recovered from the Palladium Reef.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Barathrum.

### Node `PaxComplete`

What welcome news, =factionaddress:Barathrumites=! Please, take this as a token of my gratitude.

**Choices:**
- **choice** `?` → `TombIntro`
    > Thank you.

### Node `TombIntro`

The flywheel of our scheme is spinning, but we must keep our paws on the treadle. Are you ready to learn what comes next?

**Choices:**
- **choice** `?` → `TombBody1`
    > Yes.
- **choice** `?` → `End`
    > I need time on my own first.

### Node `TombBody1`

The climber design relies on the use of electromagnets to interface with the planet's magnetic field and generate torque. Unfortunately, the Spindle generates its own interfering field, perhaps as a mechanism to prevent unwanted ascension.

				Our aim is to access the Spindle's control unit and disable the field. How we accomplish this, however, is an enigma. From disparate bits across the archives of the digitum, Ereshkigal has stitched together a cryptic but instructional brocade. She's learned the field can be turned off from a place called Brightsheol, located in the Thin World and accessible only through Resheph's tomb inside the Tomb of the Eaters.

**Choices:**
- **choice** `?` → `TombBody2`
    > ...

### Node `TombBody2`

Strange, this, and imprecise, but as tinkers we know: a crude blueprint is better than no blueprint. You must return to Omonporch and enter the Tomb of the Eaters. Once inside, trace the errant paths cut into the mausoleum by robbers and vandals, and ascend to Resheph's burial chamber.

				As for gaining entrance to the Tomb, Resheph sealed the gates a thousand years ago, but there's a flaw in the seal. The ancient Mark of Death has been lost to time, but if you were to recover it and incise the mark on your body, the Death Gate would open for you, as it did for countless Eater cadavers in the long-blurred past.

				Recover the Mark of Death, =name=, enter the Tomb, and cross into Brightsheol. Place your paws once again on the dial and drum.

**Choices:**
- **choice** `?` → `TombBody3`
    > I will enter the Tomb of the Eaters as you ask.
- **choice** `?` → `End`
    > You ask so much. I must consider it.

### Node `TombBody3`

As I'd hoped you would, =name=. Take this disk with the signal encoded, just in case. And take this tattoo gun for when you recover the Mark of Death. You'll want to bring a pickaxe, too, or some other instrument for digging through stone. And beware: the Tomb is a vast and ancient space, and sacred to many. I cannot speak to what you will experience there.

**Choices:**
- **choice** `?` → `End`
    > I heed your warning. Farewell, Barathrum.
    - _part: `ReceiveItem` (Blueprints=Decrypted Signal Data Disk,Tattoo Gun Barathrum Identify=Tattoo Gun Barathrum)_

### Node `TombExplain1`

The climber design relies on the use of electromagnets to interface with the planet's magnetic field and generate torque. Unfortunately, the Spindle generates its own interfering field, perhaps as a mechanism to prevent unwanted ascension.

				Our aim is to access the Spindle's control unit and disable the field. How we accomplish this, however, is an enigma. From disparate bits across the archives of the digitum, Ereshkigal has stitched together a cryptic but instructional brocade. She's learned the field can be turned off from a place called Brightsheol, located in the Thin World and accessible only through Resheph's tomb inside the Tomb of the Eaters.

**Choices:**
- **choice** `?` → `TombExplain2`
    > ...

### Node `TombExplain2`

Strange, this, and imprecise, but as tinkers we know: a crude blueprint is better than no blueprint. You must return to Omonporch and enter the Tomb of the Eaters. Once inside, trace the errant paths cut into the mausoleum by robbers and vandals, and ascend to Resheph's burial chamber.

				As for gaining entrance to the Tomb, Resheph sealed the gates a thousand years ago, but there's a flaw in the seal. The ancient Mark of Death has been lost to time, but if you were to recover it and incise the mark on your body, the Death Gate would open for you, as it did for countless Eater cadavers in the long-blurred past.

				You're to recover the Mark of Death, =name=, enter the Tomb, and cross into Brightsheol.

**Choices:**
- **choice** `?` → `TombExplain3`
    > ...

### Node `TombExplain3`

Use the tattoo gun I've given you when you recover the Mark of Death. You'll want to bring a pickaxe, too, or some other instrument for digging through stone. And beware: the Tomb is a vast and ancient space, and sacred to many. I cannot speak to what you will experience there.

**Choices:**
- **choice** `QuestionsChoice` → `Questions`
    > I have more to ask, Barathrum.

### Node `Old`

So I am, nestling. For a millennium now I've watched the river of Time turn the gears of Qud. I even played my part in diverting the river where I could. Oh, but there have been so many players through the years! So many players.

**Choices:**
- **choice** `?` → `Before`
    > And before Qud? Beyond the 1,000 years?
- **choice** `?`

### Node `Before`

Little do I remember now, for I was but a cub, a nestling, when my kin and I crossed the Homs Delta into Qud. We were urged on by the flooding of a glacial river that flowed through our hearth-cave. The world was just unthawing then, and I recall the roar of the freezing water as it rushed through the grotto, and the frigid spray on my face as I watched in awe.

**Choices:**
- **choice** `?`

### Node `Euclid`

That's my dear friend, Euclid. It's a prattleplant. It stores every phrase it hears in its neuroot network, and it mimics speech by flicking its leaves against one another. What comes out is gibberish as often as not, but even so, it's agreeable company for my nights spent tinkering. It is old, perhaps older than I am, and it hasn't yet run out of things to say.

**Choices:**
- **choice** `?`

### Node `Quest`

I do. Your service to the guild has been laudable, =factionaddress:Barathrumites=. You braved the vaporous depths of Bethesda Susa and decoded the signal, you secured the Spindlegrounds and handled the self-appointed Earl, and perhaps most materially, you defended our enclave from the Putus Templar.

				Since you returned from Bethesda, you've no doubt wondered at the signal's contents. Verily, I hid them to shield you from the weight of the truth. Only Otho, Q Girl, and I bear that burden, but circumstances have changed. The river of Time powers the gear train of our schemes and devices, and it rushes forth. From here, I must share the burden. You must know.

**Choices:**
- **choice** `?` → `Signal`
    > What is it? Where does the signal come from, and what does it say?

### Node `Signal`

The signal is a beacon of welcoming, and it originates from the top of the Spindle.

**Choices:**
- **choice** `?` → `Spindle`
    > And what is the Spindle, truly?

### Node `Spindle`

The beacon confirmed my hypothesis. The Spindle is an elevator, engineered by the Eaters to convey freight to and from the vault of heaven. You see, nestling, in the earliest aurora of our past, the Eaters of Earth were joined by a great coven of beings that spanned the firmament. But the Eaters succumbed to some terrible temptation, and an injunction was placed on our world.

				Since then, the stars were silent to us, and our world was left to molder and decay. But something changed. The signal affirms that an entity roosts atop the Spindle, and invites us to join it.

				Dare I say, is the injunction at an end? It's too early to tell, but alas, there could be hope for our world.

**Choices:**
- **choice** `?` → `WhatNow`
    > And what now?
- **choice** `?` → `Questions`
    > I have more to ask, Barathrum.

### Node `WhatNow`

I intend to ascend the Spindle and answer the call, =factionaddress:Barathrumites=.

				My protege Q Girl has designed a climber for the ascent. We intended to construct it piecewise at the enclave and the site itself, but the engineering feat exceeds even our capacity. With time, I am confident we could accomplish it, but the Putus Templar rob us of our patience. We need to act now, and so as loath as I am to admit it, we need Pax Klanq.

**Choices:**
- **choice** `?` → `PaxKlanq`
    > Who is Pax Klanq?

### Node `PaxKlanq`

Pax Klanq is an eccentric mushroom prodigy. All their faults aside, they are a brilliant scientist and engineer, and I have little doubt that they could build the climber faster than we could. Several years have passed since we were last in contact, but they owe us a debt, and we must now collect.

				Unfortunately, no one knows Pax Klanq's whereabouts. Through contacts I made over the years, I inquired as to their location. The most I was able to garner were these enigmatic instructions:

				"Seek the heart of the rainbow, eat the god's flesh, and follow the Coral Path."

**Choices:**
- **choice** `?` → `PaxKlanq2`
    > *continue listening*

### Node `PaxKlanq2`

I must ask you to decipher this enigma, find Pax Klanq, and convince them to construct the climber. Remind Pax of the debt they owe us.

				It strikes me as likely for this 'rainbow' to refer to the Rainbow Wood, where Klanq's kin consort, so I suggest you start there.

**Choices:**
- **choice** `?` → `Accept`
    > I will find Pax Klanq and deliver Q Girl's design.
- **choice** `?` → `End`
    > I must weigh everything you've told me.

### Node `Accept`

As I had hoped, =factionaddress:Barathrumites=. First, speak with Q Girl. She'll hand over her design.

				I await your return.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Barathrum.
