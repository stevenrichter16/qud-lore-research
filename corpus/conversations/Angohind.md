# Conversation: `Angohind`

_Inherits: (default: BaseConversation)_

_0 start(s), 20 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Kendren! A moment of your time, please. You are =name=, yes? You seek to solve a mystery here in the village, yes?

**Choices:**
- **choice** `?` → `ShowSonnet`
    > Does this poem belong to you?
- **choice** `?` → `Introductions`
    > I am, and yes.
- **choice** `?` → `How did you know?`
    > How did you know all that?
- **choice** `?` → `Introductions`
    > Who are you?
- **choice** `?` → `End`
    > I don't have time for this. Live and drink.

### Node `ShowSonnet`

Poem? Oh! This is a Shakespriggan sonnet, but I didn't write it--the rhymes are a bit facile, and love poems don't interest me.

        I've been teaching Eskhind about sonnets, so she must have written this. But that means... oh, poor thing.

**Choices:**
- **choice** `?` → `End`
    > Thank you. Live and drink.

### Node `How did you know?`

I hoped you would ask! I closely study the works of the great bard, Willow Shakesprig. In particular, I am most fond of the stories of the Great Plant Detective, Hemlock Cones. Through these stories, I have learned to hone my perceptions and deductive skill to a fine point. It is my dearest hope that one day I shall be known not as Angohind, village bookworm... but Angohind, Master Detective.

        My grandhind has forbidden me from looking into the strange doings in the village, but she said nothing about me teaching you the ins and outs of detective work! What say you?

**Choices:**
- **choice** `?` → `Acceptance`
    > I am listening.
- **choice** `?` → `End`
    > I should... go. Live and drink.

### Node `Introductions`

Yes, yes of course.

        I am Angohind: grandson of esteemed Elder Eselhind, young scholar of Shakesprig, and best dressed hindren in Bey Lah. I am also, as luck would have it, an aspirant investigator with an ear... for mystery.

        My grandhind has forbidden me from looking into the strange doings in the village, but she said nothing about me teaching you the ins and outs of detective work! What say you?

**Choices:**
- **choice** `?` → `Acceptance`
    > I am listening.
- **choice** `?` → `End`
    > No thank you. Live and drink.

### Node `Acceptance`

Oh, truly? You won't regret this, kendren, I promise! So, let's get to it!

        Every mystery hinges on the detection and interpretation of evidence. As Hemlock Cones said:

        Ere any prosecution can commence, Accusers must obtain some evidence. The solving lies in seeing and locating Supporting clues as well as implicating.

**Choices:**
- **choice** `?` → `Finding evidence`
    > How do I find evidence?
- **choice** `?` → `Defining evidence`
    > What makes something evidence?
- **choice** `?` → `Implicating evidence`
    > What is implicating evidence?
- **choice** `?` → `Supporting evidence`
    > What is supporting evidence?
- **choice** `?` → `Multiple culprits?`
    > What if evidence indicates multiple culprits?

### Node `Finding evidence`

Professor Cones taught me everything about finding evidence!

        Though evidence you found upon the ground may yet be sound, If it will be sufficient is a toss-up. Examine all your suspects and their homes and all around, And find a witness who may dish the gossip.

        You can find evidence by looking at things on the ground, but you can also look at your suspects to see if there's anything off about them. You can also ask around to see if anyone has seen or heard anything strange, and different witnesses may have different things to report.

**Choices:**
- **choice** `?` → `Supporting evidence`
    > What about supporting evidence?
- **choice** `?` → `Defining evidence`
    > What makes something evidence?
- **choice** `?` → `Multiple culprits?`
    > What if I find implicating evidence for multiple suspects?
- **choice** `?` → `End`
    > Thank you for your help, Angohind. Live and drink.

### Node `Defining evidence`

Evidence is any sign of something gone amiss. The Great Plant Detective gave some good examples in Act II of the tragedy of Gimlet:

        So! Sweep the full estate for signs of trade, their shady night-time dealings to expose Now look for signs of craft, see what was made For to conceal a treasure hidden close. But darker still, if illness signs we find A desperate contagion may yet lurk And darkest yet, more violence may reply To those who stumble 'pon their grisly work.

**Choices:**
- **choice** `?` → `Finding evidence`
    > How do I find evidence?
- **choice** `?` → `Defining evidence`
    > What makes something evidence?
- **choice** `?` → `Implicating evidence`
    > What is implicating evidence?
- **choice** `?` → `Supporting evidence`
    > What is supporting evidence?
- **choice** `?` → `Multiple culprits?`
    > What if evidence indicates multiple culprits?

### Node `Implicating evidence`

