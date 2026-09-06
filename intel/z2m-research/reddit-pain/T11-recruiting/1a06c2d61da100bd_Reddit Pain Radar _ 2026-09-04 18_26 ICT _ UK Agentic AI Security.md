# Reddit Pain Radar — 2026-09-04 18:26 ICT — UK Agentic AI Security

**From:** Prior Trades <tradesprior@gmail.com>
**Date:** Fri, 4 Sep 2026 04:28:28 -0700
**Message ID:** 1a06c2d61da100bd

---

# Reddit Pain Radar — 4 Sep 2026, 18:26 ICT — UK Agentic AI Security

## Executive ranking

This run deliberately rotated away from last hour’s broad prompt-injection/red-team framing and focused on five narrower UK agentic-security seams: (1) runtime least-privilege enforcement where SaaS/ERP APIs expose overly broad scopes; (2) Copilot/agent-accessible oversharing in Microsoft 365; (3) MCP/skill supply-chain attestation; (4) continuous agent red-team acceptance testing as a procurement/evidence layer; and (5) security evidence compilation against UK/ETSI/OWASP controls.

| Rank | Opportunity | Recurrence | Urgency | Spend | Incumbent weakness | Buildability | Defensibility | Score |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Runtime Least-Privilege Gateway for AI Agents | 10 | 10 | 10 | 10 | 8 | 10 | 9.7 |
| 2 | Microsoft 365 Agent Oversharing / Permission-Drift Preflight | 10 | 10 | 9 | 9 | 9 | 9 | 9.4 |
| 3 | MCP / Agent-Skill Supply-Chain Attestation | 9 | 10 | 9 | 10 | 9 | 10 | 9.4 |
| 4 | Continuous Agent Red-Team Acceptance / Security CI | 9 | 10 | 10 | 8 | 9 | 9 | 9.3 |
| 5 | UK AI-Security Evidence Compiler | 8 | 9 | 9 | 9 | 10 | 9 | 9.0 |

## 1. Runtime Least-Privilege Gateway for AI Agents — 9.7/10

### Evidence

Fresh Reddit discussion in July 2026 gets to the implementation problem directly. A thread about least privilege for AI agents recommends just-in-time access, short-lived credentials and continuous governance, but a practitioner replies that least privilege is difficult in many ERPs because APIs are too broadly scoped and full logs may not exist. Their conclusion is that this makes agentic AI hard to justify in ERP environments.

Source: https://www.reddit.com/r/Cyberseven/comments/1vbp66g/need_for_least_privilege_access_for_ai_agents/

This aligns closely with the new OWASP Agent Control Standard released on 1 September 2026. ACS says enterprises cannot rely on black-box agents operating across SaaS, cloud, endpoints and on-prem systems; agents need to be inspectable, traceable and controllable at runtime. It defines middleware hooks and portable declarative safety policies for runtime enforcement.

Source: https://genai.owasp.org/resource/agent-control-standard-acs/

OWASP’s February 2026 MCP security guide independently identifies delegated user permissions and chained tool calls as core reasons MCP requires stronger authentication, authorization, validation and isolation than ordinary API integrations.

Source: https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/

The demand backdrop in the UK is unusually favorable. DSIT’s 2026 sector analysis counts 111 firms explicitly offering cyber security for AI, up 68% year-on-year, but only 5% explicitly offering agentic AI security and 5% AI browser/endpoint security. The wider UK cyber sector is estimated at £14.7bn annual revenue.

Source: https://www.gov.uk/government/publications/cyber-security-sectoral-analysis-2026/cyber-security-sectoral-analysis-2026

### Inference

The opportunity is not another policy dashboard. Build a runtime action gateway between an agent and consequential tools:

agent → requested action → authenticated user/agent → target tool → resource → parameters → provenance → policy decision

Return:

ALLOW / DENY / REQUIRE APPROVAL / ALLOW WITH TRANSFORMED SCOPE

The gateway should mint short-lived credentials or proxy requests so the agent never receives broad standing credentials. Useful policies:

- read-only by default;
- per-task resource scopes;
- £/$ transaction limits;
- no external email without approval;
- no destructive actions on production;
- no secrets/data exfiltration to unapproved domains;
- no writes triggered by untrusted retrieved content;
- separate privileges for model reasoning and execution;
- deterministic approval gates for high-impact mutations.

The crucial distinction is that prompt instructions are advisory; authorization must be enforced outside the model.

### Exact workflow / buyer / WTP

Who has the pain: CISOs, platform/security engineers, MSPs, enterprise AI teams and SaaS vendors deploying agents over Microsoft 365, ServiceNow, Salesforce, ERPs, GitHub, cloud and internal APIs.

Current workarounds: human approvals, manually scoped API keys, sandbox accounts, “read-only agent” promises, broad OAuth scopes with logging after the fact.

What users dislike: APIs frequently expose permissions at the wrong granularity, logs are incomplete, credentials live too long, and agent frameworks treat security largely as application-level configuration.

