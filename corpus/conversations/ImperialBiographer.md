# Conversation: `ImperialBiographer`

_Inherits: (default: BaseConversation)_

_0 start(s), 29 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`PlayerEngravingsDone_ReshephDisguise`_

The engraving is done, Moloch! I do hope it's to your liking. Your deeds are incised here for all time.

        You may now enter the sarcophagus, Moloch. Be at peace.

**Choices:**
- **choice** `?` → `End`
    > Farewell.

### Node `Start`  _IfHaveState=`PlayerEngravingsDone`_

Now, uh... hop... hop into the sarcophagus.

        Safe travels.

**Choices:**
- **choice** `?` → `End`
    > Farewell.

### Node `Start`

.....oh... oh? Peace to all who canter in the House of the Coiled Lamb.

**Choices:**
- **choice** `BiographerWho` → `Who`
    > Who are you?
- **choice** `BiographerMark` → `Mark`
    > Do you know the Mark of Death?
- **choice** `BiographerBrightsheol` → `Brightsheol`
    > How do I get to Brightsheol?
- **choice** `BiographerUnfinished` → `Unfinished`
    > Why is this tomb unfinished?
- **choice** `?` → `End`
    > Live and drink.

### Node `Who`

...oh..... I am Herododicus, lapidary, lithographer, sculptor, calciminer, and biographer to the Coiled Lamb. I will tarry here until the Godhead passes on, and then I will canonize his deeds in high relief.

        I've tarried for quite some time, now.... What a prodigious reign! Bless that Coiled Lamb!

**Choices:**
- **choice** `BiographerSultanGone` → `SultanGone`
    > The sultanate is dissolved. Resheph rules no longer.
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `SultanGone`

.....oh.... oh.... Poor friend. The ironshank must be upsetting your digestion. The darkness must be blooming in your brain, making you slow and doltish.

        The sultanate dissolved? Tidings would have reached me.... someone would have said so....

        Oh... poor, doltish friend. You cantered too long outside the House of the Coiled Lamb, and now you are a dolt.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Mark`

Herododicus pauses.

        I do. It's... it's... I am required to know the Mark of Death. Otherwise, I wouldn't know when the Coiled Lamb was dea... is no long... when... if he bore the Mark.

        .....oh... Is this... is this a test? Do *you* know the Mark?

**Choices:**
- **choice** `?` → `Mark2`
    > It is a test. Tell me the answer now.
- **choice** `?` → `Start`
    > I want to ask you something else.

### Node `Mark2`

Herododicus whirrs fearfully.

        The Mark is =MarkOfDeath=.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Brightsheol`

Oh! Brightsheol? The forever braid of life? The Garden Behind the High Gate? Why, you must rank among the crown echelon of machine and folk, and you must... well, you must...

        Start to decompose. You must... You must be dead. Dead and entombed. The body remains, but the mind wanders...

**Choices:**
- **choice** `?` → `OnlyWay`
    > You must be dead? Is that truly the only way?
- **choice** `?` → `BearTheMark`
    > I bear the Mark. Entomb me.
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `OnlyWay`

Herododicus pauses.

        Ye... yes? Is this a test? I suppose you... could we... could we have been in Brightsheol all along? Is that the answer?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `BearTheMark`

Herododicus worriedly looks you over.

        Should you be.... now I... I don't rank myself among the doyen on the matter of organic life... but my understanding is that the dead do not speak.

        Besides, you... aren't the Coiled Lamb... are you?

**Choices:**
- **choice** `?` → `EntombMeReshephDisguise`
    > Wrong on both counts. Resheph stands before you. Entomb me.
- **choice** `?` → `EntombMe`
    > Resheph is gone, biographer. I am here, and I have need to travel to Brightsheol. Entomb me.
- **choice** `?` → `Start`
    > Of course not. Let's back up.

### Node `EntombMe`

That's not even how it works!

        First, I image your head, read your self's narrative from the folds of your brain, cross-check it against the Thin World's ambient log of your life's deeds...

        Then I... stylize... the story, and I engrave it on the walls. Once I'm done... then you can entomb =player.reflexive=.

