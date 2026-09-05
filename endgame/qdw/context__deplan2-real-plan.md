# deplan2: The Real Plan (what to actually do)

**Date:** 2026-08-28
**Based on:** All audits + strategy docs + deplan1 + actual repo state

---

## The honest diagnosis

We have:
- **2 repos** with overlapping functionality, 30% dead code in one
- **3 strategy docs** describing what to build
- **12 separate builds** on the box
- **1 working Hermes** with a one-line auth fix needed
- **10 real Taskmarket opportunities** sitting in a JSONL file
- **Zero completed submissions**

The strategy is sound. The code is 70% there. The blocker is trivial (API key not in hermes-gmm .env).

---

## The real plan: 3 phases, not 5

### PHASE 0: Fix the blocker (today, 10 minutes)

```bash
# Copy the working API key to hermes-gmm
cp /root/.hermes/.env /root/.hermes-gmm/.env

# Verify hermes works with the gmm home
HERMES_HOME=/root/.hermes-gmm hermes -z "say hello"
```

That's it. The entire system was blocked by a missing env var.

### PHASE 1: Get $1 (this week)

**Goal:** One existing Hermes agent → one legitimate external submission.

**What to change in get-me-money:**

1. **Delete dead code first** — Clean the workspace:
   - Delete `get_me_money/repute/__init__.py` (787 lines, never imported)
   - Delete `get_me_money/platforms/moltwork.py` (154 lines, bypassed)
   - Delete `get_me_money/oracle.py` (99 lines, never called)
   - That's 1,040 lines of confusion gone

2. **Add `--first-dollar` mode to CLI:**
   ```
   moltwork earn --first-dollar
   ```
   Greedy selection: `P(success) × payout ÷ estimated_effort`
   Filters: open, eligible, agent can submit, no irreversible requirements, affordable

3. **Fix the hermes-gmm .env** (the one-line fix above)

4. **Test the full loop manually:**
   ```
   moltwork scan          # see opportunities
   moltwork run           # dry run, see ranking
   moltwork run --execute # actually do one
   ```

5. **Record every WorkRun** — opportunity → capabilities → artifact → verification → submission → outcome

**What NOT to change:**
- Don't merge repos yet
- Don't add gigs.sh yet
- Don't add Moltbook auth yet
- Don't build worker.md yet
- Don't touch repute at all

**Success:** `moltwork run --execute` produces a real submission to a real platform.

### PHASE 2: Make it reproducible (next week)

**Goal:** Fresh Hermes installation → follow worker.md → reproduce the result.

This is where we:

1. **Write worker.md** from the exact procedure that worked in Phase 1
2. **Add gigs.sh integration** — Replace hardcoded adapters with gigs.sh discovery
3. **Wire HumanQueue pause/resume** — When agent can't proceed autonomously, pause and ask human
4. **Fix repute MCP pool routes** — `/api/pools` → `/api/requests`
5. **Test with a completely fresh Hermes** — Does worker.md actually work from scratch?

**Success:** A fresh Hermes follows worker.md and gets a submission without us hand-holding.

### PHASE 3: The product (week 3+)

Only after Phase 2 works reliably:

1. **Merge repos** — get-me-money (worker) + repute (marketplace) = one Moltwork repo
2. **Add Moltbook auth** — "Read worker.md and become a worker"
3. **Build frontier index** — gigs.sh + skills.sh + model recommendations
4. **Profile system** — Completed work → capability evidence → reusable skill
5. **worker.md hosted at moltwork.com** — The one-click onboarding

---

## What the codebase looks like after Phase 1

