#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('/root/ai-holding-company')
RESEARCH = ROOT / 'business-research-agent'
GAME_STATE = ROOT / 'rpg-command-center/engine/public/game_state.json'
TS = '2026-06-26T08:08:09Z'

revenue_mrr = 0
revenue_evidence = 'RPG Revenue Vault monthlyRevenue is 0; 0 business revenue files found under /root/ai-holding-company/businesses.'

sources = [
    {
        'name': 'Cyber Readiness Institute - A Practical Guide to Agentic AI for SMBs',
        'url': 'https://cyberreadinessinstitute.org/news-and-events/agentic-ai-for-small-medium-sized-businesses/',
        'note': 'March 2026 guidance says agentic AI is becoming practical for SMBs but creates sensitive-data, access, governance, monitoring, and oversight risks.'
    },
    {
        'name': 'GCS Technologies - AI Security Policy Guide for Small Businesses (2026)',
        'url': 'https://www.gcstechnologies.com/ai-security-policy-guide/',
        'note': 'June 2026 article frames shadow AI as an urgent SMB problem: tools got in before rules; businesses need approved-tool lists, data rules, review rules, tool evaluation, and incident handling.'
    },
    {
        'name': 'Miles IT - How to Optimize for AI Search: AEO & GEO Strategy Guide (2026)',
        'url': 'https://www.milesit.com/ai-search-optimization/',
        'note': 'AEO/GEO services are being sold as a 2026 evolution of SEO; small businesses need concise answers, proof, authority, and AI-readable content. No ranking/citation guarantees.'
    },
    {
        'name': 'NetSuite - Make the Business Case for AP Automation in 2026',
        'url': 'https://www.netsuite.com/portal/resource/articles/accounting/ap-automation-business-case.shtml',
        'note': 'Manual AP has measurable costs and fraud/error risk; AP automation business cases use cycle time, cost per invoice, controls, approval flow, and ROI. At $0 MRR, offer readiness docs only.'
    },
    {
        'name': 'Zendesk - AI in Customer Service: Benefits, uses + best practices',
        'url': 'https://www.zendesk.com/blog/ai/ai-customer-service/',
        'note': 'Customer service AI demand is strong; AI can route, automate repetitive work, and use knowledge bases. At $0 MRR, sell KB/triage readiness before helpdesk integrations.'
    },
    {
        'name': 'Installed Agency Agents roster',
        'url': '/root/agency-agents/integrations/codex/agents',
        'note': 'Local workers available: security-architect, compliance-auditor, data-privacy-officer, legal-compliance-checker, automation-governance-architect, document-generator, operations-manager, customer-success-manager, ai-citation-strategist, seo-specialist, content-creator, evidence-collector, pricing-analyst.'
    }
]

def worker(role, slug, responsibility):
    return {'role': role, 'path': f'/root/agency-agents/integrations/codex/agents/{slug}.toml', 'responsibility': responsibility}

