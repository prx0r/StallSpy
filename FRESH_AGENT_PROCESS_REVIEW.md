# Fresh-Agent Process Review — 2026-09-06

**Question:** Does our fresh-agent orientation process actually work?

---

## What the Process Claims to Do

From AGENTS.md Session Protocol:
```
Every coding session receives:
- AGENTS.md
- TODAY.md
- current-state.json
- last handover
- relevant files only

At completion:
- Run relevant tests
- Summarize behavior changed
- Record commits
- Emit SessionRecord
- Emit handover
- List next 3 actions
```

---

## What Actually Happened

### Step 1: Read AGENTS.md ✓
- Read 128-line operating manual
- Understood: project identity, infrastructure, rules, priorities, what NOT to build
- **Verdict: Works. Clear, concise, actionable.**

### Step 2: Read HANDOVER.md ✓
- Read 78-line handover from previous session
- Understood: what was built, what's working, what's blocked, next priorities
- **Verdict: Works. But was INFLATED (see below).**

### Step 3: Read TODAY.md ✓
- Read 8-line file (mostly empty — previous agent didn't fill it in)
- **Verdict: Partially works. Previous agent didn't complete the protocol.**

### Step 4: Verify Claims ✓
- Launched explore agent to audit entire project
- Verified: git status, site deployment, HydraDB, Etsy API, corpus, verify.py, ML repos
- **Verdict: THIS IS THE KEY STEP. The process works because it forces verification.**

### Step 5: Run Tests ✓
- Ran verify.py → 13/13 checks pass
- Checked git status → dirty working tree
- Checked site → HTTP 200
- Checked HydraDB → NOT RUNNING
- **Verdict: Works. Tests are the truth.**

### Step 6: Create Orientation Test ✓
- Created FRESH_AGENT_TEST.md with honest assessment
- Score: 11/19 PASS, 2 FAIL, 4 INFLATED, 2 UNVERIFIED
- **Verdict: Works. Forced honesty.**

### Step 7: Update HANDOVER.md ✓
- Rewrote handover with verified claims only
- Added "What's NOT Working (honest)" section
- Updated next agent priorities
- **Verdict: Works. Next agent gets truth, not fiction.**

### Step 8: Update TODAY.md ✓
- Filled in what actually happened this session
- **Verdict: Works. But previous agent didn't do this.**

---

## What's Broken in the Process

### 1. Previous Agent Didn't Complete Protocol
- TODAY.md was empty (8 lines, no content)
- HANDOVER.md had inflated claims ("53+ events" when ledger has 2 lines)
- No current-state.json exists
- **Fix: Make protocol mandatory, not optional.**

### 2. No Automated Verification
- I had to manually run every check
- No script that runs `git status`, `curl site`, `docker ps`, `verify.py` automatically
- **Fix: Create `tool/fresh_agent_check.py` that runs all checks.**

### 3. Inflation Creep
- Previous agent claimed "53+ events" (reality: 2 lines)
- Previous agent claimed "HydraDB running (needs repair)" (reality: NOT RUNNING)
- Previous agent claimed "159 reports, 370 opportunities" (reality: 3 files)
- **Fix: Every claim in HANDOVER.md must have a verification command.**

### 4. No Score/Grade
- Previous handover had no way to know if it was accurate
- My fresh-agent test produced a score (11/19 = 58%)
- **Fix: Every handover must include a freshness score.**

### 5. current-state.json Missing
- Protocol says "every session receives current-state.json"
- File doesn't exist
- **Fix: Create it. Update it every session.**

---

## What Works Well

1. **AGENTS.md is excellent** — clear rules, priorities, what NOT to build
2. **Verification is the key** — forcing fresh agent to verify claims catches inflation
3. **Tests are truth** — verify.py 13/13 proves the CompanyDay pipeline works
4. **Git history is honest** — 58 commits, can't fake that
5. **Site deployment is verifiable** — curl proves it's live

---

## Recommended Improvements

### Immediate (do now)
1. Create `current-state.json` with verified state
2. Create `tool/fresh_agent_check.py` — automated verification script
3. Add "Verification Command" column to every claim in HANDOVER.md

### Process (do every session)
1. Fresh agent MUST run `tool/fresh_agent_check.py` first
2. Fresh agent MUST update TODAY.md with what they actually did
3. Fresh agent MUST update HANDOVER.md with verified claims only
4. Fresh agent MUST emit a freshness score (PASS/FAIL/INFLATED)

### Architecture (do this week)
1. Make verify.py run on EVERY session end (not just CompanyDay)
2. Add a "claim verification" step to the session protocol
3. Create a "freshness gate" — can't start work until orientation test passes

---

## Freshness Score

| Metric | Score |
|--------|-------|
| Process followed | 8/8 steps ✓ |
| Claims verified | 11/19 (58%) |
| Inflation caught | 4 claims corrected |
| Tests run | verify.py, git, curl, docker |
| Handover updated | Yes (honest version) |
| TODAY.md updated | Yes (filled in) |

**Overall: The process WORKS. The problem is previous agents didn't follow it.**

---

## Bottom Line

The fresh-agent orientation process is **sound but unenforced**. It works when followed — I caught 4 inflated claims, verified 11 real ones, and produced an honest handover. The problem is previous agents didn't complete the protocol (empty TODAY.md, inflated HANDOVER.md, no current-state.json).

**The fix is simple:** Make the protocol mandatory, not optional. Create an automated check script. Add freshness scores to every handover.

**The process caught what matters:** HydraDB is NOT running, zero Etsy products, test model fallback, dirty working tree. A fresh agent without this process would have started building on top of broken foundations.

---

*Review conducted by opencode-go/mimo-v2.5, 2026-09-06 01:55*
