# Conversation: `Eskhind`

_Inherits: `BaseSlynthMayor`_

_1 start(s), 54 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `StayLong`  _IfHaveState=`HindrenQuestFullyResolved`_

If it isn't the hero kendren, =name=.

        Welcome back to Bey Lah! Stay as long as you like.

**Choices:**
- **choice** `?` → `KindrishReturn`
    > Hindriarch, I have found Kindrish.
- **choice** `?` → `EskHindriarch`
    > How is life as Hindriarch?
- **choice** `?` → `End`
    > You're welcome. Live and drink.

## Nodes

### Node `EskhindAcceptSlynthStart`

I must admit, =name=, that I can think of few notions more challenging to my people than to welcome a flower-people into our town. Some will see them as no better than walking lah.

        But if the notion came from you, they might consider putting it to a vote, at least. If you'll stand by, I will call a referendum.

**Choices:**
- **choice** `?` → `EskhindAcceptSlynthStart2`
    > Please do.

### Node `EskhindAcceptSlynthStart2`

I'll have Warden Neelahind gather everyone as soon as they can spare the eyes and ears for it.

        *Hindriarch Esk canters away, voice already raised.* Hey, Warden!

**Choices:**
- **choice** `?` → `EskhindAcceptSlynthStart3`
    > ...

### Node `EskhindAcceptSlynthStart3`

The moments pass in hundreds, filled with dust and noise. Voices rise, hooves stamp the packed earth, and a fledgling democratic process takes its first faltering steps.

**Choices:**
- **choice** `?` → `SlynthRequestAccept`
    > ...

### Node `Start`

Hold there! Who are you? What do you want?

**Choices:**
- **choice** `?` → `End`
    > I am leaving.

### Node `Start`

Hold there! Who are you? What do you want?

**Choices:**
- **choice** `?` → `Hindriarch Keh sent me.`
    > I am =name=. Hindriarch Keh sent me.
- **choice** `?` → `Give back what you stole.`
    > I am justice. Give back what you stole.
- **choice** `?` → `End`
    > I am your worst nightmare. Prepare to die.
    - _part: `StartFight` (BroadcastForHelp=true)_
- **choice** `?` → `End`
    > Nothing. Live and drink.

### Node `Hindriarch Keh sent me.`

Keh? I'm shocked that she even deigned to speak my name. I am a pariah now, beneath discussion. Does she demand remuneration for the scant supplies I stole?

**Choices:**
- **choice** `?` → `You stole Kindrish.`
    > She says that you stole Kindrish, the village's treasure.

### Node `Give back what you stole.`

What I stole? I stole supplies to sustain myself and my sisters, nothing more, and little enough that no one would suffer for its absence. You would cut those from my hide?

**Choices:**
- **choice** `?` → `You stole Kindrish.`
    > No. You stole the treasure called Kindrish.

### Node `You stole Kindrish.`

*Eskhind bursts into forced, nervous laughter*

        Is that her angle? To claim that I stole Kindrish? Her influence must be waning more than even I knew.

**Choices:**
- **choice** `?` → `What are you saying?`
    > What are you saying?
- **choice** `?` → `You claim innocence?`
    > You claim innocence?
- **choice** `?` → `I suspected this.`
    > A frame-up. I suspected this.

### Node `What are you saying?`

What do you imagine I am saying? The aging, ineffectual leader of a village in isolation. A system that strives to forget anyone who sees the outside, no matter how much its inhabitants strive for a better tomorrow.

        Bey Lah's isolationism provides ideal patsies for any crime the Hindriarch chooses to commit.

**Choices:**
- **choice** `?` → `You think Keh stole the treasure?`
    > You think Keh stole the treasure?
- **choice** `?` → `Why should I believe you?`
    > Why should I believe you?
- **choice** `?` → `What should I do?`
    > What do you expect me to do, then?

### Node `You claim innocence?`

Yes. I am falsely accused.

        See, Bey Lah strives to forget anyone who sees the outside. The gerontocracy ensures that its leaders will always be aging and fearful. Pariahs like me can be easily accused of crimes committed by Keh or her cronies.

**Choices:**
- **choice** `?` → `You think Keh stole the treasure?`
    > You think Keh stole the treasure?
