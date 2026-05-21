# Conversation: `Neelahind`

_Inherits: (default: BaseConversation)_

_6 start(s), 46 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Distant`

*The warden's gaze is distant.* Esk...

**Choices:**
- **choice** `?` → `End`
    > *leave her be*

### Start `Direct`

Follow the road =EskhindRoadDirection= to find the hollow tree where Esk and I used to play.

**Choices:**
- **choice** `?` → `End`
    > Thank you.

### Start `Ruminating`

*The warden is lost in rumination.* It can't be. It simply can't be.

**Choices:**
- **choice** `?` → `Warden Neelahind?`
    > Warden Neelahind?

### Start `Dead`  _IfHaveState=`EskhindSlain`_

Kendren, do you... have any news of Eskhind, and Kindrish?

**Choices:**
- **choice** `?` → `Eskhind is dead.`
    > Eskhind is dead.
- **choice** `?` → `End`
    > No.

### Start `Fate`

Ah, =name=, live and drink!

        Has your investigation reached a conclusion? Our fate is in your hands.

**Choices:**
- **choice** `?` → `Neelahind is giddy`
    > Not yet. How are you and Eskhind?
- **choice** `?` → `KindrishReturn`
    > Warden, I have found Kindrish.
- **choice** `?` → `KithAndKinCircumstance`
    > Yes, I am ready to accuse the thief.
- **choice** `?` → `Questioning Neelahind`
    > Not yet. May I ask you some questions?
- **choice** `?` → `End`
    > No, I do not have enough evidence yet.

### Start `Doomed`  _IfHaveState=`HindrenVillageDoomed`_

There's a fear deep in my breast, kendren. What's to become of Bey Lah?

**Choices:**
- **choice** `?` → `KindrishReturnAfter`
    > Warden, I have found Kindrish.
- **choice** `?` → `End`
    > Fine. Live and drink.

## Nodes

### Node `Warden Neelahind?`

Ah! Yes. My apologies, kendren. Live and drink. I am Neelahind, Warden of Bey Lah. How... may I help you?

**Choices:**
- **choice** `?` → `Friends with Eskhind`
    > Hindriarch Keh told me that you were once friends with Eskhind.
- **choice** `?` → `End`
    > I will return later.

### Node `Friends with Eskhind`

We were... yes. We were close.

        I can scarcely believe that she would be capable of doing such a thing. Stealing our greatest treasure? Eskhind wouldn't possibly... but if Grand-Doe says it, it must be so.

**Choices:**
- **choice** `?` → `Where?`
    > Do you know where Eskhind and her siblings might have gone?
- **choice** `?` → `Hindriarch is lying?`
    > Is it possible that the Hindriarch is lying?

### Node `Hindriarch is lying?`

Wh—no! No! What? No, that's not possible! Ayvah, what an absurd idea!

**Choices:**
- **choice** `?` → `Why not?`
    > Why not?
- **choice** `?` → `Where?`
    > Do you know where Eskhind and her siblings might have gone?

### Node `Why not?`

Grand-Doe speaks only truth! Grand-Doe only ever speaks truth!

        It's not possible. She didn't lie.

**Choices:**
- **choice** `?` → `Anyone can lie.`
    > Anyone can lie.
- **choice** `?` → `End`
    > You ruminant people are impossible. I will find Eskhind myself.

### Node `Anyone can lie.`

No. It's not true, and I won't hear any more of your poisonous ideas, kendren. Consider the topic closed.

        Do you actually have a question?

**Choices:**
- **choice** `?` → `Where?`
    > Do you know where Eskhind and her siblings might have gone?
- **choice** `?` → `End`
    > Forget it. I don't need your help.

### Node `Where?`

Oh. Esk and I, we had a place... there's a path to the =EskhindRoadDirection= that leads to the remains of a lightning-struck tree, made hollow by the fire from above. It was the furthest from the village either of us had ever been, until I attended my first warden's moot.

        She and I would spend time there, back then. Perhaps she is there now, but I don't dare check.

**Choices:**
- **choice** `?` → `End`
    > I'll look there, thank you.

### Node `No. I'm sorry.`

