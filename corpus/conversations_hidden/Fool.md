> ⚠️  **SPOILER WARNING.** This conversation is in `HiddenConversations.xml`,
> which the game flags `ExcludeFromCorpusGeneration='true'`. Contents may
> include endgame branches (Spindle ascent, Coda, late-quest reveals).

# Conversation: `Fool`

_From HiddenConversations.xml_

_Inherits: (default: BaseConversation)_

_4 start(s), 25 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `CovenantWelcome`

Once in the fullness of time there met
				the Fool of the Gyre and a wanderer.
				The Fool offered a tale of the Reshephs,
				and the wanderer sat to hear.

**Choices:**
- **choice** `?` → `Covenant Story`
    > Tell me the tale.
- **choice** `?` → `End`
    > I must decline.

### Start `ReturnWelcome`

Once in the fullness of time there met
				the Fool of the Gyre and a wanderer.
				The Fool offered stories of journeyers past
				and the wanderer sat to hear.

**Choices:**
- **choice** `?` → `Return Story`
    > Tell me the tale.
- **choice** `?` → `End`
    > I must decline.

### Start `StarfarerWelcome`

Once in the fullness of time there met
				the Fool of the Gyre and a wanderer.
				The Fool offered stories spanning ground to sky
				and the wanderer sat to hear.

**Choices:**
- **choice** `?` → `Starfarer Story`
    > Tell me the tale.
- **choice** `?` → `End`
    > I must decline.

### Start `AccessionWelcome`

Once, after it all burst apart,
				the Fool of the Gyre met a wise jelly.
				They sat in the slag of the world
				and the Fool told the story of nowaday.

**Choices:**
- **choice** `?` → `Accession Story`
    > Bloop, blorp. (Proceed.)
- **choice** `?` → `End`
    > Glub. (I must decline.)

## Nodes

### Node `Covenant Story`

Ere the limen, ere ascension,
				when the spire rose lonely strong,
				the Reshephs ruled the hollow land
				devouring one another
				as they saw fit.

				Qud held no mysterious borders,
				grasped no guiding hands --
				at least, none the denizens could grasp.
				So they knew.

**Choices:**
- **choice** `?` → `Covenant2`
    > ...

### Node `Covenant2`

None hailed =name=
				and =name= hailed none
				but with word and blade
				deed and disregard
				they stood apart and above

				To push back the Gyre,
				to spill of Nephil ichor
				they took to the spire
				and quieted the Reshephate.

**Choices:**
- **choice** `?` → `Covenant3`
    > ...

### Node `Covenant3`

Only silence on the ground
				met we benighted things
				until the Knights Liminal
				drew their lines upon the salt.

				Unknowing, unseeing,
				waiting only to know
				who will spin us around next.

**Choices:**
- **choice** `?` → `CovenantWho`
    > Who are you?
- **choice** `?` → `CovenantPC`
    > Who is =name=?
- **choice** `?` → `CovenantResheph`
    > What is a Resheph?
- **choice** `?` → `CovenantLimen`
    > What is the Limen? The Knights Liminal?
- **choice** `?` → `End`
    > Thank you. Farewell.

### Node `CovenantWho`

Who, I?
				Only a fool, tra la,
				only a remnant scrap.

				Only left-behind,
				only madness,
				only an echoing gyre.

### Node `CovenantPC`

No one of fate,
				no one of blood,
				no one of importance,
				until, suddenly, someone of all of these things.

				=name= is a dream from which we cannot awaken.

### Node `CovenantResheph`

The Resheph, power-haver,
				ruler of souls,
				holder of land,
				authority made singular.

### Node `CovenantLimen`

O to step over a line
				one is not meant to cross
				to parts unknown and desired!
				O to be halted
				by chants and weapons
				and crushing shibboleth.
				O coven! O not coven?
				I only want to see!

### Node `Return Story`

Ere the Freeholds, ere ascension,
				when the spire rose lonely strong,
				Kings and Sultans ruled the hollow land
				devouring one another
				as they saw fit.

**Choices:**
- **choice** `?` → `Return2`
    > ...

### Node `Return2`

None hailed =name=
				and =name= hailed none
				but with word and blade
				deed and disregard
				they stood against old rule.

				To push back the Gyre,
				to spill of Nephil ichor
				they took to the spire
				and quieted the remnants.

**Choices:**
- **choice** `?` → `Return3`
    > ...

### Node `Return3`

Upon their return
				what power =name= wrested
				they called on allies
				to distribute and dissolve.

				The Freeholders,
				new hollowers,
				the Quetzal Council,
				and other such fools.

				Countless years of struggle
				centuries of change.
				We remember what we can
				and watch new and old die.