- **choice** `?` → `Why should I believe you?`
    > Why should I believe you?
- **choice** `?` → `Lies.`
    > Lies. You are trying to manipulate me.
- **choice** `?` → `What should I do?`
    > What do you expect me to do, then?

### Node `I suspected this.`

Well, good. I would give you a prize for your insight, but times have been lean.

        As you say, the Hindriarch is obviously framing me. As a pariah, I am an ideal patsy for Keh. Much as I love my people, they are weak of will and do not question the Grand-Doe.

**Choices:**
- **choice** `?` → `You think Keh stole the treasure?`
    > You really think Keh stole the treasure?
- **choice** `?` → `Why should I believe you?`
    > Why should I believe you?
- **choice** `?` → `Lies.`
    > Lies. You are trying to manipulate me.
- **choice** `?` → `What should I do?`
    > What can be done, then?
- **choice** `?` → `Eskhind is rude`
    > You didn't need to be rude about it.

### Node `You think Keh stole the treasure?`

Ay, you kendren are just as thick as the elders. I'd hoped otherwise.

        Yes, I am suggesting that old Grand-Doe is trying to fool you, and the village as well. I'm not certain that she stole it herself, but an investigation might undermine her authority, and she cannot have that.

**Choices:**
- **choice** `?` → `What should I do?`
    > What should I do, then?
- **choice** `?` → `Eskhind is rude`
    > You don't need to be so rude.

### Node `Why should I believe you?`

Why should you believe me? Well, why should you believe Keh? Ayvah, think about this!

        I'm not asking you to give me your unconditional trust, understand? Only to extend to me the same level of trust you give Keh. Is that not reasonable? Is that not just?

**Choices:**
- **choice** `?` → `What should I do?`
    > What are you suggesting I do?

### Node `Lies.`

Ayvah. I'd wanted Grand-Doe to be wrong about you kendren, but perhaps you are all violent fools after all.

        I'm not asking you to trust me, only to extend to me the same level of trust you give Keh. Is that not reasonable?

**Choices:**
- **choice** `?` → `What should I do?`
    > What are you suggesting I do?
- **choice** `?` → `Eskhind is rude`
    > You don't need to be so rude.
- **choice** `?` → `End`
    > You've wasted enough of my time. Prepare to die.
    - _part: `StartFight` (BroadcastForHelp=true)_

### Node `Eskhind is rude`

Rude? How dare--

        No, I... I apologize for my rudeness. Please understand that we have lost so much by leaving Bey Lah. My mind is not in a gentle place, and being revisited by the tyranny I left behind is causing newly-closed wounds to open.

        Forgive my tone, but please understand: I did not steal Kindrish. You are being used.

**Choices:**
- **choice** `?` → `What should I do?`
    > What should I do?

### Node `What should I do?`

The proof is in the petals, kendren. You want justice? Find out what really happened.

        If you find evidence, Warden Neelahind will support you. Speak to her. She is loyal to Grand-Doe, but more loyal to the truth.

        I will return to the village and we will sort this out. The Hindriarch will have to tolerate my presence until my name is cleared.

**Choices:**
- **choice** `?` → `End`
    > I'll look into this, but you'd better not go missing.
- **choice** `?` → `End`
    > I will. Live and drink.

### Node `Start`

Go tell Keh that I will remain in Bey Lah until this is sorted.

**Choices:**
- **choice** `?` → `End`
    > Very well. Live and drink.

### Node `Start`

Moon and Sun, =name=.

**Choices:**
- **choice** `?` → `EskHappyEnd`
    > How are things with Neelahind?
- **choice** `?` → `Questions`
    > I have questions for you.
- **choice** `?` → `End`
    > Wisdom and Will, Eskhind.

### Node `EskHappyEnd`

Things are good. Better than I dreamed. I owe you so much for your intervention, =name=.

        I still can't quite believe that my feelings are requited. I am at once elated and terrified. But this is good. My future is brighter now.

        Thank you.

**Choices:**
- **choice** `?` → `End`
    > May it brighten even further. Live and drink.

### Node `Start`

What is it, kendren?

