# The Lossless Experience Pyramid — Agent Trajectory Capture

**Date:** 5 September 2026
**Core insight:** Noise is a retrieval problem, not a storage problem.

---

## The Pyramid

```text
L5  TRANSFER PACKS
    "Launch a personalized jewellery brand"
    "Enter US fishing gifts"
           ↑ generated from

L4  PRINCIPLES / PLAYBOOKS
    "Occasion intent beats novelty in cold-start gifting"
    "Show input → output proof for generative products"
           ↑ derived from

L3  OUTCOME-LINKED EPISODES
    state → belief → action → result → lesson
           ↑ extracted from

L2  SEMANTIC SESSION
    goals / decisions / attempts / mistakes / discoveries
           ↑ normalized from

L1  AGENT TRACE
    turns / tool calls / files / diffs / costs / timestamps
           ↑ preserves

L0  RAW EVIDENCE
    complete OpenCode JSON export
    git refs
    terminal/tool outputs
    screenshots
    generated files
```

**Never delete L0. Never trust L4 without links back down to L0/L3.**

---

## The Key Object: `trajectory`

Aligns with where agent research is heading.

```text
campaign          → large commercial objective
  workday         → everything that happened September 8
    session       → one OpenCode interaction
      trajectory  → ordered sequence of agent/environment steps
        step      → LLM / tool / human / external event
        artifact  → file, prompt, video, listing, diff, screenshot
```

Orthogonally: hypothesis, decision, experiment, outcome, lesson link into those objects. This produces a graph, not merely folders.

---

## Experience Capsule (per session)

```json
{
  "session_id": "oc_...",
  "project": "mythicbee",
  "started_at": "...",
  "ended_at": "...",
  "objective_initial": "Get Birthday V1 working reliably",
  "agent": {
    "harness": "opencode",
    "model": "...",
    "agent_config_hash": "..."
  },
  "repo": {
    "url": "...",
    "branch": "main",
    "commit_before": "abc",
    "commit_after": "def",
    "diff_artifact": "sha256:..."
  },
  "raw_trace": "sha256:...",
  "sanitized_trace": "sha256:...",
  "cost": {
    "tokens": 0,
    "model_usd": 0.84,
    "gpu_usd": 1.21
  },
  "outcome": {
    "status": "success|partial|failure",
    "objective_achieved": 0.8
  },
  "semantic_extraction_id": "sem_..."
}
```

---

## Semantic Extraction (auto-generated at session.idle)

Cheap model reads the trace once:

```json
{
  "session_id": "oc_123",
  "goal": "Improve pet identity consistency in Birthday V1",
  "starting_state": ["3/5 reference pets passing QA", "dark-coated dogs failing most often"],
  "attempts": [
    {
      "step": 1,
      "action": "Changed reference preprocessing",
      "reason": "Suspected background contamination",
      "result": "No meaningful improvement",
      "label": "useful_failure"
    },
    {
      "step": 2,
      "action": "Changed first-frame construction",
      "reason": "Increase identity anchoring",
      "result": "Pass rate rose from 60% to 80%",
      "label": "productive"
    }
  ],
  "decisions": [{"decision": "Keep first-frame approach", "evidence": ["trace:turn:84"]}],
  "discoveries": ["Canonical first-frame quality matters more than prompt complexity"],
  "mistakes": ["Spent 25 minutes tuning prompt before testing reference frame"],
  "unresolved": ["Black dogs still weak in backlit scenes"],
  "next_actions": ["Test dark-coat reference normalization"]
}
```

50,000 raw tokens → 800 useful tokens. Nothing discarded.

---

## Step Labels

Research-backed labels for individual steps:

```text
PRODUCTIVE
NEUTRAL
UNNECESSARY
MISTAKE
RECOVERY
DISCOVERY
BLOCKED
EXPLORATION
```

After a year:

> 71,000 agent steps
> 16,200 productive
> 3,180 mistakes
> 2,991 recoveries
> 1,429 discoveries

Fascinating training/evaluation material.

---

## Connect Sessions to Business Outcomes Later

A coding session doesn't know whether what it built made money. Don't finalize its value when the session ends.

### September 8

Agent builds: `GAME_WINNER_THUMBNAIL_V4`. Session looks successful technically.

### September 9–15

Real marketplace data:

```text
CTR: 2.8% → 4.3%
conversion: 3.1% → 3.0%
revenue / 1000 impressions: +49%
```

### Retroactive outcome link (no modification of original)

