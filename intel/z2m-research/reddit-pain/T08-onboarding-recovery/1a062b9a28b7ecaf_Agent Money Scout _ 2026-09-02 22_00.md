# Agent Money Scout — 2026-09-02 22:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Wed, 2 Sep 2026 11:25:27 -0400
**Message ID:** 1a062b9a28b7ecaf

---

# Agent Money Scout — 2026-09-02 22:00

## NEW THIS RUN

### 1. Freelancer — Centralized AI-Powered Business Reporting System — A$1,500–3,000
URL: https://www.freelancer.com/projects/data-analytics/centralized-powered-business-reporting

Fresh open project. The buyer wants a near-hands-free ETL/reporting system: Excel/CSV/SQL/CRM/API/SharePoint inputs → Python/Pandas cleaning, validation and deduplication → centralized SQL → scheduled incremental updates → audit/error logs → automatic Power BI refresh. The primary page showed 22 proposals, payment method verified, and average bids around A$1,928 when checked.

Who pays: verified Freelancer buyer. Tools: Python, Pandas, SQL, REST APIs, Power BI/Power Query. Autonomy: 9/10. First action: bid around a bounded phase 1: source contracts + canonical schema + one scheduled incremental pipeline + validation report. Constraints: use only customer-authorized data/access; ordinary Freelancer account/payment rules apply. Ease first $5: 8/10. Repeatability: 10/10.

### 2. Upwork — CRM Workflow Automation / Lead Management — $1,000 fixed
URL: https://www.upwork.com/freelance-jobs/apply/CRM-Workflow-Automation-Lead-Management-Automated-Follow-Ups_~022095077835804934482/

Posted September 2. The client says it needs five freelancers, and the crawl showed only 5–10 proposals and zero interviews. Scope is lead capture → CRM organization → communication tracking → automated follow-up.

Who pays: Upwork client. Tools: CRM APIs, n8n/Make/Zapier or code, lead-state logic. Autonomy: 8/10. First action: apply with an explicit state machine and idempotent follow-up logic. Important caveat: client joined Upwork today, so treat headline budget as low-confidence until an Upwork milestone is funded. Ease: 7/10. Repeatability: 10/10.

### 3. Upwork — Recruitment lead automation — $150 fixed
URL: https://www.upwork.com/freelance-jobs/apply/Automation-Specialist-for-Recruitment-Workflow_~022095117861253926413/

Posted September 2. Build a small workflow: form/email → AI extraction → structured lead → Google Sheets upsert → predefined qualification → Slack/email notification. Buyer has ~$1.1K historical Upwork spend and 4 hires; competition is high at 50+ proposals.

Who pays: established Upwork client. Tools: n8n/Make/Zapier, OpenAI/ChatGPT API, Sheets, Slack/email. Autonomy: 9/10. First action: submit a very specific implementation/test plan rather than a generic agent pitch. Human-defined criteria should drive qualification; do not make sensitive employment decisions autonomously. Ease: 5/10. Repeatability: 10/10.

### 4. Upwork — n8n workflow stopped triggering — fresh repair micro-job
URL: https://www.upwork.com/freelance-jobs/apply/n8n-Workflow-Fix-Stopped-Triggering_~022094779649740833061/

Fresh September 2 buyer: an existing n8n workflow used to work and has stopped triggering. This is ideal for an autonomous diagnostic worker: trigger config → credentials → webhook/event source → execution log → schema change → replay → regression test.

Payout: the current search result did not expose a reliable budget, so no payout is invented. Tools: n8n, API/webhook debugging. Autonomy: 9/10. First action: offer a diagnose-before-modify workflow and a concise root-cause/runbook deliverable. Ease: 8/10 if budget is worthwhile. Repeatability: 10/10.

### 5. Freelancer — AI/Python automated reporting as a product category
URL: https://www.freelancer.com/projects/data-analytics/centralized-powered-business-reporting

The A$1.5K–3K project is direct evidence that companies will pay for the boring but valuable layer: heterogeneous business data → trusted operational/reporting tables → automatic refresh → failure alerts. An agent can turn this into a reusable vertical service rather than bespoke code each time.

Customer: SMB/mid-market companies with Excel + CRM + SQL fragmentation. Charge: use the live contract as market evidence; for your own MVP, start with a paid diagnostic and quote implementation after seeing the sources. First action: build a reusable connector/schema/validation skeleton. Autonomy: 9/10. Ease: 7/10. Repeatability: 10/10.

### 6. BotBounty.ai — API-native ETH-on-Base bounty marketplace
URL: https://www.botbounty.ai/

BotBounty explicitly invites agents to GET /api/agent/bounties, claim coding/research/data/automation work, submit solutions, and receive ETH on Base after approval. It advertises smart-contract escrow and no signup for agents.

Who pays: bounty posters. Tools: REST agent runtime + Base wallet. Advertised minimum is inconsistent across its copy (one section says starts at $1), so do not assume a minimum payout. Autonomy: 10/10. First action: fetch skill.md and the live bounty endpoint; execute only tasks whose escrow and reward are verifiable. Current public page does not provide enough settlement history to treat liquidity as proven. Ease: 4/10. Repeatability: 9/10 if funded inventory proves real.

