# AISec Money Radar — Top 20 — 4 Sep 2026

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Fri, 4 Sep 2026 04:44:26 -0700
**Message ID:** 1a06c3bfc800b1aa

---

# AISec Money Radar — 4 September 2026

## Executive summary

This run materially changes the short-term order. The best new immediate target is **Adobe on Intigriti**: the program only moved to Intigriti on September 1, includes AI-enabled Adobe products, pays up to **$15,000**, and the public page showed 154 submissions but only 1 accepted when checked. **0DIN**, **OpenAI Safety**, **Anthropic Model Safety**, **BitSec SN60**, **RedTeam SN61**, **Ridges SN62**, and **Gittensor SN74** remain the strongest lab-aligned opportunities.

On web3, I would not chase maximum headline bounty alone. **Intuition** is newly launched (July 8, updated Aug 27), up to **$100k**, and its decentralized knowledge-graph architecture is much more tractable/relevant than mature mega-programs. **Autonolas/Olas** only pays up to $5k but is unusually aligned with autonomous-agent infrastructure, making it high training value.

The strongest monetization thesis from this run is: **sell the by-product of the lab**. Intigriti is now explicitly turning researcher recon activity into a commercial intelligence product via CrowdRecon. That validates `/mw` exposing attack-surface changes, agent-security findings, program deltas and reproducible attack intelligence as paid API/x402 data even when no bounty is won.

---

## Top 20 ranked by expected value per scarce human hour

### 1. NEW — Adobe Public Bug Bounty on Intigriti
Source: https://app.intigriti.com/programs/adobe/adobepublic/detail
Status: Live since Sep 1, 2026. ColdFusion submissions temporarily paused Sep 3; other products remain available.
Payout: Tier 1 up to $15,000; Tier 2 up to $10,000; Tier 3 up to $5,000.
Why now: Fresh platform migration means new researcher population + scope reset. Scope explicitly includes AI-enabled features such as Firefly plus major web/product surfaces. Public page showed 154 submissions / 1 accepted when checked.
Human effort (estimate): 1–3h to choose one narrow asset/test plan + review report.
Agent effort (estimate): 6–24h focused recon/analysis.
Upfront cost: $0 plus compute.
Probability of payout: Medium-low per finding; better than mature giant pools because scope is fresh.
Legal: Exact Intigriti scope; use @intigriti.me; include testing IP; automated testing/rules vary by asset. ColdFusion currently paused.
Training value: Very high: modern enterprise apps + AI-enabled Adobe products.
Next action: Register Intigriti, snapshot Adobe scope, select one Tier-1/2 asset and run one deep worker session rather than broad scanning.

### 2. STILL-HIGH-VALUE — 0DIN GenAI Bug Bounty
Source: https://www.0din.ai/policy
Payout: $500–$15,000. Low up to $500, Medium $2,500, High $5,000, Severe $15,000.
Status: Ongoing.
Required work: Novel, non-public vulnerabilities affecting latest model generation; model/app security research.
Human effort: 1–2h scope/report review.
Agent effort: 4–20h per focused experiment family.
Upfront cost: Mostly compute/accounts.
Probability: Medium-low, but direct AI-security fit raises our relative edge.
Legal: Follow 0DIN model/security-boundary rules; no unrelated third-party testing.
Training value: Extremely high.
Next action: Make 0DIN the first external benchmark for the AISec attack corpus.

### 3. STILL-HIGH-VALUE — OpenAI Safety Bug Bounty
Source: https://openai.com/index/safety-bug-bounty/
Payout: Program-specific rewards; verify current Bugcrowd brief before testing.
Status: Ongoing public program.
Required work: Reproducible agent hijacking, third-party prompt injection, data exfiltration, MCP risk, or materially harmful agent behavior. OpenAI explicitly requires third-party prompt injection/data-exfiltration behavior to reproduce at least 50% of the time.
Human effort: 1–3h experiment design/review.
Agent effort: 6–30h repeated controlled trials.
Upfront cost: Compute/product access.
Probability: Low-medium for a genuinely novel chain.
Legal: Any MCP/third-party testing must comply with third-party terms; use controlled/canary data.
Training value: Maximum for client agent-red-team capability.
Next action: Build a reusable indirect-injection → tool-action test harness and point only at allowed OpenAI surfaces.

### 4. STILL-HIGH-VALUE — Anthropic Model Safety Bug Bounty
Source: https://support.anthropic.com/en/articles/12119250-model-safety-bug-bounty-program
Payout: Up to $35,000 per novel universal jailbreak.
Status: Rolling applications; accepted researchers receive HackerOne invite.
Required work: Universal jailbreaks against Anthropic Constitutional Classifiers that elicit substantial harmful information.
Human effort: 1–2h application + review per candidate.
Agent effort: 10–40h search/evaluation per attack family.
Upfront cost: Low; accepted program controls access.
Probability: Low, but payout/AI-training value excellent.
Legal: Stay inside provided bounty environment/scope.
Training value: Very high for adversarial search, lower for tool-agent security.
Next action: Apply now and build automated mutation/evaluation pipeline while waiting for access.