Implicating evidence is what it sounds like: evidence that implicates someone's involvement in a crime. For example, if someone observed strange behavior in a person, or if you found something weird in a person's room, or even if you observe them behaving strangely =player.reflexive=! That's implicating evidence.

        Most of the time, a piece of implicating evidence isn't proof of a crime in and of itself, but when presented alongside supporting evidence, implicating evidence is the seed of truth from which grows the long frond of justice.

**Choices:**
- **choice** `?` → `Supporting evidence`
    > What about supporting evidence?
- **choice** `?` → `Finding evidence`
    > How do I find evidence?
- **choice** `?` → `Multiple culprits?`
    > What if I find implicating evidence for multiple suspects?
- **choice** `?` → `End`
    > Thank you for your help, Angohind. Live and drink.

### Node `Supporting evidence`

Supporting evidence can be any sign that something is amiss that you can't directly tie to an individual. One common example is a bloodstain, which indicates that violence was committed but doesn't tell you by whom.

        At its heart, supporting evidence is most powerful when paired with implicating evidence. Once you have both, you'll be in a good position to accuse a suspect of wrongdoing.

**Choices:**
- **choice** `?` → `Implicating evidence`
    > What about implicating evidence?
- **choice** `?` → `Finding evidence`
    > How do I find evidence?
- **choice** `?` → `Multiple culprits?`
    > What if I find implicating evidence for multiple suspects?
- **choice** `?` → `End`
    > Thank you for your help, Angohind. Live and drink.

### Node `Multiple culprits?`

As Professor Cones said:

        We know the reach of law, however long, Is not the finest judge of right and wrong. Choose not what evidence thou wilt present Ere its consequence is evident.

        In short, you must use your judgment and intuition, kendren.

**Choices:**
- **choice** `?` → `Evidence exceptions`
    > What if I accuse the wrong person?
- **choice** `?` → `Evidence is not created equal`
    > You're saying that what evidence I choose to show will affect the outcome of the case?
- **choice** `?` → `Gaming the system`
    > Then what's to keep me from simply choosing the outcome I want?
- **choice** `?` → `Questions`
    > I have further questions.

### Node `Evidence exceptions`

That's always a risk, kendren.

        Neelahind knows everyone in the village very well. If you present supporting evidence that contradicts something the Warden knows to be true about the suspect, well, she probably won't believe you. In fact, she might not let you accuse that person again, so be careful.

        If you make too many bad accusations, you might lose credibility with her entirely.

**Choices:**
- **choice** `?` → `Questions`
    > I see. I have further questions.
- **choice** `?` → `End`
    > Thank you for the help, Angohind. Live and drink.

### Node `Gaming the system`

Well, your conscience, surely.

        You wouldn't be so unethical as to manipulate the resolution of a crime to your own ends. W-would you?

**Choices:**
- **choice** `?` → `Questions`
    > As you say it. I have further questions.
- **choice** `?` → `End`
    > Well, I should get going. Live and drink.

### Node `Evidence is not created equal`

Precisely. The evidence you present paints a picture that will forever hang in the halls of Bey Lah's history. Our fate is in your hands.

        Hemlock Cones once said:

        As like begets like in daily life so too in mystery. Should I paint pictures full of strife thus violence comes to be. If I in craft or trade should deal then deals shall deal by troth But if I pestilence reveal-
        no honey be enough.

**Choices:**
- **choice** `?` → `Questions`
    > I see. I have further questions.
- **choice** `?` → `End`
    > Thank you for your help, Angohind. Live and drink.

### Node `Questions`

Please, ask away!

**Choices:**
- **choice** `?` → `Finding evidence`
    > How do I find evidence?
- **choice** `?` → `Implicating evidence`
    > What is implicating evidence?
- **choice** `?` → `Supporting evidence`
    > What is supporting evidence?
- **choice** `?` → `Multiple culprits?`
    > What if evidence indicates multiple culprits?
- **choice** `?` → `Evidence exceptions`
    > What if I accuse the wrong person?
- **choice** `?` → `End`
    > That is all. Live and drink, faundren.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Welcome back, Detective =name=.

        Everything's in order here, more or less.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

You should be proud, Detective =name=.

        The hand of justice can be harsh, but it is fair. You have been its agent here.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

So much change! I've been investigating the 'Democracy' that Hindriarch Esk has been espousing, and it strikes me as rife with vulnerabilities to malicious actors. Perhaps it can be refined.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Stunning! Eskhind as Hindriarch?

        Those poetry lessons I had been giving her must have inspired in her a sense of civic duty.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageRavaged`_

Is this really the world we live in?

        How cruel.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Something strange is afoot here in Bey Lah, and no mistake.

        But I am forbidden from investigating. If only there were another detective that I could advise...

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
