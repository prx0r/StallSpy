# Dogcasso — The £0 → £1M Etsy Experiment

**Brand:** Dogcasso Studios
**Tagline:** "We make tiny movies about the people you love."
**URL:** dogcasso.com

---

## What This Is

An autonomous economic agent laboratory building a portfolio of specialist Etsy gift studios, powered by AI video generation, documented daily as a public experiment.

**The flywheel:** Build stores → Content → Audience → Sales → Validation → More content → More audience.

---

## The Portfolio

20 specialist studios. One factory underneath.

| Tier | Studios | Status |
|------|---------|--------|
| **Build now** | GameWinnerz, Dogcasso, Greatest Hits, StoryStar, Cover Story | Dedicated shops |
| **Graduate if validated** | Arcana, Legend Cards, Wanted, TrailerMade, Starter Pack, Front Page, RetroQuest, Career Legend | Shared engine |
| **Viral laboratories** | MemeMint, Cerealized, Natural Habitat, EraMade, Main Event | Experiment |

See `MASTER_PLAN.md` for the full £0 → £1M experiment plan.
See `PORTFOLIO_SPEC.md` for full 20-store strategy.

---

## The Tech Stack

- **MiniMax H3** — primary render engine (text-to-video + audio)
- **LTX-2.5** — fast drafts and iteration
- **ComfyUI** — workflow orchestration
- **FFmpeg** — post-production
- **Vast.ai / RunPod** — GPU infrastructure
- **Prodigi** — physical fulfillment (cards, mugs, posters, books)
- **Etsy Open API v3** — marketplace execution
- **SQLite + Python** — data warehouse and analytics

See `TECH_STACK.md` for full architecture.

---

## The Content Engine

Daily YouTube + blog documenting the journey from £0 to £1M.

- **Daily Short** (30-60 sec): what happened today
- **Weekly Stitch** ("Etsy Money Week X"): 7 shorts + stats
- **Monthly Deep Dive** (5-10 min): full analysis
- **Quarterly Paper**: open dataset + findings

See `CONTENT_SPEC.md` for the content strategy.

---

## The Data Play

Building a free Etsy research tool to compete with EverBee ($69/mo).

- Daily marketplace snapshots (time series starts today)
- Sales estimation from reviews/favorites/views
- Seller CSV uploads for calibration
- Open dataset for researchers

See `tool/SCOPE.md` for the technical spec.
See `tool/THESIS.md` for the business thesis.

---

## Files

| File | Contents |
|------|----------|
| `MASTER_PLAN.md` | £0 → £1M experiment, flywheel, ledger, StallSpy, mini-paper |
| `PORTFOLIO_SPEC.md` | 20-store strategy, promotion system, economics |
| `CONTENT_SPEC.md` | YouTube/blog strategy, automation pipeline |
| `STRATEGY.md` | Moonpig thesis, competitive positioning, flywheel |
| `GOLD_IDEAS.md` | All key strategic insights from founding conversation |
| `ENGINES.md` | 8 core generation engines + matrix |
| `STORYBOARDS.md` | Shot-by-shot blueprints |
| `H3_PROMPT_RULES.md` | 6 canonical prompting rules |
| `TEMPLATE_FORMAT.md` | YAML schema + prompt compiler |
| `CATALOGUE.md` | Product catalogue (Classics/Trending/Occasions) |
| `PRICING.md` | Tier structure, upsells, economics |
| `TECH_STACK.md` | Models, GPUs, workflow, cost per unit |
| `FULFILLMENT.md` | Digital delivery, physical cards, books, AR |
| `STOREFRONT_UX.md` | Browse-by-joke interface |
| `TREND_RADAR.md` | Trend monitoring system |
| `RETENTION.md` | Gift CRM, reminders, referral loop |
| `CHATBOT_UX.md` | Conversational interface design |
| `PARTNERSHIPS.md` | Affiliate commerce, bundle architecture |
| `CUSTOMERS.md` | Customer segments, ad channels, pricing psychology |
| `ADS.md` | Channel priority, creative rules, budget progression |
| `MEME_CATALOGUE.md` | 10 meme products ranked by difficulty |
| `CONTENT_LANES.md` | 3 content lanes + 2 independent axes |
| `MISIRECTION_SKITS.md` | 6 shot-by-shot tension/misdirection skits |
| `AD_TESTING.md` | Test slate, ad-testing loop, cost per test |
| `GAMEWINNER_SEO_STRATEGY.md` | Etsy SEO for Game Winner products |
| `BUILD_BLUEPRINT.md` | Implementation tickets |
| `CANONICAL_RESOURCE.md` | Etsy tooling landscape |
| `tool/SCOPE.md` | Data cooperative build spec |
| `tool/THESIS.md` | EverBee competitor thesis |
| `tool/scrape.py` | Live Etsy API scraper |
| `tool/ml/` | ML repos + datasets |
| `tools/` | 7 cloned Etsy MCP servers |

---

## Key Numbers

| Metric | Current |
|--------|---------|
| Etsy API credits | 10,000/day |
| MCP servers cloned | 7 |
| ML repos cloned | 7 |
| Keywords tracked | 15 (growing to 200) |
| Live listings scraped | 200+ |
| 10K shops dataset | loaded |
| Game Winner listings | 0 (launching this week) |
| Content published | 0 (starting today) |
| Revenue | £0 |

---

*The experiment is the content. The content is the business. The business validates the content. Even if the Etsy stores fail, the timestamped dataset of someone trying is itself valuable. There is no way to lose by publishing honestly.*
