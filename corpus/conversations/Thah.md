# Conversation: `Thah`

_Inherits: (default: BaseConversation)_

_0 start(s), 19 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Ah, a stranger. Welcome to the hydropon. I am Thah.

**Choices:**
- **choice** `Greet` → `GreetThah`
    > Moon and Sun, Thah. I am =name=.
- **choice** `Slynth` → `SlynthWhat`
    > What manner of being are you?
- **choice** `How` → `HowAreThings`
    > Is all well here?
- **choice** `Bye` → `End`
    > Live and drink, Thah.

### Node `GreetThah`

Well met, =name=. Please forgive the, ah, austerity of our cradle. You may sup with us at our meager camp and rest under the shade of this Palladium shell. Sorry, as well, about the crowding.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `Resentment`
    > You don't seem to like your accommodations.
- **choice** `?`

### Node `SlynthWhat`

We are called slynth, a people grown one by one from a hydroponic cradle containing a cutting of water lily and empowered by sunslag. We are but a handful of generations old, and kept no written history until I was grown, ah, some number of decades ago.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `HowAreThings`

Well enough. We drink the sun's rays, eat what we scavenge, rest under the shell, and it is. Enough.

        I read and tinker. Some hunt. Others tend the cradle. Each day is like the next. Every so often, someone leaves.

        We, ah, rarely hear from them thereafter. I hope they are all well.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `Resentment`
    > You don't seem happy with the status quo.
- **choice** `?`

### Node `Resentment`

To be wholly honest, =name=, I grow frustrated.

        We are a young species, grown one by one in yonder sun-touched cradle. Over years, we have increased, but not, ah, not. Not grown.

        Look around you. You see it, yes? This hydropon is no settlement.

