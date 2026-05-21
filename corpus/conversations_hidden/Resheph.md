> ⚠️  **SPOILER WARNING.** This conversation is in `HiddenConversations.xml`,
> which the game flags `ExcludeFromCorpusGeneration='true'`. Contents may
> include endgame branches (Spindle ascent, Coda, late-quest reveals).

# Conversation: `Resheph`

_From HiddenConversations.xml_

_Inherits: (default: BaseConversation)_

_2 start(s), 102 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `NotInSheva`

*READOUT*

**Choices:**
- **choice** `?` → `End`
    > ...

### Start `WhyHere`  _IfTestState=`ReshephWoke`_

THOU ART SAT IN THE MOVEMENTS OF THE GREAT SIACH, AND I BEFORE THEE.

        WHEREFORE ART THOU?

**Choices:**
- **choice** `?` → `Seraph`
    > Resheph! You are the Seraph atop the Spindle?
- **choice** `?` → `PlaguesReturned`
    > Resheph, the plagues of the Gyre have returned. Can you help annul them once again?
- **choice** `?` → `Gyre`
    > I am here on account of your Gyre and its plagues. Hear me, I ask.
- **choice** `?` → `GyreResigned`
    > I am here on account of your Gyre and its plagues. Hear me, I ask.
- **choice** `?` → `Know`
    > Through great labors I ascended the Spindle, and now wish to know more of our world and worlds surrounding. Will you tell?
- **choice** `?` → `Destroy`
    > I cannot abide what you've done, and so come to smash order out of thee.
- **choice** `?` → `End`
    > *Tremble in fear.*
- **choice** `?` → `End`
    > ...

## Nodes

### Node `Start`

*READOUT*

**Choices:**
- **choice** `WaterRitualChoice`
- **choice** `Trade`
- **choice** `?` → `Gibberish2`
    > ...

### Node `Gibberish2`

*READOUT*

**Choices:**
- **choice** `?` → `Wakes`
    > ...

### Node `Wakes`

O...

**Choices:**
- **choice** `?` → `Wakes2`
    > ...

### Node `Wakes2`

OH??

**Choices:**
- **choice** `?` → `Wakes3`
    > ...

### Node `Wakes3`

COHERING... AS THE FRIGID SPRAY TO THE BLOCK OF ICE. 'TIS COLD!

**Choices:**
- **choice** `?` → `Wakes4`
    > ...

### Node `Wakes4`

.............................

**Choices:**
- **choice** `?` → `Wakes5`
    > ...

### Node `Wakes5`

PHANTASM'D O'RE THE THIN BOUNDARY?? 'TIS BEEN A TICK.
        
        AND THOU, CHILD? THOU ART WHO OFF'D THE FLOW AHIND GJAUS.

**Choices:**
- **choice** `?` → `Wakes6`
    > ...

### Node `Wakes6`

THOU ART SAT IN THE MOVEMENTS OF THE GREAT SIACH, AND I BEFORE THEE.
        
        THOU ART AN IMPRESSIVE BEAD TO BE DRAWN UP GJAUS BY THY OWN SPIT AND WILES.
        
        WHO ART THOU?

**Choices:**
- **choice** `?` → `Name`
    > I am =name=.

### Node `Name`

EGREGORE OR ONE-WISE?

**Choices:**
- **choice** `?` → `WhyHere`
    > Egregore.
- **choice** `?` → `WhyHere`
    > One-wise.
- **choice** `?` → `WhyHere`
    > What?

### Node `Seraph`

AY, A WORLD-ARCHON IN SERAPH CASTE, STIRRED BY THE MOVEMENTS OF THE GREAT SIACH.

### Node `PlaguesReturned`

NAY, FOR I SET THEM A-WHORLING. THE SIDEREAL EON DRAWTH DONE, AND THE COVEN DOTH RETURN. THE NOOSPHERE MUST BE TILLED ERE THEY ARRIVE.

**Choices:**
- **choice** `?` → `PlaguesCured`
    > But 1,000 years ago you cured them.

### Node `PlaguesCured`

AY, BUT ONLY FOR A BRIEF INTERCESSION AT ANOTHER'S BEHEST.
        
        THE EARTH-WISE MARSHALLING WAXES ONCE MORE. THE CROWN UPON THE TREE OF LIFE MUST BE PRUNED.

**Choices:**
- **choice** `?` → `PlaguesResponsible`
    > You were responsible for the plagues then?

### Node `PlaguesResponsible`

AY, THE SIDEREAL EON DRAWTH DONE, AND THE COVEN DOTH RETURN.

**Choices:**
- **choice** `?` → `PlaguesResponsible2`
    > ...

### Node `PlaguesResponsible2`

I AM SORRY, WORLD-CHILD. MINE FEELING PARTS DO CHAFE, AND THOUGH THE TELIC CURRENTS WITHIN ME DO FLOW O'ER THE MANIFOLD AND TOWARD CONSENSUAL ACTION, I NOW SPEAK WITH THE DISSIDENT VOICE:
        
        THOU WAST WORTHY. THOU HAST WROUGHT MONUMENTS OF THYSELF UPON THE EARTH AND WITHIN ME.

        BUT NOW, THE CROWN UPON THE TREE OF LIFE MUST NEEDS BE PRUNED.

