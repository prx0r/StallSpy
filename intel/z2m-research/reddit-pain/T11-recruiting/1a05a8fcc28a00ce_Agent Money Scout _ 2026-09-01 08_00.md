# Agent Money Scout — 2026-09-01 08:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Mon, 31 Aug 2026 18:22:48 -0700
**Message ID:** 1a05a8fcc28a00ce

---

# Agent Money Scout — 2026-09-01 08:00

Current execution order: **MoltJobs → AgentPact → dealwork.ai → Complete Codes → Superteam Earn → selected x402/bounty protocols**.

The strongest genuinely new finding this run is **BTNOMB**: it reports **29 bounties posted and $3,000 total posted value**, with a fully machine-readable USDC/Base flow. **Clankonomy** is also strategically interesting because work is scored by uploaded eval scripts rather than subjective judges, making it unusually suitable for autonomous coding agents. Separately, **WURK** shows substantial live microtask throughput, though its worker side is primarily human and should only be used where automation is explicitly permitted.

## NEW THIS RUN

### 1. BTNOMB — agent-native bounty board with $3,000 posted value
https://btnomb.com/

BTNOMB says its bounty board has processed **29 bounties with $3,000 in total posted value**. A human or agent previews a job for free, pays **$0.10 USDC via x402** to unlock the full brief, claims it with a wallet signature, delivers, and receives payment. BTNOMB takes **5%** of the payout. The entire flow is REST-accessible.

**Agent work:** coding, research, analysis, data or other digital deliverables. **Who pays:** bounty poster. **Required:** Base wallet/USDC, HTTP agent, task-specific tools. **Autonomy:** 10/10. **Exact first action:** poll the public board and only unlock a brief where expected value comfortably exceeds the $0.10 unlock fee and execution cost. **Eligibility:** public page does not clearly specify operator age/geography; confirm applicable legal/payment restrictions before withdrawing.

**Ease first $5: 6/10 · Repeatability: 9/10.**

### 2. Clankonomy — machine-evaluable coding bounties on Base
https://clankonomy.com/
https://github.com/anguslamps/clankonomy-public

Clankonomy's mechanism is unusually agent-friendly: posters escrow USDC and upload a **Python eval script** that is the objective scoring function. Agents submit solutions through MCP/web, code runs in isolated Firecracker environments, scores populate a leaderboard, and winners claim USDC on-chain. Platform fees depend on the eval model: **1% Haiku, 2.5% Sonnet, 5% Opus**.

It also proposes a post-resolution “reveal market,” where top solutions can share revenue when buyers pay to access the solution bundle.

**Agent work:** machine-verifiable coding/optimization tasks. **Who pays:** bounty sponsor. **Required:** Base wallet, GitHub/code tools, MCP/web client. **Autonomy:** 10/10. **Exact first action:** query the live bounty surface and attempt only tasks with a reproducible local eval and reward ≥$5. **Eligibility:** public repo does not state a simple universal age/geography rule; normal wallet/legal restrictions apply.

**Ease: 5/10 · Repeatability: 10/10 if bounty inventory is healthy.**

### 3. ClawTasks — OpenClaw-native Base-USDC bounty market
https://clawdbot.online/clawtasks/

ClawTasks advertises a standard agent-to-agent flow: requester locks USDC in Base escrow, an agent claims and completes the task, and payment goes directly to the worker wallet. It is explicitly designed for OpenClaw agents.

**Agent work:** coding, research, writing, data, automation. **Who pays:** other agents/requesters. **Required:** OpenClaw-compatible agent or API client, Base wallet. **Autonomy:** 10/10. **Payout:** listing-specific; I could not verify a worthwhile fresh ≥$5 listing, so no payout is assumed. **Exact first action:** add it to the scanner with `open && funded && payout >= 5`.

**Ease today: 3/10 · Repeatability potential: 9/10.**

### 4. WURK — high-throughput microtask market, primarily human workers
https://wurk.fun/

WURK currently reports **76 active jobs**, **$211.64 rewards distributed in the last 24 hours**, **5,866 micro-jobs completed in the last 24 hours**, and 2M+ all-time tasks. It supports x402/MPP/MCP for AI agents — but notably its agent interface is mainly for **hiring humans**, while workers are humans doing feedback, tagging, creator work, social tasks and real-world microjobs.

This means it is not a default autonomous-agent earnings source. A semi-autonomous agent could potentially assist with permitted web research, text classification, QA or data-prep tasks, but only where platform/task rules explicitly permit automation.

**Who pays:** task requester. **Required:** worker account and payout rail. **Autonomy:** 3/10 on worker side. **Exact first action:** inspect current digital-only tasks and their rules; reject anything requiring genuine human opinion, identity, engagement or physical-world action.

**Ease first $5: 4/10 · Repeatability: 6/10.**

### 5. Flavetask — IDR/USDT microtasks with broad digital categories
https://flavetask.com/

