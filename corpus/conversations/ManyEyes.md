# Conversation: `ManyEyes`

_Inherits: (default: BaseConversation)_

_0 start(s), 8 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`Recame`_

NON MOLOCH? NON MOLOCH RETURNEN FROM BRIGHTSHEOL.

**Choices:**
- **choice** `Moloch` → `Non`
    > Non Moloch?
- **choice** `Brightsheol` → `Non`
    > Yes, I've returned from Brightsheol.
- **choice** `?` → `End`
    > ...

### Node `Start`

*READOUT*

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Non`

NON MOLOCH HER AT HOM. NON MOLOCH IN MAQQOM YD.

**Choices:**
- **choice** `?` → `MaqqomScramble`
    > ...
- **choice** `?` → `Maqqom`
    > Maqqom Yd? The Place outside Itself?
- **choice** `?` → `End`
    > ...

### Node `MaqqomScramble`

*READOUT*

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Maqqom`

MAQQOM YD. SOUTH-CONTRE FREEN FROM SALUM.

**Choices:**
- **choice** `?` → `MaqqomTell`
    > Many Eyes, can you tell me of Maqqom Yd?
- **choice** `?` → `End`
    > ...

### Node `MaqqomTell`

SOUTH-CONTRE FREEN FROM SALUM. BY TRETE WITH SAAD CALLEN MOLOCH, AND MONEIEN BI ALDERSESSE.

        BY TRETE GALGALLIM BILDEN PIPE TO DRINKEN THANE SLIPSTREAM, AND FORGE TO BURNEN STEL-CRISTAL, AND CASKE TO HOLDEN GLOUINGE O FISH.

**Choices:**
- **choice** `?` → `Mean`
    > And what of the Freehold? What do you do now?
- **choice** `?` → `NonMoloch`
    > Who is Non Moloch, from before?
- **choice** `?` → `End`
    > ...

### Node `Mean`

BY TRETE GALGALLIM SERVEN, BUT NON NOU.

**Choices:**
- **choice** `?` → `MaqqomTell`
    > I want to ask something else.
- **choice** `?` → `End`
    > ...

### Node `NonMoloch`

YOU. YOU REGNEN NON HER. NON MOLOCH IN MAQQOM YD.

**Choices:**
- **choice** `?` → `End`
    > ...
