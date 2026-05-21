# Conversation: `Hortensa`

_Inherits: (default: BaseConversation)_

_3 start(s), 24 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Recame`

=name=, you are back! I feared we would lose you in the Tomb, but you look better than well. Perhaps I should have had greater faith, or at least less worry.

        Have you visited Barathrum's workshop, by the by? Klanq and Q Girl await you there.

**Choices:**
- **choice** `?` → `IHave`
    > I have.
- **choice** `?` → `IHavent`
    > Not yet.

### Start `Post Arms`

I drink in the sight of you, cub. Thank you for keeping safe.

**Choices:**
- **choice** `?` → `TombQuest`
    > I must enter Brightsheol through the Tomb of the Eaters.
- **choice** `?` → `Greetings`
    > Drink deeply of life, Hortensa. Let's talk.
- **choice** `?` → `End`
    > You too. Live and drink.

### Start `Greetings`

Drink deeply of life, =player.offspringTerm=. Are you finding your way?

**Choices:**
- **choice** `?` → `Bethesda`
    > Do you know anything about Bethesda Susa?
- **choice** `?` → `Omonporch`
    > What do you know about Omonporch and the self-appointed Earl?
- **choice** `?` → `Rumbling`
    > Did you feel that rumbling, Hortensa?
- **choice** `?` → `Klanq`
    > Have you ever met Pax Klanq?
- **choice** `?` → `HowLong`
    > Your hair is so gray! How long have you lived in Grit Gate?
- **choice** `?` → `OtherBarathrumites`
    > Could you tell me about the other Barathrumites?
- **choice** `?` → `LiquidTinker`
    > Are you a liquid-tinker?
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Start`

=player.OffspringTerm=, who are you?

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Stay safe, =name=. Please.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Hortensa.

### Node `IHavent`

Hie there now. Being tardy with Klanq carries risk, not so much from its offense as from its idle curiosity.

**Choices:**
- **choice** `?` → `End`
    > Very well. Live and drink.

### Node `IHave`

I am further relieved to know of another perspective looking upon this work. Klanq's presence here is vital, but it discomfits me: I cannot help but consider the introduction of chaos to an already chaotic endeavor to be a... conflagratory strategy.

**Choices:**
- **choice** `?` → `End`
    > I will exercise my best judgement. Live and drink.

### Node `TombQuest`

...  I do not like this.

        I know you will go. Please take care where you dig; mopango wanderers say the hot blood of Eater artifice yet runs in the guts of that place.

**Choices:**
- **choice** `?` → `End`
    > I thank you.

### Node `Bethesda`

There are pools of convalessence there. You see, when cryogenic mist condenses, it forms a cool, luminous liquid that's restorative if you're able to bathe in it.

        Oh! And in one of the ruined wards, the Alchemist keeps their shop. Who's the Alchemist, you ask? A sort of enigmatic figure -- amateur liquid-tinker, poet, merchant. Their methods aren't scientific, but they are useful if you're seeking a specific kind of liquid. Just be careful around them, =name=.

**Choices:**
- **choice** `?` → `Omonporch`
    > What do you know about Omonporch and the self-appointed Earl?
- **choice** `?` → `Rumbling`
    > Did you feel that rumbling, Hortensa?
- **choice** `?` → `Klanq`
    > Have you ever met Pax Klanq?
- **choice** `?` → `HowLong`
    > Your hair is so gray! How long have you lived in Grit Gate?
- **choice** `?` → `OtherBarathrumites`
    > Could you tell me about the other Barathrumites?
- **choice** `?` → `LiquidTinker`
    > Are you a liquid-tinker?
- **choice** `?` → `End`
    > Live and drink.

### Node `Omonporch`

Nothing other than a pet theory of mine that the Spindle is a liquid in laminar flow.

**Choices:**
- **choice** `?` → `Bethesda`
    > Do you know anything about Bethesda Susa?
- **choice** `?` → `Rumbling`
    > Did you feel that rumbling, Hortensa?
- **choice** `?` → `Klanq`
    > Have you ever met Pax Klanq?
- **choice** `?` → `HowLong`
    > Your hair is so gray! How long have you lived in Grit Gate?
- **choice** `?` → `OtherBarathrumites`
    > Could you tell me about the other Barathrumites?
- **choice** `?` → `LiquidTinker`
    > Are you a liquid-tinker?
- **choice** `?` → `End`
    > Live and drink.

### Node `Rumbling`

Yes! I was even provided with a brief premonition of it, as my workbench liquids are sensitive to small vibrations around the enclave.

**Choices:**
- **choice** `?` → `Bethesda`
    > Do you know anything about Bethesda Susa?
- **choice** `?` → `Omonporch`
    > What do you know about Omonporch and the self-appointed Earl?
- **choice** `?` → `Klanq`
    > Have you ever met Pax Klanq?
- **choice** `?` → `HowLong`
    > Your hair is so gray! How long have you lived in Grit Gate?
- **choice** `?` → `OtherBarathrumites`
    > Could you tell me about the other Barathrumites?
- **choice** `?` → `LiquidTinker`
    > Are you a liquid-tinker?
- **choice** `?` → `End`
    > Live and drink.

### Node `Klanq`

Oh, yes. You see, years and years ago, we were studying optics in the course of our research into laser technology. Barathrum was giving a lecture to some guest attendees, and...

        Oh, I'd rather not talk about it.

