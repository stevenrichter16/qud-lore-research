# Conversation: `Haddas`

_Inherits: `BaseSlynthMayor`_

_0 start(s), 16 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

You are welcome in the village of Ezra, seedling. Sit with me and watch the sun breathe shadows over the day.

**Choices:**
- **choice** `TreeChoice` → `Tree`
    > You're a tree.
- **choice** `ReliefsChoice` → `Reliefs`
    > The carved reliefs here are Eater-ancient. What is the history of this place?
- **choice** `WardenChoice` → `Warden`
    > Who is Ezra's warden?
- **choice** `MerchantsChoice` → `Merchants`
    > Point me toward your merchants.
- **choice** `WorkChoice` → `Work`
    > I'm looking for work.
- **choice** `EndChoice` → `End`
    > Live and drink, tall friend.

### Node `SlynthRequest`

HA. You would fain plant them here, to joggle their fingers at the salt sky alongside the musa?

**Choices:**
- **choice** `?` → `SlynthRequestAccept`
    > I would.

### Node `SlynthRequestAccept`

Lilypad-folk, you say. The slynth, you say. HA..... HA HA HA! Yes! I never thought to see yet fresher thought-sprouts take seed here in Ezra, but our sun is theirs, and the sky below it, and the thickening air down to the ground. Bring them to hear the songs of our musa-herders, and hope that they survive.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, mayor.

### Node `SlynthRequestReject`

Rocky soil fits only so many roots, little walker. Perhaps if yours were more anchored here. HA.

### Node `SlynthAbout`

Tell me of your seedlings.

### Node `SlynthArrived`

It is the good wind that brought the slynth to Ezra.

        HA HA HA.

        I will watch as these seedlings wilt or thrive.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, Mayor.

### Node `SlynthSettled`

Returning so soon to check on our seedlings?

        HA. They grow, eat, sing, and joggle their curious little fingers at the salt sky. See for yourself.

**Choices:**
- **choice** `?` → `End`
    > My thanks again, Mayor.

### Node `Tree`

HA.......

        HA HA HA. So I am. I split stone and joggle my fingers at the salt sky. So I do today, so I did yesterday.

**Choices:**
- **choice** `HaddasOldChoice` → `Old`
    > How old are you?
- **choice** `MayorChoice` → `Mayor`
    > How did you become mayor of this village?
- **choice** `HaddasQuestionsChoice` → `Start`
    > I'd like to ask you something else.
- **choice** `?`

### Node `Old`

I tally so many autumns, but until I am black with rot, I cannot be ring-right. The etching on my undertrunk places my seed-date to the reign of =sultan:4=, so I am told.

**Choices:**
- **choice** `EaterChoice` → `Eater`
    > Technically, that makes you an Eater, doesn't it?
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Eater`

HA HA HA. I suppose so.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Mayor`

HA. I stood long enough. I joggled my fingers at the salt sky, and I watched thy seedlings sprout and wither, and I watched thou place stones in straight lines like the bees and their nests of wax. I stood until the stones were nigh by me. The people followed the stones.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Reliefs`

Ezra is more than tree-old. It's stone-old. Seedlings have lived here since our roots dreamed of joggling their fingers at the salt sky.

        They ate earth and belched freight at the stars, and this place was their stomach.

        Later, as the Star-Tree died and they buried their dead under its roots, this was their funerary place.

        Now, we nurse electric milk from the old and aching temple to turn our wheels and grind our seeds and grains. Now we are they.

**Choices:**
- **choice** `StarTreeChoice` → `StarTree`
    > Star-Tree?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `StarTree`

Aye, the Blue Mother who breaks the sky. Those who Eat called her Gjaus, and those who Wake call her Spindle.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Warden`

One called 1-FF, who wandered in errancy out from the Tomb and was reprogrammed by the Daughter who lived and died in the rot-black box, nine Daughters ago.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Merchants`

To the northwest seek the rot-black box. There a plant and Daughter live. There cats of chrome purr at tiny suns.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Work`

Ezra is old and has long since cut a groove into the world and resides there in stillness and harmony. But Zothom the Penitent One is a seedling, new to the world, and he quakes at all the tensing the world does. Perhaps you can share in his angst.

        Go find him by the headstones for the dead.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
