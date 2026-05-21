# Conversation: `Irudad`

_Inherits: `BaseSlynthMayor`_

_1 start(s), 23 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

-mm. Mmm? =player.FormalAddressTerm=?

				*Elder Irudad smiles.*

				Live and drink. Come in- come sit 'neath the cool shade, 'cross a pillow there. And welcome to Joppa.

				You may drink of our freshwater, too, and quench your thirst.

**Choices:**
- **choice** `?` → `FinishedRedrock`
    > I'm back from Red Rock with the corpse of a pale spiderling. Elder, would you examine it?
- **choice** `?` → `Joppa`
    > What is this place, Joppa?
- **choice** `?` → `Wares`
    > Do you sell wares here?
- **choice** `?` → `Work`
    > I'm looking for work.
- **choice** `?` → `WorkAfter`
    > I'm looking for work.
- **choice** `?` → `GyreReminder`
    > Can you tell me about the Gyre and the Girsh nephilim again?
- **choice** `?` → `Stiltbound`
    > What can you tell me about the Six Day Stilt?
- **choice** `?` → `Barathrumites`
    > Argyve wants me to meet the Barathrumites.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Start`

-mm. Mmm? =player.FormalAddressTerm=.~
				*Elder Irudad smiles.*~
				*Elder Irudad smiles.*

				Come in- come sit 'neath the cool shade, 'cross a pillow there.~
				*Elder Irudad smiles.*

				Live and drink, =name=. Come, sit with me.

### Node `Joppa`

-this? The oasis-hamlet. 'Neath the shelf of the world. A million breaths of salt the wind heaves over the Great Salt Desert Moghra'yi. And to the east, the rotting jungles of Qud.

				Here in the crack between the two, watervine can grow, and we grow it. mmm, =player.formalAddressTerm=.

**Choices:**
- **choice** `?` → `Qud`
    > Can you tell me about Qud?

### Node `Qud`

-mm, there? Land slopes up and is toothed in chrome steeples, ageless things. Looming over the old-earth tunnels, pillowed in rotting jungle and fungus groves. And broken against the mounts of the north, they are, in the shadow of the Spindle...

				There are people, friends, communities. And friends-to-noone, too. History is thick as the high salt sun, =player.formalAddressTerm=, and where the past is ground up like matz meal, a mix of life sets in.

				-mm, adventurous ones set off for their own splinter of artifact. To both Fates, life and death...

### Node `Wares`

-here? Speak to my daughter through the east door, for herbs. And sitting Tam in the southeast has all manner of trinket, against his chests o' drawers.

### Node `Work`

-mm, work? The farmers are plagued by cave vermin. You might speak to Mehmet o' there, by the southern watervine patch.

				And Argyve, too, =player.formalAddressTerm=. The tinker. Always looking for trinkets to wire between, heh. Go through his hut of sheet metal, to the southwest.

### Node `WorkAfter`

-mm, work? Try Argyve, =player.formalAddressTerm=. The tinker. Always looking for trinkets to wire between, heh. Go through his hut of sheet metal, to the southwest.

### Node `Stiltbound`

-ahh, mm, such spectacle. The statues within, a revelation to the eyes. Chandlers enough to drain your skins dry 'twixt Shallows and Beetle Moon.

### Node `Barathrumites`

-mm, Barathrumites. Strange draft o'those bearfolk. They, mm, hah. They care not overly for outsiders. I hope Argyve sold you not a better welcome than you'll have.

### Node `FinishedRedrock`

-this? Oh? Oh...

				*Elder Irudad pauses for several minutes.*

				Warted leg? mm. Foul smell of sour gum? mmm. Moon and sun....

				A girshling? This is a girshling.

**Choices:**
- **choice** `?` → `Girshling`
    > What's a girshling?

### Node `Girshling`

Creature of plague, =player.formalAddressTerm=. mmm. This one...

				*Elder Irudad pauses.*

				This one covered in slick and muscled out the bilge hose of sleeping Agolgot, in the cave under the Cloaca...

				-mm, but here? Girshling this far west? There must be hundreds for one to reach... mm, does the Gyre widen again??

**Choices:**
- **choice** `?` → `Gyre`
    > Gyre?
- **choice** `?` → `GyreWight`
    > I talked to a strange figure next to the girshling.
- **choice** `?` → `GyreWight`
    > There was a strange figure shadowing the creature...
- **choice** `?` → `Defanged`
    > I noticed the creature has had its fangs removed.

### Node `Gyre`

*Elder Irudad pauses.*

				-mm, plagues. Of our great grandsires many-times-over. Salt, darkness, svardym-frog... Girshling.

**Choices:**
- **choice** `?` → `Agolgot2`
    > ...

### Node `Agolgot2`

*Elder Irudad pauses.*

				-mm, =player.formalAddressTerm=. Do not like to sour the air with a harsh word! But this tiding bites my liver like acid. mm, must ask Nima for an elixir of yuckwheat...

**Choices:**
- **choice** `?` → `GyreWight`
    > I talked to a strange figure next to the girshling.
- **choice** `?` → `GyreWight`
    > There was a strange figure shadowing the creature...
- **choice** `?` → `Defanged`
    > I noticed the creature has had its fangs removed.
- **choice** `?` → `Apology`
    > I am sorry to cause pain, Elder.

### Node `GyreWight`

-mm, oh? In dyed robes, flashing gestures of hand? And ranting about pipe milk? A gyre wight, must be. They about worship the Girsh nephilim as gods.

**Choices:**
- **choice** `?` → `Nephilim`
    > Girsh nephilim?

### Node `Nephilim`

*Elder Irudad pauses.*

				-mm, nephilim. Seventh plague. Girsh titans born on the Moon Stair, and quickened to life to eat our young. Sultan Resheph drove them back a chiliad ago, away to slumber. mm, do they rouse?

### Node `Defanged`

-mm, oh? A gyre wight, must be. They bind the teeth right up to their own gums, to make a show for the Girsh nephilim.

**Choices:**
- **choice** `?` → `Nephilim`
    > Girsh nephilim?

### Node `Apology`

-mm? No, =player.formalAddressTerm=! Your finding is rich in value to us. We are poor farmers, and sharpen our vinereapers is all we can do. But others? Perhaps more.

				Take these prickly-boons as thanks. mm, I will not soon forget this, =name=. Leave me now to muse, kindly...

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
    - _part: `QuestHandler` (QuestID=What's Eating the Watervine? Action=Complete)_
    - _part: `ReceiveItem` (Blueprints=UbernostrumTonic,Fixit Spray,SalveTonic,SalveTonic,SalveTonic Identify=UbernostrumTonic,SalveTonic)_

### Node `GyreReminder`

-mm, yes? Plagues, a chiliad old. Seven such: girshlings, darkness. mm, svardym-frog...

				Ah, nephilim, too, =player.formalAddressTerm=. Girsh titans who eat the young of kith and kin. Sultan Resheph drove them under the earth, but do they stir??

### Node `SlynthRequest`

-mm, oh? You're wondering if they might come to Joppa, then?

### Node `SlynthRequestAccept`

mm, I am for you, =name=. Any friend of yours is too a friend of Joppa, and if those friends desire shelter I wouldn't dare turn them away. I only hope these lilypad-folk have the patience for a farmer's life. -mm, not as exciting here as it was in the Palladium Reef.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, Elder.

### Node `SlynthRequestReject`

-mm, blessings upon your generous heart, =name=. I mean no slight to these slynth, but it is too great a favor you ask of the people of Joppa.

### Node `SlynthAbout`

Have you spoken to the slynth, =name=? I am curious to hear what destination they choose.

### Node `SlynthArrived`

-mm, your luminous friends are settling in quite well.

				There is yet a pall of ennui among some, but such is the case for any party of brave migrants. Ah, they will find their ground or their path, all in time. Some farmers show some small discomfort but that will pass in time.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, Elder.

### Node `SlynthSettled`

-mm, ah, =name=. Come see how the slynth have become a part of Joppa!

				Some cared not for the slow pace of our lives and struck out on their own, and with their thews and wits I have no doubt they will live to find purpose. mm, others are welcome to grow and flourish here in our marshes.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, Elder.
