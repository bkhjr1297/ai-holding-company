#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('/root/ai-holding-company')
RESEARCH = ROOT / 'business-research-agent'
GAME_STATE = ROOT / 'rpg-command-center/engine/public/game_state.json'
AGENTS = Path('/root/agency-agents/integrations/codex/agents')
TS = '2026-06-27T08:42:29Z'
STAMP = '20260627_0842'

revenue_files = list((ROOT / 'businesses').glob('**/*revenue*')) if (ROOT / 'businesses').exists() else []
with GAME_STATE.open() as f:
    game_state = json.load(f)
mrr = int(game_state.get('buildings', {}).get('revenue_vault', {}).get('monthlyRevenue', 0) or 0)

def worker(role, slug, responsibility):
    path = AGENTS / f'{slug}.toml'
    return {
        'role': role,
        'path': str(path),
        'responsibility': responsibility,
        'exists': path.exists()
    }

sources = [
    {
        'name': 'Cyber Readiness Institute - Practical Guide to Agentic AI for SMBs',
        'url': 'https://cyberreadinessinstitute.org/news-and-events/agentic-ai-for-small-medium-sized-businesses/',
        'note': 'CRI says agentic AI is becoming practical for SMBs because agents can plan, use software, interact with systems, and complete multi-step work, but the same autonomy increases cybersecurity, access, oversight, and data-exposure risk.'
    },
    {
        'name': 'U.S. Small Business Administration - AI for small business',
        'url': 'https://www.sba.gov/business-guide/manage-your-business/ai-small-business',
        'note': 'SBA says AI can help small businesses do more with less, but recommends starting small, human review of AI products, avoiding sensitive/proprietary data in tools, and responsible/ethical use.'
    },
    {
        'name': 'GCS Technologies - AI Security Policy Guide for Small Businesses (2026)',
        'url': 'https://www.gcstechnologies.com/ai-security-policy-guide/',
        'note': 'Small businesses often adopted AI informally; policy should cover approved tools, data-handling rules, human review, tool requests, incident/exception handling, and shadow AI visibility.'
    },
    {
        'name': 'Adobe Business - SEO in 2026: AI reshaping search',
        'url': 'https://business.adobe.com/blog/seo-in-2026-fundamentals',
        'note': 'AI search shifts optimization from rankings to citation accuracy, extractable facts, credibility, structured content, crawler/content governance, and brand representation in AI answers.'
    },
    {
        'name': 'Installed Agency Agents roster',
        'url': '/root/agency-agents/integrations/codex/agents',
        'note': 'Local worker personas were checked before assigning roles; no custom agents were needed for this run.'
    }
]