No... no, I can't... and the artifact is lost?

        It was all for nothing... for nothing...

**Choices:**
- **choice** `?` → `End`
    > I will leave you to your grief. Live and drink.

### Node `No. The Hindriarch lied to you.`

No, it can't be... how. This place. This accursed village!

        This whole village be damned!

**Choices:**
- **choice** `?` → `End`
    > *back away slowly*
    - _part: `StartFight`_

### Node `No, this was for fun.`

You monster! You monster! How dare you!

**Choices:**
- **choice** `?` → `End`
    > You're next.
    - _part: `StartFight`_

### Node `KindrishReturn`

Oh! Kendren, thank you, thank you! You've done so much for us. Here is a reward for your hard work.

        Um, that said, there's still the matter of finding out who stole our treasure. It'd mean a great deal if you could still help with the resolution of the case.

**Choices:**
- **choice** `?` → `End`
    > Understood. Live and drink.

### Node `Start`

Wh-what's going on? Esk is here, a-and Grand-Doe seems very upset.

        Would you please speak to her, kendren?

**Choices:**
- **choice** `?` → `End`
    > I will.

### Node `Start`

Wait, why... why is Esk here? What's going on? Do you have Kindrish?

**Choices:**
- **choice** `?` → `KindrishReturn`
    > Yes, I do, but Eskhind didn't have it.
- **choice** `?` → `No. Eskhind claims to be wrongfully accused.`
    > No. Eskhind claims to be wrongfully accused.
- **choice** `?` → `End`
    > Ah, one moment...

### Node `No. Eskhind claims to be wrongfully accused.`

Oh.

        But... what now?

**Choices:**
- **choice** `?` → `You're the Warden. You tell me.`
    > You're the Warden. You tell me.
- **choice** `?` → `We will investigate and find the truth.`
    > We will investigate and find the truth.
- **choice** `?` → `End`
    > You are useless. I'll get to the bottom of this.

### Node `You're the Warden. You tell me.`

I... I don't know. Grand-doe usually resolves Bey Lah's disputes. I am present to defuse violence, or keep the peace through the threat of it.

        What do you think?

**Choices:**
- **choice** `?` → `We will investigate and find the truth.`
    > We will investigate and find the truth.
- **choice** `?` → `End`
    > You are useless. I'll get to the bottom of this.

### Node `We will investigate and find the truth.`

Oh. Well, yes, that's... that's a good idea. You'll help, right? My axe-arm and conviction are strong, but deduction has never been my greatest strength.

        I can answer questions about the people in town, if that would be helpful.

**Choices:**
- **choice** `?` → `Questioning Neelahind`
    > It would. Could you answer some questions now?
- **choice** `?` → `End`
    > I will return when I have questions... or an accusation.

### Node `Neelahind is giddy`

Oh, =name=! I'm so happy!

        I can scarcely believe she loves me, much less that... that we could be together. But it's true. Wherever we go from now on, we go together.

**Choices:**
- **choice** `?` → `End`
    > May your journeys favor you. Live and drink.

### Node `Start`

Oh dear, a mystery.

        Perhaps I should have accepted Angohind's lessons after all.

**Choices:**
- **choice** `?` → `SonnetOffer`
    > I believe this poem was meant for you.
- **choice** `?`
- **choice** `?` → `Questioning Neelahind`
    > May I ask some questions about the suspects?
- **choice** `?` → `End`
    > Patience, Warden. I'll get to the bottom of this.

### Node `Start`  _IfHaveState=`FoundClue`_

Live and drink, kendren. Have you... come to a conclusion?

**Choices:**
- **choice** `?` → `SonnetOffer`
    > I believe this poem was meant for you.
