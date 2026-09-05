# The Prompt Archive — Human Language as Operator Model Training Data

**Date:** 5 September 2026

---

## Why Raw Prompts Are More Valuable Than Structured Data

When you ask an agent to do something, the **way you ask** reveals more than the answer:

> "Can you just quickly make a listing for this" — you're optimizing for speed, not perfection

> "I'm not sure about this but maybe try..." — you're uncertain but exploring

> "Don't spend too much on this" — you're risk-averse on this specific thing

> "Actually wait, what about..." — you just had an insight that changes direction

> "This looks cheap, fix it" — you have aesthetic standards you can articulate

> "I don't care about the details, just get it done" — you're delegating fully on this task

These linguistic patterns are **operator metadata** that never appear in structured data.

---

## What the Prompt Archive Captures

### Management Style Indicators

```
DELEGATOR SIGNALS:
"just do it"
"don't ask me about this"
"you decide"
"whatever works"

MICROMANAGER SIGNALS:
"no, change that to..."
"exactly this color"
"move it 2px to the left"
"not like that, like this"

COLLABORATOR SIGNALS:
"what do you think about..."
"which of these is better"
"help me decide between..."
"I'm leaning toward X but..."
```

### Risk Tolerance Signals

```
CONSERVATIVE:
"let's not spend anything yet"
"can we do this for free"
"is there a cheaper way"
"let's test with a small amount first"

AGGRESSIVE:
"just launch it"
"spend $50 on ads and see"
"let's go all in on this"
"ship now, fix later"

CONTEXTUAL:
"I'd spend on this but not that"
"$10 is fine for testing, $100 is not"
"invest in infrastructure but not marketing yet"
```

### Creative Instinct Signals

```
EXCITEMENT:
"oh that's actually really cool"
"wait this could be huge"
"yes exactly that"
"I love this concept"

AVERSION:
"this feels generic"
"meh, not excited about this"
"it's fine but not special"
"I wouldn't buy this"

TASTE:
"that looks cheap"
"make it more premium"
"the font is wrong"
"this doesn't feel like a real brand"
```

### Avoidance Patterns

```
WHAT THE HUMAN SKIPS:
- never talks about marketing
- avoids customer contact
- procrastinates on pricing
- redirects to infrastructure when launch approaches

WHAT THE HUMAN GRAVITATES TO:
- product concepts
- visual design
- brand naming
- technical implementation
```

---

## The Prompt Processing Pipeline

```text
RAW PROMPT (from OpenCode session)
      ↓
PROMPT EXTRACTOR
      ├── sentiment (positive/negative/neutral)
      ├── uncertainty markers ("maybe", "I think", "not sure")
      ├── delegation signals ("you decide", "just do it")
      ├── risk signals ("don't spend", "test first", "go all in")
      ├── creative signals (excitement/aversion markers)
      ├── avoidance detection (what topics get skipped)
      ├── decision markers ("let's go with", "actually wait")
      └── temporal markers ("today", "this week", "eventually")
      ↓
OPERATOR FEATURES (per session)
      ├── management_style_score
      ├── risk_tolerance_score
      ├── creative_engagement_score
      ├── delegation_level
      ├── avoidance_topics
      ├── decision_speed
      └── uncertainty_level
      ↓
OPERATOR MODEL UPDATE
      ├── update preferences
      ├── update risk calibration
      ├── update creative preferences
      ├── update delegation patterns
      └── update avoidance map
```

---

## The Language → Behavior Link

After 100+ sessions, patterns emerge:

```
WHEN HUMAN SAYS "just do it":
  → 78% of the time, they're happy with the result
  → 22% of the time, they later say "actually change X"
  → Average economic outcome: +$12.40

WHEN HUMAN SAYS "I'm not sure but...":
  → 45% of the time, their instinct was right
  → 55% of the time, agent's alternative was better
  → Average economic outcome: +$3.20

WHEN HUMAN SAYS "this looks cheap":
  → 92% accuracy on aesthetic judgment
  → Average economic outcome: -$8 if ignored, +$24 if addressed
```