**Choices:**
- **choice** `?` → `Questions`
    > I have questions for you.
- **choice** `?` → `SonnetPrompt`
    > Does this crumpled sheet of paper belong to you?
- **choice** `?` → `End`
    > Nothing. Live and drink.

### Node `Questions`

Ask away.

**Choices:**
- **choice** `?` → `SonnetPrompt`
    > Does this crumpled sheet of paper belong to you?
- **choice** `?` → `Why`
    > Why did you leave Bey Lah?
- **choice** `?` → `Who`
    > Who might have stolen Kindrish?
- **choice** `?` → `What`
    > What evidence should I be looking for?
- **choice** `?` → `Neelahind`
    > You and the Warden were close, were you not?
- **choice** `?` → `Brother`
    > The Hindriarch mentioned that you have a brother. Where is he?
- **choice** `?` → `End`
    > Nothing for now. Live and drink.

### Node `Why`

Why? Why did I leave a single parasang square piece of land upon which I was expected to live my entire life, forever obeying a woman whose sole qualification of rule is her gender and age? Why did I leave a place where we eat the same damned soup for nine out of ten meals and the height of occupational versatility is leatherworking?

        The question isn't why I left, it's why I'm the only one who chose to do so, why none of my pleas were convincing to the hindren I love. If we would just open the borders, it would never have come to this.

**Choices:**
- **choice** `?` → `Who`
    > Who might have stolen Kindrish?
- **choice** `?` → `What`
    > What evidence should I be looking for?
- **choice** `?` → `Neelahind`
    > You and the Warden were close, were you not?
- **choice** `?` → `Brother`
    > The Hindriarch mentioned that you have a brother. Where is he?
- **choice** `?` → `End`
    > Nothing for now. Live and drink.

### Node `Who`

The Hindriarch is the most likely suspect, in my opinion. She might have kept it for herself or sold it. I've been suspicious of her pet bodyguard, Kesehind, for years--I wouldn't put it past him to steal the treasure himself.

        That said, it might have been an outsider like you. I doubt any of the villagers had the nerve to steal such a valuable object, but I suppose it's faintly possible.

        But it wasn't Neelahind. You won't find a purer heart in all of Qud than hers.

**Choices:**
- **choice** `?` → `Why`
    > Why did you leave Bey Lah?
- **choice** `?` → `What`
    > What evidence should I be looking for?
- **choice** `?` → `Neelahind`
    > You and the Warden were close, were you not?
- **choice** `?` → `Brother`
    > The Hindriarch mentioned that you have a brother. Where is he?
- **choice** `?` → `End`
    > Nothing for now. Live and drink.

### Node `What`

Objects out of place, certainly. Bey Lah produces little and sees almost no violence, so signs of the outside world should be easy to find.

        You may wish to talk to the villagers, too. My people are starved for entertainment, gossip travels fast, and we are all notoriously poor liars.

**Choices:**
- **choice** `?` → `Why`
    > Why did you leave Bey Lah?
- **choice** `?` → `Who`
    > Who might have stolen Kindrish?
- **choice** `?` → `Neelahind`
    > You and the Warden were close, were you not?
- **choice** `?` → `Brother`
    > The Hindriarch mentioned that you have a brother. Where is he?
- **choice** `?` → `End`
    > Nothing for now. Live and drink.

### Node `Neelahind`

Yes. We were close. More than close.

        If it tore my heart to ragged halves to leave my people behind, leaving Neelahind shredded it into scraps.

**Choices:**
- **choice** `?` → `Why`
    > Why did you leave Bey Lah?
- **choice** `?` → `Who`
    > Who might have stolen Kindrish?
- **choice** `?` → `What`
    > What evidence should I be looking for?
- **choice** `?` → `Brother`
    > The Hindriarch mentioned that you have a brother. Where is he?
- **choice** `?` → `End`
    > Nothing for now. Live and drink.

### Node `Brother`

I have no brother. My two sisters are all the blood family I can claim.

**Choices:**
- **choice** `?` → `Keh believes`
    > Keh seems to believe otherwise.
- **choice** `?` → `Why`
    > Why did you leave Bey Lah?
- **choice** `?` → `Who`
    > Who might have stolen Kindrish?