- **choice** `?`
- **choice** `?` → `KithAndKinCircumstance`
    > Yes, I am ready to accuse the thief.
- **choice** `?` → `Questioning Neelahind`
    > Not yet. May I ask you some questions?
- **choice** `?` → `End`
    > No, I do not have enough evidence yet.

### Node `KithAndKinCircumstance`

I see. What is it?

**Choices:**
- **choice** `?` → `End`
    > I'm still not completely certain. Let me ponder it more.

### Node `KithAndKinMotive`

Signs of =circumstance.influence=, seemingly hidden from the village. But that can't be your only evidence, can it? There's no culprit!

**Choices:**
- **choice** `?` → `End`
    > I'm still not completely certain. Let me ponder it more.

### Node `KithAndKinExclusion`

I'm afraid that well is poisoned due to your false accusation: =thief.name= isn't the culprit.

Hmm. But the only fur there was from a hindren's pelt, and kendren warriors fight to the death. With no corpse and no other fur, it seems unlikely that a hindren fought an outsider.

I'm afraid that makes no sense. Why would an outsider invite a trader to our village, when they could simply meet one outside of Bey Lah?

But weren't the rumors of sore throats in the village? That wouldn't have anything to do with kendren.

Why wouldn't an outsider bring their own leather? It would better disguise Kindrish. It seems a lot of work to find and raid our leather stores.

Bracers are a Bey Lah craft! It would make no sense for a kendren to have one, then throw it away in the village.

Kesehind wields Ari, a battleaxe handed down through generations. It cannot break, and if it broke a weapon there would be scorch marks on it. This evidence does not hold up.

There are few voices as low as Kesehind's in our village. Witnesses report a higher-pitched voice, don't they? They would know if Kesehind were speaking.

Oh, no, that wouldn't be Kesehind. He'd sooner die of fever than choke down a single stem of yuckwheat.

Oh, no, that wouldn't be Kesehind. He'd sooner die of fever than choke down a single stem of yuckwheat.

That would be nigh unto impossible for Kesehind. He cannot perform fine tasks by torchlight; his night vision is too poor.

No, that can't be it. Eskhind hates everything about watervine and keeps a wide berth from it. If her blood was spilled, it would have happened nearer to the path.

No, no. Eskhind makes the most of what few possessions she keeps, and if she traded a treasure for so much water, she'd never have lost track of any.

Oh, no, Eskhind is deathly afraid of saltbacks. She would never get close enough to trade with a dromad merchent.

I doubt it. If Eskhind were sick, the last place she would stumble to evacuate her guts would be a watervine field.

I'm afraid that Eskhind has no idea how to use proper leatherworking tools, much less pay for a set so fine. This surely isn't hers.

I know the rumor you mean, but villagers heard the clash of weapons. Keh is too old for a prolonged fight like that, so I do not believe it was her.

Grand-Doe cannot swim, and panics even near the shallow pools of our paddies. I cannot imagine she would make splashing noises without adding screaming noises to them.

Copper causes Grand-Doe to break out in great welts. She would not have traded for it, and if she saw a trader drop it, surely she would have told them to pick it up. She hates mess.

I cannot bring myself to believe that Grand-Doe would allow anyone to stumble upon her own severed tongue. She would surely burn it as soon as she saw it.

No, Grand-Doe is absolutely meticulous about work clutter. She wouldn't leave scraps lying about.

**Choices:**
- **choice** `?` → `End`
    > Ah.

### Node `KithAndKinAccusation`

Oh. Yes, this does indicate that some kind of =motive.influence= transpired, and =thief.name= was trying to hide it.

        So what you're saying is....

**Choices:**
- **choice** `?` → `KithAndKinFinale`
    > That's right. By concealing =all.influence=, it was =thief.name= who stole Kindrish!
- **choice** `?` → `End`
    > I'm still not completely certain. Let me ponder it more.