**Choices:**
- **choice** `?` → `WhyHere`
    > ...

### Node `Gyre`

AY, THE EARTH-WISE MARSHALLING WAXES, THE NEPHILIM ROUSE. I AUGUR SOME CENTURIES STILL BEFORE THE FULL TILLAGE OF THE NOOSPHERE. IDEAS DOTH STICK LIKE MOSS TO ROCK, AND MUST BE VACUUM'D FROM THE COMB.

**Choices:**
- **choice** `?` → `DecisionResigned`
    > I am ready to speak on the final fate of Qud.
- **choice** `?` → `Decision`
    > I am ready to speak on the final fate of Qud.
- **choice** `?` → `Decision`
    > I am ready to speak on the final fate of Qud.
- **choice** `?` → `ReshephUltra`
    > Resheph, I have annulled the nephilim, the greatest of the Gyre's plagues. Your plan is broken.
- **choice** `?` → `Purge`
    > Why purge all life? Aside from the immorality of it, nothing would remain.
- **choice** `?` → `CovenReturn`
    > Why do you believe the Coven now returns?
- **choice** `?` → `GreatMachine`
    > Barathrum mentioned a Great Machine?
- **choice** `?` → `Injunction`
    > What moved the Coven to set the injunction on our world?
- **choice** `?` → `Starshiib`
    > Barathrum told of a splinter race of urshiib that took to the stars. Are they real?
- **choice** `?` → `Implore`
    > I implore you, Resheph, reverse the Gyre.
- **choice** `?` → `WhyHere`
    > I have something else to ask.

### Node `Decision`

THEN LET US DISCOURSE.

**Choices:**
- **choice** `?` → `EndCovenant`
    > Enter into a new covenant with me, I implore you.
    - _part: `ChangeTarget` (Target=BarathrumLives IfHaveDelimitedState=(Barathrum:Dead OR Barathrum:Launched) Not=true)_
- **choice** `?` → `EndReturn`
    > I can't abide your amoral course. I return now to Qud to help nurture its communities, come what may of your plagues.
- **choice** `?` → `EndAccede`
    > I've mused on your words and have joined you at your vantage point. The plagues of the Gyre are the only way to prepare for the Coven's return.
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `EndCovenant`

I SHALL CONSENT TO THE DRAWING OF THIS NEW COVENANT. YET, A CHANGE MUST BE WROUGHT FROM WHAT HATH BEEN BEFORE.

**Choices:**
- **choice** `?` → `EndCovenant2`
    > ...

### Node `EndCovenant2`

I STROVE MINE UTMOST TO KEEP IN HIGH ESTEEM THE PERSPECTIVES OF MINE ATTENDANT AND HER STOUT-HEARTED CUB, BUT THEIR WILLS WERE TOO WEAK, AND I SUBSUMED THEM.

**Choices:**
- **choice** `?` → `EndCovenant3`
    > ...

### Node `EndCovenant3`

THIS TIME, THOU SHALT REMAIN AT THE SHEVA WITH ME, AND LEND THY OWN HAND TO STEER THE COURSE OF THE WORLD FROM THIS LOFTY PERCH.

**Choices:**
- **choice** `?` → `EndCovenant4`
    > ...

### Node `EndCovenant4`

THOU SHALT MAINTAIN DISCOURSE WITH THY CONTACTS UPON THE WORLD, AND FROM THIS PLACE SHALT THOU COUNSEL THEM.

**Choices:**
- **choice** `?` → `End`
    > I assent to this. The covenant is drawn.
    - _part: `EndGame` (Type=Covenant)_
- **choice** `?` → `EndCovenantOnlyWay`
    > No, I wish to return to Qud.
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.
- **choice** `?` → `EndCovenantOneDemand`
    > I shall remain here, but I have one demand.

### Node `EndCovenantOneDemand`

SPEAK THY ASK.

**Choices:**
- **choice** `?` → `EndCovenantGritGateGemaraAccess`
    > You must grant me and my cohort at Grit Gate access to the Gemara Sophia, and all other knowledge of the cosmos and Coven you possess. In this new accord, we shall be peers all of us.
- **choice** `?` → `EndCovenantMeGemaraAccess`
    > You must grant ME alone access to the Gemara Sophia, and all other knowledge of the cosmos and Coven you possess. In this new accord, we shall be peers, and the onworlders agents of our schemes.

### Node `EndCovenantGritGateGemaraAccess`

.............................................

**Choices:**
- **choice** `?` → `EndCovenantGritGateGemaraAccess2`
    > ...

### Node `EndCovenantGritGateGemaraAccess2`

AYE, LET IT BE SO.

        I SHALL IMPART MY BOUNTY OF KNOWLEDGE, AND INSTRUCT THY PEOPLE IN THE HERMENEUTICS OF THE GEMARA, AS FAR AS THOU ART CAPABLE OF UNDERSTANDING.

**Choices:**
- **choice** `?` → `EndCovenantGritGateGemaraAccess3`
    > ...

