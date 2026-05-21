# Conversation: `Jacobo`

_Inherits: (default: BaseConversation)_

_3 start(s), 15 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Recame`

Why, =name=, Brightsheol treated you well. There is a new gravity about you; your proverbial boots ring louder in the Annals with each step.

        I imagine you're off to Teach's study? They're already at work down there.

**Choices:**
- **choice** `?` → `GuestKlanq`
    > What do you think of Klanq's presence?
- **choice** `?` → `Greetings`
    > Light shine through you, Jacobo. Let's talk.
- **choice** `?` → `End`
    > Live and drink.

### Start `Post Arms`

Never before had the Templar broken so far through our defenses. We live a new reality now, one harder to weather.

        Is there anything you need, =name=?

**Choices:**
- **choice** `?` → `TombQuest`
    > I must enter Brightsheol through the Tomb of the Eaters.
- **choice** `?` → `Greetings`
    > Light shine through you, Jacobo. Let's talk.
- **choice** `?` → `End`
    > No. Live and drink.

### Start `Greetings`

Light shine through you, friend.

**Choices:**
- **choice** `JacoboRumblingChoice` → `Rumbling`
    > Did you feel that rumbling, Jacobo?
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Music`
    > Is that... music... coming from your loudspeaker?
    >         It sounds like a bell echoing in the void backward through time.
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Start`

Who are you? What? Please, do not disturb me.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

The Templar are assaulting the enclave? Oh dear, dear...

        May our guns' lasers shine with the light of the Kasaphescence.

**Choices:**
- **choice** `?` → `End`
    > I must go.

### Node `GuestKlanq`

I admit a burning curiosity to see the joined imagination of our Q Girl and Pax Klanq, and no doubt yours as well. Watching such a creation burgeon from empty space to fullness of being would be a joyful entry in the chronicles of my life, but...

        Too many fingers tangle in the honeypot, as my cubhood mentor would tell me.

**Choices:**
- **choice** `?` → `End`
    > So they do. Live and drink, Jacobo.

### Node `TombQuest`

My quills prickle with unease to hear you say such things.

        Be certain to visit the village of Ezra. The Daughter of Exile who lives there is as good a tinker as any I know, and she always has surplus she's willing to sell.

**Choices:**
- **choice** `?` → `End`
    > I thank you. Live and drink.

### Node `Bethesda`

The Temple of the Rock is cut off from the wider world, and I hear the Mechanimist colonists no longer recognize High Priest Eschelstadt. That said, if you are favored by the Mechanimists, if you are welcome in their holy places, then I've no doubt that Phinae Hoshaiah will grant you peaceful entry.

**Choices:**
- **choice** `?` → `Music`
    > Is that... music... coming from your loudspeaker?
    >         It sounds like a bell echoing in the void backward through time.
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `Music`

Yea! So you like it? Sheba Hag and I composed it on a wavelathe. We made a series of songs about the birth and life of the Kasaphescence. Together we call them "Spun on the Cosmic Loom".

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Sheba`
    > Sheba Hag?
- **choice** `?` → `Kasaphescence`
    > What's the Kasaphescence?
- **choice** `?` → `Mechanimist`
    > So you're a Mechanimist?
- **choice** `?` → `Songs`
    > Have you made other songs?
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `Sheba`

Oh, Sheba Hagadias. She's the librarian at the cathedral of the Six Day Stilt. My water-sister and cohort in chrome.

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Kasaphescence`
    > What's the Kasaphescence?
- **choice** `?` → `Mechanimist`
    > So you're a Mechanimist?
- **choice** `?` → `Songs`
    > Have you made other songs?
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `Kasaphescence`

Beauty manifest, whose chromium shoals are Awe itself. In my belief system, She's the being from whom all metal was birthed, out in the ever-void. There are pieces of Her in every chrome belfry and every machine. Even bits of Her in our own blood.

        For me, Her essence extends beyond mere metal. Anything that's ordered, She infuses: a poem, a mathematical proof, a clean workspace... so definitely not Q Girl's.

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Mechanimist`
    > So you're a Mechanimist?
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `Mechanimist`

Of a sort, yes. I'm part of a branch who deify the Kasaphescence only. We believe the argent fathers to be earthly beings: important to the faith's early history but not divine.

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Songs`
    > Have you made other songs?
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `Songs`

Many. Many. This is my third collaboration with Sheba. Our first two collections were called "Immaculate Chrome" and "Outside In".

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Sheba`
    > Sheba Hag?
- **choice** `?` → `Kasaphescence`
    > What's the Kasaphescence?
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `Orb`

Oh, it's the silver rondure. It's a mark of devotion to the Kasaphescence.

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Kasaphescence`
    > What's the Kasaphescence?
- **choice** `?` → `Mechanimist`
    > So you're a Mechanimist?
- **choice** `?` → `Music`
    > Is that... music... coming from your loudspeaker?
    >         It sounds like an bell echoing in the void backward through time.
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `Machine`

Don't I know it. I've had to invent eight separate systems of organization to manage them all. At the moment I'm trying out a new one, Harmonices Spiralis. Spiral towers with heights increasing according to the harmonic series of numbers. It's... fine.

        The problem is I'm always inscribing more disks. New contraptions. Reverse-engineered artifacts. It's a good problem to have, I suppose.

        Take a look. See if any interest you.

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Music`
    > Is that... music... coming from your loudspeaker?
    >         It sounds like a bell echoing in the void backward through time.
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `GritGate`

We're a vibrant community here. A circle of monks mapping the outer lattices and raising viaducts where we need to.

        We remain secluded to protect ourselves. Otho and Barathrum insist on it. They are wise, and I defer to them. My collaboration with Sheba Hag does cause them worry, but they tolerate it, bless their hearts.

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Sheba2`
    > Sheba Hag?
- **choice** `?` → `Music`
    > Is that... music... coming from your loudspeaker?
    >         It sounds like a bell echoing in the void backward through time.
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `End`
    > Live and drink.

### Node `Sheba2`

Oh, Sheba Hagadias. She's the librarian at the cathedral of the Six Day Stilt. My water-sister and cohort in chrome.

**Choices:**
- **choice** `?`
- **choice** `?` → `Bethesda`
    > Jacobo, do you have advice for entering Bethesda Susa?
- **choice** `?` → `Music`
    > Is that... music... coming from your loudspeaker?
    >         It sounds like a bell echoing in the void backward through time.
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.

### Node `Rumbling`

Argggggggh! Yes! Three towers of disks came crashing down!

**Choices:**
- **choice** `?` → `Music`
    > Is that... music... coming from your loudspeaker?
    >         It sounds like a bell echoing in the void backward through time.
- **choice** `?` → `Orb`
    > That chrome orb earring you're wearing. What's the meaning of it?
- **choice** `?` → `Machine`
    > You have so many data disks.
- **choice** `?` → `GritGate`
    > What can you tell me about Grit Gate?
- **choice** `?` → `End`
    > Live and drink.
