# Conversation: `MechanimistLibrarian`

_Inherits: `BaseSlynthMayor`_

_0 start(s), 9 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Live and learn, wanderer. Have you come across any books or scrolls in your travels? Do you care to donate one to the cathedral library? Whenever you return, you may speak to me and read anything you've donated.

**Choices:**
- **choice** `?` → `Start`
    > Yes.
    - _part: `LibrarianGiveBook`_
- **choice** `?` → `Where`
    > Where is the library?
- **choice** `?` → `What`
    > What use is a library in this salt den? Or in the marshes, strangled by wild plants and poisoned by the glow? Wouldn't a stash of vinereapers serve us better?
- **choice** `?` → `End`
    > Not today. Live and drink, chronicler.

### Node `SlynthRequest`

You imagine they will thrive here at the Stiltgrounds, among the faithful?

**Choices:**
- **choice** `?` → `SlynthRequestAccept`
    > I do.

### Node `SlynthRequestAccept`

This wouldn't be the first time the Stiltgrounds have hosted refugees, =name=, and make no mistake: it is a burden upon the church, Catechists and Protectors in particular. But your words echo loud in our hearts as our hallways. Some in our number will see the slynth as the chosen of chosen, and if I speak to them first, everyone else will take it as Shekhinah's will. Which, arguably, it would be. Tell the slynth that the Mechanimists will have them.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, Sheba.

### Node `SlynthRequestReject`

I mean no slight to these slynth folk, =name=, but the Stiltgrounds have hosted refugees before and it is a substantial burden upon our stewards. Our resources and space are scant, and I must request that you find another home for them. May the Kasaphescence shine upon them, and you, in this endeavor.

### Node `SlynthAbout`

=name=, bless you. Have you brought tidings of the slynth?

### Node `SlynthArrived`

Praise be to Shekhinah, =name=, your slynth friends are hard workers and quick learners!

        I can't help but feel a bit concerned at their ethic, and who in the church might take advantage of it. I hope to foster an interest in reading in them if I can, before they are taught incuriosity. Perhaps a book club?

**Choices:**
- **choice** `?` → `Start`
    > My thanks, chronicler.

### Node `SlynthSettled`

Live and learn, =name=.

        The slynth are settling in as folk do. I see some flank the Priests and Catechists with empty eye, but some have proven hungry for knowledge. I have established a weekly Canticle study group, and its numbers grow each meeting.

        Praise be to Shekhinah for this meeting, =name=.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, chronicler.

### Node `Where`

Oh, we're in but the first phase of its foundation. The church has amassed a splendid collection of scripts through the years. Glorious Shekhinah, praise be upon Him, gifted us with several caches. The eremites work day and night reproducing them in the scriptorium, and I have taken it upon myself to beseech travelers, for the rarest finds often come from the least likely places.

**Choices:**
- **choice** `?` → `Start`
    > I will donate a book.
    - _part: `LibrarianGiveBook`_
- **choice** `?` → `What`
    > What use is a library in this salt den? Or in the marshes, strangled by wild plants and poisoned by the glow? Wouldn't a stash of vinereapers serve us better?
- **choice** `?` → `End`
    > Live and drink, chronicler.

### Node `What`

You share the pessimism of my kin, and several of the priests as well. My heart hears you, but listen to my words, and maybe you will come to feel as I do.

        To devalue wisdom is to devalue the Kasaphescence. She shines in the void, refracting light, illuminating those around her. So does the written wisdom of our elders.

        The machinery of chromium is complex in its divinity. Don't we do a disservice to our Fathers when we remain ignorant of it, of our past, of our future? Don't we deserve the joy of knowing? Bless Eschelstadt II, first Child, for he believes as I do.

**Choices:**
- **choice** `?` → `Start`
    > I will donate a book.
    - _part: `LibrarianGiveBook`_
- **choice** `?` → `Where`
    > Where is the library?
- **choice** `?` → `End`
    > Live and drink, chronicler.