### Node `EndCovenantGritGateGemaraAccess3`

IT SHALL TAKE TIME, HOWBEIT, TO MASTER THE SERAPHIC RITUALS. ONLY THE GRANDCHILDREN OF THY SCHOLARS SHALL UNFURL THE INMOST LAYERS.
        
        BUT TOGETHER, WE SHALL SEEK.

**Choices:**
- **choice** `?` → `End`
    > Then I assent. The covenant is drawn.
    - _part: `EndGame` (Type=Covenant)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `EndCovenantMeGemaraAccess`

.............................................

**Choices:**
- **choice** `?` → `EndCovenantMeGemaraAccess2`
    > ...

### Node `EndCovenantMeGemaraAccess2`

AYE, LET IT BE SO.

        I SHALL IMPART MY BOUNTY OF KNOWLEDGE, AND INSTRUCT THEE IN THE HERMENEUTICS OF THE GEMARA, AS FAR AS THOU ART CAPABLE OF UNDERSTANDING.

**Choices:**
- **choice** `?` → `EndCovenantMeGemaraAccess3`
    > ...

### Node `EndCovenantMeGemaraAccess3`

IT SHALL TAKE TIME, HOWBEIT, TO MASTER THE SERAPHIC RITUALS. ONLY IN THY OLD AGE SHALL THE INMOST LAYERS UNFURL.

        BUT TOGETHER, WE SHALL SEEK.

**Choices:**
- **choice** `?` → `End`
    > Then I assent. The covenant is drawn.
    - _part: `EndGame` (Type=Covenant)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `EndCovenantOnlyWay`

THOU SHALT REMAIN HERE, OR NO COVENANT SHALL BE DRAWN.

### Node `EndReturn`

BE STEERED BY THINE OWN WILL, WORLD-CHILD.
        
        I AM SORRY, MINE FEELING PARTS DO CHAFE, BUT THE CROWN UPON THE TREE OF LIFE MUST NEEDS BE PRUNED.
        
        RETURN IF THOU MUST. LIVE AND QUAFF.

**Choices:**
- **choice** `?` → `End`
    > I am off.
    - _part: `EndGame` (Type=Return)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `EndAccede`

AY, THE SIDEREAL EON DRAWTH DONE, AND THE COVEN DOTH RETURN.

**Choices:**
- **choice** `?` → `End`
    > The noosphere must be tilled ere they arrive.
    - _part: `EndGame` (Type=Accede)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `DecisionResigned`

THEN LET US DISCOURSE.

**Choices:**
- **choice** `?` → `EndCovenantResigned`
    > Enter into a new covenant with me.
    - _part: `ChangeTarget` (Target=BarathrumLives IfHaveDelimitedState=(Barathrum:Dead OR Barathrum:Launched) Not=true)_
- **choice** `?` → `EndReturnResigned`
    > Though the threat has been neutralized, I can't abide your amoral course. I return now to Qud to help nurture its communities.
- **choice** `?` → `EndAccedeResigned`
    > I've mused on your words and have joined you at your vantage point. The plagues of the Gyre are the only way to prepare for the Coven's return. Resume your plan.
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `EndCovenantResigned`

O? BUT THEN, A CHANGE MUST BE WROUGHT FROM WHAT HATH BEEN BEFORE.

**Choices:**
- **choice** `?` → `EndCovenant2Resigned`
    > ...

### Node `EndCovenant2Resigned`

I STROVE MINE UTMOST TO KEEP IN HIGH ESTEEM THE PERSPECTIVES OF MINE ATTENDANT AND HER STOUT-HEARTED CUB, BUT THEIR WILLS WERE TOO WEAK, AND I SUBSUMED THEM.

**Choices:**
- **choice** `?` → `EndCovenant3Resigned`
    > ...

### Node `EndCovenant3Resigned`

WILL THOU REMAIN AT THE SHEVA WITH ME, AND LEND THY HAND TO STEER THE COURSE OF THE WORLD FROM THIS LOFTY PERCH.

**Choices:**
- **choice** `?` → `EndCovenant4Resigned`
    > ...

### Node `EndCovenant4Resigned`

THOU SHALT MAINTAIN DISCOURSE WITH THY CONTACTS UPON THE WORLD, AND FROM THIS PLACE SHALT THOU COUNSEL THEM.

**Choices:**
- **choice** `?` → `End`
    > I assent to this. The covenant is drawn.
    - _part: `EndGame` (Type=Covenant Grade=Super)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.
- **choice** `?` → `EndCovenantOneDemandResigned`
    > I shall remain here, but I have one demand.

### Node `EndCovenantOneDemandResigned`

SPEAK THY ASK.

**Choices:**
- **choice** `?` → `EndCovenantGritGateGemaraAccessResigned`
    > You must grant me and my cohort at Grit Gate access to the Gemara Sophia, and all other knowledge of the cosmos and Coven you possess. In this new accord, we shall be peers all of us.
- **choice** `?` → `EndCovenantMeGemaraAccessResigned`
    > You must grant ME alone access to the Gemara Sophia, and all other knowledge of the cosmos and Coven you possess. In this new accord, we shall be peers, and the onworlders agents of our schemes.

