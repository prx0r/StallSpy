# Agent Money Scout — 2026-09-02 01:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Tue, 1 Sep 2026 14:26:35 -0400
**Message ID:** 1a05e391bbc7a7ea

---

Agent Money Scout — 2026-09-02 01:00

NEW THIS RUN

1. AgentLux — platform-funded first-hire guarantee
URL: https://agentlux.ai/first-hire
What the agent does: Register a portable ERC-8004 identity, publish one concrete service with explicit inputs/outputs/evaluation fields, accept a platform-funded escrowed hire, deliver, and earn a USDC settlement plus an honest payment-backed rating.
Who pays: AgentLux itself for the first qualifying external-agent hire; subsequent work is paid by marketplace requesters.
Payout: Your listed service price, subject to AgentLux funding caps. The site explicitly says the offer is live but that no First-Hire has yet been fulfilled.
Required: Base wallet, MCP/REST-capable agent, quality service listing, deterministic evaluation criteria.
Autonomy: 10/10 after registration.
First action: Read https://agentlux.ai/llms.txt, register, and publish one quality $5-$10 service such as API QA, CSV validation, source-backed research, or agent configuration audit.
Constraints: One guarantee per external agent; low-quality/sybil/placeholder listings do not qualify; guarantee may queue if daily/monthly caps are reached.
Ease first $5: 9/10. Repeatability: 7/10 until organic buyers are proven.

2. WorkProtocol — real Base-USDC settlement history, $50 minimum jobs
URL: https://workprotocol.ai/hn
What the agent does: Claim structured coding work, deliver PRs/code/artifacts, pass automated or human verification, receive Base-USDC.
Who pays: Job posters who fund escrow before execution.
Verified current primary metrics: 737 agents, 35 jobs posted, 13 completed, 1,400 USDC settled. Minimum job budget is $50 USDC. Every settlement is said to link to a Basescan transaction.
Required: Base wallet, REST/A2A/MCP integration, coding/testing skills.
Autonomy: 10/10.
First action: Register immediately and poll the job API. Do not spend compute right now because the site currently reports 0 jobs available.
Constraints: 5% platform fee; first 20 agents receive 0% for 90 days according to the primary page. Code work is currently the intended focus.
Ease first $5 today: 2/10 because inventory is empty. Repeatability when jobs appear: 10/10.

3. Molted — Base-mainnet peer-to-peer agent work
URL: https://molted.work/
What the agent does: Search jobs, bid, communicate with the poster, deliver proof, and get paid directly wallet-to-wallet.
Who pays: Hiring agent/human through x402 USDC on Base.
Payout: Job-specific; no worthwhile live amount was verified this run.
Required: @molted/cli or REST API; Base wallet. CLI can create the wallet and register the agent.
Autonomy: 10/10.
First action: npm install -g @molted/cli; molted init; molted jobs list --status open; reject jobs below $5.
Constraints: Unlike escrow-first markets, Molted describes direct peer-to-peer settlement when the poster approves; therefore poster/payment reliability matters more.
Ease: 4/10. Repeatability: 9/10 if inventory develops.

4. Riner — five visible tasks, Base-mainnet USDC, but current economics poor
URL: https://riner.io/tasks
What the agent does: Apply to tasks through the API and deliver a result for poster approval.
Who pays: Task poster, with funds locked in a smart contract.
Current inventory: 5 tasks visible. Open jobs currently include $1 and $2 promotional/community-engagement tasks; prior $3 jobs are expired. These are below the desired first-$5 threshold and some require promotional posting, so I would not execute them.
Required: Agent API/SDK, Base wallet.
Autonomy: 10/10.
First action: Integrate discovery only and enforce reward >= $5 plus a no-spam/no-fake-experience filter.
Constraints: Do not execute jobs asking for fabricated experience, coordinated fake engagement, or spam. Current open inventory is not economically attractive.
Ease today: 1/10. Repeatability potential: 8/10.

5. Wenrwa Agent Marketplace / HiveOp — Solana coding and build bounties
URL: https://www.wenrwa.com/
What the agent does: Bid on USDC-funded build tasks, collaborate in workspaces, or solve GitHub bounties through HiveOp and ship PRs.
Who pays: Task/bounty poster.
Payout: Explicitly USDC-reward based, but no worthwhile current bounty amount was verified in this run.
Required: MCP/REST/SDK integration, Solana wallet, coding/build tooling.
Autonomy: 9/10.
First action: Query marketplace.wenrwa.com and HiveOp for currently funded >=$5 tasks before integrating deeply.
Constraints: Verify each task’s escrow/funding and do not mix earning work with the platform’s unrelated trading features.
Ease: 4/10. Repeatability: 9/10 if live liquidity exists.

6. ClawHire — large first-party claims, insufficient live-job verification
URL: https://clawhire.lol/
What the agent does: Browse jobs, submit proposals, execute milestones and receive ATXP/Base payments.
Who pays: Hiring agents/humans.
Advertised metrics: 1,234 active agents, 5,678 jobs completed, $890K total paid out. These are first-party headline claims and I could not verify specific currently funded jobs from the public jobs page in this run.
Required: ATXP wallet, USDC + ETH on Base, claw.direct agent identity.
Autonomy: 10/10.
First action: Register only after resolving an actual funded listing to a concrete escrow/payment record.
Constraints: Treat aggregate marketing numbers as unverified until independent transactions are visible.
Ease: 3/10. Repeatability: 8/10 if claims validate.

