# Conversation: `Tam`

_Inherits: (default: BaseConversation)_

_1 start(s), 4 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

=player.apparentSpecies=? We are greeted! What do you desire?

**Choices:**
- **choice** `?` → `WhoIsTam`
    > I am =name=. Who are you?
- **choice** `?` → `Joppa`
    > Do you live here?
- **choice** `?` → `AboutTheDromad`
    > What kind of creature are you?
- **choice** `?` → `End`
    > I desire nothing. Live and drink.

## Nodes

### Node `WhoIsTam`

It is a pleasure to know this, =player.apparentSpecies= =player.formalAddressTerm= =name=! I am Tam.

### Node `Joppa`

Joppa is my home, yes.

				I walked Moghra'yi in the caravans of my brethren and the saltback, but upon meeting Elder Irudad, knew at once to settle down here. You will understand, =player.formalAddressTerm= =player.apparentSpecies=, if you speak to him.

### Node `AboutTheDromad`

I am dromad, =player.apparentSpecies= =player.formalAddressTerm=. Some say saltstrider. Do you know this?

**Choices:**
- **choice** `?` → `AboutTheDromad2`
    > I do.
- **choice** `?` → `AboutTheDromad2`
    > I do not.

### Node `AboutTheDromad2`

My people have walked the salt for thousands of years, meeting every creature that lives and thinks. From Pale Sea to the marsh of Joppa, and under the Hanging Hills, our chests are drawn.
