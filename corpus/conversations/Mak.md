# Conversation: `Mak`

_Inherits: (default: BaseConversation)_

_0 start(s), 10 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

What indignity have you come to heap upon the mound, whelp? Out with it.

**Choices:**
- **choice** `FounderChoice` → `Founder`
    > You're one of the founders of this freehold, aren't you?
- **choice** `WhoChoice` → `Who`
    > Who are you?
- **choice** `StatureChoice` → `Stature`
    > I've never seen a frog of your stature.
- **choice** `FreeholdChoice` → `Freehold`
    > What can you tell me about the Freehold?
- **choice** `PondChoice` → `Pond`
    > This pond is peaceful.
- **choice** `?` → `End`
    > Live and drink.

### Node `Croak`

*crrrk*

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
    > Live and drink.

### Node `Founder`

What of it? Scurry on and leave me to brood.

**Choices:**
- **choice** `?` → `Founder2`
    > This seems a joyful place. Why are you angry?
- **choice** `?` → `Start`
    > I've something else to ask
- **choice** `?` → `End`
    > Live and drink.

### Node `Founder2`

Why? A lifetime of vexation. Born to a cacophony of static ringing the ears raw. Thousands of my kinfolk cut down by that porphyric wasp fools called Lamb. A millenium of hot stinking sun and disgusting brine lice for supper.

        Misery obtains on this pond, whelp. By Chavvah if you start beaming like a sunray and yodeling at the Beetle Moon, I'll eat you where you stand.

**Choices:**
- **choice** `?` → `Start`
    > ...I've more to ask.
- **choice** `?` → `End`
    > Live and drink.

### Node `Who`

Who am I? Mak. That's all you get. I'll not waste the honey of my mouth on idle inquiries.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Stature`

...

        And? Is that the whole of your fool statement?

**Choices:**
- **choice** `?` → `Stature2`
    > Yes.
- **choice** `?` → `Croak`
    > I'll ask something else.

### Node `Stature2`

Trust what you hear of the svardym, whelp. The sky blackens at our accession and we are like to eat you.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Freehold`

Have the adiyy chewed the hue from your eyes? See for yourself. Free folk make a gathering here and their racket rings through the reef. One can hardly steep in his greens without being mewled to by a salt-stung baby.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Pond`

It was once.

**Choices:**
- **choice** `?` → `Pond2`
    > What happened?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Pond2`

Whelp, affix your eyes to that clam right yonder. Go step inside and find your answers.

**Choices:**
- **choice** `?` → `End`
    > ...
