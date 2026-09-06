# How It All Comes Together — Autonomous Ecom via WorkerKit

## The Existing Infrastructure

```
/bitt
├── private-lab/lab/contracts/     ← Pydantic frozen models (RunSpec, Worker, Finding, etc.)
├── private-lab/lab/controller/    ← Orchestrate: INGEST → MATCH → ALLOCATE → DISPATCH → OUTCOME → LEARN
├── private-lab/lab/evaluation/    ← RunEvaluator, paired evaluation
├── workers/bitsec/learning_loop.py ← CGE → FailureCluster → mutation → promotion
├── workers/bitsec/miner_v5.py     ← Scout/Strategist/Analyst pipeline
├── tooling/agentvault/            ← Credential storage (Fernet encrypted)
├── integration/hydra/             ← HydraDB graph database (experience graph)
├── mwgym/                         ← CG worlds, deterministic evaluation
└── cge/                           ← Candidate generation / evolution
```

## The Mapping: Ecom → Existing Contracts

### What Already Exists

| Lab Contract | Ecom Equivalent |
|-------------|-----------------|
| `Worker` | Ecom worker (product scout, store builder, ad optimizer) |
| `WorkerVersion` | Immutable version of ecom worker |
| `RunSpec` | One attempt at a niche/product/country |
| `Finding` | Product opportunity, ad creative, store config |
| `TaskInstance` | "Find profitable products in Finland for espresso niche" |
| `CapabilityPool` | "ecommerce", "product-research", "google-ads" |
| `Venue` | "google-shopping", "etsy", "shopify" |
| `BudgetEnvelope` | Ad spend limits, API costs, time constraints |
| `ExperimentSpec` | A/B test: this product at this price in this country |
| `ExperimentResult` | Conversion rate, CPC, AOV, profit margin |
| `LearningProposal` | "Expand heated-jacket collection because Finland converting at 8%" |
| `ImprovementReceipt` | Validated: new product added, margin improved, etc. |
| `FailureCluster` | "This product rejected: margin too thin after VAT/shipping" |
| `LabController` | Orchestrates the full pipeline |
| `Ledger` | Immutable record of every decision and outcome |
| `ArtifactStore` | Store screenshots, ad creatives, product images |
| `HydraDB` | Experience graph: product × country × date × outcome |

### What We Need to Add

```python
# New contracts for the ecom domain

class ProductOpportunity(FrozenModel):
    """A product candidate from the scanner."""
    product_id: str
    gtin: str = ""
    name: str
    category: str
    supplier_cost: float
    supplier_url: str = ""
    google_search_volume: int = 0
    google_cpc_range: tuple[float, float] = (0, 0)
    google_best_seller_rank: int = 0
    competitor_count: int = 0
    price_benchmark: float = 0
    margin_estimate: float = 0
    countries: list[str] = Field(default_factory=list)
    status: str = "scanned"  # scanned → validated → listed → tested → scaled → rejected


class StoreConfig(FrozenModel):
    """Configuration for a specialist store."""
    store_id: str
    niche: str
    domain: str
    country: str
    language: str
    currency: str
    payment_methods: list[str] = Field(default_factory=list)
    shipping_config: dict = Field(default_factory=dict)
    tax_config: dict = Field(default_factory=dict)
    product_count: int = 0
    monthly_revenue: float = 0
    monthly_profit: float = 0


class AdCampaign(FrozenModel):
    """Google Ads campaign state."""
    campaign_id: str
    store_id: str
    budget_daily: float
    products_included: list[str] = Field(default_factory=list)
    roas: float = 0
    cpc: float = 0
    ctr: float = 0
    conversion_rate: float = 0
    total_spend: float = 0
    total_revenue: float = 0
    status: str = "paused"  # paused → testing → scaling → optimized


class SupplierAudit(FrozenModel):
    """Supplier quality assessment."""
    supplier_id: str
    name: str
    country: str
    has_eu_warehouse: bool = False
    shipping_speed_days: int = 0
    warranty_months: int = 0
    return_address: str = ""
    live_stock: bool = False
    gtin_available: bool = False
    sample_ordered: bool = False
    score: float = 0  # 0-100


class CountryMarket(FrozenModel):
    """Market intelligence for a country × niche."""
    country: str
    niche: str
    search_volume_total: int = 0
    avg_cpc: float = 0
    competitor_density: int = 0
    payment_preferences: list[str] = Field(default_factory=list)
    shipping_preferences: list[str] = Field(default_factory=list)
    currency: str = ""
    vat_rate: float = 0
    customs_duty: bool = False
    opportunity_score: float = 0
```

## The Pipeline (Wired to LabController)