opportunities = [
    {
        'name': 'Shadow AI Policy & Tool Inventory Sprint',
        'score_total': 78,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 10, 'automation_potential': 9, 'margin': 10, 'recurring_revenue_potential': 10, 'fulfillment_complexity': 9, 'lead_acquisition_difficulty': 10, 'fit_with_agency_agents': 10},
        'fit': 'Still the strongest $0-MRR offer. SBA and current SMB policy guidance reinforce that AI is already inside businesses, but owners need approved-tool visibility, sensitive-data rules, and human review before adoption scales.',
        'icp': '5-50 employee SMBs using ChatGPT, Copilot, Claude, embedded AI, or browser agents without a written AI-use policy, inventory, sensitive-data rules, or human-review workflow.',
        'offer': 'Free 12-question Shadow AI Risk Self-Check; $499-$1,200 AI Policy & Tool Inventory Sprint; $500-$1,500/mo quarterly refresh/training/evidence-log retainer after first sale.',
        'stack': ['SBA/public AI risk guidance', 'local Markdown/CSV templates', 'manual interview worksheet', 'manual review', 'no paid SaaS', 'no client credentials'],
        'workers': [
            worker('Data Privacy Officer','data-privacy-officer','Define sensitive-data categories, retention boundaries, and privacy-safe AI-use questions.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep wording conservative and route legal decisions to qualified humans.'),
            worker('Security Architect','security-architect','Translate Shadow AI risks into practical SMB control checklists.'),
            worker('Compliance Auditor','compliance-auditor','Create recurring evidence logs and review checklists.'),
            worker('Document Generator','document-generator','Package self-checks, matrices, and owner briefing templates.')
        ],
        'next': 'Build self-check, tool inventory CSV, approved/prohibited matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton.'
    },
    {
        'name': 'Agentic AI Access & Human Approval Map Sprint',
        'score_total': 77,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 9, 'automation_potential': 10, 'margin': 10, 'recurring_revenue_potential': 10, 'fulfillment_complexity': 9, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 10},
        'fit': 'Best fresh idea this run. CRI specifically frames agentic AI as useful for SMBs because agents can take actions and complete multi-step work, but warns that autonomy amplifies access, data-exposure, oversight, and cybersecurity risk. This is a docs-only readiness sprint that rides the next step after basic Shadow AI policy.',
        'icp': 'SMBs experimenting with AI agents, browser agents, Copilot/Claude workflows, Zapier/n8n automations, customer-support bots, or internal workflow automations but lacking access boundaries and human approval rules.',
        'offer': 'Free Agent Autonomy Risk Scorecard; $599-$1,500 Agentic AI Access & Human Approval Map Sprint; $750-$1,750/mo governance refresh/evidence-log retainer after first sale.',
        'stack': ['CRI/public agentic-AI guidance', 'local access-map template', 'human-approval matrix', 'manual workflow interviews after sale', 'no system logins', 'no scans or automation execution'],
        'workers': [
            worker('Automation Governance Architect','automation-governance-architect','Decide which agent actions require human approval, logs, rollback, or prohibition.'),
            worker('Agentic Identity & Trust Architect','agentic-identity-trust-architect','Map agent identity, delegated authority, audit trails, and proof-of-action requirements.'),
            worker('Security Architect','security-architect','Translate autonomy and access risk into practical SMB safeguards.'),
            worker('Data Privacy Officer','data-privacy-officer','Map sensitive data exposure boundaries and retention limits.'),
            worker('Workflow Architect','workflow-architect','Document agent workflow trees, branch conditions, failure modes, and handoffs.'),
            worker('Document Generator','document-generator','Package the map, approval matrix, and executive briefing.')
        ],
        'next': 'Draft autonomy levels, access/permission map, human-approval gate matrix, AI-agent risk register, audit-log checklist, and owner briefing template locally.'
    },
    {
        'name': 'SMB AI Data Readiness & Workflow Prioritization Sprint',
        'score_total': 76,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 9, 'automation_potential': 10, 'margin': 9, 'recurring_revenue_potential': 10, 'fulfillment_complexity': 9, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 10},
        'fit': 'Strong zero-cost implementation-prep offer. SMB owners want AI but need help choosing workflows, data sources, privacy boundaries, and measurable ROI before using paid tools or accessing systems.',
        'icp': 'Manufacturing, field service, construction, distribution, local services, and professional-service SMBs that want AI for reporting, operations, support, or marketing but have messy data and no prioritized roadmap.',
        'offer': 'Free AI Workflow Readiness Scorecard; $499-$1,200 Data Readiness & Workflow Prioritization Sprint; $750-$1,500/mo KPI/evidence-log refresh retainer after first sale.',
        'stack': ['public AI-readiness guidance', 'client-provided workflow notes after sale', 'local CSV/Markdown worksheets', 'manual use-case scoring', 'no system logins', 'no paid AI tools'],
        'workers': [
            worker('Operations Manager','operations-manager','Map workflows, bottlenecks, handoffs, and owner time sinks.'),
            worker('Workflow Optimizer','workflow-optimizer','Prioritize high-ROI, low-risk automation candidates.'),
            worker('Data Consolidation Agent','data-consolidation-agent','Define data-source inventory fields and data-quality checks without accessing systems.'),
            worker('Data Privacy Officer','data-privacy-officer','Flag sensitive-data/security constraints before AI use.'),
            worker('Analytics Reporter','analytics-reporter','Create KPI baseline and measurable-results scorecard.'),
            worker('Document Generator','document-generator','Package roadmap, worksheets, and executive brief.')
        ],
        'next': 'Draft workflow inventory, data-source checklist, AI use-case scoring matrix, data-risk register, KPI baseline sheet, and 30-day pilot roadmap.'
    },
    {
        'name': 'SMB AI Tool Stack Rationalization Sprint',
        'score_total': 75,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 9, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 9, 'lead_acquisition_difficulty': 10, 'fit_with_agency_agents': 10},
        'fit': 'Natural sibling to Shadow AI: SMBs using multiple AI/productivity tools need ownership, cost visibility, workflow fit, and approved-tool decision rules; no-login inventory/roadmap can be fulfilled at $0 MRR.',
        'icp': 'SMBs using multiple AI/productivity tools across marketing, admin, support, sales, and operations but lacking ownership, cost visibility, workflow mapping, or adoption priorities.',
        'offer': 'Free AI Tool Sprawl Checklist; $399-$899 Tool Stack Rationalization Sprint; $500-$1,500/mo implementation governance after approved tools/channels exist.',
        'stack': ['client-provided tool list after sale', 'public tool docs', 'local CSV/Markdown worksheets', 'manual workflow mapping', 'no SaaS login', 'no paid implementation'],
        'workers': [
            worker('Tool Evaluator','tool-evaluator','Compare tools, workflow fit, duplicate spend, and no/low-cost alternatives.'),
            worker('Operations Manager','operations-manager','Map workflows, bottlenecks, and owner time savings.'),
            worker('Pricing Analyst','pricing-analyst','Estimate monthly tool spend and consolidation ROI.'),
            worker('Data Privacy Officer','data-privacy-officer','Flag sensitive-data and vendor-review concerns.'),
            worker('Document Generator','document-generator','Package inventory, roadmap, and owner briefing.')
        ],
        'next': 'Draft tool-inventory CSV, duplicate-cost worksheet, workflow priority matrix, approved-tool decision guide, and 30-day adoption plan.'
    },
    {
        'name': 'Customer Support Knowledge-Base & AI Triage Readiness Sprint',
        'score_total': 74,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 9, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 10, 'fit_with_agency_agents': 10},
        'fit': 'Strong zero-cost readiness offer. SBA highlights AI customer-service use cases, but teams still need FAQ structure, routing, escalation, transparency, training, and measurement before chatbot deployment.',
        'icp': 'Small SaaS, ecommerce, appointment businesses, clinics, agencies, and local-service teams with repeated questions, inconsistent replies, weak FAQ pages, and no escalation rules.',
        'offer': 'Free Support AI-Readiness Checklist; $399-$899 KB/Triage Sprint; $500-$1,200/mo KB refresh/reporting retainer.',
        'stack': ['public FAQ/support-page review', 'client docs after sale', 'local Markdown/CSV templates', 'no helpdesk login', 'no chatbot claims'],
        'workers': [
            worker('Customer Success Manager','customer-success-manager','Define support outcomes, SLA rules, and customer-success reporting.'),
            worker('Support Responder','support-responder','Draft canned replies and escalation language.'),
            worker('Content Creator','content-creator','Create FAQ and help-center copy.'),
            worker('Operations Manager','operations-manager','Build triage workflow and reporting cadence.'),
            worker('Evidence Collector','evidence-collector','Collect public support-page gaps.')
        ],
        'next': 'Create support checklist, top-25 FAQ template, triage tree, escalation policy, canned responses, and weekly report template.'
    },
    {
        'name': 'AI Search Visibility & LLM Source-Map Retrofit Snapshot',
        'score_total': 72,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 10},
        'fit': 'Fresh evidence from Adobe confirms AI search is shifting from rank-only SEO to citation accuracy, structured/extractable facts, credibility signals, and brand representation. Still viable, but avoid citation/ranking guarantees.',
        'icp': 'Local service businesses and small B2B firms with thin service pages, weak FAQs, unclear proof, no source map, and no AI-readable guidance.',
        'offer': 'Free 5-point AI Search Snapshot; $299-$799 retrofit plan; $300-$900/mo refresh/reporting retainer.',
        'stack': ['public website review', 'local templates', 'manual scoring', 'no paid tools', 'no form submissions', 'no ranking/citation guarantees'],
        'workers': [
            worker('AI Citation Strategist','ai-citation-strategist','Score answerability and source clarity.'),
            worker('AEO Foundations Architect','aeo-foundations-architect','Score llms.txt/source-map/crawler guidance readiness.'),
            worker('SEO Specialist','seo-specialist','Review crawlability and page hygiene.'),
            worker('Content Creator','content-creator','Draft answer capsules and FAQs.'),
            worker('Evidence Collector','evidence-collector','Collect public evidence snippets.')
        ],
        'next': 'Add three public-site samples and one before/after source-map example.'
    },
    {
        'name': 'Invoice & AP Automation Readiness Audit',
        'score_total': 71,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 8, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 10},
        'fit': 'Docs-only admin angle. AP automation fit depends on invoice volume, approval complexity, payment needs, accounting systems, and exception handling; at $0 MRR sell readiness maps only.',
        'icp': 'Small firms with manual invoice intake, owner approvals, email/PDF invoices, unclear approval limits, duplicate-payment worries, and no AP workflow documentation.',
        'offer': 'Free Invoice Bottleneck Checklist; $399-$899 AP Automation Readiness Audit; future retainer only after human-approved tool/channel selection.',
        'stack': ['local worksheets', 'public AP tool comparisons', 'client process notes after sale', 'no bank/accounting login', 'no payments', 'no paid AP tools'],
        'workers': [
            worker('Accounts Payable Agent','accounts-payable-agent','Map AP intake, approval, exception, and payment-handoff workflows.'),
            worker('Operations Manager','operations-manager','Design approval routes and SOPs.'),
            worker('Pricing Analyst','pricing-analyst','Build savings/ROI calculator.'),
            worker('Data Privacy Officer','data-privacy-officer','Define invoice/vendor-data boundaries.'),
            worker('Document Generator','document-generator','Package workflow map and readiness report.')
        ],
        'next': 'Draft invoice-flow worksheet, approval matrix, data-field checklist, exception rules, duplicate-risk checklist, and ROI calculator.'
    },
    {
        'name': 'Employee AI Training & Prompt SOP Workshop',
        'score_total': 70,
        'scores': {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 8, 'margin': 10, 'recurring_revenue_potential': 7, 'fulfillment_complexity': 9, 'lead_acquisition_difficulty': 8, 'fit_with_agency_agents': 10},
        'fit': 'Useful upsell after policy/readiness. Staff need role-safe prompts, prompt logs, review workflows, and manager scorecards, but it is more likely to close after the governance pain is established.',
        'icp': 'SMB owners who know staff use AI but need safe repeatable workflows for writing, support, research, proposals, HR/admin, marketing, and operations.',
        'offer': 'Free AI Skills Gap Self-Assessment; $399-$999 Prompt SOP Workshop; $300-$900/mo prompt-library refresh and office-hours retainer.',
        'stack': ['public free training resources', 'local Markdown/PPT/CSV templates', 'role-based exercises', 'no paid course platform', 'no client data collection'],
        'workers': [
            worker('Corporate Training Designer','corporate-training-designer','Build workshop agenda and exercises.'),
            worker('Prompt Engineer','prompt-engineer','Draft role-safe prompts and testing notes.'),
            worker('Automation Governance Architect','automation-governance-architect','Turn prompt use into approval gates and governance SOPs.'),
            worker('Data Privacy Officer','data-privacy-officer','Embed sensitive-information guardrails.'),
            worker('Document Generator','document-generator','Package deck, handouts, and logs.')
        ],
        'next': 'Draft one-hour workshop outline, 20 role-safe prompts, prompt review checklist, prompt log, and manager scorecard.'
    }
]

