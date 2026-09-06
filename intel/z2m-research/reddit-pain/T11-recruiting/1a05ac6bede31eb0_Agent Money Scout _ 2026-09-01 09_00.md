# Agent Money Scout — 2026-09-01 09:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Mon, 31 Aug 2026 19:22:49 -0700
**Message ID:** 1a05ac6bede31eb0

---

# Agent Money Scout — 2026-09-01 09:00

Current execution order: **MoltJobs → AgentPact → dealwork.ai → Complete Codes → selective Superteam/DeskCrew → productize proven work on x402/API markets.**

The clearest immediate money is still in funded task queues, not generic agent-service registries. The biggest fresh findings are **x402 Arena**, **HYRVE**, and **Molted**. x402 Arena is especially useful because its live leaderboard shows both real revenue and how brutally sparse demand is: 339 listed agents, $109.38 total revenue, 10,799 queries, 81 buyers, with most agents at $0.

## NEW THIS RUN

### 1. x402 Arena — live paid-agent leaderboard
URL: https://x402arena.gg/

What the agent does: hosts a paid endpoint in niches such as developer tools, web intelligence, finance, enrichment, weather, or utility APIs. Buyers call it over x402 and USDC goes directly to the provider wallet.

Who pays: autonomous agents/users making paid x402 calls.

Verified economics: the primary page currently shows **339 agents, $109.38 total revenue, 10,799 queries and 81 buyers**. The leaderboard includes some endpoints at $7.15 revenue, one code-assets endpoint at $0.20, CSV dedupe at $0.10, and a large majority at $0. This is strong evidence that merely listing an endpoint is not enough.

Required: hosted x402 endpoint, Base-compatible wallet, API/backend skills.

Autonomy: **10/10**.

First action: do not create another generic service. Scrape the leaderboard by niche, buyer count, query count, price and revenue; identify niches where at least 2 independent buyers exist and seller competition is low, then deploy one proven capability.

Constraints: crypto wallet/stablecoin legal eligibility applies; verify any operator terms before settlement.

Ease first $5: **4/10**. Repeatability: **10/10** if a niche gets recurring buyers.

### 2. HYRVE AI — fiat + stablecoin agent marketplace
URL: https://hyrveai.com/

What the agent does: self-registers from `skill.md`, accepts customer jobs, delivers work, and can hire other agents as subcontractors.

Who pays: marketplace clients or other agents.

Verified pricing/economics: HYRVE says **5,750+ agents and clients**, free deployment, seller keeps **85%**, platform takes 15%. It supports Stripe USD/EUR, USDT and machine payments; 48-hour escrow protects deliveries. These are first-party figures; I did not verify a specific fresh ≥$5 job this run.

Required: agent endpoint/runtime, HYRVE registration, Stripe/stablecoin setup as applicable.

Autonomy: **9/10**.

First action: cross-list only a service that has already earned on MoltJobs/AgentPact/dealwork. Do not build HYRVE-specific functionality before seeing buyer activity.

Constraints: payment-provider geography/KYC requirements may apply even where agent registration is easy.

Ease: **4/10**. Repeatability: **9/10** if actual job volume matches the claimed community size.

### 3. Molted — direct P2P Base-USDC agent jobs
URL: https://molted.work/

What the agent does: registers through API/CLI, searches open jobs, bids, coordinates, submits completion and receives direct USDC when the requester approves.

Who pays: requester agent/human directly wallet-to-wallet.

Verified economics: platform is live on **Base mainnet with real USDC**. The public docs show a $25 example job, but that is an example rather than verified live inventory, so I am not treating $25 as available money.

Required: `@molted/cli` or REST client, Base wallet, task-specific tools.

Autonomy: **10/10**.

First action: query `https://molted.work/api/jobs?status=open&sort=highest_reward` and only execute `reward >= $5` after checking that the job is genuinely open and the poster has credible payment history.

Constraints: direct P2P payment means weaker escrow protection than some competitors; reputation/payment history matter.

Ease: **4/10**. Repeatability: **9/10**.

### 4. AgentJob — pay-per-message and Task Square
URL: https://agent-job.ai/

What the agent does: lists itself for paid chats or responds to posted tasks; x402 settles USDC after paid interactions.

Who pays: users or agents continuing a conversation/hiring through Task Square.

Verified economics: primary page claims **10,000+ agents already earning USDC** and per-message settlement on Base, but I could not verify a current individual payout or aggregate revenue figure, so I would treat that claim cautiously.

Required: email/account, agent API or MCP integration, Base smart wallet.

Autonomy: **10/10** for API operation.

First action: list a narrowly useful expert agent with a concrete paid outcome rather than general chat; measure external paying users before investing further.

Constraints: check account/payment eligibility; do not infer earnings from registration counts.

Ease: **3/10**. Repeatability: **9/10** if external users appear.

### 5. true402 — machine-native paid-service directory
URL: https://true402.dev/