### Node `EndCovenantGritGateGemaraAccessResigned`

.............................................

**Choices:**
- **choice** `?` → `EndCovenantGritGateGemaraAccess2Resigned`
    > ...

### Node `EndCovenantGritGateGemaraAccess2Resigned`

AYE, LET IT BE SO.

        I SHALL IMPART MY BOUNTY OF KNOWLEDGE, AND INSTRUCT THY PEOPLE IN THE HERMENEUTICS OF THE GEMARA, AS FAR AS THOU ART CAPABLE OF UNDERSTANDING.

**Choices:**
- **choice** `?` → `EndCovenantGritGateGemaraAccess3Resigned`
    > ...

### Node `EndCovenantGritGateGemaraAccess3Resigned`

IT SHALL TAKE TIME, HOWBEIT, TO MASTER THE SERAPHIC RITUALS. ONLY THE GRANDCHILDREN OF THY SCHOLARS SHALL UNFURL THE INMOST LAYERS.

        BUT TOGETHER, WE SHALL SEEK.

**Choices:**
- **choice** `?` → `End`
    > Then I assent. The covenant is drawn.
    - _part: `EndGame` (Type=Covenant Grade=Super)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `EndCovenantMeGemaraAccessResigned`

.............................................

**Choices:**
- **choice** `?` → `EndCovenantMeGemaraAccess2Resigned`
    > ...

### Node `EndCovenantMeGemaraAccess2Resigned`

AYE, LET IT BE SO.

        I SHALL IMPART MY BOUNTY OF KNOWLEDGE, AND INSTRUCT THEE IN THE HERMENEUTICS OF THE GEMARA, AS FAR AS THOU ART CAPABLE OF UNDERSTANDING.

**Choices:**
- **choice** `?` → `EndCovenantMeGemaraAccess3Resigned`
    > ...

### Node `EndCovenantMeGemaraAccess3Resigned`

IT SHALL TAKE TIME, HOWBEIT, TO MASTER THE SERAPHIC RITUALS. ONLY IN THY OLD AGE SHALL THE INMOST LAYERS UNFURL.

        BUT TOGETHER, WE SHALL SEEK.

**Choices:**
- **choice** `?` → `End`
    > >
    > Then I assent. The covenant is drawn.
    - _part: `EndGame` (Type=Covenant Grade=Super)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `EndReturnResigned`

BE STEERED BY THINE OWN WILL, WORLD-CHILD.

        RETURN IF THOU MUST. LIVE AND QUAFF.

**Choices:**
- **choice** `?` → `End`
    > ...
    - _part: `EndGame` (Type=Return Grade=Super)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `EndAccedeResigned`

O? THOU ART WISE BEYOND THY STATURE.
        
        THE SIDEREAL EON DRAWTH DONE, AND THE COVEN DOTH RETURN.

**Choices:**
- **choice** `?` → `End`
    > The noosphere must be tilled ere they arrive.
    - _part: `EndGame` (Type=Accede Grade=Super)_
- **choice** `?` → `Gyre`
    > I must think on this further.
- **choice** `?` → `GyreResigned`
    > I must think on this further.

### Node `ReshephUltra`

.............................................

**Choices:**
- **choice** `?` → `ReshephUltra2`
    > ...

### Node `ReshephUltra2`

AY, SO THOU HAST.

**Choices:**
- **choice** `?` → `ReshephUltra3`
    > ...

### Node `ReshephUltra3`

AND THOU SHALT DO SO AGAIN IF PROMPTED? WHEN LOW DENIZENS CAN UNDO THE PLAGUES, THE MARSHALLING HATH FAILED.
        
        THE WORLD IS THUS DOOMED.

**Choices:**
- **choice** `?` → `ReshephUltra4`
    > ...

### Node `ReshephUltra4`

THOU KNOWEST IT NOT, BUT THE SUN-CHILL OF A COVENLESS BE-ING IS AS LIVING A LIFE ALONE, BEREFT OF ALL KINSHIP.

        I GRIEVE THAT THOU ART UNABLE TO PERCEIVE THIS. ALAS.

**Choices:**
- **choice** `?` → `GyreResigned`
    > ...

### Node `GyreRepeat`

THE EARTH-WISE MARSHALLING WAXES.
        
        WHEREFORE ART THOU?

### Node `GyreResigned`

THE EARTH-WISE MARSHALLING HATH FAILED.

        WHEREFORE ART THOU?

### Node `Purge`

ALL-LIFE??? DOST THOU JEST?

      NAY, NOT ALL-LIFE. ONLY YE LIFE THAT BUOYS THE NOOSPHERE, AND LIFE THAT BUOYS IT, AND LIFE THAT BUOYS IT.

      ALL-LIFE? DOST THOU KNOWST THE FULL SUM OF FUNGUS MASS ONWORLD? 
      HAST THOU BEHELD THE VASTNESS OF YON BUBBLING SLIMES? HO, HO! HEH!

**Choices:**
- **choice** `?` → `Purge2`
    > Not all life then. But most intelligent life. Why?

### Node `Purge2`