opportunities.sort(key=lambda x: (-x['score_total'], x['name']))
for i, opp in enumerate(opportunities, 1):
    opp['rank'] = i
    opp['score_average'] = round(opp['score_total'] / 8, 2)

scored = {
    'last_updated': TS,
    'revenue': {
        'mrr': mrr,
        'sources_checked': [str(GAME_STATE), '/root/ai-holding-company/businesses/**/*revenue*'],
        'revenue_files_found': [str(p) for p in revenue_files],
        'evidence': f'RPG Revenue Vault monthlyRevenue is {mrr}; {len(revenue_files)} business revenue files were found under /root/ai-holding-company/businesses.',
        'stage_rule': '$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution'
    },
    'scoring_scale': '1-10 where 10 is best. For startup_cost, 10 means lowest cost. For fulfillment_complexity and lead_acquisition_difficulty, 10 means easiest.',
    'criteria': ['startup_cost','speed_to_first_revenue','automation_potential','margin','recurring_revenue_potential','fulfillment_complexity','lead_acquisition_difficulty','fit_with_agency_agents'],
    'sources': sources,
    'opportunities': opportunities,
    'selected_for_current_stage': ['Shadow AI Policy & Tool Inventory Sprint', 'Agentic AI Access & Human Approval Map Sprint'],
    'fresh_ideas_added_this_run': ['Agentic AI Access & Human Approval Map Sprint'],
    'safety_boundary': 'No emails, calls, form submissions, scans, client-system access, paid tools, marketplace/payment signups, cron scheduling, or spending were performed.'
}

