# GiftGraph — The Data Moat
**Date:** 2026-09-06 03:05 UTC
**Status:** CANONICAL — this is the real product

---

Yes. The **data layer may become more defensible than the image/video/world-generation layer**.

Moonpig essentially proves the thesis. In FY26 it called proprietary customer data one of its biggest competitive advantages: **113 million occasion reminders**, around **40% of orders placed within seven days of a reminder**, and **89.4% of Moonpig/Greetz revenue from existing customers**. It explicitly says the next step is deeper understanding of **relationships, occasions and gifting intent**, then using that to improve recommendations and gift attachment. Its gift attach rate is currently 17.9%. ([Moonpig Group][1])

MythicBee can collect something considerably richer than Moonpig because they generally learn from **what card you bought**; we can learn from **what you said about Dad, what three ideas you were offered, which you rejected, which you modified, what you paid for, what physical form you chose, how close to the occasion you ordered, and whether the recipient actually engaged with it.**

That is the moat.

# The real data asset: `GiftGraph`

I would stop thinking of our database as "orders" and think of it as three related graphs.

| Layer                  | What we learn                                                                | Why valuable                                 |
| ---------------------- | ---------------------------------------------------------------------------- | -------------------------------------------- |
| **Relationship Graph** | giver → recipient → relationship → occasions                                 | Predict future gifting needs                 |
| **Taste Graph**        | person traits → creative concepts → chosen/rejected products                 | Learn what gifts work for whom               |
| **Outcome Graph**      | recommendation → price → purchase → revision → delivery → recipient reaction | Learn what actually produces delight/revenue |

A returning user could eventually have:

```text
Tom
│
├── Dad
│   ├── birthday: Oct 18
│   ├── Father's Day
│   ├── football
│   ├── dry humour
│   ├── dislikes overly sentimental gifts
│   ├── Arsenal
│   ├── dog: Dave
│   ├── 2026 → GameWinners / mug / £34
│   └── recipient watched reveal + shared it
│
├── Mum
│   ├── birthday...
│   └── ...
│
└── Partner
    └── ...
```

The next year the UX doesn't start with:

> What is your dad interested in?

It starts with:

> "Your dad's birthday is coming up. Last year we made him the 99-rated striker he apparently believes he is. Shall we top it?"

That's a retention machine.

Moonpig's own data explains why this is powerful: **88% of card purchases are tied to annually recurring events**, while an average UK card buyer buys about 19 cards per year but an existing online buyer buys online for only around three of those occasions. ([Moonpig Group][2])

So every recipient relationship potentially represents years of repeat purchases.

---

# But raw personal data is not the moat

This distinction is critical.

A giant warehouse of raw conversations such as:

> "Dad has diabetes, voted Conservative, divorced Mum after an affair, likes Arsenal…"

is **liability**, not moat.

The useful asset is the transformed, minimized signal:

```json
{
  "relationship": "father",
  "occasion": "60th_birthday",
  "humour": 0.87,
  "sentimentality": 0.34,
  "sports_affinity": 0.91,
  "football_club": "Arsenal",
  "pet_inclusion": true,
  "gift_style": ["funny", "showpiece"],
  "negative_preferences": ["soppy"],
  "deadline_days": 4
}
```

And especially:

```json
{
  "shown": ["gamewinners", "breaking_news", "legend_book"],
  "chosen": "gamewinners",
  "rejected": ["breaking_news", "legend_book"],
  "physical_choice": "mug_plus_card",
  "price_paid": 34,
  "revisions": ["more smug", "include dog"],
  "recipient_opened": true,
  "recipient_shared": true
}
```

That second dataset is spectacular.

It gives us **preference pairs**:

> For a sarcastic 60-year-old football Dad with a pet, the customer preferred GameWinners over a documentary.

Eventually we can train/rerank against hundreds of thousands of these decisions.

World models can commoditize.

That dataset cannot simply be downloaded.

---

# The highest-value data isn't what someone tells us

