# Conversation: `Goek`

_Inherits: `BaseSlynthMayor`_

_0 start(s), 16 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Live and drink, friend. rrk come to the Yd, shared together. Feel safe and free as woodsmoke.

**Choices:**
- **choice** `GoekGreetingsChoice` → `Greetings`
    > Greetings, Goek!
- **choice** `GoekWhoChoice` → `Who`
    > Who are you?
- **choice** `GoekToweringChoice` → `Towering`
    > You tower over every other frog I've seen. Are you svardym?
- **choice** `GoekPipesChoice` → `Pipes`
    > These shining pipes! What are they?
- **choice** `GoekFreeholdChoice` → `Freehold`
    > What can you tell me about Yd?
- **choice** `GoekEndChoice` → `End`
    > Live and drink.

### Node `SlynthRequest`

rrk knows of the glow-hats! Yd-friends see glimpses at night, about the reef.

**Choices:**
- **choice** `?` → `SlynthRequestAccept`
    > If you would have them, I ask that you grant them sanctuary.
- **choice** `?` → `SlynthRequestReject`
    > If you would have them, I ask that you grant them sanctuary.

### Node `SlynthRequestAccept`

Boon-friend asks a friend-boon, and what boon is friend! rrk welcome slynth to an Yd, be safe and free as woodsmoke.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, Goek.

### Node `SlynthRequestReject`

Ah! rrk would grant you this boon, rrk would. Were not for the unspoken cries of future-kin, free as woodsmoke but no more safe so longer. rrk would and cannot.

### Node `SlynthAbout`

rrk wonder of the glow-hats. Which wind will blow.

### Node `SlynthArrived`

Greetings, =player.formalAddressTerm=! How arresting of the glow-hats arrival, much to do. rrk soothe Mak, Bep, Krka, look stores, still much slime and sweat to pool below rrk. Enjoy helpful toil!

**Choices:**
- **choice** `?` → `Start`
    > My thanks, Goek.

### Node `SlynthSettled`

All is well, =name=! Trials make for overcoming, and done together.

        rrk can tell the sky dark and not know. Visit and witness! Glow-hats enliven the night, safe and free. Slynth-home is Yd.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, Goek.

### Node `Greetings`

*reeeeeps joyfully*

        Greetings, =name=! Live and drink, friend.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Who`

rrk is called by dwellers Goek. rrk is a dweller here, too, and before then, a builder of place. Goek, Geeub, Mak and Many Eyes build a new Yd in the reef, hundreds of years.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Built`

rrk did before then, but rrk all build it now.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Towering`

rrk is svardym like the hatchling from the egg, but wound down the chute of years in hundreds, and grown so long and warty! rrk was a hatchling once, cries to think on it!

**Choices:**
- **choice** `?` → `Gyre`
    > Aren't the svardym one of the Gyre plagues?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Gyre`

Yes rrk was once, "plague" in the sky hundreds of years. Not so now. Longtime rrk, Geeub, Mak hide in the sponge and eat lice. When find Many Eyes, rrk and friends built the Yd. Joyful helping!

**Choices:**
- **choice** `?` → `OtherPlagues`
    > Do you know anything of the other plagues?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `OtherPlagues`

Plagues bloom a thousand year then die back, shrink under the earth-sponge or move here and east. Vanta, girshling, rot die. rrk the hatchling once saw the Nephilim loom! rrk frightened and hid inside a sponge for thirty moons.

**Choices:**
- **choice** `?` → `OtherPlagues`
    > Do you know anything of the other plagues?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Pipes`

Water and gas piped through the Yd to feed the plants, dwellers, and machines! Dwellers blew the glass in hues like the prism perch, to look pretty. Shared together. Joyful helping!

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Freehold`

*reeeeeps joyfully*

        Yd shared together. rrk walk and feel safe and free as woodsmoke. Here, there through the corals. Under the pipes.

        Great pond and reef air, eat starapple and drink, see pattern on the bright slugs.

**Choices:**
- **choice** `?` → `Freehold2`
    > ...

### Node `Freehold2`

rrk read the signs and descend the stairs. rrk breathe the water smoke and sit on starfish.

        Visit hovels, meet friends Mak, Geeub, Bep, Krka, Une, Tilli, farmer Rokhas, and every rest!

        rrk rrkself.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.
