# Moltwork Lab — Documentation Cleanup

**Date:** 5 September 2026

---

## The Problem

Documentation drift. Historical files in active namespace. Unclear boundaries. No single current identity.

`/cg` is the model. Clean info architecture: README (what), AGENTS (rules), SPEC (decisions), STATUS (now), GUIDE (how).

---

## What Needs to Happen

### 1. Canonical Naming

```
System: Moltwork Lab
Internal: LAB
Repo: prx0r/qdw-workbench (don't rename yet)
Local: private-lab
```

### 2. Replace AGENTS.md

~100 lines max. Binding rules only:

```
1. Ledger + artifacts + Git are canonical
2. HydraDB is disposable derived projection
3. Hydra failure never blocks canonical operations
4. Domain concepts stay outside generic kernel
5. External side effects typed/receipted
6. Agent runtimes replaceable
7. No new framework when existing substrate works
8. No architecture redesign during bounded tasks
9. Tests include negative/broken cases
10. Current phase: Dogcasso live validation
```

Remove all credentials and stale Hydra tutorials.

### 3. Create SPEC.md

Mission → Non-goals → Architecture decisions → Module layout → Current milestone → Deferred endgame.

### 4. Create STATUS.md

Current, concise, dated. Distinguish: REAL / PARTIAL / PLANNED / FROZEN.

Primary: Dogcasso Etsy live validation.

### 5. Create docs/GUIDE.md

Operational: fresh checkout → config → tests → start Lab → run without Hydra → enable Hydra → rebuild.

### 6. Create docs/STACK.md

Map all repos: Moltwork, Moltwork Lab, CG, MWGym, StallSpy/Dogcasso, FinalBuilds.

### 7. Create docs/CONTRACTS.md

Semantic roles of RunSpec, RunReceipt, ArtifactRef, etc. Link to source, don't duplicate.

### 8. Create/update docs/HYDRA.md

Doctrine: derived, optional, rebuildable, failure never blocks.

### 9. Archive historical material

```
docs/archive/handovers/
docs/archive/plans/
docs/archive/reviews/
docs/archive/reference/
```

Root should not look like an archaeological dig.

### 10. Remove exposed credentials

Search entire repo for committed Hydra credential. Remove from docs/scripts/Python. Rotate outside Git.

### 11. Add `make doctor`

```
Git SHA / dirty
ledger OK / chain VALID
artifact store OK
Hydra OFF / READY / STALE
Hydra required: NO
tests: PASS
current phase: DOGCASSO LIVE VALIDATION
read: STATUS.md
```

### 12. Fresh-agent orientation test

Give agent only: README, AGENTS, SPEC, STATUS, HANDOVER.

Verify it answers:
- What is canonical?
- Is Hydra optional?
- What is the current live experiment?
- Where does domain code live?
- What is CG for?
- What work is frozen?
- How are tests run?
- What are next actions?

### Definition of Done

```
root = current canonical entrypoint docs only
old plans/history archived
AGENTS.md short and binding
SPEC.md = canonical architecture decisions
STATUS.md = current phase
GUIDE.md = sufficient to operate
STACK.md = all related repos
Hydra = consistently derived/optional
no credentials committed
fresh agent orients in <5 documents
tests baseline or better
```

Then stop. Don't redesign the Lab.