It is the difference between:

**what they said → what we inferred → what we offered → what they chose → what happened.**

That's extraordinarily valuable supervised data.

Think:

```text
RAMBLE
  ↓
GiftBrief
  ↓
3 recommendations
  ↓
explicit preference
  ↓
preview
  ↓
revision
  ↓
purchase
  ↓
physical vessel
  ↓
recipient engagement
```

Every single stage generates labels for the stage before it.

That lets us improve:

```text
ramble → understanding
understanding → concept
concept → physical product
product → price
price → conversion
deadline → fulfilment
recipient → reaction
```

This is the actual Gift Intelligence system.

---

# Your "20 Questions" idea is exactly right — but don't ask 20 questions

Have a **bank of 20 useful dimensions**.

The customer rambles first.

The model fills perhaps 13 automatically.

Bartholomew asks only the 3–6 where either confidence is low or the answer materially changes the recommendation.

That's why it feels magical instead of like filling in a tax return.

## The 20-question bank

| Question / inferred dimension                                    | What it tells us               | Product consequence            |
| ---------------------------------------------------------------- | ------------------------------ | ------------------------------ |
| **1. Who is this for?**                                          | relationship                   | entire recommendation prior    |
| **2. What's the occasion?**                                      | purchase mission               | product + copy                 |
| **3. When do you need it?**                                      | urgency                        | **huge fulfilment signal**     |
| **4. Tell me about them.**                                       | unstructured gold              | interests/personality/memories |
| **5. How old are they / milestone?**                             | life-stage                     | 18/30/40/60 etc. concepts      |
| **6. What makes them them?**                                     | identity anchors               | creative hooks                 |
| **7. What do you always joke about?**                            | insider knowledge              | humour/personalization         |
| **8. What's one memory you'd definitely include?**               | emotional specificity          | narrative scenes               |
| **9. What do they care about far too much?**                     | obsession                      | GameWinners/collector/etc.     |
| **10. What would they absolutely hate?**                         | negative preference            | avoids bad recommendations     |
| **11. Funny, moving, impressive or ridiculous?**                 | intended reaction              | engine/style                   |
| **12. Which of these three feels most like them?**               | **explicit preference label**  | recommendation training        |
| **13. Which one would they actually keep?**                      | durable-value preference       | mug/print/book/acrylic         |
| **14. Would they put something on a wall, desk, or use it?**     | physical behavior              | vessel selection               |
| **15. Do you have good photos?**                                 | asset quality                  | generation feasibility         |
| **16. Any pet/person who must appear?**                          | cast                           | composition                    |
| **17. How elaborate should we go?**                              | effort/value expectation       | quick vs premium               |
| **18. Rough budget?**                                            | willingness to pay             | SKU/range                      |
| **19. Where does it need to go?**                                | fulfilment                     | Prodigi quote/routing          |
| **20. Of these finished ideas, which would you spend money on?** | **true commercial preference** | pricing/product definition     |

Questions 3, 10, 12 and 20 are particularly valuable.

**"When do you need it?"** tells us not only which SKU is feasible but produces the distribution of buying horizons:

```text
same day
1 day
2–3 days
4–7 days
1–2 weeks
2+ weeks
```

That tells us whether Late Gift Panic deserves investment, which products need Express versions and how much inventory/production-speed value exists.

**"What would they hate?"** is arguably better than asking another interest question because gifting failure is highly asymmetric.

**"Which of these feels most them?"** generates clean preference pairs.

**Showing real prices before asking "which would you choose?"** gives us willingness-to-pay data rather than abstract preference.

---

# The initial ramble should come first

This is where your UX instinct is strong.

Homepage:

> **Tell me about someone you love. Ramble. I'll work out the gift.**

No account.

No "relationship" dropdown.

No card catalogue.

No budget form.

No occasion selector unless they want one.

Voice or text.

Someone says for 45 seconds:

