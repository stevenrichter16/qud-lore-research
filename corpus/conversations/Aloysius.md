# Conversation: `Aloysius`

_Inherits: (default: BaseConversation)_

_3 start(s), 11 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Recame`

Ah. It's you again, returning from ever more unreturnable locales. Alive and come to bother the disagreeable urshiib.

**Choices:**
- **choice** `?` → `GuestKlanq`
    > What do you think of Klanq's visit?
- **choice** `?` → `Greetings`
    > Can we talk, Aloysius?
- **choice** `?` → `End`
    > Live and drink.

### Start `Post Arms`

I spent so long preparing for the eventuality that my home might be breached.

        I was not ready. This sense of violation burns like electrocautery.

**Choices:**
- **choice** `?` → `TombQuest`
    > I must enter Brightsheol through the Tomb of the Eaters.
- **choice** `?` → `Greetings`
    > Can we talk, Aloysius?
- **choice** `?` → `End`
    > Live and drink.

### Start `Greetings`

Of course it was only a matter of time before you came to speak to me.

        I don't suppose I can convince you to let me tend to my duties in peace? I know nothing of interest to a wayfarer. Each of my days is like the others; I maintain and protect my children, and this is enough. If I desire conversation, there is Ereshkigal.

**Choices:**
- **choice** `Aloysusa` → `Bethesda`
    > Do you know anything about Bethesda Susa?
- **choice** `Aloyporch` → `Omonporch`
    > What do you know about Omonporch and the self-appointed Earl?
- **choice** `Aloyrumbling` → `Rumbling`
    > Did you feel that rumbling, Aloysius?
- **choice** `Aloyklanq` → `Klanq`
    > Have you ever met Pax Klanq?
- **choice** `Kids` → `Children`
    > You have children?
- **choice** `Introvert` → `Quiet`
    > You don't care for conversation?
- **choice** `Eresius` → `Ereshkigal`
    > Who is Ereshkigal?
- **choice** `?` → `End`
    > Live and drink in peace, Aloysius.

## Nodes

### Node `Start`

I propose an accord, =factionaddress:Barathrumites=: You remove =player.reflexive= from my sight immediately, and I will refrain from asking that Ereshkigal reduce you to your component atoms.

**Choices:**
- **choice** `?` → `End`
    > I'm going, I'm going.

### Node `Start`

Not like this. After all we've accomplished...

**Choices:**
- **choice** `?` → `End`
    > Don't lose hope.

### Node `GuestKlanq`

I did not consider that my life could be further upturned. Truly, I have learned much and I hate it all.

        Once you lot reach the spindle's apex, perhaps you could be convinced to stay there? Or perhaps I could go in your stead.

**Choices:**
- **choice** `?` → `End`
    > We will miss you too, Aloysius. Live and drink.

### Node `TombQuest`

Good. Shut the sarcophagus door behind you.

**Choices:**
- **choice** `?` → `End`
    > Perhaps I will.

### Node `Bethesda`

Bethesda Susa is a vibrant and thriving ecosystem in which we have no place. That said, I certainly would not complain if someone were to clear out its Mechanimist infestation.

        Should you travel there, watch your step. The fronds of a lurking beth can rapidly exsanguinate fleshy creatures such as we.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink in peace, Aloysius.

### Node `Omonporch`

I know that Omonporch is a miserable, hot place and Asphodel is a self-important churl.

        I don't even like bananas.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink in peace, Aloysius.

### Node `Rumbling`

Yes, and I fear the worst. Hie to Ereshkigal. She will know what to do.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink in peace, Aloysius.

### Node `Klanq`

I have met Pax Klanq. I was puffed on.

        Candidly, I prefer fungi edible and inert.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink in peace, Aloysius.

### Node `Children`

My chromelings, my machines, my crops. I tend to them and they tend to me.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink in peace, Aloysius.

### Node `Quiet`

Speaking to other organics is as strenuous to me as any physical exercise.

        My reclusiveness is not born of antipathy; I simply cannot converse as easily as you do and don't wish to learn how.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink in peace, Aloysius.

### Node `Ereshkigal`

Ereshkigal is the mainframe computer of Grit Gate. She keeps watch through the thin world, as she would put it, while we maintain her presence in the thick world.

        I feel as though she and I understand one another.

**Choices:**
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?`
- **choice** `?` → `End`
    > Live and drink in peace, Aloysius.