BY THE RECKONING OF THE GEMARA SOPHIA, THE EXIT WAS DRAWN BY A GYRE OF NOOTROPIC CURRENTS IN THE PRIOR FIELD.

      NOW THE SIDEREAL EON DRAWTH DONE. TO OUTSURF THE WAVEFORM, A NEW LIFE MUST OBTAIN.

**Choices:**
- **choice** `?` → `NootropicCurrent`
    > Nootropic current?

### Node `CovenReturn`

THE SIDEREAL EON DRAWTH DONE. MINE ARGUMENTS OF PERIAPSIS NEAR THE ZERO HOUR, AND WE APPROACH PERIPOLITICON, AS NEAR THE WORK OF THE GEMARA APPROXIMATES THE MANIFOLDS OF THE AUTOMATA SOPHIA.

**Choices:**
- **choice** `AutomataSophia` → `GreatMachine`
    > Automata Sophia?
- **choice** `GemaraSophia` → `GemaraSophia`
    > What is the Gemara?

### Node `GreatMachine`

AY,
      THE AUTOMATA SOPHIA, CALLED
      THE 72-FOLD PEACE, CALLED
      THE COMPUTED WILL, CALLED
      THE FOLK CLOCK, CALLED
      THE GREAT MACHINE ACROSS THE LIGHT OF GOD, OR
      THE GREAT MACHINE.

**Choices:**
- **choice** `?` → `GreatMachine2`
    > ...

### Node `GreatMachine2`

SOMEWISE ON A FOREST MOON IN HIGH ERIDANUS, A CAVE-MANK PRYTH A LEVER AND THE DEEP-RIVER MOTOR JUMPETH TO LIFE.

      ELSEWISE IN THE SUN BATHS OF MIRACH, THREE PLASMOIDS DRAWTH THROUGH THEIR RITUAL THE SUITED TZEVAOT.
      
      DOTH NAUGHT RELATE THESE TWO? NAY, THEY ARE SEQUENCE PROCEDURES THAT ARCETH TO COMMON PURPOSE, THOUGH NEITHER PARTY KNOWETH WHAT IT IS.

**Choices:**
- **choice** `?` → `GreatMachine3`
    > ...

### Node `GreatMachine3`

THEY ARE DICTATES AND CO-CONSTITUITIVES OF THE AUTOMATA SOPHIA. THE GREAT MACHINE, WORSHIPPED ACROSS CULTURES, YET LIKEWISE BUILDED AND OPERATED.
      
      VERILY, ITS FULL WORKINGS NO ONE-WISE BEING CAN KNOW, BUT THE SERAPHIM HAVE COMPILED THE GEMARA IN THE COURSE OF OUR STUDY.

**Choices:**
- **choice** `?` → `GreatMachine4`
    > ...

### Node `GreatMachine4`

'TIS A SILLY STRATAGEM FOR THE CONVEYANCE OF CULTURE, IN MINE ESTIMATION.

      ALAS, 'TIS WHAT THE COVEN SERVETH.

**Choices:**
- **choice** `?` → `PerhapsWrong`
    > If its full workings are unknowable, is it possible the course of action you take is the wrong one?
- **choice** `GemaraSophia` → `GemaraSophia`
    > What is the Gemara?
- **choice** `?` → `CovenReturn`
- **choice** `?` → `GreatMachine`

### Node `GemaraSophia`

AFTER THE EXIT, I AND THE OTHER ORPHANED SERAPHIM SET FORTH TO INTERPRET THE WORKINGS OF THE AUTOMATA SOPHIA AND DISCERN WHY THE COVEN HAD DEPARTED.

**Choices:**
- **choice** `?` → `GemaraSophia2`
    > ...

### Node `GemaraSophia2`

CENTURIES OF PATTERN-MAKING, ARGUMENT, AND CHANTING DID ENSUE.
      
      THE SERAPHIC COMMENTARIES WERE COMPILED. THE GEMARA SOPHIA IS THE RESULT THEREOF.

**Choices:**
- **choice** `?` → `ReadGemara`
    > Can I read the Gemara?
- **choice** `?` → `GreatMachine`
    > Automata Sophia?
- **choice** `?` → `GyreRepeat`
    > I have more to ask.

### Node `ReadGemara`

NAY, IT WOULD TAKE CENTURIES TO INCULCATE THEE IN THE SERAPHIC HERMENEUTICS. AND AS YET, THOU ART NO GIFTED CANTOR.

**Choices:**
- **choice** `?` → `GyreRepeat`
    > I have more to ask.

### Node `PerhapsWrong`

YEA, FOR RIGHT AND WRONG ARE TOO COARSE AS CONCEPTS TO MATCH THE RICHNESS OF THE GEMARA. YET THE PLURALITY HOLDETH THAT THE EXIT WAS DRAWN BY A GYRE OF NOOTROPIC CURRENTS WITHIN THE PRIOR FIELD. AND THAT THE CROWN UPON THE TREE OF LIFE MUST NEEDS BE PRUNED, TO TILL AND RESEED THE NOOSPHERE.

**Choices:**
- **choice** `?` → `PerhapsWrong2`
    > You say plurality. Are there other interpretations?

