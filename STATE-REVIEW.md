# StallShark — State Review
**Date:** 2026-09-06 02:35 UTC
**Status:** 65-70% to "usable V0", 35-40% to "automatic"

---

## What Works

| Component | Status |
|-----------|--------|
| CompanyDay identity | ✅ |
| Local artifact storage | ✅ proven |
| R2 backup | ✅ proven |
| SHA-256 integrity | ✅ proven |
| Expense logger | ✅ usable |
| Git commit collection | ✅ usable, crude |
| Daily log generation | ✅ prototype |
| Daily TL;DR | ✅ prototype |
| YouTube script | ✅ prototype |
| Cron nightly job | ✅ exists |
| Meta-enquiry system | ✅ prototype |
| Day verification | ✅ prototype |

## What's Missing

| Component | Status |
|-----------|--------|
| OpenCode flight recorder | ❌ #1 priority |
| Token/model cost capture | ❌ not wired |
| Session Git before/after/diff | ❌ not automatic |
| Human session close review | ❌ not wired |
| Blind review enforced | ❌ not wired |
| PublicDailyDigest | ❌ not wired |
| Live blog | ❌ |
| Video pipeline | ❌/partial |
| YouTube/TikTok upload | ❌ |

---

## The One Pipeline That Matters

```
YOU WORK IN OPENCODE
        ↓
session starts
        ↓
record: prompts, responses, tools, model, tokens, files, errors, timestamps
        ↓
Git HEAD before
        ↓
session ends
        ↓
Git HEAD after + diff
        ↓
raw export → sanitize → SHA256 → local → R2
        ↓
SessionRecord
```

---

## The 5 Jobs Before "Experiment Live"

1. **OpenCode Flight Recorder** — capture every session
2. **Canonical CompanyDay close** — assemble sessions, expenses, perspectives
3. **PublicDailyDigest** — rights-safe structured JSON
4. **Blog + one video renderer** — static deploy + one video template
5. **Strengthen verify** — prove everything is captured

---

## The Milestone

```
OpenCode session → Git + tokens + money → R2 → CompanyDay → human review → public digest → blog + MP4
```

Get that one line working once.

Then stop being the systems architect and start being the human in the experiment.
