# The Operational Plan — Stop Designing, Start Operating

**Date:** 5 September 2026

---

## The Central Rule

> **Build businesses. Preserve the cognition around building them. Publish one useful slice each day.**

StallShark is the machine watching and learning from the process — not another giant project that prevents the process from happening.

---

## Rename: StallShark

"Shark" sounds like an operator that finds opportunities and acts. "Spy" sounds like passive analytics. StallShark gives stronger visual identity.

Do proper trademark clearance before meaningful spend.

---

## V0: Only 8 Schemas

Everything else can be derived later.

### 1. `company_day`
Root object. Everything belongs to a CompanyDay.

### 2. `state_snapshot`
Facts only. No interpretation. What existed.

### 3. `perspective`
Same schema for human, agent, predicted_human, blind_reviewer, working agent. The Human ↔ Agent divergence dataset.

### 4. `session`
OpenCode session metadata + immutable trace pointer. Raw transcript always stays.

### 5. `decision`
Where BATS eventually plugs in. Record intended resource budgets.

### 6. `problem`
The operating primitive. Persistent problems the company attacks.

### 7. `experiment`
Brutally practical. Hypothesis, intervention, metric, result.

### 8. `economic_event`
Everything that costs or makes resources. One unified ledger.

---

## What These Preserve

```
what existed
what everyone thought
what everyone predicted
what was decided
what was done
what it cost
what problem it addressed
what reality did afterward
```

Everything else can be reconstructed.

---

## The Daily Process

### Morning (5 min)

1. `stallshark day start` → freeze state
2. Dynamic interview → 5 highest-information questions
3. Human answers by voice
4. Agent + predicted-human answer same questions
5. Choose 1-3 priorities, budgets
6. Work on Dogcasso

### During Day (zero extra effort)
OpenCode captures everything automatically.

### End of Session
Worker debrief. Export raw session.

### Evening (2 min)
Raw voice note. Not polished.

### Night
Blind review → divergence → public content.

### Weekly
One extra synthesis + "Week N: $X" video.

---

## V0 Success Criterion

By end of one real business day:

```
day_0001/
├── state_start.json
├── human_morning.json
├── agent_morning.json
├── predicted_human.json
├── decisions.jsonl
├── economic_events.jsonl
├── sessions/
│   └── <raw OpenCode export>
├── worker_debrief.json
├── human_evening.json
├── state_end.json
├── blind_review.json
├── divergence.json
├── company_day.json
├── blog.md
└── short_script.md
```

---

## Immediate Fixes

### 1. Rotate credentials
`.env` with API keys. Never commit secrets.

### 2. Separate business metrics from market research
First-party store state ≠ external market research.

### 3. Replace morning CLI
Dynamic interview from state_start, not fixed questions.

---

## Three Sprints

### Sprint A — Recorder
8 schemas (Pydantic) + capture + interview + review + publish + CLI.

### Sprint B — DOGCASSO
Get actual product live. No Hydra, no fine-tuning, no RL.

### Sprint C — GAME WINNER
Only after Dogcasso is moving. Same recorder.

---

## V0 Success = One Real Day

```
day_0001/
├── state_start.json
├── human_morning.json
├── agent_morning.json
├── predicted_human.json
├── decisions.jsonl
├── economic_events.jsonl
├── sessions/
│   └── <raw OpenCode export>
├── worker_debrief.json
├── human_evening.json
├── state_end.json
├── blind_review.json
├── divergence.json
├── company_day.json
├── blog.md
└── short_script.md
```

14 days of this = the beginning of the weird, difficult-to-copy dataset.

**Build businesses. Preserve cognition. Publish one slice each day.**
