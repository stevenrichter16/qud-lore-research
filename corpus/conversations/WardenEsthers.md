# Conversation: `WardenEsthers`

_Inherits: (default: BaseConversation)_

_1 start(s), 5 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

Live and drink, traveler. Welcome to the Stilt.

**Choices:**
- **choice** `?` → `Praise`
    > Praise be to Shekhinah! O, sovereign Fathers... at last, I am here!
- **choice** `?` → `Huh`
    > This is the Six Day Stilt, huh. It's... colossal, beautiful. I see why the chrome stewards gather here.
- **choice** `?` → `Folks`
    > So... many... folks....
- **choice** `?` → `True`
    > Is it true what they say? That it's a petrified kraken?
- **choice** `?` → `Bazaar`
    > What a grand bazaar! What's in each of these tents?
- **choice** `?` → `End`
    > Live and drink, wardens.

## Nodes

### Node `Praise`

You are among friends here, pilgrim. Stay peaceful.

### Node `Huh`

Then you're not of the faith =player.reflexive=, huh? Me neither. Do go inside, though. She's a beauty. Got dyed glass high in her rafters, she does. And two marvelous carvings on the wings. Plus a light-sculpture of a god. Hear the sermon, too, as you like. The high priest is persuasive, but not half as persuasive as the cathedral herself. In beauty there is power, you know.

      Either way, while you're in the cathedral or on the Stiltgrounds, stay peaceful.

### Node `Folks`

Aye, aye. The clamor of it all can overwhelm.

      The glowcrows say 'twas a bird-god who taught folks to gather like this, in large flocks. So blame birds.

### Node `True`

Who knows? I've wondered it myself. Sometimes she'll catch my eye, when the moon's silver-bright, and she's there bearing down on the flats.

      Whatever she is, she's gigantic. And old. Real old. Way older than the cathedral the Mechanimists built inside her.

### Node `Bazaar`

Are you mad? You think I keep a tally of every shopkeeper that steps foot on the Stiltgrounds? They come and go as they please. You've got merchants of all types here. Winesellers, honey hawkers, bookbinders, cobblers.

      Have a look around for =player.reflexive=. Following the road around the Stilt. There's tents the whole way round.
