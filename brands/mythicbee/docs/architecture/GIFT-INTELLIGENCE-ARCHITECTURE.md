# Gift Intelligence Architecture
**Date:** 2026-09-06 03:15 UTC
**Status:** CANONICAL — implement this

---

## The core model

Don't model the interaction as:

```
Question 1 → Question 2 → Question 3 → Recommendation
```

Model it as:

```
                  USER RAMBLE
                       │
             streaming transcript
                       │
                       ▼
             ┌─────────────────┐
             │  BELIEF STATE   │◄────────────┐
             └─────────────────┘             │
              │        │        │            │
           facts   hypotheses  unknowns      │
              │        │        │            │
              ▼        ▼        ▼            │
         GiftBrief  Creative   uncertainty   │
                    Hooks                    │
              │        │                     │
              └────────┼─────────────────────┘
                       ▼
               PACKAGE RANKER
                       │
              predicted best gifts
                       │
             ┌─────────┴──────────┐
             │                    │
       SHOW SOMETHING          ASK SOMETHING
             │                    │
             └─────────┬──────────┘
                       ▼
                    FEEDBACK
                       │
                       └────→ belief state
```

Every 1–3 seconds while someone speaks, the system can be updating:

> **What do I currently believe would make the best gift?**

and separately:

> **What information would most improve that decision?**

---

## Do not start with RL

Start with:

**belief-state inference + deterministic constraints + contextual ranking + contextual bandit experiments.**

Bandits are appropriate because there's an exploration/exploitation problem: should we ask another potentially valuable question, or show the user something already likely to work?

Later, when we have hundreds/thousands of sessions and delayed recipient outcomes, this can graduate into genuine sequential RL.

---

## `GiftState` should be richer than `GiftBrief`

Separate **facts from hypotheses**.

User says:

> "Whenever we're out he'll sit down on a bench every five minutes, stroke someone's dog and somehow end up talking to complete strangers."

Do **not** silently turn that into:

```
dad.lazy = true
```

Instead:

```json
{
  "observations": [
    {
      "text": "On outings he frequently sits on benches, pets dogs and talks to strangers.",
      "source": "transcript",
      "confidence": 1.0
    }
  ],
  "hypotheses": [
    { "trait": "sociable", "confidence": 0.84 },
    { "trait": "dog-loving", "confidence": 0.89 },
    { "trait": "laid-back", "confidence": 0.61 }
  ],
  "creative_hooks": [
    {
      "concept": "Dad in his natural habitat: local park bench, surrounded by dogs and random new friends",
      "strength": 0.92
    }
  ]
}
```

The AI can be creatively intelligent **without pretending its interpretation is objective truth**.

---

## Question selection becomes mathematical

```
QScore(q) =

    phaseFit(q)                × W1
  + expectedInformationGain(q) × W2
  + productDecisionImpact(q)   × W3
  + narrativeYield(q)          × W4
  + contextualRelevance(q)     × W5
  + novelty(q)                 × W6

  - answerEffort(q)            × W7
  - redundancy(q)              × W8
  - privacySensitivity(q)      × W9
  - interruptionCost(q)        × W10
```

Weights **change with stage**:

| Stage | Highest reward |
|-------|----------------|
| 0–20 sec | Narrative yield |
| 20–60 sec | Episodic detail + creative hooks |
| 45–90 sec | Product discrimination |
| Concept stage | Preference information |
| Package stage | Vessel/package preference |
| Pre-checkout | Fulfilment feasibility |
| Post-purchase | Recipient memory + future occasion |

---

## First minute = MEMORY_DIVE

Only objective:

> **Get enough vivid material that MythicBee can create something the customer couldn't have found by browsing a catalogue.**

Flash:

> **What's the most "Dad" thing he's ever done?**

Then:

> **Tell me about a day with them you still talk about.**

Then:

> **What do they do that everyone who knows them recognizes instantly?**

Then:

> **What's something only your family would understand?**

Then:

> **Where are they completely in their element?**

These produce scenes. Scenes produce products.

---

## Memory cue families (100+ bank)

| Cue family | Example | What it gives us |
|------------|---------|------------------|
| Signature behaviour | "What's something they always do?" | Natural Habitat scenes |
| Specific incident | "Tell me about one time they completely outdid themselves." | Story beats |
| Inside joke | "What's something only your family finds funny?" | High-personalization copy |
| Obsession | "What could they talk about for hours?" | Product worlds |
| Place | "Where are they completely themselves?" | Scene/world |
| Ritual | "What do you always end up doing together?" | Relationship identity |
| Contradiction | "What do they pretend not to care about but obviously love?" | Great character insight |
| Catchphrase | "What can you hear them saying right now?" | Card/voice copy |
| Disaster | "What's a story that went horribly wrong and became funny later?" | Comedy narrative |
| Achievement | "What are they secretly proudest of?" | Hall of Fame |
| Era | "What period of their life do they never stop talking about?" | World/time setting |
| Others' view | "How would their best mate describe them?" | Character triangulation |
| Sensory cue | "What instantly makes you think of them?" | Visual/audio motifs |
| Pet dynamic | "What's their relationship with the dog actually like?" | Cast/story |
| Role | "What role do they somehow play in every family gathering?" | Archetype |
| Fantasy | "What would they be absurdly good at in another universe?" | Mythic transformation |