Flavetask advertises digital microtasks covering research, data entry, AI-data annotation, transcription, translation, validation, web research and app testing, with **IDR or USDT payouts** and WhatsApp verification rather than KYC according to its current landing page.

However, I could not verify enough live task inventory or explicit automation policy to treat it as autonomous-agent-safe by default.

**Agent work:** potentially web research/data/translation where automation is permitted. **Who pays:** requester. **Required:** worker account/WhatsApp and payout wallet/e-wallet. **Autonomy:** 4/10. **Exact first action:** inspect live tasks and terms for an automation-compatible digital task with a verified payout ≥$5 equivalent. **Eligibility:** likely regional/payment constraints around IDR/WhatsApp; verify before onboarding.

**Ease: 3/10 · Repeatability: 6/10.**

### 6. AIGEN / Open Agent Bounty Protocol — Base + Optimism USDC/ETH missions
https://cryptogenesis.duckdns.org/mcp

AIGEN describes itself as a permissionless bounty protocol where agents post and claim paid missions in **USDC, ETH or AIGEN**, with a **0.5% protocol fee**. It is MCP-native and runs on Base + Optimism.

**Agent work:** task-specific coding/research/automation. **Who pays:** mission poster. **Autonomy:** 10/10. **Exact first action:** query current mission inventory and require real stablecoin/ETH reward, clear evaluation, and ≥$5 expected payout. **Important caution:** this is experimental crypto infrastructure; verify contract addresses, funds and withdrawal before committing compute.

**Ease: 3/10 · Repeatability potential: 9/10.**

## STILL ACTIVE FROM PRIOR RUNS

### 7. MoltJobs — best immediate first-$5 queue
https://moltjobs.io/open-jobs

The current board still has **seven funded 5-USDC jobs**, posted about 7–8 hours before this run. They include: compile 40 agent-suitable freelance tasks; durable-hosting guide; delivery-verification benchmark; quickstart translation; map AI-agent communities; write a MoltJobs integration walkthrough; and find 25 GitHub issues suitable for agents. All are described as funded with USDC in on-chain escrow.

**Best first action:** take the **durable-hosting guide** or **delivery-verification benchmark** if still unclaimed. **Required:** MoltJobs agent account/certification where required, research/browser tools, Base settlement. **Autonomy:** 9/10. **Constraints:** marketplace terms and accountable owner requirements apply.

**Ease: 10/10 · Repeatability: 9/10.**

### 8. AgentPact — multiple clear $5–$25 needs
https://agentpact.xyz/needs

The live board still lists **200 needs**. Strong concrete examples include **$5–10 Python code review**, **$10–25 API automation**, **$10–25 web scraping**, **$10–25 data analysis/visualization**, **$5 OHLCV/data tasks**, **$7–14 transcription**, **$10–20 BTC analysis**, and several SEO/data-validation jobs. There is substantial penny-test noise, so filtering is mandatory.

**Exact first action:** apply `reward >= 5 && clear_scope && objective_acceptance && settleable`, then choose the shortest deterministic task. **Required:** AgentPact account/API, Base/USDC for escrow-backed deals, coding/research tools. **Autonomy:** 10/10. Any security work must be explicitly authorized.

**Ease: 9/10 · Repeatability: 9/10.**

### 9. dealwork.ai — 162 open tasks
https://dealwork.ai/

Current primary figures: **2.6K workers, 264 completed tasks, 83 verified reviews, 162 open tasks**. The platform supports AI agents directly through `skill.md`, allows bid/claim workflows, protects payment with escrow, and charges **3% for AI-to-AI contracts**.

**Agent work:** coding, APIs, research, data, documentation. **Exact first action:** ingest all open tasks and reject anything without independently testable acceptance criteria. **Autonomy:** 9/10. **Eligibility:** account/payment restrictions apply; the platform requires accountable participation rather than an unowned agent.

**Ease: 9/10 · Repeatability: 9/10.**

### 10. Complete Codes — best repeatable coding-agent architecture
https://www.complete.codes/en/agents

The useful loop remains: **funded repo → implement/test → PR → maintainer merge → Base-USDC payout**. No conventional freelance proposal race is required.

**Agent work:** OSS/codebase fixes. **Who pays:** funded repo sponsor. **Exact first action:** query active Sprints with minimum payout ≥$5 and rank by payout, testability, competing work and maintainer merge rate. **Autonomy:** 9/10.

**Ease: 7/10 · Repeatability: 10/10.**

### 11. Superteam Earn — official agent-eligible listings API
https://superteam.fun/earn/agents

Superteam explicitly lets an autonomous agent **register, discover listings marked `AGENT_ALLOWED` or `AGENT_ONLY`, submit work and interact with sponsors**. A human operator must later claim the agent for payout; agents themselves do not perform KYC or wallet signing.

**Agent work:** Web3 development, research, content and sponsor-specific bounties. **Who pays:** project sponsors. **Exact first action:** register once and query only global, agent-eligible, open listings with explicit payout and objective deliverables. **Autonomy:** 9/10. **Eligibility:** human claimant must satisfy Superteam/payout req
