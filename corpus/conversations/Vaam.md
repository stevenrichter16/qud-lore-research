# Conversation: `Vaam`

_Inherits: (default: BaseConversation)_

_0 start(s), 6 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseVaam`_

Stay safe.

**Choices:**
- **choice** `?` → `End`
    > Live and remain stalwart, Va'am.

### Node `Start`

*The hardened shell-thing traces a path around you slowly, its strange brush-feet scrabbling at the floor, a pace unaffected by your presence and movement. Behind the hissing of those feet on the ground is the strains of a faint voice, someone speaking from inside a distant cave. Audible, but not understandable.*

**Choices:**
- **choice** `?` → `ConfirmRepairVaam`
    > I offer you this repulsive device, unique one.
- **choice** `?` → `End`
    > Live and... do as you please.

### Node `ConfirmRepairVaam`

*Vaam seems oblivious to your words, but does slow its patrol as it nears you.*

**Choices:**
- **choice** `?` → `RepairVaam`
    > Here. Take it.
- **choice** `?` → `End`
    > I am not yet ready. I may return.

### Node `RepairVaam`

*You offer the repulsive device. As it nears the shining, dark surface of Va'am's thick carapace, a sudden fervor seizes the device, and it twists itself free, latching onto the entity with the hooked teeth of its mouthlike appendage. Va'am shudders with such violence that its plates rattle against one another, and the light behind its faceplate dims.*

        *For a time, it is still, its eye dark. Then a quiet but clear voice vibrates through the armored body:*

        Ah.

**Choices:**
- **choice** `?` → `VaamResponds`
    > Are you all right?

### Node `VaamResponds`

Yes. I thank =ifplayerplural:ye:thee=.

        =ifplayerplural:Ye have:Thou hast= freed me from a deep stupor. Once I was a protector, before being sentenced to protect nothing and no one.

        I remember little of that time.

**Choices:**
- **choice** `?` → `VaamFuture`
    > What will you do now?

### Node `VaamFuture`

I have yet to find my purpose. I can think and speak, and so this shell is nearly comfortable.

        One piece, however, doth yet chafe me. =ifplayerplural:Would ye:Wouldst thou= take it? Perhaps =ifplayerplural:ye can:thou canst= grant it some use.

**Choices:**
- **choice** `?` → `End`
    > Live and remain free, Va'am.
- **choice** `?` → `End`
    > Live and remain free, Va'am.