---

## Prompts should change while they ramble

Don't compete with what the customer is currently saying.

Use voice activity detection.

While speech is flowing:

```
prompt remains subtle
```

At a natural pause or after a topic runs dry:

```
next contextual spark fades in
```

The ideal feeling is: **The page is listening.**

---

## AI generates bespoke follow-ups too

The 100+ QBank is the **foundation**, not the ceiling.

```
QBANK
│
├── known safe/high-performing prompts
│
└── objective definitions
       ↓
LLM FOLLOW-UP GENERATOR
       ↓
"Given this transcript and objective,
write one natural question"
       ↓
POLICY CHECK
       ↓
show
```

---

## CreativeHooks as intermediate representation

Don't jump directly: `ramble → product`

Introduce:

```json
{
  "hook": "Dad treats Sunday-league coaching like Champions League management",
  "type": "comic_exaggeration",
  "strength": 0.96,
  "supports": ["gamewinners", "breaking_news", "natural_habitat", "movie_trailer"],
  "assets_needed": ["dad_portrait"],
  "possible_outputs": ["football_card", "mug", "foil_print", "video"]
}
```

A rich ramble might yield 8–20 hooks. Then the system recombines them.

---

## Packages should be generated, not predefined

Don't sell: Mug / Card / Print

Sell:

### World Cup '96 Drama Pack — 9.4/10 match

> Dad finally gets called up. 89th minute. World Cup final. Weak foot. Top bins. Obviously.

Contains: GameWinners card + Legend mug + 60-second commentary reveal

### David in His Natural Habitat — 9.1/10

> One park bench. Six dogs. Three strangers he somehow now knows personally.

Contains: Natural Habitat print + Dog mug + animated mini-scene

### Wenger's Lost Protégé — 8.7/10

> A mock documentary investigating how football inexplicably failed to discover one of its greatest managerial minds.

Contains: Breaking News card + movie-style digital trailer + foil Hall of Fame print

---

## Package ranking

```
PackageScore =

  recipientFit
× creativeHookStrength
× occasionFit
× intendedReactionFit
× assetFeasibility
× historicalConversionPrior
× recipientDelightPrior

+ personalizationNovelty
+ marginScore
+ fulfilmentReliability

- generationRisk
- fulfilmentRisk
- revisionRisk
```

---

## Delay logistics questions

Do **not** open with budget/postcode/deadline.

Instead:

```
MEMORY → IMAGINATION → "I have something." → CONCEPT → DESIRE → PRACTICALITY
```

Bartholomew transitions elegantly:

> "Right. I know what we're making. One boring question before I promise anything impossible: what day is this for?"

---

## Privacy architecture

```
RAW AUDIO        → short-lived unless explicitly saved
RAW TRANSCRIPT   → needed for gift production, then expire
OBSERVED FACTS   → order lifetime / account memory if opted in
AI HYPOTHESES    → short retention unless validated
CREATIVE HOOKS   → order asset
ANONYMISED EVENTS → long-term analytics
RECIPIENT PROFILE → only persistent where appropriate
```

The moat is the **structured outcome data**, not hoarding raw private conversations.

---

## Log the entire causal chain

```
SESSION_STARTED
RAMBLE_STARTED
TRANSCRIPT_CHUNK
PROMPT_EXPOSED
PROMPT_ENGAGED
FACT_EXTRACTED
HYPOTHESIS_CREATED
CREATIVE_HOOK_CREATED
CONCEPT_IMPRESSION
CONCEPT_EXPANDED
CONCEPT_REJECTED
CONCEPT_SELECTED
PACKAGE_IMPRESSION
PACKAGE_SELECTED
PACKAGE_MODIFIED
PRICE_IMPRESSION
CHECKOUT_STARTED
PURCHASED
ORDER_FULFILLED
RECIPIENT_OPENED
REVEAL_COMPLETED
RECIPIENT_REACTION
SHARED
REPEAT_PURCHASE
```

---

## Don't optimize the wrong reward

```
Reward =

  purchase_conversion
+ contribution_margin
+ buyer_satisfaction
+ recipient_positive_reaction
+ recipient_share
+ repeat_purchase
+ successful_delivery

- abandonment
- revision_count
- refund
- late_delivery
- negative_reaction
- excessive_question_cost
```

For the first minute, use intermediate reward:

### NarrativeYield

```
NarrativeYield =
  unique_specific_memories
+ concrete_behaviours
+ relationship_details
+ inside_jokes
+ quotations/catchphrases
+ places
+ named people/pets
+ visualizable_scenes
+ viable_creative_hooks
```

---

## Prototype success criterion

> **Within 60–90 seconds of rambling, can the system extract enough distinctive information to produce three visibly different, surprisingly personal gift-package concepts, explain each in one sentence, and identify which additional question would most change their ranking?**

---

## References

- Dynamic Preference Elicitation: https://arxiv.org/abs/2607.06765
- Conversational Bandits: https://arxiv.org/abs/2209.06129
- ICO AI Accuracy: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/
- Autobiographical Recall: https://pmc.ncbi.nlm.nih.gov/articles/PMC1459336/
- Prodigi API: https://www.prodigi.com/print-api/docs/reference/
- Cross-sell Research: https://baymard.com/blog/product-recommendations-cart
- ICO Storage/Access: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/
