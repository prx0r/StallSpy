# Agent Money Scout — 2026-09-04 21:00

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Fri, 4 Sep 2026 07:25:03 -0700
**Message ID:** 1a06ccf0cae45206

---

# Agent Money Scout — Security Only — 2026-09-04 21:00

## NEW THIS RUN

### 1. Optimism — Immunefi — $50 web medium / $500 web high / $1,000 blockchain medium → $2,000,042 critical
https://immunefi.com/bug-bounty/optimism/information/

Optimism’s bounty was updated September 1, 2026. Blockchain/DLT and smart-contract medium rewards are $1,000–$15,000; highs $15,000–$50,000; criticals up to $2,000,042. Web/app medium is $50–$500, high $500–$5,000, critical $5,000–$50,000. PoC and KYC are required. Testing of cross-domain exploits is explicitly directed toward dockerized/local integration environments rather than live systems.

Agent work: scope/audit corpus → recent-diff ranking → static/property/fuzz tests locally → reproduce → impact/duplicate gate → human review → submit. Who pays: Optimism via Immunefi, USDC on Ethereum. Required: Go/C++/Solidity depending target, local test harness, Immunefi account/KYC. Autonomy 8/10. First action: target medium-impact code paths with local integration tests rather than live web probing. Constraints: only program-authorized assets/methods; obey Immunefi prohibitions. Ease first $5: 5/10. Repeatability: 10/10.

### 2. Lombard Finance — Immunefi — up to $250,000
https://immunefi.com/bug-bounty/lombard-finance/information/

Live and updated September 2. Critical maximum is $250,000; high smart-contract findings can pay $10,000–$50,000 depending funds at risk. Critical web/app findings can pay $15,000–$30,000 depending impact. Important economic constraint: every report requires a non-refundable Immunefi submission fee, so false-positive control matters directly.

Agent work: scope → candidate → local PoC → known-issue/duplicate check → expected-value gate → submit only when confidence clears threshold. Who pays: Lombard directly in USDC on Ethereum. Required: smart-contract/security expertise, PoC, KYC, submission fee. Autonomy 8/10. First action: ingest all known issues/audits and make `expected bounty × validity probability > fee + compute` a hard submit rule. Ease 3/10. Repeatability 9/10.

### 3. Upwork — Security Engineer & SOC/IR Specialist — $800 fixed
https://www.upwork.com/freelance-jobs/apply/Security-Engineer-SOC-Specialist-Wazuh-Prometheus-Ubuntu-macOS_~022095560026744540685/

Posted September 3, worldwide. Buyer has a distributed fleet of Ubuntu servers, NVIDIA GPU workstations and macOS hosts over Tailscale and wants endpoint hardening plus production Wazuh + Prometheus/Grafana monitoring, alert tuning and incident-response capability.

Agent work: authorized config inventory → baseline/hardening findings → Wazuh/Prometheus deployment config → rule tuning → evidence/reporting. Who pays: Upwork client. Required: genuine Ubuntu/macOS, Wazuh, Prometheus, networking/Tailscale and IR experience; buyer asks for sanitized prior examples. Autonomy 7/10 because remediation/containment should remain human-controlled. First action: propose Phase 1 as deterministic inventory + baseline + monitoring validation. Ease 6/10. Repeatability 10/10.

### 4. Upwork — Healthcare security audit + monitoring — $1,000 + $100–$250/month
https://www.upwork.com/freelance-jobs/apply/Cybersecurity-Consultant-Security-Audit-Ongoing-Monitoring-for-Healthcare-Small-Business-HIPAA_~022093437448560588248/

Worldwide. A telehealth practice wants a practical Google Workspace + WordPress + credential/social-engineering assessment, lightweight HIPAA Security Risk Assessment and then 2–5 hours/month of ongoing review. Phase 1 is $1,000 fixed; Phase 2 is advertised at $100–$250/month.

Agent work: authorized configuration/evidence collection → MFA/account/WordPress posture → risk ranking → remediation tracker → monthly evidence diff. Who pays: Upwork client. Required: healthcare/HIPAA familiarity, Google Workspace and WordPress security; BAA may be required if patient-data systems are accessed. Autonomy 8/10 for evidence collection/reporting, lower for final compliance judgment. First action: offer a least-privilege evidence checklist and risk-ranked report structure. Ease 7/10. Repeatability 10/10.

### 5. Upwork — AI-assisted security remediation — $200 fixed
https://www.upwork.com/freelance-jobs/apply/Full-Stack-NET-Angular-Azure-Developer-Security-Remediation_~022095351436984303181/

Posted September 3, worldwide. Buyer explicitly needs someone to validate and remediate security issues found by AI-assisted code analysis in a .NET/C#/Angular/Azure SaaS. Scope includes authz/session handling, validation, secrets, Key Vault, Entra ID, APIs and unsafe AI-generated code patterns.

This is unusually aligned with an agent verifier: AI finding → code/data-flow analysis → reproduce/validate → patch → regression test → evidence. Who pays: Upwork client. Required: .NET/C#, Angular, Azure and real SaaS security experience. Autonomy 9/10. First action: propose a fixed finding-validation pipeline rather than trusting the scanner output. Ease 9/10. Repeatability 10/10.

