# Conversation: `Asphodel`

_Inherits: (default: BaseConversation)_

_0 start(s), 7 node(s), 0 root-level choice(s)_

---

## Nodes

### Node `Start`

Welcome to Omonporch, traveler. Enjoy your visit to my earldom. Feast your eyes upon my tall and glorious Spindle. Take in the scent of roasted musa.

**Choices:**
- **choice** `WhyYours` → `Yours`
    > Are you truly the Earl of Omonporch?
- **choice** `NeedThisLand` → `Lease`
    > Earl Asphodel, the Barathrumites request your permission to lease control of the Spindle. Their inquiries into the past have led them here.
- **choice** `ByeAsphodel` → `End`
    > Live and drink, Earl.

### Node `Yours`

Indubitably, for I've proclaimed it so! There was no Earl to tell me otherwise.

**Choices:**
- **choice** `?`
- **choice** `?`

### Node `Lease`

Lease control of my Spindle, you say? Well, well... That's a colossal request. There's no simple price I can assign to such a thing. Were I to grant such a request, you would owe me a great debt. You and several of your allies.

**Choices:**
- **choice** `?` → `Council`
    > So you say. How can I appease you?
- **choice** `?`

### Node `Council`

I will convene a council. The First Council of Omonporch. Send word to four of your allied factions. Have them send delegates. Together, perhaps, you can appease me.

**Choices:**
- **choice** `?` → `Loved`
    > Hear me, Asphodel. I am a dear friend to the Consortium. I ask that you reconsider.
    - _part: `RequireReputation` (Faction=Consortium Level=Loved)_
- **choice** `?` → `End`
    > Convene the council, then. I am willing.
    - _part: `AngorNegotiation`_
- **choice** `?` → `End`
    > Not today, Asphodel. Live and drink.

### Node `Loved`

Oh... oh! It's you! You are a dear friend, indeed. Of course, of course! You and your bear friends are most welcome to my Spindle.

**Choices:**
- **choice** `?` → `End`
    > You are kind, Earl Asphodel. You have my thanks.

### Node `Start`

Greetings, my viceroy. Sit your rump on a cushion or lie your long back on a kline. Soak in the natural light.

**Choices:**
- **choice** `?` → `Viceroy`
    > Viceroy?
- **choice** `?` → `End`
    > Live and drink, Earl.

### Node `Viceroy`

That's right. I've leased your friends the Spindlegrounds and appointed you viceroy to oversee their operation.

        Welcome to court, asphodelyte. You serve at my pleasure.

**Choices:**
- **choice** `?` → `Start`
    > ...
- **choice** `?` → `End`
    > Live and drink, Earl.