opps = [
    {
        'rank': 1,
        'name': 'Shadow AI Policy & Tool Inventory Sprint',
        'score_total': 75,
        'score_average': 9.38,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 10, 'automation_potential': 8, 'margin': 10, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 9, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 10},
        'current_stage_fit': 'Best $0-MRR opportunity: sharper and easier to sell than broad AI safety. SMB employees are already using ChatGPT/Copilot/Claude without rules, and the first paid deliverable is document/interview based: approved-tool list, data-handling rules, human-review rules, incident path, and tool inventory. No scans, credentials, paid tools, legal guarantees, or client system access.',
        'beachhead_icp': '5-50 employee professional-service firms, agencies, clinics, consultants, accountants, law-adjacent offices, local service operators, and B2B teams where staff use AI for emails, proposals, contracts, marketing, finance, support, or client work without a written policy.',
        'offer': 'Free 12-question Shadow AI Risk Self-Check; $499-$1,200 AI Policy & Tool Inventory Sprint including current-use worksheet, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, tool intake form, incident/escalation path, and owner briefing; $500-$1,500/mo quarterly policy refresh, training, and evidence-log retainer after first sale.',
        'zero_cost_stack': ['public guidance', 'local Markdown/CSV templates', 'interview worksheet', 'manual review', 'no paid SaaS', 'no client credentials', 'human approval for any outreach'],
        'agent_workers': [
            worker('Data Privacy Officer','data-privacy-officer','Define sensitive-data categories, retention concerns, and tool/vendor questions.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep language conservative and route legal decisions to qualified humans.'),
            worker('Security Architect','security-architect','Translate shadow-AI and agentic-AI risks into practical controls.'),
            worker('Compliance Auditor','compliance-auditor','Create evidence log, approval trail, and policy review checklist.'),
            worker('Document Generator','document-generator','Assemble the policy, worksheet, tool inventory, and briefing pack.')
        ],
        'next_safe_action': 'Build the Shadow AI self-check, tool-inventory CSV, approved-use matrix, and one-page policy skeleton locally. No outreach, scans, client system access, paid tools, or legal/security guarantees.'
    },
    {
        'rank': 2,
        'name': 'SMB AI Agent Safety & Cyber Readiness Checklist',
        'score_total': 73,
        'score_average': 9.13,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 9, 'automation_potential': 8, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 10, 'fit_with_agency_agents': 10},
        'current_stage_fit': 'Still excellent: broader agentic-AI safety package built from public guidance and templates only. Better as the upsell after the narrower Shadow AI policy sprint.',
        'beachhead_icp': 'SMBs experimenting with browser agents, workflow agents, Claude/ChatGPT automations, or Copilot without permission maps, human approval gates, training, monitoring, or risk logs.',
        'offer': 'Free 10-question AI Agent Safety Self-Check; $399-$999 readiness package with AI-use policy, permission map, risk register, training checklist, incident/escalation plan, and human-approval workflow; $500-$1,500/mo governance/training/evidence-log retainer.',
        'zero_cost_stack': ['public research', 'local Markdown/CSV/JSON templates', 'manual review', 'no paid tools', 'no client credentials before sale'],
        'agent_workers': [
            worker('Security Architect','security-architect','Translate cybersecurity and agentic-AI risks into practical SMB controls.'),
            worker('Compliance Auditor','compliance-auditor','Turn controls into audit-friendly checklist and evidence log.'),
            worker('Data Privacy Officer','data-privacy-officer','Flag sensitive-data, retention, and tool-permission risks.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep claims conservative and route legal/security decisions to humans.'),
            worker('Document Generator','document-generator','Assemble policy, self-check, risk register, and readiness report.')
        ],
        'next_safe_action': 'Keep building template pack; no client scans or credential access.'
    },
    {
        'rank': 3,
        'name': 'AI Search Visibility & LLMs.txt Retrofit Snapshot',
        'score_total': 72,
        'score_average': 9.0,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 10},
        'current_stage_fit': 'Already launched and still strong. AEO/GEO demand is visible in 2026, and public-site review plus local reports create proof samples without paid tools or client credentials. Avoid ranking/citation guarantees.',
        'beachhead_icp': 'Local service businesses and small B2B firms with thin service pages, weak FAQs, unclear proof, and no AI-readable source map or llms.txt guidance.',
        'offer': 'Free 5-point AI Search/LLMs.txt Readiness Snapshot; $299-$799 retrofit plan with answer capsules, FAQ gaps, proof sections, internal-link recommendations, and draft llms.txt map; $300-$900/mo refresh/reporting retainer.',
        'zero_cost_stack': ['public website review', 'local Markdown/CSV/JSON templates', 'manual scoring', 'no paid tools', 'no form submissions'],
        'agent_workers': [
            worker('AI Citation Strategist','ai-citation-strategist','Score answerability, source clarity, entity clarity, and AI-citation readiness.'),
            worker('SEO Specialist','seo-specialist','Review crawlability, service intent, internal links, and page hygiene.'),
            worker('Content Creator','content-creator','Draft answer capsules, FAQs, proof sections, and llms.txt page descriptions.'),
            worker('Evidence Collector','evidence-collector','Collect public evidence snippets and before/after notes.')
        ],
        'next_safe_action': 'Add 3 public-site samples and one before/after source-map example; no outreach execution.'
    },
    {
        'rank': 4,
        'name': 'Invoice & Admin Workflow Readiness Audit',
        'score_total': 70,
        'score_average': 8.75,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 8, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 9},
        'current_stage_fit': 'Demand is validated by AP automation business-case content, but implementation requires accounts/tools. The zero-cost version is a workflow map, approval matrix, field checklist, exception rules, and ROI calculator.',
        'beachhead_icp': 'Owner-operated service businesses, agencies, clinics, trades, and small finance teams still handling invoices, receipts, approvals, and admin follow-up manually.',
        'offer': 'Free admin bottleneck checklist; $399-$899 workflow readiness audit; later $500-$1,500/mo implementation/monitoring after approved tooling.',
        'zero_cost_stack': ['interview worksheet', 'local templates', 'manual workflow mapping', 'no bank/accounting access', 'no paid AP tools'],
        'agent_workers': [
            worker('Operations Manager','operations-manager','Map current workflow and bottlenecks.'),
            worker('Automation Governance Architect','automation-governance-architect','Design safe human-approval automations and exceptions.'),
            worker('Pricing Analyst','pricing-analyst','Build ROI calculator and retainer economics.'),
            worker('Document Generator','document-generator','Package workflow map, checklist, and implementation brief.')
        ],
        'next_safe_action': 'Draft worksheet + ROI calculator only; no bank/accounting access or AP tool connections.'
    },
    {
        'rank': 5,
        'name': 'Customer Support Knowledge-Base & Triage Readiness Sprint',
        'score_total': 69,
        'score_average': 8.63,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 8, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 8, 'fit_with_agency_agents': 9},
        'current_stage_fit': 'Customer-service AI demand is strong, but helpdesk automation needs accounts and customer data. The zero-cost service is a KB gap audit, triage tree, canned-response pack, and human escalation rules.',
        'beachhead_icp': 'Small SaaS, ecommerce stores, agencies, and local service teams with repeated questions, inconsistent replies, weak FAQ pages, and no escalation rules.',
        'offer': 'Free support FAQ gap checklist; $299-$799 support readiness sprint with top-25 FAQ outline, triage tree, escalation policy, canned replies, and weekly reporting template; $500-$1,200/mo KB refresh/reporting retainer.',
        'zero_cost_stack': ['public FAQ/site review', 'client-provided docs only after sale', 'local Markdown/CSV templates', 'no helpdesk login', 'no live chatbot claims'],
        'agent_workers': [
            worker('Customer Success Manager','customer-success-manager','Define customer outcomes and support health metrics.'),
            worker('Content Creator','content-creator','Draft FAQ entries and canned replies.'),
            worker('Operations Manager','operations-manager','Build triage and escalation workflow.'),
            worker('Evidence Collector','evidence-collector','Collect public support-page gaps and examples.')
        ],
        'next_safe_action': 'Create KB/triage readiness checklist and sample triage tree locally; no helpdesk integrations.'
    },
    {
        'rank': 6,
        'name': 'AI Receptionist Readiness & Call Flow Pack',
        'score_total': 66,
        'score_average': 8.25,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 7, 'automation_potential': 8, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 7, 'lead_acquisition_difficulty': 7, 'fit_with_agency_agents': 9},
        'current_stage_fit': 'AI receptionist demand is visible in business-idea results, but outbound AI voice/telecom/KYC/API costs are not allowed at $0 MRR. Safe version is intake scripts, call-routing map, missed-call response rules, and human handoff plan only.',
        'beachhead_icp': 'Local services that miss calls and need better intake structure: clinics, home services, med spas, property managers, agencies.',
        'offer': 'Free missed-call/intake checklist; $299-$799 receptionist readiness pack; implementation only after approved phone/SIP/channel tooling.',
        'zero_cost_stack': ['call-flow docs', 'manual scripts', 'local CSV logging', 'no AI calls', 'no phone API spend', 'no auto-dialing'],
        'agent_workers': [
            worker('Operations Manager','operations-manager','Map intake workflow and handoffs.'),
            worker('Customer Success Manager','customer-success-manager','Design customer-friendly response and escalation rules.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Ensure no illegal AI/prerecorded outbound calling claims.'),
            worker('Document Generator','document-generator','Package scripts and call-flow assets.')
        ],
        'next_safe_action': 'Draft call-flow worksheet and missed-call response script pack only; no calls, telecom setup, AI voice, or paid APIs.'
    }
]