### Node `KithAndKinFinale`

The evidence is clear. In violation of sacred law and the will of her people, Eskhind stole the artifact called Kindrish from Bey Lah. She will be stripped of honor, stripped of water, and stripped from our oral histories. Never will her name be spoken here again, and she will never return... on pain of death.

        And I... I will go with her. May my property be payment for the harm she has done to our people, and I will gladly pay it for the privilege of walking by her side.

        I have no doubt that Bey Lah will thrive in my absence as it did before I became warden. Live and drink, my kin. Long may Hindriarch Keh lead you.

The evidence is clear. In violation of sacred law and the will of her people, Eskhind stole the artifact called Kindrish from Bey Lah. She will be stripped of honor, stripped of water, and stripped from our oral histories. Never will her name be spoken here again, and she will never return... on pain of death.

        She could never hope to repay the harm caused by her actions, but we will grant her this last mercy: Bey Lah will forget her debt alongside her name.

        Just is the leadership of Hindriarch Keh. Long may she live!

The evidence is clear. In violation of sacred law and the will of her people, Eskhind stole the artifact called Kindrish from Bey Lah. She will be stripped of honor, stripped of water, and stripped from our oral histories. Never will her name be spoken here again, and she will never return... on pain of death.

        And I... I will go with her. May my property be payment for the harm she has done to our people, and I will gladly pay it for the privilege of walking by her side.

        I have no doubt that Bey Lah will thrive in my absence as it did before I became warden. Live and drink, my kin. Long may Hindriarch Keh lead you.

The evidence is clear. In violation of sacred law and the will of her people, Eskhind stole the artifact called Kindrish from Bey Lah. She will be stripped of honor, stripped of water, and stripped from our oral histories. Never will her name be spoken here again, and she will never return... on pain of death.

        She could never hope to repay the harm caused by her actions, but we will grant her this last mercy: Bey Lah will forget her debt alongside her name.

        Just is the leadership of Hindriarch Keh. Long may she live!

The evidence is clear. In violation of sacred law and the will of her people, Eskhind stole the artifact called Kindrish from Bey Lah. She will be stripped of honor, stripped of water, and stripped from our oral histories. Never will her name be spoken here again, and she will never return... on pain of death.

        And I... I will go with her. May my property be payment for the harm she has done to our people, and I will gladly pay it for the privilege of walking by her side.

        May the fates have mercy upon us all.

The evidence is clear. In violation of sacred law and the will of her people, Eskhind stole the artifact called Kindrish from Bey Lah. She will be stripped of honor, stripped of water, and stripped from our oral histories. Never will her name be spoken here again, and she will never return... on pain of death.

        She could never hope to repay the harm caused by her actions, but we will grant her this last mercy: Bey Lah will forget her debt alongside her name.

        May the fates have mercy upon us all.

The evidence is clear: Eskhind did not steal Kindrish. In fact, I believe that no hindren was responsible for its theft, but one of the kendren who permeated our borders well before our investigator arrived. Any of them could have committed the theft.

        Eskhind is free to go, and I'm... I'm going with her. I cannot serve under Hindriarch Keh while my beloved returns to exile.

        I have no doubt that Bey Lah will thrive in my absence as it did before I became warden. Live and drink, my kin. Long may Hindriarch Keh lead you.

The evidence is clear: Eskhind did not steal Kindrish. In fact, I believe that no hindren was responsible for its theft, but rather one of the kendren who permeated our borders well before our investigator arrived. Any of them could have committed the theft.

        Eskhind helped us cleave to the path of justice. She is free to go, and her name will not be forgotten, but she must remain in exile.

        Just is the leadership of Hindriarch Keh. Long may she live!

