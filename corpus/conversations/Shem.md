# Conversation: `Shem`

_Inherits: (default: BaseConversation)_

_0 start(s), 10 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

*Shem whispers*

        You're not supposed to be here. But I won't tell.

**Choices:**
- **choice** `?` → `End`
    > Live and drink.

### Node `Start`

Should I hide in the library? I believe it's the clever thing to do.

**Choices:**
- **choice** `?` → `End`
    > Stay safe, Shem.

### Node `Start`

Approach. Be easy. You are my herefriend, my nowfriend.~
        Would you like to read me a story?~
        I know of so many other ways to be.~
        Where does it end?~
        I live, but do I drink?~
        Would you like to eat vapor?~
        Quetzal, I say.~
        *Shem nods.*~
        The gaseous butterfly flits out of the dense worm.~
        I am sharp. I am handy.~
        *Shem yawns.* I am yawning.~
        'Immaculate Chrome' is my favorite.

**Choices:**
- **choice** `ShemSafe` → `YouAreSafe`
    > I'm glad you are safe, Shem.
- **choice** `ShemPax` → `Klanq`
    > What do you think of Klanq's visit?
- **choice** `ShemSpeak` → `Speak`
    > You're a chromeling... that speaks? Can you understand me?
- **choice** `Shem-1` → `-1`
    > Why are you called Shem -1?
- **choice** `ShemFriend` → `Friend`
    > I am your friend, Shem.
- **choice** `ShemEnd` → `End`
    > Live and... remain ever rustless.

### Node `YouAreSafe`

I am glad you are safe, =name=.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Klanq`

I wonder if the distributed consciousness of a fungal entity is similar to that of a distributed machine mind. I shall ask Father when he is not so busy.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Speak`

Is... is this a question trick? I suppose I cannot know what you intend. Can I understand you?

**Choices:**
- **choice** `?` → `Understand`
    > I just meant to ask if you're able to communicate. It seems so.
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Understand`

What kind words. It seems so with you, too.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `-1`

Would you like to hear? When I was first put together by Father and friends, I was Shem 2, the second iteration of the make-me project.

        As I came along, scampered through the halls, listened to the stories Neek read me, climbed onto Sparafucile's workbench to have my screws replaced, I realized I was not what I could be. And so I downgraded myself to Shem 1.

        That has happened three times.

**Choices:**
- **choice** `?` → `Worried`
    > Are you worried that you're getting further away from your ideal self?
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Worried`

It's unclear to me that I should be.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`

### Node `Friend`

I am your friend, =name=.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
