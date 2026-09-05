# AGENTS.md — Operating Rules for StallShark

## Phase: LIVE VALIDATION

**Primary objective:** Get Dogcasso Etsy products selling and preserve high-quality evidence about decisions/actions/outcomes.

**Priority:** DOGCASSO > OPS/BOOK > RADAR > LAB/GYM.

---

## Core Rules

1. **The business comes first.** Content records the business. Content must never become the business's main source of busywork.
2. **Reality outranks narrative.** Economic outcomes outrank agent confidence.
3. **Never rewrite history.** Incorrect beliefs remain recorded as beliefs held at that time.
4. **Independent review means independent.** Blind reviewer commits before seeing interpretations.
5. **Every expenditure has a budget.** Track cash, tokens, human time.
6. **Autonomy is earned per decision class.** Don't automate what you haven't proven you can do.
7. **Prefer experiments that reduce important uncertainty.**
8. **Don't promote a lesson because an agent wrote it.** Promotion requires evidence.
9. **One intervention at a time.** Don't confound experiments.
10. **The simplest thing that could work.** No Hydra, no fine-tuning, no RL until Dogcasso is selling.

---

## What to Do Each Day

```
MORNING (5 min)
  stallspy day start
  → agent generates 5 questions from state
  → human answers
  → agent + predicted-human answer same questions
  → choose 1-3 priorities
  → WORK ON DOGCASSO

DURING DAY
  Just use OpenCode. Recorder captures everything.

END OF SESSION
  Worker debrief. Export raw session.

EVENING (2 min)
  Raw voice note. Not polished.

NIGHT
  Blind review → divergence → public content.
```

---

## What to Build Next (Sprint A)

1. **Book schemas** — 8 core schemas (Pydantic)
2. **Local store** — filesystem append/write
3. **Etsy snapshot** — capture metrics
4. **Listing version registry** — track changes
5. **Render receipts** — record generation costs
6. **Daily report** — print summary
7. **OpenCode session recorder** — capture traces
8. **Blind review** — independent assessment

---

## What NOT to Build

Until 20 paid Etsy orders or 30 days real data:

- New generalized databases
- New graph abstractions
- New agent runtimes
- Amazon/eBay
- Complex Arenav2 work
- Fine-tuning
- Multi-company hierarchies
- Elaborate dashboards
- 20-store launches

**If it doesn't improve revenue, fulfillment quality, experimental observability, or operating speed — question why it's being built.**

---

## File Map

```
dogcasso-ops/     ← LIVE DATA (8 schemas)
corpus/           ← ARCHITECTURE SPECS
endgame/          ← PLANNING
tool/             ← AUTOMATION + SCHEMAS
brands/           ← BRAND STRATEGY
content/          ← CONTENT STRATEGY
product/          ← PRODUCT ARCHITECTURE
research/         ← MARKET RESEARCH
tools/            ← CLONED MCP SERVERS
data/             ← LOCAL DATABASES
```

---

## Session Protocol

Every coding session receives:

```
AGENTS.md
TODAY.md
current-state.json
last handover
relevant files only
```

At completion:
- Run relevant tests
- Summarize behavior changed
- Record commits
- Emit SessionRecord
- Emit handover
- List next 3 actions

---

## The Endgame

The corpus is the primary asset. Dogcasso and Game Winner generate the data. StallShark watches and learns. The research substrate does not need to produce the real business — the real business produces the research substrate.

**Build businesses. Preserve cognition. Publish one slice each day.**
