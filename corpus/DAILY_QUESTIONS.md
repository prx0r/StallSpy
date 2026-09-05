# The Daily Operator Interview — Evidence-Based Question Set

**Date:** 5 September 2026
**Research basis:** Decision journaling literature (Duke, Dalio, Tetlock), entrepreneurial diary research (Dewey, Zimmerman), founder personality studies (Freiberg & Matz 2023), venture success predictors (HBS Eisenmann survey, PSED longitudinal data)

---

## Core Insight

Research shows:

1. **Morning identity intervention increases daily entrepreneurial action** (Stevenson et al. 2023, 201 entrepreneurs, 1458 observations) — simple self-reflection about entrepreneurial qualities in the morning measurably increases action throughout the day.

2. **Decision quality ≠ outcome quality** (Annie Duke, Ray Dalio) — must separate process from luck. The journal captures process; outcomes come later.

3. **"What would change my mind" is the highest-value field** (Tetlock superforecasters) — forces explicit falsification criteria.

4. **Same questions daily = calibration data** — after 30+ entries, you can measure: when human intuition was predictive vs when it wasn't.

5. **Agent-human divergence is itself data** — the gap between what the agent predicts the human will say and what they actually say reveals the operator's unique judgment patterns.

---

## The 12 Daily Questions

Research-backed. Same every day. Takes 2-3 minutes voice or 5 minutes typed.

### MORNING (before work)

**1. What is the single most important outcome today?**
*(Research: goal specificity predicts venture growth — Baum & Locke 2004)*

**2. What do I currently believe will work?**
*(Research: belief state before outcome is the most valuable field for preventing hindsight leakage)*

**3. What am I testing today?**
*(Research: lean startup practices — conducting MVP tests — predict better seed valuation — Eisenmann HBS survey)*

**4. How confident am I this will work? (0-100%)**
*(Research: Tetlock superforecasters — quantified confidence is calibratable; "pretty sure" is not)*

**5. What would prove me wrong?**
*(Research: falsification criteria — the single highest-leverage field in decision journaling — Tetlock, Duke)*

### EVENING (after work)