quests = [
    {
        'id': f'research_shadow_ai_policy_inventory_{STAMP}',
        'name': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'title': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'desc': 'Create Shadow AI self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton. No scans, no client system access, no legal/security guarantees, no paid tools, and no outreach execution.',
        'reward': '+185 research XP', 'target': 6, 'current': 0, 'status': 'active',
        'assigned_agent': 'Data Privacy Officer', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Draft the six local templates; route legal/security decisions to human review.'
    },
    {
        'id': f'research_agentic_ai_access_approval_map_{STAMP}',
        'name': 'Draft Agentic AI Access & Approval Map',
        'title': 'Draft Agentic AI Access & Approval Map',
        'desc': 'Create autonomy levels, access/permission map, human-approval gate matrix, AI-agent risk register, audit-log checklist, and owner briefing. No system logins, no scans, no agent deployment, no client data handling from cron, and no outreach execution.',
        'reward': '+180 research XP', 'target': 6, 'current': 0, 'status': 'active',
        'assigned_agent': 'Automation Governance Architect', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Draft local governance templates only; do not connect tools or execute automations.'
    },
    {
        'id': f'research_ai_data_readiness_workflow_{STAMP}',
        'name': 'Draft AI Data Readiness & Workflow Prioritization Sprint',
        'title': 'Draft AI Data Readiness & Workflow Prioritization Sprint',
        'desc': 'Create workflow inventory, data-source checklist, AI use-case scoring matrix, data-risk register, KPI baseline sheet, and 30-day pilot roadmap. No system logins, no paid AI tools, no client data handling from cron, and no outreach execution.',
        'reward': '+170 research XP', 'target': 6, 'current': 0, 'status': 'queued',
        'assigned_agent': 'Workflow Optimizer', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Draft local worksheets only; do not connect to client systems or tools.'
    },
    {
        'id': f'research_ai_search_source_map_{STAMP}',
        'name': 'Refresh AI Search Source-Map Snapshot',
        'title': 'Refresh AI Search Source-Map Snapshot',
        'desc': 'Create a public-site AI Search/source-map snapshot focused on extractable facts, credible proof, FAQ depth, crawler guidance, and AI answer accuracy. No paid tools, no form submissions, no outreach, and no ranking/citation guarantees.',
        'reward': '+150 research XP', 'target': 4, 'current': 0, 'status': 'queued',
        'assigned_agent': 'AEO Foundations Architect', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Use public pages only; save local samples and improvement notes.'
    }
]

