# StallSpy Company Substrate — Implementation Brief

**Date:** 5 September 2026
**Source:** Implementation brief from Tom

---

## Objective

Not building a standalone Etsy automation app. Building the first real economic environment operated by a general agent-company substrate.

## Loop

```
OBSERVE → ASSESS → DETECT → HYPOTHESIZE → DESIGN → ALLOCATE → EXECUTE → CAPTURE → OBSERVE OUTCOMES → COLD REVIEW → ATTRIBUTE → LEARN → NEXT STATE
```

## Ownership Boundaries

```
private-lab ledger     = canonical record of what happened
private-lab artifacts  = canonical immutable bytes
Git                    = canonical code/config/template lineage
RunReceipt             = immutable account of what a run consumed/produced
HydraDB                = rebuildable graph/index/projection
PydanticAI             = replaceable execution/orchestration runtime
StallSpy               = Etsy/Dogcasso domain implementation
finalbuilds            = donor + product-building intelligence module
```

## Key Invariants

- If deleting Hydra or Hindsight destroys unique knowledge, architecture is wrong
- If swapping PydanticAI destroys historical comparability, architecture is wrong
- If an Etsy API response becomes canonical domain object, architecture is wrong
- Domain-specific facts in StallSpy. Universal machinery in private-lab.

## Kernel Hardening Required

1. Ledger append must be transactional (BEGIN IMMEDIATE)
2. Fix event ID semantics (UUIDv7 or explicit time-sortable)
3. Hydra projection must be pure (never creates new ledger events)
4. All state changes ledger-first
5. Preserve published contract compatibility (v2 adapters, not destructive renames)

## Two Experiment Classes

- **CapabilityExperiment**: WorkerVersion A vs B, model A vs B, context strategy A vs B
- **WorldExperiment**: listing title A vs B, thumbnail A vs B, price A vs B, product format A vs B

## CompanyDay Orchestration (State Machine)

```
COLLECT → ASSESS → DIAGNOSE → HYPOTHESIZE → ALLOCATE → EXECUTE → OBSERVE → REVIEW → LEARN → CLOSE
```

## Definition of Success

```text
stallspy company-day run --mode replay --fixture demo-shop
```

Produces verifiable chain:

```
CompanyDay → StateSnapshot → ActorAssessment → Problem → ResearchBundle →
Hypothesis → WorldExperiment → WorkOrder → InterventionProposed → RunReceipt →
OutcomeObservation → ColdReview → ExperimentResult → Finding
```

With:
- All artifacts content-addressed
- All canonical facts in ledger
- All graph state rebuildable
- All agent/model/tool versions attributable
- All costs attributable
- All information boundaries recorded
- All actions policy checked
- All external effects idempotent

Then: delete Hydra → rebuild Hydra → verify lineage.

## Do NOT Build Yet

- Large frontend
- Dozens of Etsy listings
- Complex multi-agent org charts
- Fine-tuning
- OperatorTwin predictive model
- Automatic large ad-spend policy
- Hindsight dependency
- Full autonomous refunds/customer service

Capture contracts/data for these. Don't build before the loop works.

## Deliverables

### private-lab
Kernel fixes, universal company contracts, RunReceiptV2, WorldExperiment, policy layer, reconciliation, attribution, information-boundary, CompanyDay primitives, tests

### StallSpy
Python package, private-lab integration, Etsy domain contracts, fixture adapter, gateway skeleton, MarketSignal adapter, state snapshot compiler, problem/hypothesis pipeline, CompanyDay adapter, ColdReview adapter, Dogcasso template contract, tests, AGENTS.md, ARCHITECTURE.md

### finalbuilds
No destructive changes. Document what was ported.
