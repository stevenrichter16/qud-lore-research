# Conversation: `Gyamyo`

_Inherits: (default: BaseConversation)_

_0 start(s), 11 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseKah`_

I hope =ifplayerplural:ye are:thou art= confident in =ifplayerplural:your:thy= choice, =factionaddress:Mopango=. I am happy with it, to be sure.

        Kah is free. It heals my heart to see it at rest. =ifplayerplural:Ye have:Thou hast= my thanks.

**Choices:**
- **choice** `?` → `End`
    > You're welcome, Gyamyo. Live and drink.

### Node `Start`

=ifplayerplural:Did ye:Didst thou= truly free one of the children? I see =ifplayerplural:ye did:thou didst=. Congratulations.

        Wouldst fain see Kah free, one day. I shall have to live a while and find a way.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, Gyamyo.

### Node `Start`

=factionaddress:Mopango|capitalize=, welcome. =ifplayerplural:Ye have:Thou hast= done well to survive so long in this peculiar place.

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

My name is Gyamyo. I am pleased to meet =ifplayerplural:ye:thee=, =name=. =ifplayerplural:Have ye:Hast thou= spoken to the other watchers? How fare they?

        Well, I hope.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `WhyAreYouHere`

I have volunteered to monitor an ancient machine-creature called Kah. Perhaps =ifplayerplural:ye have:thou hast= seen it, skipping hither and yon on strange limbs.

        Often I wonder if Kah knoweth aught else but fear.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `YourCredo`

I do, and I thank =ifplayerplural:ye:thee= for asking after it.

        My credo is "Reconciliation without understanding is a salt poultice."

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `Meaning`
    > What does that mean?
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Meaning`

Oh dear.

        This is the credo by which I live my life, and =ifplayerplural:ye ask:thou asketh= "what does that mean?"

        I cannot summarize such a thing for =ifplayerplural:ye:thee=. It is too great, too multifaceted.

**Choices:**
- **choice** `?` → `Apologize`
    > I apologize for my rudeness.
- **choice** `?` → `End`
    > I am leaving.

### Node `Apologize`

May the future bear out =ifplayerplural:your:thy= promises.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Device`

=ifplayerplural:Ye have:Thou hast= an object of great interest.

        An =ifplayerplural:ye would:thou wouldst= allow, I'd fain commune with it.

**Choices:**
- **choice** `?` → `Commune`
    > I wouldst.
- **choice** `?` → `Deny`
    > I wouldstn't.

### Node `Deny`

Hm. I wonder at =ifplayerplural:your:thy= decision.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, watcher.

### Node `Commune`

*Gyamyo moves little during communion, but shivers and twitches from time to time. After a minute or so, ey returns the device to you.*

        I am shaken. No doubt my journey wast shallow compared to Lebah's dive. But now, by my troth I say: Kah hath ever been a being of motion. Swift, kinetic, and elegant. No doubt 'twould be so if freed by yon device.

**Choices:**
- **choice** `?` → `End`
    > We'll see. Live and drink.
