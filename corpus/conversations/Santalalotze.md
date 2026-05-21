# Conversation: `Santalalotze`

_Inherits: (default: BaseConversation)_

_1 start(s), 8 node(s), 0 root-level choice(s)_

---

## Start nodes (conditional entry points)

### Start `Welcome`

Oh wow, an animal.
        
        Congratulations for... not dying.
        
        ... wanna buy something?

**Choices:**
- **choice** `?` → `Name`
    > I am =name=. Who are you?
- **choice** `?` → `Tree`
    > Are you part of this tree?
- **choice** `?` → `Dangerous`
    > Why are you selling goods in such a remote and dangerous place?
- **choice** `?` → `Animal`
    > Don't call me "an animal."
- **choice** `?` → `End`
    > Live and drink.

## Nodes

### Node `Name`

I am Santalalotze.
      
      ... of ... the Consortium of Phyta. Some call me 'Sant', I think, in
      fantasy or memory.

**Choices:**
- **choice** `?` → `Memory`
    > You don't remember?

### Node `Tree`

No. Well... no, no. I don't think so.
      
      We're just... sharing nutrients.

**Choices:**
- **choice** `?` → `Parasite`
    > So you're a parasite?
- **choice** `?` → `Uncertain`
    > You don't seem sure.
- **choice** `?` → `Questions`
    > May I change the subject?
- **choice** `?` → `End`
    > I see. Live and drink.

### Node `Questions`

Would you? Yes.
      
      What may... can I help with?

### Node `Parasite`

'Parasite' so negative. It's like... ah... economic symbiosis?
      
      Chavvah sustains me, and we are, I am not... them. We are in a... beneficial arrangement, you know. Yes?

**Choices:**
- **choice** `?` → `Uncertain`
    > You don't seem sure about any of this.
- **choice** `?` → `Questions`
    > I'd like to ask you about something else.
- **choice** `?` → `End`
    > Fair enough. Live and drink.

### Node `Dangerous`

It is safe here.
      
      Business is slow, but I've... gotten attached, ahaha.

### Node `Animal`

Buy something, and I will call you 'customer'.
      
      If I remember to.

**Choices:**
- **choice** `?` → `Memory`
    > Are you having some memory trouble?

### Node `Memory`

It's fine. I... forget nothing important.
      
      Or, I don't remember. So no sense worrying. Right?

**Choices:**
- **choice** `?` → `Parasite`
    > Perhaps being Chavvah's parasite is affecting your mind.
- **choice** `?` → `Questions`
    > I'd like to ask you about something else.
- **choice** `?` → `End`
    > Right.

### Node `Uncertain`

Well. Nothing... is like Chavvah. Nothing at all.

      I once thought ... my haustorium carried only lifestuff. Now I am unsure. Am I of Twofirm, now?
      
      It's fine.
    
      Let's... change subjects.
