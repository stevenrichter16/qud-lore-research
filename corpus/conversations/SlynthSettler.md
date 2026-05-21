# Conversation: `SlynthSettler`

_Inherits: (default: BaseConversation)_

_0 start(s), 2 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Is okay?~
        Ahh... nervous ... excited.~
        Happy do not fight here.~
        Ah ha ha... nervous!~
        Stay here?~
        =player.FormalAddressTerm= stay also?~
        Strange new.~
        Live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`LandingPadsSlynthSettled`_

This is home.~
        Welcome here.~
        Good meeting.~
        Ah... good.~
        We chose our new home well.~
        Happy here.~
        Ha ha ha! Joyful!~
        Ah =player.formalAddressTerm= visit, good.~
        Live and drink.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
