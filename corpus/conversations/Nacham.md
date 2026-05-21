# Conversation: `Nacham`

_Inherits: (default: BaseConversation)_

_0 start(s), 6 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseNacham`_

Learn well, =factionaddress:Mopango=. I would fain see =ifplayerplural:ye:thee= succeed in =ifplayerplural:your:thine= task.

**Choices:**
- **choice** `?` → `End`
    > Live and learn, Nacham.

### Node `Start`

*Every surface of the strange entity vibrates with the sound of a hundred dry lectures by long-dead scholars, teaching a volume of knowledge so dense and overlapping that the end result is incomprehensible.*

**Choices:**
- **choice** `?` → `ConfirmRepairNacham`
    > I offer you this repulsive device, unique one.
- **choice** `?` → `End`
    > Live and... do as you please.

### Node `ConfirmRepairNacham`

*Swimming in sound, Nacham stares at you and looks away simultaneously, giving no indication of understanding.*

**Choices:**
- **choice** `?` → `RepairNacham`
    > Here. Take it.
- **choice** `?` → `End`
    > I am not yet ready. I may return.

### Node `RepairNacham`

*You offer the repulsive device. As it nears the shining, dark surface of Nacham's shell, a sudden fervor seizes the device, and it twists itself free, latching onto the entity with the hooked teeth of its mouthlike appendage. Nacham reacts with a violent spasm, cable-limbs flailing as the entity staggers back.*

        *For a time, Nacham is still, but then it speaks, a chorus of voices finally speaking in unison:*

        It ceases. At last it ceases.

**Choices:**
- **choice** `?` → `NachamResponds`
    > Are you all right?

### Node `NachamResponds`

Yes. =ifplayerplural:Ye have:Thou hast= quelled the mania.

        I can focus. I can render sensible the things I have seen and heard now, though I remember little of my time before the mania. Was I artisan? Teacher? I possessed great knowledge that this shell twisted into a prison. I thank =ifplayerplural:ye:thee= for the gift of =ifplayerplural:your:thy= untwisting.

**Choices:**
- **choice** `?` → `NachamFuture`
    > What will you do now?

### Node `NachamFuture`

The mopango have cared for me whilst I could not care for myself, giving me the only name I now know. I will stay to help them. This chassis is a prison no longer, and perhaps deeper truths may yet be found within it.

        To =ifplayerplural:ye:thee=, new friend, I offer a piece of this former prison that =ifplayerplural:ye may:thou mayest= find useful, along with my thanks.

**Choices:**
- **choice** `?` → `End`
    > Live and remain free, Nacham.
- **choice** `?` → `End`
    > Live and remain free, Nacham.
