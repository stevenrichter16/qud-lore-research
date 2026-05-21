# Conversation: `Une`

_Inherits: (default: BaseConversation)_

_0 start(s), 17 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Moon and Sun, =player.formalAddressTerm=. You walk the Yd Freehold and are welcome if peaceful.

        Is there aught you need from Une? Need you defending, or cybernetic wares, or are you here for the hurdy-gurdy?

**Choices:**
- **choice** `UneWho` → `Whomst`
    > Who are you?
- **choice** `UneYd` → `Freehold`
    > Tell me about the Freehold.
- **choice** `UneParts` → `Cybernetics`
    > You said you sell cybernetics?
- **choice** `UneHurdy` → `Gurdy`
    > What is a hurdy-gurdy?
- **choice** `UneDying` → `Dying`
    > That thing sounds like a dying animal.
- **choice** `UneGlow` → `Glowing`
    > Are your eyes glowing?
- **choice** `UneListen` → `Listen`
    > I'm just here to listen.
- **choice** `UneBye` → `End`
    > Live and drink.

### Node `Cybernetics`

I did, and I do.

        Are you in the market?

**Choices:**
- **choice** `?` → `Source`
    > Where did you get these implants?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Source`

I found them, here and there.

        Are you interested, or merely fatally curious?

**Choices:**
- **choice** `?` → `Ignore`
    > Were they in use when you found them?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Whomst`

I am called Une. "Warden" Une, when someone needs to wear authority for outsiders.

        And you? What's your name?

**Choices:**
- **choice** `?` → `Whomst2`
    > I am =name=.
- **choice** `?` → `Snub`
    > None of your business.

### Node `Whomst2`

Lovely to meet you, =name=.

        Now. Need a question answered, a tune played, a body upgraded?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Snub`

*Warden Une tilts their head and purses their lips*

        Very well. Need you aught, O Nameless One?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Freehold`

Oh, I am hardly an unbiased observer, I'm afraid -- the Freehold is the only welcoming home I could ever have imagined for myself, and my home before was worse than most. I feel a freedom and responsibility here that I would know nowhere else. That no one else could ever know at all.

        But bias aside, you can see for yourself that we are a collective thriving without hierarchy. I'm rightly proud to defend that.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Gurdy`

An old, old, old, old music machine.

        Well, I suppose this one is not so old. This one I commissioned from a wandering artisan whose life I saved. A story for another time. Surely you've business.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Dying`

Oh, so it called to you, a fellow dying animal?

**Choices:**
- **choice** `?` → `Dying2`
    > I'm not a dying animal.
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Dying2`

You are a dying animal. So am I. We are all dying animals, scrabbling for what extra scraps of time we can grasp. Even the eons-old. We are each and every one of us a dying animal. Or plant. We all decay, is the point.

        And the hurdy-gurdy doesn't like how you sound either, for what it is worth.

**Choices:**
- **choice** `?` → `Dying3`
    > Is this how you always greet visitors?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Dying3`

Is this how you always visit settlements?

        No. Do not answer. Is there aught you need?

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Glowing`

Of course my eyes do not glow. You see the glint of my mask's optics.

**Choices:**
- **choice** `?` → `Shield`
    > Your shield bears resemblance to a Templar's Aegis.
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Shield`

If it were a Templar's Aegis, it would bear the holy rhombus.

        No knight would be caught dead carrying this blank slate.

**Choices:**
- **choice** `?` → `Ignore`
    > Where did you get it?
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Ignore`

*one long, luminous stare*

        I think it best if we kept to more practical questions.

**Choices:**
- **choice** `?` → `Sorry`
    > I apologize for prying.
- **choice** `?` → `Pushing`
    > I insist you tell me.
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Sorry`

I am not wroth with you, but I owe you no conclusions so easily grasped.

        All the same, consider yourself forgiven if you wish. Sit and listen to my hurdy-gurdy and we shall be friends.

**Choices:**
- **choice** `?` → `End`
    > Very well.

### Node `Pushing`

I ken not why you thirst for truths not yours to consume. If I refuse, will you wrench them from my mouth as I wrench teeth from yours? What does that gain you?

        Sit down, fool. Listen to music and calm yourself.

**Choices:**
- **choice** `?` → `End`
    > ...

### Node `Listen`

Then you are welcome. Make comfort as you need and I will play.

**Choices:**
- **choice** `?` → `End`
    > ...