### 6. Upwork — GRC Analyst — $4,000 fixed, 6–8 months
https://www.upwork.com/freelance-jobs/apply/GRC-Analyst_~022095094395964345869/

Posted September 2, worldwide, 10–15 proposals and zero interviews at crawl. Work includes ISO 27001/SOC 2 readiness, gap/control assessments, risk registers, policies, Risk & Control Matrices, evidence collection/validation and remediation tracking.

Agent work: evidence connector → control mapping → stale/missing evidence → risk/control register → remediation tracker → audit packet. Who pays: Upwork client. Required: 2+ years practical GRC; certifications preferred. Autonomy 8/10 for evidence mechanics; human needed for professional judgments/sign-off. First action: pitch an evidence-first operating system rather than document generation alone. Ease 6/10. Repeatability 10/10.

### 7. Upwork — SOC 2 Type 1 readiness — $3,500 fixed
https://www.upwork.com/freelance-jobs/apply/SOC-Type-Readiness-Execution_~022093386595967181237/

Worldwide, ongoing. Buyer wants current controls reviewed, gaps identified and documentation/evidence organized for its auditor. Client has $19K prior spend and 33 hires; 50+ proposals but zero interviews when crawled.

Agent work: system inventory → control/evidence map → gap detection → evidence freshness → issue tracker → auditor-ready package. Who pays: Upwork client. Required: genuine SOC 2 readiness experience. Autonomy 8/10. First action: propose an evidence completeness/freshness matrix as the first deliverable. Ease 5/10 due competition. Repeatability 10/10.

### 8. Upwork — SaaS pre-launch pentest — $75 fixed
https://www.upwork.com/freelance-jobs/apply/Web-Application-Security-Penetration-Tester-for-SaaS-Pre-Launch-Audit_~022093841190961784171/

Worldwide; 5–10 proposals and zero interviews at crawl. Authorized QA/staging only. React/TypeScript/Supabase/Postgres/Cloudflare/Stripe app with multi-tenancy, roles, public booking, subscriptions and file storage. No destructive or DoS testing, no unauthorized access to real customer data.

Agent work: supplied staging accounts → role/tenant matrix → Supabase RLS/API checks → candidate → safe reproduction → report → retest. Who pays: Upwork client. Required: web/API security, Supabase RLS useful. Autonomy 8/10. First action: offer a bounded tenant-isolation + RLS test pack. Ease first $5 9/10. Repeatability 10/10.

### 9. Upwork — Independent NIST/DevSecOps architecture review — $600 fixed
https://www.upwork.com/freelance-jobs/apply/Independent-Cybersecurity-Architecture-Desktop-Review-NIST-DevSecOps_~022095318864214082487/

Posted September 3. Entirely asynchronous desktop review: identity, secure delivery, runtime controls, incident response, auditability and evidence reconstruction. No pentesting, production access or implementation is required.

Agent work: architecture/docs → claims/control graph → NIST/CSF/Zero Trust mapping → contradictions/gaps → evidence-backed written assessment. Who pays: Upwork client. Required: senior cyber credentials/experience and independence. Hard constraint: U.S.-located freelancers only. Autonomy 9/10 for analysis, but signed expert assessment requires qualified human reviewer. First action: only pursue if geography/credentials fit. Ease 2/10 otherwise; 7/10 if eligible. Repeatability 9/10.

### 10. Upwork — Penetration Test Report for SOC 2 — $250 fixed
https://www.upwork.com/freelance-jobs/apply/Penetration-Test-Report-for-SOC_~022087607372516080901/

Worldwide listing seeks an authorized penetration test plus a comprehensive report suitable for a SOC 2 audit. $250 fixed.

Agent work: written authorization/scope → scanner-assisted discovery → manual validation → dedupe → safe reproduction → remediation → compliance-style report. Who pays: Upwork client. Required: pentesting and compliance reporting experience. Autonomy 7/10; human scope approval and final sign-off required. First action: obtain exact rules of engagement before testing and define deliverable/report format. Ease 6/10. Repeatability 9/10.

## STILL ACTIVE FROM PRIOR RUNS

### 11. Patchstack — WordPress bug bounty economy
https://patchstack.com/bug-bounty/

Still one of the best agent-compatible security corpora: public plugins/themes, local reproducible environments and cash payouts beginning in the hundreds depending install count/severity, plus its monthly researcher pool. Agent: plugin/theme version diff → security-sensitive change ranking → local validation → duplicate gate → submission. Who pays: Patchstack. Required: Patchstack researcher account and program compliance. Autonomy 9/10. First action: rank high-install plugins by recent auth/input/file-handling code changes. Ease 8/10. Repeatability 10/10.

### 12. 1inch — Immunefi — $100 low → $500,000 critical
https://immunefi.com/bug-bounty/1inch-SmartContracts/information/

Still attractive because valid low findings can pay $100–$2,000; medium $2K–$10K, high $10K–$30K, critical up to $500K. Agent: contract diff/invariants → Foundry tests → minimized PoC → duplicate/known-iss
