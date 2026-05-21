# Conversation: `Yurl`

_Inherits: (default: BaseConversation)_

_1 start(s), 8 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

Friend! Guns? Knives? Hats? Cucumbers?

**Choices:**
- **choice** `?` → `Asphodel`
    > You're a member of the Consortium of Phyta, right? What do you know about the Earl of Omonporch?
- **choice** `?` → `Story`
    > What are you? What's your story?
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Reset`

...

### Node `Story`

I'm Yurl, chandler and Consortium notary. As for my story, I've been growing out of this pot for a while now. Before that, I was in another pot.

**Choices:**
- **choice** `?` → `Consortium`
    > Consortium?

### Node `Consortium`

Yes, the Consortium of Phyta. We're a merchant fellowship of trees, vines, shrubs, weeds, flowers, herbs, cacti, algae -- most sorts of plants, really.
              
              I can't say I trust any of them, but there is no doubting their usefulness. My shelves are full and the gossip flows.

**Choices:**
- **choice** `?` → `Fungi`
    > What about fungi?

### Node `Fungi`

*Yurl flicks a leaf in displeasure.*
				
				What about fungi?

**Choices:**
- **choice** `?` → `Fungi2`
    > Are there any fungi in the Consortium?
- **choice** `?` → `Reset`
    > Let's change the subject.

### Node `Fungi2`

*Yurl flicks several of their leaves.*

				No.
				
				Shop's closed. Live and drink.

**Choices:**
- **choice** `?` → `But`
    > But...

### Node `But`

I am a gentleplant, -friend-. Uncross your roots and figure it out.
				
				Live and DRINK.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Asphodel`

Asphodel the socialite? Asphodel the scoundrel? You can hate xym -- and I do -- but you have to admire xym (I don't).

				The truth of it is that Plysago had the idea first, to lay claim to the Spindle per some precedent of law established in Abram's time. Of course, Plysago isn't around to make their case, are they?

**Choices:**
- **choice** `?` → `Lease`
    > How can I convince Asphodel to lease the Spindle to Barathrum?

### Node `Lease`

Asphodel trades on reputation and favors. Xe is likely to want to leverage your connections, so be in good social standing with a few factions for xem to even consider it.

				Now, alternatively, if you're loved by the Consortium, xe will feel the pressure to acquiesce. Xe has enough enemies among phyta.

				Of course, where all else fails, you can always sharpen your shears, if you get my meaning.

				*Yurl winks with one of their leaves.*

**Choices:**
- **choice** `?` → `End`
    > I see. Live and drink, Yurl.