**6. What actually happened today?**
*(Simple factual summary — what moved, what didn't)*

**7. What surprised me?**
*(Research: surprise signals model-update-worthy information — more valuable than confirming evidence)*

**8. What did I waste time on?**
*(Research: "mistakes" category in agent trajectory labeling — JetBrains Step Rejection 2026)*

**9. What do I now believe that I didn't this morning?**
*(Research: belief update is the core learning unit — Bayesian updating of confidence)*

**10. What is the single biggest risk right now?**
*(Research: pre-mortems — assume failure, identify top 3 risks — Klein, used at Amazon)*

**11. Am I overthinking or underthinking anything?**
*(Research: founders systematically overthink reversible decisions and underthink irreversible ones — Bezos two-way door framework)*

**12. What is tomorrow's bet?**
*(Research: the "main bet" framing — forces prioritization — one thing, not ten)*

---

## Why These 12 Specifically

| # | Question | What It Captures | Research |
|---|----------|-----------------|----------|
| 1 | Single most important outcome | Goal specificity | Baum & Locke 2004: goals → growth |
| 2 | Current belief | Belief state (before outcome) | Prevents hindsight leakage |
| 3 | What am I testing | Lean hypothesis testing | Eisenmann: MVP tests → valuation |
| 4 | Confidence % | Calibration data | Tetlock: superforecasters quantify |
| 5 | What would prove me wrong | Falsification criteria | Duke/Tetlock: highest-value field |
| 6 | What happened | Factual summary | Baseline for comparison |
| 7 | What surprised me | Model-update signal | Bayesian: surprises > confirmations |
| 8 | What I wasted time on | Mistake identification | JetBrains: useful_failure label |
| 9 | What I now believe | Belief update | Core learning unit |
| 10 | Biggest risk | Risk awareness | Klein pre-mortem: top 3 risks |
| 11 | Over/underthinking | Metacognition | Bezos: reversibility framework |
| 12 | Tomorrow's bet | Prioritization | Forces one thing, not ten |

---

## The Agent-Human Divergence Protocol

This is the unique part.

### Daily agent prediction

Before the human answers, the agent (with access to git history, metrics, previous answers) predicts:

```json
{
  "date": "2026-09-06",
  "agent_predictions": {
    "q1_goal": "Launch Birthday V1 listing",
    "q2_belief": "Birthday converts better than generic",
    "q3_test": "New thumbnail",
    "q4_confidence": 72,
    "q5_falsification": "CTR below 2%",
    "q7_surprise": "None expected",
    "q9_belief_update": "No change expected",
    "q10_risk": "Generation cost too high",
    "q12_tomorrow": "Fix first-frame quality"
  }
}
```

### Human answers

```json
{
  "date": "2026-09-06",
  "human_answers": {
    "q1_goal": "Actually I'm going to fix the scraper today",
    "q2_belief": "Honestly I'm not sure Game Winner is right",
    "q3_test": "Not testing anything — just cleaning up",
    "q4_confidence": 45,
    "q5_falsification": "I don't even know what success looks like yet",
    "q7_surprise": "I spent three hours on something I didn't plan",
    "q9_belief_update": "I think I'm building tools instead of products",
    "q10_risk": "I'm avoiding launching because I'm scared it won't work",
    "q12_tomorrow": "Actually launch something"
  }
}
```

### Divergence score

```json
{
  "divergence": {
    "goal_alignment": 0.3,
    "belief_alignment": 0.4,
    "confidence_delta": 27,
    "surprise_delta": 1,
    "risk_delta": 0.8,
    "pattern": "human_more_uncertain_than_agent"
  }
}
```

**After 30 days:** patterns emerge like "agent consistently overestimates human confidence" or "human changes plans 3x more than agent predicts" or "human's evening belief updates are more pessimistic than agent expects."

**After 180 days:** agent can predict human answers with ~70% accuracy. The remaining 30% is where the human's unique judgment lives.

---

## The Problem-Matching Layer

Daily problems identified get tagged and indexed:

```json
{
  "problem_id": "prob_047",
  "date": "2026-09-19",
  "description": "H3 generates good video but face doesn't match reference photo",
  "context": "Dogcasso Birthday V1, customer photo of golden retriever",
  "tags": ["face_identity", "h3", "golden_retriever", "reference_quality"],
  "status": "unsolved"
}
```

Future agent encounters similar problem:

> "Show me historical problems matching 'face identity mismatch in video generation'"

Corpus returns:
- prob_012: same issue, resolved by preprocessing reference images
- prob_028: similar, resolved by switching to first-frame anchoring
- prob_041: same breed, resolved by increasing reference photo count to 5

**Case-based problem solving from accumulated experience.**

---

## The Deterministic Agentic Protocol

This is what it all converges to:

### The $0 → $1M Protocol

```text
INPUT
├── Starting capital ($0)
├── Skills/knowledge (whatever the human has)
├── Time constraint (hours per day)
└── Goal (£1M revenue)

DAILY LOOP
├── MORNING
│   ├── Agent predicts human answers (12 questions)
│   ├── Human answers (voice or typed)
│   ├── Divergence calculated
│   └── Day's plan generated
├── WORK
│   ├── OpenCode sessions → trajectories
│   ├── Git commits → file changes
│   ├── Etsy API → store metrics
│   ├── Financial → costs/revenue
│   └── Generated assets → production data
├── EVENING
│   ├── Human answers (6 evening questions)
│   ├── Agent extracts semantic summary
│   ├── Business state snapshot
│   └── Workday.json created
└── NIGHTLY
    ├── Corpus enriched
    ├── Outcomes attached to past actions
    ├── Playbooks updated
    └── Blog + Short generated

WEEKLY
├── Synthesis video
├── P&L report
├── Experiment leaderboard
├── Hypotheses supported/rejected
└── Next week's bets

MONTHLY
├── Calibration review (agent vs human predictions)
├── Principle extraction
├── Playbook updates
├── Portfolio review (promote/maintain/kill)
└── Corpus metrics

QUARTERLY
├── Paper / long-form analysis
├── Dataset release
├── Strategy pivot if needed
└── Full decision audit
```

### The Compounding Effect

Day 1: Agent knows nothing. Predicts randomly.

Day 30: Agent learns human's goal patterns. Predicts goals with 60% accuracy.

Day 90: Agent learns human's confidence calibration. Predicts belief updates.

Day 180: Agent can predict human's risk assessment and time allocation.

Day 365: Agent can generate a plausible "human-like" daily plan without input.

**The human becomes the training data for their own replacement.**

But that's fine — because the corpus is the asset, not the human's daily labor.

---

## What Makes This Different From a Journal

| Journal | This System |
|---------|------------|
| Free-form | Structured, same 12 questions daily |
| No agent comparison | Agent predicts, human answers, divergence measured |
| No outcome linking | 1d/7d/30d outcomes attached to beliefs |
| No problem matching | Problems indexed, searchable, cross-referenced |
| No protocol | Deterministic daily loop with defined outputs |
| Personal | Transferable — anyone's agent can learn from it |

---

## Implementation

### Voice flow (2-3 minutes)

```text
1. Open app
2. "Today I want to..." (30 sec)
3. "I think..." (30 sec)
4. "I'm testing..." (15 sec)
5. "I'm about X% confident..." (10 sec)
6. "What would change my mind is..." (15 sec)

[work happens]

7. "Today I..." (30 sec)
8. "Surprisingly..." (15 sec)
9. "I wasted time on..." (10 sec)
10. "Now I think..." (15 sec)
11. "The biggest risk is..." (10 sec)
12. "Tomorrow I'm going to..." (10 sec)
```

Total: ~3 minutes. Zero busywork. The agent does everything else.

### Typed flow (5 minutes)

```python
python3 tool/daily_record.py --day 1 \
  --q1 "Get Birthday V1 listing live" \
  --q2 "Football birthday gifts convert better than generic" \
  --q3 "Test 50th birthday variant" \
  --q4 70 \
  --q5 "Zero favorites after 48 hours" \
  --q6 "Generated 3 videos, 2 passed QA" \
  --q7 "H3 quality much better than expected" \
  --q8 "Spent 2 hours on scraper improvements" \
  --q9 "1080p is sufficient, don't need 4K" \
  --q10 "May be over-optimizing before launch" \
  --q11 "Overthinking the scraper, underthinking the listing copy" \
  --q12 "Actually publish the listing"
```

---

*The 12 questions are not arbitrary. Each one maps to a specific finding in the entrepreneurship, decision science, or agent trajectory literature. The divergence between agent predictions and human answers is itself the training signal. The problem-matching layer turns individual struggles into reusable institutional knowledge. The deterministic protocol means anyone can run the same system and contribute to the corpus.*
