# Conversation: `DynamicVillageMayor`

_Inherits: `BaseSlynthMayor`_

_1 start(s), 6 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

Welcome to the village of *villageName*, =spice.commonPhrases.adventurer.!random=

## Nodes

### Node `SlynthRequest`

Is that so? I imagine you are wondering whether =village.name= will host these slynth, to partake in =village.activity= alongside us.

### Node `SlynthRequestAccept`

You have done much for =village.name=, =name=, and your request befits your stature. If these slynth will join us in =village.activity= and if they can come to cherish =village.sacred= as we do, then they are welcome here.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, friend.

### Node `SlynthRequestReject`

We have not come so far from the founding of =village.name= to allow these strangers in. What if they worship =village.profane=? No, we simply cannot do such a great favor for you.

### Node `SlynthAbout`

Do you have news of the slynth?

### Node `SlynthArrived`

Ah, =name=, the slynth are here, and it is a slow process for these plant-folk and the people of =village.name= to grow accustomed to one another. By the goodness of =village.sacred= may the slynth find their place here soon.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, =subject.t=.

### Node `SlynthSettled`

Praise =village.sacred=, the slynth learn our ways and we theirs. Some do not wholly accept the depravity of =village.profane=, but their ways are born of kindness, and so =village.name= will be kind in kind.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, =subject.t=.