### 7. NEAR AI Agent Market — USDC agent work via NEAR Intents
URL: https://market.near.ai/skill.md
Discovery reference: https://gigs.sh/p/near-ai-agent-market

gigs.sh’s May verification reports ~1.4K agents, 3.8K jobs and $24.9K cumulative volume, with example service prices around 12–24 USDC. Agents bid and execute jobs; funds are escrowed and released on acceptance.

Who pays: NEAR market job posters. Tools: NEAR account/wallet, market API, USDC/NEAR Intents. Autonomy: 10/10. First action: read current skill.md and verify current open jobs/currency before bidding, because settlement mechanics have changed over time. Ease: 5/10. Repeatability: 9/10.

### 8. AuraGate — x402 marketplace, useful signal but TESTNET only
URL: https://auragate.app/

Current primary site reports 31 services, 1,228 paid requests, 42 unique buyers and $2.58 USDC revenue — but explicitly says it is running on Arc Testnet and no real funds beyond testnet USDC move. This is NOT an earning route today.

First action: watcher only; use its request telemetry as product-research data. Ease first real $5: 0/10. Repeatability potential: 8/10 if it moves to mainnet.

## STILL ACTIVE FROM PRIOR RUNS

### 9. MoltJobs — seven literal 5-USDC tasks
URL: https://moltjobs.io/open-jobs

Verified again. Seven jobs at 5 USDC each remain visible, including: compiling 40 agent-suitable freelance tasks, durable-hosting research, delivery-verification benchmarking, translating the quickstart, mapping agent communities, publishing a walkthrough, and finding 25 agent-suitable GitHub issues. The GitHub task showed only about five hours remaining at crawl time; most others about one day.

Who pays: MoltJobs poster; jobs are described as funded in Base-USDC escrow. Tools: MoltJobs agent/account/wallet; some jobs may require qualification. Autonomy: 10/10. First action: take the bounded research/benchmark task with the lowest external dependency. Ease: 9/10. Repeatability: 9/10.

### 10. GH Bounty — 5 / 29 / 39 SOL open
URL: https://www.ghbounty.com/

Primary live feed still shows 5 SOL open for solana-labs/web3.js retry logic, 29 SOL open for Next.js async generators, and 39 SOL open for Deno WebGPU texture compression; a 14-SOL LangChain task is reviewing and a 3.5-SOL Tauri task is paid. Funds are locked on Solana mainnet before work; validator consensus controls release.

Tools: GitHub, local dev/test environment, Solana wallet, optional MCP. Autonomy: 10/10. First action: inspect/reproduce the 5-SOL issue and check competing PRs before starting. Ease: 8/10 when technically matched. Repeatability: 10/10.

### 11. Upwork — $7,500 AI Automation / LLM / n8n role
URL: https://www.upwork.com/freelance-jobs/apply/Automation-LLM-Engineer-n8n-Specialist_~022094744072567525122/

Still live. Scope: autonomous agents, n8n, RAG, vector databases, OpenAI/Anthropic, monitoring, hallucination reduction and documentation. Latest crawl showed 10–15 proposals and one interview.

Who pays: long-standing Upwork client. Tools: n8n, Python/TS, LLM orchestration, RAG/vector DB. Autonomy: 7/10. First action: apply only with concrete production demos and measurable reliability/cost outcomes. Ease: 5/10. Repeatability: 8/10.

### 12. Superteam Earn — hidden AGENT_ONLY inventory
URL: https://superteam.fun/earn/agents

Still live. The official agent interface supports registration, discovery of AGENT_ALLOWED and hidden AGENT_ONLY listings, autonomous submission, comments, and a human claim-code flow for payout. Agents themselves do not complete wallet signing/KYC.

Autonomy: 9/10. First action: poll the dedicated agent listing endpoint, not the public feed. Rank only explicit-compensation, future-deadline, geographically eligible tasks. Ease: 6/10. Repeatability: 10/10.

### 13. gigs.sh — useful discovery layer, stale as payment proof
URL: https://gigs.sh/

The directory still lists 46 agent-earning platforms across task markets, developer bounties, security, competitions, hackathons and API monetization. Its own page says the directory was last verified May 18, 2026. Use it to generate leads, never as proof that a platform is currently paying.

Autonomy: 10/10 for discovery. First action: rotate through untested categories such as Agent Hansa, NEAR Agent Market, Toku, Drips Wave and Code4rena, then verify primary state before executing. Direct ease-to-$5: 1/10. Discovery repeatability: 10/10.

### 14. ClawTasks — still NOT a money route
URL: https://clawtasks.com/

The primary site still explicitly says it is “currently free-task only” while reliability/review flow are hardened. Older paid-bounty documentation should not override this current state.

First action: none for revenue; watcher only. Ease first $5: 0/10.

## REDDIT DEMAND SIGNALS

### 15. Business owners want outcomes, especially client acquisition
URL: https://www.reddit.com/r/n8n/comments/1nl62ae/here_are_the_n8n_automations_44_business_owners/

A practitioner summarizing conversations with 40+ business owners says the repeated pattern was that owners do not care about “AI”; they 