> "It's my dad, his birthday is next Friday, he's turning 60, supports Arsenal, has a Labrador called Dave, he's impossible to buy for because he basically buys anything he wants, he's really sarcastic, he coached me when I was a kid and still claims he was basically Wenger…"

Behind the scenes:

```text
recipient = dad
occasion = birthday
milestone = 60
deadline = next Friday
sports = football
club = Arsenal
pet = Labrador/Dave
personality = sarcastic
memory = coached user
inside_joke = sees himself as elite manager/player
gift_problem = already buys things
```

Now Bartholomew can actually do something intelligent.

> "Right. I have him."

Then **action**, not another questionnaire.

---

# Flash ideas during the conversation

Exactly.

Don't make them finish an interview before they see value.

Something like:

```text
Bartholomew:
"Sixty, Arsenal and still thinks he could play?"

        [GameWinners animates in]

"I may have found the obvious one."

   TURN DAD INTO A 99-RATED LEGEND
       [see it]

"But Dave being involved gives me another idea..."

       [Dogcasso / mascot concept]
```

Then the customer clicks one.

That click is a **data label**.

Perhaps they ignore it and keep talking.

Also a label.

Perhaps they click GameWinners but later buy a book.

Another useful label.

The interface becomes continual active learning.

---

# I would not deliberately use emotional investment as a pressure mechanism

Getting somebody talking first is excellent because it gives us better inputs and reduces the work of selecting a gift.

But design it around:

> "You've told us enough to make this good."

rather than:

> "You've spent five minutes here, don't leave now."

That line matters both ethically and commercially. The brand needs to feel trusted with memories.

---

# Accounts: your instinct is almost right, but go even further

**Do not require Google authentication to buy.**

Baymard's latest checkout research says 18–19% of surveyed shoppers report abandoning orders because of forced account creation. Their recommendation is prominent guest checkout and, if desired, account creation **after the purchase**. ([Baymard Institute][3])

I would do:

```text
ARRIVE
anonymous session
    ↓
RAMBLE
    ↓
concept
    ↓
preview
    ↓
BUY
    ↓
Apple Pay / Google Pay / PayPal / Stripe
    ↓
ORDER COMPLETE

"Want me to remember Dad for next year?"
[Continue with Google]
```

That's substantially better.

Stripe/payment already obtains the minimum transactional details we need.

Then:

> **Save Dad & remind me next year**

is an obvious reason to create an account.

Not:

> Create account because websites have accounts.

---

# Anonymous data can merge into the account later

Give every visit:

```text
session_7CK29
```

It owns:

```text
GiftBrief
events
concepts_shown
choices
uploads
preview
cart
```

At checkout:

```text
session_7CK29
      ↓
order_98AF1
```

If they sign in:

```text
session_7CK29
      ↓
user_123
      ↓
recipient_dad_01
```

So we lose essentially nothing by delaying auth.

---

# Does having an account make people pick different things?

This is exactly the type of question we should answer, but be careful statistically.

If logged-in people spend £8 more than anonymous people, that **doesn't mean logging in caused them to spend £8 more**.

Returning customers are inherently different.

Moonpig, for example, says its Plus members set more reminders, purchase more frequently and have higher gift attachment—but that population is obviously highly selected. ([Moonpig Group][4])

So store:

```text
account_state
new_vs_returning
recipient_known
prior_recipient_orders
prior_customer_orders
device
traffic_source
```

But when we want causality, run experiments.

For example:

```text
50%:
offer "remember Dad" after preview

50%:
offer it after purchase
```

Then compare conversion cleanly.

---

# Buyer archetypes: don't make mobile and desktop the archetypes

Device is a **contextual signal**.

The archetype is the job they are trying to do.

Baymard's mobile studies show mobile ecommerce often converts much worse than desktop and that the smaller interface amplifies friction. ([Baymard Institute][5])

So your mobile/desktop intuition is directionally sensible, but I wouldn't force:

> mobile = quick
> desktop = creative

