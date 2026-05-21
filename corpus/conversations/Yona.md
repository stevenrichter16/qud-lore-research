# Conversation: `Yona`

_Inherits: (default: BaseConversation)_

_0 start(s), 11 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseDagasha`_

=factionaddress:Mopango|capitalize=, =ifplayerplural:ye have:thou hast= done a momentous thing.

        I feel the stored energy of Her Light. Dagasha shall shepherd us to our uplifting. =ifplayerplural:Ye should:Thou shouldst= be proud.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Yona. Live and drink.

### Node `Start`

Ah, =factionaddress:Mopango=, =ifplayerplural:ye are:thou'rt= a bittersweet sight. Would fain =ifplayerplural:ye had:thou hadst= chosen Dagasha, but my Light shineth elsewhere.

        Still, I hope to see more of =ifplayerplural:ye:thee= in my future. =ifplayerplural:Ye are:Thou'rt= welcome back, an =ifplayerplural:ye survive:thou surviveth=.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Yona.

### Node `Start`

What have we here? Approach, =player.formalAddressTerm=, and be known.

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

=name=. Greetings. I am called Yona. =ifplayerplural:Ye seem:Thou seemest= unlike most other climbers. I wonder why.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `WhyAreYouHere`

=ifplayerplural:Have ye:Hast thou= seen it, out there? The spiny, eel-like creature. That is Dagasha, angry one, lost child. =ifplayerplural:Ye can:Thou canst= feel the hostility pour from it in waves.

        Yet, it attacketh not.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `YourCredo`

Yes. "Anyone may strike a slumberling once."

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `Meaning`
    > What does that mean?
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Meaning`

Only a fool asketh after the meaning of a credo.

**Choices:**
- **choice** `?` → `Apologize`
    > I apologize for my rudeness.
- **choice** `?` → `End`
    > I am leaving.

### Node `Apologize`

I am not offended, simply making =ifplayerplural:ye:thee= aware of =ifplayerplural:your:thy= foolishness.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Device`

I am consumed by curiosity. How it resembleth the children in make!

        May I hold the device in communion?

**Choices:**
- **choice** `?` → `Commune`
    > You may.
- **choice** `?` → `Deny`
    > You may not.

### Node `Deny`

Ahh.

        Stranger, =ifplayerplural:ye are:thou art= cruel to withhold this experience, but I shall abide.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Commune`

*Yona gasps upon touching the repulsive device, and eir eyes go wide. Ey is silent and still for nearly a minute, until the repulsive device tumbles from eir claws and you catch it.*

        What was that? I need to know more. I know I cannot. Key to a lock of self? I feel great intellect and charisma bound up in Dagasha's prison-body, the mind of a leader, or a tyrant. Too much to know, too much unknown.

        =ifplayerplural:Your:Thy= will hath great weight, wanderer. =ifplayerplural:Will ye:Wilt thou= free Dagasha?

**Choices:**
- **choice** `?` → `End`
    > We'll see. Live and drink.
