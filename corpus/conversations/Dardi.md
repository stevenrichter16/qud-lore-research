# Conversation: `Dardi`

_Inherits: (default: BaseConversation)_

_3 start(s), 15 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Recame`

=name=. Come in. Eat.

**Choices:**
- **choice** `?` → `GuestKlanq`
    > You seem more irritated than usual.
- **choice** `?` → `Greetings`
    > About your workshop...
- **choice** `?` → `End`
    > Live and drink.

### Start `Post Arms`

Death to all subjugators who dare face us.

**Choices:**
- **choice** `?` → `TombQuest`
    > I must enter Brightsheol through the Tomb of the Eaters.
- **choice** `?` → `Greetings`
    > About your workshop...
- **choice** `?` → `End`
    > Live and drink.

### Start `Greetings`

*Dardi addresses you without looking up from =pronouns.possessive= many workspaces, many of which billow smoke, steam, or some unknown miasma.*

        Welcome to my laboratory, =name=. Rest and sustain =player.reflexive= before returning to your travels.

**Choices:**
- **choice** `BajaBlast` → `Bethesda`
    > Do you know anything about Bethesda Susa?
- **choice** `BananasFoster` → `Omonporch`
    > What do you know about Omonporch and the self-appointed Earl?
- **choice** `VanillaShake` → `Rumbling`
    > Did you feel that rumbling, Dardi?
- **choice** `MushroomRisotto` → `Klanq`
    > Have you ever met Pax Klanq?
- **choice** `ThePorridge` → `Porridge`
    > That smell from the oven is... indescribable.
- **choice** `Platespinning` → `FoodNetwork`
    > What are you working on?
- **choice** `?` → `Kitchen`
    > Laboratory? You work in a kitchen.
- **choice** `?` → `End`
    > Live and drink, food-tinkerer.

## Nodes

### Node `Start`

Who are you? Get out of my work space!

**Choices:**
- **choice** `?` → `End`
    > Sorry! I'm going!

### Node `Start`

Innovation's sworn enemies have come knocking, =name=. Let us answer them.

**Choices:**
- **choice** `?` → `End`
    > Take care.

### Node `GuestKlanq`

Otho has forbidden me from requesting a sample of Klanq. I am to refrain from being puffed on, to cultivate my own!

        Are we yet researchers? Is subject consent no longer adequate ethical rigor? Let Klanq puff on Dardi!

**Choices:**
- **choice** `?` → `End`
    > Well, I should go. Live and drink.

### Node `TombQuest`

Oh? Oh! Do pick up the mopango recipe for bone babka while you're there, won't you? I must know how they make it so dense.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Bethesda`

Yes! I have braved its wharf in the past, to gather precious convalessence for my experiments.

        Are you going? Dress warmly and mind the trolls.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `KitchenNightmare` → `Kitchen`
    > Did you call this kitchen your laboratory?
- **choice** `?` → `End`
    > Live and drink, food-tinkerer.

### Node `Omonporch`

Omonporch is a fine source of bananas, but I have little to say about self-appointed nobility.

        Claimed authority has a heady aroma, but no broth beneath it. Let us simply appease Asphodel and leave xem to xyr fantasies.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, food-tinkerer.

### Node `Rumbling`

My air-puffed pastry experiment collapsed thanks to that disturbance.

        Whoever is responsible will pay dearly.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, food-tinkerer.

### Node `Klanq`

I have visited the rainbow wood but once, and there I sampled an array of strange foods, one of which allowed me an unusual lens through which to view the world. It was nothing like I had ever experienced, and I imagined such wondrous recipes. I wrote them all down as best I could, of course.

        Sadly, once I returned to my ordinary frame of reference, my scribblings proved impossible to read. So it goes.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, food-tinkerer.

### Node `Porridge`

What you smell is Grit Gate's signature dish. The Porridge is a recipe passed down through generations of Barathrumites, and it is the food that inspired me to pursue my craft. Yes, outsiders quail at the intensity of the scent, for its flavor is as bold as its effects!

        We use cuisine to channel lightning from our bodies! Other recipes may let us breathe fire, or learn the secrets of the Eaters. The Porridge is as precious a part of our legacy as the Barathrum Clock or the foaminator.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, food-tinkerer.

### Node `FoodNetwork`

Oh, it changes by the hour, sometimes the minute. Preserve this, observe that, add anything, taste everything.

        But the starapple of my eye, the Spindle up which I cast my ambitious gaze... is edible vapor. Food that you eat, food that you breathe. Sadly, to date the most I have managed is an herbed saline suspension. Salty air, if you will.

**Choices:**
- **choice** `?` → `VaporAndSalt`
    > Vapor... and salt?
- **choice** `?` → `LuckyPlate`
    > Good luck with your experiments, then.
- **choice** `?` → `End`
    > Well, I should be going.

### Node `VaporAndSalt`

Yes. The flavor, the breathability, all successful, but the barrier between flavor and food is in the calories, and they have yet eluded me. But it is only a matter of time. I am patient, and I am relentless.

**Choices:**
- **choice** `?` → `LuckyPlate`
    > Good luck, then.
- **choice** `?` → `End`
    > I will leave you to it. Live and drink.

### Node `LuckyPlate`

I have no need for luck, but I appreciate your well-wishes nonetheless.

        May your own endeavors drive you as mine drive me. Did you wish to speak of anything else?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, food-tinkerer.

### Node `Kitchen`

Kitchen? You think this a mere kitchen?

**Choices:**
- **choice** `?` → `Kitchen2`
    > It certainly looks like a kitchen.
- **choice** `?` → `Kitchen3`
    > No, of course it's a laboratory, I wasn't thinking.
- **choice** `?` → `End`
    > Why don't I see myself out?

### Node `Kitchen2`

And I suppose the Stilt is a modest church, its great bazaar a junk sale?

        Look about you. Every instrument you see is precision-calibrated, every tool handcrafted and built to last. In this room, sustenance and ingenuity come together to evolve cuisine itself, to shape not this culture alone but, over time, every culture. Is that kind of influence the product of a kitchen? Can a simple clay oven in the flower fields do what we do here? Has every kitchen an indelible influence over Qud?

        *He frowns.*

        Should they? Should we not all?

**Choices:**
- **choice** `?` → `Kitchen3`
    > Yes?
- **choice** `?` → `Kitchen3`
    > No?
- **choice** `?` → `Kitchen3`
    > I'm lost.
- **choice** `?` → `End`
    > *mutter 'live and drink' while backing away*

### Node `Kitchen3`

But perhaps you are right, =player.formalAddressTerm=. Think for a moment.

        Every ingredient in the soup of collective knowledge is a valuable one, and who am I to elevate myself over more humble pioneers? But! All the more reason for us to regard cuisine (and by extension, culture itself) to be a scientific endeavor, an ongoing trial-and-error, a blending of what we know and what we don't know, calling upon reality itself to be our guide.

        You are more insightful than I realized, =name=. Thank you for this discussion. Did you need aught else?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, food-tinkerer.