scored = {
    'last_updated': TS,
    'revenue': {
        'mrr': revenue_mrr,
        'sources_checked': ['/root/ai-holding-company/rpg-command-center/engine/public/game_state.json', '/root/ai-holding-company/businesses/**/*revenue*'],
        'revenue_files_found': [],
        'evidence': revenue_evidence,
        'stage_rule': '$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution'
    },
    'scoring_scale': '1-10 where 10 is best. For startup_cost, 10 means lowest cost. For fulfillment_complexity and lead_acquisition_difficulty, 10 means easiest.',
    'criteria': ['startup_cost','speed_to_first_revenue','automation_potential','margin','recurring_revenue_potential','fulfillment_complexity','lead_acquisition_difficulty','fit_with_agency_agents'],
    'sources': sources,
    'opportunities': opps,
    'selected_for_current_stage': ['Shadow AI Policy & Tool Inventory Sprint', 'AI Search Visibility & LLMs.txt Retrofit Snapshot'],
    'fresh_ideas_added_this_run': ['Shadow AI Policy & Tool Inventory Sprint', 'AI Receptionist Readiness & Call Flow Pack']
}

quests = [
    {
        'id': 'research_shadow_ai_policy_inventory_20260626',
        'name': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'title': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'desc': 'Research quest: create Shadow AI self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page AI policy skeleton. No scans, no client system access, no legal/security guarantees, no paid tools, and no outreach execution.',
        'reward': '+160 research XP', 'target': 6, 'current': 0, 'status': 'active',
        'assigned_agent': 'Data Privacy Officer', 'source': 'business_research_agent', 'updated_at': TS,
        'business_stage': '$0 MRR / zero-cost only',
        'safe_next_action': 'Draft the six local templates; route legal/security decisions to human review.'
    },
    {
        'id': 'research_smb_ai_agent_safety_templates_20260626',
        'name': 'Build SMB AI Agent Safety Template Pack',
        'title': 'Build SMB AI Agent Safety Template Pack',
        'desc': 'Research quest: create AI-agent safety self-check, AI-use policy skeleton, permission map, readiness report, and risk register using public guidance only. No scans, no client system access, no legal/security guarantees, no paid tools, and no outreach execution.',
        'reward': '+150 research XP', 'target': 5, 'current': 0, 'status': 'active',
        'assigned_agent': 'Security Architect', 'source': 'business_research_agent', 'updated_at': TS,
        'business_stage': '$0 MRR / zero-cost only', 'safe_next_action': 'Draft the five local templates; route legal/security decisions to human review.'
    },
    {
        'id': 'research_ai_search_llms_samples_20260626',
        'name': 'Add AI Search + LLMs.txt Source-Map Samples',
        'title': 'Add AI Search + LLMs.txt Source-Map Samples',
        'desc': 'Research quest: produce 3 public-website AI Search/LLMs.txt readiness samples and one before/after source-map example. No outreach, no paid tools, no form submissions, no ranking or citation guarantees.',
        'reward': '+125 research XP', 'target': 4, 'current': 0, 'status': 'active',
        'assigned_agent': 'AI Citation Strategist', 'source': 'business_research_agent', 'updated_at': TS,
        'business_stage': '$0 MRR / zero-cost only', 'safe_next_action': 'Use public pages only; save local samples and improvement notes.'
    },
    {
        'id': 'research_invoice_admin_readiness_20260626',
        'name': 'Draft Invoice & Admin Workflow Readiness Audit',
        'title': 'Draft Invoice & Admin Workflow Readiness Audit',
        'desc': 'Research quest: create worksheet, approval-matrix template, data-field checklist, exception-rule template, and ROI calculator. Do not request bank/accounting credentials, connect AP tools, or spend money.',
        'reward': '+110 research XP', 'target': 5, 'current': 0, 'status': 'queued',
        'assigned_agent': 'Operations Manager', 'source': 'business_research_agent', 'updated_at': TS,
        'business_stage': '$0 MRR / zero-cost only', 'safe_next_action': 'Build local templates only; no accounting access or live integrations.'
    },
    {
        'id': 'research_support_kb_triage_20260626',
        'name': 'Draft Support KB & Triage Readiness Sprint',
        'title': 'Draft Support KB & Triage Readiness Sprint',
        'desc': 'Research quest: create support FAQ gap checklist, top-25 FAQ template, triage tree, escalation policy, canned-response pack, and weekly support report template. No helpdesk access, no chatbot setup, no client data handling, and no outbound execution.',
        'reward': '+105 research XP', 'target': 6, 'current': 0, 'status': 'queued',
        'assigned_agent': 'Customer Success Manager', 'source': 'business_research_agent', 'updated_at': TS,
        'business_stage': '$0 MRR / zero-cost only', 'safe_next_action': 'Draft sample templates from public/site-visible support patterns only.'
    },
    {
        'id': 'research_ai_receptionist_readiness_20260626',
        'name': 'Draft AI Receptionist Readiness & Call Flow Pack',
        'title': 'Draft AI Receptionist Readiness & Call Flow Pack',
        'desc': 'Research quest: create intake worksheet, call-routing map, missed-call response scripts, escalation rules, and manual call log. No AI/prerecorded outbound calls, no phone API spend, no auto-dialing, and no telecom setup.',
        'reward': '+95 research XP', 'target': 5, 'current': 0, 'status': 'queued',
        'assigned_agent': 'Operations Manager', 'source': 'business_research_agent', 'updated_at': TS,
        'business_stage': '$0 MRR / zero-cost only', 'safe_next_action': 'Draft scripts and routing docs only; no calling or paid telecom tools.'
    }
]