```text
OPPORTUNITY ORACLE (MW oracle or Google API)
    │
    ▼
LabController.ingest_opportunity()
    │
    ├── Match to Pool: "product-research"
    ├── Match to Venue: "google-shopping"
    ├── Match to Worker: ecom-scout-worker
    │
    ▼
DISPATCH
    │
    ▼
EcomScoutWorker.run()
    │
    ├── 1. Scan Google Best Sellers (API)
    ├── 2. Scan Google Keyword Planner (API)
    ├── 3. Scan AliExpress/Alibaba (scraper)
    ├── 4. Score each product × country
    ├── 5. Reject thin-margin (automatic)
    ├── 6. Return: list[ProductOpportunity]
    │
    ▼
LabController.record_outcome()
    │
    ├── HydraDB: ProductOpportunity nodes
    ├── Ledger: immutable record
    ├── LearningProposal: "add 20 heated-jacket variants to Finland store"
    │
    ▼
EcomStoreWorker.run()
    │
    ├── 1. Check SupplierAudit
    ├── 2. Check CountryMarket economics
    ├── 3. If passes: create/update Shopify listing
    ├── 4. Generate localized PDP (AI)
    ├── 5. Generate Merchant feed
    ├── 6. Push to Google Shopping
    │
    ▼
LabController.record_outcome()
    │
    ├── HydraDB: StoreConfig + AdCampaign nodes
    ├── Ledger: listing created, feed pushed
    │
    ▼
EcomAdWorker.run()
    │
    ├── 1. Check AdCampaign performance
    ├── 2. If ROAS > 2.5: scale budget 20%
    ├── 3. If ROAS < 1.5: pause product
    ├── 4. If new products available: add to campaign
    ├── 5. Generate new ad creatives (AI)
    │
    ▼
LabController.record_outcome()
    │
    ├── HydraDB: AdCampaign updated
    ├── Ledger: budget changed, creative generated
    │
    ▼
CGE (Candidate Generation & Evolution)
    │
    ├── Reads FailureClusters from Ledger
    │   "3 products rejected: margin < 15% after VAT"
    │   "Finland espresso converting at 2.1% (below threshold)"
    │   "Norway boot dryers: 6.2% conversion, scaling"
    │
    ├── Proposes mutations:
    │   "Expand Norway winter-gear collection"
    │   "Remove espresso from Finland (thin margin)"
    │   "Add 15 new heated-jacket SKUs (proven demand)"
    │
    └── PromotionReceipt or REJECT
```

## The Key Insight: Same Learning Loop

The BitSec worker uses:

```
FailureCluster → CGE → mutation → sealed evaluation → promotion
```

The ecom worker uses the SAME loop:

```
FailureCluster ("margin too thin", "conversion below threshold", "supplier rejected")
    → CGE
    → mutation ("expand this collection", "remove this product", "test new country")
    → sealed evaluation (run against Google API data)
    → promotion or reject
```

**The lab doesn't care whether it's security or ecommerce.** The contracts are domain-agnostic.

## HydraDB Experience Graph

After running for a month:

```
ProductOpportunity
    ├── "heated-jacket" → Finland → 8.2% conversion → SCALE
    ├── "heated-jacket" → Norway → 6.1% conversion → SCALE  
    ├── "heated-jacket" → Denmark → 3.1% conversion → WATCH
    ├── "espresso-tamper" → Finland → 1.8% conversion → REJECT
    ├── "espresso-tamper" → Norway → 4.5% conversion → TEST
    ├── "dog-car-seat" → Finland → 9.3% conversion → SCALE
    └── ...

StoreConfig
    ├── "home-barista-fi" → 47 products → €12k/month
    ├── "winter-gear-no" → 32 products → €8k/month
    └── ...

AdCampaign
    ├── "home-barista-fi" → ROAS 3.2 → scale to €50/day
    ├── "winter-gear-no" → ROAS 2.8 → scale to €30/day
    └── ...
```

Then the query becomes:

> "Which product × country combinations have the highest margin and should be scaled?"

HydraDB answers from real data, not guessing.

## The Credential Layer

AgentVault already handles:

```
H1_API_TOKEN → HackerOne
BC_API_TOKEN → Bugcrowd
GH_PAT → GitHub/Gittensor
```

Add:

```
SHOPIFY_API_KEY → Shopify Admin API
GOOGLE_ADS_API_KEY → Google Ads
GOOGLE_MERCHANT_API_KEY → Merchant Center
ALIEXPRESS_API_KEY → AliExpress
CJ_API_KEY → CJ Dropshipping
ETSY_API_KEY → Etsy
STRIPE_API_KEY → Stripe
```

Worker retrieves credentials via:

```python
from agentvault import get_credential
shopify_key = get_credential("SHOPIFY_API_KEY", vault="ecom-worker")
```

## The Autonomous Loop (Final)

```
EVERY DAY:
    1. Scanner: Google Best Sellers + Keyword Planner → new opportunities
    2. Evaluator: margin calculation (cost + shipping + VAT + payment + returns)
    3. Router: which products go to which countries
    4. Store Manager: add winners, remove losers
    5. Ad Optimizer: scale winners, pause losers
    6. Creative Generator: new ad variants for winners
    7. Learning Loop: FailureCluster → CGE → mutation → promotion
    8. HydraDB: record everything
    9. Human Queue: approve high-spend decisions

HUMAN APPROVALS:
    - Budget > €100/day change
    - New country launch
    - New supplier (sample ordered)
    - Store design changes
    - Anything with legal/compliance implications
```

## What We Clone Now

| Repo | What We Use |
|------|------------|
| bin1732/global-ecommerce-intelligence | Product selection, compliance, pricing, profit, PPC |
| Attribuly-US/ecommerce-dtc-skills | AI marketing analytics, ROAS tracking |
| chenyedamw/dropshipping-product-scout | MCP server for product research |
| shopnex-ai/shopnex | Open-source Shopify alternative |
| lofder/dsers-mcp-product | MCP for AliExpress → Shopify |
| sudheer-ranga/aliexpress-product-scraper | AliExpress product data |

## Next Steps

1. Define ecom contracts in `lab/contracts/ecommerce.py`
2. Create `workers/ecom/` directory structure
3. Wire scanner → controller → worker → learning loop
4. Add ecom venues to HydraDB (google-shopping, etsy, shopify)
5. Build the first worker: product scout
6. Test with one niche × one country
7. Scale
