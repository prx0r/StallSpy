# Q4 Oracle × Z2M Intelligence Pack — 4 Sep 2026

This pack turns current Q4 ecommerce research into an ingestible extension for the existing MW/Z2M/FinalBuilds system.

## Contents

- `00_ARCHITECTURE_SYNTHESIS.md` — how MW, Z2M and FinalBuilds should divide responsibilities
- `01_EXECUTIVE_SYNTHESIS.md` — main Q4 conclusions
- `02_CHANNEL_ECONOMICS.md` — paid/free channel benchmarks and rules
- `03_PRODUCT_OPPORTUNITY_MATRIX.md` — ranked low-capital opportunities
- `04_STORE_ARCHETYPES.md` — store types to build/reuse
- `05_AI_MOATS.md` — where AI creates a real quality/cost moat
- `06_ORACLE_Z2M_INTEGRATION.md` — schemas, sensors, events and admission logic
- `07_EXPERIMENT_BACKLOG.md` — first 30 experiments
- `data/` — machine-readable sources, benchmarks, hypotheses and opportunities
- `code/q4_intel.py` — working CLI scorer/filter
- `code/test_q4_intel.py` — tests
- `SOURCES.md` — source register

## Run the ranking CLI

```bash
python3 code/q4_intel.py --data data/opportunities.json --top 15
python3 code/q4_intel.py --data data/opportunities.json --zero-capital --top 20
python3 code/q4_intel.py --data data/opportunities.json --q4 --json
```

## Important

The `model_score_100` is a prioritization score, not proof of profitability.

Before paid spend, replace the `competition_whitespace_hypothesis` score with live competition evidence from Etsy/Google/Pinterest/marketplace data. Unknown competition should block high-spend admission.

## Recommended integration

1. Keep MW Oracle as economic-surface/data intelligence.
2. Keep Z2M as commerce sensors/strategy pack.
3. Ingest both into FinalBuilds `EconomicOpportunity`.
4. Let FinalBuilds own admission/experiment allocation.
5. Let Hermes/WorkerKit execute.
6. Write raw evidence to R2 and projections/outcomes to Hydra.
7. Attribute actual money outcomes back to source, hypothesis and build process.
