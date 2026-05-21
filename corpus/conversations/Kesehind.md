# Conversation: `Kesehind`

_Inherits: (default: BaseConversation)_

_0 start(s), 5 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Why are you talking to me?

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

No sudden moves around the Hindriarch, kendren. I am watching you.

**Choices:**
- **choice** `?` → `Who are you?`
    > Who are you?
- **choice** `?` → `ShowSonnet`
    > Does this poem belong to you?
- **choice** `?` → `End`
    > Live and drink.

### Node `ShowSonnet`

Do I look like a poet to you, kendren?

**Choices:**
- **choice** `?` → `End`
    > I suppose not. Live and drink.

### Node `Who are you?`

I am Kesehind, protector of Hindriarch Keh, the Grand-Doe of Bey Lah.

**Choices:**
- **choice** `?` → `Questions`
    > May I ask you some questions?
- **choice** `?` → `End`
    > I see. Live and drink.

### Node `Questions`

You may not.

**Choices:**
- **choice** `?` → `End`
    > Oh.
