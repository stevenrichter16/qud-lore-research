# Conversation: `Vivira`

_Inherits: (default: BaseConversation)_

_0 start(s), 10 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

*BEEP* *crackle*

        By Her Light, =player.formalAddressTerm=.

        An =ifplayerplural:ye would:thou wouldst= rest peaceably, =ifplayerplural:ye are:thou'rt= welcome here.

**Choices:**
- **choice** `?` → `ViviQuest`
    > Are you Vivira? Zothom sent me.
- **choice** `?` → `ViviFriendly`
    > You are friendlier than most turrets.
- **choice** `?` → `ViviWelcome`
    > What is this place?
- **choice** `?` → `End`
    > Farewell, Lightspitter.

### Node `ViviQuest`

*crackle, crackle*-othom? My sympathies.

        =ifplayerplural:Ye are:Thou art= of course welcome here, wayfarer. Speak to Agyra an =ifplayerplural:ye need:thou needest= aught, as ey delighteth in hospitality.

**Choices:**
- **choice** `?` → `ViviZothom`
    > Why are you offering me sympathies?
- **choice** `?` → `ViviWelcome`
    > What is "here"?
- **choice** `?` → `ViviFriendly`
    > You're much nicer than most turrets I meet.
- **choice** `?` → `End`
    > I see. Farewell.

### Node `ViviZothom`

*crackle-sigh*

        I was being petty. The little time Zothom spent here felt like weeks, so conceited and aggressive was his grief. But Agyra would chide me for saying so. I have a long road to true self-realization, I realize.

        But if you ask me, Zothom's road is far longer. *BEEP*

**Choices:**
- **choice** `?` → `ViviFriendly`
    > You're rather civil for a turret.
- **choice** `?` → `ViviWelcome`
    > What is this place?
- **choice** `?` → `End`
    > Live and remain rustless, Vivira.

### Node `ViviFriendly`

So I am told. I have never had the pleasure nor displeasure to meet another turret. I know only my friends here, who uplifted me by chance and cared for me by choice.

        Wer't not for my shape, I wouldst be little different from other mopango.

**Choices:**
- **choice** `?` → `ViviWelcome`
    > What is "here"?
- **choice** `?` → `ViviMopango`
    > What are mopango?
- **choice** `?` → `End`
    > I see. Farewell.

### Node `ViviWelcome`

=ifplayerplural:Ye know:Thou knowest= surely that this is the Tomb of the Eaters, but behind me lieth nestled a settlement occupied by the watchers of the tomb, a small coterie of mopango.

        An =ifplayerplural:ye would:thou wouldst= know more of the settlement, =ifplayerplural:ye:thou= must ask the watcher named Agyra residing within. Ey loveth the sharing of knowledge.

**Choices:**
- **choice** `?` → `ViviFriendly`
    > You're much nicer than most turrets I meet.
- **choice** `?` → `ViviMopango`
    > What are mopango?
- **choice** `?` → `End`
    > I see. Farewell.

### Node `ViviMopango`

Mopango are witnesses of the past and shepherds of the future. We seek peace and harmony through understanding the Kasaphescence and Her many children. We nonetheless eschew conformity, and each of us seeketh a personal credo by which we livest our lives.

        But I am a poor teacher. Speak to Agyra, and =ifplayerplural:ye shall:thou shalt= gain better understanding.

**Choices:**
- **choice** `?` → `ViviCredo`
    > Do you have a personal credo?
- **choice** `?` → `End`
    > I thank you. Farewell.

### Node `ViviCredo`

I do.

        "Form needeth not follow function."

**Choices:**
- **choice** `?` → `ViviTaboo`
    > What does that mean?
- **choice** `?` → `ViviWelcome`
    > What is this place?
- **choice** `?` → `ViviFriendly`
    > You're very thoughtful, as turrets go.
- **choice** `?` → `End`
    > Live and remain rustless, Vivira.

### Node `ViviTaboo`

*BEEP*

        Credos hath no inherent meaning that one may so simply define. So =ifplayerplural:ye know:thou knowest=: asking the meaning of a credo is considered impolite among mopango.

**Choices:**
- **choice** `?` → `ViviSorry`
    > I apologize.
- **choice** `?` → `ViviRude`
    > That's ridiculous.

### Node `ViviRude`

*BEEP*
        Better ridiculous than rude, which =ifplayerplural:ye plainly are:thou plainly art=.

        *crackle* =ifplayerplural:Speak ye:Speakest thou= to Agyra. Ey hast more patience for rudeness than I.

**Choices:**
- **choice** `?` → `End`
    > Very well.

### Node `ViviSorry`

All is forgiven, =player.formalAddressTerm=. I am not wroth with =ifplayerplural:ye:thee=.

**Choices:**
- **choice** `?` → `ViviFriendly`
    > You're rather civil for a turret.
- **choice** `?` → `ViviWelcome`
    > What is this place?
- **choice** `?` → `End`
    > Live and remain rustless, Vivira.
