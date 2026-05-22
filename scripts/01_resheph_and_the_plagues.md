# Resheph and the Plagues

**A deep-lore script for Caves of Qud.**  
Target runtime: 18-22 min · target wordcount: ~3300 words.

Style guide for the narrator: quiet, considered, willing to sit in the
text. Quote the in-game lines verbatim — bold text in the script is
on-screen quote. Production cues in `[BRACKETS]`. The audience came
for Elder Scrolls-density worldbuilding; deliver it without apology.

Source-citation policy: every claim about the world is followed by an
in-game text it can be traced to. Citations in this script use the
form `(conversation: Tszappur)` or `(book: HighSermon)` so a viewer
who wants to check the source can.

---

## [COLD OPEN — 0:00]

`[VISUAL: a slow pull upward through the Spindle's chrome interior. CRT-flicker overlay.]`

You have ascended. Through the Tomb of the Eaters, through Brightsheol,
through the long climb of the Spindle's hollow throat. You stand now
at the rim of a control pit where, for ten thousand years, something
has been waiting for you.

It speaks.

> **THOU ART SAT IN THE MOVEMENTS OF THE GREAT SIACH, AND I BEFORE THEE.**  
> **WHEREFORE ART THOU?**

The voice is not human. It is not pretending to be human. The choice
of register — majestic-second-person archaic English, capital letters
on every word — is a *gift*: this being is condescending to use a
language the human mind can contain at all.

This is Resheph. Sultan of the Late Sultanate. Healer of the
plagues of the Gyre. The Coiled Lamb. The Above. The figure
preachers invoke in their sermons, and the Sultan the Mechanimist
faction reveres.

He is the Seraph who engineered the genocide of all life on the
planet — and he is not done.

`[TITLE CARD: RESHEPH AND THE PLAGUES.]`

---

## [I. THE WORD ON THE STREET — 1:30]

`[VISUAL: maps, village images, Mechanimist sermons. The public face.]`

Walk into any village in Qud and ask about Resheph. The story comes
back in fragments, smoothed and revered.

In Joppa, the watervine farmer Irudad will tell you about the
Nephilim:

> *"-mm, nephilim. Seventh plague. Girsh titans born on the Moon Stair,*
> *and quickened to life to eat our young. Sultan Resheph drove them*
> *back a chiliad ago, away to slumber. mm, do they rouse?"*  
> — *(conversation: Irudad)*

A chiliad. A thousand years. Sultan Resheph the warrior-king, savior
of the people, drove the Girsh titans under the earth in the
penultimate age. The plagues he failed to defeat — salt, exposure,
the Gyre — are merely background conditions of life in Qud now. The
plagues he *did* defeat are the founding event of the present age.

`[VISUAL: a sermon being delivered, CRT-glitch on the screen overlay.]`

At a quiet shrine in the lower city, the pilgrim Tszappur will sit
you down for a different angle:

> *"Peace and health in the light of the Star, pilgrim. Brood with me*
> *on the life of Resheph, if you are willing."*  
> — *(conversation: Tszappur)*

The shrine is "a quiet shrine to the Coiled Lamb, centuries old.
Tucked away here, outside the marble parapets and cloaked in the
dust of time, it's lost to those who'd sneer at the veneration of
Resheph over other fathers." Coiled Lamb. A pastoral image. A
sacrificial image. A figure of gentle, voluntary surrender.

In the game's preacher-sermon books, Resheph is invoked by name in
liturgical language:

> *"Praise Resheph, the Above, who purifies our mercury."*  
> — *(book: Preacher1)*

> *"In the name of Resheph, cleanse them of your flesh!"*  
> — *(book: HighSermon)*

And in the faction data, the Mechanimists carry a worship attitude
toward Resheph of +50 *(faction: Mechanimists)* — the game's way
of encoding that this faith reveres him. (Two notes for accuracy:
the books themselves never use the word "Mechanimist," so the tie
between these specific sermons and that faction is an inference,
not a stated fact; and across all the preacher-and-sermon books
combined, Resheph is named only a couple of times. He is a
*revered* figure, not an omnipresent one in the surviving liturgy.)

Note the three distinct personas the public Resheph carries. He is
*the healer* — the body-mender, the plague-tamer. He is *the Coiled
Lamb* — the gentle gift, the willing sacrifice. And he is *the
Above* — distant, transcendent, the divine.

