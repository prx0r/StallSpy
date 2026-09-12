# Handover — 2026-09-12 (MogMug session)

## Where everything lives

- Code + plans: `/stallspy` → `prx0r/StallSpy@master` (all pushed, tree clean — verify with `git status`)
- Frontend spec docs: `~/mogmug` (11 numbered notes, local only, indexed in `00-INDEX.md`)
- Vaults: `prodigi` (PRODIGI_API_KEY live), `etsy` (KEYSTRING + SHARED_SECRET)
- Company substrate: `/agentcom` → `prx0r/agentcom@main`

## Built today (StallSpy commits, oldest → newest)

1. `66cac6b` — MOGMUG_DEV_PLAN.md + character-kit (Character schema, conversion copy, loading engine)
2. `6d31dcc` — funnel (Etsy 5 fields, photo pipeline, 10 recipes, Prodigi builder, portals, free-tier)
3. `0c8713c` — Prodigi import (api/products/pricing-shipping/etsy docs, real mug+card SKUs)
4. `5435df7` — catalogue (200+/500k count, portal-fit categories, top-10 picks)
5. `b915569` — THE TEN locked (8 heroes + 2 Xmas, LAUNCH_TEN in code, 9 tests green)
6. `b2db832` — OCCASIONS.md (Halloween/birthday/M-Day/F-Day on verified SKUs)
7. `459701d` — TOPSELLERS.md (repo seller-data audit, transferable patterns, pet scrape spec)
8. `5159255` — FINAL_LISTINGS.md (occasion targets, £1.99 clip menu, kill criteria)
9. `8a954ea` — CANONICAL_PRODUCTS.md (1 digital + 10 physical, frozen)
10. `8ed73b1` — COSTS_UK.md v1 (estimates, shipping flagged)
11. `341ac87` — COSTS_UK.md v2 (**live quotes, all 10 SKUs, margin verdicts**)

Tests: `node --test character-kit/tests/*.mjs` → 9 green.

## Key findings (don't re-derive)

- The pasted UUID is the LIVE Prodigi key (401 sandbox, 200 live). Stored as PRODIGI_API_KEY.
- Live UK Standard totals incl VAT in COSTS_UK.md. Bauble loses on Standard (ship Budget);
  stickers bundle-only; magic/bandana/ornament need +£2–3 or Budget.
- No stallshark repo exists. Prior Etsy research = `research/archive/MARKET_RESEARCH.md` + `tool/data/*.csv`.
- Site storefront still MythicBee-branded; rebrand not started.
- Pet-niche Etsy scrape still unwired (keys must go via vault proxy, never env paste).

## Open threads

- Sample pack order (50% off first) + quality check before listings go live.
- Memorial art pack + human-review gate before Q4.
- Playing-card SKU for trading-card route.
- Xmas art deadline early Nov (ornaments 120h production).