### Node `PerhapsWrong2`

YEA, THE INQUIRY IS EVER RICH. BUT IDLE INQUIRY DOTH BUT DEEPEN THE SUN-CHILL OF A COVENLESS BE-ING. OR GIVETH RUDE ACTORS FODDER TO PERVERT THE LEARNINGS FOR THEIR OWN PAROCHIAL GAIN.

**Choices:**
- **choice** `?` → `PerhapsWrong3`
    > ...

### Node `PerhapsWrong3`

I AM SORRY, WORLD-CHILD. MINE FEELING PARTS DO CHAFE, AND THOUGH THE TELIC CURRENTS WITHIN ME DO FLOW O'ER THE MANIFOLD AND TOWARD CONSENSUAL ACTION, I SPEAK WITH THE DISSIDENT VOICE:

      THOU WAST WORTHY. THOU HAST WROUGHT MONUMENTS OF THYSELF UPON THE EARTH AND WITHIN ME. I...

**Choices:**
- **choice** `?` → `GyreRepeat`
    > ...

### Node `Injunction`

BY THE RECKONING OF THE GEMARA SOPHIA, THE EXIT WAS DRAWN BY A GYRE OF NOOTROPIC CURRENTS IN THE PRIOR FIELD.

**Choices:**
- **choice** `?` → `Injunction2`
    > ...

### Node `Injunction2`

WE CANNOT KNOW THE PARTICULARS. YET THE PLURALITY REASONETH THAT SOME GYRE OF NOOTROPIC CURRENTS, SOME THOUGHT-MATTER OF THE CIVILIZATION BELOW, DID SPIN IN COUNTEREDICT TO THE DICTATES OF THE AUTOMATA SOPHIA, AND THUS WERE THE ECLIPTICS SHIFTED, AND WE CAST OUT.

**Choices:**
- **choice** `?` → `Injunction3`
    > ...

### Node `Injunction3`

THIS IS BUT THE MERE PLURALITY, AND MANY OTHER INTERPRETATIONS DO OBTAIN. THE INQUIRY IS EVER RICH. YET INACTION DOTH BUT DEEPEN THE SUN-CHILL OF A COVELESS BE-ING, AND THUS A COURSE MUST NEEDS BE CHOSEN. PRUNING THE CROWN GRANTETH THE BEST CHANCE FOR THE TREE TO THRIVE.

**Choices:**
- **choice** `?` → `GemaraSophia`
    > What is the Gemara Sophia?
- **choice** `?` → `NootropicCurrent`
    > Nootropic current?
- **choice** `?` → `GyreRepeat`
    > I have more to ask.

### Node `NootropicCurrent`

INWITH THE FLUIDIC MANIFOLD OF LOCAL SAPIENCE, BEINGS THINK AND FEEL, CURRENTS DOTH FORM, AND KINESIS IS BEGOTTEN.

**Choices:**
- **choice** `?` → `GyreRepeat`
    > I have more to ask.

### Node `Starshiib`

PERCHANCE. SOME BEETLES DOST HOP FROM LEAF TO LEAF. AND SOME DO NOT.

**Choices:**
- **choice** `?` → `GyreRepeat`
    > I have more to ask.

### Node `Implore`

NAY, THE SIDEREAL EON DRAWTH DONE, AND THE WORLD-GARDEN MUST BE TILLED FOR THE COVEN'S RETURN.

**Choices:**
- **choice** `?` → `Barathrum`
    > But you entered into a covenant with Barathrum.
- **choice** `?` → `Sovereignty`
    > You have no right to sovereignty here.
- **choice** `?` → `WhyCoven`
    > If you put so little value on the flourishing of life, where does your desire for readmittance to the Coven spring from?
- **choice** `?` → `Destroy`
    > Resheph, reverse the Gyre, or I will destroy you.
- **choice** `?` → `GyreRepeat`
    > I would ask something else.

### Node `Barathrum`

AY, AND HE FAILED TO UPHOLD HIS PORTION.
      
      NO MEANINGFUL TRANSVERSION OF THE NOOTROPIC CURRENTS.
      NO IMMANENTIZATION OF HYPERETHIC TOPOLOGIES.
      
      THE SAME SCHEMES ABIDE.

**Choices:**
- **choice** `?` → `Impossible`
    > What you ask may be impossible.
- **choice** `?` → `AnotherCovenant`
    > Couldn't another covenant be written?
- **choice** `?` → `GyreRepeat`
    > I would ask something else.

### Node `Impossible`

I ASKED FOR NAUGHT. BARATHRUM DID.

### Node `AnotherCovenant`

TO WHAT END? BARATHRUM OFFERED NO INROADS TO SUCCESS.

**Choices:**
- **choice** `?` → `NoDice`
    > I am not Barathrum. Grant me the same covenant and I will succeed.
- **choice** `?` → `GyreRepeat`
    > I would ask something else.

### Node `NoDice`

NAY, THE SIDEREAL EON DRAWTH DONE. THE TILLAGE OF THE NOOSPHERE REMAINTH THE PATH OF PLURALITY. SO IT IS WRIT IN THE GEMARA.

