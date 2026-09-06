# AGENTS.md — StallShark

**This is the primary working spot for the StallShark / MythicBee / Moltwork project.**

All development, experimentation, and business operations happen here.

---

## Project Identity

**StallShark** — Commerce trajectory corpus + autonomous microbrand operator.

The repo contains:
- Live business data (mythicbee-ops/)
- Architecture specs (corpus/)
- Planning docs (endgame/)
- Automation + schemas (tool/)
- Brand strategy (brands/)
- 49 platinum video renderers (tool/r2_imports/)
- 12 ML research repos (tool/ml/)
- 7 Etsy MCP servers (tools/)

---

## Infrastructure

| Service | Backend | Status |
|---------|---------|--------|
| HydraDB | R2 bucket `stallshark` | Running (needs repair — see fixes/HYDRA_RECOVERY.md) |
| Etsy API | Live | Working |
| OpenCode | mimo-v2.5 | Working |
| Cloudflare R2 | 2 buckets: hydradb + stallshark | Connected |

### Credentials

**All API keys and credentials live in `.env` (never committed).**
When agent-vault is running, prefer vault for new credentials.
Reference this section before using any external service.

| Key | Where | Status |
|-----|-------|--------|
| Etsy API | .env | Live |
| R2 (general) | .env | Live |
| R2 (stallshark) | .env | Live |
| HydraDB token | .env | Live |
| OpenCode API | .env | Live |
| Cloudflare API Token | .env | Live |
| Cloudflare Account ID | .env | Live |
| Prodigi API Key | .env | Live |
| Inworld API Key | — | Not yet |
| Anthropic API Key | — | Not yet |

**Never hardcode API keys in source files. Always read from `.env` or vault.**

### HydraDB

R2 bucket `stallshark` is ready for HydraDB backend. Current instance uses `hydradb` bucket with R2.

**Known issue:** Cypher parser incompatibility with neo4j Python driver. See `fixes/HYDRA_RECOVERY.md` for the full repair brief. **Do not block MythicBee on this.**

---

## Operating Rules

1. **Build businesses. Preserve cognition. Publish one slice each day.**
2. Reality outranks narrative.
3. Never rewrite history.
4. Independent review means independent.
5. Every expenditure has a budget.
6. Autonomy earned per decision class.
7. One intervention at a time.
8. Simplest thing that works.

---

## Priority Stack

```
P0: MAKE MONEY / GET REAL DATA (60%)
P1: INSTRUMENT THE EXPERIMENT (25%)
P2: MARKET INTELLIGENCE (10%)
P3: RESEARCH STACK (5% max)
```

---

## Daily Workflow

```
Morning (5 min):
  stallshark day start → interview → priorities → WORK

During day:
  OpenCode captures everything

End of session:
  Worker debrief → export session

Evening (2 min):
  Raw voice note

Night:
  Blind review → divergence → public content
```

---

## What NOT to Build

Until 20 paid Etsy orders or 30 days data:
- New generalized databases
- New graph abstractions
- New agent runtimes
- Amazon/eBay
- Complex Arenav2 work
- Fine-tuning
- Multi-company hierarchies

---

## Session Protocol

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
