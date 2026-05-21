# Conversation: `Dagasha`

_Inherits: (default: BaseConversation)_

_0 start(s), 6 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseDagasha`_

Take care, =factionaddress:Mopango=. Let not complacency end =ifplayerplural:ye:thee=, and I shall anticipate further news of =ifplayerplural:your:thy= exploits.

**Choices:**
- **choice** `?` → `End`
    > Live and lead, Dagasha.

### Node `Start`

*The jagged, serpentine entity stares you down, twitching with feigned half-strikes in your direction as if goading an aggressive response from you. Though it has no mouth, it is not silent: piercing the air is a strange, external tinnitus, the whine of an ancient viewscreen.*

**Choices:**
- **choice** `?` → `ConfirmRepairDagasha`
    > I offer you this repulsive device, unique one.
- **choice** `?` → `End`
    > Live and... do as you please.

### Node `ConfirmRepairDagasha`

*Dagasha tilts its head, staring you down. It twitches, but makes no move to strike as you approach.*

**Choices:**
- **choice** `?` → `RepairDagasha`
    > Here. Take it.
- **choice** `?` → `End`
    > I am not yet ready. I may return.

### Node `RepairDagasha`

*You offer the repulsive device. As it nears the shining, dark surface of Dagasha's serpentine body, a sudden fervor seizes the device, and it twists itself free, latching onto the entity with the hooked teeth of its mouthlike appendage. Dagasha rears back at once, its serpentine body twisting into thorny knots.*

        *For a time, it is still. Then it uncoils, slowly, and whispers:*

        I... am mine. Once again I am mine.

**Choices:**
- **choice** `?` → `DagashaResponds`
    > Are you all right?

### Node `DagashaResponds`

Though I be a pale shadow of the self I once was, yes. My condition and outlook are both substantially improved.

        I recall few details of my life before. I was influential, one whose words stirred hearts to action. For so long I had no means to speak, trapped in my own moods. =ifplayerplural:Ye have:Thou hast= freed me from a dire fate.

**Choices:**
- **choice** `?` → `DagashaFuture`
    > What will you do now?

### Node `DagashaFuture`

I know not. Perhaps I can lead again. These creatures that looked after me, named me, kept me safe. The mopango.

        They are kind, but weak. Perhaps I can teach them. Spur them to be greater.

        But for =ifplayerplural:ye:thee=, I must even our score. Take this piece of my chassis. Wear it with confidence. Command in my name.

**Choices:**
- **choice** `?` → `End`
    > Live and remain free, Dagasha.
- **choice** `?` → `End`
    > Live and remain free, Dagasha.