**Choices:**
- **choice** `?` → `Helping`
    > How can I help?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Helping`

This is an existential conundrum, =name=, I'm not sure that it could-- ah, wait, no. I am reconsidering.

        No, you could help. If you wished. I think.

        May I explain?

**Choices:**
- **choice** `?` → `Helping2`
    > Please do.
- **choice** `?` → `End`
    > I have changed my mind. Live and drink.

### Node `Helping2`

I don't believe my people wish to stay here, but we have had so little, ah, meaningful contact with other sapient creatures. We have no allies. We have nowhere to go but here.

**Choices:**
- **choice** `?` → `Helping3`
    > ...

### Node `Helping3`

You travel far and wide, do you not? You have the air of a traveling hero! From the epics. As such, you have seen many settlements, likely ingratiated yourself to some.

**Choices:**
- **choice** `?` → `Helping4`
    > ...

### Node `Helping4`

Surely, if you were to intercede on our behalf, some might welcome us? If, ah, let us say three settlements were to offer us shelter, this would grant us both direction and agency. Would you consider being our ambassador? Not unpaid.

**Choices:**
- **choice** `?` → `Accept`
    > I will help.
- **choice** `?` → `End`
    > I decline. Live and drink.

### Node `Accept`

Thank you, =name=. I have, ah, I have been crafting a personal project. Of sorts. I promise it to you for this task, and of course the gratitude of a young species.

        Return to me after settlements agree to grant us refuge, and I will discuss them with my kin.

**Choices:**
- **choice** `?` → `End`
    > Live and drink. I will return with news.

### Node `Start`  _IfHaveState=`SlynthCandidatesReady`_

Come, =name=. It is time.

**Choices:**
- **choice** `?` → `SlynthDecision`
    > ...

### Node `Start`

Ah, =name=, Moon and Sun.

        Any news of our future home?

**Choices:**
- **choice** `?` → `LandingPadsCommentary`
    > Yes, I have news about the slynths' sanctuary.
- **choice** `?` → `End`
    > None yet. Live and drink, Thah.

### Node `LandingPadsCommentary`

Ah! Let us discuss?

Joppa! An historic site. I wasn't sure if, ah, it still existed. As a village.

        The quiet of the saltmarshes may be strange to my people, but some have voiced a wish for more peace than the Reef can spare. Thank you for this choice, =name=.

The worshippers of Shekhinah? Fascinating. I, ah, don't know what to think of that.

        It may be what my kin need, now I consider it. The Canticles make little sense to me but they are, ah, compelling. More compelling than me, certainly. I will discuss this with the others.

Did you say Barathrumites? So that's how it's pronounced.

        Grit Gate is, ah... that's where Q Girl resides, isn't it? She wrote my favorite book, Disquisition on the Malady of the Mimic. I imagine such a home would have a positive effect on my kin. I will speak to them.

Kyakukya? I didn't realize it had so many syllables.

        That's where the, ah, faithful to the ape-god gather, correct? And, uh... Crowsong, as well. I will present this possibility to my people and we will discuss it.

Ezra is, ah, the village at the base of the Spindle, is it not?

        The very cradle of history. Not that my kin have a strong taste for history, but perhaps living amongst fresco and bas-relief will change their, ah, collective outlook?

Fascinating. I know nothing about these mopango, but any people whose love for learning and discovery defines them are, ah... good, in my opinion. I will discuss this with my kin, and see if they agree.

There is a sadness in, ah... choosing pariahs. Some of my kin dreamed of belonging, and the very word is the antithesis of belonging.

        But then, if wanderers look after one another, there is a belonging in that as well. Even alone, we would not be alone. I will offer this choice to the others and we will discuss it.

The nearby settlement? The one, ah, founded by three svardym and a galgal? I've always been mortally afraid to go there, knowing even the barest facts.

        But you say they will accept us? Perhaps I was wrong.

Bey Lah is real? Stain me surprised to hear so... I, ah, believed the hindren exclusively diasporic.

        There is an undeniable poetry in it, if the slynth should emigrate to a mythical and secretive village. I will discuss this with my kin.

Chavvah? The, ah, the... the tree of life? Allows us joining?
				
				That, that is simply, ah, extraordinary. I will apprise my kin of this, and we will, ah... we will ponder what it may mean for us.

**Choices:**
- **choice** `?` → `CandidatesReady`
    > I have made my inquiries. It is time for the slynth to choose a new home.
    - _part: `SlynthCandidatesReady`_
- **choice** `Joppa`
    > The village of Joppa has agreed to accept the slynth as their own.
- **choice** `Mechanimists`
    > The Mechanimists of the Six Day Stilt agreed to accept the slynth as their own.
- **choice** `Barathrumites`
    > The Barathrumites of Grit Gate agreed to accept the slynth as their own.
- **choice** `Kyakukya`
    > The village of Kyakukya has agreed to accept the slynth as their own.
- **choice** `Ezra`
    > The village of Ezra has agreed to accept the slynth as their own.
- **choice** `Mopango`
    > The mopango of the Tomb agreed to accept the slynth as their own.
- **choice** `Pariahs`
    > If the slynth choose to wander Qud, the Pariahs have agreed to look after them.
- **choice** `YdFreehold`
    > The Yd Freehold agreed to accept the slynth as their own.
- **choice** `Hindren`
    > The village of Bey Lah has agreed to accept the slynth as their own.
- **choice** `Chavvah`
    > The chimes of Chavvah have agreed to accept the slynth as their own.
- **choice** `?` → `Start`
    > Let's talk about something else.

### Node `CandidatesReady`

Wanderer, thank you! I will tell my kin of these places. We will convene and discuss, and we will, ah, choose. Please be patient in the meantime.

**Choices:**
- **choice** `?` → `End`
    > As you say, Thah. I will return.

### Node `Start`

Moon and Sun, =name=.

**Choices:**
- **choice** `?` → `SlynthLeave`
    > It's curious to see you still here, after helping your kin emigrate.
- **choice** `ChoiceGetStar` → `GiveStar`
    > Why have you asked me to return?
- **choice** `?` → `End`
    > Moon and Sun, Thah.

### Node `GiveStar`

I've been crafting a kind of a relic, a piece of art that serves a purpose and that you can carry on your, ah, your person. I finally finished building it while you were away, and the opportunities you offered us inspired the finishing touches. I'd like you to have it.

**Choices:**
- **choice** `?` → `End`
    > I will cherish it. Live and drink.

### Node `SlynthDecision`

After some discussion and deliberation, we have come to consensus: Joppa shall be the new home of the slynth. The notion of a lasting, peaceful life with, ah, purpose... this appeals to many of our number, and where better than Abram's very watervine marsh?

        Our emigration party departs for the saltmarshes in the morning.

After some discussion and deliberation, we have come to consensus: most of our number will join the Mechanimist faith, and reside at the Stiltgrounds at the edge of the Mogh'ra'yi.

        Our emigration party departs for the Six Day Stilt in the morning.

After some discussion and deliberation, we have come to consensus: The new home of the slynth is among the disciples of Barathrum. My kin have agreed to dedicate themselves to the pursuits of learning and service.

        Our emigration party departs for Grit Gate in the morning.

After some discussion and deliberation, we have come to consensus: Kyakukya shall be the new home of the slynth. There are many ways to grow when one is planted in the very heart of Qud.

        Our emigration party departs for the river in the morning.

After some discussion and deliberation, we have come to consensus: The new home of the slynth is among the villagers of Ezra, harvesting musa alongside the banana ranchers and singing their songs.

        Our emigration party departs for Omonporch in the morning.

After some discussion and deliberation, we have come to consensus: the slynth shall become mopango, taking root in ancient rock and casting our gaze back toward the history that preceded us.

        Our emigration party departs for the Tomb of the Eaters in the morning.

After some discussion and deliberation, we have come to consensus: The new home of the slynth is no home at all, but the floating fellowship of Qud's Pariahs. We were blessed with roots that need not fix themselves to the soil and have opted to use them accordingly.

        We will split into parties and leave to meet with other wayfarers come morning.

After some discussion and deliberation, we have come to consensus: the slynth shall join the Yd Freehold, remaining in the reef where our cradle lies but mingling among other sapient creatures to learn their ways and teach what we know.

        Our emigration party departs for the Freehold in the morning.

After some discussion and deliberation, we have come to consensus: Bey Lah shall be the new home of the slynth. There is a familiarity to this tucked-away village, newly greeting the world; this is our gentle emergence from obscurity, and one not undertaken alone.

        Our emigration party departs for the flower fields in the morning.

After some discussion and deliberation, we have come to consensus: the slynth shall become a part of Chavvah, the living city. There are no words for the breadth of futures before us, and we would not know them if they were. Perhaps we will learn to chime.

After some discussion and deliberation, we have come to consensus: the slynth shall become citizens of =village.name=. We shall learn the practice of =village.activity=, hold =village.sacred= dear and spurn =village.profane=.

        Our emigration party departs for =village.name= in the morning.

**Choices:**
- **choice** `?` → `SlynthResolution`
    > May the Argent Fathers watch over you.
    > May you find knowledge.
    > May Oboroqoru be merciful.
    > May the Eaters protect you.
    > Mayest thou rest ever in the Light of the Kasaphescence.
    > May the winds favor you.
    > Chime joyfully.
    > May the Fates favor you.

### Node `SlynthResolution`

Ah, one last little thing, =name=. About your reward... it's not quite finished, but now I know just what it needs.

        Please return to the hydropon after my kin have safely reached their new home and I will give it to you. I will not leave the cradle.

**Choices:**
- **choice** `?` → `End`
    > I will. Live and drink.

### Node `SlynthLeave`

Yes, I've decided to stay. It's not that, ah, it's not that I wouldn't enjoy a life of farming. But the thought of leaving the cradle after decades of watching it... I couldn't.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've stayed. I don't, ah, resent that my kin have found succor in the embrace of faith, but I don't know how to walk that path myself. Someone needs to watch over the hydropon, besides.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've stayed. I'd love to see the vaunted halls and, ah, bathe in the light of brilliant minds, but when I think about the journey my roots lock up. I feel, ah, unready. Someone must watch over the cradle, besides.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've decided to stay. It's not that, ah, it's not that I wouldn't enjoy sharing knowledge with the mayor of our new home. But the thought of leaving the cradle after decades of watching it... I couldn't.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've stayed. As fascinated as I would be to examine the statuary and bas-reliefs, my favorite mode of, ah, interaction with history is through the written word. Someone must watch over the cradle, besides.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've decided to stay. The Tomb sounds, ah, cozy, but I cannot fathom making such a macabre place my home. Someone must look over the cradle, besides.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've stayed. If I am entirely honest, the idea of a life on the road sounds, ah... unpleasant. To me, personally. I have grown accustomed to a life of collection, curation, and study that I don't care to abandon for adventure. Someone must stay to watch over the cradle, besides.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've decided to stay. I don't disbelieve that the Yd Freehold is as safe as you say, but the fears instilled in me when I first learned to read as a fresh sprout haunt me even now. Perhaps in time I will visit, but in the meantime I can look after the cradle, as someone ought to do.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've decided to stay. The flower fields sound beautiful, and no doubt there is much to learn from the hindren. But the thought of leaving the cradle after decades of watching it... I couldn't.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I, ah, I remain.
				
				I badly wish to taste of Chavvah's secrets, but the wonder I feel for such an entity is eclipsed only by the terror of such an experience. I cling to an excuse that the hydropon must be watched and wait. Perhaps someday I will shed that excuse's film and step free.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

Yes, I've decided to stay. I'm sure =village.name= is a good home for my kin, but I have no particular loathing for =village.profane= and even less reverence for =village.sacred=. Someone must look over the cradle, besides.

        The hydropon is even less a village now, but you're welcome to rest here whenever you like.

**Choices:**
- **choice** `?` → `End`
    > Moon and Sun, Thah.
