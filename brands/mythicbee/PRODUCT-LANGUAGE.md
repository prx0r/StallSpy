# MythicBee — Canonical Product Language
**Date:** 2026-09-06 04:35 UTC
**Status:** FROZEN — this is the company language

---

> **MythicBee — Make it mythical.**

> Bees are the tiny workers of the natural world. MythicBee's bees work for humans instead: learning who matters to them, finding the right idea, taking it to the hive, and getting it made.

"**Bee mythic**" is excellent secondary copy. "Make it mythical" is the stronger primary promise.

---

## The Fiction → Architecture Map

| Product concept | MythicBee language |
|-----------------|-------------------|
| User account | **Your Hive** |
| AI personal shopper | **Your Bee** |
| Shopping/gifting session | **Mission** |
| Cart/basket | **Satchel** |
| Saved unfinished session | **Sleeping Bee** / **Resting Mission** |
| Recommendation engine | **The Hive** |
| User understanding/confidence | **Hive Signal** |
| AI credits | **Honey** |
| Generated idea | **Hive Idea** / **Concept** |
| Multi-agent review | **Hive Council** |
| Order submitted | **Sent to the Hive** |
| Production | **In the Hive** |
| Completed order | **Mission Complete** |
| Past gifts/projects | **Mission Log** |
| Collection of discovered agents | **The Bees You've Met** |
| Favorite agent | **Your Bee** / **Favourite Bee** |
| Seasonal collection | **Seasonal Hive** |

Internal code keeps boring names: `BeeSession`, `GiftState`, `Basket`, `Order`. Customer-facing language gets the fiction.

---

## The Bees Are Personal Shoppers, Not Skins

Each bee has 10–15% meaningful behavioral variation, not a completely different recommendation system.

### Bartholomew III — The Ceremonialist

Bias: impressive gifts, story, occasion significance, premium presentation
Voice: grandiose, reassuring, mildly pompous

> "This is a sixtieth birthday. We are not sending him a keyring."

### Martin — Keeper of Sensible Expenditure

Bias: lowest landed cost, digital + cheap physical combos, strong value bundles
Voice: dry, practical, suspicious of luxury

> "The acrylic is handsome. It is also £17 more. I remain unconvinced."

### Lucifer — Bad Ideas Department

Bias: funniest, strangest, most shareable, maximal transformation

> "Technically we could make him Pope. I see no reason not to."

### Myshkin — Keeper of Small Important Things

Bias: memories, relationships, sentimental details, books/documentaries

### Spinoza — Department of Why This Actually Matters

Bias: fewer gimmicks, strong conceptual connections, deeper story hooks

### Gerald — General Gifts

No meaningful specialization. Somehow incredibly competent. This makes his normality funny.

---

## Bee Selection = User Preference

Customer choosing Martin tells us: `preferred_recommendation_style = value`

Without asking: "Do you prioritize cost-effectiveness?"

---

## The Recommendation Contract

```
Global Gift Intelligence
        +
Bee Bias
        +
User Preference
        +
Current Mission
        =
Recommendation
```

---

## Follow-up Emails Come From the Bee

**From: MythicBee**
**Martin from the Hive**

Subject: Your dad is becoming 61 again.

Body:
> Tom,
> I've checked. It appears your father's birthday is approaching despite everyone's best efforts.
> Last year we made him a football legend. I have two less expensive ideas this time.
> — Martin
> Keeper of Sensible Expenditure

---

## Seasonality Transforms the Hive

### Christmas Hive
- Snowy/warm-lit honeycomb
- Bee wardrobe: scarves, fur hats, antlers
- Departments change: "Borzitov — Emergency Christmas Division"
- Bartholomew: "December. The hive hasn't slept in seventeen days."

### Valentine's
- Myshkin, Casanova Bee, cynical Martin variant

### Father's Day
- Borzitov, Coach Bumble, Martin, "Big Dave"

### Halloween
- Lucifer outranks everyone

---

## The Canonical Lore

> Bees have always been unusually good at finding things.
>
> MythicBee's hive has taken on a slightly more complicated job: finding humans the right gifts.
>
> Every mission gets a bee.
>
> Tell them about them.
>
> They'll take it from there.

---

## The Recurring Lines

> **Make it mythical.**
> **Bee mythic.**
> **Tell me about them.**
> **Every gift gets a bee.**
> **Good stories earn Honey.**
> **I'll take it to the hive.**
> **The hive has an idea.**
> **Mission complete.**

---

## The Naming Pool

Range from brilliant literary references to terrible bee puns to inexplicably mundane humans:

Bartholomew III, Count Buzz, Myshkin, Spinoza, Borzitov, Lucifer, Martin, Gerald, Mittens, Beetrice, Ambrose, Dr. Nectar, Stingbert, Kevin, Clementine, Inspector Bumble, Father Honeywell, Archibald VII, Dave

You need **Geralds and Daves** to make Count Buzz funny.

---

## Desktop vs Mobile

**Mobile:** Bee → conversation → concept feed → preview → pay

**Desktop:** The Hive environment with bee flying, satchel, honey jar, ambient delight

---

## Customer Support Language

> "I was working with Martin yesterday and had a GameWinners mug in his bag."

Support sees:
```
BeeSession: bee_4821
Bee: Martin
Mission: Dad Birthday
State: Resting
Satchel: 3 items
```

Responds: "Found Martin. Your mission is safe."

Playful externally. Incredibly precise internally.