**Choices:**
- **choice** `?` → `Bethesda`
    > Do you know anything about Bethesda Susa?
- **choice** `?` → `Omonporch`
    > What do you know about Omonporch and the self-appointed Earl?
- **choice** `?` → `Rumbling`
    > Did you feel that rumbling, Hortensa?
- **choice** `?` → `HowLong`
    > Your hair is so gray! How long have you lived in Grit Gate?
- **choice** `?` → `OtherBarathrumites`
    > Could you tell me about the other Barathrumites?
- **choice** `?` → `LiquidTinker`
    > Are you a liquid-tinker?
- **choice** `?` → `End`
    > Live and drink.

### Node `HowLong`

*Hortensa chuckles.*

        Years. Decades on decades. Centuries, perhaps. Most of these wet-earred cubs were merely sketches in their mothers' dreambooks when I arrived to study under Barathrum. We knew so little then, know so little now.

**Choices:**
- **choice** `?` → `OtherBarathrumites`
    > Could you tell me about the other Barathrumites?
- **choice** `?` → `LiquidTinker`
    > Are you a liquid-tinker?
- **choice** `?` → `End`
    > Live and drink.

### Node `LiquidTinker`

*Hortensa chuckles.*

        You are sharp, =name=. In a way that's what I am. But liquids are more willful than scrap. I can't solder them together; they would run away, hide in the shale cracks, slowly come apart and disappear. I moreso think of myself as a wisewoman in dialogue with them -- I manage their moods and phases. My notebooks are full of their quirks and caprices. It's a wonder, isn't it, how at just the right temperature and pressure the continuity of matter is smashed apart? How the gaseous butterfly flits out of the dense worm?

**Choices:**
- **choice** `?` → `HowLong`
    > How long have you lived in Grit Gate?
- **choice** `?` → `OtherBarathrumites`
    > Could you tell me about the other Barathrumites?
- **choice** `?` → `End`
    > Live and drink.

### Node `OtherBarathrumites`

I won't denigrate them, =name=, or presume to speak for what's in their hearts. But I can direct you around the contours of the impressions they've left on me.

        Who would you like to hear about, =player.offspringTerm=?

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Barathrum`

Larger than life. Paternal. Concerned. The lenses of his eyes are focused on the far points of the world.

**Choices:**
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Otho`

Brassy. If you bent him he might snap. The way I treat liquids on my burner, Otho treats the units of the enclave.

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Jacobo`

Sharp as a tack, and living a life of deep meaning. Inventive and orderly. I can't say I understand his music, but I do love how expressive he is with it.

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Sparafucile`

Oh, I have such a precious vantage point on my sweet neighbor! When he achieves a moment of perfection in his craft -- a flawlessly spiraled barrel, a mound of powder measured to the grain -- he beams like the high salt sun. What a lovely smile.

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Q Girl`

She explodes like gas and dust in a quiet corner of the galaxy. Radiant. Revolutionary. She's a good listener and companion for supper, which you mightn't expect.

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Mafeo`

After supper I like to retreat to the library, take a storybook off the shelves, flop down on the chairbear, and lose myself in another world. Many of these worlds feature palaces, markets, gardens, ships. Many of those places have bells. When they do, I always think of Mafeo. More than anyone else, Mafeo could be a character in the bright world of a story, where this dusty place is itself confined to a mere storybook.

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Iseppa`

Our sleepy sage. So sweet. She calms me. I sit in her room and we muse on the nature of things.

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Neek`

I've instructed Neek since they were a lil' cub. What a strange one! Bouncey. Full of smiles. But brilliant in their own way. My favorite book in all the world is Neek's "Spiderwebs on Hoversleds". Who would have ever thought?

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Dardi`

Fiery. Blustery. Like the stews he cooks. If you're going to chat with him, make sure you have your schedule cleared and a ewer of honeyed wine.

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Shem -1`

Precious Shem. They've such a wider view of the world than we do. What a momentous obligation we've created for ourselves, and how I wouldn't undo it!

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Aloysius`

I've shared my honey with that prickly troglodyte for more years than I can count. I can't help but like him, and while he won't admit it, he feels the same about me.

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Ereshkigal`
    > Ereshkigal.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.

### Node `Ereshkigal`

She's a sphinx! So enigmatic that one. It's not entirely clear if she was there, waiting, when Q Girl succeeded at retreading the mainframe's guts, or if she sparked into being that very moment. Or was it some synthesis of the two?

**Choices:**
- **choice** `?` → `Barathrum`
    > Barathrum.
- **choice** `?` → `Otho`
    > Otho.
- **choice** `?` → `Sparafucile`
    > Sparafucile.
- **choice** `?` → `Jacobo`
    > Jacobo.
- **choice** `?` → `Q Girl`
    > Q Girl.
- **choice** `?` → `Mafeo`
    > Mafeo.
- **choice** `?` → `Iseppa`
    > Iseppa.
- **choice** `?` → `Neek`
    > Neek.
- **choice** `?` → `Dardi`
    > Dardi.
- **choice** `?` → `Shem -1`
    > Shem -1.
- **choice** `?` → `Aloysius`
    > Aloysius.
- **choice** `?` → `Start`
    > I'd like to ask about something else.
- **choice** `?` → `End`
    > Live and drink.