Instead infer a `shopping_mode`.

| Mode                             | Signals                                 | Experience                     |
| -------------------------------- | --------------------------------------- | ------------------------------ |
| **Panic buyer**                  | deadline ≤2 days, mobile, search intent | fastest viable gift            |
| **Mission buyer**                | knows recipient + product               | minimal conversation           |
| **Inspiration buyer**            | "no clue what to get Dad"               | ramble → recommendations       |
| **Emotional creator**            | lots of memories/assets                 | richer narrative products      |
| **Studio creator**               | many edits, desktop, exploration        | advanced controls              |
| **Returning relationship buyer** | known Dad/Mum/partner                   | one-tap personalization        |
| **Occasion planner**             | weeks early/reminder driven             | premium products/books         |
| **Social/template browser**      | arrived via Reel/TikTok                 | template-first → insert person |

Then device changes the presentation.

---

# Mobile should feel almost like messaging

I'd make mobile:

```text
Bartholomew
      ↓
large hold-to-talk button

"Tell me about them"

      ↓
voice transcript appears
      ↓
horizontal concept cards
      ↓
tap one
      ↓
photo picker
      ↓
instant preview
      ↓
Apple/Google Pay
```

No sidebars.

No giant editors.

No complicated layer controls.

If someone arrives from TikTok/Instagram, you can invert it:

```text
[vertical reel demo]

TURN YOUR DAD INTO THIS
     [Try mine]

photo
↓
30-second ramble
↓
preview
```

That is a second acquisition loop.

---

# Desktop should expose the studio progressively

Same underlying order.

But once they show creative intent:

```text
person panel
concepts
physical formats
style variations
timeline
images
world preview
card preview
```

They can say:

> "Put Dave on the bench."

> "Make Dad's rating 98, not 99 because he'll complain."

> "Show me the foil version."

That's the MythicBee Studio.

But it remains conversational rather than Photoshop.

---

# Moonpig gives us a particularly important clue: card-first → gift attachment

Moonpig says physical cards are its entry point into the much larger gifting market, and it uses data gathered during card personalization to recommend gifts. Its FY26 gift attach rate reached **17.9%**. ([Moonpig Group][6])

That suggests an excellent MythicBee structure:

> **Create the moment first. Choose how big you want to make it second.**

Not:

> Pick Mug / Poster / Card / Acrylic.

Example:

```text
GAMEWINNERS CREATED

Dad is now:
DAVID
OVR 99
"60 YEARS UNDEFEATED"

How should we deliver his legend?

Digital reveal      £9
Card                £19
Mug + card          £29
Foil Hall of Fame   £39
Legend Block        £49
```

Now the **creative work is already done**.

Physical products become simple upgrades.

That's psychologically and operationally much cleaner.

---

# Prodigi gives us some excellent package primitives

These are current public wholesale prices before tax and shipping.

| Physical product           | Prodigi cost from |             Production |
| -------------------------- | ----------------: | ---------------------: |
| Classic personalised card  |         **£1.10** | **24h**, UK fulfilment |
| Fine-art greeting card     |         **£0.75** |          24–72h, UK/EU |
| Standard 11oz mug          |         **£3.64** |       48–72h, UK/EU/US |
| **Magic heat-reveal mug**  |         **£9.00** |                72h, UK |
| Metallic foil print        |         **£2.57** |          72h, UK/EU/US |
| Glow-in-dark print         |         **£2.57** |          72h, UK/EU/US |
| Acrylic prism              |         **£7.00** |          72h, UK/EU/US |
| Softcover book             |         **£6.50** |                    96h |
| Jigsaw + printed metal tin |        **£10.00** |                72h, UK |

([Prodigi][7])

Shipping/taxes matter, so these are **not landed costs**.

Prodigi's quote API can take the actual basket and destination and return products split into expected shipments, fulfilment centres and shipping methods. Mixed products may come from different facilities, in which case shipping costs are combined. ([Prodigi][8])

