# Conversation: `Gritgate Intercom`

_Inherits: (none — explicit empty, suppresses default)_

_0 start(s), 9 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

[Voice transmitting through panel]

        Be gone, wayfarer. This is no place for you.

**Choices:**
- **choice** `?` → `TradeEntrance`
    > I come by way of Joppa. The elder Irudad calls me friend.
- **choice** `?` → `GiveDisk`
    > Wait! My name is =name=. I've come into possession of a data disk stamped with a peculiar sigil. Does this have meaning to your order of tinkers? Might you examine it?
- **choice** `?` → `GiveDisk`
    > Wait! My name is =name=. I've come into possession of a data disk stamped with a peculiar sigil. Does this have meaning to your order of tinkers? Might you examine it?
- **choice** `?` → `TradeEntrance`
    > I am a merchant, cave dweller. I wish only to trade.
- **choice** `?` → `GiveDisk`
    > Wait! My name is =name=. I bring a message from Argyve of Joppa.
- **choice** `?` → `GiveDisk`
    > Wait! My name is =name=. The people of =villageZeroName= recently came into possession of a data disk, onto which a strange signal was recorded. At their behest I carry the disk with me. They say your tutelage is to be my reward.
- **choice** `?` → `End`
    > ...

### Node `GiveDisk`

[A slot opens from the center of the door and a metal tray slides out]

**Choices:**
- **choice** `?` → `GaveDiskFromVillage`
    > [Place stamped disk in tray]
- **choice** `?` → `GaveDiskSolo`
    > [Place scratched disk in tray]
- **choice** `?` → `GaveDisk`
    > [Place disk in tray]
- **choice** `?` → `End`
    > Uh, I'll come back later with it.

### Node `GaveDiskFromVillage`

[several minutes pass]

        So you wish to study with us. Unfortunately, we require more than a willing spirit.

        Qud is not =villageZeroName=. You will need to prove your worth, that you might not waste our time and efforts. Travel to the great cavern Golgotha to the north. Within its halls you will find a cache of dysfunctional waydroids.

        Recover one, repair it, and return here. If we are satisfied with your work, you will be admitted to our order. Otherwise, you will not be.

        Do you accept this arrangement?

**Choices:**
- **choice** `?` → `End`
    > Yes.
- **choice** `?` → `End`
    > No, I'm not interested.

### Node `GaveDiskSolo`

[several minutes pass]

        The disk you bring is encoded with an important signal. To discuss it further, we must admit you to our order. Unfortunately, we require more than a willing spirit.

        You will need to prove your worth, that you might not waste our time and efforts. Travel to the great cavern Golgotha to the north. Within its halls you will find a cache of dysfunctional waydroids.

        Recover one, repair it, and return here. If we are satisfied with your work, you will be admitted as an apprentice. Otherwise, you will be turned away.

        Do you accept this arrangement?

**Choices:**
- **choice** `?` → `End`
    > Yes.
- **choice** `?` → `End`
    > No, I'm not interested.

### Node `GaveDisk`

[several minutes pass]

        So it seems that you are indeed Argyve's apprentice. He wishes you to study with us. Unfortunately, we require more than a willing spirit.

        Qud is not Joppa. You will need to prove your worth, that you might not waste our time and efforts. Travel to the great cavern Golgotha to the north. Within its halls you will find a cache of dysfunctional waydroids.

        Recover one, repair it, and return here. If we are satisfied with your work, you will be admitted to our order. Otherwise, you will not be.

        Do you accept this arrangement?

**Choices:**
- **choice** `?` → `End`
    > Yes.
- **choice** `?` → `End`
    > No, I'm not interested.

### Node `Start`

Have you completed the task?

**Choices:**
- **choice** `?` → `RepairedWaydroid`
    > Yes.
- **choice** `?` → `TradeEntrance`
    > Not yet. But I require entrance to the city for the purposes of trade.
- **choice** `?` → `End`
    > ...

### Node `Start`

Welcome, wayfarer.

**Choices:**
- **choice** `?` → `TradeEntrance`
    > I require entrance to the city.

### Node `TradeEntrance`

Enter then, traveler.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
    - _part: `GritGateHandler` (Door=0)_

### Node `RepairedWaydroid`

[The slot opens from the center of the door. A bright red light shines through.]

        [Several minutes pass.]

        You may enter. Simply walk through the force barrier. Make your first two lefts and speak to Steward Otho in his office.

**Choices:**
- **choice** `?` → `End`
    > ...
    - _part: `GritGateHandler` (Door=1)_