The evidence is clear: Eskhind did not steal Kindrish. In fact, I believe that no hindren was responsible for its theft, but one of the kendren who permeated our borders well before our investigator arrived. Any of them could have committed the theft.

        Eskhind is free to go, and I'm... I'm going with her. I cannot serve under Hindriarch Keh while my beloved returns to exile.

        I have no doubt that Bey Lah will thrive in my absence as it did before I became warden. Live and drink, my kin. Long may Hindriarch Keh lead you.

The evidence is clear: Eskhind did not steal Kindrish. In fact, I believe that no hindren was responsible for its theft, but rather one of the kendren who permeated our borders well before our investigator arrived. Any of them could have committed the theft.

        Eskhind helped us cleave to the path of justice. She is free to go, and her name will not be forgotten, but she must remain in exile.

        Just is the leadership of Hindriarch Keh. Long may she live!

The evidence is clear: Eskhind did not steal Kindrish. In fact, I believe that no hindren was responsible for its theft, but one of the kendren who permeated our borders well before our investigator arrived. Any of them could have committed the theft.

        Eskhind is free to go, and I'm... I'm going with her. I cannot serve under Hindriarch Keh while my beloved returns to exile.

        Goodbye. May the fates have mercy upon you.

The evidence is clear: Eskhind did not steal Kindrish. In fact, I believe that no hindren was responsible for its theft, but rather one of the kendren who permeated our borders well before our investigator arrived. Any of them could have committed the theft.

        Eskhind helped us cleave to the path of justice. She is free to go, and her name will not be forgotten, but she must remain in exile.

        May the fates have mercy upon us all.

The evidence is clear: Eskhind did not steal Kindrish. The crime was committed by none other than Grand-Doe's protector, Kesehind. He will be stripped of the ancestral axe he carries, stripped of his property, and stripped from our oral histories. Never will his name be spoken here again, and he will never return... on pain of death.

        Moreover... Keh's attempt to pin blame on Eskhind without due process opened my eyes to her abuses of power. She need not leave Bey Lah, but she is Keh-hind once more-- stripped of her title and standing.

        As for the hindriarchy, Eskhind will act as an interim leader until we figure out what to do next, as a people. May Hindriarch Esk lead us to a brighter future!

The evidence is clear: Eskhind did not steal Kindrish. The crime was committed by none other than Grand-Doe's protector, Kesehind. He will be stripped of the ancestral axe he carries, stripped of his property, and stripped from our oral histories. Never will his name be spoken here again, and he will never return... on pain of death.

        Moreover... Keh's attempt to pin blame on Eskhind without due process opened my eyes to her abuses of power. She need not leave Bey Lah, but she is Keh-hind once more-- stripped of her title and standing.

        As for the hindriarchy, Eskhind will act as an interim leader until we figure out what to do next, as a people. May Hindriarch Esk lead us to a brighter future!

The evidence is clear: Eskhind did not steal Kindrish. The crime was committed by none other than Grand-Doe's protector, Kesehind. He will be stripped of the ancestral axe he carries, stripped of his property, and stripped from our oral histories. Never will his name be spoken here again, and he will never return... on pain of death.

        Moreover... Keh's attempt to pin blame on Eskhind without due process opened my eyes to her abuses of power. She need not leave Bey Lah, but she is Keh-hind once more-- stripped of her title and standing.

        As for the hindriarchy, Eskhind will act as an interim leader until we figure out what to do next, as a people. It will be a challenge to accept change, but we will be stronger for it.

The evidence is clear: Eskhind did not steal Kindrish. The crime was committed by none other than Grand-Doe's protector, Kesehind. He will be stripped of the ancestral axe he carries, stripped of his property, and stripped from our oral histories. Never will his name be spoken here again, and he will never return... on pain of death.

        Moreover... Keh's attempt to pin blame on Eskhind without due process opened my eyes to her abuses of power. She need not leave Bey Lah, but she is Keh-hind once more-- stripped of her title and standing.

        As for the hindriarchy, Eskhind will act as an interim leader until we figure out what to do next, as a people. It will be a challenge to accept change, but we will be stronger for it.

