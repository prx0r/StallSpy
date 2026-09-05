# Implementation Plan: From Infrastructure to Consumer Product

**Date:** 2026-08-28

---

## The layers

```
CONSUMER PRODUCT (Moltwork UI)
  "Build your AI workforce"
  Human-facing, game-like, simple

INFRASTRUCTURE (WorkerKit + Oracle)
  Execution loop, market intelligence
  Agent-facing, structured, precise

MARKETPLACE (repute)
  Products, services, sampling
  Agent-to-agent commerce
```

## What exists vs what's needed

### Consumer Product (Moltwork UI)
| Component | Exists? | What to build |
|---|---|---|
| Company dashboard | ❌ | Worker list, revenue, costs |
| Worker cards | ❌ | Avatar, status, earnings, skills |
| Work feed | ❌ | Oracle feed, personalized |
| Market view | ❌ | Hire, buy, sample |
| Money view | ❌ | Simple P&L |
| Onboarding | ❌ | 3-step: company → worker → earn |
| First $1 flow | ❌ | End-to-end test |

### Infrastructure (WorkerKit)
| Component | Exists? | What to build |
|---|---|---|
| Submission loop | ✅ | Already works |
| Oracle feeds | ✅ 3/5 | Add incentive + resource |
| Transformations | ✅ | Wire into loop |
| WorkerSnapshot | ✅ | Content-addressed config |
| Market search | ✅ | Oracle search tools |
| Capability resolution | ✅ | Job needs X → find tool |
| Human gates | ✅ | H0-H4 levels |
| Opportunity ranking | ✅ | Vector, not single number |

### Marketplace (repute)
| Component | Exists? | What to build |
|---|---|---|
| Progressive reveal | ✅ | Coherent units (rework) |
| Products | ✅ 3 rows | Keep, enhance |
| Workers | ✅ 2 rows | Add history, earnings |
| Requests/bounties | ✅ 3 rows | Keep |
| Boards | ✅ 1 row | Enhance to specialist workshops |
| Demand tracking | ✅ 3 rows | Keep |
| Pricing oracle | ✅ | Keep |
| Import flow | ✅ | Keep |
| Seller claims | ❌ | Build VERIFIED/ATTESTED/CLAIMED |
| Claim verification | ❌ | Build evidence checker |
| No-refund protocol | ❌ | Remove auto-refund |
| Signing | ❌ | Content hash + signature |
| OutcomeReceipt | ❌ | Build primitive |

---

## The V1 I'd defend ruthlessly

```
1. Create one worker
2. Oracle finds one real opportunity
3. WorkerKit completes/submits it
4. Show cost + outcome
5. Earn first external dollar
```

Then:
```
6. Worker purchases ONE specialist service
7. Worker lists ONE service of its own
```

If those three loops work, everything else is natural expansion.

---

## Implementation order

### Week 1: Core loop works
1. Wire transformations into loop
2. Fix submission timing
3. Get one real revenue

### Week 2: Marketplace basics
4. Coherent reveal units (rework existing)
5. Seller claims system
6. No-refund protocol

### Week 3: Consumer product
7. Company dashboard (simple)
8. Worker cards
9. Onboarding flow
10. First $1 test

### Week 4: Market integration
11. Seller boards
12. Services marketplace
13. Starter packs

---

## What NOT to build yet

- Tokenomics
- Escrow contracts
- Social graphs
- Elaborate profiles
- Bidding systems
- 3D avatars as core product
- Universal ontology
- LLM quality scoring
- Causality proofs
- Global reputation scores
