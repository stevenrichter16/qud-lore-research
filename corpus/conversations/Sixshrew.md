# Conversation: `Sixshrew`

_Inherits: (default: BaseConversation)_

_0 start(s), 7 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Oh joy, another meat-being. Please tell me you're here to buy something.

**Choices:**
- **choice** `Greet` → `Introduction`
    > I am =name=. You are?
- **choice** `Rude` → `Impolite`
    > You're being a bit rude.
- **choice** `Ask` → `CrankyPlant`
    > Is something the matter?
- **choice** `?` → `End`
    > I suppose I'll be leaving, then.

### Node `Introduction`

I am Sixshrew, a merchant from the Consortium of Phyta disinclined to waste xyr time on talkative strangers.

        I sell things, and you can buy them. I would in fact strongly encourage you to buy them, or be on your way.

**Choices:**
- **choice** `?` → `Name`
    > Why are you called Sixshrew?
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > I'll be on my way. Live and drink.

### Node `Name`

Why are you called pest?

**Choices:**
- **choice** `?` → `NotPest`
    > I'm not...
- **choice** `?` → `Pest`
    > Because I am a pest?

### Node `NotPest`

You are now.

        Are you going to buy something, pest?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > I'm all set. Live and drink, rude one.

### Node `Pest`

Just so.

        Would you like to buy something, pest?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > I'm all set. Live and drink, rude one.

### Node `Impolite`

You're being a bit annoying, so I suppose both of us have our burdens to bear.

        Perhaps we should do some trading and move on with our lives, hmm?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > I'll skip to the last part. Live and drink, rude one.

### Node `CrankyPlant`

Oh, I'm fine, fine.

        I simply adore being assigned this stinking backwater musa grove after decades of service, unceremoniously dumped in an office next to a fleshy tinker who works day and night, making all manner of racket through the thinnest, most conductive walls ever crafted.

        What is it humans say? "Living the dreen?" Yes, I am living the dreen.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > I'll be on my way. Live and drink.
