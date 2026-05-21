> ⚠️  **SPOILER WARNING.** This conversation is in `HiddenConversations.xml`,
> which the game flags `ExcludeFromCorpusGeneration='true'`. Contents may
> include endgame branches (Spindle ascent, Coda, late-quest reveals).

# Conversation: `InheritorGodling`

_From HiddenConversations.xml_

_Inherits: (default: BaseConversation)_

_4 start(s), 29 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `CovenantWelcome`

Hie, pather. Hear tell of the ancient Reshephs, how their foibles led to our nowaday.

**Choices:**
- **choice** `?` → `Covenant Story`
    > Tell me the story.
- **choice** `?` → `End`
    > I must decline.

### Start `ReturnWelcome`

Hie, pather. Hear tell of the travails of our precursors, how they led to the Freeholds of nowaday.

**Choices:**
- **choice** `?` → `Return Story`
    > Tell me the story.
- **choice** `?` → `End`
    > I must decline.

### Start `StarfarerWelcome`

Hie, pather. Hear tell of ancient journeying, how the stars beckoned and yet beckon.

**Choices:**
- **choice** `?` → `Starfarer Story`
    > Tell me the story.
- **choice** `?` → `End`
    > I must decline.

### Start `AccessionWelcome`

Hie, liquid mind. Absorb you tales of the creatures before, how their rise and fall gave way to your ascension to wanderer-state.

**Choices:**
- **choice** `?` → `Accession Story`
    > Bloop, blorp. (Proceed.)
- **choice** `?` → `End`
    > Glub. (I must decline.)

## Nodes

### Node `Covenant Story`

It begins in a time before the Limen and its vanguard, before the ascension, when the spire rose unchallenged and unascended. The hollowers who committed their work to emptying our world were long gone, but Reshephs laid claim to the baffled ground in their place. Even as their holdings withered, they held on.

        By the time of the last Resheph, little remained of their works, less of their glory.

**Choices:**
- **choice** `?` → `Covenant2`
    > ...

### Node `Covenant2`

When it began, =name= had no shared helices with the Reshephs previous, making their name through works and alliances alone. The lives saved and otherwise changed by =name= were myriad, uncountable, and only partially made record. When they spoke, even the plagues of Qud listened.

        At the end of their reign, =name= made a compact with the Nephilim that they should never vex the creatures of Qud again. So done, they climbed to the top of the spire, there to end the Reshephate altogether and never be heard from again.

**Choices:**
- **choice** `?` → `Covenant3`
    > ...

### Node `Covenant3`

Word of =name='s deeds reached record only after the unheralded appearance of the Knights Liminal, and broad assumption suggests that the former established the latter. It could be that the ancient Resheph yet lives within or outside of the boundaries of the Limen, but no word escapes its borders.

**Choices:**
- **choice** `?` → `CovenantWho`
    > Who are you?
- **choice** `?` → `CovenantPC`
    > Who is =name=?
- **choice** `?` → `CovenantResheph`
    > What is a Resheph?
- **choice** `?` → `CovenantLimen`
    > What is the Limen? The Knights Liminal?
- **choice** `?` → `CovenantNephilim`
    > What became of the Nephilim?
- **choice** `?` → `End`
    > Thank you. Farewell.

### Node `CovenantWho`

I have been called Inheritor, Godling, Spirechild, Nephiling. They are all fitting names, but none complete or sufficient.

        As it is with you, I am the convergence of past-ripples into present-force. As it is with you, I am deeds done and the intention toward deeds yet to be done.

### Node `CovenantPC`

Who? No one of significance until fortune and volition made them otherwise. Now? No one knows.

### Node `CovenantResheph`

Ancient leaders called themselves such.

### Node `CovenantLimen`

To me, they are stories. I have made no quest to trespass the borders they hold so dear in their rituals. Some say they are mortal creatures like any other, contracted by an outsider coven. Others do not believe they are mortal, others still do not believe that those mysterious strangers have anything to do with the Limen at all.

        Mayhap someone ought seek them.

