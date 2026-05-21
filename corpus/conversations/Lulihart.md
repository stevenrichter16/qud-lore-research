# Conversation: `Lulihart`

_Inherits: `BaseSlynthMayor`_

_1 start(s), 18 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Refuse`

I see. In that case, rest and speak a bit with me, won't you? My worries can wait another day.

        That said, if you change your mind, you'll come find me, won't you?

**Choices:**
- **choice** `?` → `End`
    > Perhaps. Live and drink.

## Nodes

### Node `Start`

Be careful in the flower fields.

        Even with Bey Lah marked on your map, it's easy to get lost. Lost travelers feed the lah.

**Choices:**
- **choice** `?` → `End`
    > I will be careful, thank you.

### Node `Start`

Hold a moment, =player.formalAddressTerm=. Are you looking for work?

**Choices:**
- **choice** `?` → `Job seeker`
    > I am.
- **choice** `?` → `Refuse`
    > I am not.

### Node `SlynthRequest`

I can't help but wonder why you're telling me this in particular. I am not a mayor, nor even a citizen. I am a drifter, a pariah, and my 'people' are those who have no home anywhere else.

      ... and here I wonder a bit less. You're asking me to whisper into the winds on behalf of the slynth, aren't you?

### Node `SlynthRequestAccept`

What a strange fate, to pass from new sentience to outcast with no steps in between. Regardless, if it is their will and you vouch for them, that is enough for me. Tell the slynth that should they choose to wander, the wind will blow at their backs.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, Lulihart.
    - _part: `AddSlynthCandidate` (Sanctuary=pariah caravans Plural=true)_

### Node `SlynthRequestReject`

It is hardly so simple, =name=. We drifters hold no hierarchy. I can whisper all I like, but no winds will blow behind the slynth if your name cannot stir more than a breeze. Make yourself known to Pariahs and ask me again.

### Node `SlynthAbout`

Still gathering landing pads for your drifting vessels, then, =name=?

**Choices:**
- **choice** `?` → `Start`
    > Yes, I am.

### Node `SlynthArrived`

New voices, strange and beautiful, carry on the salt breeze.

        Some will no doubt be silenced by sun, blade, thirst, bullet, or glow, but they will not fall still alone.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, Lulihart.

### Node `SlynthSettled`

Live and drink, =name=.

        Have you seen your slynth out there? My sources tell me that they are, for the most part, traveling well enough with others. They stop by my tent from time to time to visit and smoke with me, as you do.

        One might assume they were born for this kind of life.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, Lulihart.

### Node `Job seeker`

Lovely. Take a seat. Chew the bark with me, and I will tell you what I know.

        I've heard tell that my ancestral hometown, Bey Lah, is in some kind of trouble. They've opened their borders for the first time I know of and are specifically seeking to hire kendren -- that's their word for outsiders like you. Would you be willing to go see what they need?

**Choices:**
- **choice** `?` → `Who`
    > Who are you?
- **choice** `?` → `How`
    > How do you know this?
- **choice** `?` → `Why`
    > Why do you care?
- **choice** `?` → `Why Not`
    > Why don't you go there yourself?
- **choice** `?` → `Very Well`
    > Very well, I will go to Bey Lah as you ask.
- **choice** `?` → `Refuse`
    > Pass. This task is not to my liking.

### Node `Who`

My name is Lulihart. The blood of the hindren runs through my veins, but two of my three parents were kendren, so that blood is... dilute, and salt-brined from being born out here.

        Dilute, salty blood. Heh.

**Choices:**
- **choice** `?` → `Very Well`
    > Very well, I will go to Bey Lah as you ask.
- **choice** `?` → `How`
    > How do you know about Bey Lah's trouble?
- **choice** `?` → `Why`
    > Why do you care about Bey Lah?
- **choice** `?` → `Why Not`
    > Why don't you go there yourself?
- **choice** `?` → `Refuse`
    > Pass. This task is not to my liking.

### Node `How`

My water goes to scouts to keep a distant eye on Bey Lah. To make sure that it is still there, still safe.

        I have never been within a parasang of my people's land, but I know exactly where the once-hidden village stands. I will share this knowledge with you if you agree to consider whatever their request may be.

**Choices:**
- **choice** `?` → `Very Well`
    > Very well, I will go to Bey Lah as you ask.
- **choice** `?` → `Who`
    > Wait, who are you?
- **choice** `?` → `Why`
    > Why do you care?
- **choice** `?` → `Why Not`
    > Why don't you go there yourself?
- **choice** `?` → `Refuse`
    > Pass. This task is not to my liking.

### Node `Why`

Even blood as thin as mine ties me to the cervidian meadow. The hindren may not say so, but they are my family.

**Choices:**
- **choice** `?` → `Very Well`
    > Very well, I will go to Bey Lah as you ask.
- **choice** `?` → `Who`
    > And who are you?
- **choice** `?` → `How`
    > How do you know Bey Lah's trouble?
- **choice** `?` → `Why Not`
    > Why don't you go there yourself?
- **choice** `?` → `Refuse`
    > Pass. This task is not to my liking.

### Node `Why Not`

I am not welcome in Bey Lah.

        My blood is not pure, and I was not born in the meadow. These things make my name as salt in the mouths of true hindren.

        They are misguided, but they are my misguided family. They stagnate as Qud changes around them. I worry.

**Choices:**
- **choice** `?` → `Very Well`
    > Very well, I will go to Bey Lah as you ask.
- **choice** `?` → `Who`
    > Who are you?
- **choice** `?` → `How`
    > How do you know this?
- **choice** `?` → `Why`
    > Why do you care?
- **choice** `?` → `Refuse`
    > Pass. This task is not to my liking.

### Node `Very Well`

Bless you, =player.formalAddressTerm=. I feel better knowing that at least one kendren will reach back to aid my kin. They are on the cusp of a new fate, and I wish to see it while I yet live.

        Let me advise you of Bey Lah's location, and here is a little chew-boon for your trouble.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Lulihart. Live and drink.

### Node `Start`

I hear that Bey Lah's status is once again quo. I hoped for a measure more of change, but thousands of years of tradition do not give so easily.

        Thank you for helping my foolish people.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

I've heard that the youngest Hindriarch in history now leads Bey Lah, and their warden aims to join the Quetzal Caucus. You've worked wonders, kendren.

        I can't wait to see what happens next.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageRavaged`_

Every flame burns low one day, but the warmth of my people's story still carries me forward.

        Bey Lah has not survived joining Qud, but the hindren live on, and our legacy will never be wholly lost.

        I wonder what became of Kindrish.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Come smoke with me, friend. Set a spell.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
