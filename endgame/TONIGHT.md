# Tonight's Priority — Make the Loop Work

**Date:** 5 September 2026

---

## Goal

By end of tonight, tomorrow can be the first genuinely valuable day of the experiment. The system silently captures data, stores it safely, performs human/agent comparison, and produces publishable daily content.

---

## 18 Must-Have Items

### 1. Secrets rotated ✓ (done)
### 2. Canonical CompanyDay as sole daily identity ✓ (done)
### 3. Private local artifact store works
### 4. R2 upload + verification works
### 5. Real OpenCode session gets automatically captured
### 6. Raw + sanitized trace stored
### 7. Token/model/tool usage recorded
### 8. Git before/after/diff recorded
### 9. Morning P/A/H flow runs once
### 10. Worker debrief runs
### 11. Human evening note can be ingested
### 12. Blind review has actual isolation test
### 13. PublicDailyDigest generated
### 14. Blog deployed and publicly reachable
### 15. YouTube account exists
### 16. TikTok account exists
### 17. Daily publish bundle generated
### 18. `stallshark verify --day today` passes

---

## The 17-Phase CompanyDay

```
00  State Freeze
01  Fresh Blind Diagnosis
02  Human Morning State
03  Agent Predicts Human
04  Reveal / Divergence
05  Problem Selection
06  Hypothesis + Experiment
07  BATS Allocation
08  WorkerKit Execution
09  Worker Debrief
10  Human Evening Note
11  Blind Evidence Review
12  Reconciliation
13  Hydra Candidates
14  Blog + YouTube Short
15  Future Outcomes
16  Reality Scores Everyone
```

---

## Storage Architecture

```
LOCAL PRIVATE SPOOL
        ↓
SHA-256
        ↓
canonical ledger event
        ↓
encrypted/private R2 upload
        ↓
verify uploaded object
        ↓
ArchiveReceipt
```

---

## Verification Command

```bash
stallshark verify --day today
```

Must show all green:

```
CAPTURE: all traces archived
INDEPENDENCE: no future leakage, blind review isolated
STORAGE: local + R2 verified
PUBLIC: digest + blog + publish bundle
DAY COMPLETE: TRUE
```

---

## What Can Wait

- Hydra
- Fine-tuning
- PPL training
- TokenWise
- Sophisticated BATS
- Problem Scientist
- Multi-agent companies
- Dashboards
- GameWinner itself

**Tomorrow is the first genuinely valuable day.**
