# Conversation: `Meyehind`

_Inherits: (default: BaseConversation)_

_0 start(s), 15 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`HindrenVillageRavaged`_

Bey Lah is gone. I hope you're happy.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageDoomed`_

Our world is ending...

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Live and drink, =name=.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Perhaps it was too much to wish that Bey Lah would change.

        But Esk is happy again. That makes me feel happy too.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

I can't imagine why you would think we want your company, kendren.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Leave us alone.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Thank you for what you've done for our sister.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

If you've nothing you need of me, kendren, I'd just as soon hold my peace.

**Choices:**
- **choice** `?` → `ShowSonnet`
    > Does this poem belong to you?
- **choice** `?` → `Meyequeries`
    > May I ask you some questions?
- **choice** `?` → `End`
    > Very well. Live and drink.

### Node `Meyequeries`

I suppose.

**Choices:**
- **choice** `Family` → `Family`
    > Tell me about your family.
- **choice** `Brother` → `Brother`
    > Keh told me that Eskhind has a brother.
- **choice** `Culprit` → `Culprit`
    > Who do you think stole Kindrish?
- **choice** `?` → `End`
    > Never mind. Live and drink.

### Node `Brother`

... did she.

**Choices:**
- **choice** `?` → `Demand`
    > Where is he? Tell me what happened to him.
- **choice** `?` → `Correct`
    > But she doesn't, does she? Only sisters.

### Node `Culprit`

I don't like to speculate on a matter I know so little of, nor one whose outcome so dearly affects my life.

        If what you want is a strongly-worded accusation based on nothing, Liihart is the sister to talk to.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > That's all for now. Live and drink.

### Node `Correct`

*You see Meyehind's body relax a bit.*

      That's right, kendren.

      It's naught to do with the case anyway. Only cold tradition and the cold heart that keeps it.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > That's all for now. Live and drink.

### Node `Demand`

*Meyehind's glare turns withering for the few seconds it takes before she turns her face and body away from you.*

**Choices:**
- **choice** `?` → `End`
    > ...?

### Node `Family`

What's to tell? We are outcasts, pushed to the margins by our people for the crime of harmless deviance.

        It's beyond perverse to call us back just so Grand-Doe can punish us further.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > That's all for now. Live and drink.

### Node `ShowSonnet`

Hm! No, Eskhind wrote that, but I thought she burned it.

        If you return it to anyone, you should return it to her.

**Choices:**
- **choice** `?` → `End`
    > Thank you. Live and drink.
