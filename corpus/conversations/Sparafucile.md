# Conversation: `Sparafucile`

_Inherits: (default: BaseConversation)_

_0 start(s), 23 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

*Sparafucile lifts one brow, giving you a wary look.*

**Choices:**
- **choice** `?` → `End`
    > I'll be going.

### Node `Start`

*Sparafucile gives =pronouns.possessive= carbine a once-over and gives you a resolute nod.*

**Choices:**
- **choice** `?` → `End`
    > *nod back*

### Node `Start`

*Sparafucile gives you a resolute nod.*

**Choices:**
- **choice** `?` → `End`
    > *nod back*

### Node `Start`

*Sparafucile nods.*

**Choices:**
- **choice** `GreetSpara` → `SilentGreeting`
    > Greetings, Sparafucile.
- **choice** `?` → `End`
    > *nod back*

### Node `SilentGreeting`

*Sparafucile raises one long-fingered hand in greeting.*

**Choices:**
- **choice** `BethesdaSpara` → `SparaSusa`
    > Do you know anything about Bethesda Susa?
- **choice** `RumbleSpara` → `GrimNod`
    > Did you feel that rumbling, Sparafucile?
- **choice** `KlanqSpara` → `ShroomPal`
    > Have you ever met Pax Klanq?
- **choice** `TombSpara` → `Sparagon`
    > I must enter Brightsheol through the Tomb of the Eaters.
- **choice** `GolemSpara` → `SparaStumped`
    > What do you think of Klanq's presence?
- **choice** `CarbineSpara` → `PraiseCarbine`
    > Your carbine is as fine an instrument as I have ever wielded.
- **choice** `PistolSpara` → `PraiseCarbine`
    > Your pistol is as fine an instrument as I have ever wielded.
- **choice** `FewWordsSpara` → `QuietBear`
    > You are a bear of few words.
- **choice** `GritGateSpara` → `SparaFam`
    > Are you happy living in this cave, away from the sun and open sky?
- **choice** `FarewellSpara` → `LiveDrinkSign`
    > Live and drink, harm-artisan.

### Node `Sparagon`

*Sparafucile frowns. After several moments of paper-shuffling, he presents you with a charcoal drawing depicting a gelatinous creature in the shape of a gumdrop. Sketches below depict the ooze enveloping a bipedal figure, then falling through the floor.*

**Choices:**
- **choice** `?` → `SparaNod`
    > An ooze that can melt through the floor...
- **choice** `?`

### Node `SparaStumped`

*Sparafucile furrows his brow for a few moments, then shakes his head, sighs, and offers you a shrug. He puts a paw on your shoulder and squeezes.*

**Choices:**
- **choice** `?` → `SparaNod`
    > Fair enough, friend.
- **choice** `?`

### Node `SparaSusa`

*Sparafucile instructs you to wait, and spends a minute or so rifling through the papers and scraps scattered across =pronouns.possessive= workbench. At last =pronouns.subjective= produces a graphite sketch of a cylinder, an expertly-rendered specular revealing its surface to be shiny like glass. The detail of the cylinder's contents are indistinct and dark, but somehow menacing.*

        *Sparafucile points to the glass and makes a breaking motion, then draws a thumb across =pronouns.possessive= throat.*

**Choices:**
- **choice** `?` → `SparaNod`
    > I'll have to be careful of... glass tubes?
- **choice** `?`

### Node `SparaFam`

*Sparafucile gives you a warm smile and a firm nod. Pressing both pointers to their respective thumbs, =pronouns.subjective= taps these finger-circles together before =pronouns.possessive= chest and rotates both hands in place until the smallest of =pronouns.possessive= long fingers touch. Finally, =pronouns.subjective= gestures toward the other Barathrumites working at their stations.*

**Choices:**
- **choice** `idkSpara` → `SparaSigh`
    > I don't understand. Can you explain aloud?
- **choice** `FamilySpara` → `SparaNod`
    > You are happy because you are with your family?
- **choice** `SubjectChange` → `Sparatopics`
    > If I might change the subject...
- **choice** `?`

### Node `PraiseCarbine`

*Sparafucile smiles. =pronouns.Subjective= raises a flat hand to =pronouns.possessive= chin and lowers it in your direction.*

**Choices:**
- **choice** `WelcomeSpara` → `Sparatopics`
    > You are welcome.
- **choice** `?`
- **choice** `?`

### Node `Sparatopics`

*With a nod, Sparafucile waits for you to continue, keeping =pronouns.possessive= eyes focused on your lips.*

**Choices:**
- **choice** `MoufSpara` → `QuietBear`
    > Why are you staring at my mouth?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `QuietBear`

*Sparafucile places a closed fist over =pronouns.possessive= mouth, then taps =pronouns.possessive= ear, then muzzle with one long finger.*

**Choices:**
- **choice** `?`
- **choice** `oicSpara` → `Disabearlity`
    > You are... unable to hear or speak.
- **choice** `?`
- **choice** `?`

### Node `Disabearlity`

*Smiling a bit, Sparafucile nods.*

**Choices:**
- **choice** `AccidentSpara` → `Miscongenitality`
    > Is your condition a result of your work?
- **choice** `PatronizeSpara` → `SparaStare`
    > Yet you are an expert in your field? How inspiring!
- **choice** `?`
- **choice** `?`

### Node `Miscongenitality`

*Sparafucile shakes =pronouns.possessive= head.*

**Choices:**
- **choice** `ConfirmSpara` → `SparaNod`
    > Your condition is lifelong?
- **choice** `ThankSpara` → `SparaThank`
    > Thank you for your clarity and patience, tinkerfriend.
- **choice** `?`
- **choice** `?`

### Node `SparaNod`

*Sparafucile nods.*

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `GrimNod`

*Sparafucile nods grimly.*

**Choices:**
- **choice** `?`
- **choice** `?`

### Node `SparaThank`

*With a small smile of gratitude, Sparafucile taps his chin with a flat hand and lowers it toward you like a drawbridge.*

**Choices:**
- **choice** `?`
- **choice** `?`

### Node `SparaSigh`

*Sparafucile averts =pronouns.possessive= gaze and heaves a tired sigh.*

**Choices:**
- **choice** `CluelessSpara` → `SparaStare`
    > I merely asked...
- **choice** `ApologizeSpara` → `BearySorry`
    > I apologize for my carelessness.
- **choice** `?`
- **choice** `?`

### Node `BearySorry`

*Sparafucile gives you a wan smile and a thumbs-up.*

**Choices:**
- **choice** `?`
- **choice** `?`

### Node `ShroomPal`

*=pronouns.Subjective= nods slowly, smirking.*

**Choices:**
- **choice** `?` → `ShroomPal2`
    > Is... there any advice you can give me about going to meet him?
- **choice** `?` → `Sparatopics`
    > So anyway...

### Node `ShroomPal2`

*Sparafucile shrugs, still smirking.*

**Choices:**
- **choice** `?` → `Sparatopics`
    > Let us speak of other things.
- **choice** `?`

### Node `SparaStare`

*Sparafucile stares at you as if you have grown an additional, substantially uglier head, which you have not.*

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > I'll... be going then.

### Node `LiveDrinkSign`

*Sparafucile makes an 'L' shape with both hands, thumbs facing down and fingers pointed toward one another, before flipping both hands so =pronouns.possessive= thumbs face up. =pronouns.Subjective= then raises a closed fist to =pronouns.possessive= mouth, thumb out, and mimes drinking from it.*

        *This done, =pronouns.subjective= nods once more and turns back to =pronouns.possessive= work.*

**Choices:**
- **choice** `?` → `End`
    > ...
