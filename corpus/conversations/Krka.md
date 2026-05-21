# Conversation: `Krka`

_Inherits: (default: BaseConversation)_

_0 start(s), 9 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Live and =player.formalAddressTerm=!

        *self-conscious rkkk*

        Dr... drink and =player.formalAddressTerm=!

        Krka, me. Krka.

**Choices:**
- **choice** `KrkaChoice` → `Krka`
    > Krka?
- **choice** `SvardymChoice` → `Svardym`
    > Are you svardym?
- **choice** `ApothecaryChoice` → `Apothecary`
    > Why are you dressed like an apothecary?
- **choice** `FreeholdChoice` → `Freehold`
    > What do you think of the Freehold?
- **choice** `KrkaEndChoice` → `End`
    > Live and drink, Krka.

### Node `Krka`

*gweep!*

        Krka, me!

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Svardym`

Vardy! Yes.

        But. Gemtle? No kill.

**Choices:**
- **choice** `?` → `Svardym2`
    > Why aren't you aggressive too?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Svardym2`

Hatchling hungry. Angry. Angry-hungry.

        Kill, eat, don't eaten. Calm down evengefully.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Apothecary`

*chirp!*

        Poth carry!

**Choices:**
- **choice** `?` → `Apothecary2`
    > Yes, apothecary. Do you know what those are?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Apothecary2`

Krka poth!

        *affirmative rrk!*

        Eel woon a-banjage. Wikky wood, orsh room, jector! All sale, wants?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Freehold`

*several moments of softly creaking thought*

        G-good!

**Choices:**
- **choice** `?` → `Freehold2`
    > Just... good?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Freehold2`

V-very good?

        *deflates with a long reeeeeep.*

        Krka not very. Words.

**Choices:**
- **choice** `?` → `Freehold3`
    > It's all right. You seem to like it here.
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Freehold3`

*krka!*

        Yes! To like! But... never home else. So *reep?*.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