### Node `CovenantNephilim`

They lived.

        Simply a part of the world now, no longer a cilice scourging the Earth, they lived as the creatures they were. Descendants of their offspring may walk on and under Qud. Mayhap the first ones yet live. Mayhap they slumber. Mayhap they will rage again one day, to disrupt a stagnant world.

### Node `Return Story`

It begins in a time before the Freeholders, before the final Sultan was entombed, when the spire rose unchallenged and unascended. The hollowers who committed their work to emptying our world were long gone, but Kings and Sultans laid claim to the baffled ground in their place. Even as their holdings withered, they held on.

        They so devoured one another’s history that little substance remained outside of their strongholds.

**Choices:**
- **choice** `?` → `Return2`
    > ...

### Node `Return2`

When their works began, =name= had no connection to the Sultanate. The rule of these ancient leaders had ended, but not fully: a ghost of the last Sultan yet ruled over the spire, tormenting those on and under the ground with plagues. As =name= grew mighty and challenged the rampaging Nephilim, they came to recognize the source of their shared conflict.

        Seeking freedom from the reign of the Sultan, =name= struck a compact with the Nephilim and climbed to the top of the spire, there to confront and banish the cerulean ghost.

        And so it proceeded.

**Choices:**
- **choice** `?` → `Return3`
    > ...

### Node `Return3`

Upon their return, =name= participated in the dissolution and federation of all power-concentrate. Allies of the new equalizer gathered and rose, forming the Quetzal Council and other, shorter-lived managing bodies.

        Since then, we have lived in tenuous harmony on the dwindling land and under it.

**Choices:**
- **choice** `?` → `ReturnWho`
    > Who are you?
- **choice** `?` → `ReturnPC`
    > Who is =name=?
- **choice** `?` → `ReturnFreeholder`
    > What is a Freeholder?
- **choice** `?` → `ReturnNephilim`
    > What became of the Nephilim?
- **choice** `?` → `End`
    > Thank you. Farewell.

### Node `ReturnWho`

I have been called Inheritor, Godling, Spirechild, Nephiling. They are all fitting names, but none complete or sufficient.

        As it is with you, I am the convergence of past-ripples into present-force. As it is with you, I am deeds done and the intention toward deeds yet to be done.

### Node `ReturnPC`

Who? No one of significance until fortune and volition made them otherwise. They died without title, or perhaps did not die at all. Tales abound, and thus far no one has stepped forth to renounce or affirm them.

### Node `ReturnFreeholder`

The Freeholds of Qud, that web of folk-clusters, of committees and caucuses, syndicated slime-mold cities held in peace by mutual frustration and monumental effort.

        If you need detail, ask a Freeholder, but clear your day first.

### Node `ReturnNephilim`

They lived.

        Simply a part of the world now, no longer a cilice scourging the Earth, they lived as the creatures they were. Descendants of their offspring walk on and under Qud. Mayhap the first ones yet live. Mayhap they slumber, to wake again when needed.

### Node `Starfarer Story`

It begins in a time before =name='s ascension, when the spire rose unchallenged and unascended. The hollowers who committed their work to emptying our world were long gone, but long had rulers laid claim to the baffled ground in their place. Even as their holdings withered, they held on.

        By the end of the time of Kings and Sultans, little remained of their works, less of their glory.

**Choices:**
- **choice** `?` → `Starfarer2`
    > ...

### Node `Starfarer2`

When it began, =name= had no shared helices with Qud’s leaders, making their name through works and alliances alone. The lives taken and saved by =name= were myriad, uncountable, and only partially made record. When they spoke, even the plagues of Qud listened.

        At the end of their reign, =name= made a compact with the Nephilim that they should never vex the creatures of Qud again. So done, they climbed to the top of the spire and boarded an ancient vessel, thereby to travel the star-dusted expanse.

**Choices:**
- **choice** `?` → `Starfarer3`
    > ...

### Node `Starfarer3`

