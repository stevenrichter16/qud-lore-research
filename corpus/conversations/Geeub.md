# Conversation: `Geeub`

_Inherits: (default: BaseConversation)_

_0 start(s), 11 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

*long, smoky croak*

        Ah, =player.formalAddressTerm=, here at last. Sit. Smoke. Rest.

**Choices:**
- **choice** `GeeubFamiliarChoice` → `Familiar`
    > Sorry, have we already spoken?
- **choice** `FounderChoice` → `Founder`
    > You're one of the founders of this freehold, aren't you?
- **choice** `GeeubWhoChoice` → `Whomst`
    > Who are you?
- **choice** `GeeubToweringChoice` → `Towering`
    > I can't help but notice your impressive stature, even in repose.
- **choice** `GeeubFreeholdChoice` → `Freehold`
    > What can you tell me about Yd?
- **choice** `GeeubEndChoice` → `End`
    > Live and drink.

### Node `Familiar`

Ayup. But seconds ago. As only yesterday, no? Hoh hoh hoh.

        *continued croaking laughter*

**Choices:**
- **choice** `GeeubLaugh` → `Laughing`
    > *laugh*
- **choice** `?`
- **choice** `GeeubQuery` → `Query`
    > Ah. Well. Let's talk about something else, then.
- **choice** `?` → `End`
    > Oh, very funny. Live and drink.

### Node `Query`

*grrrk*
        We ask, we answer.

        We call, we respond.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Whomst`

Over time, Geeub. Good as any.

        *roooak*

        Names, ehh.

**Choices:**
- **choice** `?` → `Introduce`
    > Greetings, Geeub. I am =name=.
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Introduce`

*croaking sigh*

        Congratulation, condolence, which ever. Mind and name slip by another.

**Choices:**
- **choice** `?`
- **choice** `?`

### Node `Towering`

So large? Hoh hoh. Well. Hatchlings, so rage-dense. Size diffuses, no?

        However. Mak diverges, hoh hoh. Egg-rage simmers on a greater pot. Our voice eld-feeble, close your ears to it. Hoh hoh hoh.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Freehold`

Sun we once blotted out nestles our horizon. We tend thought-seeds with algae, wrap in crysteel, bathe in arc-light. Build, live, fight.

        Here as elsewhere, grow is struggle. Fun to watch, no? Hoh. Hoh.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Laughing`

Hoh hoh hoh hoh.

        *grrrrrk*

        We have fun.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Founder`

'Founder' the query. 'Founder' is water-taking, no? To be breached and sink. How cruel the judgment.

        *rrrrroak*

        Hoh hoh. This voice japes -- we, witness to the birth of Yd. The query, no?

**Choices:**
- **choice** `?` → `Founder2`
    > ...

### Node `Founder2`

Yes, we were present, if less active than other-bodies. But we saw, and rattle with memory-artifacts as a Consortium lockbox rattles with jewels; shards of an eon-old data disk, bits of stories and places. Kin-fleeing, louse-meals, ghastly boredom. But Fate's caprice brought us through history's footsteps. There was a machine-speaker, and her ursine apprentice with his little plant, and the Sower with a tetrad of chubby whelps, and then, at last, Many-Eyes. Our dear galgal. So many.

**Choices:**
- **choice** `?` → `Founder3`
    > ...

### Node `Founder3`

But alas. Like our sea-grape friend's lockbox, these memories are not mine to retrieve at will. They come and go, and may be warped by eld.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