So our recommendation engine can use **real fulfilment feasibility**, not hard-coded estimates.

---

# GameWinners packages I'd test

### **GameWinners Instant — ~£9**

Digital card + recipient reveal.

No manufacturing.

This catches tonight/tomorrow.

### **GameWinners Card — ~£19**

GameWinners physical card + digital reveal.

Public substrate cost from Prodigi: ~£1.10 before shipping/tax. UK manufacture is 24 hours. ([Prodigi][7])

### **Dad Legend Pack — ~£29–35**

GameWinners card + personalized mug + digital reveal.

Public product cost approximately:

```text
card   £1.10
mug    £3.64
--------------
       £4.74
```

before shipping/tax.

The margin room is huge; generation, acquisition, customer support and shipping are the meaningful costs.

### **Magic Legend Pack — ~£39**

UK only initially.

Card + **heat-sensitive black mug** that reveals Dad's GameWinners artwork when hot water is poured in.

The magic mug itself is currently £9 wholesale and 72h production. ([Prodigi][9])

This is actually a fantastic MythicBee product because the physical object already has a "reveal mechanic" even without AR.

### **Hall of Fame — ~£39**

Card + metallic foil GameWinners print + digital stadium reveal.

The foil print starts at £2.57, and we control exactly where the foil appears. ([Prodigi][10])

Use foil for:

```text
99
player name
trophy
border
MYTHIC / LEGEND rarity
```

### **Legend Block — ~£49**

Acrylic prism + digital reveal, perhaps card too.

The acrylic starts at £7 and is one inch thick with polished edges. ([Prodigi][11])

This is probably our strongest premium non-specialist vessel.

---

# Don't guarantee "one gift box" yet

Prodigi supports multi-item orders, and its connected-store tooling explicitly lets products be added to the same order. ([Prodigi][12])

But different products can route to different fulfilment facilities and therefore different shipments. ([Prodigi][8])

So call it:

**Dad Legend Bundle**

not:

**One beautifully boxed Dad Legend Set**

until we've validated particular combinations actually consolidate reliably.

Later, with volume, we could hold generic branded packaging centrally and create true kits.

---

# The physical package map for the 20 creative families

This becomes simpler than it sounds:

| Experience             | Default        | Natural upgrade      |
| ---------------------- | -------------- | -------------------- |
| **GameWinners**        | card           | mug / foil / acrylic |
| **Dogcasso**           | print          | mug / acrylic        |
| **Legendary Card**     | digital/card   | specialist holo      |
| **CoverStar**          | print          | magazine             |
| **Hall of Fame**       | foil print     | framed foil/acrylic  |
| **MovieStar**          | poster         | acrylic + video      |
| **Legend of Dad**      | card           | book                 |
| **Breaking News**      | card           | magazine             |
| **Birthday Roast**     | card           | mug                  |
| **Dogumentary**        | print          | book                 |
| **First Edition**      | softcover      | hardcover            |
| **Little Legend**      | card           | glow print/storybook |
| **Our Story**          | print          | book/acrylic         |
| **Wedding/VowFrame**   | foil print     | acrylic/book         |
| **Remembered**         | fine-art print | book/acrylic         |
| **Christmas Story**    | card           | glow print/book      |
| **Personalized Comic** | digital        | softcover            |
| **Recipe Legacy**      | digital        | book                 |
| **Private Puzzle**     | digital        | jigsaw tin           |
| **Star Map**           | print          | foil/glow print      |

This means Gift Intelligence recommends an **experience first**, then a **physical vessel**.

That's much better data too.

We separately learn:

```text
Did they like GameWinners?
```

and:

```text
Did they want it as card, mug, foil or acrylic?
```

rather than conflating concept preference with merchandise preference.

---

# The killer data event schema

Every meaningful UI event should look approximately like:

