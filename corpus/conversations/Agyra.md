# Conversation: `Agyra`

_Inherits: `BaseSlynthMayor`_

_0 start(s), 27 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`  _IfHaveState=`ChoseNacham`_

=ifplayerplural:Ye have:Thou hast= changed the world, =factionaddress:Mopango=. These strange beings have been confined for thousands of years, and =ifplayerplural:ye have:thou hast= given one a voice.

        If Nacham is as wise as Doyoba believes, we stand to learn much very soon. Perhaps our coterie will spread the knowledge we gain, and we become a step closer to the Kasaphescence.

        =ifplayerplural:Ye are:Thou'rt= welcome to visit and stay here whenever =ifplayerplural:ye will:thou wilt=.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Agyra. Live and drink.

### Node `Start`  _IfHaveState=`ChoseDagasha`_

=ifplayerplural:Ye have:Thou hast= changed the world, =factionaddress:Mopango=. These strange beings have been confined for thousands of years, and =ifplayerplural:ye have:thou hast= given one a voice.

        I cannot help but hold some fear toward Dagasha. However, an it means us no harm I am open to allying with it. No doubt the future of this coterie hath changed, mayhap for the better.

        =ifplayerplural:Ye are:Thou'rt= welcome to visit and stay here whenever =ifplayerplural:ye will:thou wilt=.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Agyra. Live and drink.

### Node `Start`  _IfHaveState=`ChoseVaam`_

=ifplayerplural:Ye have:Thou hast= changed the world, =factionaddress:Mopango=. These strange beings have been confined for thousands of years, and =ifplayerplural:ye have:thou hast= given one a voice.

        That said, I am uncertain what changes to expect. Dost the ancient Va'am yet have the capacity to defend, or protect? Can we gift it with a better means for transportation? I'll speak to Dadogom of this, and time shall reveal all.

        =ifplayerplural:Ye are:Thou'rt= welcome to visit and stay here whenever =ifplayerplural:ye will:thou wilt=.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Agyra. Live and drink.

### Node `Start`  _IfHaveState=`ChoseNacham`_

=ifplayerplural:Ye have:Thou hast= changed the world, =factionaddress:Mopango=. These strange beings have been confined for thousands of years, and =ifplayerplural:ye have:thou hast= given one a voice.

        I find myself amused at Kah's 'rest', for it appeareth as active as ever--far more so than I, ever. But running free and running unwillingly are certainly not the same. Perhaps, in time, it can learn a deeper rest from us.

        =ifplayerplural:Ye are:Thou'rt= welcome to visit and stay here whenever =ifplayerplural:ye will:thou wilt=.

**Choices:**
- **choice** `?` → `End`
    > Thank you, Agyra. Live and drink.

### Node `Start`

Greetings, =player.formalAddressTerm=. =ifplayerplural:Ye are:Thou art= welcome here.

        An =ifplayerplural:ye have:thou hast= any questions, I would fain answer them.

**Choices:**
- **choice** `?` → `Agoninon`
    > What can you tell me of k-Goninon?
- **choice** `?` → `AgyraDevice`
    > I have recovered a repulsive device.
- **choice** `?` → `AgyraGreet`
    > Greetings. I am =name=. Who are you?
- **choice** `?` → `AgyraLeader`
    > Are you in charge here?
- **choice** `?` → `AgyraWelcome`
    > This settlement is... cozy.
- **choice** `?` → `AgyraTomb`
    > What do you know about the Tomb?
- **choice** `?` → `AgyraMopango`
    > Tell me about your people.
- **choice** `?` → `End`
    > Live and drink, plated one.

### Node `SlynthRequest`

=ifplayerplural:Would ye:Wouldst thou= press these slynth into the fissures of historic stone where we reside, that they may observe what we do?

**Choices:**
- **choice** `?` → `SlynthRequestAccept`
    > I would.

### Node `SlynthRequestAccept`

If these slynth wish to become mopango and =ifplayerplural:ye speak:thou speakest= for them, then we shall accept them. Let them gaze into the schematics that wrote history beside us if they so choose.

**Choices:**
- **choice** `?` → `End`
    > You have my thanks, Agyra.
    - _part: `AddSlynthCandidate` (Sanctuary=the mopango hideout)_

### Node `SlynthRequestReject`

Please understand that we mean no slight to =ifplayerplural:you:thee= in saying so, but what =ifplayerplural:ye ask:thou asketh= of us is too heavy a weight for =ifplayerplural:your names:thy name= to bear.
      
      Perhaps this will change, come deed and time.

### Node `SlynthAbout`

How =ifplayerplural:fare ye:farest thou=, then, and what word of the slynth?
      
      We shine with curiosity to hear it.

### Node `SlynthArrived`

The Kasaphescence shine upon =ifplayerplural:ye:thee=, =name=.

        Although the welcome of these slynth be not entirely without incident, I am yet hopeful that their curiosity and dedication to tasks will serve them well among us.

**Choices:**
- **choice** `?` → `Start`
    > My thanks, Agyra.

### Node `SlynthSettled`

These lilypad folk fascinate by their similarities and differences to us alike--we have much to explore, as individuals and together.

        The experiences and beings =ifplayerplural:ye herald:thou heraldest= overwhelm this humble pilgrim, =name=. May =ifplayerplural:ye:thou= bathe ever in Her light.

**Choices:**
- **choice** `?` → `Start`
    > My thanks again, Agyra.

### Node `AgyraDevice`

Oh, so =ifplayerplural:ye have:thou hast=, and what a sight. Please forgive my distance, but I am loath to touch it.

        It appeareth of similar make to the children, and I believe its jaw seeketh them. Lebah claimeth that the device grants freedom, and I wonder what that freedom will look like. Perhaps =ifplayerplural:ye should:thou shouldst= speak to the watchers of the children for further insight.

**Choices:**
- **choice** `?` → `End`
    > Understood. Live and drink, Agyra.

### Node `Agoninon`

=ifplayerplural:Seek-ye:Seekest-thou= the repulsive device, then?

        k-Goninon, ancient and venerated gelatinous cupola, doth patrol the catacombs. Arrived centuries ere we discovered this place, k-Goninon hath hardened and eateth not through the floor, and yet it eateth prodigiously. Safe from the conservators, as k-Goninon long ago consumed the Mark of Death itself.

        Please be careful. k-Goninon hath devoured watchers and wouldst devour =ifplayerplural:ye:thee= as well.

**Choices:**
- **choice** `?` → `End`
    > I will be careful. Live and drink.

### Node `AgyraGreet`

I am Agyra, a watcher of the tomb.

**Choices:**
- **choice** `?` → `AgyraGender`
    > May I call you man, woman, or something else?
- **choice** `?` → `AgyraLeader`
    > Are you in charge here?
- **choice** `?` → `AgyraWelcome`
    > It's a cozy home you have here.
- **choice** `?` → `AgyraTomb`
    > What do you know about the Tomb?
- **choice** `?` → `AgyraMopango`
    > Tell me about your people.
- **choice** `?` → `End`
    > Live and drink, Agyra.

### Node `AgyraWelcome`

I hope it is not overly crowded for =ifplayerplural:ye:thee=. We mopango are most comfortable in close quarters, but I acknowledge that not all creatures adore the close embrace of the depths as we do.

        Regardless, =ifplayerplural:ye are:thou'rt= welcome to stay and sup, and ask of me any questions =ifplayerplural:ye may:thou mayest= have.

**Choices:**
- **choice** `?` → `AgyraGreet`
    > I am =name=. Who are you?
- **choice** `?` → `AgyraLeader`
    > Are you in charge here?
- **choice** `?` → `AgyraWelcome`
    > This settlement is... cozy.
- **choice** `?` → `AgyraTomb`
    > What do you know about the Tomb?
- **choice** `?` → `AgyraMopango`
    > Tell me about your people.
- **choice** `?` → `End`
    > Thank you. Live and drink.

### Node `AgyraLeader`

No one leadeth us. We mopango hold little regard for hierarchy, and our shared decisions are made through discussion, quiet consideration, and consensus.

        Shouldst be otherwise?

**Choices:**
- **choice** `?` → `AgyraAssent`
    > I suppose not.
- **choice** `?` → `AgyraWelcome`
    > It's a cozy home you have here.
- **choice** `?` → `AgyraTomb`
    > What do you know about the Tomb?
- **choice** `?` → `AgyraMopango`
    > Tell me about your people.
- **choice** `?` → `End`
    > Live and drink, Agyra.

### Node `AgyraAssent`

*Agyra smiles at you, glowing softly.*

**Choices:**
- **choice** `?` → `AgyraWelcome`
    > It's a cozy home you have here.
- **choice** `?` → `AgyraTomb`
    > What do you know about the Tomb?
- **choice** `?` → `AgyraMopango`
    > Tell me about your people.
- **choice** `?` → `End`
    > I should take my leave. Live and drink.

### Node `AgyraMopango`

We are mopango: witnesses of the past and shepherds of the future. The Sacred Light of the Kasaphescence shineth within us, and we commune with relics of antiquity to maintain our humility and grow our wisdom.

        We believe that one day, with enough knowledge, anyone who seeketh the Light shalt find it within emself. In the meantime, we work to become better and brighter as each one of us findeth a personal credo by which to live.

**Choices:**
- **choice** `?` → `AgyraGender`
    > Emself?
- **choice** `?` → `AgyraCredo`
    > Credo?
- **choice** `?` → `AgyraDialect`
    > Why do you speak so strangely?
- **choice** `?` → `AgyraWheels`
    > Why do some of you have wheels?
- **choice** `?` → `AgyraTomb`
    > What do you know about the Tomb?
- **choice** `?` → `End`
    > Live and drink.

### Node `AgyraGender`

Aye. Ey, em, eir, eirs, emself. Thusly do we call ourselves and one another.

        Sex is personal and mattereth not to a bare acquaintence. Gender is a societal relic in which we see no current utility.

**Choices:**
- **choice** `?` → `AgyraQuestions`
    > I see. I have further questions.
- **choice** `?` → `End`
    > Oh. Live and drink.

### Node `AgyraTomb`

The Tomb of the Eaters consisteth of twelve strata, or ten, once =ifplayerplural:ye account:thou accounteth= for transitional levels: the Folk Catacombs (in which =ifplayerplural:ye currently stand:thou currently standeth=), the Crematory and Columbarium, the Two Crypts, and the Six Tombs of Qud's Sultans above.

        An =ifplayerplural:ye seek:thou seekest= fortune here, gird =ifplayerplural:thyselves:thyself= for disappointment. The tomb playeth host to objects wondrous and profane alike, but little of what surface-dwellers considereth treasure.

**Choices:**
- **choice** `?` → `WondrousAndProfane`
    > 'Wondrous and profane?' Now I'm curious.
- **choice** `?` → `AgyraQuestions`
    > I see. I have further questions.
- **choice** `?` → `End`
    > I thank you. Live and drink.

### Node `AgyraCredo`

Aye. One's own credo shouldst inspire reflection and thought, with no clear-cut meaning but meaning nonetheless. Some of our coterie yet seeketh theirs, but an experienced watcher no doubt hath one. Any mopango who hath a credo wilt share it with =ifplayerplural:ye:thee=, an =ifplayerplural:ye request:thou requesteth= it.

        My credo is: "Malice alone staineth the sanctity of questioning."

**Choices:**
- **choice** `?` → `AgyraTaboo`
    > What does that mean?
- **choice** `?` → `AgyraQuestions`
    > I have further questions.
- **choice** `?` → `End`
    > I will ponder this. Live and drink.

### Node `AgyraTaboo`

I cannot simply explain my credo to =ifplayerplural:ye:thee=. A credo informeth and confoundeth at once, and must be reflected upon by the listener.

        =ifplayerplural:Ye are:Thou art= inexperienced in our ways, so please bear my words in the kind spirit they are meant: to ask a mopango to explain eir credo is to commit one of our few taboo acts. Be advised.

**Choices:**
- **choice** `?` → `AgyraQuestions`
    > Hmm. I have further questions.
- **choice** `?` → `End`
    > Thank you. Live and drink.

### Node `AgyraDialect`

Why do we speak strangely? Why =ifplayerplural:do ye:dost thou= speak strangely?

        Is not all speech strange?

**Choices:**
- **choice** `?` → `AgyraQuestions`
    > Hmm. I have further questions.
- **choice** `?` → `End`
    > I see. Live and drink.

### Node `AgyraWheels`

Maladies of the bone are not uncommon in our people. We build devices to assist friends who wouldst otherwise struggle to walk.

**Choices:**
- **choice** `?` → `AgyraQuestions`
    > Ah. I have further questions.
- **choice** `?` → `End`
    > I see. Live and drink.

### Node `AgyraQuestions`

Answering =ifplayerplural:your:thy= questions giveth me satisfaction. Asketh an =ifplayerplural:ye will:thou wilt=.

**Choices:**
- **choice** `?` → `AgyraGreet`
    > May I have your name?
- **choice** `?` → `AgyraLeader`
    > Are you in charge here?
- **choice** `?` → `AgyraWelcome`
    > Isn't this settlement a bit cramped?
- **choice** `?` → `AgyraTomb`
    > What do you know about the Tomb?
- **choice** `?` → `AgyraMopango`
    > May I know more about the mopango?
- **choice** `?` → `End`
    > Never mind. Live and drink.

### Node `WondrousAndProfane`

I admire =ifplayerplural:your:thy= curiosity and hope =ifplayerplural:your:thy= prudence informeth it.

        I have an example at hand. Mere days ago, one of our coterie named Lebah happened upon a repulsive device. Ey was so shaken after attempting communion with the object that ey hath spent less time away from eir nook than ever.

**Choices:**
- **choice** `?` → `AskLebah`
    > Where may I find Lebah? I wish to know more.
- **choice** `?` → `AgyraQuestions`
    > I see. May I ask about something else?

### Node `AskLebah`

Our little sanctuary here hath a fissure in its inner walls. Find that gap and =ifplayerplural:ye will:thou wilt= find Lebah.

        Please be gentle. Ey hath ever been the most insightful reader among us, but beareth the weight of an anxious mind.

**Choices:**
- **choice** `?` → `End`
    > I will. Live and drink.
