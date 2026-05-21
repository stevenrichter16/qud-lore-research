# Conversation: `JoppaFarmerConvert`

_Inherits: (default: BaseConversation)_

_5 start(s), 16 node(s), 1 root-level choice(s)_

---

## Conversation-level choices

- **choice** `Trade`

## Start nodes (conditional entry points)

### Start `SpeakNoMore`  _IfTestState=`ConvertNoSpeak`_

There are no more words for us, wanderer.

**Choices:**
- **choice** `?` → `End`
    > ...

### Start `SpeakNoMore`  _IfTestState=`ConvertSated`_

=name=! Live and drink, pilgrim.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Start `FinishedPilgrimageQuest`

=name=! Live and drink, pilgrim.

**Choices:**
- **choice** `?` → `Stilted`
    > I have visited the Six Day Stilt.
- **choice** `?` → `End`
    > Live and drink.

### Start `HasPilgrimageQuest`

Wanderer and =pronouns.formalAddressTerm=! Have you journeyed yet to the Stilt, and seen the Sacred Well?

**Choices:**
- **choice** `?` → `End`
    > Not yet, friend. Live and drink.

### Start `Welcome`

Wanderer! Do you venture northwise? Into the Great Desert and nearer the Six Day Stilt?

**Choices:**
- **choice** `?` → `Stilt`
    > What is the Six Day Stilt?
- **choice** `?` → `Why`
    > Why do you ask?
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Stilted`

Ah!

				Tell me, =pronouns.formalAddressTerm=, was it the picture of wonder as I see it in my mind's eye? Were you beauty-struck by its truths?

**Choices:**
- **choice** `?` → `Ohh`
    > Truly breathtaking. How the glass glittered in the sun!
- **choice** `?` → `Glorious`
    > To behold the Argent Fathers in simulacra... what revelation!
- **choice** `?` → `ShakyNah`
    > I saw only empty spectacle. Who can worship a hole in the ground?

### Node `Ohh`

So it's true! O Argent Fathers, how far-reaching your works!

				... and my trinket? Did you cast it into the Sacred Well?

**Choices:**
- **choice** `?` → `Well`
    > I did.
- **choice** `?` → `Lost`
    > Sadly, it was lost.
- **choice** `?` → `Flipped`
    > No, I took it apart or sold it or something.

### Node `Well`

Moon and Sun! The Argent Fathers bless us, our paths are chromed and glistering.

				You have my thanks, =pronouns.formalAddressTerm=. Bel shield you.

**Choices:**
- **choice** `?` → `End`
    > And you as well.

### Node `Lost`

Oh, I am leaden with this knowledge. Yet am I soothed by your pilgrimage.

				Moon and Sun, I feel the warmth of the Kasaphescence yet. Praise the Argent Fathers.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Flipped`

Oh, how your words rasp my soul, =player.formalAddressTerm=. You abrade me.

				Let us speak no more.

**Choices:**
- **choice** `?` → `End`
    > Very well.

### Node `Glorious`

So you have seen the truth? Great are the machinations of our Argent Fathers!

				Our meeting, a tiny Canticle. Fate dances in our shadows by their will and word.

				Moon and sun, what a day! What a fine day. Praise Shekhinah!

**Choices:**
- **choice** `?` → `End`
    > Praise Shekhinah!

### Node `ShakyNah`

Wh-

				My heart's sheen wanes to hear this of you. You abrade me, =player.formalAddressTerm=, I am scuffed.

				What of my trinket, then? Did you cast it into the... "hole in the ground?"

**Choices:**
- **choice** `?` → `InTheHole`
    > Yes, I threw it in the hole.
- **choice** `?` → `LostIt`
    > No, I lost it.
- **choice** `?` → `LosingIt`
    > I gave it to someone. Or sold it, perhaps.

### Node `InTheHole`

Well... the light of the Kasaphescence yet glimmers through your rasping edge.

				I must, then, thank you.

**Choices:**
- **choice** `?` → `End`
    > You're welcome.

### Node `LostIt`

My stomach lurches and quavers at the shock of this knowledge.

				If there is a lesson in your disregard, I will meditate upon it in my own time.

				Let us speak no more.

**Choices:**
- **choice** `?` → `End`
    > As you say.

### Node `LosingIt`

Ah, a pit opens under my stomach!

				Let us speak no more, I beg you. You scuff me. Live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Stilt`

Ah! The great Mechanimist temple of glass, the sacred offering Well, and history in stone relief. Peopled by the Argent Fathers, in statue and light sculpture. And circled by the grand bazaar. I hear there are more people there than numbers in the void, and their chatter makes a sound wholly raw and new to the world.

				Will you go there, and take my bauble? Will you offer it at the Well, where I cannot?

**Choices:**
- **choice** `?` → `Bauble`
    > Your bauble?
- **choice** `?` → `Fathers`
    > Argent Fathers?
- **choice** `?` → `WhyNot`
    > Why can you not go?
- **choice** `?` → `Agree`
    > I will make the journey.
- **choice** `?` → `End`
    > I cannot commit to this. Live and drink.

### Node `Bauble`

Yes! My neighbor-kin tire of the tale. I was scything the vine when the flat of my blade turned something loose from the soil. My heart has stirred before at the sight of chrome, but to free a small splinter myself, to slide a bead on the abacus of Beauty...
        
        Will you go, then? And offer my bauble at the Well?

**Choices:**
- **choice** `?` → `WhyNot`
    > Why can you not go?
- **choice** `?` → `Stilt`
    > What is the Six Day Stilt again?
- **choice** `?` → `Agree`
    > I will make the journey.
- **choice** `?` → `End`
    > I cannot commit to this. Live and drink.

### Node `Fathers`

I am no rector, understand, but They are the molders of chrome. The gods under Shekhinah who wrought metal edifices from the raw Kasaphescence.

				Will you go?

**Choices:**
- **choice** `?` → `Why`
    > Perhaps. Why?
- **choice** `?` → `End`
    > I cannot commit to this. Live and drink.

### Node `Why`

I would ask you make an offering at the sacred Well of my bauble. Moon and sun, I beg you!

**Choices:**
- **choice** `?` → `WhyNot`
    > Why can you not go?
- **choice** `?` → `Stilt`
    > What is the Six Day Stilt?
- **choice** `?` → `Agree`
    > I will make the journey.
- **choice** `?` → `End`
    > I cannot commit to this. Live and drink.

### Node `WhyNot`

Friend, I would be a smoldering heap, cooked to death by the ray of a dawnglider! I would be a slug-riddled corpse by the rifles of the Issachari!

				There is no kindness in the Great Desert, and little more in the canyons. I cannot go and live.

**Choices:**
- **choice** `?` → `Stilt`
    > What is the Six Day Stilt again?
- **choice** `?` → `Agree`
    > I will make the journey.
- **choice** `?` → `End`
    > I cannot commit to this. Live and drink.

### Node `Agree`

Moon and sun, =pronouns.formalAddressTerm=! You have my deep and many-sided thanks. Here, take the trinket now. And if you're to ever return, let us visit again.

				Live and drink!

**Choices:**
- **choice** `GiveTrinket` → `End`
    > Live and drink.
    - _part: `ReceiveItem` (Table=JoppaConvertTrinket)_