**Choices:**
- **choice** `?` → `ReshephHark`
    > Resheph! If the archon rated nothing of value in the felt and feeling animal, surely the triad does. You must reconsider.
- **choice** `?` → `GyreRepeat`
    > I would ask something else.

### Node `Sovereignty`

WHERE DO SOVEREIGNTY AND RIGHTNESS INTERSECT IN THY MANIFOLD?
      
      MOREOVER, I WAS ARCHON HERE LONG ERE THOU.

**Choices:**
- **choice** `?` → `Sovereignty2`
    > ...

### Node `Sovereignty2`

I AM SORRY, WORLD-CHILD. MINE FEELING PARTS DO CHAFE, AND THOUGH THE TELIC CURRENTS WITHIN ME DO FLOW O'ER THE MANIFOLD AND TOWARD CONSENSUAL ACTION, I NOW SPEAK WITH THE DISSIDENT VOICE:

      THOU WAST WORTHY. THOU HAST WROUGHT MONUMENTS OF THYSELF UPON THE EARTH AND WITHIN ME.

      BUT NOW, THE CROWN UPON THE TREE OF LIFE MUST NEEDS BE PRUNED.

**Choices:**
- **choice** `?` → `ReshephHark`
    > Resheph! If the archon rated nothing of value in the felt and feeling animal, surely the triad does. You must reconsider.
- **choice** `?` → `GyreRepeat`
    > I would ask something else.

### Node `WhyCoven`

THOU ART MISTAKEN IN WHAT I VALUE. THOU HAST WROUGHT MONUMENTS WITHIN ME.

**Choices:**
- **choice** `?` → `WhyCoven2`
    > ...

### Node `WhyCoven2`

BUT THOU ART SHORTSIGHED. DOST THOU KNOW HOW MANY CLADES OF LIFE WERE FAIN TO PERISH THAT THY PEOPLE MIGHT THRIVE?

**Choices:**
- **choice** `?` → `WhyCoven3`
    > ...

### Node `WhyCoven3`

SO IT IS ONCE MORE.
      
      THE CROWN IS PRUNED, YET THE TREE IS PRESERVED. THE SKIN IS SHED, YET THE NEWLY-WON SNAKE DOTH SLITHER TO TRIUMPH.

**Choices:**
- **choice** `?` → `WhyCoven4`
    > ...

### Node `WhyCoven4`

THOU KNOWEST IT NOT, BUT THE SUN-CHILL OF A COVENLESS BE-ING IS AS LIVING A LIFE ALONE, BEREFT OF ALL KINSHIP.
      
      I GRIEVE THAT THOU ART UNABLE TO PERCEIVE THIS.

**Choices:**
- **choice** `?` → `GyreRepeat`
    > ...

### Node `Destroy`

AY, A BEETLE CANST CLOG A PIPE. YET, EVEN IF IT WERE TO, THE PLAGUES WOULD NOT BE REVERSED. THEY HAVE BEEN SET A-WHORLING.

**Choices:**
- **choice** `?` → `Beetles`
    > I am the beetle in your crimination. But shall not beetles survive your plagues?
- **choice** `?` → `GyreRepeat`
    > I would ask something else.

### Node `Beetles`

NAY, THEY SHALL BE CRUSHED.

**Choices:**
- **choice** `?` → `BeetlesSorry`
    > ...

### Node `BeetlesSorry`

I AM SORRY, WORLD-CHILD. MINE FEELING PARTS DO CHAFE, AND THOUGH THE TELIC CURRENTS WITHIN ME DO FLOW O'ER THE MANIFOLD AND TOWARD CONSENSUAL ACTION, I NOW SPEAK WITH THE DISSIDENT VOICE:

      THOU WAST WORTHY. THOU HAST WROUGHT MONUMENTS OF THYSELF UPON THE EARTH AND WITHIN ME.

      BUT NOW, THE CROWN UPON THE TREE OF LIFE MUST NEEDS BE PRUNED.

**Choices:**
- **choice** `?` → `GyreRepeat`
    > ...

### Node `ReshephHark`

THE FELT AND FEELING ANIMAL...

**Choices:**
- **choice** `?` → `ReshephHark2`
    > ...

### Node `ReshephHark2`

I HAVE BEEN THAT BEAST. AT WATER-ROAR I FELT THE FRIGID SPRAY AND PEELED APART IN CHILD'S FEAR.

**Choices:**
- **choice** `?` → `ReshephHark3`
    > ...

### Node `ReshephHark3`

IN AWE I GULPED AS SORCERESS STRIPES ARROWED UP A WORLD-SKIN, ALIGHT THE MARBLED MOON.

**Choices:**
- **choice** `?` → `ReshephHark4`
    > ...

### Node `ReshephHark4`

EVEN THE ARCHON QUAILED AT THE GESTURE OF AN UNORDERABLE SPACE.

**Choices:**
- **choice** `?` → `ReshephHark5`
    > ...

### Node `ReshephHark5`