For centuries, we of listening inclination have kept sharp for some sign that =name= will return to the stars. Those of preaching inclination proclaim the imminent return of the starfarer, bearing tidings from parsecs forgotten and the last light of dying stars.

        All others have lived in tenuous harmony on the dwindling land and under it, waiting for the next great history.

**Choices:**
- **choice** `?` → `StarfarerWho`
    > Who are you?
- **choice** `?` → `StarfarerPC`
    > Who is =name=?
- **choice** `?` → `StarfarerTravel`
    > Can one really travel the stars?
- **choice** `?` → `StarfarerNephilim`
    > What became of the Nephilim?
- **choice** `?` → `End`
    > Thank you. Farewell.

### Node `StarfarerWho`

I have been called Inheritor, Godling, Spirechild, Nephiling. They are all fitting names, but none complete or sufficient.

        As it is with you, I am the convergence of past-ripples into present-force. As it is with you, I am deeds done and the intention toward deeds yet to be done.

### Node `StarfarerPC`

Who, indeed? Who ever was =name=? Dare we hang such hopes and fears on so tiny and distant a figure? Will it bear the weight?

### Node `StarfarerTravel`

Oh, yes. Never doubt this.

        Can one return? Hmm. There’s the rub.

### Node `StarfarerNephilim`

They lived.

        Simply a part of the world now, no longer a cilice scourging the Earth, they lived as the creatures they were. Descendants of their offspring walk on and under Qud. It’s said that they ascended to the stars to find =name=, but it seems equally plausible that they may have returned to their slumber in the depths.

### Node `Accession Story`

It begins in a time before the dread ascension of =name=, a time wherein the spire rose unchallenged and unascended. The hollowers who committed their work to emptying our world were long gone, but long had rulers laid claim to the baffled ground in their place. Even as their holdings withered, they held on.

        The last of them would be the worst.

**Choices:**
- **choice** `?` → `Accession2`
    > ...

### Node `Accession2`

When it began, =name= had no shared helices with Qud’s leaders, making their name through the spilling of blood and terror. Uncountable lives were taken by their hand alone, all to slake age-old desires of control and might.

        Perhaps hunger turned to malice, or the adoption of a greater principle, or simple boredom. Whatever the reason, =name= formed a fast alliance with the ancient plagueborn Nephilim, ascended the spire, and sealed the fate of the world below.

        The Plagues of the Gyre raged unchecked.

**Choices:**
- **choice** `?` → `Accession3`
    > ...

### Node `Accession3`

In time, animal and even plant rule waned as their numbers fell to disease, slaughter, and wasting. More resilient, simple life took up the complexity left behind by the former rulers of Qud.

        What few Nervous Ones remained passed our stories on to the new life that saw fit to seek our counsel, that you remember the collective fate of those gone. Will you have your own =name=, or have you evolved truly past those before?

**Choices:**
- **choice** `?` → `AccessionWho`
    > Who are you?
- **choice** `?` → `AccessionPC`
    > Who is =name=?
- **choice** `?` → `AccessionNervous`
    > I thought the Nervous Ones extinct.
- **choice** `?` → `AccessionNephilim`
    > What became of the Nephilim?
- **choice** `?` → `End`
    > Thank you. Farewell.

### Node `AccessionWho`

I am history’s leftovers, an inheritor of nothing, a bit of marginalia in a burned tome.

        That I have persisted to witness this day leaves me in awe. It is extraordinary.

### Node `AccessionPC`

Who, indeed? Who ever was =name=? Dare we hang such hopes and fears on so tiny and distant a figure? Will it bear the weight?

### Node `AccessionNervous`

Every possibility nestles in the deepest of the comb-caves and labyrinths, and even Nervous life is tenacious. Perhaps in this very moment, a moss piglet drinks of its first water in an eon.

### Node `AccessionNephilim`

They played their role so well, and lived in power for a time.

        If they had any illusion that they would be spared the fate =name= determined for life on Qud, it surely died before the great beings themselves. Mayhap they went to ground and survived. Mayhap their spawn persisted.
