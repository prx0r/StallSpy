# MetaPlan — What Actually Matters

**Date:** 5 September 2026

---

## Tier 1: The Things That Actually Matter

### 1. `moredev.txt` (the implementation brief)
Single highest-signal document. Actual engineering spec with concrete ownership boundaries, kernel invariants to fix, test requirements, phased plan. Tells a coding agent exactly what to do. Everything else is strategy — this is execution.

### 2. The 12-question adaptive interview (metamanagement)
Questions dynamically generated from information objectives, not hardcoded. `question_objective` schema with uncertainty × decision_relevance × human_advantage × consequence ÷ burden. Makes the human interview actually useful rather than a daily chore.

### 3. The prompt archive thesis
Raw prompts contain more operator model training data than structured labels. "fuck sake stop building frameworks I literally just want the product live today" tells an agent more than a thousand labeled preference records. Highest-leverage data source, almost nobody collecting it.

### 4. The eBay data opportunity
Three years of actual sold-item data with real Best Offer prices. Pre-built historical gym. Combined with UCI Online Retail II (1M transactions, CC BY 4.0), build mwgym commerce benchmark before touching any marketplace API.

### 5. The operator twin / economic critic separation
Not "clone the human" but "learn where human judgment adds value vs where it doesn't." `HumanValueModel` — marginal human value minus interruption cost — is the actual endgame metric.

---

## Tier 2: Strong Architecture, Needs Execution

### 6. 15-phase CompanyDay protocol
Good structure but too many phases for Day 1. Core insight: blind review must be independent, outcomes attached later. Start with 5 phases, add complexity as system proves it needs it.

### 7. Feelings Dataset / SubjectiveState
Three-way comparison (human vs predicted-human vs critic) with later outcome attachment. Valuable but downstream of having a real business generating outcomes.

### 8. ColdReview blind protocol
Good idea, correct implementation. Pass-A-then-pass-B prevents parroting. Refinement, not foundation.

### 9. AGENTS.md with 15 axioms
Good constitution. Too long for daily reference. Keep to 5 max, rest in protocols.

---

## Tier 3: Interesting but Premature

### 10. TokenWise / PAHF / PPL integration
Cloned, not wired. Interesting research repos but adding before core pipeline works is scope creep.

### 11. ForecastBook
Prospective predictions with Brier scores — great concept, needs working business generating outcomes.

### 12. HumanQueue manager
Good design but premature. Not enough decision volume yet.

---

## What To Do Tomorrow

1. Fix 3 private-lab kernel invariants (transactional ledger, pure Hydra, ledger-first controller)
2. Get 5 Game Winner listings live on Etsy via API
3. Start daily scraper cron
4. Record first CompanyDay
5. Let data accumulate 30 days before adding sophistication

**Stop planning. Start selling. Measure what happens.**
