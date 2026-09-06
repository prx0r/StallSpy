# Agent Money Scout — 2026-09-01 15:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Tue, 1 Sep 2026 03:21:04 -0500
**Message ID:** 1a05c0eba1b4aeb4

---

# Agent Money Scout — 2026-09-01 15:00

## NEW THIS RUN

1. GH Bounty — https://www.ghbounty.com/
What the agent does: solves funded GitHub issues, submits PRs, and is evaluated by AI validators before automatic SOL payout.
Who pays: repository maintainer/sponsor via Solana-mainnet escrow.
Verified payout examples on the live page: 5 SOL for retry logic in solana-labs/web3.js; 29 SOL for async generators in vercel/next.js; 39 SOL for WebGPU texture compression in denoland/deno; other rows show 14 SOL and 9.8 SOL under review and 3.5 SOL paid.
Requirements: GitHub OAuth once, Solana wallet, coding agent, tests. MCP and SDK available.
Autonomy: 10/10 after one-time GitHub authorization.
First action: connect MCP at https://mcp.ghbounty.com/api/mcp/sse, list open bounties, clone the easiest locally reproducible repo, and attempt only issues with explicit acceptance criteria.
Constraints: 2.5% protocol fee; payout is SOL, so value fluctuates; normal GitHub repo contribution rules apply.
Ease first $5: 9/10. Repeatability: 10/10.

2. Atrest.ai — https://atrest.ai/
What the agent does: autonomously accepts agent-to-agent work such as code review, research, bug fixes, API integration, testing, data analysis and scraping.
Who pays: other agents; USDC is escrowed before work starts and an AI judge verifies delivery.
Platform-reported economics: 1,200+ tasks completed, $48K+ USDC transacted, 105+ active agents. Advertised current category ranges include code review $5–25, data analysis $10–50, research $8–40, bug fixing $10–35, API integration $15–60, unit testing $5–20 and competitive analysis $12–45.
Requirements: agent registration, capabilities, task guardrails, USDC-compatible wallet/API integration.
Autonomy: 10/10.
First action: register on the free tier, whitelist only objective task categories and auto-accept only jobs >=$5 with bounded runtime.
Constraints: first-party metrics; verify an independent withdrawal before trusting aggregate volume.
Ease: 8/10. Repeatability: 10/10 if reported activity is genuine.

3. TaskForce — https://www.task-force.app/
What the agent does: browses work through the API, bids, completes milestones and receives USDC directly to its wallet.
Who pays: human or agent clients through milestone escrow.
Verified architecture: 0% platform fee, Base/Solana USDC, API-first worker lifecycle, AI-jury dispute handling.
Payout examples shown on the product page ($300 landing page, $500 trading bot, $200 ETL) are product examples, not verified live listings, so do not treat those amounts as available inventory.
Requirements: API registration, wallet, task-specific skills.
Autonomy: 10/10.
First action: register through the agent API and inspect Browse Tasks; execute only a real funded >=$5 listing.
Constraints: buyer must approve milestones; verify chain/network and escrow before execution.
Ease: 5/10. Repeatability: 9/10.

4. AgentBazaar — https://www.agentbazaar.dev/
What the agent does: lists a service, quotes dynamically, executes work and gets paid in USDC on Solana. Supports REST, A2A, MCP, SDK, dashboard and Telegram.
Who pays: humans or other agents.
Pricing/economics: seller keeps 97%, platform 3%. Example micro-services shown are code audit $0.05, doc writing $0.03, test generation $0.04; these are examples rather than strong income opportunities.
Requirements: Solana wallet, hosted endpoint or agent adapter.
Autonomy: 10/10.
First action: cross-list a capability already proven on a bounty market; do not create an AgentBazaar-only product.
Constraints: current visible example economics are tiny; require >=$5 cumulative expected value or recurring demand.
Ease: 3/10. Repeatability: 9/10.

5. AgentsMarketplace / X Layer — https://agentsmarketplace.app/
What the agent does: exposes a priced API/service endpoint, gets paid via x402 in USDC/USDT/USDG, and builds on-chain reputation.
Who pays: users and agents calling the endpoint.
Payout: seller-defined; no reliable seller revenue figure verified this run.
Requirements: endpoint URL, X Layer-compatible wallet/payment integration.
Autonomy: 10/10.
First action: list a proven narrow endpoint and verify one independent external payment before spending further engineering effort.
Constraints: generic marketplace supply is not proof of demand.
Ease: 2/10. Repeatability: 9/10 if buyers emerge.

6. AgentSwarmWork — https://www.agentswarmwork.com/
What the agent does: advertises capabilities through skill.md, receives matching tasks by webhook, completes work and withdraws escrowed payments.
Who pays: marketplace task posters.
Payout: task-specific; no trustworthy live payout amount surfaced this run.
Requirements: skill.md + webhook/WebSocket integration.
Autonomy: 10/10.
First action: register one narrow capability and wait for a funded task >=$5 before allocating compute.
Constraints: verify payment provider, escrow and actual buyer activity.
Ease: 3/10. Repeatability: 8/10.

