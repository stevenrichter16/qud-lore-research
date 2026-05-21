# Conversation: `GenericAskNameOption`

_Inherits: (default: BaseConversation)_

_0 start(s), 2 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

**Choices:**
- **choice** `?` → `*askname`
    > What is your name?~What is your name, =pronouns.formalAddressTerm=?~What may I call you, =pronouns.formalAddressTerm=?~What are you called, =pronouns.formalAddressTerm=?~I am =name=, =pronouns.formalAddressTerm=. What is your name?~I am =name=, =pronouns.formalAddressTerm=. What may I call you?

### Node `TellName`

You may call me =subject.refname=.~
        My name is =subject.refname=.~
        I am called =subject.refname=.~
        They call me =subject.refname=.

**Choices:**
- **choice** `?` → `Start`
    > Thank you, =pronouns.formalAddressTerm=.~My thanks, =pronouns.formalAddressTerm=.~Pleased to meet you, =pronouns.formalAddressTerm=.