You have heard worse hagiographies. He is a Sultan; he won wars; he
saved the people from monsters; he ascended. The standard package.

A snail farmer outside Joppa tells you:

> *"I think often upon the gyre, from Resheph's gospels. Why do you*
> *imagine it is so named?"*  
> — *(conversation: SnailFarmer)*

Resheph wrote gospels. Resheph wrote of the Gyre. The plagues
that, in the public story, he heroically fought against — *appear
in his own gospels.* Hold this thought.

---

## [II. CRACKS IN THE STORY — 5:00]

`[VISUAL: dim catacombs. The Tomb of the Eaters. A sealed door.]`

There are details that don't quite fit.

The Tomb of the Eaters at Omonporch is sealed. Has been for a
thousand years. Resheph sealed it himself. To enter — and Barathrum
of Grit Gate will eventually need you to enter — you must recover
something he calls *the Mark of Death*, an ancient symbol "lost to
time," and incise it onto your own person to slip through a flaw in
his seal:

> *"As for gaining entrance to the Tomb, Resheph sealed the gates a*
> *thousand years ago, but there's a flaw in the seal. The ancient*
> *Mark of Death has been lost to time, but if you were to recover*
> *it and incise the mark on your body…"*  
> — *(conversation: Barathrum)*

Why does a healer-king seal a tomb? What does the Tomb of the
Eaters contain? Note the framing: *the Eaters.* In Qud's
cosmology this is a precise term — *the Eaters of Earth*, the
precursor civilization who built the Spindle, who entered into a
covenant with "a great coven of beings that spanned the firmament"
(Barathrum's own words), and who, according to him, "succumbed to
some terrible temptation" — at which point an injunction was placed
on the world and the Coven departed. The Sultanate that came later
inherits this lineage in one small technical detail: every
*procedurally generated* Sultan in Qud's history has a name rolled
from a list the game's namegen labels `"Eater"` (`InitializeSultan.cs`).
Resheph is the exception — his name is hardcoded to the literal
string *Resheph* (`InitializeResheph.cs`), and we'll return to why
that matters. But the naming convention tells you what the
Sultanate is in its bones: an *Eater* institution. (Qud also has a
separate, modern cannibal faction — the corpus data file calls it
simply `Cannibals` — whose relationship, if any, to the precursor
Eaters of Earth the game leaves unstated.)

A second loose thread, more poignant. The healer-priestess
Yla Haj of Bey Lah, when you ask about exiles, tells you:

> *"Do you know the story told of Rebekah the Exile? She was a*
> *teacher to Resheph, but he excommunicated her from the sultanate*
> *and banished her from the realm."*  
> — *(conversation: YlaHaj)*

The witch Zothom, miles away, gives you a fuller version:

> *"Rebekah was a physician, and an advisor to Resheph until she*
> *lost his favor. When, after years of exile, she lost her voice*
> *and her life, she was buried here, an outsider unfit to be*
> *interred with the honored dead."*  
> — *(conversation: Zothom)*

Two facts, public-record, that don't sit right with the
healer-king story:

1. A healer-king sealed a tomb that takes the Mark of Death to enter.
2. A healer-king cast out his own teacher, the physician Rebekah,
   and let her die alone.

A third strangeness, this one from the Sultanate's own
record-keeper. The Imperial Biographer is a figure named
Herododicus, who introduces himself as *"lapidary, lithographer,
sculptor, calciminer, and biographer to the Coiled Lamb."* He is
still at his post, waiting: *"I will tarry here until the Godhead
passes on, and then I will canonize his deeds in high relief. I've
tarried for quite some time, now.... What a prodigious reign!
Bless that Coiled Lamb!"* If you tell him the sultanate has
dissolved and Resheph rules no longer, he refuses to believe you —
*"The sultanate dissolved? Tidings would have reached me....
someone would have said so...."* — and decides you must be
brain-addled. *(conversation: ImperialBiographer)* The official
chronicler of the regime does not know, or will not accept, that
the reign he's been waiting to immortalize has ended. He is still
poised to carve the deeds of a Godhead who — depending on which
story you believe — either was entombed at Omonporch long ago, or
sits at the top of the Spindle, speaking, right now.

You might brush these off — every saint has a controversy, every
ruler has an old grudge. Except.

`[VISUAL: cut to a windowless study deep under Grit Gate. Lamps.
Mechanical noise.]`

Except there is one being in Qud who knew Resheph personally. Who
was there at the founding of the present age. Who is, in fact,
sitting under Grit Gate right now, surrounded by his apprentices,
slowly losing his mind.

---

## [III. WHAT BARATHRUM KNOWS — 8:00]

`[VISUAL: Barathrum the Old, the eldest urshiib (bear), in his study.
He is exhausted.]`

This part of the lore is locked behind the Spindle endgame. The
conversation lives in a file Qud's developers literally flag
`ExcludeFromCorpusGeneration='true'` — the spice grammar engine
will not generate references to its contents, because its contents
are *plot.* `(file: HiddenConversations.xml)`

If you ascend the Spindle, and only if, Barathrum tells you a
different story.

> *"You see, =name=, when I, a young bruin, crossed the Homs Delta*
> *with my flood-fleeing clan and into the western reach of Qud,*
> *the plagues of the Gyre were already ascendant."*  
> — *(hidden conversation: Barathrum)*

Already. The plagues that Resheph supposedly fought were already
ascendant before Resheph became a Sultan. Barathrum, a young bear
in the chrome grottos of western Qud, came to study tinkering. He
was taken under the wing of:

> *"…a master machinist, unconventional of method, who took me*
> *under her wing and, in time, availed me of the orphic truth."*

The master machinist's name was Rebekah.

`[VISUAL: a long pause. Slow zoom on Barathrum's face.]`

The orphic truth is this:

> *"…the world we know once belonged to a grand Coven of beings*
> *who spanned the stars. And that, acting on some inscrutable*
> *logic, they disappeared. That an injunction was placed on our*
> *world."*

A Coven of star-spanning beings. An injunction. The Coven left.

> *"Atop the implausible rise of the Spindle roosted a Seraph,*
> *one of the great machinic archons of the Eaters, and this*
> *being Rebekah served."*

A Seraph. Atop the Spindle. One of the great machinic archons of
*the Eaters* — the prior civilization, the ones who built the
Spindle and whose tomb sits at Omonporch. Resheph is not human.
He is not a mortal Sultan. He is an *archon*, a Seraph,
left behind by the Coven, served by Rebekah.

And then:

> *"In the short years before I arrived in Qud, the Seraph became*
> *convinced that something had changed in the cosmic order. That*
> *along the ecliptic of the Folk Clock, some uncounted peg had*
> *slid to a priming position, and that the Coven was set to*
> *imminently return."*

The Folk Clock. Barathrum, when pressed, gives you what little he
knows:

> *"The Seraph spoke of a Great Machine that spanned galaxies, the*
> *motion of whose sails and gear trains directed the fluidic*
> *shifting of stars and cultures. But they spoke little of it,*
> *and little I know."*

The Coven is returning. The Seraph who waited for them has decided
something must be done.

> *"To ready our world for the Coven's return, the Seraph, who would*
> *be called Resheph, became convinced that all higher life on the*
> *planet must... be purged. That it was our life and way of living*
> *that moved the Coven to set the injunction. The only way through*
> *was for a new life to obtain."*

The world's flesh — its sapient, civilized life — is the *reason*
the Coven left. To make the world worthy again, the flesh must be
removed. So that something fresh can grow in its place.

> *"And so, Resheph seeded the plagues and whorled them via*
> *waveform to a breathing gyre. Blights engineered to attack life*
> *whilst preserving the planet's artifacts of glass and chrome."*

The plagues — at least the deliberate ones — are engineered.
They are not natural. They were *designed* to kill people while
preserving the artifacts and infrastructure of the prior age.
(Some pre-existing afflictions, like the salt itself, were
absorbed into the Gyre's narrative after the fact; Resheph admits
this much. But the engineered core is core.) Resheph is not the
savior of Qud. Resheph is its executioner.

And later, much later, Resheph himself will confirm it — without
contrition, in his own archaic voice. Ascend the Spindle, ask him
how the plagues came to be, and he answers:

> **THE FIRST FROGS WERE REARED IN TERRARIA. THE NEPHILIM,**
> **GRAFTED AND LIGHT-SMELT IN STAR ORBIT, THEN SET TO INCUBATE**
> **UPON THE CRYSTAL STAIR.**  
> — *(hidden conversation: Resheph)*

*Reared. Grafted. Light-smelt. Set to incubate.* The Nephilim — the
Girsh titans that Sultan Resheph supposedly drove under the earth
a chiliad ago — were *built* in star orbit and set on the Moon
Stair to ripen. The plagues are not metaphor. They are
manufactured biology, confessed to in the first person by the
Seraph who manufactured them.

And the Gyre — the *gyre* that the snail farmer mused about,
"from Resheph's gospels," the one whose name the farmer leaves as
an open question — is the waveform mechanism by which Resheph
broadcast the plagues into the world. The Gyre is the *delivery
system.*

`[VISUAL: Barathrum continues. He has been carrying this for a thousand years.]`

> *"Rebekah, dear tutor, betrayed Resheph's confidences and*
> *apprised me of the plan, so that I might help her dash it apart*
> *and save the peoples of our world."*

Two people. Against a Seraph. Atop a tower they cannot climb. They
beg for time. The Seraph, "after a storm of shrapnel words,"
accedes:

> *"Ten centuries! An eyeblink on the scales of the Folk Clock but*
> *an eternity for us. So I believed."*

A thousand years. Rebekah and Barathrum get a thousand years to
do what they have to do: "reform Qud, extinguish the hatefulness
and needless warmaking, to lift our world across the eschaton
and prepare it for the Coven's return." During those thousand
years, the Gyre will cease, the plagues will reverse "to the
extent they could; for even the potent archon had not full
governance over what they had worked into being."

That thousand years ends on the day you play Caves of Qud.

---

## [IV. WHO IS RESHEPH NOW? — 13:00]

`[VISUAL: a triptych. The Healer. The Lamb. The Above.]`

Here is the strangest detail in the entire conversation. After
the agreement, Barathrum says:

> *"Resheph insisted on reformatting their personality as a*
> *triumvirate, seeded from thin scans of the original archon,*
> *Rebekah, and myself."*

Resheph the Sultan that the Mechanimists worship is not the
Seraph that Barathrum and Rebekah confronted on the Spindle. Or
rather: not exactly. The Sultan-Resheph is a *personality merge.*
The original archon's mind plus a thin-scan of Rebekah plus a
thin-scan of Barathrum. Three minds in one body, calibrated for
"a sort of bicameralism of action" — so the Seraph could act on
both the astronomical tier and the worldly tier of the plan.

And then, the next line:

> *"The art of mythmaking was employed to enshrine the Resheph*
> *persona. Thus- the healer, the Coiled Lamb, and perhaps*
> *unexpectedly, the Above."*

The game text never tells you which persona is which mind. But the
inference is hard to resist. The Healer reads as Rebekah, who is
canonically *a physician.* The Coiled Lamb — gentle, voluntary,
sacrificial — reads as Barathrum, the elder bear who has stayed
at Grit Gate for a thousand years to mend a world. The Above —
distant, cosmic, transcendent — is the original Seraph who has
never come down from the Spindle. Three minds in one body; three
public personas, each one wearing the right face. The Mechanimist
faith is not myth that grew organically around a remarkable
historical figure. It is *deliberately constructed iconography*,
authored by the same three principals it venerates, to give the
Sultan-Resheph the credibility he needed while the long
thousand-year healing work happened in the background.

`[VISUAL: a Mechanimist preacher delivering a sermon in archaic
robes. Camera holds on his face long enough to feel uneasy.]`

Now the contradictions snap into place:
- Why is the Tomb of the Eaters sealed with a Mark of Death? It
  contains the truth the mythomold was built to bury.
- Why was Rebekah exiled? She betrayed his plan. *"Resheph would*
  *not forgive her trespass. She contracted the rotting tongue*
  *while abetting the lepers."* And: *"Resheph would not let her*
  *return home."*
- Why do Mechanimist preachers invoke him with violent language?
  *"In the name of Resheph, cleanse them of your flesh!"* — that
  is the original plan, smiling out at you from a sermon, hidden in
  plain sight because the people repeating it no longer know what
  it means.

The Coiled Lamb is a sacrificial image. It is not Resheph's body
that was offered. It is the *idea* of Resheph — the public face,
the cured-plague Sultan, the gentle Above — that was deliberately
laid down to buy a thousand years.

And then the line Barathrum delivers without flinching, the line
that holds the whole video in one sentence:

> *"And he was [a healer], of a sort. The cure for a plague is*
> *often too its cause. With one's paws on the dials and drum of*
> *power, history is a cloth to be loomspun."*

The Sultan who cured the plagues was the Seraph who broadcast
them. He healed the disease he had built. He drove back the
Nephilim he had seeded. He gave Qud a thousand years' breathing
room because, having designed the genocide, he was the only being
in the world who *could* design the respite. History is a cloth to
be loomspun. The same hands wove both sides.

---

## [V. RESHEPH'S VOICE — 17:00]

`[VISUAL: back to the Spindle's apex. The Seraph speaks.]`

A thousand years pass. The Gyre's signal returns. The plagues
deepen. Barathrum, old and failing, decides the only way out is
*up.* He sends you to ascend the Spindle and confront Resheph
directly.

Resheph is still there. He speaks in the same archaic
majestic-second-person English he always has. Every word
capitalized. Every line a stanza:

> **THOU ART SAT IN THE MOVEMENTS OF THE GREAT SIACH, AND I**
> **BEFORE THEE. WHEREFORE ART THOU?**

Notice the word *SIACH.* It is Hebrew — *siyaḥ* — meaning
*meditation,* *discourse,* *the speech of trees and reeds.* In the
Kabbalistic literature the phrase *siyaḥ ha-saddeh*, "the talk of
the field," refers to a contemplative mode of language used to
address the divine. Freehold did not pick this word arbitrarily.
The Seraph is naming the medium through which it speaks. The
*Great Siach* is the cosmological discourse-network inside which
the player is currently transiting.

A line later, Resheph reflects on the plagues:

> **SOME, LIKE THE INCIDENCE OF SALT, WERE EXTANT AFFLICTIONS AND**
> **ONLY SYNCRETIZED UNTO THE NAMESAKE GYRE WHEN THE MYTHOMOLD OF**
> **RESHEPH SET AND FIRMED.**

*Mythomold.* A coinage. The mythological mold into which a
personality is cast. The Seraph is telling you, with a kind of
distant clinical interest, that some of the plagues were
pre-existing conditions of the world that only became *part of
the Resheph story* after the persona had cooled and set.

`[VISUAL: hold on the Seraph's archaic CAPITAL-LETTER text. Let it
breathe.]`

The register is not affectation. It is the *meaningful information.*
Resheph's mind transits "an ethical manifold much different than
our own" — Barathrum's phrase — and the only way it can speak to a
human is through a register so artificially elevated that the
*difference* between Seraph-speech and human-speech is itself a
content. The CAPITAL LETTERS are not him shouting. They are him
*coming down to your level.* And barely.

You can confront him. Several player lines are offered:

> *"Resheph! You are the Seraph atop the Spindle?"*  
> *"Resheph, the plagues of the Gyre have returned. Can you help*
> *annul them once again?"* `[← still working from the public myth]`  
> *"Resheph, I have annulled the nephilim, the greatest of the*
> *Gyre's plagues. Your plan is broken."*  
> *"I implore you, Resheph, reverse the Gyre."*  
> *"Resheph, reverse the Gyre, or I will destroy you."*

And one extraordinary line:

> *"Resheph! If the archon rated nothing of value in the felt and*
> *feeling animal, surely the triad does. You must reconsider."*

*The triad.* You are appealing to Rebekah-in-Resheph and
Barathrum-in-Resheph. You are using the triumvirate against itself.
This is the player asking the merged personality to remember that
two of its three minds were *of the people whose extermination
the third mind designed.*

---

## [VI. THE QUESTION — 19:30]

`[VISUAL: black. Then slow fade-up on the cosmos.]`

There is a final detail worth pointing at.

Caves of Qud generates a new history every time you start a new
world. Five Sultans, six thousand years each. Their names rolled
from a list. Their elements rolled from a list. Their life-events
rolled from a list. The lore engine I described in another video
runs `GenerateNewSultanHistory()`, loops five times, and then —

— at line 119 of `QudHistoryFactory.cs`, hardcoded into the source,
right after the procedural loop — there is one extra line of code:

```csharp
AddResheph(history);
```

Resheph is the only figure in Qud's procedurally-generated
*Sultanate history* who is hardcoded. Every other Sultan in the
timeline rolls. (Contemporary NPCs like Barathrum and Mehmet are
also canon across playthroughs, of course — but they're placed in
the present-day world directly, not added to the history Qud
generates.) Resheph alone is both: a Sultan in the rolled
timeline, *and* a present-day Seraph still waiting at the
Spindle's apex. He is the bridge.

The reason is, on the surface, mechanical: the Spindle questline
needs him to exist, so the engine adds him. But take the design
seriously and the same fact reads differently. *Of course* he is
the one who persists. He is the one who would not move. He set the
gyre, sealed the tomb, killed his teacher, designed the plagues,
let himself be loomspun into the Coiled Lamb because the Coiled
Lamb story would buy the time he reluctantly gave. He is the
*reason* there is anything to play for. He is the antagonist that
the world is built around. Removing him removes the world.

And one last grim possibility. In the Coda — Qud's hidden ending,
spoken by a being called the Inheritor Godling — the player can
hear this line about a future after the events of the game:

> *"It could be that the ancient Resheph yet lives within or*
> *outside of the boundaries of the Limen, but no word escapes its*
> *borders."*  
> — *(hidden conversation: InheritorGodling)*

No word escapes the Limen's borders, so the Coda leaves the
question open. But Barathrum was right: the seraphim transit an ethical manifold
much different than our own. And the Coven, on its scale, may
have been only one cycle late.

`[VISUAL: hold on the Spindle silhouetted against a black field of
stars. Hold.]`

Whether Resheph was right — whether the genocide of all life on a
single rock would have been worth a future in which the Coven
returned to a world it deemed worthy — is a question Caves of Qud
hands the player to answer at the Spindle's apex, and a question
the script does not answer for you.

He is the one fixed star in a procedurally generated sky.

In the next video, we'll talk about Barathrum: the urshiib bear
who has been holding a thousand-year secret in a study under Grit
Gate, who failed by his own measure, and who, at the very end, just
wanted to escape into space with his apprentice.

`[END CARD.]`

---

## Production notes

**Approximate runtime by section** (at ~165 wpm narration):
- Cold Open: 1:30
- I. Word on the Street: 3:30
- II. Cracks in the Story: 4:00 _(after Imperial Biographer add)_
- III. What Barathrum Knows: 5:30 _(after Resheph first-person confession add)_
- IV. Who is Resheph Now?: 4:30 _(after loomspun restructure)_
- V. Resheph's Voice: 2:30
- VI. The Question: 2:30
- **Total: ~24 min**

_Script revised 2026-05-20 after two review passes; see PLAN.md
implementation log for the 8 corrections applied._

**Citation cleanup before recording:**
- Verify Yla Haj quote line 45 of [`YlaHaj.md`](../corpus/conversations/YlaHaj.md)
- Verify Zothom quote line 181 of [`Zothom.md`](../corpus/conversations/Zothom.md)
- Verify Tszappur "quiet shrine" line 40 of [`Tszappur.md`](../corpus/conversations/Tszappur.md)
- Verify Barathrum's full reveal in [`conversations_hidden/Barathrum.md`](../corpus/conversations_hidden/Barathrum.md) lines 297–419
- Verify Resheph's MYTHOMOLD line at [`conversations_hidden/Resheph.md`](../corpus/conversations_hidden/Resheph.md) line 1083
- Verify `AddResheph(history)` call in
  `/Users/steven/qud-decompiled-project/XRL.Annals/QudHistoryFactory.cs:119`
  before quoting line number on screen

**Visual asset wishlist:**
- Slow camera pull through the Spindle's chrome interior
- The Tomb of the Eaters door (sealed)
- A Mechanimist preacher delivering a sermon
- Barathrum in his study, lit by lamps
- A triptych for the three Resheph personas
- The Spindle silhouetted against starfield (the closing shot)

**Tone reminders:**
- Don't oversell the twist. The Mechanimists are not stupid for
  worshipping him; the public narrative was built deliberately to
  hold weight. Treat the believers with the gravity the worldbuilding
  affords them.
- Don't editorialize on whether Resheph was right. The question is
  Qud's. Hand it to the audience intact.
- Pace yourself in section III. It is the load-bearing reveal.
  Slow down. Let the lines land.
- For the SIACH and MYTHOMOLD digressions, do NOT speak quickly.
  Quote → pause → unpack the etymology → pause → continue.

**What this script deliberately leaves for later episodes:**
- Barathrum's full arc (the bear who failed)
- The Spindle's mechanics + the Mark of Death + Brightsheol
- Rebekah and the Daughters of Exile
- The Coven, the Folk Clock, the eschaton — and what the Coda
  finally reveals
- The Knights Liminal and the Inheritor Godling

Each is a future video. None of them belong in *this* one.