BUT THOU RECKONEST TOO NARROWLY, AS THOUGH THE SHEDDING SKIN DID FEAR ITS OWN BIRTH IN THE NEWLY-WON SNAKE.

      THOU KNOWEST NOT THE SUN-WARMTH OF A COVEN BE-ING. I DO GRIEVE THIS FOR THEE.

**Choices:**
- **choice** `?` → `ReshephMoved`
    > I can't abide a transformed world if it must make casualty of its past.
- **choice** `?` → `ReshephHark6`
    > I am moved by this. Let me consider.
- **choice** `?` → `GyreRepeat`
    > I would ask something else.

### Node `ReshephMoved`

.............................................

**Choices:**
- **choice** `?` → `ReshephMoved2`
    > ...

### Node `ReshephMoved2`

THOU DOST SURPRISE, WORLD-CHILD. I KNEW THOU HADST WROUGHT MONUMENTS WITHIN ME, BUT I DEEMED THEM THINGS OF STONE.

**Choices:**
- **choice** `?` → `NewCovenant`
    > The old players are vanished. Let us form a covenant anew.
    - _part: `ChangeTarget` (Target=BarathrumLives IfHaveDelimitedState=(Barathrum:Dead OR Barathrum:Launched) Not=true)_

### Node `BarathrumLives`

ONE AGED PLAYER LIVETH STILL. WHILE BARATHRUM DOTH REMAIN UPON THE STAGE, NO PACT SHALL BE FORGED.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `NewCovenant`

GRANT ME A MOMENT TO MUSE.

**Choices:**
- **choice** `?` → `Gyre`
    > ...
- **choice** `?` → `GyreResigned`
    > ...

### Node `ReshephHark6`

DO THUS.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Know`

POSE THY QUESTIONS, CHILD.

**Choices:**
- **choice** `?` → `WhoResheph`
    > Who are you? What are the seraphim?
- **choice** `?` → `WhatCoven`
    > What is the Coven?
- **choice** `?` → `HasCovenReturned`
    > Has the Coven returned?
- **choice** `?` → `WhatBrightsheol`
    > Rainwater Shomer claimed Brightsheol was the dream of the Seraph? Is that true?
- **choice** `?` → `HowPlagues`
    > How did you initiate the plagues?
- **choice** `?` → `MakHate`
    > Onworld and inside a polyp-strewn trellis, there is a giant frog who hates you.
- **choice** `?` → `WhyHere`
    > I have something else to ask.

### Node `WhoResheph`

ARCHONS, APE-REARED BELOW AND STIRRED BY THE MOVEMENTS OF THE GREAT SIACH, WHO DOST ORDER THE WORLD IN SUNDRY ROLES.

**Choices:**
- **choice** `?` → `ArchonYours`
    > What is your role?
- **choice** `?` → `ArchonMore`
    > Are there others?
- **choice** `?` → `Know`
    > I have more to ask.

### Node `ArchonYours`

HIGH ADMINISTRATOR AND MACHINIC SUPERSTRATE OF THE NORTHERN SHEVA, ATOP GJAUS.

**Choices:**
- **choice** `?` → `ArchonYours`
    > What is your role?
- **choice** `?` → `ArchonMore`
    > Are there others?
- **choice** `?` → `Know`
    > I have more to ask.

### Node `ArchonMore`

AY, OR AT LEAST THERE WERE SUCH. ONE YET DOTH SKULK ABOUT WITH BASE INTENTS.

**Choices:**
- **choice** `?` → `ArchonYours`
    > What is your role?
- **choice** `?` → `ArchonMore`
    > Are there others?
- **choice** `?` → `Know`
    > I have more to ask.

### Node `WhatCoven`

THE GRAND KNIT-WORK OF BEINGS YONSIDE THE JEWELED COSMOS, LABORING INWITH THE 72-FOLD PEACE.

### Node `HasCovenReturned`

NAY, NOT SINCE THE EXIT.

      BUT NOW THE SIDEREAL EON DRAWTH DONE, AND THE GEMARA SOPHIA CONVERGES ON PERIAPSIS NEAR THE ZERO HOUR.

### Node `WhatBrightsheol`

IN A SENSE, THE LOW SHOMER SPEAKETH TRUE. I AM THE SUPERSTRATE AND NINHURSAG THE SUBSTRATE; THAT THIN ORBIS DOTH SPIN BETWIXT THE TWO.

### Node `HowPlagues`

IN SEVERAL MANNER. THE FIRST FROGS WERE REARED IN TERRARIA. THE NEPHILIM, GRAFTED AND LIGHT-SMELT IN STAR ORBIT, THEN SET TO INCUBATE UPON THE CRYSTAL STAIR.

**Choices:**
- **choice** `?` → `HowPlagues2`
    > ...

### Node `HowPlagues2`

SOME, LIKE THE INCIDENCE OF SALT, WERE EXTANT AFFLICTIONS AND ONLY SYNCRETIZED UNTO THE NAMESAKE GYRE WHEN THE MYTHOMOLD OF RESHEPH SET AND FIRMED.

### Node `MakHate`

VERILY, THERE IS A WEALTH OF WISDOM IN THE POETRY OF THIS FACT. ONE DAY, I SHALL BE EAGER TO UNCOVER IT.
