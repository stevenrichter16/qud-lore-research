# Conversation: `Doyoba`

_Inherits: (default: BaseConversation)_

_0 start(s), 11 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseNacham`_

I'm so excited.

        Many thanks for releasing Nacham, =factionaddress:Mopango=. I believe that its presence here will provide a great mutual boon.

**Choices:**
- **choice** `?` → `End`
    > You're welcome. Live and drink.

### Node `Start`

=factionaddress:Mopango|capitalize=, I hear that =ifplayerplural:ye have:thou hast= freed one of the children! I cannot wait to speak to it, but for now I must observe Nacham to see if this event hath affected it. =ifplayerplural:Ye are:Thou art= welcome to watch too.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Doyoba.

### Node `Start`

Welcome, =factionaddress:Mopango=. Live and drink. =ifplayerplural:Need ye:Needest thou= a place to rest and sup? =ifplayerplural:Would ye:Wouldst= trade?

**Choices:**
- **choice** `?` → `Device`
    > I seek a use for this repulsive device.
- **choice** `Who` → `WhoAreYou`
    > I am =name=. Who are you?
- **choice** `Why` → `WhyAreYouHere`
    > Why are you here?
- **choice** `Credo` → `YourCredo`
    > Have you a credo?
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `WhoAreYou`

I am Doyoba, proud watcher of the children of the tomb. One child in particular. Of course =ifplayerplural:ye:thou= must comprehend, 'child' is but a fabricated epithet, as they are far older than we. The children are, that is.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `WhyAreYouHere`

We mopango watch the past, each of us a different facet. My charge is named Nacham, that which watcheth and understandeth not, that which speaketh and cannot be understood. Information floweth through Nacham as water through a sieve, mixed together beyond ken.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `YourCredo`

I do.

        "Suffering breedeth in still water."

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `Meaning`
    > What does that mean?
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Meaning`

...?

        =ifplayerplural:Ye ask:Thou askest= after the meaning of my credo. Wouldst I shall chew =ifplayerplural:your:thy= food for =ifplayerplural:ye:thee= as well?

**Choices:**
- **choice** `?` → `Apologize`
    > I apologize for my rudeness.
- **choice** `?` → `End`
    > I am leaving.

### Node `Apologize`

No, no, =ifplayerplural:ye know:thou knowest= not our ways and I was too harsh. I apologize, and I am not wroth with =ifplayerplural:ye:thee=.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Device`

By Her Light, it's ghastly. May I touch it?

**Choices:**
- **choice** `?` → `Commune`
    > You may.
- **choice** `?` → `Deny`
    > You may not.

### Node `Deny`

Oh.

        Well then, I suppose I have no insight for =ifplayerplural:ye:thee=.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Commune`

*Doyoba's face scrunches in pain as ey communes with the device, before finally pushing it back into your grasp*

        By her light, that was unpleasant. How it twisted and turned, leading me to visions of Nacham's past, scraps and flashes. I can discern only glimpses of significance. Once a creator, an innovator. Can these parts of itself return intact, under the device's influence? An thou sendest void away, hast thou lost a part of thee?

**Choices:**
- **choice** `?` → `End`
    > Perhaps we will find out. Live and drink.
