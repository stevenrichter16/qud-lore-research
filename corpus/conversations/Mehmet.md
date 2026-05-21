# Conversation: `Mehmet`

_Inherits: (default: BaseConversation)_

_2 start(s), 7 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `RedrockNews`

Live and drink, =name=. Any news from Red Rock?

**Choices:**
- **choice** `?` → `BackFromRedrock`
    > Yes. I found the vermin and bits of gnawed watervine. I carry one's corpse with me.
- **choice** `?` → `Aye`
    > None yet.
- **choice** `MehmetIntroduce`

### Start `Welcome`

Live and drink, =name=.~
				Taste what on the wind today, =name=?~
				Moon and sun, =name=.~
				I can taste lime, =name=. And mayhaps gallium?~
				Aye, the pest-vanquisher! Live and drink, =name=.

A waterhand? Aye. Live and drink, traveller.

**Choices:**
- **choice** `MehmetIntroduce` → `Name`
    > I am called =name=.
- **choice** `?` → `Village`
    > Can you tell me about your village, Joppa?
- **choice** `?` → `Work`
    > I am in search of work.
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Name`

Mehmet, the tongue says. Live and drink, =name=.

### Node `Village`

Watervine farm in the lap of the marsh. You've sucked the moisture out a vinewafer, yea? We tend the plant here.

**Choices:**
- **choice** `?` → `VillageMore`
    > ...

### Node `VillageMore`

Wind off the Great Desert cools a touch and gives up moisture. Just enough. A tongue can taste a hundred kinds of wind, y'know?

				Anywhile, that's where my wandering mind goes. More's about Joppa I say speak to our Elderfriend. Irudad. Up northwise the path.

### Node `Work`

Aye? I have it, then.
				
				Somethin' is eating our watervine, 'round Beetle Moon. Q-ruun says he saw a creature, spider-like, slinking in the brine. But no cave spider would dare get so near Warden's stomps.
				
				I tasted a bit of red fleck in the pool. Shale, like we find in the soil by Red Rock...

**Choices:**
- **choice** `?` → `WorkMore`
    > ...

### Node `WorkMore`

Hike there, will you? To Red Rock. Just about two parasangs north of Joppa.
				
				Kill the vermin and bring one's corpse back, for seein' what it is. Elder will take care to pay you after, waterhand.

**Choices:**
- **choice** `?` → `End`
    > I will do as you ask.
- **choice** `?` → `Start`
    > I'm not interested.

### Node `Aye`

Aye.

### Node `BackFromRedrock`

Oh? Oh. *Mehmet pauses.*

				Don't like the look o' that thing. Best bring it to Elder. Hut's northwise up the path.

**Choices:**
- **choice** `?` → `End`
    > As you say.