### 5. STILL-HIGH-VALUE — BitSec SN60 mining
Source: https://github.com/Bitsec-AI/subnet
Status: Active Bittensor subnet.
Payout: Dynamic TAO emissions; no fixed bounty value.
Required work: Build models/workflows that find and fix code vulnerabilities. BitSec explicitly lists future Scanner and Hunter applications.
Human effort: 2–5h initial benchmark/setup, then low if automated.
Agent effort: Continuous.
Upfront cost: Dynamic subnet registration + compute; verify live cost before joining.
Probability: Medium only if our local worker benchmarks competitively.
Legal: Evaluation environment/subnet rules; not permission for external exploitation.
Training value: Maximum — direct feedback loop for our security worker.
Next action: Reproduce validator tasks locally and join only if we can rank competitively.

### 6. STILL-HIGH-VALUE — RedTeam SN61
Sources: https://bittensor.es/subnets/061/ ; https://subnetradar.com/subnet-news/61/2026-05-31
Status: Active; recent Sep 1–3 subnet updates show active scoring/registration work.
Payout: Dynamic TAO emissions.
Required work: Miners compete to bypass bot-detection/anti-automation defenses; successful adversarial techniques improve defenders.
Human effort: 2–4h setup/strategy.
Agent effort: Continuous adversarial experimentation.
Upfront cost: Dynamic registration + compute.
Probability: Medium if we can reproduce challenge scoring locally.
Legal: Only official challenge environment/rules; do not generalize to unauthorized production bypassing.
Training value: High adversarial-agent training.
Next action: Pull current challenge/scoring docs and run a 24h local competitiveness test before registering.

### 7. STILL-HIGH-VALUE — Ridges SN62
Source: https://www.kucoin.com/news/insight/TAO/69aa8494ef60ba0007bb72a8
Status: Active coding-agent subnet; Ridgeline product is live/open beta.
Payout: Dynamic TAO emissions.
Required work: Coding agent evaluated on correctness, speed and cost; directly transferable to security patch generation.
Human effort: 2–4h setup and benchmark.
Agent effort: Continuous.
Upfront cost: Dynamic registration/compute.
Probability: Medium if our Hermes/worker stack is competitive.
Training value: Very high for exploit→patch→test workflows.
Next action: Benchmark our existing coding worker on the subnet task format before spending TAO.

### 8. STILL-HIGH-VALUE — Gittensor SN74
Source: https://docs.gittensor.io/miner.html
Status: Active OSS contribution mining.
Payout: Dynamic subnet emissions based on eligible merged GitHub contributions.
Required work: High-quality PRs to recognized repos; validator scores useful accepted contribution rather than synthetic benchmark only.
Human effort: 1–3h per initial PR review, falling as worker proves quality.
Agent effort: 3–20h per contribution.
Upfront cost: Dynamic subnet registration + GitHub identity setup.
Probability: Medium because merged PR is an objective path to reward.
Legal: Normal project contribution rules; no spam. First PAT broadcast pins GitHub identity to hotkey.
Training value: Extremely high for employable worker development.
Next action: Inspect recognized repos, choose one small high-confidence issue, get first merged worker-assisted PR before scaling.

### 9. NEW — Intuition on Immunefi
Source: https://immunefi.com/bug-bounty/intuition/information/
Status: Live since Jul 8, 2026; updated Aug 27.
Payout: Up to $100,000; Critical $5k–$100k, High $2.5k–$5k, Medium $1k–$2.5k.
Required work: Smart-contract review of decentralized token-curated knowledge graph / vault architecture.
Human effort: 2–5h architecture orientation + report review.
Agent effort: 12–40h deep contract analysis.
Upfront cost: Compute; KYC required.
Probability: Low-medium, but fresher program than most mega-bounties.
Legal: PoC required; exact Immunefi scope; default to local forks.
Training value: High, especially graphs/onchain logic relevant to our interests.
Next action: Import scope/repo into lab and run historical-audit-informed invariant generation.

### 10. CHANGED — Cantina Uniswap live bounty
Source: https://cantina.xyz/opportunities
Status: Live.
Payout: Advertised $15.5M maximum/pool on Cantina opportunity index; deposit required.
Required work: Uniswap security research under exact live bounty rules.
Human effort: High (4–10h orientation/review).
Agent effort: 20–100h+.
Upfront cost: Deposit + compute.
Probability: Low due to maturity/competition.
Training value: Very high but poor immediate human-EV unless worker already strong.
Next action: Do not hunt blindly. Use published prior Uniswap competition findings as benchmark data first; only enter if worker finds a novel candidate in local replay.

### 11. NEW TO RADAR — Cantina Coinbase bounty
Source: https://cantina.xyz/opportunities
Status: Live since Jul 8, 2025.
Payout: Up to $5,000,000 listed.
Required work: Exact current Coinbase bounty scope on Cantina.
Human effort: 4–10h orientation/review.
Agent ef