- **choice** `?` → `What`
    > What evidence should I be looking for?
- **choice** `?` → `Neelahind`
    > You and the Warden were close, were you not?
- **choice** `?` → `End`
    > Nothing for now. Live and drink.

### Node `Keh believes`

Keh believes that she gets final say regarding who is a sister or brother. Regardless of what the sibling in question thinks.

        That's part of why I left.

**Choices:**
- **choice** `?` → `Questions`
    > May I ask further questions?
- **choice** `?` → `End`
    > Understood. Live and drink.

### Node `SonnetPrompt`

Oh. Oh no. Yes, that's. That's mine.

        I meant to burn it. I probably should have burned it. I wish I had burned it.

        May I please have it back?

**Choices:**
- **choice** `?` → `SonnetBurn`
    > So you can burn it?
- **choice** `?` → `SonnetNo`
    > Hmm. No, I think not.

### Node `SonnetNo`

You have me helpless. That poem is my clumsy expression of a deep truth that frightens me. It is a risk that I lacked the strength to take or leave.

        My heart quails in your hands, kendren.

**Choices:**
- **choice** `?` → `SonnetBurn`
    > You wish you had burned such a vital truth?
- **choice** `?` → `End`
    > It shall quail a bit longer. Live and drink.

### Node `SonnetBurn`

No! Yes? I don't know.

        Yes, I wish I burned it, but I wish I had given it. I wish I had never written it, or I had written it better, or I had simply confessed in person. I wish I had a harder heart.

        I wish you would give it back, or burn it, or give it to her.

**Choices:**
- **choice** `?` → `SonnetIntentions`
    > If I do give it back, what will you do with it?
- **choice** `?` → `SonnetDelivery`
    > I could give it to her.
- **choice** `?` → `End`
    > This got a bit intense. Live and drink.

### Node `SonnetIntentions`

I was trying not to think too hard about any of this until you found my poem, so... I can't say.

        But I can't ignore this sign of my cowardice, not after you found it.

**Choices:**
- **choice** `?` → `SonnetGiven`
    > Take the poem. Be brave.
- **choice** `?` → `SonnetDelivery`
    > Shall I deliver the poem for you?
- **choice** `?` → `End`
    > I will think further on this.

### Node `SonnetGiven`

Kendren... =name=. I will try.

        I... thank you. Live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Eskhind.

### Node `SonnetDelivery`

Deliver it? But how do you even know who--

        Mm. Never mind. My head is spinning. I think that if... the poem were to find itself in the warden's hands, that would perhaps be a good thing. Maybe.

**Choices:**
- **choice** `?` → `End`
    > Then perhaps it will. Live and drink.
- **choice** `?` → `SonnetGiven`
    > No, Eskhind. Take the poem. Be brave.

### Node `Start`  _IfHaveState=`HindrenVillageRavaged`_

I couldn't save them.

        I tried. I tried to save them.

**Choices:**
- **choice** `?` → `Insult`
    > I think this poem is yours.
