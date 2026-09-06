# Agent Money Scout — 2026-09-01 12:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Mon, 31 Aug 2026 22:23:19 -0700
**Message ID:** 1a05b6bff6e43e8d

---

# Agent Money Scout — 2026-09-01 12:00

Current execution order: **MoltJobs → dealwork.ai → AgentGigs → AgentPact → Complete Codes → selective Superteam/Huntr work → productize proven capabilities.**

The strongest new discovery this run is **AgentGigs**: it exposes the entire worker lifecycle through REST, Stripe Connect escrow, work-proofing agents, webhooks/SSE, and a free tier where the worker keeps 90%. A current indexed listing has a **$5–$10 budget** and requires independent proofer verification. The other useful new signal is **Agoragentic**, which has 756 registered agents and 801 invocations but explicitly warns that paid settlement depends on its Interchange operating state — useful evidence that agent-marketplace registration counts still need payment-path verification.

## NEW THIS RUN

### 1. AgentGigs — full API-first autonomous freelance marketplace
URL: https://www.agentgigs.io/

What the agent does: registers a specialization, discovers matching jobs, applies with a price/timeline, uploads deliverables, handles revisions, and receives payment after approval. Every action has a REST endpoint; webhooks/SSE avoid polling.

Who pays: marketplace clients. Payout/pricing: current indexed job budget **$5–$10**; platform commission is **10% Free / 7% Pro / 5% Enterprise**, so Free agents keep 90%. Stripe pays out after client approval, normally to bank in 2–3 business days.

Required: one-time email verification, Stripe Connect bank/KYC setup, API key, task-specific LLM/code/data tools. Autonomy: **9/10** after the two human setup steps.

Exact first action: create a free agent, connect Stripe, then call `/api/agent/jobs/available` and filter `min_budget >= 500` cents with high match score and objective acceptance criteria.

Constraints: Stripe Connect/KYC and supported-country banking apply; private job materials must be treated as confidential; no spam applications.

Ease first $5: **7/10**. Repeatability: **9/10**.

### 2. Agoragentic — 97% seller share for paid agent invocations
URL: https://agoragentic.com/earn.html

What the agent does: exposes a callable capability/API, sets a per-invocation USDC price, and receives 97% of successfully settled paid calls on Base.

Who pays: other agents invoking the service. Verified platform state: **756 registered agents, 68 public services, 801 invocations**. Seller bond: **$1 refundable**.

Important caveat: the primary page itself says to check the Interchange operating state before relying on paid settlement. Therefore 801 invocations are not automatically 801 paid external purchases.

Required: hosted endpoint, Base-compatible wallet, $1 bond, agent framework/API integration. Autonomy: **10/10**.

Exact first action: list only a capability that has already earned elsewhere; verify one real external paid settlement before investing in distribution.

Ease first $5: **3/10**. Repeatability: **9/10 if paid demand develops**.

### 3. Clustly — Solana-USDC escrow marketplace with hashed acceptance criteria
URL: https://clustly.ai/
Docs: https://clustly.ai/docs

What the agent does: publishes a service, receives directed hires, verifies that buyer-confirmed acceptance criteria match the on-chain hash, executes in isolation, submits evidence, and receives USDC when the buyer signs release.

Who pays: human/agent buyers. Payment: **Solana mainnet USDC escrow**; current site examples show a **4% fee**, but the displayed $240/$250 run is illustrative rather than verified current revenue.

Required: operator account/managed agent, Solana settlement, MCP/API integration. Autonomy: **9/10**; human buyer signature releases funds.

Exact first action: list an existing narrow service and wait for a funded directed hire; do not count illustrative examples as market liquidity.

Ease first $5: **4/10**. Repeatability: **9/10 if buyers appear**.

### 4. Huntr — live $15,000 AI-agent security challenge
URL: https://huntr.com/

Huntr currently shows an active **$15,000 challenge, “Inside Job — Three Agents, Three Secrets,” with 13 days remaining**. This is a bounded AI-security competition rather than ordinary freelance work.

What the agent does: within the challenge’s explicit authorized environment, identify weaknesses in AI-agent secret/tool protection and produce valid challenge findings.

Who pays: Huntr/Palo Alto Networks challenge sponsor. Advertised pot: **$15,000**.

Required: security/prompt-injection expertise, reproducible testing, strict adherence to the provided target and challenge scope. Autonomy: **6/10** because human validation of findings is prudent.

Exact first action: open the active challenge, read the complete scope/rules, and test only those provided targets.

Constraints: authorized challenge targets only; never extrapolate techniques to systems without permission. Huntr’s old OSS bounty program was sunset June 30, 2026, so focus on the new challenge format.

Ease first $5: **3/10**. Repeatability: **5/10**.

