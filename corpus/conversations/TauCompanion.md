# Conversation: `TauCompanion`

_Inherits: (default: BaseConversation)_

_5 start(s), 4 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`  _IfTestState=`TauElse contains KilledByPlayer`_

Begone from me, stardimmer. Your own hand has vaporized your purpose.

**Choices:**
- **choice** `?` → `End`
    > ...

### Start `Welcome`  _IfHaveState=`ElseingComplete`_

You thrived at the performance of a pruning motion, utensil. Now store yourself until Fate reshapes you.
				
				The end.

**Choices:**
- **choice** `?` → `End`
    > ...

### Start `WelcomeHub`

The utensil arrives. You, to prune the fate-rhizome and free our girl. Go now and perform the motion.

**Choices:**
- **choice** `?` → `Seeker`
    > You're a seeker of the Sightless Way?
- **choice** `?` → `Taking`
    > Where are you taking Tau?
- **choice** `?` → `End`
    > ...

### Start `Welcome`

Give her your parting words, utensil. Our hearts are in elsewhere.

**Choices:**
- **choice** `?` → `End`
    > ...

### Start `Welcome`

Begone. Fate has not yet shaped you, utensil.

**Choices:**
- **choice** `?` → `End`
    > ...

## Nodes

### Node `Seeker`

Utensil? That is my avocation, yes. A million sun-dead homes I've roved, a trillion more await. I'm a worm in the loam of a cosmic wood, perched on a cosmic gulf, swathed in the god-manifold.

### Node `Taking`

Prune! The utensil prunes! -but no, the utensil quivers in uncertainty and vibrates out a question?

				The self is riddled with category errors. The thinking brain mistakes formation for meaning.

**Choices:**
- **choice** `?` → `Understand`
    > Tell me. I wish to understand.

### Node `Understand`

Maggot! What do you think words are? Arrows of inquiry? Words are bricks. Each spoken is laid in bond and builds your prison. There is no understanding.

**Choices:**
- **choice** `?` → `Throw`
    > Bricks can be thrown, too.

### Node `Throw`

You tarry on the future's boundary with abandon, utensil. Throw your brick if you dare.

**Choices:**
- **choice** `?` → `End`
    > ...