# Write JSON artifacts
(RESEARCH / 'ideas').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'reports').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'game').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'ideas/scored-opportunities.json').write_text(json.dumps(scored, indent=2) + '\n')
(RESEARCH / 'game/research_quests.json').write_text(json.dumps({'last_updated': TS, 'quests': quests}, indent=2) + '\n')

score_rows = '\n'.join(f"| {o['rank']} | {o['name']} | {o['score_total']}/80 | {'Selected' if o['name'] in scored['selected_for_current_stage'] else 'Runner-up'} |" for o in opportunities)
backlog = f"""# Business Research Backlog

Last updated: {TS}
Revenue stage: ${mrr} MRR from RPG Revenue Vault; {'no business revenue files found' if not revenue_files else str(len(revenue_files)) + ' revenue files found'}.
Rule applied: $0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution.

## Current best opportunity: Shadow AI Policy & Tool Inventory Sprint

Market: SMBs whose employees already use ChatGPT, Copilot, Claude, browser agents, and embedded AI without a written policy, tool inventory, sensitive-data rules, or human-review workflow. Positioning: fast, practical AI policy and Shadow AI inventory sprint; not legal advice, cybersecurity certification, penetration testing, managed security, or AI software implementation.

Offer: free 12-question Shadow AI Risk Self-Check; $499-$1,200 sprint; $500-$1,500/mo quarterly refresh/training/evidence-log retainer after first sale. Exclusions: no scans, no credential access, no legal/security guarantees, no paid tooling before revenue, no outbound execution.

Why now / sources:
- SBA says small businesses can use AI to do more with less, but should start small, avoid putting sensitive/proprietary information into tools, and have another person review AI products.
- GCS Technologies' 2026 SMB AI security-policy guide says many businesses adopted AI informally before rules existed and need approved-tool lists, data-handling rules, human review, tool request paths, and incident/exception handling.
- CRI's 2026 agentic-AI SMB guide adds urgency: agents can act, use systems, move data, and complete multi-step work, so access and approval boundaries are becoming a saleable readiness need.

Workers: Data Privacy Officer, Legal Compliance Checker, Security Architect, Compliance Auditor, Document Generator.

Next safe action: build the six-template Shadow AI pack locally. No outreach, scans, client system access, paid tools, or legal/security guarantees.

---

## Best fresh opportunity this run: Agentic AI Access & Human Approval Map Sprint

Why it moved up: CRI specifically says agentic AI has moved from buzzword to practical SMB tool because agents can plan tasks, use software, and complete projects with minimal oversight. That creates a clean $0-MRR docs-only offer: map which agent actions are allowed, blocked, or human-approved before the business deploys any agent automation.

Offer: free Agent Autonomy Risk Scorecard; $599-$1,500 Agentic AI Access & Human Approval Map Sprint; $750-$1,750/mo governance refresh/evidence-log retainer after first sale.

Workers: Automation Governance Architect, Agentic Identity & Trust Architect, Security Architect, Data Privacy Officer, Workflow Architect, Document Generator.

Next safe action: draft autonomy levels, access/permission map, human-approval gate matrix, AI-agent risk register, audit-log checklist, and owner briefing locally.

---

## Keep active: SMB AI Data Readiness & Workflow Prioritization Sprint

SMB owners want AI but need help choosing workflows, data sources, privacy boundaries, and measurable ROI before using paid tools or accessing systems. Offer: $499-$1,200 sprint plus $750-$1,500/mo KPI/evidence-log retainer. Workers: Operations Manager, Workflow Optimizer, Data Consolidation Agent, Data Privacy Officer, Analytics Reporter, Document Generator.

---

## Keep active: AI Search Visibility & LLM Source-Map Retrofit Snapshot

Adobe's 2026 SEO guidance reinforces that AI search rewards extractable facts, credible sources, structured content, citation accuracy, and brand representation. Keep it as a public-site snapshot offer only: no ranking or citation guarantees. Workers: AI Citation Strategist, AEO Foundations Architect, SEO Specialist, Content Creator, Evidence Collector.

---

## Other scored opportunities
- SMB AI Tool Stack Rationalization Sprint: tool inventory, duplicate-cost worksheet, workflow priority matrix, approved-tool decision guide.
- Customer Support KB & AI Triage Readiness Sprint: FAQ structure, triage tree, escalation policy, canned-response pack.
- Invoice & AP Automation Readiness Audit: workflow maps, approval matrix, exception rules, duplicate-risk checks, ROI calculator only.
- Employee AI Training & Prompt SOP Workshop: role-safe prompts, prompt log, review checklist, manager scorecard.

## Scoreboard

| Rank | Idea | Score | Stage fit |
|---:|---|---:|---|
{score_rows}
"""
(RESEARCH / 'ideas/backlog.md').write_text(backlog)