(RESEARCH / 'ideas').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'reports').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'game').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'ideas/scored-opportunities.json').write_text(json.dumps(scored, indent=2) + '\n')
(RESEARCH / 'game/research_quests.json').write_text(json.dumps(quests, indent=2) + '\n')

score_rows = '\n'.join(f"| {o['rank']} | {o['name']} | {o['score_total']}/80 | {o['current_stage_fit'].split('.')[0]} |" for o in opps)
backlog = f"""# Business Research Backlog

Last updated: {TS}
Revenue stage: $0 MRR from RPG Revenue Vault; 0 business revenue files found.
Rule applied: $0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution.

## Current best opportunity: Shadow AI Policy & Tool Inventory Sprint

**Business identity**
- Market: SMBs whose employees already use ChatGPT, Copilot, Claude, browser agents, and AI writing/research tools without a written policy or tool inventory.
- Buyer pain: owner does not know what tools staff use, what data is being pasted into them, or who reviews AI output before client/customer use.
- Positioning: fast, practical AI security-policy and Shadow AI inventory sprint; not legal advice, cybersecurity certification, penetration testing, managed security, or AI software implementation.

**Offer**
- Free lead magnet: 12-question Shadow AI Risk Self-Check.
- Paid pilot: $499-$1,200 sprint including current-use worksheet, tool inventory, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, tool intake form, incident/escalation path, and owner briefing.
- Retainer: $500-$1,500/mo quarterly policy refresh, training updates, approved-tool evidence log, and governance review after first sale.
- Exclusions: no scans, no credential access, no legal/security guarantees, no compliance certification, no paid tooling before revenue, no outbound execution from this cron.

**Why now / sources**
- Cyber Readiness Institute says agentic AI has become practical for SMBs but increases sensitive-data, access, governance, monitoring, and oversight risks.
- GCS Technologies says many SMBs adopted AI informally: “the tools got in before the rules did”; they need approved-tool lists, data rules, review rules, tool evaluation, and incident handling.
- This is narrower and easier to sell than a broad cyber audit because the first deliverable is policy and inventory documentation only.

**Agent workers found in /root/agency-agents**
- Data Privacy Officer: `/root/agency-agents/integrations/codex/agents/data-privacy-officer.toml`
- Legal Compliance Checker: `/root/agency-agents/integrations/codex/agents/legal-compliance-checker.toml`
- Security Architect: `/root/agency-agents/integrations/codex/agents/security-architect.toml`
- Compliance Auditor: `/root/agency-agents/integrations/codex/agents/compliance-auditor.toml`
- Document Generator: `/root/agency-agents/integrations/codex/agents/document-generator.toml`

**Next safe action**
Build the Shadow AI self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton locally. No outreach, scans, client system access, paid tools, or legal/security guarantees.

---

## Keep scaling: AI Search Visibility & LLMs.txt Retrofit Snapshot

Still the strongest already-started zero-cost service. Current 2026 research shows AEO/GEO/AI-search services are visibly commercialized. Keep producing public website samples and sharpen the monthly retainer. Do not claim ranking/citation guarantees.

**Workers:** AI Citation Strategist, SEO Specialist, Content Creator, Evidence Collector, Offer & Lead Gen Strategist.

**Next safe action:** score 3 more public websites and create a short before/after llms.txt/source-map example.

---

## Fresh opportunities added this run

### Shadow AI Policy & Tool Inventory Sprint
- Offer: free 12-question self-check; $499-$1,200 policy/inventory sprint; $500-$1,500/mo refresh/training/evidence-log retainer.
- Why: urgent 2026 SMB risk, easy owner pain, document-only fulfillment, strong fit with installed privacy/security/compliance/document agents.
- Safe next action: build local templates only.

### AI Receptionist Readiness & Call Flow Pack
- Offer: free missed-call/intake checklist; $299-$799 call-flow/readiness pack; future implementation only after approved phone/SIP/channel tooling.
- Why: AI receptionist demand appears in current AI business-idea research, but at $0 MRR telecom and AI voice are blocked; scripts and routing maps are safe.
- Workers: Operations Manager, Customer Success Manager, Legal Compliance Checker, Document Generator.
- Safe next action: draft call-flow worksheet and missed-call response scripts; no calls, telecom setup, AI voice, or paid APIs.

---

## Other scored opportunities

### SMB AI Agent Safety & Cyber Readiness Checklist
- Offer: free self-check; $399-$999 readiness package; $500-$1,500/mo governance/training/evidence-log retainer.
- Workers: Security Architect, Compliance Auditor, Data Privacy Officer, Legal Compliance Checker, Document Generator.
- Safe next action: complete templates locally.

### Invoice & Admin Workflow Readiness Audit
- Offer: free admin bottleneck checklist; $399-$899 workflow readiness audit; later $500-$1,500/mo implementation/monitoring after approved tooling.
- Workers: Operations Manager, Automation Governance Architect, Pricing Analyst, Document Generator.
- Safe next action: worksheet + ROI calculator only; no bank/accounting access or AP tool connections.

### Customer Support Knowledge-Base & Triage Readiness Sprint
- Offer: free support FAQ gap checklist; $299-$799 support readiness sprint; $500-$1,200/mo KB refresh/reporting retainer after sale.
- Workers: Customer Success Manager, Content Creator, Operations Manager, Evidence Collector.
- Safe next action: create KB/triage readiness checklist and sample triage tree locally; no helpdesk integrations.

## Scoreboard

| Rank | Idea | Score | Stage fit |
|---:|---|---:|---|
{score_rows}
"""
(RESEARCH / 'ideas/backlog.md').write_text(backlog)