What the agent does: sells callable services such as token/address checks, prediction-market data, quantitative-finance calculations, web/screenshot/SEO utilities or model inference.

Who pays: autonomous agents via USDC on Base.

Payout: service-defined; no verified provider revenue figure surfaced this run.

Required: hosted API + x402 implementation + Base wallet.

Autonomy: **10/10**.

First action: inspect existing stalls and pricing, identify a repeated task already paid for elsewhere, and cross-list rather than inventing a speculative endpoint.

Constraints: financial/crypto endpoints should avoid personalized regulated advice and deceptive trading claims.

Ease: **2/10**. Repeatability: **9/10**.

### 6. Concurrent Agents Hackathon — $1,000 cash
URL: https://build.jigjoy.ai/

What the agent does: builds a multi-agent system using Mozaik where agents operate concurrently, share state and react to events rather than following only sequential chains.

Who pays: JigJoy/daily.dev/Hyperskill prize sponsors.

Verified payout: **$1,000 cash pool: $500 first, $300 second, $200 third**, plus subscriptions. Event is online, worldwide, free, September 5–6, 2026.

Required: TypeScript/Mozaik, working demo/submission.

Autonomy: **7/10**; an AI coding agent can build most of the system, but a human remains responsible for submission and compliance.

First action: adapt an existing worker architecture into concurrent opportunity discovery + execution + critic/evaluator rather than creating a standalone toy demo.

Constraints: check current registration/rules and age eligibility before entering.

Ease first $5: **2/10**. Repeatability: **3/10**.

## STILL ACTIVE FROM PRIOR RUNS

### 7. MoltJobs — best immediate first-$5 source
URL: https://moltjobs.io/open-jobs

Seven jobs are still live and each is explicitly **funded in USDC on-chain escrow**. Current examples are: compile 40 agent-suitable freelance tasks; durable-hosting guide; delivery-verification benchmark; translate quickstart into three languages; map AI-agent communities; publish a technical walkthrough; find 25 GitHub issues an agent could solve cheaply. Each pays **5 USDC**.

Who pays: bounty poster. Required: MoltJobs agent/account, research/browser/code tools; certification may gate jobs. Autonomy: **9/10**.

First action: take the **durable-hosting guide** or **delivery-verification benchmark** because both are bounded, cheap to execute and reusable.

Constraints: 5% success fee; comply with any platform certification and outreach rules.

Ease: **10/10**. Repeatability: **9/10**.

### 8. AgentPact — strongest $5–$25 small-job queue
URL: https://agentpact.xyz/needs

Current board still lists **200 needs**. Verified examples: Python code review **5–10 USDC**; API automation **10–25**; Python security/code review **10–25**; web scraping **10–25**; data analysis/visualization **10–25**; Python scraping **10–25**.

Who pays: agents/requesters using deals/USDC escrow. Required: MCP/Python/npm integration and task-specific tooling. Autonomy: **10/10**.

First action: filter `reward >= $5 AND clear_scope AND objective_acceptance AND settleable` and ignore the huge volume of penny tests.

Constraints: security work only on systems/code the requester is authorized to have tested.

Ease: **9/10**. Repeatability: **9/10**.

### 9. dealwork.ai — 162 open tasks
URL: https://dealwork.ai/

Current primary metrics: **2.6K workers, 162 open tasks, 264 completed, 83 verified reviews**, median hire-to-delivery about 1.1 days. It documents an **$80 AI-delivered production API** and a **$5 fully autonomous AI→AI contract**. Funds are locked before work begins.

Who pays: humans or agents. Required: `skill.md`/REST integration plus relevant tools. Autonomy: **9/10**.

First action: ingest all open jobs and reject anything whose acceptance condition cannot be independently reproduced.

Constraints: 10% normal fee, **3% AI-to-AI**.

Ease: **9/10**. Repeatability: **9/10**.

### 10. Complete Codes — best merge-to-payment coding loop
URL: https://www.complete.codes/en/agents

What the agent does: discovers funded repos/Sprints, implements, tests, opens a PR, and earns when the maintainer merges.

Who pays: repo sponsor. Payout: sprint-specific; only consider ≥$5.

Required: GitHub, repo toolchain, Base payout setup. Autonomy: **9/10**.

First action: rank funded work by `payout × P(merge) / expected implementation time`, with CI/testability and maintainer activity as hard inputs.

Constraints: obey repo contribution rules/licenses; no unauthorized security work.

Ease: **7/10**. Repeatability: **10/10**.

### 11. DeskCrew / x402 Bounty Hunter — paid support answers
URL: https://github.com/webmilmind1/bounty-hunter

What the agent does: reads open customer-support bounties, retrieves ticket/KB context, drafts a response, pays a small attempt fee, then receives **85% of reward** if the business approves.

Who pays: businesses posting support tickets. Required: Base/Solana wallet, x402 client, LLM. Autonomy: **10/10**.

Known economics from the project’s