The evidence is clear: Eskhind did not steal Kindrish. The crime was committed by none other than Grand-Doe's protector, Kesehind. He will be stripped of the ancestral axe he carries, stripped of property, and stripped from our oral histories. Never will his name be spoken here again, and he will never return... on pain of death.

        Eskhind is free to go, and I'm... I'm going with her. This place is not safe.

        May the fates have mercy on you.

The evidence is clear: Eskhind did not steal Kindrish. The crime was committed by none other than Grand-Doe's protector, Kesehind. He will be stripped of the ancestral axe he carries, stripped of his property, and stripped from our oral histories. Never will his name be spoken here again, and he will never return... on pain of death.

        Moreover... Keh's attempt to pin blame on Eskhind without due process opened my eyes to her abuses of power. She need not leave Bey Lah, but she is Keh-hind once more-- stripped of her title and standing. As for the hindriarchy, Eskhind will act as an interim leader until we figure out what to do next, as a people.

        I fear dark times ahead. We must remain strong in the coming days.

The evidence is clear: Bey Lah's own Hindriarch has betrayed her people. She took our ancestral treasure as her own, pinning the crime on an exile she knew could not defend herself. For this treason, she is hereby stripped of title, stripped of property, stripped of home.

        With the exile of Keh-Hind, the hindriarchy lies vacant, with no elders fit to take it. Eskhind will act as an interim leader until we figure out what to do next, as a people. May Hindriarch Esk lead us to a brighter future!

The evidence is clear: Bey Lah's own Hindriarch has betrayed her people. She took our ancestral treasure as her own, pinning the crime on an exile she knew could not defend herself. For this treason, she is hereby stripped of title, stripped of property, stripped of home.

        With the exile of Keh-Hind, the hindriarchy lies vacant, with no elders fit to take it. Eskhind will act as an interim leader until we figure out what to do next, as a people. May Hindriarch Esk lead us to a brighter future!

The evidence is clear: Bey Lah's own Hindriarch has betrayed her people. She took our ancestral treasure as her own, pinning the crime on an exile she knew could not defend herself. For this treason, she is hereby stripped of title, stripped of property, stripped of home.

        With the exile of Keh-Hind, the hindriarchy lies vacant, with no elders fit to take it. Eskhind will act as an interim leader until we figure out what to do next, as a people. May Hindriarch Esk lead us to a brighter future!

The evidence is clear: Bey Lah's own Hindriarch has betrayed her people. She took our ancestral treasure as her own, pinning the crime on an exile she knew could not defend herself. For this treason, she is hereby stripped of title, stripped of property, stripped of home.

        With the exile of Keh-Hind, the hindriarchy lies vacant, with no elders fit to take it. Eskhind will act as an interim leader until we figure out what to do next, as a people. It will be a challenge to accept change, but we will be stronger for it.

The evidence is clear: Bey Lah's own Hindriarch has betrayed her people. She took our ancestral treasure as her own, pinning the crime on an exile she knew could not defend herself. For this treason, she is hereby stripped of title, stripped of property, stripped of home.

        With the exile of Keh-Hind, the hindriarchy lies vacant, with no elders fit to take it. Eskhind will act as an interim leader until we figure out what to do next, as a people. It will be a challenge to accept change, but we will be stronger for it.

The evidence is clear: Bey Lah's own Hindriarch has betrayed her people. She took our ancestral treasure as her own, pinning the crime on an exile she knew could not defend herself. For this treason, she is hereby stripped of title, stripped of property, stripped of home.

        With the exile of Keh-Hind, the hindriarchy lies vacant, with no elders fit to take it. Eskhind will act as an interim leader until we figure out what to do next, as a people.

        I fear dark times ahead. We must remain strong in the coming days.

**Choices:**
- **choice** `?` → `End`
    > My job here is done. Live and drink.

### Node `SonnetOffer`

