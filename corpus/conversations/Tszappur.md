# Conversation: `Tszappur`

_Inherits: (default: BaseConversation)_

_0 start(s), 3 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Peace and health in the light of the Star, pilgrim. Brood with me on the life of Resheph, if you are willing.

**Choices:**
- **choice** `SecretTszappur` → `Start`
    > I am.
    - _part: `GiveReshephSecret`_
- **choice** `ReshephTszappur` → `Resheph`
    > Who is Resheph?
- **choice** `InsideTszappur` → `Inside`
    > What's inside the tent?
- **choice** `?` → `End`
    > Live and drink, priest.

### Node `Resheph`

A spiritual patron of kith and kin, who did so much for us, and who leads me and others like me to the path of healing. For, above all, he was a healer. He dressed the wounds of the sick and rid the land of the plagues of the Gyre.

        He was also a sultan, but he was the last sultan. He unbricked the walls of monocracy so we could pick berries in the orchards they hid.

**Choices:**
- **choice** `?` → `Start`
    > I've more to ask.
- **choice** `?` → `End`
    > Live and drink, priest.

### Node `Inside`

A quiet shrine to the Coiled Lamb, centuries old. Tucked away here, outside the marble parapets and cloaked in the dust of time, it's lost to those who'd sneer at the veneration of Resheph over other fathers.

        Step inside and voice a prayer, if you are willing.

**Choices:**
- **choice** `?` → `Start`
    > I've more to ask.
- **choice** `?` → `End`
    > Live and drink, priest.
