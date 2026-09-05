# Peer Review — Integration Assessment

**Date:** 5 September 2026
**Verdict:** Direction very strong. Implementation not yet wired end-to-end.

---

## Scores

| Area | Assessment |
|------|-----------|
| Conceptual architecture | **A** |
| Frontier decomposition | **A-** |
| Scope discipline | **B** |
| Actual integration | **C** |
| Canonical data correctness | **C-** |
| Test quality | **C-** |
| Security | **D until secrets rotated** |
| Ready to collect real CompanyDays | **Not yet — one short repair sprint away** |

---

## P0 — Fix Before Collecting Data

### FIX-01: Security
- Rotate exposed Etsy/R2 credentials
- Remove every hard-coded secret
- `git rm --cached data/ledger.db`
- Secret-scan full Git history

### FIX-02: Semantics
- Etsy snapshot: views ≠ impressions, unknown orders/revenue = null
- HumanValueEstimate dimensional bug
- External marketplace data gets rights classification

### FIX-03: Canonical Core
- Actual Pydantic V1 records
- UUIDv7
- Timezone-aware timestamps
- Append-only ledger
- BOOK schemas become legacy adapters

### FIX-04: One Pipeline
```
CompanyDay → State → P/A/H → Decision → Budget → Session →
Trajectory → End State → ColdReview → PublicDigest
```

### FIX-05: Real E2E
- `demo-shop` fixture
- No network
- Prove: blindness, future leakage, budget reconciliation, token reconciliation, event replay, public-rights filtering

### FIX-06: Content
- Rewrite content generator to consume only `PublicDailyDigest`

### FIX-07: DOGCASSO
- Stop infrastructure, create first real listing/render

---

## Key Issues Found

1. **Credentials still exposed** in e2e_test.py and daily_content.py
2. **Ledger committed publicly** despite .gitignore
3. **Etsy snapshot corrupts metrics** (views ≠ impressions, orders/revenue should be null)
4. **HumanValueEstimate units bug** (mixing conversion rates with dollar penalties)
5. **No canonical Pydantic layer** — dict factories, not validated schemas
6. **Split-brain architecture** — new DP2 components not wired to daily CLI
7. **14/14 E2E is misleading** — tests old architecture, not canonical CompanyDay
8. **ColdReview claims blindness but doesn't prove it**
9. **Memory writes candidates as validated** — should be candidate → validated
10. **BATS priority never used** — tasks processed in input order
11. **Day counter off-by-one** — cron starts at Day 2, not Day 1
12. **Daily content doesn't use CompanyDay data** — derives from Git commits only
13. **CLI queries all-time records** — not filtered by company_day_id

---

## What's Good

- Correctly stopped treating HydraDB as blocker
- Frontier feature registry
- PPL intervention capture from theory to code
- Simple budget layer (not over-engineered)
- Right first version of TrajectoryIR
- Persistent problem registry
- Automated daily execution
- Honest status reporting ("no listings live")
