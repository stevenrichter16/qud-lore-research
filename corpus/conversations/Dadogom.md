# Conversation: `Dadogom`

_Inherits: (default: BaseConversation)_

_0 start(s), 11 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseVaam`_

Va'am is released. =ifplayerplural:Ye have:Thou hast= done something great, for good or ill.

        I thank =ifplayerplural:ye:thee= for this new future.

**Choices:**
- **choice** `?` → `End`
    > You're welcome. Live and drink.

### Node `Start`

=factionaddress:Mopango|capitalize=. =ifplayerplural:Ye did:Thou didst= rouse a child. Well done.

**Choices:**
- **choice** `?` → `End`
    > Thank you. Live and drink, Dadogom.

### Node `Start`

Live and drink.

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

I am Dadogom.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `WhyAreYouHere`

I watch over Va'am. It watcheth over me. Together, we watch.

        =ifplayerplural:Ye should:Thou shouldst= as well, =factionaddress:Mopango=. Sit. Watch. Consider how =ifplayerplural:ye would:thou wouldst= fare under a dome of adamant carapace.

        Safe, undying, alone.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `YourCredo`

"Be still and know."

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `Meaning`
    > What does that mean?
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Meaning`

I cannot think on =ifplayerplural:your:thy= behalf.

**Choices:**
- **choice** `?` → `Apologize`
    > I apologize for my rudeness.
- **choice** `?` → `End`
    > Very well.

### Node `Apologize`

Consider =ifplayerplural:your:thy= words ere =ifplayerplural:ye say:thou sayest= them, and =ifplayerplural:ye will:thou wilt= issue fewer apologies.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Device`

Ah. May I?

**Choices:**
- **choice** `?` → `Commune`
    > You may.
- **choice** `?` → `Deny`
    > You may not.

### Node `Deny`

Ah, pity.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Commune`

*Dadogom is still for a while, and you can see no expression on eir face. At last, ey returns the device.*

        Unique. Puzzling, but clear. Painfully illuminating.

        Grant this to Va'am and it shall become as 'twere once: still stalwart, but confined to a crawl no longer. At least, so I believe. Communion and certainty share no blood.

**Choices:**
- **choice** `?` → `End`
    > Perhaps we will find out. Live and drink.