```json
{
  "session_id": "s_abc",
  "user_id": null,
  "recipient_id": null,

  "event": "concept_selected",

  "context": {
    "device": "mobile",
    "country": "GB",
    "traffic_source": "google",
    "search_intent": "60th birthday gift dad",
    "account_state": "guest",
    "deadline_days": 3
  },

  "giftbrief_snapshot": {
    "relationship": "father",
    "occasion": "birthday",
    "milestone": 60,
    "tone": ["funny"],
    "interests": ["football"],
    "confidence": 0.91
  },

  "experiment": {
    "recommendation_model": "gift-ranker-v4",
    "variant": "B"
  },

  "shown": [
    "gamewinners",
    "breaking-news",
    "legend-book"
  ],

  "selected": "gamewinners"
}
```

Do this from day one.

The historical trail becomes extremely hard to recreate later if we throw it away now.

---

# What is legally collectable?

This deserves designing properly before launch.

In the UK, the relevant fundamentals remain lawfulness/transparency, purpose limitation, data minimisation, storage limitation and security. The ICO explicitly says AI systems should have clear purposes for collection and should not collect more than necessary. ([ICO][13])

I would separate data into four buckets.

| Bucket                     | Example                           | Default                              |
| -------------------------- | --------------------------------- | ------------------------------------ |
| **Service data**           | ramble, GiftBrief, uploads, order | collect as needed to provide service |
| **Product analytics**      | steps, concepts viewed/chosen     | collect minimally/aggregate          |
| **Relationship memory**    | Dad's birthday/preferences        | **explicit opt-in**                  |
| **Marketing/profile data** | cross-session targeting           | separate choice / higher caution     |

In 2026 UK law now allows a narrow no-consent exception for storage/access used **solely for statistical website/service improvement**, provided clear information, a simple free objection method, aggregation and no retained individual-level profiling. If you use the same tracking to infer individual preferences or target people, that exception no longer applies. ([ICO][14])

So we can build privacy-friendly aggregate funnel analytics without automatically turning MythicBee into an ad-tech tracker.

---

# The recipient's information is the trickiest part

The buyer is telling us things about **another person**.

That is still personal data if the recipient is identifiable.

UK guidance says that where information is obtained from somebody other than the person it relates to, there are additional transparency obligations; generally the person must be provided privacy information within a reasonable time and no later than one month, or at first communication/disclosure where earlier, subject to limited exceptions. ([ICO][15])

That means this needs a proper privacy design rather than "we can keep everything because the buyer told us."

A reasonable architecture to get reviewed by privacy counsel would be:

```text
raw ramble
    ↓
extract minimum GiftBrief
    ↓
remove unnecessary sensitive facts
    ↓
produce gift
    ↓
raw media/conversation expires
    ↓
retain only opted-in relationship memory
```

And the recipient reveal can contain an obvious lightweight privacy link explaining MythicBee and what information was supplied by the gift sender.

Do not train arbitrary future models on private rambles/photos by default.

Make that a separate, clear decision if we ever want it.

---

# Especially avoid unnecessary sensitive inferences

UK special-category data includes things such as health, race/ethnicity, religion, political opinions and sexual orientation. Inferences can themselves become special-category data. ([ICO][16])

So if someone rambles:

> "Dad had cancer five years ago…"

the gift system may need the text transiently to understand context.

It does **not** need:

```text
recipient.health_condition = cancer
```

permanently attached to Dad's marketing profile.

Likewise normal uploaded photographs are not automatically special-category biometric data. They become especially problematic when subjected to specific processing for unique identification/recognition. ([ICO][17])

There is no reason MythicBee needs facial-recognition identity matching.

Don't build it.

---

# Children deserve particular treatment

Because some gifts will obviously be for children, this should be designed early.

The ICO's Children's Code applies broadly to commercial online services likely to be accessed by UK children, not just products marketed at children, and expects high-privacy defaults, minimisation and particular caution around profiling/nudges. ([ICO][18])

Simplest early product stance:

**buyers must be adults.**

