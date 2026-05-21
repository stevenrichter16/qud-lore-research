# Conversation: `TauNoLonger`

_Inherits: (default: BaseConversation)_

_2 start(s), 13 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Orphaned`  _IfTestState=`TauCompanion contains KilledByPlayer`_

You have severed the hand outstretched to me. Why?

        What have you done? What am I to do?

**Choices:**
- **choice** `?` → `Suborned`
    > Your will would have been suborned to Ptoh.
- **choice** `?` → `Uncaring`
    > That's not my problem.
- **choice** `?` → `Sorry`
    > I am sorry.
- **choice** `?` → `Happier`
    > You will be happier this way.

### Start `Welcome`

*Tau's crystal body yet rings softly from her separation from Taproot.*

        Again I perceive.

        Thank you, rootclimber. Chavvah's rewards are great and you are deserving of them.

**Choices:**
- **choice** `?` → `How`
    > How are you feeling?
- **choice** `?` → `Liaison`
    > It seems that someone is waiting for you.
- **choice** `?` → `Ptoh`
    > You would suborn your will to Ptoh?
- **choice** `?` → `EndGift`
    > Live and drink.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Suborned`

You suborn my will! You allow me to start upon this path and block it. Yes?

        Now I am truly adrift.

### Node `Uncaring`

Ah.

        Well. You have my thanks for your help in -elseing, but by blocking my path you create fresh problems. Yes?

        I do not wish to know you.

        Live and drink.

### Node `Sorry`

I resent what has befallen me, but I am yet embodied. You have still helped me live, yes?

        I forgive you, but I don't wish to know you. Live and drink.

### Node `Happier`

Perhaps. My future is hazy. My future twists in the chill wind of the Gyre. I can have no faith in your vision. You understand this, yes?

        I do not wish to know you.

        Live and drink.

### Node `How`

Present. Alone, afraid, but anticipating my return to the embrace of a collective.

### Node `Liaison`

More than someone. My liaison is the extended, outstretched hands of a greater mind-haven than I have otherwise known. I might not have had the courage to -else without knowing that a collective awaited me.

        My future is hazy, my future is bright.

### Node `Ptoh`

Speaking creatures seem very engrossed in this 'will' idea, but few agree what it is. Your mind is under influence from other thinkbeings the moment you observe them, yes? You 'learn' by imitating, your values and beliefs are adopted from observation. Yes?

        I have made a choice to offer my consciousness to a new paradigm, but this choice seems distinct from your conception of 'will'. We speak past one another.

**Choices:**
- **choice** `?` → `Hunt`
    > The Seekers of the Sightless Way hunt espers.
- **choice** `?` → `Favor`
    > May the Fates favor you, Tau-no-Longer.
- **choice** `?` → `FavorGift`
    > May the Fates favor you, Tau-no-Longer.
- **choice** `?` → `Leave`
    > I leave you to your fate, then.
- **choice** `?` → `LeaveGift`
    > I leave you to your fate, then.

### Node `Hunt`

Oh, yes? I see. Well.

        Do you... not hunt? Or align with hunters? You reek of predation yourself. You kill, yes?

        I recall no promise to become a grazing hedonist. If I am called to hunt I will hunt.

### Node `Favor`

I wish the same for you, =name=. Live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `FavorGift`

I wish the same for you, =name=.
				
				Before you go, take this, a piece of my bodystuff, as thanks for completing the -elseing.
				
				Then live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Leave`

As I you to yours, =name=. Live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `LeaveGift`

As I you to yours, =name=. 
				
				But before you go, take this, a piece of my bodystuff, as thanks for completing the -elseing.
				
				Then live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `EndGift`

Before you go, take this, a piece of my bodystuff, as thanks for completing the -elseing.

				Then live and drink, =name=.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
