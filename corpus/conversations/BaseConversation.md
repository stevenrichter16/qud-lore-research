# Conversation: `BaseConversation`

_Inherits: (default: BaseConversation)_

_0 start(s), 1 node(s), 1 root-level choice(s)_

---

## Conversation-level choices

- **choice** `AskName` → `TellName`
    > What is your name?
    > What is your name, =pronouns.formalAddressTerm=?
    > What may I call you, =pronouns.formalAddressTerm=?
    > What are you called, =pronouns.formalAddressTerm=?
    > I am =name=, =pronouns.formalAddressTerm=. What is your name?
    > I am =name=, =pronouns.formalAddressTerm=. What may I call you?
    - _part: `AskName`_

## Nodes

### Node `TellName`

You may call me =subject.refname=.

My name is =subject.refname=.

I am called =subject.refname=.

They call me =subject.refname=.

**Choices:**
- **choice** `?` → `Start`
    > Thank you, =pronouns.formalAddressTerm=.
    > My thanks, =pronouns.formalAddressTerm=.
    > Pleased to meet you, =pronouns.formalAddressTerm=.