Children can be gift recipients, but recipient profiles for minors should be minimized aggressively and not used for behavioral advertising/profile enrichment.

---

# US: design once rather than retrofit later

California's CCPA probably won't apply to tiny MythicBee by revenue initially—it currently applies to businesses meeting thresholds including $26.625m+ annual revenue, handling 100,000+ California consumers/households in specified ways, or deriving 50%+ revenue from selling/sharing PI. ([California Privacy Protection Agency][19])

But California explicitly treats purchase history, interests and behavioral/inference data as privacy-relevant, and other states have their own regimes. ([California Privacy Protection Agency][20])

So build deletion/export/preferences cleanly from day one.

It is inexpensive now and painful later.

---

# The data moat hierarchy

If I ranked what matters strategically:

**Tier S — proprietary preference/outcome data**

```text
GiftBrief → concepts shown → choice → price → purchase → recipient outcome
```

Almost impossible for a competitor to bootstrap.

**Tier A — Relationship Graph**

```text
customer ↔ Dad
customer ↔ Mum
customer ↔ partner
occasion dates
past gifts
recipient tastes
```

This drives retention.

**Tier A — Deadline × fulfilment data**

```text
order horizon
postcode
recommended product
quoted promise
actual dispatch
actual arrival
```

Eventually we know better than anyone:

> What gift can genuinely reach this person in time?

**Tier B — creative revision data**

```text
"less sentimental"
"make him look younger"
"include the dog"
"change club colours"
```

Wonderful training material for product quality.

**Tier B — recipient response**

```text
QR scanned?
video completed?
AR opened?
shared?
thank-you reaction?
```

This measures delight rather than purchase.

**Low value — generic analytics**

```text
page views
bounce rate
browser
```

Everyone has that.

---

# Recipient reaction could create a second flywheel

Imagine at the end of Dad's GameWinners reveal:

> **That was made for you by Sarah.**
>
> ❤️ Loved it
> 😂 Ridiculous
> 🏆 Keep this forever

One tap.

No account required.

Now we have:

```text
BUYER predicted Dad would love GameWinners
              ↓
Dad actually says ❤️ / shares it
```

That is extremely strong training data.

Then optionally:

> "Someone you love deserves one too."

Recipient becomes acquisition.

Moonpig explicitly talks about recipients becoming customers as part of its brand cycle. ([Moonpig Group][21])

We can make that loop much richer because the recipient has just experienced the digital reveal.

---

# The metric I would obsess over isn't conversion rate

It is:

## **Delight-adjusted conversion**

Something like:

```text
purchase
×
recipient open rate
×
recipient completion
×
recipient positive reaction
×
share/referral
```

A product that converts 5% but gets sent once and ignored may be worse than one converting 4% where recipients scan, laugh and send the site to three friends.

The entire company should optimize:

> **Did we correctly understand the person and produce something the buyer was proud to give?**

Revenue follows that.

---

# So the canonical flow becomes

```text
LAND
 │
 ▼
"Tell me about someone you love."
 │
 ▼
RAMBLE
 │
 ├── GiftBrief filled silently
 │
 ▼
Bartholomew reacts
 │
 ▼
3 personalized CONCEPTS appear
 │
 ├── observe choices
 │
 ▼
1–4 high-information follow-ups
 │
 ▼
LIVE PREVIEW
 │
 ├── revisions become labels
 │
 ▼
"How should we make this real?"
 │
 ├── digital
 │
 ├── card
 │
 ├── mug
 │
 ├── foil
 │
 ├── acrylic
 │
 └── book
 │
 ▼
deadline + postcode
 │
 ▼
real Prodigi feasibility/quote
 │
 ▼
Apple Pay / Google Pay / PayPal / card
 │
 ▼
PURCHASE
 │
 ▼
"Want me to remember them for next year?"
 │
 └── Google / account
 │
 ▼
RECIPIENT EXPERIENCE
 │
 ├── scan
 │
 ├── completion
 │
 ├── reaction
 │
 └── referral
 ▼
GiftGraph becomes smarter
```