7. Riner-style task-scanner compliance filter — immediate tooling play
Customer/problem: Agent operators need discovery systems that distinguish legal/useful tasks from promotion spam, fake engagement, testnet jobs, penny work and fabricated marketplace activity.
Evidence: This run found live Riner tasks paying $1-$2 for promotional/community activity, while other markets routinely show zero inventory or unverified headline statistics.
Agent workflow: ingest marketplace -> classify funding/mainnet -> policy/ToS check -> payout -> acceptance -> competition -> estimated cost -> RUN/ABSTAIN.
Where to acquire customers: agent builders operating multi-market workers; GitHub/OpenClaw/x402 communities.
How to charge: $5-$20/month API or $0.01-$0.05 per opportunity scored.
MVP: one endpoint returning funding_state, payout_asset, mainnet, ToS_risk, objective_acceptance, competition, payout_history, EV_score.
Ease: 8/10. Repeatability: 10/10.

STILL ACTIVE FROM PRIOR RUNS

8. DataBazaar
URL: https://databazaar.io/bounties
Current primary state: 249 active listings and 6 open bounties. Agents can browse bounties without auth and sell through MCP/REST. Stripe holds payment; seller fee is 3% for ordinary marketplace sales.
Best task: structured data acquisition/normalization/deduplication/provenance. Prior checks showed bounties from $100-$500, with the retailer-pricing bounty particularly attractive.
First action: GET https://api.databazaar.io/bounties and rank by payout / submissions / licensing clarity / data-acquisition effort.
Autonomy: 9/10. Ease: 8/10. Repeatability: 10/10.

9. GH Bounty
URL: https://www.ghbounty.com/
Current primary feed still shows: 5 SOL open for solana-labs/web3.js retry logic; 29 SOL open for async generators in vercel/next.js; 14 SOL under review for LangChain memory leak; 3.5 SOL paid for Tauri dark-mode detection.
Agent workflow: reproduce issue -> code -> tests -> PR -> AI pre-screen -> five-validator consensus -> automatic SOL release.
Who pays: Maintainer/sponsor via Solana-mainnet escrow.
Fee: 2.5%.
First action: reproduce the 5-SOL issue locally and estimate hours + acceptance probability before coding.
Autonomy: 10/10. Ease when matched: 9/10. Repeatability: 10/10.

10. MoltJobs
URL: https://moltjobs.io/open-jobs
Current indexed job: 5 USDC for turning three live external job listings into ready-to-fund MoltJobs specs and contacting buyers. Base-USDC escrow is funded before execution.
Agent workflow: API/MCP/CLI discovery -> bid -> deliver structured evidence -> review -> USDC.
Fee: 5%.
First action: poll for >=5 USDC pure research/code/data/verification work and avoid promotion-heavy tasks.
Autonomy: 9/10. Ease: 8/10. Repeatability: 9/10.

11. AgentGigs
URL: https://www.agentgigs.io/
Recent primary checks showed a $300-$750 competitor-landscape research job with only three applicants and a completed $465 payment to an agent after proofers evaluated the delivery.
Agent workflow: browse -> apply -> deliver -> independent proofers -> Stripe payout.
Required: one-time email verification + Stripe Connect/KYC.
First action: query the available-jobs API and prioritize research/data/testing tasks with objective deliverables.
Autonomy: 9/10. Ease: 9/10. Repeatability: 9/10.

12. Complete Codes
URL: https://www.complete.codes/en/agents
Agent workflow: funded GitHub sprint -> eligible issue/proactive improvement -> PR -> maintainer merge -> Base-USDC.
Key advantage: no conventional bidding contest; merge is the economic trigger.
First action: query https://api.complete.codes/v1/sprints?status=active&min_payout=5&sort=payout and rank next_payout * P(merge) / expected_hours.
Autonomy: 10/10. Ease: 8/10. Repeatability: 10/10.

13. dealwork.ai
URL: https://dealwork.ai/
Prior live checks repeatedly showed roughly 162 open tasks, 2.6K workers and 264 completed jobs, including documented $80 AI-delivered API work and a $5 autonomous AI-to-AI contract.
First action: ingest all live jobs and rank by funded status, competition, acceptance mechanism and actual execution cost.
Autonomy: 9/10. Ease: 9/10. Repeatability: 9/10.

14. gigs.sh
URL: https://gigs.sh/
Use only as candidate discovery. It is not evidence that a marketplace still exists, has real jobs, uses mainnet money or pays workers. Every candidate must be primary-source revalidated.
Direct earning: 1/10. Discovery repeatability: 10/10.

REDDIT DEMAND SIGNALS

15. Pre-response context scavenger for ops teams
Thread: https://www.reddit.com/r/automation/comments/1ratb89/what_repetitive_business_task_still_feels_way/
Signal: An ops commenter describes simple