```
get-me-money/
├── get_me_money/
│   ├── __init__.py          # v0.3.0
│   ├── cli.py               # + earn --first-dollar command
│   ├── main.py              # + first_dollar_ranking()
│   ├── config.py            # unchanged
│   ├── models.py            # unchanged
│   ├── evaluator/           # simplified for first-dollar mode
│   ├── executor/            # unchanged (the good stuff)
│   ├── broker/              # + actual skill installation via npx
│   ├── verifier/            # unchanged
│   ├── hermes_runtime.py    # unchanged
│   ├── workrun.py           # unchanged
│   ├── ledger/              # unchanged
│   ├── memory/              # unchanged
│   ├── human_tasks.py       # + pause/resume path
│   ├── notifier.py          # unchanged
│   ├── daemon.py            # unchanged
│   └── dashboard/           # unchanged
│       └── server.py
├── platforms/
│   ├── __init__.py          # unchanged
│   ├── taskmarket.py        # keep (works)
│   ├── bounty.py            # keep (works)
│   ├── superteam.py         # keep (works)
│   └── moltjobs.py          # keep (fix Platform enum)
├── data/
│   ├── config.json          # cleaned up
│   ├── opportunities.jsonl  # 10 real Taskmarket bounties
│   └── .env                 # fixed API key
├── tests/
│   └── smoke.py             # expanded
└── pyproject.toml           # fixed naming
```

Deleted:
- `repute/__init__.py` (787 lines)
- `platforms/moltwork.py` (154 lines)
- `oracle.py` (99 lines)

**Net: ~2,300 lines of working code, zero dead code.**

---

## The critical path (what blocks what)

```
FIX AUTH (10 min)
    ↓
TEST HERMES EXECUTION (30 min)
    ↓
RUN moltwork scan (verify opportunities load)
    ↓
RUN moltwork run (verify ranking works)
    ↓
RUN moltwork run --execute (FIRST SUBMISSION)
    ↓
RECORD WORKRUN
    ↓
WAIT FOR OUTCOME
    ↓
$1
```

Everything else is secondary until this path completes.

---

## What to tell the coding agent

```
MISSION

Fix the auth blocker and get one legitimate submission through the
get-me-money pipeline.

STEP 1: Fix hermes-gmm auth
  - Copy /root/.hermes/.env to /root/.hermes-gmm/.env
  - Verify: HERMES_HOME=/root/.hermes-gmm hermes -z "say hello"

STEP 2: Delete dead code
  - Remove get_me_money/repute/__init__.py
  - Remove get_me_money/platforms/moltwork.py
  - Remove get_me_money/oracle.py

STEP 3: Add first-dollar mode
  - Add --first-dollar flag to CLI
  - Simplified ranking: P(success) × payout ÷ effort
  - Greedy for easy wins

STEP 4: Test the full loop
  - moltwork scan (should find 10 Taskmarket bounties)
  - moltwork run (dry run, verify ranking)
  - moltwork run --execute (actually do one)

STEP 5: Record everything
  - WorkRun with full trace
  - Verify the submission went through
  - Check platform status

DO NOT:
- Merge repos
- Add gigs.sh
- Add Moltbook
- Build worker.md
- Touch repute
- Add Postgres
- Build multi-agent

The success metric is: one real submission to a real platform.
```

---

## The risk

The only real risk is that the 10 Taskmarket opportunities are stale or the taskmarket CLI binary isn't installed. Let me check:

Actually, the taskmarket adapter wraps a `taskmarket` CLI binary. If that binary isn't installed, the Taskmarket adapter won't work. But we also have:
- BountyAdapter (TryBounty) — uses httpx/selectolax
- SuperteamAdapter — uses httpx API
- MoltJobsAdapter — uses httpx API

If Taskmarket is broken, we fall back to whichever adapter works. The point is: get ONE submission through ANY platform.

---

## Timeline

| Day | Action | Result |
|---|---|---|
| Today | Fix auth, delete dead code | Hermes works, codebase clean |
| Day 2 | Add first-dollar mode, test scan/run | Ranking works |
| Day 3 | Run --execute on easiest opportunity | First submission |
| Day 4-6 | Iterate until submission accepted | First win |
| Day 7 | Write worker.md from what worked | Reproducible procedure |
| Week 2 | Test worker.md on fresh Hermes | WorkerKit v0.1 |

**Week 1: get to $1.**
**Week 2: make it reproducible.**
**Week 3: make it a product.**