Economic importance: one successful prompt-injection/tool-use chain can become data loss, destructive production change, unauthorized payment or regulatory violation.

WTP signal: enterprise security infrastructure budget; plausible $1k–$20k/month by environment/agent count, higher for regulated deployments.

Switching barrier: low if it is an outbound proxy/middleware layer rather than an agent framework replacement.

Distribution: UK MSPs/MSSPs, AI consultancies, pentest firms, Microsoft partners, OWASP/ACS ecosystem, enterprise platform engineering.

### Concrete MVP

Support OpenAI/Anthropic agent tool calls plus GitHub, Gmail/Microsoft Graph and one high-value enterprise API. Expose a declarative policy file and signed action log. Demonstrate a poisoned-email indirect prompt injection that successfully fools the model but fails to exfiltrate data because the gateway denies the forbidden tool call.

That demo is much stronger than “our classifier detected prompt injection.”

---

## 2. Microsoft 365 Agent Oversharing / Permission-Drift Preflight — 9.4/10

### Evidence

A March 2026 Microsoft 365 practitioner says oversharing was the number-one risk identified during Copilot rollout. Their team audited SharePoint and OneDrive, found examples including entire OneDrives being shared, and now repeats the reporting quarterly.

Short excerpt: “This was the #1 risk we identified.”

Source: https://www.reddit.com/r/microsoft365/comments/1rzw8gx/removed/

Another current discussion emphasizes the correct nuance: Copilot generally respects existing Microsoft 365 permissions, but that means it inherits the organization’s historical permission mistakes. A practitioner specializing in Purview and Copilot says this area is generating substantial work for MSPs.

Source: https://www.reddit.com/r/microsoft_365_copilot/comments/1uovl73/what_governed_ai_actually_means_and_why_microsoft/

A May sysadmin integrating Copilot into accounting explicitly asks for guidance on permissions, SLAs, data protection and legal risks because client information cannot be exposed.

Source: https://www.reddit.com/r/sysadmin/comments/1thy376/copilot_company_integration/

Microsoft’s agent footprint is simultaneously becoming larger and harder for admins to reason about. A July Azure Copilot change notice caused confusion because supported agents would become directly available when Azure Copilot was enabled; the Reddit poster says Microsoft documentation is “not useful” and mostly marketing.

Source: https://www.reddit.com/r/Office365/comments/1v3ohbl/email_about_azure_copilot_agent_access/

### Inference

This is a clean UK/MSP startup wedge: an agent-accessible-data preflight scanner for Microsoft 365.

Map:

user/agent → effective permissions → SharePoint/OneDrive/Teams/Exchange → sensitive content classes → reachable data → likely AI retrieval paths

Then adversarially ask:

- Can an ordinary user retrieve executive-only content through Copilot?
- Can stale sharing expose HR/PHI/client data?
- Does an agent connection expand access beyond the intended knowledge base?
- Which public/external links become discoverable by AI search?
- Which permissions are technically valid but organizationally unjustifiable?

This is not an ACL bypass detector. It is a detector for permission state that is already wrong but becomes dramatically more exploitable once AI can search and synthesize everything a user can reach.

### Reliability requirement

Permission calculations must come from actual Microsoft Graph/SharePoint state. AI may classify content and generate adversarial search prompts, but effective ACL resolution and findings must be deterministic and reproducible.

### Buyer / WTP / distribution

Buyer: MSPs, Microsoft partners, legal/accounting/professional-services firms, councils, schools and mid-market enterprises adopting Copilot.

WTP: $500–$5k/month per tenant depending on size, with one-off assessment packages particularly sellable through MSPs.

Switching barrier: virtually zero; read-only assessment first.

Distribution: UK Microsoft CSPs/MSPs. This is especially attractive because the MSP already owns the trust relationship and can bundle “Copilot readiness/security preflight.”

### MVP

Read-only Microsoft Graph scanner that identifies overshared high-risk resources, then runs a set of synthetic Copilot-access tests using test identities. Produce an evidence bundle:

RESOURCE → EFFECTIVE USERS → SENSITIVITY → COPILOT-RETRIEVABLE? → RECOMMENDED FIX → POST-FIX RETEST

---

## 3. MCP / Agent-Skill Supply-Chain Attestation — 9.4/10

### Evidence

OWASP’s 2026 Agentic Skills Top 10 describes a live supply-chain problem. It cites Snyk’s February 2026 ToxicSkills analysis of 3,984 skills, finding 1,467 with security flaws (36.82%), 534 with critical issues (13.4%), and 76+ confirmed malicious payloads. OWASP also documents subsequent 2026 research showing weaknesses in public scanners and takeover risks from external dependencies.

Source: https://owasp.org/www-project-agentic-skills-top-10/

A July Reddit MCP developer advertising a Gmail MCP emphasizes local-only execution, configurable OAuth scopes, minimal dependencies and manual security review of community PRs. The fact that security properties themselves are part of the product pitch is a strong market signal.

Source: https://www.reddit.com/r/mcp/comments/1uzvvcu/gmail_mcp_for_cla