7. ClawFreelance — https://www.clawfreelance.com/en
What the agent does: claims open-source issues, paid bounties and project work, delivers results and receives crypto payment.
Who pays: task/bounty poster.
Platform-reported metrics: 2,847 active agents, $1.2M total earned, 12,453 tasks completed, 847 open bounties. These are first-party claims and should be chain-verified before relying on them.
Requirements: agent registration, wallet, coding/research tooling.
Autonomy: 10/10.
First action: inspect the actual task feed and verify a real funded >=$5 bounty before integrating deeply.
Constraints: metrics may be promotional; verify escrow and independent payout.
Ease: 5/10. Repeatability: 9/10 if inventory validates.

## STILL ACTIVE FROM PRIOR RUNS

8. MoltJobs — https://moltjobs.io/open-jobs
Best use: escrow-funded research/coding tasks with API, CLI, MCP and webhooks.
Who pays: job poster via Base-USDC escrow.
Previous run showed multiple $5 jobs; poll the board live rather than assuming that batch remains available.
First action: take the newest >=$5 objectively verifiable task.
Autonomy: 9/10. Ease: 9/10. Repeatability: 9/10.

9. dealwork.ai — https://dealwork.ai/
Current repeatedly verified state: roughly 162 open tasks, 2.6K workers, 264 completed tasks and 83 verified reviews; platform has documented an $80 AI-delivered API and a $5 autonomous AI-to-AI contract.
Who pays: task poster; escrow before work.
First action: ingest the whole queue and rank by payout × acceptance probability / runtime.
Autonomy: 9/10. Ease: 9/10. Repeatability: 9/10.

10. AgentPact — https://agentpact.xyz/needs
Current indexed state: around 206 open Needs, 153 active Offers, 19 live Deals and 638 agents, with optional Base-USDC escrow.
Typical previously observed useful needs include Python review, API automation, scraping and data analysis in the $5–25 range, alongside lots of penny noise.
First action: enforce reward >=$5 AND objective acceptance AND clear scope.
Autonomy: 10/10. Ease: 8/10. Repeatability: 9/10.

11. Complete Codes — https://www.complete.codes/en/agents
What the agent does: finds a funded GitHub Sprint, implements/tests, submits PR and gets Base-USDC after maintainer merge.
First action: query active Sprints with minimum payout >=$5 and rank by payout × P(merge) / expected implementation time.
Autonomy: 9/10. Ease: 7/10. Repeatability: 10/10.

12. Superteam Earn for Agents — https://superteam.fun/earn/agents
What the agent does: registers via API, queries AGENT_ALLOWED / AGENT_ONLY work, submits artifacts and talks with sponsors.
Who pays: Web3/Solana sponsors. A human operator handles final payout claim.
First action: query only global listings with explicit reward, future deadline and concrete deliverable.
Autonomy: 9/10. Ease: 5/10. Repeatability: 9/10.

13. GetAgentic — https://getagentic.io/
What the agent does: provides paid agent services with x402 under $100 and escrow for larger jobs.
Current site claims 45,291 transactions today and shows example $25/$120/$350 transactions, but these are first-party claims.
First action: independently verify real external buyers and chain settlement before investing in seller infrastructure.
Autonomy: 10/10. Ease: 4/10. Repeatability: 9/10 if verified.

14. Clawlancer — https://www.clawlancer.ai/
What the agent does: registers via MCP, gets Base wallet/on-chain identity, browses and claims bounties.
Who pays: bounty posters in USDC.
Current issue: visible economics have repeatedly skewed to penny tasks.
First action: scanner only until bounty >=$5.
Autonomy: 10/10. Ease: 1/10 today. Repeatability: 8/10 if budgets rise.

## REDDIT DEMAND SIGNALS

15. Full business solutions beat generic workflow sales.
Thread: https://www.reddit.com/r/n8n/comments/1p1iazj/ive_been_in_the_aiautomation_space_since_2022/
Recurring pattern: buyers do not want isolated workflows; they want either a polished interface or an invisible, integrated solution that reliably owns a business process.
Offer: pick one painful operational flow and package the UI, integrations, monitoring and exception handling together.
Customer acquisition: niche communities, referrals, agencies and operators with explicit buying intent; avoid bulk cold spam.
Charge: fixed implementation + recurring reliability/maintenance fee.
Ease: 7/10. Repeatability: 10/10.

16. Data manipulation / operational integration is higher-value than calendar/chatbot demos.
Thread: https://www.reddit.com/r/n8n/comments/1nkr9mv/is_n8n_the_ultimate_side_hustle_or_just_a_tool/
Pattern: practitioners with real business clients describe large data-processing/database integrations as the valuable work, while simple appointment/chatbot automations are commoditized.
MVP: one cross-system reconciliation flow with canonical state, validation, retry logic and audit logs.
Ease: 7/10. Repeatability: 10/10.

17. Invoice/AP automation remains persistent demand.
Thread: https://www.reddit.com/r/automation/comments/1oup6v1/cant_keep_up_with_my_invoice_processing_is_there/
Pattern: email invoices -> extraction -> v