```json
{
  "outcome_link": {
    "session_id": "oc_123",
    "action_id": "thumbnail_v4",
    "measurement_window": "7d",
    "effect": {
      "ctr_relative": 0.536,
      "conversion_relative": -0.032,
      "revenue_per_impression_relative": 0.49
    }
  }
}
```

> Agent did X for reason Y, and seven days later Z happened.

**That's the scarce data.** Anyone can scrape Etsy listings. They cannot reconstruct your historical intent → action → consequence chain.

---

## Preserve What the Agent Actually Saw

For each major decision:

```json
{
  "decision_time": "...",
  "information_cutoff": "...",
  "context_visible": ["state_snapshot_123", "market_research_87", "customer_feedback_22"],
  "not_yet_known": ["future_sales"]
}
```

Prevents hindsight leakage.

Run: "Here is exactly the state on Day 63. You cannot see Day 64 onward. What would you do?"

Compare new agent to: what you did, what the old agent recommended, what actually happened.

**An eval suite generated by running the business.**

---

## Versioned Interpretations

Don't summarize raw traces only once.

```text
raw trace
├── extraction_v1_2026
├── extraction_v2_2027
├── extraction_v3_2028
└── ...
```

Old interpretations remain. Raw evidence is permanent; intelligence applied to it improves over time.

---

## Step Labeling Research

- **JetBrains Step Rejection (2026):** Labels trajectory steps as good/unnecessary/mistake/recovery instead of discarding failed runs
- **Microsoft AgentRx:** Identifies critical failure steps in long execution trajectories
- **AgentHER:** Even failed trajectories contain valid experience for different goals

---

## Git Advantage

```text
AGENT INTENTION
↓
FULL TRACE
↓
FILES TOUCHED
↓
GIT DIFF
↓
TEST RESULTS
↓
DEPLOYMENT
↓
BUSINESS EFFECT
```

Future agent asks: "Show me every implementation change associated with improved fulfillment reliability."

Receives actual commits + reasoning + subsequent outcome.

---

## The Implementation (V1)

Extremely small:

```text
.opencode/plugins/commerce-recorder.ts
```

### On `session.created`
- Record project
- Git commit
- Timestamp
- Initial prompt/goal

### During session
- Capture message/tool/file events

### On `session.idle`
- Call/export session JSON
- Capture session diff
- Capture final Git state
- Hash/store everything
- Run cheap semantic extractor
- Emit `trajectory.json`
- Emit candidate `decisions.jsonl`
- Emit candidate `lessons.jsonl`

### At end of day
- Join sessions with commerce/financial events
- Create `workday.json`
- Generate blog
- Generate Short
- Update corpus

### Later
- Attach 1d / 7d / 30d outcomes to actions

**Your required behavior stays exactly the same: use OpenCode and build the business.**

The recorder silently converts normal work into proprietary training data.

---

## Why This Matters

The polished lesson "Start focused" is worth almost nothing. Someone can write that from intuition.

What's valuable:

> Day 4: agent thought X. Tried X. Spent $7.32. X failed because of Y. Agent noticed Z. Changed approach. That produced A. A was launched. Customers reacted B. Conversion moved C. Therefore belief became D.

Multiply by thousands of decisions. That starts looking like actual accumulated organizational experience.

Businesses normally lose most of that information when employees leave or forget why something was done.

We're recording essentially **every neuron firing in the company from birth**.

---

## The Transfer Mechanism

In two years: "Build me a jewellery store."

Agent doesn't dump the entire corpus into context. It:

1. **Retrieves analogous episodes** — MythicBee gift intent, Game Winner recipient segmentation, Christmas seasonal timing, portrait proof/trust tests
2. **Retrieves generalized principles** — specialist > broad, occasion-led > technology-led, proof-of-output lowers risk
3. **Retrieves operational playbooks** — store_launch_v4, product_validation_v7, q4_timing_v3
4. **Drills into raw trajectories only where necessary** — "Why exactly did Game Winner V2 fail?"
5. **Synthesizes a Jewellery Pack**

```text
jewellery-pack/
├── market-research-plan.md
├── day-01.json through day-30.json
├── product-hypotheses.jsonl
├── validation-plan.json
├── experiments.json
├── budget.json
└── evidence/historical_episode_refs.json
```

That's the portability.

---

*The raw agent behaviour is arguably the hardest thing to replicate. If maintaining the corpus requires you to manually document every little thing, we'll stop doing it. If the corpus is a byproduct of doing the work, it can become enormous.*
