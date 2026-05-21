# Conversation: `Iseppa`

_Inherits: (default: BaseConversation)_

_3 start(s), 18 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Recame`

You're back, I see.

        Brightsheol must not have been that interesting, I suppose? Or perhaps you missed me.

        *Iseppa winks*

**Choices:**
- **choice** `?` → `GuestKlanq`
    > What do you think of Klanq's visit?
- **choice** `?` → `Greetings`
    > Good to see you, Iseppa. Let's chat.
- **choice** `?` → `End`
    > Live and drink.

### Start `Post Arms`

These are the final chapters of this story, =name=, and likely of many stories more too.

        It will be well to see the other side of all this, one way or another.

**Choices:**
- **choice** `?` → `TombQuest`
    > I must enter Brightsheol through the Tomb of the Eaters.
- **choice** `?` → `Greetings`
    > Let's talk, Iseppa.
- **choice** `?` → `End`
    > It will. Live and drink.

### Start `Greetings`

Ah, it is our new short-fingered friend. Set a spell, if you like setting.

        *Iseppa yawns*

        Or spells. Or Iseppa. If you like Iseppa, this is a very good place to be.

**Choices:**
- **choice** `IseppaSusa` → `Bethesda`
    > Do you know anything about Bethesda Susa?
- **choice** `Isepporch` → `Omonporch`
    > What do you know about Omonporch and the self-appointed Earl?
- **choice** `Isepquake` → `Rumbling`
    > Did you feel that rumbling, Iseppa?
- **choice** `Isepshroom` → `Klanq`
    > Have you ever met Pax Klanq?
- **choice** `Iseproject` → `Project`
    > What are you working on, Iseppa?
- **choice** `Isleepy` → `Tired`
    > Are you tired?
- **choice** `Bioseppa` → `AboutMe`
    > I wish to know more about you.
- **choice** `?` → `Like`
    > I do like you, Iseppa.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Start`

Oh. Are you lost, =player.formalAddressTerm=?

        I don't mind that you're here, but I was not expecting anyone.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Is this it, I wonder?

**Choices:**
- **choice** `?` → `End`
    > Not today.

### Node `GuestKlanq`

I don't know.

        Klanq's opacity is alluring, frustrating, and dangerous. Like Klanq, my thoughts on Klanq evade easy explanation.

        What you build together will be amazing. Craft well.

**Choices:**
- **choice** `?` → `End`
    > Well, I should go. Live and drink.

### Node `TombQuest`

You're going to the Thin World? I confess to some measure of envy.
        
        I have dreamt many times of disappearing into a cool ocean of information, shaking the cruft of my physical form from newly-freed quills. If that came of my waking life, would I then dream as chore-doing Iseppa in her chambers? Perhaps it's best I don't know.

**Choices:**
- **choice** `?` → `End`
    > Very well, Iseppa. Live and drink.

### Node `Like`

Thank you, =name=. I like you too.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `Gosseppa` → `Gossip`
    > What can you tell me about the other Barathrumites?
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Bethesda`

Bethesda Susa is an antipodal place, a gallery of life and death and the stages between. Its depths prolong life and end it early, remove life from the flow of days or return it.

        It will seek to make you late. Take care you come back on time.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Omonporch`

Though I adore the sights and smells of Omonporch, its bug problem becomes distracting.

        If I'm to travel there, I always bring something they cannot zip away from.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Rumbling`

Yes. That was not the voice of the caverns.

        It feels like one of my nightmares come to life at last.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Klanq`

I have not.

        I would, however, love to meet him. He seems a fun fungus.

        But I daren't go. I fear the sludges.

**Choices:**
- **choice** `?` → `Sludges`
    > You fear sludge?
- **choice** `?` → `MmHmm`
    > I see.

### Node `Sludges`

I fear sludges, the kind you may no longer describe with 'some'. Born of the ancient stuff of existence, possessed of malice and wanting nothing more than to eat whatever they can, and they can eat whatever. It is even worse when they drink.

        Take care with them.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Tired`

I am always tired, =player.formalAddressTerm=.

        My sleep comes in fits and starts, and always with ghastly visions. Sometimes my rest must be coaxed along with medicine.

**Choices:**
- **choice** `?` → `Dreams`
    > You have prophetic visions in your sleep?
- **choice** `?` → `MmHmm`
    > I see. That seems difficult.

### Node `Dreams`

No. My nightmares are a concoction of my disordered mind, nothing more. The fumes from this cauldron have nothing to do with the future, save how they affect it.

        *Iseppa sighs.*

        I'd rather speak of something else, =player.formalAddressTerm=.

**Choices:**
- **choice** `?` → `MmHmm`
    > Oh.

### Node `MmHmm`

Mm-hmm.

        *Iseppa yawns.*

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Gossip`

I would never think to steal from you the delight of forming opinions of my enclave on your own.

        *Iseppa yawns.*

        Besides, that sounds like rather a lot of talking.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `AboutMe`

I am Iseppa, and she is me.

        I've given thought to being someone else, but never enough to try.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Project`

I am contemplating the distinction between animal and rock. Why are they different? How much like a rock must an animal be when it ceases to be an animal?~
        I am considering the window of consciousness through which each of us views the universe. What happens to it when we die?~
        I am taking inventory of my faculties, and looking for any that I might not previously have considered.~
        I am considering the thought as a discrete object. I wish to determine whether I am able to think a single thought only, and to determine how to distinguish it from another thought in the same vein.~
        I am considering the determination of goodness and badness in a thing, and how it is determined. The interaction between data and subjective evaluation, and the values that guide us that we cannot put to words.~
        I am contemplating the Spindle's place in Qud, its position as a conceptual focal point. How much of what we know of the Spindle is the craft of those before us, carried forward?~
        I am considering narrative inheritances. The stories we were told when our minds were more putty-like, the follies that shaped who we are, that shape the whole of Qud.

**Choices:**
- **choice** `?` → `Project2`
    > Oh. It looks like you are sorting screws and fasteners.
- **choice** `?` → `Project3`
    > Have you come to any conclusions?
- **choice** `?` → `End`
    > I shall leave you to it. Live and drink, contemplatrix.

### Node `Project2`

Yes.

**Choices:**
- **choice** `?` → `MmHmm`
    > But you're also doing the other thing.
- **choice** `?` → `End`
    > I'll leave you to it.

### Node `Project3`

Not yet, but that's not the point.

**Choices:**
- **choice** `?` → `MmHmm`
    > Oh, I see.
- **choice** `?` → `End`
    > I'll leave you to it, then.
