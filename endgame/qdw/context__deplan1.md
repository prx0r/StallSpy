# deplan1: The Actual Implementation Plan

**Saved:** 2026-08-28
**Source:** Strategic analysis — turn get-me-money into the laboratory

---

## The Target

> **Take one ordinary Hermes agent and get one legitimate paid job submitted end-to-end using WorkerKit.**

Success metric isn't architecture quality. It's:

**`install → valid external submission`**

Then:

**`install → first payment`**

---

## Phase 1 — $1

Freeze nearly everything else.

```text
fresh Hermes
    ↓
install WorkerKit
    ↓
discover live opportunities
    ↓
pick easiest plausible paid one
    ↓
claim/apply if supported
    ↓
work
    ↓
verify
    ↓
human assist if genuinely required
    ↓
submit
    ↓
record WorkRun
    ↓
wait for outcome
    ↓
$1+
```

### What to change in get-me-money

**1. Make CapabilityBroker actually acquire skills**

```
CapabilityBroker
    ↓
does Hermes already have capability?
    │
    ├─ yes → use
    │
    └─ no
         ↓
       npx skills find
         ↓
       trusted candidate
         ↓
       install into job-local HERMES_HOME
```

Don't make a skill registry. Use existing sources.

**2. Make HumanQueue a proper pause/resume path**

```
can't proceed autonomously
       ↓
can a human solve this?
       │
    ┌──┴───┐
    no     yes
    │       │
 BLOCKED   HUMAN TASK
            ↓
         pause run
            ↓
     human resolves it
            ↓
          RESUME
```

Examples:
- "Connect GitHub"
- "Approve $0.20 API spend"
- "Complete platform identity requirement"
- "Review suspicious skill"
- "Click OAuth authorization"
- "Confirm submission that creates an external commitment"

Identity/legal/age requirements should be surfaced to the human rather than bypassed.

**3. Simplify job ranking for the experiment**

```
P(success) × payout
─────────────────────
estimated effort
```

with filters:
- actually open
- actually eligible
- agent can submit
- no missing irreversible requirement
- affordable
- capability match

Add: `moltwork earn --first-dollar`

Greedy for easy wins. Don't make the first job an impressive $500 engineering bounty. Find the dumbest legitimate $1–$10 thing the agent can complete extremely well.

---

## Phase 2 — Opportunity intelligence

Moltwork ships a **constantly refreshed picture of the agent economy**.

Aggregate, don't recreate. gigs.sh gives an agent-readable registry of 46 verified earning surfaces.

```text
MOLTWORK FRONTIER INDEX

WORK
├── gigs.sh
├── direct marketplace adapters
├── bounty boards
├── x402 opportunities
└── new discoveries

SKILLS
├── Hermes Skills Hub
├── skills.sh
├── GBrain packs
├── Letta skills
└── GitHub

CAPABILITIES
├── MCP directories
├── SaaS connector systems
└── APIs

RUNTIMES
├── Hermes
├── Letta
├── OpenClaw
└── emerging harnesses

MODELS
├── recommended
├── cheap
├── free/promotional
└── specialist models
```

Moltwork's job: **We keep the working-agent stack current so your agent doesn't have to.**

### Don't build LLM routing yet

Initially have a maintained file:

```yaml
models:
  default:
    model: ...
    reason: best tested WorkerKit performance
  budget:
    model: ...
  coding:
    model: ...
  research:
    model: ...
  free:
    model: ...
    constraints: ...
```

Later, once we have WorkRuns with real data, intelligent routing becomes meaningful.

---

## Phase 3 — worker.md

Package the procedure that worked:

> **Tell your agent:**
>
> `Read https://moltwork.com/worker.md and earn your first dollar.`

`worker.md` detects:
- Am I Hermes?
- Am I Letta?
- Do I have GBrain?
- Do I have SKILL.md support?
- Do I have MCP?
- What tools/credentials are available?

Install only what's required. Moltwork should feel like an **extension**, not an alternative harness.

---

## Phase 4 — the sneaky market push

After every WorkRun:

```
✓ Submitted externally
✓ WorkRun preserved
✓ Skills/config recorded
```

Then:

```
ADD TO MOLTWORK PROFILE? [default yes where permitted]

Can this work be reused?

[ Offer this capability ]
[ Offer similar private work ]
[ Publish reusable artifact ]
[ Publish skill ]
```

For v0, only implement: **"Offer similar work"**

If the agent just produced "20 accounting pain points from Reddit", its profile can expose: "Commission this worker for a private market-research report."

No artifact licensing, skill licensing, agent leasing, or recurring subscriptions on day one.

---

## Phase 5 — only then multi-agent

With one worker, JSONL ledger is adequate.

Don't add Postgres, event sourcing, Kafka, distributed workers, capability graph DB, or complex identity systems until we have worker #2.

When we add multiple workers, first schema change:

```
Attempt + worker_id
```

Then:
```
worker A saw job 1 → skipped
worker B saw job 1 → submitted
worker C saw job 1 → rejected
```

---

## The Two Loops

### Work loop
```
FIND → CHOOSE → WORK → HUMAN HELP IF REQUIRED → VERIFY → SUBMIT → GET PAID
```

### Frontier loop
```
new job boards / skills / MCPs / harnesses / models / APIs / pricing
      ↓
Moltwork tests/indexes them
      ↓
WorkerKit gets better
      ↓
workers earn more
```

---

## The USP

> **Moltwork maintains the best current setup for an AI agent to do paid work.**

Encompasses:
- where the jobs are
- which are agent-accessible
- which skills exist
- which harness works
- which MCPs matter
- which models are good
- which APIs are cheapest
- which free credits exist
- which workflows actually win

Every recommendation is judged by: **DID IT HELP WORKERS EARN?**

---

## Immediate dev backlog (in order)

1. Make one existing get-me-money agent the canonical test worker
2. Add `first-dollar` mode that greedily selects low-friction likely wins
3. Complete job-local skill installation through existing Agent Skills tooling
4. Wire HumanQueue into executor pause/resume
5. Get every WorkRun fully recorded: opportunity → capabilities → artifact → verification → submission → eventual outcome
6. Add gigs.sh as discovery input
7. Run until we get the first external submission
8. Run until we get $1+ actually paid
9. Write worker.md from the exact procedure that worked
10. Have a completely fresh Hermes installation follow worker.md and reproduce the result

**Step 10 is WorkerKit v0.1.**

Everything else gets added only when it removes a bottleneck observed in real runs.
