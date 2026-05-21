# Conversation: `Indrix`

_Inherits: (default: BaseConversation)_

_0 start(s), 13 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Impudent swine! You would bear that stygian charm in my presence?

**Choices:**
- **choice** `?` → `End`
    > !
    - _part: `StartFight`_

### Node `Start`

Make haste, traveller.

**Choices:**
- **choice** `?` → `PariahA`
    > Why are you called "pariah"?
- **choice** `?` → `Raising1`
    > I am in search of work.
- **choice** `?` → `End`
    > Live and drink, warden.

### Node `Start`

Is Mamon dead? Have you recovered the talisman?

**Choices:**
- **choice** `?` → `HasPrism`
    > Yes. Mamon is dead and I possess the prism.
- **choice** `?` → `River`
    > Where will I find him again?
- **choice** `?` → `End`
    > Not yet.

### Node `Start`

Live and drink, traveler.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, warden.

### Node `PariahA`

Speak nothing of that name to me. You are warned.

**Choices:**
- **choice** `?` → `Pariah2`
    > I must insist; why are you called "pariah"?
- **choice** `?` → `Raising1`
    > I am in search of work.
- **choice** `?` → `End`
    > Live and drink, warden.

### Node `PariahB`

Speak nothing of that name to me. You are warned.

**Choices:**
- **choice** `?` → `Pariah2`
    > I must insist; why are you called "pariah"?
- **choice** `?` → `End`
    > Live and drink, warden.

### Node `Pariah2`

I will ravage your nubile heart!

**Choices:**
- **choice** `?` → `End`
    > !
    - _part: `StartFight`_

### Node `Raising1`

Grrrraaaah! There is but one task I know to offer. It is most treacherous, and in all likelihood you will perish. Is your interest waned?

**Choices:**
- **choice** `?` → `Raising2`
    > No. Continue.
- **choice** `?` → `End`
    > Yes. Goodbye.

### Node `Raising2`

There is a river just south of the village that runs an eastwardly course into the jungle. Along its bank lies a goatfolk village. There resides a mighty shaman, Mamon Souldrinker. He is in possession of a talisman of great power, an amaranthine prism that refracts the psyche of its handler in much the same way, as Mayor Nuntu has explained to me, a common prism refracts light. The thing is cursed, traveler. No man or goat may safely wield it for long. You must travel to the village and retrieve the prism from Mamon by any means necessary. Do you understand?

**Choices:**
- **choice** `?` → `Raising3a`
    > Why don't you retrieve it yourself?
- **choice** `?` → `Raising3b`
    > Yes. Is there anything else I should know?

### Node `Raising3a`

Because, traveler, Mamon is my elder brother. He would discern my presence before I could strike.

**Choices:**
- **choice** `?` → `Raising3b`
    > Is there anything else I should know?

### Node `Raising3b`

There is. Firstly, Mamon will likely have several goatfolk under his enthrallment, and they will protect him at all costs.

        Secondly, take care to stay out of Mamon's reach, for his power is most potent when he may lay hands on you.

        Finally, once you recover the prism, do not under any circumstances wield it. I needn't warn you of the consequences should you return to me bearing that charm.

        That is all. Are you willing?

**Choices:**
- **choice** `?` → `End`
    > I am willing.
- **choice** `?` → `End`
    > No, I would risk too much.

### Node `River`

Just south of the village, there's a river that runs an eastwardly course into the jungle. Follow it to the goatfolk village. There you will find Mamon.

**Choices:**
- **choice** `?` → `End`
    > My thanks, warden.

### Node `HasPrism`

Is it so? Only a ferocious warrior could have slain Mamon. You must be such a warrior. Now hand over the prism and choose your reward.

**Choices:**
- **choice** `?` → `End`
    > [Give the amaranthine prism to Warden Indrix]
    - _part: `ReceiveItem` (Mods=1 Pick=true Table=RaisingIndrix_Rewards Identify=All)_
    - _part: `QuestHandler` (QuestID=Raising Indrix Action=Complete)_
- **choice** `?` → `End`
    > No, warden. It is mine.
    - _part: `StartFight`_