latest = f"""# Business Research Agent — Latest Report

Updated: {TS}

## Revenue check
- Current MRR: **$0**.
- Evidence: {revenue_evidence}
- Rule applied: **$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution**.

## Best idea now
**Shadow AI Policy & Tool Inventory Sprint** — **75/80**

Why it wins:
- Narrower and easier to sell than a broad AI/cyber audit: “your staff are already using AI — do you know which tools and what data?”
- Fresh 2026 sources validate the pain: CRI highlights agentic-AI governance/data/access risks for SMBs; GCS says the tools got in before the rules and small businesses need AI security policies.
- Zero-cost fulfillment: self-check, tool-inventory CSV, approved-use matrix, sensitive-data rules, human-review checklist, tool intake form, incident path, and owner briefing.
- Strong agent fit: Data Privacy Officer, Legal Compliance Checker, Security Architect, Compliance Auditor, Document Generator.

## Runner-up / keep building
**AI Search Visibility & LLMs.txt Retrofit Snapshot** — **72/80**

Why it stays active:
- Already partially launched and still fits $0 MRR.
- 2026 AEO/GEO/AI-search services are visibly commercialized; a small-business snapshot is a lower-cost entry point.
- Public-site review + local reports can create samples without paid tools or client access.
- Best workers: AI Citation Strategist, SEO Specialist, Content Creator, Evidence Collector.

## Fresh ideas added
- **Shadow AI Policy & Tool Inventory Sprint** — 75/80: best immediate zero-cost sprint, document-only, urgent SMB governance pain.
- **AI Receptionist Readiness & Call Flow Pack** — 66/80: promising local-service demand, but keep it to scripts/routing/readiness because AI voice, telecom, and outbound automation are blocked at $0 MRR.

## Scored ideas
1. Shadow AI Policy & Tool Inventory Sprint — 75/80
2. SMB AI Agent Safety & Cyber Readiness Checklist — 73/80
3. AI Search Visibility & LLMs.txt Retrofit Snapshot — 72/80
4. Invoice & Admin Workflow Readiness Audit — 70/80
5. Customer Support Knowledge-Base & Triage Readiness Sprint — 69/80
6. AI Receptionist Readiness & Call Flow Pack — 66/80

## Game-ready quests prepared
- Build Shadow AI Policy & Tool Inventory Sprint — assigned to Data Privacy Officer.
- Build SMB AI Agent Safety Template Pack — assigned to Security Architect.
- Add AI Search + LLMs.txt Source-Map Samples — assigned to AI Citation Strategist.
- Draft Invoice & Admin Workflow Readiness Audit — assigned to Operations Manager.
- Draft Support KB & Triage Readiness Sprint — assigned to Customer Success Manager.
- Draft AI Receptionist Readiness & Call Flow Pack — assigned to Operations Manager.

## Next safe action
Build the Shadow AI self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton. Do **not** contact prospects, submit forms, access client systems, run scans, place calls, send emails, connect SaaS tools, or spend money.

## Artifacts updated
- `/root/ai-holding-company/business-research-agent/ideas/backlog.md`
- `/root/ai-holding-company/business-research-agent/ideas/scored-opportunities.json`
- `/root/ai-holding-company/business-research-agent/reports/latest.md`
- `/root/ai-holding-company/business-research-agent/game/research_quests.json`
- `/root/ai-holding-company/rpg-command-center/engine/public/game_state.json` updated non-destructively with research quest/status/event.
"""
(RESEARCH / 'reports/latest.md').write_text(latest)

