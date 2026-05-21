# Conversation: `BaseSlynthMayor`

_Inherits: (default: BaseConversation)_

_0 start(s), 6 node(s), 4 root-level choice(s)_

---

## Conversation-level choices

- **choice** `?` → `SlynthRequest`
    > In my travels I encountered a people, the slynth, seeking a new home.
- **choice** `?` → `SlynthAbout`
    > About the slynth...
- **choice** `?` → `SlynthArrived`
    > I see the slynth have arrived. How are they faring?
- **choice** `?` → `SlynthSettled`
    > It's been a week. Are the slynth settled in?

## Nodes

### Node `SlynthRequestAccept`

BASE SLYNTH REQUEST ACCEPT TEXT

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, friend.
    - _part: `AddSlynthCandidate`_
- **choice** `?` → `Start`
    > I want to ask something else.

### Node `SlynthRequestReject`

BASE SLYNTH REQUEST REJECT TEXT

**Choices:**
- **choice** `?` → `Start`
    > I understand.

### Node `SlynthRequest`

BASE SLYNTH REQUEST TEXT

**Choices:**
- **choice** `?` → `SlynthRequestAccept`
    > I am.
- **choice** `?` → `SlynthRequestReject`
    > If you would have them, yes.

### Node `SlynthAbout`

BASE SLYNTH ABOUT TEXT

**Choices:**
- **choice** `?` → `Start`
    > They are not ready to choose yet.

### Node `SlynthArrived`

BASE SLYNTH ARRIVED TEXT

**Choices:**
- **choice** `?` → `Start`
    > My thanks.

### Node `SlynthSettled`

BASE SLYNTH SETTLED TEXT

**Choices:**
- **choice** `?` → `Start`
    > My thanks again.
