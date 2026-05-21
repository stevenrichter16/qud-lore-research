# Conversation: `PaxKlanq2`

_Inherits: (default: BaseConversation)_

_1 start(s), 20 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

Klanq puff on you...
				
				
				..later. Now, Klanq pause puff for prickles favor.

**Choices:**
- **choice** `?` → `IsGolemReady`
    > Is the Creature ready?
- **choice** `?` → `BuildGolem`
    > I am ready for the Creature to be moulded and catalyzed.
- **choice** `?` → `Die`
    > Didn't you die?
- **choice** `?` → `GolemComponentQuestions`
    > Can you tell me about the components I must gather?
- **choice** `?` → `GolemOtherQuestions`
    > What should I know about the Creature?
- **choice** `?` → `BarathrumsStudy`
    > Do you live in Grit Gate now?
- **choice** `?` → `GolemOtherQuestions`
    > I would like to ask some questions about the large creature.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Die`

Klanq distribute! Cannot kill Klanq in a way that matters.

### Node `BuildGolem`

Materials ready? Circuits to solder. Klanq stir the soup?

**Choices:**
- **choice** `?` → `GolemThreeDays`
    > Yes.
    - _part: `BuildGolem` (TimeDays=3)_
        > You haven't provided the mound with all the necessary materials.
    - _part: `TakeLiquid` (Liquids=proteangunk Amount=20 Destroy=true Priority=10)_
        > You don't have enough primordial soup.
- **choice** `?` → `Welcome`
    > Not yet.

### Node `GolemThreeDays`

Klanq stir! Come back three days and Creature arrive. Now, take operating manual.

**Choices:**
- **choice** `?` → `End`
    > I'll return in three days.

### Node `IsGolemReady`

No! Be back =mound.complete.days=.

**Choices:**
- **choice** `?` → `Welcome`
    > OK.

### Node `GolemComponentQuestions`

Soup, body, catalyst, atzmus, armament, incantation, hamsa, power source, soup. Ask component!

**Choices:**
- **choice** `?` → `Soup`
    > Tell me about the soup.
- **choice** `?` → `Body`
    > Tell me about the body.
- **choice** `?` → `Catalyst`
    > Tell me about the catalyst.
- **choice** `?` → `Atzmus`
    > Tell me about the atzmus.
- **choice** `?` → `Armament`
    > Tell me about the armament.
- **choice** `?` → `Incantation`
    > Tell me about the incantation.
- **choice** `?` → `Hamsa`
    > Tell me about the hamsa.
- **choice** `?` → `Power`
    > Tell me about the power source.
- **choice** `?` → `Mound`
    > Where do I place components once they are gathered?
- **choice** `?` → `Welcome`
    > I have something else to ask.

### Node `Soup`

Primordial soup 20 drams. Act as Creature circulatory liquid. Catalyzed and boom! Animating substance. Electromagnets induce sinusoidal flow.

### Node `Body`

Body of creature friend to form Creature after. Must follow you and be experience. No worry, friend not consumed in creation.

### Node `Catalyst`

Three dram of pure liquid to catalyze soup and circulate nutrient. Liquid choice alter sanguine mixture, change Creature.

### Node `Atzmus`

Atzmus transcendental imprint of being. Pattern trait after creature part, crossed with Body.

### Node `Armament`

Zetachrome weapon. Attune Creature to the martial art and shape metachrome fist-types in the fashion after.

### Node `Incantation`

Words spoken from your experience and inscribed to form being-bond. First sounds heard in Creature's early dreambrain.

### Node `Hamsa`

Chosen token to palm-solder and orient with object-meaning, 5 lbs. or less. Like others, choice alters Creature trait and behavior.

### Node `Power`

Ascending Creature need mightful battery with rare electromagnet shielding. Purple prickles make neutron cell with 3 flux drams, or must find different source.

### Node `Mound`

Interact with scrap-clay mound. Then chat Klanq to solder circuits and stir the soup.

### Node `GolemOtherQuestions`

What ask! Klanq say.

**Choices:**
- **choice** `?` → `Work`
    > I will bond with the Creature. How does this work?
- **choice** `?` → `Work`
    > I am bonded with the Creature. How does this work?
- **choice** `?` → `Spindle`
    > Barathrum and I will ascend the Spindle inside the Creature?
- **choice** `?` → `Equip`
    > Can the Creature wear equipment?
- **choice** `?` → `Damage`
    > What if it's damaged or destroyed?
- **choice** `?` → `Welcome`
    > I have something else to ask.

### Node `Work`

Creature follow you like friend. Also, can enter Creature and take control. One friend fit inside with you.

### Node `Equip`

Creature is large creature, can only wear gigantic gear. Like kraken or saltback.

### Node `Damage`

Prickles install reshaping nook in Court of Sultans at Omonporch. There, respackle Creature with one dram of sunslag. Or recall creature if lost.

### Node `Spindle`

Yes! But before then, can walk around with creature. Talk, fight, sleep... the normal. Friend.

### Node `BarathrumsStudy`

Klanq live! Tragedy of jalopy invite Klanq to dimcandlespace. Klanq soften stone floor with plushes, dust shelves of boring jars with happy and spores. Prickles look at it.