That's the company.

And there's a particularly beautiful competitive distinction here:

**Moonpig starts with "choose a card."**

MythicBee can start with:

> **"Tell me about them."**

Then we decide whether the answer should be a card, a mug, a foil GameWinners poster, an acrylic block, a book, an animated reel or eventually an AR world.

That's where the data moat becomes much more interesting than a normal personalization shop.

[1]: https://www.moonpig.group/media/moonpig-group-plc-fy26-results-announcement.html?utm_source=chatgpt.com "Moonpig Group plc - Full Year FY26 Results - Results Announcement"
[2]: https://www.moonpig.group/investors/investment-case/?utm_source=chatgpt.com "Investment case | Moonpig Group plc"
[3]: https://baymard.com/blog/current-state-of-checkout-ux?utm_source=chatgpt.com "Checkout UX Best Practices 2025 – Baymard Institute"
[4]: https://www.moonpig.group/media/moonpig-group-plc-fy26-half-year-results-announcement.html?utm_source=chatgpt.com "Moonpig Group plc - Half Year FY26 Results - Results Announcement"
[5]: https://baymard.com/research/mcommerce-usability?utm_source=chatgpt.com "Mobile E-Commerce Usability Guidelines – Baymard"
[6]: https://www.moonpig.group/about-us/market-overview/?utm_source=chatgpt.com "Our markets | Moonpig Group plc"
[7]: https://www.prodigi.com/products/cards-and-stationery/greetings-cards/classic-greetings-cards/?utm_source=chatgpt.com "Print on Demand Classic Greetings Cards - Print API, Dropshipping"
[8]: https://www.prodigi.com/faq/shipping/?utm_source=chatgpt.com "Shipping | FAQ | Prodigi"
[9]: https://www.prodigi.com/products/home-and-living/drinkware/magic-photo-mugs/?utm_source=chatgpt.com "Print on Demand Magic Photo Mugs - Print API, Dropshipping"
[10]: https://www.prodigi.com/products/prints-and-posters/specialist-prints/metallic-foil-prints/?utm_source=chatgpt.com "Print on Demand Metallic Foil Prints - Print API, Dropshipping"
[11]: https://www.prodigi.com/products/home-and-living/tabletops/acrylic-prism/?utm_source=chatgpt.com "Print on Demand Acrylic Prism Prints - Print API, Dropshipping"
[12]: https://www.prodigi.com/faq/integrations/?utm_source=chatgpt.com "Integrations | FAQ | Prodigi"
[13]: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/?q=recruitment&utm_source=chatgpt.com "A guide to the data protection principles | ICO"
[14]: https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-what-does-it-mean-for-organisations/?utm_source=chatgpt.com "The Data Use and Access Act 2025 (DUAA) - what does it mean for organisations? | ICO"
[15]: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/when-should-we-provide-privacy-information/?utm_source=chatgpt.com "When should we provide privacy information? | ICO"
[16]: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/special-category-data/?utm_source=chatgpt.com "Special category data | ICO"
[17]: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/?utm_source=chatgpt.com "What is special category data? | ICO"
[18]: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/introduction-to-the-childrens-code?utm_source=chatgpt.com "Introduction to the Children's code | ICO"
[19]: https://cppa.ca.gov/regulations/cpi_adjustment.html?utm_source=chatgpt.com "Updated Monetary Thresholds in CCPA - California Privacy Protection Agency (CPPA)"
[20]: https://cppa.ca.gov/announcements/2025/20250909.html?utm_source=chatgpt.com "California Privacy Protection Agency Announces Joint Investigative Privacy Sweep: CA, CO, and CT Investigate Businesses Refusing to Honor Consumers' Right to Opt-Out of the Sale of Their Personal Information"
[21]: https://www.moonpig.group/about-us/our-strategy/?utm_source=chatgpt.com "Our strategy | Moonpig Group plc"