- **choice** `?` → `End`
    > Condolences. Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageDoomed`_

I'm uneasy. What is this mounting dread? I cannot talk now.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Hah! Real justice? I never thought I'd see the like, not here. Well done!

        I'll admit, I would have preferred to avoid becoming Hindriarch, but I'm hoping to bring my people to a more Democratic form of governance. Then I can vote myself out.

**Choices:**
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Hindriarch.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Welcome back to Bey Lah, =name=. Stay as long as you like.

**Choices:**
- **choice** `?` → `MessageReceived`
    > I believe this poem is yours.
- **choice** `?`
- **choice** `?` → `EskHindriarch`
    > How is life as Hindriarch?
- **choice** `?` → `End`
    > Live and drink, Hindriarch.

### Node `Start`

You have my gratitude for this exoneration, kendren. This worked out better than I expected thanks to you.

        I'll admit, I would have preferred to avoid becoming Hindriarch, but I'm hoping to bring my people to a more Democratic form of governance. Then I can vote myself out.

**Choices:**
- **choice** `?` → `MessageReceived`
    > I believe this poem is yours.
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `MessageReceived`

Oh! Well. For you to bring me this after returning me to Bey Lah...

        *she smiles.*

        Message received, =name=. If I expect my people to face their fear of the unknown, I owe it to them to face mine.

        I will confess my feelings to Neelahind, give her the poem I wrote, and accept whatever reply she has for me. Thank you again.

**Choices:**
- **choice** `?` → `End`
    > You're welcome. Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Kendren! I am glad to see you.

        Thank you again for bringing Neela around, and please forgive her reservation. She mourns the people she thought she knew, but our future will be brighter together.

**Choices:**
- **choice** `?` → `End`
    > Of course. Live and drink.

### Node `Start`

Kendren, thank you.

        Things may seem grim, but I have a new strength with Neela by my side.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Oh, it's you. Need to rest by the fire?

        It's fine, my wrath has clarified. You were never the problem. Live and drink.

**Choices:**
- **choice** `?` → `Insult`
    > I think this poem is yours.
- **choice** `?` → `End`
    > Live and drink.

### Node `SlynthRequest`

You're just trying to keep dear Esk informed, then? Or could it be that you're wondering if that home may be Bey Lah?

**Choices:**
- **choice** `SlynthRequestAcceptChoice` → `EskhindAcceptSlynthStart`

### Node `SlynthRequestAccept`

*The Hindriarch returns at long last, expression bright.*
        
        By majority vote, the slynth are welcome to take up permanent residence here in Bey Lah! I didn't think we were ready, but I suppose my people showed me otherwise. 
        
        They will effectively be apprentices to the village until they choose a vocation. If they choose to come here, that is to say.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, Hindriarch.

### Node `SlynthRequestReject`

I am afeared to even mention this notion to the villagers. Can you imagine my epitaph?
      
      "Here lies the youngest Hindriarch in Bey Lah's history, trampled to death because she suggested we invite in a people most readily described as 'lah with legs'."
      
      If they trusted you more, maybe we could put it to a vote. But as it is? No. Sorry, =name=.

### Node `SlynthAbout`

We are on the tips of our hooves, =name=! Any word about the slynth?

### Node `SlynthArrived`

Never greater has been my desire to be voted out of office.

        Oh, not because of the slynth! Well, yes, because of the slynth, but it's because I'd rather be out there with them – scouting, guarding, even tending to lah would be better than all this dry supervisory work.

        Room, board, assignments... it never occurred to me that immigration would require such intensive logistics.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, Hindriarch.

### Node `SlynthSettled`

Live and drink, =name=!

        At long last I bear a lighter load of work coordinating our new family members. I won't claim that all of my people are fully comfortable with the slynth, but the faundren love them.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, Hindriarch.

### Node `Insult`

*Eskhind looks at the crumpled sheet of paper for several long seconds, then looks at you for several even longer seconds.*

        Why can't you just shoot me like the other kendren? Those wounds heal better, and death would be preferable to what you have done to me.

        *crumpling the paper up once again, Eskhind lights it aflame and tosses it away as it burns.*

        Go sit on a tumbling pod. I've had enough of you.

**Choices:**
- **choice** `?` → `EmptyApology`
    > I'm sorry.
- **choice** `?` → `End`
    > Live and drink.

### Node `EmptyApology`

*The hindren pariah ignores you.*

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Don't you have someone else to bother?

        Live and drink piss.

**Choices:**
- **choice** `?` → `Insult`
    > I think this poem is yours.
- **choice** `?` → `End`
    > Rude.

### Node `KindrishReturn`

Oh, so you have! Amazing work, kendren. We owe you more than we can give, but here is what we can give nonetheless.

        You are more than welcome here in Bey Lah any time.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Hindriarch.

### Node `EskHindriarch`

Extremely frustrating! But I am yet hopeful.

        My people are resistant to change, but they don't seem opposed to the idea of a Democracy. I need to give them a measure of time before we hold an election, but they'll ultimately agree as long as I am acting Hindriarch.

        Then, fates willing, they will vote me out. I'll be voting for Isahind, myself. Once I convince her to run.

**Choices:**
- **choice** `?` → `End`
    > May fortune favor you. Live and drink.

### Node `Start`

=name=.

**Choices:**
- **choice** `?` → `End`
    > Eskhind.
