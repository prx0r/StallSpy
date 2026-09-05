# The Human–Agent Operating System

**Date:** 5 September 2026

---

## The Central Question

> For an AI-native company, what allocation of cognition between human and machines maximizes long-run economic return—and how can that allocation itself be learned from experience?

The company becomes the experiment.

---

## Five Layers That Must Never Be Conflated

| Layer | Meaning |
|-------|---------|
| **Constitution** | Invariants every worker must obey |
| **Operator model** | What the human appears to value/do |
| **Empirical policy** | What historical outcomes indicate actually works |
| **Current intent** | What the human wants *right now* |
| **Task context** | What this particular worker needs for this job |

---

## AGENTS.md — Permanent Operating Axioms

Keep it small and constitutional. 15 axioms:

1. Reality outranks narrative.
2. Preserve evidence before abstraction.
3. Never rewrite history.
4. Distinguish fact, inference, preference and hypothesis.
5. Human preference is not ground truth.
6. Independent review means independent.
7. Every meaningful expenditure has an intended return.
8. Ask humans where their marginal value is high.
9. Autonomy is earned per decision class.
10. Prefer experiments that reduce important uncertainty.
11. Do not promote a lesson merely because an agent wrote it.
12. Context is an economic resource.
13. The business precedes the documentation.
14. Optimize the organization, not individual agent cleverness.
15. Record sufficient provenance that a future model can reinterpret the raw evidence.

---

## Orientation Checkpoints (Not Hardcoded Token Intervals)

Triggered by:
- context utilization > threshold
- session compaction imminent
- major task phase completed
- major assumption changed
- large Git diff completed
- significant unexpected result
- BATS budget 50% consumed
- BATS budget 80% consumed
- before irreversible action
- worker is about to terminate

Each checkpoint asks:
- CURRENT MISSION
- CURRENT WORK ORDER
- CURRENT STATE
- CURRENT BOTTLENECK
- CURRENT BELIEFS
- NEW INFORMATION
- PLAN DEVIATION
- BUDGET
- UNRESOLVED RISKS
- NEXT ACTION
- CONTEXT TO PRESERVE

---

## Raw Prompts Are Behavioral Telemetry

Store the human's uncompressed direction at the exact time decisions form.

Extract longitudinal features per intervention:
urgency, certainty, enthusiasm, frustration, risk appetite, desired speed, desired quality, complexity tolerance, exploration appetite, capital willingness, delegation willingness, creative conviction, desire for control, perceived opportunity magnitude, perceived downside.

Model as inferences, not asserted facts:

```json
{
  "signal": "urgency",
  "estimate": 0.83,
  "confidence": 0.71,
  "evidence_refs": ["message_928"],
  "extractor_version": "v3"
}
```

---

## PPL Integration

Human interventions contain information about the **future trajectory the human is trying to prevent**.

Interpret:
```
CURRENT STATE → HUMAN INTERVENTION → IMPLIED TRAJECTORY CONCERN
→ PREFERENCE HORIZON → INFERRED TEMPORARY POLICY
```

---

## HumanValueModel

```
Marginal Human Value =
    E[outcome | human consulted]
  - E[outcome | no consultation]
  - interruption_cost
```

Ask human only when Marginal Human Value > 0 by enough margin.

---

## Human Queue (First-Class System)

Every item must specify:
- task
- reason human needed
- agent best answer
- agent confidence
- expected human value (USD)
- expected human minutes
- urgency
- reversibility

Evaluate queue performance:
- Naming input: +38% downstream preference
- SEO input: no measurable improvement
- Thumbnail selection: +4% CTR but costs 12 min
- Customer service: no improvement over agent
- New-product ideation: 3.1x more promoted concepts

---

## Memory Has a P&L

For every memory:
- times retrieved
- tokens added
- total retrieval cost
- tasks where retrieved
- measured performance delta
- economic outcome delta

**Memory ROI** = some memories cost 2M tokens and never change an action (delete from hot retrieval). Others cost 300 tokens and prevent £50 mistakes (promote).

---

## Four Memory Temperatures

```
RAW / COLD       Complete transcripts, never auto-inserted
EPISODIC / WARM  Relevant trajectories, retrieved by similarity
SEMANTIC / HOT   Empirically supported compact principles
CONSTITUTIONAL   AGENTS.md axioms, always loaded
```

---

## Operator Memory (Four Categories)

```
STABLE PREFERENCE    "I strongly value X."
CONTEXTUAL PREF      "When Y is true, prefer X."
ROUTINE              "In this state, human usually does X."
LATENT RULE          "Observed behavior suggests X, never stated."
```

Current explicit intent ALWAYS outranks operator memory.

---

## Return on Cognition

```
economic value created
────────────────────────
human time + inference spend
```

---

## TokenWise + BATS Integration

```
BATS          → economic/resource policy
                ↓ budget envelope
TokenWise     → execution-level model routing
                ↓
Hydra         → "did spending $0.25 produce value over $0.07?"
                ↓
BATS updates
```

---

## Hierarchical Objective Function

```
LEVEL 0: invariants (legal/policy/safety/capital)
LEVEL 1: survival (avoid catastrophic loss)
LEVEL 2: economics (maximize risk-adjusted contribution)
LEVEL 3: learning (reduce decision-relevant uncertainty)
LEVEL 4: asset accumulation (build reusable IP/data/distribution)
LEVEL 5: human attention (minimize involvement subject to performance)
LEVEL 6: autonomy (increase only where evidence supports it)
```

---

## Learned Operator Phenotype

Not "best entrepreneur personality" but **state-conditioned management policy**:

```
cold start + Q4 approaching → Attacker wins
stable winner + high organic conversion → Conservator wins
novel unvalidated product → Exploratory low-dollar policy wins
```

---

## The Three Learned Models

```
Operator(Tom | state)        → What would this founder think/do?
HumanValue(task, state)      → How useful would asking be?
EconomicPolicy(action | state) → What does experience indicate?
```

The manager reasons:

```
I know what Tom would probably say.
I know how often Tom has been right for this kind of decision.
I know what I independently recommend.
I know how novel this state is.
I know the economic downside.
I know the cost of interrupting him.

Therefore: ACT or ASK.
```

---

## The Endgame Definition of Autonomy

Not: "Nobody human ever touches it."

Instead:

> **The system determines empirically where human cognition creates positive marginal value and requests precisely that cognition while autonomously handling the rest.**

---

*The raw prompt corpus is foundational because the Operator model isn't trained only on neat labels. It inspects the complete situated language, evolving vision, interventions, emphasis, corrections, contradictions and changing ambitions that produced every decision.*
