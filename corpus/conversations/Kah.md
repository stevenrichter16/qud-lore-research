# Conversation: `Kah`

_Inherits: (default: BaseConversation)_

_0 start(s), 6 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseKah`_

=ifplayerplural:May ye:Mayst thou= loose the bonds that keep =ifplayerplural:ye:thee= from =ifplayerplural:your:thy= goals, =factionaddress:Mopango=. Be free.

**Choices:**
- **choice** `?` → `End`
    > Live and be free, Kah.

### Node `Start`

*The creature-silhouette lacks any means to make sound, save for the pointed tips of its six flexible legs. These tap against the ground like a sparse but heavy rainfall on a scrap metal roof as the strange pseudo-beast skitters away from predicted or perceived threats.*

**Choices:**
- **choice** `?` → `ConfirmRepairKah`
    > I offer you this repulsive device, unique one.
- **choice** `?` → `End`
    > Live and... do as you please.

### Node `ConfirmRepairKah`

*Kah skitters away, but soon returns, and skitters away a shorter distance. Whether because of your words or because you are still, its desire for flight ebbs over the course of a minute until its escape attempts halt.*

**Choices:**
- **choice** `?` → `RepairKah`
    > Here. Take it.
- **choice** `?` → `End`
    > I am not yet ready. I may return.

### Node `RepairKah`

*You offer the repulsive device. As it nears the shining, dark surface of Kah's hide, a sudden fervor seizes the device, and it twists itself free, latching onto the entity with the hooked teeth of its mouthlike appendage. Kah scrabbles to escape again, but its limbs twist and collapse, rubbery and useless. Kah flails for a few moments before going completely limp*

        *For a time, it is still. When it once again moves to clamber to the points of its shaky legs, Kah speaks in a smooth, buzzing voice:*

        I feel... calm.

**Choices:**
- **choice** `?` → `KahResponds`
    > Are you all right?

### Node `KahResponds`

I am weary to my core, but at last this once-hateful body obeyeth me. I thank =ifplayerplural:ye:thee= for restoring my autonomy.

        Memory of my once-self doth elude me, but I recognize the irony of my punishment. Once a strider, then sentenced to stride without restraint, forever. I knew only fear and flight. No more.

**Choices:**
- **choice** `?` → `KahFuture`
    > What will you do now?

### Node `KahFuture`

I shall enjoy my free mobility freely, for a time. After that, I know not. I may speak to these mopango creatures that named me, and find a purpose with them. I cannot ever repay their care, but perhaps I may repay =ifplayerplural:yours:thine=.

        I wouldst fain offer =ifplayerplural:ye:thee= a fragment of this form come loose. =ifplayerplural:May ye:Mayst thou= ever run free.

**Choices:**
- **choice** `?` → `End`
    > Live and remain free, Kah.
- **choice** `?` → `End`
    > Live and remain free, Kah.
