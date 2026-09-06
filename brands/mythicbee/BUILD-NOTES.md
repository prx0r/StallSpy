# MythicBee — Build Notes
**Date:** 2026-09-06
**Session:** Full product integration + MCP API

---

## What Was Built

### Core Architecture
- **Product Language** — "Make it mythical", bees as personal shoppers, missions, satchels, honey
- **Gift Intelligence** — Adaptive conversational recommender with belief state
- **GiftGraph** — Data moat (relationship/taste/outcome graphs)
- **BeeSession** — Every gift gets a bee, every bee has a mission
- **Honey** — AI credits for experimentation
- **Fulfilment** — Zero human-in-the-loop via Prodigi

### The Site
- Bartholomew art (12 poses + 2 animated WebP)
- Hive Activity Engine (186 status entries + 5 seasonal overlays)
- BeeSession persistence (localStorage)
- Honey earn/spend system
- Gift Intelligence (flash prompts + confidence tracking)
- LLM backend (Cloudflare Llama 3.3)
- Voice input (Cloudflare Whisper)
- Product language integration

### MCP API
- `create_bee` — Create new bee session
- `chat_with_bee` — Send message, get response
- `get_bee` — Get session state
- `get_concepts` — Get gift ideas
- `add_to_satchel` — Add product
- `get_satchel` — View cart
- `adjust_honey` — Earn/spend
- `list_bees` — List all sessions

---

## File Structure

```
brands/mythicbee/
├── docs/
│   ├── architecture/
│   │   ├── giftgraph.md                    # Data moat
│   │   └── GIFT-INTELLIGENCE-ARCHITECTURE.md  # Adaptive recommender
│   ├── product/
│   │   ├── PRODUCT-LANGUAGE.md             # Canonical language
│   │   ├── products.md                     # 20 product families
│   │   ├── BRAND.md                        # Brand identity
│   │   ├── PRICING.md                      # Pricing strategy
│   │   ├── CATALOGUE.md                    # Product catalogue
│   │   └── CONTENT_LANES.md               # Content strategy
│   ├── strategy/
│   │   ├── LAUNCH-DECISION.md              # Launch decision
│   │   ├── LAUNCH-PLAN.md                  # 30-day plan
│   │   └── STRATEGY.md                     # Overall strategy
│   └── operations/
│       ├── GAMEWINNERZ-FULFILMENT.md       # Fulfilment summary
│       └── GAMEWINNERZ-FULFILMENT-FULL.md  # Full spec
├── bee-session/
│   └── thesis.md                           # BeeSession system
├── honey/
│   └── thesis.md                           # Honey economy
├── hive-activity/
│   └── mythicbee-hive-activity/            # Hive Activity package
├── bartholomew-kit/                        # Character assets
├── api/
│   ├── bee-api.js                          # REST API
│   ├── mcp-server.js                       # MCP server
│   └── package.json
├── site/
│   ├── index.html                          # Main site
│   ├── js/
│   │   ├── bee-session.js                  # BeeSession system
│   │   ├── hive-activity.js                # Hive Activity engine
│   │   ├── cloudflare-ai.js                # LLM + Whisper
│   │   ├── gift-intelligence.js            # Flash prompts
│   │   ├── card-renderer.js                # Card generation
│   │   ├── prodigi-provider.js             # Fulfilment
│   │   └── order-pipeline.js               # Order flow
│   └── assets/
│       ├── poses/                          # 12 Bartholomew poses
│       └── animations/                     # 2 animated WebP
```

---

## Key Decisions

1. **Product Language frozen** — "Make it mythical", bees as personal shoppers
2. **BeeSession is first-class** — every gift gets a bee
3. **Honey = AI credits** — not money-off, exploration budget
4. **Gift Intelligence = adaptive** — not linear questionnaire
5. **Fulfilment = zero human** — Prodigi API, no manual intervention
6. **MCP API for agents** — bees as clients

---

## Deployed URLs

- **Site:** https://a1600aaa.mythicbee.pages.dev
- **API:** MCP server at api/mcp-server.js

---

## What's Next

1. Wire MCP server to Cloudflare Workers
2. Add Inworld voice integration
3. Build recipient reveal page
4. Create first GameWinners product
5. Test end-to-end flow
