# Conversation: `Mafeo`

_Inherits: (default: BaseConversation)_

_1 start(s), 12 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Post Arms`

Such interesting times we inhabit, =name=!

        Good to see you well. Is there anything you need?

**Choices:**
- **choice** `?` → `TombQuest`
    > I must enter Brightsheol through the Tomb of the Eaters.
- **choice** `?` → `GuestKlanq`
    > What do you think of the situation?
- **choice** `?` → `End`
    > Not at this time. Live and drink.

## Nodes

### Node `Start`

I always knew this part of our story would come. Our efforts today determine the genre of the tale we tell. Is this a triumphant epic, or a tale of woe?

        Fight well, =player.formalAddressTerm=.

**Choices:**
- **choice** `?` → `End`
    > I will.

### Node `GuestKlanq`

What novelty, to shelter the mysterious Klanq! I have heard no stories of this tinker-fungus that could be described as dull, though ‘calamitous' could apply to more than one.

        My mind tells tales of what might be brewing in the basement, but I am quite relieved to be out here rather than down there.

**Choices:**
- **choice** `?` → `End`
    > So they do. Live and drink, Mafeo.

### Node `TombQuest`

Coming from anyone else, I would ask that further japery be left to me.

        But from you? I wouldn't startle to see you return wearing a Sultan's burial mask, having destroyed half a dozen invincible cherubim in the doing. Fates be with you.

**Choices:**
- **choice** `?` → `End`
    > I thank you. Live and drink.

### Node `Start`

Welcome to Grit Gate, =factionaddress:Barathrumites=. Care to enhance the quality of your stay with a wise purchase?

**Choices:**
- **choice** `MafeoGolgotha` → `Golgotha`
    > I have been tasked to travel to Golgotha.
- **choice** `MafeoBethesda` → `Bethesda`
    > Do you know anything about Bethesda Susa?
- **choice** `MafeoOmonporch` → `Omonporch`
    > What do you know about Omonporch and the self-appointed Earl?
- **choice** `MafeoRumbling` → `Rumbling`
    > Did you feel that rumbling, Mafeo?
- **choice** `MafeoKlanq` → `Klanq`
    > Have you ever met Pax Klanq?
- **choice** `MafeoWhat` → `WhatWares`
    > What wares do you sell?
- **choice** `MafeoWhere` → `GritGate`
    > What is this place?
- **choice** `MafeoWho` → `AboutTheQuillbear`
    > What kind of creature are you?
- **choice** `?` → `End`
    > Live and drink, =pronouns.formalAddressTerm=.

### Node `Golgotha`

My condolences to your sense of smell, =player.formalAddressTerm=.

        Golgotha is an execrable place in more ways than one, and I would advise you not to visit without a healthy stock of yuckwheat and honey. If you can cook, a meal with yuckwheat may banish a disease before it comes into its own. Bring salves or urberries, too, and mind your feet in the Cloaca.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Mafeo.

### Node `Bethesda`

Bethesda Susa? Lovely, but a bit dangerous for a holiday destination. You'll want to bring bandages and warm clothing. Why not take a look at my stock in case something suits you?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Mafeo.

### Node `Omonporch`

It's a lovely place, and the bananas are delicious.

        As for the so-called Earl, well. I'm loath to recognize nobility to begin with, and I cannot decide whether Asphodel claiming xyr own title is better or worse than if xe inherited it.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Mafeo.

### Node `Rumbling`

Nothing short of explosives or heavy equipment could have made such a sound.

        Be ready for the worst, =player.formalAddressTerm=.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Mafeo.

### Node `Klanq`

The Rainbow Wood is a fair bit too dangerous for a casual promenade, but nothing compares to its beauty. Once, I viewed it from above by means of a gyrocopter, and I will never forget the sights that I saw.

        Nor will I forget crashing to the ground because the gyrocopter broke, but every adventure has its complications, wouldn't you say?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Mafeo.

### Node `WhatWares`

Oh, I sell whatever sundries that meet my standards of quality, with some measure of curation. I try to ensure that my shelves carry a bit of many things, but you can count on finding more than enough ammunition and a few recoilers that can lead you back here in difficult times.

        If you have anything in need of identification or repair, I can take care of that for you for a few drams as well.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Mafeo.

### Node `GritGate`

Why, this place is Grit Gate! O the vaulted halls, the glint of chrome, the gentle hum of chain turret emplacements!

        There's nowhere like Grit Gate in the whole of Qud, =player.formalAddressTerm=. I've journeyed in my comparatively short time, but I always return here. The very air buzzes with knowledge, as well as quite a few other things.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Mafeo.

### Node `AboutTheQuillbear`

We are called the Urshiib, =player.formalAddressTerm=.

        Our kind are smarter than the average bear. Sharper, too, and a bit more handy.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, Mafeo.
