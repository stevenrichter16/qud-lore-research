# Conversation: `Lebah`

_Inherits: (default: BaseConversation)_

_0 start(s), 17 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

*The little watcher stares at you.*

**Choices:**
- **choice** `?` → `LebahHides`
    > Look, Lebah. I have recovered the repulsive device.
- **choice** `?` → `HelloLebah`
    > Hello?
- **choice** `?` → `End`
    > Live and drink, quiet one.

### Node `HelloLebah`

... aye.

**Choices:**
- **choice** `?` → `LebahQuest`
    > Agyra tells me you found some kind of repulsive device.
- **choice** `?` → `LebahReminder`
    > Where is the repulsive device, again?
- **choice** `?` → `Freed`
    > I have freed one of the children.
- **choice** `?` → `LebahGreet`
    > I am =name=. What is your name?
- **choice** `?` → `LebahCredo`
    > What is your credo?
- **choice** `?` → `End`
    > Live and drink, quiet one.

### Node `Freed`

Ah.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
- **choice** `?` → `Indignant`
    > That's all you have to say?

### Node `Indignant`

Yes?

**Choices:**
- **choice** `?` → `CheckinOut`
    > I barely survived and all you can say is 'ah' and 'yes'?
- **choice** `?` → `End`
    > Fair enough. Live and drink.

### Node `CheckinOut`

*Lebah curls into an armored ball and stops responding to your questions.*

**Choices:**
- **choice** `?` → `LebahPoke`
    > Lebah, do not ignore me.
- **choice** `?` → `End`
    > Fine. Live and drink.

### Node `LebahGreet`

Lebah.

**Choices:**
- **choice** `?` → `LebahCredo`
    > What is your credo?
- **choice** `?` → `End`
    > Live and drink, Lebah.

### Node `LebahCredo`

"An thou art swallowed by the Gyre, sing thee to the last."

**Choices:**
- **choice** `?` → `LebahMeaning`
    > What does that mean?
- **choice** `?` → `LebahGreet`
    > What is your name?
- **choice** `?` → `End`
    > Live and drink.

### Node `LebahMeaning`

The meaning is plain: An =ifplayerplural:ye are:thou'rt= swallowed by the Gyre, =ifplayerplural:ye should:thou shouldst= sing to the last.

**Choices:**
- **choice** `?` → `LebahStare`
    > I don't understand.
- **choice** `?` → `LebahStare`
    > Can you explain further?
- **choice** `?` → `LebahStare`
    > That was not so much an explanation as it was a rephrasing.
- **choice** `?` → `End`
    > I... see. Live and drink.

### Node `LebahStare`

*Lebah stares at you wordlessly.*

**Choices:**
- **choice** `?` → `End`
    > I should go.

### Node `LebahQuest`

Ah,

        aye.

        a most repulsive device. The mind-echoes of that communion yet haunteth me.

**Choices:**
- **choice** `?` → `Repulsive`
    > What was so bad about the device?
- **choice** `?` → `End`
    > I will trouble you no further, then.

### Node `Repulsive`

Not... the device. Repulsive as a key to a prison doth repulse. To know a key is to know of a prison.

        Our watched children are bound, and lock swalloweth key. An =ifplayerplural:ye free:thou freest= one, three remaineth forever.

        k-Goninon hath it now. An =ifplayerplural:ye seek:thou seekest=.

**Choices:**
- **choice** `?` → `LebahHides`
    > Oh, do you mean this thing?
- **choice** `?` → `Curl`
    > I will seek to retrieve it, then.
- **choice** `?` → `OozeThat`
    > Who or what is k-Goninon?

### Node `OozeThat`

An elder ooze. My communion so disturbed me that I allowed them too close.

        k-Goninon consumed the device, but I escaped.

**Choices:**
- **choice** `?` → `Curl`
    > I will seek to retrieve it, then.
- **choice** `?` → `WhatsGoninon`
    > Tell me more about k-Goninon.

### Node `WhatsGoninon`

I concern myself little with oozes but to stay away.

        Please, no more. I tire. Talk to Agyra.

**Choices:**
- **choice** `?` → `Curl`
    > I thank you.

### Node `LebahReminder`

k-Goninon hath it.

        Ask Agyra.

**Choices:**
- **choice** `?` → `Curl`
    > Of course. k-Goninon.

### Node `Curl`

*Lebah nods to you, slowly curls into an armored ball, and speaks no further*

**Choices:**
- **choice** `?` → `End`
    > Live and drink, little seer.

### Node `LebahHides`

*Lebah yelps at the sight of the device, curling into an armored ball.*

**Choices:**
- **choice** `?` → `LebahPoke`
    > Lebah?
- **choice** `?` → `End`
    > Maybe I'll take this somewhere else.

### Node `LebahPoke`

*you receive no reply*

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
