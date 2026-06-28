#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('/root/ai-holding-company')
RESEARCH = ROOT / 'business-research-agent'
GAME_STATE = ROOT / 'rpg-command-center/engine/public/game_state.json'
AGENTS = Path('/root/agency-agents/integrations/codex/agents')
TS = '2026-06-27T04:38:07Z'

for p in [RESEARCH/'ideas', RESEARCH/'reports', RESEARCH/'game']:
    p.mkdir(parents=True, exist_ok=True)

def worker(role, slug, responsibility):
    path = AGENTS / f'{slug}.toml'
    return {'role': role, 'path': str(path), 'responsibility': responsibility, 'exists': path.exists()}

opportunities = [
    {
        'name': 'Shadow AI Policy & Tool Inventory Sprint',
        'score_total': 78,
        'scores': {'startup_cost':10,'speed_to_first_revenue':10,'automation_potential':9,'margin':10,'recurring_revenue_potential':10,'fulfillment_complexity':9,'lead_acquisition_difficulty':10,'fit_with_agency_agents':10},
        'fit': 'Still the strongest $0-MRR service. Public guidance confirms SMBs can benefit from AI but must manage review, ethics, security, and data risks. First deliverable is local docs/interviews only: no paid tools, scans, credentials, legal/security guarantees, or outreach execution.',
        'icp': '5-50 employee SMBs using ChatGPT, Copilot, Claude, embedded AI, or browser agents without a written AI-use policy, inventory, sensitive-data rules, or human-review workflow.',
        'offer': 'Free 12-question Shadow AI Risk Self-Check; $499-$1,200 AI Policy & Tool Inventory Sprint; $500-$1,500/mo quarterly refresh/training/evidence-log retainer after first sale.',
        'stack': ['SBA/public AI risk guidance','local Markdown/CSV templates','manual interview worksheet','manual review','no paid SaaS','no client credentials'],
        'workers': [
            worker('Data Privacy Officer','data-privacy-officer','Define sensitive-data categories, retention boundaries, and privacy-safe AI-use questions.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep wording conservative and route legal decisions to qualified humans.'),
            worker('Security Architect','security-architect','Translate Shadow AI risks into practical SMB control checklists.'),
            worker('Compliance Auditor','compliance-auditor','Create recurring evidence logs and review checklists.'),
            worker('Document Generator','document-generator','Package self-checks, matrices, and owner briefing templates.'),
        ],
        'next': 'Build self-check, tool inventory CSV, approved/prohibited matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton.',
    },
    {
        'name': 'SMB AI Data Readiness & Workflow Prioritization Sprint',
        'score_total': 76,
        'scores': {'startup_cost':10,'speed_to_first_revenue':9,'automation_potential':10,'margin':9,'recurring_revenue_potential':10,'fulfillment_complexity':9,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'fit': 'Best fresh idea this run. ECI reports SMBs are optimistic but cautious: barriers include lack of expertise, data readiness/security concerns, uncertainty about where to start, and difficulty tying AI to measurable results. This is a $0-MRR docs-only readiness sprint before any tool implementation.',
        'icp': 'Manufacturing, field service, construction, distribution, local services, and professional-service SMBs that want AI for reporting, operations, support, or marketing but have messy data and no prioritized use-case roadmap.',
        'offer': 'Free AI Workflow Readiness Scorecard; $499-$1,200 Data Readiness & Workflow Prioritization Sprint; $750-$1,500/mo KPI/evidence-log refresh retainer after first sale.',
        'stack': ['public AI-readiness guidance','client-provided workflow notes after sale','local CSV/Markdown worksheets','manual use-case scoring','no system logins','no paid AI tools'],
        'workers': [
            worker('Operations Manager','operations-manager','Map workflows, bottlenecks, handoffs, and owner time sinks.'),
            worker('Workflow Optimizer','workflow-optimizer','Prioritize high-ROI, low-risk automation candidates.'),
            worker('Data Consolidation Agent','data-consolidation-agent','Define data-source inventory fields and data-quality checks without accessing systems.'),
            worker('Data Privacy Officer','data-privacy-officer','Flag sensitive-data/security constraints before AI use.'),
            worker('Analytics Reporter','analytics-reporter','Create KPI baseline and measurable-results scorecard.'),
            worker('Document Generator','document-generator','Package roadmap, worksheets, and executive brief.'),
        ],
        'next': 'Draft workflow inventory, data-source checklist, AI use-case scoring matrix, data-risk register, KPI baseline sheet, and 30-day pilot roadmap.',
    },
    {
        'name': 'SMB AI Tool Stack Rationalization Sprint',
        'score_total': 75,
        'scores': {'startup_cost':10,'speed_to_first_revenue':9,'automation_potential':9,'margin':9,'recurring_revenue_potential':9,'fulfillment_complexity':9,'lead_acquisition_difficulty':10,'fit_with_agency_agents':10},
        'fit': 'Strong runner-up and natural sibling to Shadow AI. SMBs using several AI/productivity tools need ownership, cost visibility, workflow fit, and approved-tool decision rules; no-login inventory/roadmap can be fulfilled at $0 MRR.',
        'icp': 'SMBs using multiple AI/productivity tools across marketing, admin, support, sales, and operations but lacking ownership, cost visibility, workflow mapping, or adoption priorities.',
        'offer': 'Free AI Tool Sprawl Checklist; $399-$899 Tool Stack Rationalization Sprint; $500-$1,500/mo implementation governance after approved tools/channels exist.',
        'stack': ['client-provided tool list after sale','public tool docs','local CSV/Markdown worksheets','manual workflow mapping','no SaaS login','no paid implementation'],
        'workers': [
            worker('Tool Evaluator','tool-evaluator','Compare tools, workflow fit, duplicate spend, and no/low-cost alternatives.'),
            worker('Operations Manager','operations-manager','Map workflows, bottlenecks, and owner time savings.'),
            worker('Pricing Analyst','pricing-analyst','Estimate monthly tool spend and consolidation ROI.'),
            worker('Data Privacy Officer','data-privacy-officer','Flag sensitive-data and vendor-review concerns.'),
            worker('Document Generator','document-generator','Package inventory, roadmap, and owner briefing.'),
        ],
        'next': 'Draft tool-inventory CSV, duplicate-cost worksheet, workflow priority matrix, approved-tool decision guide, and 30-day adoption plan.',
    },
    {
        'name': 'Customer Support Knowledge-Base & AI Triage Readiness Sprint',
        'score_total': 74,
        'scores': {'startup_cost':10,'speed_to_first_revenue':9,'automation_potential':9,'margin':9,'recurring_revenue_potential':9,'fulfillment_complexity':8,'lead_acquisition_difficulty':10,'fit_with_agency_agents':10},
        'fit': 'Strong zero-cost readiness offer. SBA highlights AI customer-service use cases, while SMBs still need FAQ structure, routing, escalation, transparency, training, and measurement before chatbot deployment.',
        'icp': 'Small SaaS, ecommerce, appointment businesses, clinics, agencies, and local-service teams with repeated questions, inconsistent replies, weak FAQ pages, and no escalation rules.',
        'offer': 'Free Support AI-Readiness Checklist; $399-$899 KB/Triage Sprint; $500-$1,200/mo KB refresh/reporting retainer.',
        'stack': ['public FAQ/support-page review','client docs after sale','local Markdown/CSV templates','no helpdesk login','no chatbot claims'],
        'workers': [
            worker('Customer Success Manager','customer-success-manager','Define support outcomes, SLA rules, and customer-success reporting.'),
            worker('Support Responder','support-responder','Draft canned replies and escalation language.'),
            worker('Content Creator','content-creator','Create FAQ and help-center copy.'),
            worker('Operations Manager','operations-manager','Build triage workflow and reporting cadence.'),
            worker('Evidence Collector','evidence-collector','Collect public support-page gaps.'),
        ],
        'next': 'Create support checklist, top-25 FAQ template, triage tree, escalation policy, canned responses, and weekly report template.',
    },
    {
        'name': 'Employee AI Training & Prompt SOP Workshop',
        'score_total': 73,
        'scores': {'startup_cost':10,'speed_to_first_revenue':9,'automation_potential':8,'margin':10,'recurring_revenue_potential':8,'fulfillment_complexity':9,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'fit': 'Natural upsell after policy/readiness. SBA recommends human review and ethical/secure use; staff need role-safe prompts, prompt logs, review workflows, and manager scorecards.',
        'icp': 'SMB owners who know staff use AI but need safe repeatable workflows for writing, support, research, proposals, HR/admin, marketing, and operations.',
        'offer': 'Free AI Skills Gap Self-Assessment; $399-$999 Prompt SOP Workshop; $300-$900/mo prompt-library refresh and office-hours retainer.',
        'stack': ['public free training resources','local Markdown/PPT/CSV templates','role-based exercises','no paid course platform','no client data collection'],
        'workers': [
            worker('Corporate Training Designer','corporate-training-designer','Build workshop agenda and exercises.'),
            worker('Automation Governance Architect','automation-governance-architect','Turn prompt use into approval gates and governance SOPs.'),
            worker('Data Privacy Officer','data-privacy-officer','Embed sensitive-information guardrails.'),
            worker('Document Generator','document-generator','Package deck, handouts, and logs.'),
            worker('Business Strategist','business-strategist','Tie training outcomes to business workflows and owner priorities.'),
        ],
        'next': 'Draft one-hour workshop outline, 20 role-safe prompts, prompt review checklist, prompt log, and manager scorecard.',
    },
    {
        'name': 'Invoice & AP Automation Readiness Audit',
        'score_total': 71,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':8,'fulfillment_complexity':8,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'fit': 'Docs-only admin angle. AP automation fit depends on invoice volume, approval complexity, payment needs, accounting systems, and exception handling; at $0 MRR sell readiness maps only.',
        'icp': 'Small firms with manual invoice intake, owner approvals, email/PDF invoices, unclear approval limits, duplicate-payment worries, and no AP workflow documentation.',
        'offer': 'Free Invoice Bottleneck Checklist; $399-$899 AP Automation Readiness Audit; future retainer only after human-approved tool/channel selection.',
        'stack': ['local worksheets','public AP tool comparisons','client process notes after sale','no bank/accounting login','no payments','no paid AP tools'],
        'workers': [
            worker('Accounts Payable Agent','accounts-payable-agent','Map AP intake, approval, exception, and payment-handoff workflows.'),
            worker('Operations Manager','operations-manager','Design approval routes and SOPs.'),
            worker('Pricing Analyst','pricing-analyst','Build savings/ROI calculator.'),
            worker('Data Privacy Officer','data-privacy-officer','Define invoice/vendor-data boundaries.'),
            worker('Document Generator','document-generator','Package workflow map and readiness report.'),
        ],
        'next': 'Draft invoice-flow worksheet, approval matrix, data-field checklist, exception rules, duplicate-risk checklist, and ROI calculator.',
    },
    {
        'name': 'AI Search Visibility & LLM Source-Map Retrofit Snapshot',
        'score_total': 70,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':9,'fulfillment_complexity':8,'lead_acquisition_difficulty':7,'fit_with_agency_agents':10},
        'fit': 'Already launched and useful, but current research favors AI governance/readiness offers. Continue samples without ranking/citation guarantees.',
        'icp': 'Local service businesses and small B2B firms with thin service pages, weak FAQs, unclear proof, no source map, and no AI-readable guidance.',
        'offer': 'Free 5-point AI Search Snapshot; $299-$799 retrofit plan; $300-$900/mo refresh/reporting retainer.',
        'stack': ['public website review','local templates','manual scoring','no paid tools','no form submissions','no ranking/citation guarantees'],
        'workers': [
            worker('AI Citation Strategist','ai-citation-strategist','Score answerability and source clarity.'),
            worker('SEO Specialist','seo-specialist','Review crawlability and page hygiene.'),
            worker('Content Creator','content-creator','Draft answer capsules and FAQs.'),
            worker('Evidence Collector','evidence-collector','Collect public evidence snippets.'),
        ],
        'next': 'Add three public-site samples and one before/after source-map example.',
    },
]
for i, o in enumerate(opportunities, 1):
    o['score_average'] = round(o['score_total']/8, 2)
    o['rank'] = i

sources = [
    {'name':'U.S. Small Business Administration - AI for small business','url':'https://www.sba.gov/business-guide/manage-your-business/ai-small-business','note':'SBA says AI can help small businesses save time, reduce costs, automate repetitive tasks, create content, improve customer service, and make better decisions; it also recommends ethical/secure use and human review of AI-generated products.'},
    {'name':'ECI Software Solutions - AI Readiness Report for SMBs','url':'https://www.ecisolutions.com/resources/ebook/ai-readiness-report/','note':'Survey of 550+ SMB leaders: over 70% are positive on AI, but barriers include lack of expertise, data readiness/security concerns, uncertainty about where to start, and difficulty connecting AI to measurable results. Top use cases include data/reporting, content/marketing, and customer service.'},
    {'name':'Wolters Kluwer - Top small business ideas for 2026','url':'https://www.wolterskluwer.com/en/expert-insights/best-small-business-ideas','note':'2026 small-business trend roundup says AI is becoming table stakes and businesses need help implementing AI, cybersecurity, cloud tools, and digital systems; focused problem-solving businesses are favored.'},
    {'name':'Xero - Small business ideas that actually work in 2026','url':'https://www.xero.com/us/guides/small-business-ideas/','note':'Service-based/home-based businesses often require under $1,000 to start and can generate income quickly; digital products and templates can be prepared later but marketplace/payment setup remains blocked until approval.'},
    {'name':'Installed Agency Agents roster','url':'/root/agency-agents/integrations/codex/agents','note':'Existing roles were checked and mapped before inventing any custom worker roles.'},
]

scored = {
    'last_updated': TS,
    'revenue': {
        'mrr': 0,
        'sources_checked': [str(GAME_STATE), '/root/ai-holding-company/businesses/**/*revenue*'],
        'revenue_files_found': [],
        'evidence': 'RPG Revenue Vault monthlyRevenue is 0; no business revenue files were found under /root/ai-holding-company/businesses.',
        'stage_rule': '$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution'
    },
    'scoring_scale': '1-10 where 10 is best. For startup_cost, 10 means lowest cost. For fulfillment_complexity and lead_acquisition_difficulty, 10 means easiest.',
    'criteria': ['startup_cost','speed_to_first_revenue','automation_potential','margin','recurring_revenue_potential','fulfillment_complexity','lead_acquisition_difficulty','fit_with_agency_agents'],
    'sources': sources,
    'opportunities': opportunities,
    'selected_for_current_stage': ['Shadow AI Policy & Tool Inventory Sprint','SMB AI Data Readiness & Workflow Prioritization Sprint'],
    'fresh_ideas_added_this_run': ['SMB AI Data Readiness & Workflow Prioritization Sprint'],
    'safety_boundary': 'No emails, calls, form submissions, scans, client-system access, paid tools, marketplace/payment signups, or spending were performed.'
}
(RESEARCH/'ideas/scored-opportunities.json').write_text(json.dumps(scored, indent=2) + '\n')

score_rows = '\n'.join(f"| {o['rank']} | {o['name']} | {o['score_total']}/80 | {'Selected' if o['name'] in scored['selected_for_current_stage'] else 'Runner-up'} |" for o in opportunities)
backlog = f"""# Business Research Backlog

Last updated: {TS}
Revenue stage: $0 MRR from RPG Revenue Vault; no business revenue files found.
Rule applied: $0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution.

## Current best opportunity: Shadow AI Policy & Tool Inventory Sprint

Market: SMBs whose employees already use ChatGPT, Copilot, Claude, browser agents, and embedded AI without a written policy, tool inventory, sensitive-data rules, or human-review workflow. Positioning: fast, practical AI policy and Shadow AI inventory sprint; not legal advice, cybersecurity certification, penetration testing, managed security, or AI software implementation.

Offer: free 12-question Shadow AI Risk Self-Check; $499-$1,200 sprint; $500-$1,500/mo quarterly refresh/training/evidence-log retainer after first sale. Exclusions: no scans, no credential access, no legal/security guarantees, no paid tooling before revenue, no outbound execution.

Why now / sources:
- SBA says small businesses can use AI to save time, reduce costs, automate repetitive tasks, create content, make better decisions, and improve customer service — but should use AI ethically/securely and review AI-generated work.
- ECI's 550+ SMB leader AI Readiness Report says leaders are positive but blocked by lack of expertise, data readiness/security concerns, uncertainty about where to start, and lack of measurable results.
- Wolters Kluwer's 2026 small-business trend report says AI is becoming table stakes and SMBs need help implementing AI, cybersecurity, cloud tools, and digital systems.

Workers: Data Privacy Officer, Legal Compliance Checker, Security Architect, Compliance Auditor, Document Generator.

Next safe action: build the six-template Shadow AI pack locally. No outreach, scans, client system access, paid tools, or legal/security guarantees.

---

## Best fresh opportunity this run: SMB AI Data Readiness & Workflow Prioritization Sprint

Why it moved up: ECI's SMB readiness research points to the practical pain before implementation: leaders want AI but do not know where to start, whether their data is ready, how to protect data, or how to measure ROI. This can be sold as a no-login, docs-only workflow/data readiness sprint using interviews and worksheets after a sale.

Offer: free AI Workflow Readiness Scorecard; $499-$1,200 Data Readiness & Workflow Prioritization Sprint; $750-$1,500/mo KPI/evidence-log refresh retainer after first sale.

Workers: Operations Manager, Workflow Optimizer, Data Consolidation Agent, Data Privacy Officer, Analytics Reporter, Document Generator.

Next safe action: draft workflow inventory, data-source checklist, AI use-case scoring matrix, data-risk register, KPI baseline sheet, and 30-day pilot roadmap locally.

---

## Keep active: SMB AI Tool Stack Rationalization Sprint

SMBs using multiple AI/productivity tools need ownership, cost visibility, workflow fit, and approved-tool rules. Offer: free AI Tool Sprawl Checklist; $399-$899 sprint; $500-$1,500/mo implementation governance after first sale and approved tools/channels. Workers: Tool Evaluator, Operations Manager, Pricing Analyst, Data Privacy Officer, Document Generator.

---

## Keep active: Customer Support KB & AI Triage Readiness Sprint

SBA highlights AI customer-service use cases; ECI reports customer service as a major SMB AI use case. Teams still need KB structure, triage/routing rules, transparency, training, and measurement before chatbot deployment. Offer: $399-$899 sprint plus $500-$1,200/mo refresh/reporting retainer. Workers: Customer Success Manager, Support Responder, Content Creator, Operations Manager, Evidence Collector.

---

## Other scored opportunities
- Employee AI Training & Prompt SOP Workshop: role-safe prompts, prompt log, review checklist, manager scorecard.
- Invoice & AP Automation Readiness Audit: workflow maps, approval matrix, exception rules, duplicate-risk checks, ROI calculator only.
- AI Search Visibility & LLM Source-Map Retrofit Snapshot: continue public website samples; no ranking/citation guarantees.

## Scoreboard

| Rank | Idea | Score | Stage fit |
|---:|---|---:|---|
{score_rows}
"""
(RESEARCH/'ideas/backlog.md').write_text(backlog)

report = f"""# Business Research Agent Latest Report

Updated: {TS}
Revenue stage: $0 MRR, so only zero-cost/no-account/manual-review opportunities are allowed.

## Best idea now
**Shadow AI Policy & Tool Inventory Sprint** remains the best $0-MRR business.

Why: current sources reinforce the same pain — SMBs are using AI for efficiency, content, decisions, and customer service, but need ethical/security review, tool inventories, data rules, and human-review workflows. This can be fulfilled with local templates and interviews only.

Needed workers: Data Privacy Officer, Legal Compliance Checker, Security Architect, Compliance Auditor, Document Generator.

Next safe action: build the six-template Shadow AI pack locally: self-check, tool inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton.

## Best fresh idea added
**SMB AI Data Readiness & Workflow Prioritization Sprint**.

Why: ECI's SMB AI readiness data shows leaders are positive on AI but stuck on data readiness, data security, lack of expertise, where to start, and measurable ROI. This is a high-margin docs-only sprint before any implementation.

Needed workers: Operations Manager, Workflow Optimizer, Data Consolidation Agent, Data Privacy Officer, Analytics Reporter, Document Generator.

Next safe action: draft workflow inventory, data-source checklist, AI use-case scoring matrix, data-risk register, KPI baseline sheet, and 30-day pilot roadmap locally.

## Safety boundary
No emails, calls, form submissions, scans, client-system access, paid tools, marketplace/payment signups, or spending were performed.

## Artifacts updated
- `/root/ai-holding-company/business-research-agent/ideas/backlog.md`
- `/root/ai-holding-company/business-research-agent/ideas/scored-opportunities.json`
- `/root/ai-holding-company/business-research-agent/reports/latest.md`
- `/root/ai-holding-company/business-research-agent/game/research_quests.json`
- RPG game state received safe research quests and a research_update event.
"""
(RESEARCH/'reports/latest.md').write_text(report)

quests = [
    {
        'id': 'research_shadow_ai_policy_inventory_20260627_0438',
        'name': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'title': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'desc': 'Create Shadow AI self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton. No scans, no client system access, no legal/security guarantees, no paid tools, and no outreach execution.',
        'reward': '+180 research XP','target': 6,'current': 0,'status': 'active','assigned_agent': 'Data Privacy Officer','source': 'business_research_agent','updated_at': TS,
        'next_step': 'Draft the six local templates; route legal/security decisions to human review.'
    },
    {
        'id': 'research_ai_data_readiness_workflow_20260627_0438',
        'name': 'Draft AI Data Readiness & Workflow Prioritization Sprint',
        'title': 'Draft AI Data Readiness & Workflow Prioritization Sprint',
        'desc': 'Create workflow inventory, data-source checklist, AI use-case scoring matrix, data-risk register, KPI baseline sheet, and 30-day pilot roadmap. No system logins, no paid AI tools, no client data handling from cron, and no outreach execution.',
        'reward': '+170 research XP','target': 6,'current': 0,'status': 'active','assigned_agent': 'Workflow Optimizer','source': 'business_research_agent','updated_at': TS,
        'next_step': 'Draft local worksheets only; do not connect to client systems or tools.'
    },
    {
        'id': 'research_ai_tool_stack_rationalization_20260627_0438',
        'name': 'Draft SMB AI Tool Stack Rationalization Sprint',
        'title': 'Draft SMB AI Tool Stack Rationalization Sprint',
        'desc': 'Create AI tool inventory CSV, duplicate-cost worksheet, workflow priority matrix, approved-tool decision guide, and 30-day adoption roadmap. No SaaS logins, no paid tools, no client system access, no payment/marketplace setup, and no outbound execution.',
        'reward': '+165 research XP','target': 5,'current': 0,'status': 'queued','assigned_agent': 'Tool Evaluator','source': 'business_research_agent','updated_at': TS,
        'next_step': 'Draft local worksheets only; do not connect to client tools.'
    },
    {
        'id': 'research_support_kb_ai_triage_20260627_0438',
        'name': 'Draft Support KB & AI Triage Readiness Sprint',
        'title': 'Draft Support KB & AI Triage Readiness Sprint',
        'desc': 'Create support AI-readiness checklist, top-25 FAQ template, triage tree, escalation policy, canned-response pack, and sample weekly report. No helpdesk login, no chatbot setup, no paid tools, no client data handling, and no outbound execution.',
        'reward': '+150 research XP','target': 6,'current': 0,'status': 'queued','assigned_agent': 'Customer Success Manager','source': 'business_research_agent','updated_at': TS,
        'next_step': 'Draft local KB/triage templates from public support patterns only.'
    },
    {
        'id': 'research_employee_ai_training_prompt_sop_20260627_0438',
        'name': 'Draft Employee AI Training & Prompt SOP Workshop',
        'title': 'Draft Employee AI Training & Prompt SOP Workshop',
        'desc': 'Create one-hour AI training outline, 20 role-safe starter prompts, prompt log, data-safety rules, review checklist, and manager scorecard. No client data collection, no paid course platform, no outbound execution.',
        'reward': '+145 research XP','target': 6,'current': 0,'status': 'queued','assigned_agent': 'Corporate Training Designer','source': 'business_research_agent','updated_at': TS,
        'next_step': 'Draft local training assets as an upsell to policy/readiness sprints.'
    },
]
(RESEARCH/'game/research_quests.json').write_text(json.dumps({'last_updated': TS, 'quests': quests}, indent=2) + '\n')

# Non-destructively update game_state with the top two fresh visible quests and a research_update event.
state = json.loads(GAME_STATE.read_text())
existing_ids = {q.get('id') for q in state.get('quests', [])}
for q in quests[:2]:
    if q['id'] not in existing_ids:
        state.setdefault('quests', []).append(q)

for agent in state.get('agents', []):
    if agent.get('name') == 'Business Research Agent':
        agent['status'] = 'working'
        agent['current_task'] = 'Confirmed Shadow AI Policy as best $0-MRR opportunity; added AI Data Readiness & Workflow Prioritization as best fresh opportunity. No outreach or spend.'
        agent['last_seen'] = TS
        agent['last_message'] = 'Best idea remains Shadow AI Policy & Tool Inventory. Fresh add: SMB AI Data Readiness & Workflow Prioritization Sprint.'

state.setdefault('events', []).append({
    'timestamp': TS,
    'type': 'research_update',
    'agent': 'Business Research Agent',
    'message': 'Confirmed Shadow AI Policy & Tool Inventory Sprint as best $0-MRR opportunity; added SMB AI Data Readiness & Workflow Prioritization as fresh safe research. Safe quests only; no outreach or spend.',
    'source': 'business_research_agent'
})
state['timestamp'] = TS
GAME_STATE.write_text(json.dumps(state, indent=2) + '\n')

print('updated artifacts at', TS)
print('opportunities', len(opportunities), 'quests', len(quests))
print('visible quest ids', quests[0]['id'], quests[1]['id'])
print('all worker paths exist:', all(w['exists'] for o in opportunities for w in o['workers']))
