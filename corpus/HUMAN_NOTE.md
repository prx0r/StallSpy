# The Human Note — Operator State Capture

**Date:** 5 September 2026
**Core insight:** The human note captures latent state that observable business data cannot recover reliably.

---

## What the Human Note Adds

Logs tell a future agent: "You changed the thumbnail at 14:32, spent $3.20, sales increased."

The human note tells it: "I almost didn't launch this because I thought the result looked slightly cheap. I'm intentionally shipping anyway because I think I'm over-optimizing quality before validating demand."

It captures **why the trajectory took the shape it did**.

---

## Six Missing Variables

### 1. Belief State

What did you believe **before** seeing the outcome?

> "I currently think Game Winner is stronger than MythicBee because the buying intent is clearer."

Lets a future agent distinguish prediction → result rather than retrospectively inventing reasons.

**Probably the most valuable field.**

### 2. Uncertainty

> "I'm 55% convinced this is worth its own shop."
> "I'm worried we're making the product too complicated."
> "I have no idea whether anyone will pay £20 for the physical bundle."

Lets an agent learn **where uncertainty existed and how it resolved**.

### 3. Motivation Behind an Action

`lower_price: £9.99 → £6.99` could mean:

- increase conversion
- sacrifice margin to get first reviews
- test price elasticity
- liquidate a failing product

Telemetry doesn't know. The operator note does.

### 4. Constraints Not Visible in Data

> "I only have $40 left so I can't test ads."
> "I could spend five more hours improving this, but I'm deliberately stopping because shipping matters more."
> "I hate doing customer support manually, so I'm weighting automation unusually highly."

Without this, a future agent might conclude "the optimal decision was X" when X was simply unavailable.

### 5. Counterfactuals

> "I considered opening three shops today but decided against it because we'd fragment reviews."

Now the corpus contains an **unchosen branch**.

```text
State
├── action actually taken
├── alternative considered
└── why alternative was rejected
```

Normal business data only records the branch that happened.

### 6. Human Intuition / Weak Signals

> "There's something about this product that people immediately understand."
> "The samples look technically good but don't feel giftable."
> "This customer message makes me think we're solving the wrong problem."

Sometimes this intuition will be wrong. Excellent. Now the dataset can measure **when human intuition was predictive and when it wasn't**.

---

## The Operator State Schema

### Morning

```json
{
  "date": "2026-09-06",
  "objective": "Get MythicBee's first product live",
  "current_beliefs": [
    {"claim": "Birthday is the best first buying intent", "confidence": 0.78},
    {"claim": "Customers care more about likeness than 4K", "confidence": 0.66}
  ],
  "main_plan": ["finish Birthday V1", "test on five dogs", "publish if >=4 pass"],
  "concerns": ["generation costs may kill £4.99 economics", "product may look obviously AI-generated"],
  "constraints": {"cash_available_usd": 45, "hours_available": 6},
  "alternatives_considered": ["build Natural Habitat instead", "open Game Winner first"],
  "success_condition": "4/5 test dogs produce commercially acceptable output",
  "kill_condition": "average accepted output costs more than £2"
}
```

### Evening

```json
{
  "surprises": ["H3 identity consistency was much better than expected"],
  "mistakes": ["spent too long attempting native 4K"],
  "belief_updates": [
    {"claim": "1080p/upscaled output is sufficient", "before": 0.55, "after": 0.87}
  ],
  "emotional_signal": {
    "confidence_in_business": 0.74,
    "uncertainty": 0.39,
    "energy": 0.66
  },
  "tomorrow_intent": "publish listing rather than improving generation further"
}
```

You don't need to manually fill this JSON. You speak naturally for 60–180 seconds and the extraction agent produces it.

---

## Voice Is Better Than Typing

Typing becomes **edited reasoning**.

Voice produces things like:

> "I dunno, this feels weird because…"

Those hesitations are information.

> "Technically this one looks better, but I'd buy the other one."

That is a valuable preference signal that may never appear in Git, metrics or structured fields.

Keep:
- raw audio permanently
- → transcript
- → structured extraction
- → embedding
- → linked decisions

Future models may derive useful information from tone/prosody too. Keeping the source costs almost nothing.

---

## Don't Sound Smart

The best operator note is messy:

> "I'm annoyed because I wasted two hours on this."
> "I really want to build the AR thing but I know that's probably me avoiding launching."
> "This seems too obvious, which weirdly makes me distrust it."
> "I think this product is good but I wouldn't personally spend £20 on it."
> "Three people asked basically the same question today."

Much more useful than polished commentary.

An agent can later discover:

> Whenever the operator reported "this feels too complicated," products subsequently underperformed.

or:

> Operator enthusiasm had no predictive value, but repeated unsolicited customer questions were highly predictive.

---

## The Agent Should Learn From You, Not Become You

Separate:

| Type | Example |
|------|---------|
| **Generalizable principle** | Focused specialist storefronts increased trust |
| **Operator-specific preference** | Tom strongly dislikes repetitive manual fulfillment |
| **Temporary constraint** | Cash available was only $40 |
| **Emotional state** | Operator was unusually pessimistic after a failed generation |

Then it can decide which information transfers to a new owner's situation.

---

## The Three Synchronized Timelines

### 1. Internal Timeline
What the human/operator believed, feared, intended and noticed.

### 2. Action Timeline
What humans and agents actually did.

### 3. Economic Timeline
What the market actually rewarded or punished.

Everything gets linked:

```text
HUMAN
"I think customers don't trust the likeness."
        ↓
DECISION
show real input → output examples
        ↓
ACTION
listing hero changed
        ↓
MARKET
CTR +8%  conversion +31%  refunds unchanged
        ↓
BELIEF UPDATE
trust hypothesis strengthened
        ↓
PRINCIPLE
generative personalization benefits from explicit proof
```

**That's the corpus.**

The uniqueness isn't just a year of Etsy data.

It's the normally invisible bridge between **human judgment → agent execution → market consequence**.

If this experiment becomes materially successful, that is exactly the kind of history an autonomous commerce agent should study before being given control of real capital.
