# Conversation: `Dreamer`

_Inherits: (default: BaseConversation)_

_5 start(s), 9 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `KilledTau`  _IfTestState=`TauElse contains KilledByPlayer`_

*A long chime rings. The bed of a shallow creek teems with brief life.*

**Choices:**
- **choice** `?` → `Killed2`
    > Tau has met her fate.

### Start `LostInSoft`  _IfHaveState=`TauLostInSoft`_

*A long chime rings. The bed of a shallow creek teems with life and death, nature's self-consuming ouroboros.*

**Choices:**
- **choice** `?` → `Lost2`
    > Tau is gone.

### Start `KilledCompanion`  _IfTestState=`TauCompanion contains KilledByPlayer`_

*A long chime rings. The bed of a shallow creek teems with life and death, nature's self-consuming ouroboros.

**Choices:**
- **choice** `?` → `Companion2`
    > Tau has completed the -elseing ritual.

### Start `ElseWelcome`  _IfHaveState=`ElseingComplete`_

*A long chime rings. The bed of a shallow creek teems with life and death, nature's self-consuming ouroboros.*

**Choices:**
- **choice** `?` → `Else2`
    > Tau has completed the -elseing ritual.

### Start `Welcome`

*the chime rings*

				*In your mind's eye, you see yourself touching a mirror. You tap the glass and it ripples like the surface of a placid lake.*

**Choices:**
- **choice** `?` → `Silent`
    > ...
- **choice** `?` → `Name`
    > Your name is pronounced as the pause between two words, friend. How do I know this?
- **choice** `?` → `Gyredream`
    > Tell me of gyredream.
- **choice** `?` → `TauChime`
    > I am to carry Tau's chime to Taproot, so she can leave Chavvah.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Killed2`

*You tumble from the jar, your sinewy body twisting against the electric emptiness in your belly, the weight of eggs. You discover a morsel and consume it soft and delicious. You will spawn here. You will eat the morsels. Your babies will eat all of the morsels.

**Choices:**
- **choice** `?` → `Welcome`
    > I... have more to ask you.
- **choice** `?` → `End`
    > Live and drink.

### Node `Lost2`

*Wielding an oversized jar in little hands, a child tips it into the running current of a softly burbling creek. Tiny creatures that had been living in the jar spill into the creek, protected from the killing current by a clump of slimy biofilm. The child peers at a little fry swimming in the jar.

**Choices:**
- **choice** `?` → `Welcome`
    > I... have more to ask you.
- **choice** `?` → `End`
    > Live and drink.

### Node `Companion2`

*From the banks of a shallow creek, you watch a toad floating on the water, belly up. It flails, helpless against even the gentle current of the water in which you placed it seconds ago. You watch it float away, toward the rushing currents ahead.

        Helpless to myriad unknowable fates, the toad disappears from view into the rapids, sent there by your hand.*

**Choices:**
- **choice** `?` → `Welcome`
    > I... have more to ask you.
- **choice** `?` → `End`
    > Live and drink.

### Node `Else2`

*From the mouth of the jar in your little hands, you watch a frog leap into the water of a softly burbling creek. The gentle current sweeps the frog's little body away to an unknown fate as curious crayfish peek out from their hiding places. The jar in your hands is empty.*

**Choices:**
- **choice** `?` → `Welcome`
    > I... have more to ask you.
- **choice** `?` → `End`
    > Live and drink.

### Node `Silent`

*The moment stretches on into a steep asymptote, the peaks and valleys of possible outcomes speeding by in an imaginary blur. You imagine the sound of a tiny metal thread brushing across the bottom of a dusty valley, amplified a thousand times.*

### Node `Name`

*the entity chimes, and you witness water lapping at the long edge of a pebble beach. Slowly, the tide brushes clean the surface of each rock, etching time's passage onto millions of tiny canvases. Somewhere, something dies.*

### Node `Gyredream`

*Your entire self buzzes at the sound of _'s chime, a shock from the center and radiating outward. Sensation bubbles up to the surface, a tightening of the self. It is as if cresting a great hill atop a cathedra or an oncoming witchwood overdose; the void yawns under you. Something terrible is born.*

**Choices:**
- **choice** `?` → `Meaning`
    > I don't understand. What could it mean?
- **choice** `?` → `Welcome`
    > Let... let us speak of other things.
- **choice** `?` → `End`
    > Excuse... excuse me.

### Node `Meaning`

*You are a little sapfly resting in the crook of a swarmshade tree. The boughs stretch in great barkish deserts before exploding into a tangle of branches. Your brethren buzz in an agitated cloud, feeling fear or excitement or hunger. Something buzzes beyond the leafy reaches of your sight, all-consuming but unclear.*

**Choices:**
- **choice** `?` → `Welcome`
    > I... wish to speak of other things.
- **choice** `?` → `End`
    > I will think on this... live and drink.

### Node `TauChime`

*Just as you activate an artifact listening device that ceased to exist centuries ago, you hear the end of an emotional song. The space between relief and sorrow throbs with uncomfortable tension. You ache with it.*