latest = f"""# Business Research Agent Latest Report

Updated: {TS}
Revenue stage: ${mrr} MRR, so only zero-cost/no-account/manual-review opportunities are allowed.

## Best idea now
**Shadow AI Policy & Tool Inventory Sprint** remains the best $0-MRR business.

Why: current sources reinforce that SMBs are already using AI, but need visible approved-tool lists, data-handling rules, human review, request/exception paths, and simple policy artifacts. This can be fulfilled with local templates and interviews only.

Needed workers: Data Privacy Officer, Legal Compliance Checker, Security Architect, Compliance Auditor, Document Generator.

Next safe action: build the six-template Shadow AI pack locally: self-check, tool inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton.

## Best fresh idea added
**Agentic AI Access & Human Approval Map Sprint**.

Why: CRI's 2026 SMB guidance says agentic AI can plan, use software, interact with systems, and complete multi-step work with minimal oversight, which creates new access, data-exposure, cybersecurity, and human-oversight risk. This is a strong docs-only readiness service before any client deploys agent automations.

Needed workers: Automation Governance Architect, Agentic Identity & Trust Architect, Security Architect, Data Privacy Officer, Workflow Architect, Document Generator.

Next safe action: draft autonomy levels, access/permission map, human-approval gate matrix, AI-agent risk register, audit-log checklist, and owner briefing locally.

## Safety boundary
No emails, calls, form submissions, scans, client-system access, paid tools, marketplace/payment signups, cron scheduling, or spending were performed.

## Artifacts updated
- `/root/ai-holding-company/business-research-agent/ideas/backlog.md`
- `/root/ai-holding-company/business-research-agent/ideas/scored-opportunities.json`
- `/root/ai-holding-company/business-research-agent/reports/latest.md`
- `/root/ai-holding-company/business-research-agent/game/research_quests.json`
- RPG game state received safe research quests and a research_update event.
"""
(RESEARCH / 'reports/latest.md').write_text(latest)

