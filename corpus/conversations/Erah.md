# Conversation: `Erah`

_Inherits: (default: BaseConversation)_

_0 start(s), 10 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Be nimble, wayfarer. Take in a draught of cider before leaving.

**Choices:**
- **choice** `?` → `Introduce`
    > I am =name=. Who are you?
- **choice** `?` → `Cider`
    > Why is the cider chunky?
- **choice** `?` → `Mask`
    > Is that a Naphtaali mask over there?
- **choice** `?` → `End`
    > Live and drink, cider-friend.

### Node `Introduce`

I am called Erah. Branches part for you, =name=.

### Node `Cider`

That'd be the mushrooms. Bit heartier, a-ye?

**Choices:**
- **choice** `?` → `Mushrooms`
    > Why would you put mushrooms in cider?

### Node `Mushrooms`

...
    
    Bit heartier, a-ye?

### Node `Mask`

Is. Was naphtaali once.

**Choices:**
- **choice** `?` → `Naphtaali`
    > Was? Not any more?
- **choice** `?` → `Subject`
    > Let us speak of something else.

### Node `Subject`

Mmm. Have cider?

### Node `Naphtaali`

A-ye, quit. Lost most my minyan to goatfolk. The sower's eye fell upon us and so we fell too.

**Choices:**
- **choice** `?` → `Minyan`
    > What is a minyan?
- **choice** `?` → `Godhed`
    > What became of your Godhed?
- **choice** `?` → `Memories`
    > May their memories bless you.
- **choice** `?` → `Subject`
    > Let us speak of something else.

### Node `Memories`

As the very canopy, they will.
    
    Thank you.

**Choices:**
- **choice** `?` → `Subject`
    > Let us speak of something else.
- **choice** `?` → `End`
    > Live and drink, ciderer.

### Node `Minyan`

Pilgrims, drawn together by need and awe and inspiration. Tinkers and sodders and guards and scouts, alloyed under the pressure of lifeswork.
    
    Family, like.

### Node `Godhed`

Don't know. Wrecked? Fled?
    
    I crawled away, never looked back. That's the all of it.