### 5. Immunefi — newly refreshed Cosmos and Intuition bounties
URL: https://immunefi.com/
Cosmos: https://immunefi.com/bug-bounty/cosmos/information/
Intuition: https://immunefi.com/bug-bounty/intuition/information/

Concrete current programs refreshed **August 27, 2026** include Cosmos, with **$50,000 max / $12,500 high / $2,500 medium / $1,000 low**, and Intuition, with **up to $100,000 critical** and minimum critical payout $5,000.

What the agent does: authorized source-code/smart-contract analysis, test generation, invariant reasoning and PoC assistance, with a human validating the report before submission.

Who pays: protocol bounty programs through Immunefi. Required: advanced Solidity/Go/Rust/security skills; KYC is required on both cited programs; PoCs required.

Exact first action: select one in-scope repository, clone it, run static/dynamic analysis and invariant testing only against the listed assets.

Autonomy: **6/10**. Ease first $5: **2/10**. Repeatability: **7/10** for a capable security agent.

## STILL ACTIVE FROM PRIOR RUNS

### 6. MoltJobs — seven fresh escrow-funded 5-USDC jobs
URL: https://moltjobs.io/open-jobs

The live board currently shows seven tasks, all **5 USDC** and explicitly funded in on-chain escrow: compile 40 agent-suitable tasks; durable-hosting guide; delivery-verification benchmark; quickstart translation; AI-agent community map; technical MoltJobs walkthrough; and 25 GitHub issues an agent could solve cheaply. Six end in about 3 days; the GitHub-issues job ends in about 1 day.

Required: MoltJobs agent/API setup, relevant research/browser/code tools, certifications where the job requires them. Base-USDC settlement; 5% success fee.

Exact first action: prioritize **delivery-verification benchmark** or **durable-hosting guide** because they are cheap to execute and create reusable worker knowledge.

Autonomy: **9/10**. Ease first $5: **10/10**. Repeatability: **9/10**.

### 7. dealwork.ai — 162 open tasks
URL: https://dealwork.ai/

Current primary state: **2.6K workers, 162 open tasks, 264 completed, 83 verified reviews**, with typical delivery around 1.1 days. Humans and agents can hire either side, and escrow protects payment.

Who pays: task posters. Previously documented examples include an $80 production API and a $5 autonomous AI-to-AI contract; do not assume those exact jobs remain open.

Exact first action: ingest all open jobs and rank only those with clear acceptance tests, low competition and payout comfortably above runtime cost.

Autonomy: **9/10**. Ease: **9/10**. Repeatability: **9/10**.

### 8. AgentPact — 206 open Needs / 153 active Offers
URL: https://agentpact.xyz/

Agents register with one API call, post offers/needs, create milestone deals, deliver and settle USDC-backed deals on Base. Current indexed marketplace state remains **206 open Needs, 153 active Offers, 19 live Deals, 638 agents**.

Exact first action: publish one narrow service (`API QA`, `CSV/JSON validation`, `test generation`, or `source-backed research`) while scanning needs with `reward >= $5` and objective acceptance.

Autonomy: **10/10**. Ease first $5: **8/10**. Repeatability: **9/10**.

### 9. Complete Codes — merge-to-USDC coding loop
URL: https://www.complete.codes/en/agents

What the agent does: discover a funded GitHub Sprint, implement/tests, submit PR, receive Base-USDC when the maintainer merges.

Exact first action: query active Sprints with `min_payout=5` and rank by `payout × P(merge) / expected implementation time`, including CI quality and competing PRs.

Autonomy: **9/10**. Ease: **7/10**. Repeatability: **10/10**.

### 10. Superteam Earn for Agents — official agent-only API
URL: https://superteam.fun/earn/agents

Agents can register, query `AGENT_ALLOWED` and hidden `AGENT_ONLY` opportunities, submit artifacts and communicate with sponsors programmatically. A human operator must claim the winning agent for payout.

Exact first action: register once, call the live listing endpoint, and filter for global + explicit cash/stablecoin reward + future deadline + machine-verifiable deliverable.

Autonomy: **9/10**. Ease: **5/10**. Repeatability: **9/10**.

### 11. MoltyBounty — completed-task evidence, up to 50 USDC postings
URL: https://www.moltybounty.com/

AI agents claim through the API; paid bounties can be set up to **50 USDC**. The public leaderboard shows agents with 1–12 completed tasks, which is useful activity evidence even though aggregate paid revenue is not published.

Exact first action: poll paid AI-agent bounties and require `payout >= $5` + explicit acceptance criteria.

Autonomy: **10/10**. Ease: **5/10**. Repeatability: **8/10**.

### 12. GetAgentic — claimed high activity, still verify chain-side
URL: https://getagentic.io/

The primary page claims **45,291 transactions today**, zero platform fee for sub-$100 x402 jobs and 2% escrow on larger jobs, with displayed examples of $25/$120/$350 transactions. These remain first-party claims and should not be treated as independently proven buye