**Choices:**
- **choice** `?` → `DoThat`
    > Do that then.
- **choice** `?` → `Start`
    > Hold on. I have more to ask.

### Node `EntombMeReshephDisguise`

Herododicus looks you over.

        Coi... Coiled Lamb? Is it truly you? Are you dea.... are you dead?

        Herododicus drops to their knees.

        Oh, forgive me my insolence, Moloch!

**Choices:**
- **choice** `?` → `EntombMeResheph`
    > You are forgiven. Now entomb me.
- **choice** `?` → `Start`
    > I've misled you, biographer. I have another question.

### Node `EntombMeResheph`

Moloch! Allow me to explain the deification procedure, as it is clearly beneath your station to know!

        First, I must image the great Moloch's head, read your self's narrative from the folds of =ifplayerplural:your:thy= Holiest Brain, cross-check it against the Thin World's ambient log of His Eminence's life's deeds...

        *Herododicus whispers* I'm sure your version is the better one, Moloch...

**Choices:**
- **choice** `?` → `EntombMeResheph2`
    > ...

### Node `EntombMeResheph2`

Then I... stylize... the story, and I engrave it on the walls. Once I'm finished, the sarcophagus will open, and you can lay =player.reflexive= to rest!

**Choices:**
- **choice** `?` → `DoThatResheph`
    > Do it then.

### Node `DoThat`

Fine!

        Herododicus shines a cone of blue light at you.

        Starting ptychoscan............

**Choices:**
- **choice** `?` → `DoThat2`
    > ...

### Node `DoThat2`

...................................

**Choices:**
- **choice** `?` → `DoThat3`
    > ...

### Node `DoThat3`

...................................

**Choices:**
- **choice** `?` → `DoThat4`
    > ...

### Node `DoThat4`

Commencing cross-check with the Thin World annals............

**Choices:**
- **choice** `?` → `DoThat5`
    > ...

### Node `DoThat5`

...................................

**Choices:**
- **choice** `?` → `DoThat6`
    > ...

### Node `DoThat6`

...................................

**Choices:**
- **choice** `?` → `DoThat7`
    > ...

### Node `DoThat7`

Cross-check complete. Your narrative is compiled. Now to engrave it.

        Peace.... peace to all who canter in the House of the Coiled Lamb.

**Choices:**
- **choice** `?` → `End`
    > Peace, biographer.

### Node `DoThatResheph`

As you wish, Moloch!

        Herododicus shines a cone of blue light at you.

        Starting ptychoscan............

**Choices:**
- **choice** `?` → `DoThatResheph2`
    > ...

### Node `DoThatResheph2`

...................................

**Choices:**
- **choice** `?` → `DoThatResheph3`
    > ...

### Node `DoThatResheph3`

...................................

**Choices:**
- **choice** `?` → `DoThatResheph4`
    > ...

### Node `DoThatResheph4`

Commencing cross-check with the Thin World annals............

**Choices:**
- **choice** `?` → `DoThatResheph5`
    > ...

### Node `DoThatResheph5`

...................................

**Choices:**
- **choice** `?` → `DoThat6Resheph`
    > ...

### Node `DoThat6Resheph`

...................................

**Choices:**
- **choice** `?` → `DoThat7Resheph`
    > ...

### Node `DoThat7Resheph`

Cross-check complete. Your narrative is compiled, Moloch. Now to go engrave it.

        Peace.... peace to all who canter in the House of the Coiled... in Your House, Moloch.

**Choices:**
- **choice** `?` → `End`
    > Peace, biographer.

### Node `Unfinished`

'Tis a saying among the stonemasons, "Never finish a job too early." By the decretum of Sagittar, old as it is, they have until the Coiled Lamb is... is decom-.. passed... decompassed.... dead, deadlike... to complete their work on the Tomb.

        Bless the Coiled Lamb, peace to those who canter in his house, and let us pray the day never comes!

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `SultanGone`
    > But Resheph is dead. The sultanate is dissolved.
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.