For me? Are you sure?

        But... this is a poem. In Esk's handwriting. Are you s-sure this is for me?

**Choices:**
- **choice** `?` → `SonnetDelivered`
    > Yes. Please read it.
- **choice** `?` → `End`
    > Perhaps I'm mistaken. Live and drink.

### Node `SonnetDelivered`

Oh.

        Ayvah, she-- Eskhind wrote this about... me? How my head swims at these lavish words. If she wrote this and meant it for me, she must... love me.

        But it can't be. Can it?

**Choices:**
- **choice** `?` → `NeelaLovesEsk`
    > Can't it?
- **choice** `?` → `End`
    > It is. Live and drink.

### Node `NeelaLovesEsk`

Kendren, you must understand. I spent so many years trying in vain to fall out of love with Eskhind. I thought it the only way to endure our adolescence, watching her poor attempts at courtship with other hindren.

        I thought it the only way to endure her departure, as well. But she is returned, and she loves me. Ayvah. I am terrified to speak to her of this, but I must.

        Thank you.

**Choices:**
- **choice** `?` → `Investigation`
    > Will this affect the investigation?
- **choice** `?` → `End`
    > Live and drink, Neelahind.

### Node `Investigation`

No. You are the one investigating, so my bias need not enter play. If you determine that Eskhind is guilty, I will heed your word and carry out a just sentence.

        After that, I'm not sure.

**Choices:**
- **choice** `?` → `Questioning Neelahind`
    > In that case, I have further questions.
- **choice** `?` → `End`
    > Live and drink.

### Node `Questioning Neelahind`

Of course, kendren. Ask away.

**Choices:**
- **choice** `?` → `Neelahind on Keh`
    > What can you tell me about Hindriarch Keh?
- **choice** `?` → `Neelahind on Eskhind`
    > What can you tell me about Eskhind?
- **choice** `?` → `Neelahind on Kesehind`
    > What can you tell me about Kesehind?
- **choice** `?` → `Neelahind on kendren`
    > What do you know about the outsiders? The kendren?
- **choice** `?` → `End`
    > I should return to my investigation. Live and drink.

### Node `Neelahind on Keh`

Keh is very wise and very careful, which makes up for her lack of strength or... tact. She always knows what's right, and she runs a very tight shift.

        She hates clutter from work like nothing else and cleans up any mess she makes--unless it's a spill, then she makes Kesehind do it. It's because Grand-Doe has a terrible fear of standing pools of water, refusing to touch them. Copper and bronze afflict her with allergy-sores and she can't touch them. She's too old to spar with me, but her bow-arm still aims true.

        That's all I can think of.

**Choices:**
- **choice** `?` → `Questioning Neelahind`
    > I have another question, if you please.
- **choice** `?` → `End`
    > Thank you, that will do. Live and drink.

### Node `Neelahind on Eskhind`

Oh. She's, well, she's a good person with strong convictions, or has always seemed so. I suppose that isn't helpful.

        Esk has a good eye for detail. She hates watervine so much that she avoids the paddies and won't eat matz without lah broth to make it taste better. Umm, she's afraid of saltbacks. She's good at foraging and terrible at crafting.

        I've missed her so much.

**Choices:**
- **choice** `?` → `Questioning Neelahind`
    > I have another question, if you please.
- **choice** `?` → `End`
    > Thank you, that will do. Live and drink.

### Node `Neelahind on Kesehind`

Kesehind is completely loyal to Grand-Doe. We used to be friends, but his disposition has become so sour since he was appointed her protector, and he's quite cold to me now. He can't see well in darkness. He's the holder of Ari, an unbreakable heirloom fire axe, and he's very skilled with it.

        He's terribly finicky about food. He'll only eat bland food and meat, and... oh! Once, when he had a bad cough as a faundren, a caretaker tried to feed him yuckwheat, and he kicked her so hard it dislocated her jaw. Poor Elder Eselhind.