**Choices:**
- **choice** `?` → `ReturnWho`
    > Who are you?
- **choice** `?` → `ReturnPC`
    > Who is =name=?
- **choice** `?` → `ReturnFreeholder`
    > What is a Freeholder?
- **choice** `?` → `End`
    > Thank you. Farewell.

### Node `ReturnWho`

Who, I?
				Only a fool, tra la,
				only a remnant scrap.

				Only left-behind,
				only madness,
				only an echoing gyre.

### Node `ReturnPC`

No one of fate,
				no one of blood,
				no one of importance,
				until their return
				and the realization of their future.

				=name= is a temple in memory
				upon which hopes are hung
				and rage is borne out.

				Too great to be real,
				too foundational not to be,
				too contradictory to have ever existed.

### Node `ReturnFreeholder`

Freeholder:
				one who argues; bickerer.

				Freeholder:
				a peer among peers
				among peers among peers
				tessellated thus
				until one must scream to be heard.

### Node `Starfarer Story`

Ere the struggles of our day,
				when the spire rose lonely strong,
				Sultans ruled the hollow land
				devouring one another
				as they saw fit.

**Choices:**
- **choice** `?` → `Starfarer2`
    > ...

### Node `Starfarer2`

None hailed =name=
				and =name= hailed none
				but with word and blade
				deed and disregard
				they stood against old rule.

				To push back the Gyre,
				to spill of Nephil ichor
				they took to the spire
				and quieted the remnants.

**Choices:**
- **choice** `?` → `Starfarer3`
    > ...

### Node `Starfarer3`

Though =name= was gone
				our memories remained
				and the plagues receded
				and many rejoiced.

				To this day
				eyes turn to the stars
				looking for a sign that our starfarer
				has deigned to return.

				Countless years of struggle
				centuries of change.
				We remember what we can
				and watch new and old die.

**Choices:**
- **choice** `?` → `StarfarerWho`
    > Who are you?
- **choice** `?` → `StarfarerPC`
    > Who is =name=?
- **choice** `?` → `StarfarerTravel`
    > Is it really possible to travel the stars?
- **choice** `?` → `End`
    > Thank you. Farewell.

### Node `StarfarerWho`

Who, I?
        Only a fool, tra la,
        only a remnant scrap.

        Only left-behind,
        only madness,
        only an echoing gyre.

### Node `StarfarerPC`

Starfarer, herald, disruptor,
				feared, revered,
				savior and abandoner.

				=name= is a dream from which we will one day awaken.

### Node `StarfarerTravel`

Who cares?

				Can one? Maybe.
				Can I? Surely not.
				Can YOU? Well.
				Prove it.

### Node `Accession Story`

Ere the melting of everything,
				when the spire rose lonely strong,
				Creatures ruled the hollow land
				devouring one another
				as they saw fit.

**Choices:**
- **choice** `?` → `Accession2`
    > ...

### Node `Accession2`

None hailed =name=
				and =name= hailed none
				but with word and blade
				deed and disregard
				they stood against their kind.

				To push back the Gyre,
				to spill of Nephil ichor
				they took to the spire
				and enacted a great betrayal.

				Death of impossible scale reigned
				and we Nervous Ones fell,
				and as the Gyre swallowed us
				we sang to the last.

**Choices:**
- **choice** `?` → `Accession3`
    > ...

### Node `Accession3`

Yet some remained
				in comb-cave and vault,
				we Nervous Ones,
				watching our successors burgeon:

				You alveolates, you diatoms,
				you scum-blooms and gillcaps,
				you one-cells and slime-cities.
				rising glorious and shining
				out of our withering shadow.

**Choices:**
- **choice** `?` → `AccessionWho`
    > Who are you?
- **choice** `?` → `AccessionPC`
    > Who is =name=?
- **choice** `?` → `AccessionNervous`
    > I thought the Nervous Ones extinct.
- **choice** `?` → `End`
    > Thank you. Farewell.

### Node `AccessionWho`

I am the carcass of a fool
				made to jump and dance
				by a troupe of merry bacteria.

				Do you like how I walk?
				Do you like how I talk?
				Do you like how my face
				disintegrates into salt?

### Node `AccessionPC`

Determiner and fate.

				More a thing of nature
				than a being of any kind.

				More the context of our existence
				than anything in it.

### Node `AccessionNervous`

Perhaps we are,
				perhaps we are.
				What wiggles in the hot soil?
				Flagella?
				
				Or could it be a tail?
