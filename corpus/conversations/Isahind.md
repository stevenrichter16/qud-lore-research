# Conversation: `Isahind`

_Inherits: (default: BaseConversation)_

_0 start(s), 7 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`HindrenVillageRavaged`_

I'd rather not talk. Sorry.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageDoomed`_

Strange and rocky times have befallen Bey Lah.

        But I'm confident that we can get through this, as we always do. Shall we trade?

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageProspers`_

My friend! Thank you so much for helping our village!

        Our prosperity means that I have new goods for you to peruse, if you're interested.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

As if a new Hindriarch weren't enough, I hear we might become a Democracy! How thrilling.

        This is a new chapter in Bey Lah's history, kendren. Would you care to trade?

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Amazing! The youngest hindriarch in Bey Lah's preserved history, if only temporarily so.

        Care to buy a souvenir to commemorate this historic occasion?

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Oh! A real live kendren, here in our village! Live and drink, lovely friend!

        If you'd care to trade, I have a modest amount of local goods I can offer.

**Choices:**
- **choice** `?` → `ShowSonnet`
    > Does this poem belong to you?
- **choice** `?` → `End`
    > I have all I need. Live and drink.

### Node `ShowSonnet`

No, that's not mine. But it looks lovely!

**Choices:**
- **choice** `?` → `End`
    > I see. Live and drink.