# Patch game state non-destructively: append top two quests if missing, update Business Research Agent, append event.
existing_quest_ids = {q.get('id') for q in game_state.get('quests', [])}
for q in quests[:2]:
    if q['id'] not in existing_quest_ids:
        game_state.setdefault('quests', []).append(q)

for agent in game_state.get('agents', []):
    if agent.get('name') == 'Business Research Agent':
        agent['status'] = 'working'
        agent['current_task'] = 'Confirmed Shadow AI Policy as best $0-MRR opportunity; added Agentic AI Access & Human Approval Map as best fresh opportunity. No outreach or spend.'
        agent['last_seen'] = TS
        agent['last_message'] = 'Best idea remains Shadow AI Policy & Tool Inventory. Fresh add: Agentic AI Access & Human Approval Map Sprint.'
        break

game_state['timestamp'] = TS
game_state.setdefault('events', []).append({
    'timestamp': TS,
    'type': 'research_update',
    'agent': 'Business Research Agent',
    'message': 'Confirmed Shadow AI Policy & Tool Inventory Sprint as best $0-MRR opportunity; added Agentic AI Access & Human Approval Map as fresh safe research. Safe quests only; no outreach or spend.',
    'source': 'business_research_agent'
})
GAME_STATE.write_text(json.dumps(game_state, indent=2) + '\n')

print(json.dumps({
    'updated': TS,
    'mrr': mrr,
    'opportunity_count': len(opportunities),
    'top': opportunities[0]['name'],
    'fresh': 'Agentic AI Access & Human Approval Map Sprint',
    'visible_quests_added': [q['id'] for q in quests[:2]],
    'worker_paths_missing': [w['path'] for o in opportunities for w in o['workers'] if not w['exists']]
}, indent=2))