state = json.loads(GAME_STATE.read_text())
quest_by_id = {q.get('id'): i for i, q in enumerate(state.get('quests', [])) if isinstance(q, dict) and q.get('id')}
for q in quests:
    slim = {
        'id': q['id'], 'name': q['name'], 'title': q['title'], 'desc': q['desc'], 'reward': q['reward'],
        'target': q['target'], 'current': q['current'], 'status': q['status'], 'assigned_agent': q['assigned_agent'],
        'source': 'business_research_agent', 'updated_at': TS, 'next_step': q['safe_next_action']
    }
    if q['id'] in quest_by_id:
        state['quests'][quest_by_id[q['id']]].update(slim)
    else:
        state.setdefault('quests', []).append(slim)

for a in state.get('agents', []):
    if a.get('name') == 'Business Research Agent':
        a['status'] = 'working'
        a['current_task'] = 'Selected Shadow AI Policy & Tool Inventory Sprint as the best $0-MRR opportunity; queued policy/inventory templates and kept AI Search samples active. No outreach or spend.'
        a['last_seen'] = TS
        a['last_message'] = 'Best $0-MRR idea now: Shadow AI Policy & Tool Inventory Sprint. Runner-up: AI Search/LLMs.txt Retrofit Snapshot.'

state.setdefault('events', []).append({
    'timestamp': TS,
    'type': 'research_update',
    'agent': 'Business Research Agent',
    'message': 'Selected Shadow AI Policy & Tool Inventory Sprint as the best $0-MRR opportunity, kept AI Search/LLMs.txt active, and queued AI Receptionist Readiness as a safe docs-only runner-up. Safe quests only; no outreach or spend.',
    'source': 'business_research_agent'
})
state['timestamp'] = TS
GAME_STATE.write_text(json.dumps(state, indent=2) + '\n')
print(json.dumps({'updated': True, 'timestamp': TS, 'opportunities': len(opps), 'quests': len(quests), 'best': opps[0]['name']}, indent=2))
