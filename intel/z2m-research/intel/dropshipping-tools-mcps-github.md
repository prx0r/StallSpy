# Dropshipping Tools, MCPs & GitHub Resources (Sept 2026)

---

## GitHub Repos Worth Cloning

### Open-Source E-Commerce Platforms

| Repo | Stars | What It Does | Why We Care |
|------|-------|-------------|-------------|
| **shopnex-ai/shopnex** | Growing | Open-source Shopify alternative (Payload CMS) | No Shopify fees, full control |
| **medusajs/medusa** | 25K+ | Headless commerce platform, Node.js | API-first, multi-warehouse, multi-currency |
| **openshiporg/openship** | Active | Multi-channel fulfillment at scale | Agentic commerce marketplace |
| **HULL (ndimatteo/HULL)** | 1.4K | Headless Shopify starter (Next.js + Sanity) | Modern stack, fast |
| **itswadesh/svelte-commerce** | Active | Open-source headless for Medusa/Shopify/Woo | Svelte, fast |

### Dropshipping Automation

| Repo | What It Does |
|------|-------------|
| **lofder/dsers-mcp-product** | MCP server for AliExpress/Alibaba → Shopify via DSers. 9 tools, 4 workflow prompts, zero-password auth, safety checks |
| **dsers/dsers-mcp-server** | Official DSers MCP Server (Apache 2.0) |
| **sudheer-ranga/aliexpress-product-scraper** | AliExpress product details as JSON (feedback, variants, shipping, images) |
| **ndgigliotti/shopify-spy** | Extract structured data from Shopify websites |
| **malikad778/nexus-inventory** | Laravel multi-channel inventory sync (Shopify, WooCommerce, Amazon, Etsy) |
| **bagisto/laravel-aliexpress-dropship** | Laravel AliExpress dropship package |

### AI Business Skills

| Repo | What It Does |
|------|-------------|
| **minhnv0807/ai-business-skills** | 138 bilingual AI marketing skills for Claude Code/OpenCode. Includes dropshipping, content, design, performance. 4 regions (US/EU/SEA/LATAM) |

---

## MCP Servers for E-Commerce

### Dropshipping MCPs

| MCP Server | What It Does | Link |
|-----------|-------------|------|
| **DSers MCP Product** | Import AliExpress/Alibaba → Shopify/Wix. Bulk import, pricing rules, SEO, safety checks | github.com/lofder/dsers-mcp-product |
| **DSers Official MCP** | Official DSers MCP Server | github.com/dsers/dsers-mcp-server |
| **AutoDS + Claude** | Chat with AI agent to run store tasks (eBay, Shopify, WooCommerce) | autods.com |
| **GetHookd MCP** | E-commerce analytics via MCP | gethookd.ai/mcp |

### Product Research MCPs

| MCP Server | What It Does |
|-----------|-------------|
| **Amazon All-in-One Scrape MCP** | Real-time Amazon SP ad placements, keyword tracking, review data. MIT license |
| **mcp-producthunt** | Product Hunt data via GraphQL API |
| **VOC AI** | Voice-of-customer from Amazon reviews, REST API + MCP |
| **Dropship.io** | Track real revenue of live Shopify stores |
| **AliShopping** | AliExpress product data, trending scores, competition analysis |

### Agentic Commerce

| Resource | What It Does |
|---------|-------------|
| **awesome-agentic-commerce** | Curated list: protocols, MCP servers, tools, APIs for AI agents that shop/sell/transact |
| **OpenShip Agentic Marketplace** | Open-source ChatGPT Checkout (marketplace.openship.org) |
| **Shopify UCP** | Universal Commerce Protocol — open standard for AI agents to transact with any merchant |

---

## High-Alpha Product Research Tools

| Tool | Price | Best For |
|------|-------|---------|
| **Minea** | Paid | Ad intelligence + TikTok products |
| **Sell The Trend** | Paid | AI automation |
| **Niche Scraper** | $49/mo | Shopify insights, thousands of products daily |
| **Dropship.io** | Paid | Competitor store revenue tracking |
| **TikTok Creative Center** | Free | Trending products, viral scores |
| **Google Trends** | Free | Demand validation |
| **AliShopping** | Free beta | AliExpress data + winning scores |
| **Thieve.co** | $23-89/mo | Curated products with conversion scores |
| **FindNiche** | Paid | Store intelligence |
| **ZIK Analytics** | Paid | eBay dropshipping research |

---

## Product Research APIs

| API | What It Does |
|-----|-------------|
| **AliExpress API** | Product search, details, pricing |
| **Alibaba API** | Wholesale product data |
| **Google Ads API** | Keyword Planner, forecasts, bid ranges |
| **Google Merchant API** | Best Sellers, benchmark prices, competitive visibility |
| **Amazon SP-API** | Product search, pricing, reviews |
| **Printify API** | POD product catalog + fulfillment |

---

## The Stack We Should Build

```
OPPORTUNITY LAYER
├── Google Best Sellers API → what sells where
├── Google Keyword Planner → demand + competition
├── Google Price Benchmark → pricing opportunity
├── AliShopping/Alibaba API → supplier matching
└── Trendsmcp → trend validation

EXECUTION LAYER
├── DSers MCP → product import to Shopify
├── Shopify API → store management
├── Google Merchant API → feed generation
└── Google Ads API → campaign management

INTELLIGENCE LAYER
├── Dropship.io → competitor tracking
├── Minea → ad intelligence
├── TikTok Creative Center → viral signals
└── Google Trends → demand signals

AI LAYER
├── Claude/GPT → product descriptions, SEO
├── AI UGC → creative generation
├── AI Ad Copy → localized ad content
└── AI Customer Service → chatbot
```

---

## Key Insight: MCP is the Bridge

The biggest shift in 2026 is that **MCP servers connect AI agents to e-commerce platforms**. Instead of clicking buttons in a dashboard, you describe outcomes in natural language:

> "Import this product from AliExpress, mark up 2.5x, rewrite the title for SEO, and push to my US store as a draft."

DSers MCP does this today. AutoDS connects to Claude via MCP. The whole industry is moving this direction.

Our GeoCommerce system should use MCP as the integration layer between our opportunity scanner and the execution platforms.

---

## Shopify's Open-Source Pivot (2026)

- **Hydrogen Developer Preview** — framework-agnostic, runtime-agnostic, designed for AI agents
- **Universal Commerce Protocol (UCP)** — open standard co-built with Google for AI agent transactions
- **Catalog API** — LLM-powered API clustering billions of products for AI agents

AI-driven orders on Shopify grew **11x YoY**. 71% of AI-attributed orders came from **long-tail niches**.

---

## Sources

- github.com/topics/dropshipping
- github.com/topics/shopify
- dev.to: DSers MCP comparison
- mcp.so: DSers MCP Product
- awesome-agentic-commerce (GitHub)
- autods.com/blog/ai-agents-for-ecommerce
- scavio.dev: Best Dropshipping Research APIs 2026
- seonib.com: Shopify Open Source 2026
- shopify.com/news/spring-26-edition-dev