Now the agent knows:

> When Tom says "this looks cheap," address it immediately — it's a strong signal with high economic impact.

> When Tom says "I'm not sure," the agent's alternative may be better — worth proposing.

> When Tom says "just do it," the delegation is usually appropriate.

---

## The Autonomy Calibration Loop

The human's language reveals when they want to lead vs follow:

```
HUMAN LEADS:
"Here's what I want to build..."
"I have a vision for..."
"The concept is..."
"My gut says..."

HUMAN FOLLOWS:
"What do you recommend?"
"Which option is best?"
"Help me decide..."
"What would you do?"
```

Track the ratio over time:

```
Day 1:    90% human leads, 10% follows
Day 30:   70% human leads, 30% follows
Day 90:   40% human leads, 60% follows
Day 180:  20% human leads, 80% follows
Day 365:  10% human leads, 90% follows
```

That's the actual autonomy curve. Not imposed — **revealed by the human's own language.**

---

## The Human Queue Design

Based on prompt analysis, the agent populates a queue with decisions that genuinely need human judgment:

### Creative Decisions (human excels)
- Brand name selection
- Concept prioritization
- Aesthetic judgment
- Emotional tone
- "Does this feel right?"

### Strategic Decisions (human leads early, agent later)
- Kill/continue brand
- Resource allocation between brands
- New market entry
- Partnership decisions

### Technical Decisions (agent excels, human verifies)
- SEO optimization
- Price testing
- Listing structure
- Generation parameters
- A/B test design

### Economic Decisions (collaborative)
- Budget allocation
- Ad spend
- Pricing
- Inventory
- Supplier selection

The queue should feel like a smart assistant, not a questionnaire.

---

## What Makes This Different From a Standard Agent

Most agents ask:

> "What should I do?"

Our system asks:

> "Based on everything I've observed about how you think, make decisions, and what you care about — here's what I think you'd want. Do you agree?"

The difference:

```
STANDARD AGENT:
"What do you want?" → Human answers from scratch every time

OUR SYSTEM:
"I predict you'd choose X because [evidence]. Do you agree?"
→ Human confirms, corrects, or overrides
→ Each response refines the model
```

After 30 days, the agent predicts with 70% accuracy.
After 90 days, 80%.
After 180 days, 85%+.

At that point, the human only needs to engage on the 15% of decisions where the agent is uncertain.

**That's the endgame: the human handles the 15% that matters most.**

---

## The Company Structure Implication

This directly answers "what is the human best suited to within this domain?"

The prompt archive reveals:

```
HUMAN EXCELS AT:
- Concept selection (what will people love)
- Aesthetic judgment (what looks premium)
- Emotional intelligence (what will make someone cry/laugh)
- Brand voice (what feels authentic)
- Strategic vision (where this goes in 2 years)

HUMAN IS MEDIOCRE AT:
- SEO optimization
- Price testing
- Data analysis
- Financial forecasting
- Operational efficiency

AGENT EXCELS AT:
- SEO optimization
- Price testing
- Data analysis
- Market research
- Listing optimization
- Content generation
- Routine operations
- Financial tracking
- Competitor monitoring

AGENT IS MEDIOCRE AT:
- Novel concept generation
- Emotional judgment
- Brand naming
- "Would a real person cry at this?"
- Strategic vision
```

So the optimal company structure is:

```
HUMAN: Chief Creative Officer + Chief Strategy Officer
AGENT: Chief Operating Officer + Chief Marketing Officer + Chief Data Officer
```

The human does the 15% that matters. The agent does the 85% that's necessary.

**That's the endgame of the entire project.**

---

*The raw prompts are the most valuable dataset in the system. They capture what structured data never can: how a human actually thinks, decides, avoids, and creates. The language IS the operator model.*
