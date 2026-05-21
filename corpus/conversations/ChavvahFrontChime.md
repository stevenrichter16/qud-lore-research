# Conversation: `ChavvahFrontChime`

_Inherits: (default: BaseConversation)_

_1 start(s), 3 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

*The chiming rock burns in soft light.*

**Choices:**
- **choice** `?` → `What`
    > ...what are you?
- **choice** `?` → `Welcome`
    > [Touch the chiming rock and attune to Chavvah.]
    - _part: `ChavvahAttune` (FailTarget=AlreadyAttuned)_
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `What`

*The chiming rock rings a sonorous tone.*
				
				Touch the chiming rock and seek me at the keter. Will you?

**Choices:**
- **choice** `?` → `Mean`
    > What does that mean?

### Node `Mean`

*The chiming rock is silent and still.*

### Node `AlreadyAttuned`

*You are already attuned.*
