# Conversation: `Nuntu`

_Inherits: `BaseSlynthMayor`_

_1 start(s), 16 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

Be ape-still and muse, wanderer, and welcome to my village, Kyakukya. Have some mulled mushroom cider!

**Choices:**
- **choice** `?` → `Ape`
    > You are... an albino ape.
- **choice** `?` → `Village`
    > Why do you call it "your" village?
- **choice** `?` → `Kyakukya`
    > What can you tell me about Kyakukya?
- **choice** `?` → `Work`
    > Is there work to be found here?
- **choice** `?` → `Joppa`
    > Have you heard news of girshlings on Qud's surface? The watervine farmers of Joppa confirm it is true.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Service`

I am at your service.

### Node `Ape`

Correct!

### Node `Village`

Ah, bad habit. It's a possessive feeling I should work to scrub myself of, perhaps?

				But I am its mayor, and I have been for some time. You see, years ago I deserted my people. We were of two different minds -- they desired nothing but to bludgeon everything to death, while I asked, "What is the nature of this thing we bludgeon? Or of the act itself?"

				Recognizing that my answers lay elsewhere, I cast myself into the swell of the wilds, as a sailor from Perth with no windweird casts their ship to the whims of the Pale Sea!

**Choices:**
- **choice** `?` → `Village2`
    > *continue listening*

### Node `Village2`

Some years later and twenty ago, I came upon these mushrooms huts and their goodly inhabitants. They are a people full of earthen poetry, and I was charmed by the warmth they welcomed me with. Surely, I owed my acceptance at first to the countenance I share with their mighty god, but they soon grew to love me, and I them. I've remained here ever since in contemplation of those questions that first stirred in me all those years ago.

### Node `Kyakukya`

We're watered by the river spray -- we pluck the fruit of the wood, and we hunt. The worshippers of Oboroqoru whittle and brood, too. They will pay you no mind unless you ask of them. Here you can be with friends, or muse alone. 
												
				If it's trade goods that interest you, take a gander at Yurl's wares in the northwest corner. The odd one Crowsong's, too, if you can scry them in the bush.
				
				I must warn you, however; cast no villain's shadow on these grounds. Warden Indrix will be watching.

**Choices:**
- **choice** `?` → `Yurl`
    > Who is Yurl?
- **choice** `?` → `Crowsong`
    > Who is Crowsong?
- **choice** `?` → `Indrix`
    > Who is Indrix?
- **choice** `?` → `Service`
    > I have some other questions.

### Node `Yurl`

Yurl is a harmless cucumber vine. They came to Kyakukya a few years ago after the last Consortium chandler, a wicked little hyacinth named Plysago, suffered something of an... accident. In Tarotep's defense, Plysago shouldn't have berated someone with claws so close in resemblance to pruning shears. At any length, Yurl stocks a plethora of goods; you will be satisfied with your visit.

### Node `Crowsong`

Oh, another of our dwellers. I won't speak to what Crowsong's deal is. Best you find them and ask yourself.

### Node `Indrix`

Warden Indrix is one of the most ferocious warriors I've ever met. Once upon a time, he and his brothers gorged themselves on the flesh of beasts by starlight, but now I count myself lucky to call him my warden. Some believe he is of sour kind, though I assure you, he's but a victim of his goatish nature.

### Node `Work`

A waterhand, you are? Speak to my friend and warden Indrix. You'll find him patrolling the village.

### Node `Joppa`

As far west as Joppa, you say? Oh, grim! Yes, we found the remains of pale-things in the mouth of Svy. Does the Gyre widen again? Hrmmmm.

### Node `SlynthRequest`

I don't imagine you brought me this information merely to observe. Are you suggesting that these slynth might take up residence here in my village?

### Node `SlynthRequestAccept`

Coming from anyone else, =name=, I might refuse outright. Housing recently-sentient refugees is no mean favor, I think you'll agree. My people are slow to trust, as well, so I fear that the slynth may feel unwelcome for some time. But then, grafted branches grow the best starapples, do they not? Yes, your lilypad friends are welcome here if they wish.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, mayor.

### Node `SlynthRequestReject`

Had I no responsibility to represent my people, I might accept out of the goodness of my own heart alone. Sadly, I do not consider my heart, or even my mind, to be more important than my duty. Perhaps if you were a more renowned figure among my people, I would reconsider.

### Node `SlynthAbout`

Have the slynth yet to choose a destination, =player.formalAddressTerm=?

### Node `SlynthArrived`

Never has Kyakukya seen such bustle. These slynth are seem to be as good citizens as any, but I am at my limit with the stress of keeping track of everything.

				Please check in again after some time, when I have my wits about me once again.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, Mayor.

### Node `SlynthSettled`

Greetings once again, =name=. I am pleased to report that the settling-in of the slynth has gone well, more or less. The villagers are yet wary, but as some slynth have joined in the rituals and worship of Oboroqoru that wariness has waned somewhat.

				They've settled in across the village over time. Crowsong has taught the basics of hunting to a select few, and I'll be teaching a cooking class once I can wrest aside the time.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, Mayor.