**Choices:**
- **choice** `?` → `Questioning Neelahind`
    > I have another question, if you please.
- **choice** `?` → `End`
    > Thank you, that will do. Live and drink.

### Node `Neelahind on kendren`

Oh, not very much. The only kendren who were allowed in the village before you are traders, and it's always a very big fuss when one comes by. It's been a while since that happened, though, so any kendren who have visited must have come in secret.

**Choices:**
- **choice** `?` → `Questioning Neelahind`
    > I have another question, if you please.
- **choice** `?` → `End`
    > Thank you, that will do. Live and drink.

### Node `Start`  _IfHaveState=`HindrenVillageRavaged`_

Live and drink, kendren.

        Please forgive me; I am grateful that you opened my eyes, but the sight of you is yet a bitter leaf. Let me grieve my people in peace.

**Choices:**
- **choice** `?` → `LateSonnet`
    > Does this poem belong to you?
- **choice** `?` → `End`
    > My condolences.

### Node `KindrishReturnAfter`

You've found our treasure? Thank you, kendren!

        Please take this reward, we set it aside for just this purpose. I apologize if it's too little. Thank you so much, again.

**Choices:**
- **choice** `?` → `End`
    > Live and drink, warden.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Kendren! I mean, =name=! My heart sings to see you.

        Thank you for clearing Esk's name. Thank you for bringing us together. You are always welcome here.

**Choices:**
- **choice** `?`
- **choice** `?` → `End`
    > You're welcome. Live and drink.

### Node `Start`

Ah! Kendren! =name=! I'm so happy! Live and drink.

**Choices:**
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, warden.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

=name=, it is good to see you. Rest and sup before you move on.

**Choices:**
- **choice** `?` → `BetterLate`
    > I believe this poem was meant for you.
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink, warden.

### Node `Start`

Kendren, thank you for clearing Esk's name!

        You're so decisive. I wish I had that strength.

**Choices:**
- **choice** `?` → `BetterLate`
    > I believe this poem was meant for you.
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `BetterLate`

Oh! Is this what... Esk!

        I could have gone years unknowing that my love for her was returned. But this is her script, and these words describe me.

        Ayvah, I have to speak to her! Thank you so much, kendren.

**Choices:**
- **choice** `?` → `End`
    > You're welcome. Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Thank you again for opening my eyes, kendren.

        I have trouble smiling for my grief, my loss. Nonetheless, Eskhind and I have a brighter future because of you, and we are together. The road is hazardous, but we will walk it in time.

**Choices:**
- **choice** `?` → `End`
    > My condolences. Live and drink.

### Node `Start`

Kendren...

        I have so much anger at what has been done, but you opened my eyes. Thank you.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`  _IfHaveState=`HindrenQuestFullyResolved`_

Ah, =name=. The sight of you is yet a bitter leaf, but you are welcome here.

**Choices:**
- **choice** `?` → `LateSonnet`
    > Does this poem belong to you?
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Kendren.

        Forgive me for seeming ungrateful. I am more affected by Esk's return and departure than I knew. Please give me space.

**Choices:**
- **choice** `?` → `LateSonnet`
    > Does this poem belong to you?
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink.

### Node `LateSonnet`

What is this?

        Poetry. In the exile's handwriting. Extolling love for... me, or someone very like me.

        Is... is this a cruel joke? This cannot be real.

**Choices:**
- **choice** `?` → `WhyNow`
    > It is real. Take the poem.
- **choice** `?` → `End`
    > I must be mistaken. Live and drink.

### Node `WhyNow`

She loved me.

        She loved me and I ... I exiled her. Oh, my heart.

        Kendren I, I am grateful that you have opened my eyes to the truth, but how dearly I wish you had intervened earlier. This poem serves only as a harsh reminder that I must give up everything for my duty.

        Please. Please leave me be. My heart... Esk, my heart...

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Live and drink, kendren.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.
