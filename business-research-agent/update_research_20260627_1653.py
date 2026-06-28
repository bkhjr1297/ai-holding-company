#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path('/root/ai-holding-company')
RESEARCH = ROOT / 'business-research-agent'
IDEAS = RESEARCH / 'ideas'
REPORTS = RESEARCH / 'reports'
GAME = RESEARCH / 'game'
STATE_PATH = ROOT / 'rpg-command-center/engine/public/game_state.json'
AGENTS = Path('/root/agency-agents/integrations/codex/agents')
TS = '2026-06-27T16:53:21Z'

IDEAS.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)
GAME.mkdir(parents=True, exist_ok=True)

state = json.loads(STATE_PATH.read_text())
mrr = int(state.get('buildings', {}).get('revenue_vault', {}).get('monthlyRevenue', 0) or 0)
revenue_files = [str(p) for p in (ROOT / 'businesses').glob('**/*revenue*')]

sources = [
    {
        'name': 'GCS Technologies - AI Security Policy Guide for Small Businesses (2026)',
        'url': 'https://www.gcstechnologies.com/ai-security-policy-guide/',
        'note': 'SMBs often adopted ChatGPT/Copilot/Claude informally before policy, IT approval, vendor review, or visibility; policies should cover approved tools, prohibited data, review, approvals, and incidents.'
    },
    {
        'name': 'Microsoft Security Blog - Active AI agents, observability, governance, security (2026)',
        'url': 'https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/',
        'note': 'Microsoft reports 80%+ of Fortune 500 use active AI agents and says agents need observability, governance, least privilege, owner accountability, and service-account-like controls.'
    },
    {
        'name': 'Miles IT - AEO & GEO Strategy Guide (2026)',
        'url': 'https://www.milesit.com/ai-search-optimization/',
        'note': 'AI search rewards direct answers, structured trustworthy content, citation-worthy proof, and SEO foundations; do not promise rankings or citations.'
    },
    {
        'name': 'Kittl - 25 Best Digital Products to Sell in 2026',
        'url': 'https://www.kittl.com/blogs/digital-products-to-sell-dsi/',
        'note': 'Digital products have no inventory/shipping, can be created once and sold repeatedly, but require niche focus and quality packaging because the market is crowded.'
    },
    {
        'name': 'InsightAgent - Best Selling Digital Products on Etsy (2026)',
        'url': 'https://www.insightagent.app/guides/best-selling-digital-products-etsy',
        'note': 'Printable/digital products can reach 85-95% margins; strongest categories include planners, business templates, educational worksheets, and bundles. Marketplace setup/payment remains a later approval step.'
    },
    {
        'name': 'Installed Agency Agents roster',
        'url': '/root/agency-agents/integrations/codex/agents',
        'note': 'Local worker personas checked before role assignment; no custom roles required this run.'
    }
]

def worker(role: str, slug: str, responsibility: str):
    path = AGENTS / f'{slug}.toml'
    return {'role': role, 'path': str(path), 'responsibility': responsibility, 'exists': path.exists()}

opportunities = [
    {
        'name': 'Shadow AI Policy & Tool Inventory Sprint',
        'scores': {'startup_cost':10,'speed_to_first_revenue':10,'automation_potential':9,'margin':10,'recurring_revenue_potential':10,'fulfillment_complexity':9,'lead_acquisition_difficulty':10,'fit_with_agency_agents':10},
        'fit': 'Best $0-MRR beachhead. SMBs are already using AI informally and need practical visibility, allowed/prohibited-use rules, sensitive-data boundaries, and human review before risk becomes an incident.',
        'icp': '5-50 employee SMBs using ChatGPT, Copilot, Claude, browser agents, embedded AI, or no-code automations without a written AI-use policy or tool inventory.',
        'offer': 'Free 12-question Shadow AI Risk Self-Check; $499-$1,200 AI Policy & Tool Inventory Sprint; $500-$1,500/mo quarterly refresh, staff training, and evidence-log retainer after first sale.',
        'stack': ['public AI/security guidance','local Markdown/CSV templates','manual interview worksheet','manual review','no paid SaaS','no client credentials'],
        'workers': [
            worker('Data Privacy Officer','data-privacy-officer','Define sensitive-data categories, retention boundaries, and privacy-safe AI-use questions.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep wording conservative and route legal decisions to qualified humans.'),
            worker('Security Architect','security-architect','Translate Shadow AI risks into practical SMB control checklists.'),
            worker('Compliance Auditor','compliance-auditor','Create recurring evidence logs and review checklists.'),
            worker('Document Generator','document-generator','Package self-checks, matrices, and owner briefing templates.'),
        ],
        'next': 'Build self-check, tool inventory CSV, approved/prohibited matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton.'
    },
    {
        'name': 'AI Agent Observability & Inventory Lite Sprint',
        'scores': {'startup_cost':10,'speed_to_first_revenue':9,'automation_potential':10,'margin':10,'recurring_revenue_potential':10,'fulfillment_complexity':9,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'fit': 'Best adjacent/fresh offer. As agents/custom GPTs/no-code automations spread, owners need a simple list of what exists, who owns it, what it can access, which actions need approval, and what evidence should be kept.',
        'icp': 'SMBs/agencies experimenting with Copilot agents, custom GPTs, browser agents, n8n/Zapier automations, AI support bots, or no-code agents without owner maps or audit evidence.',
        'offer': 'Free AI Agent Visibility Checklist; $599-$1,500 Observability & Inventory Lite Sprint; $750-$1,750/mo quarterly agent inventory/evidence-log refresh after first sale.',
        'stack': ['public Microsoft/GCS guidance','local agent-inventory CSV','service-account style ownership map','manual workflow interviews after sale','no system logins','no monitoring tools or scans'],
        'workers': [
            worker('Automation Governance Architect','automation-governance-architect','Define governance fields, approval gates, and safe operating rules for agent workflows.'),
            worker('Agentic Identity & Trust Architect','agentic-identity-trust-architect','Map agent identity, owner, delegated authority, and proof-of-action requirements.'),
            worker('Security Architect','security-architect','Apply least-privilege and visibility checks without performing scans.'),
            worker('Data Privacy Officer','data-privacy-officer','Map sensitive data boundaries and retention constraints.'),
            worker('Analytics Reporter','analytics-reporter','Design a simple inventory/evidence-log dashboard.'),
            worker('Document Generator','document-generator','Package the inventory, map, and executive brief.'),
        ],
        'next': 'Draft agent inventory CSV, owner/permission map, data-touch checklist, approval/rollback matrix, evidence-log template, and executive briefing locally.'
    },
    {
        'name': 'AI Governance Template Micro-Store Assets',
        'scores': {'startup_cost':10,'speed_to_first_revenue':7,'automation_potential':10,'margin':10,'recurring_revenue_potential':6,'fulfillment_complexity':10,'lead_acquisition_difficulty':6,'fit_with_agency_agents':10},
        'fit': 'Useful productized derivative of the service templates. Digital-products research shows high-margin template bundles work, but marketplace/payment setup requires approval; until then, create local assets and listing copy only.',
        'icp': 'Solo consultants, fractional ops leaders, SMB owners, and agencies needing editable AI policy, tool inventory, prompt log, approval matrix, and training templates.',
        'offer': 'Local bundle draft now; future $19-$79 template pack and $199-$499 customization add-on after Brian approves sales channel/payment setup.',
        'stack': ['local Markdown/DOCX/CSV templates','free design/export tooling','no marketplace account','no payment processor','no ad spend'],
        'workers': [
            worker('Document Generator','document-generator','Package polished templates and export-ready docs.'),
            worker('Content Creator','content-creator','Write listing copy and buyer instructions.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Add disclaimers and avoid legal-advice claims.'),
            worker('Prompt Engineer','prompt-engineer','Build prompt/SOP templates.'),
            worker('Pricing Analyst','pricing-analyst','Model bundle pricing and customization upsells.'),
        ],
        'next': 'Package template files and listing draft only; do not open Etsy/Gumroad/Shopify/payment accounts.'
    },
    {
        'name': 'AI Search Visibility & LLM Source-Map Retrofit Snapshot',
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':9,'fulfillment_complexity':8,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'fit': 'Still viable but now runner-up. AEO/GEO sources show demand for structured direct answers and citation-worthy content, but the offer must avoid ranking/citation guarantees.',
        'icp': 'Local service businesses and small B2B firms with thin service pages, weak FAQs, unclear proof, no source map, and no AI-readable guidance.',
        'offer': 'Free 5-point AI Search Snapshot; $299-$799 retrofit plan; $300-$900/mo refresh/reporting retainer.',
        'stack': ['public website review','local templates','manual scoring','no paid tools','no form submissions','no ranking/citation guarantees'],
        'workers': [
            worker('AI Citation Strategist','ai-citation-strategist','Score answerability and source clarity.'),
            worker('AEO Foundations Architect','aeo-foundations-architect','Score llms.txt/source-map/crawler guidance readiness.'),
            worker('SEO Specialist','seo-specialist','Review crawlability and page hygiene.'),
            worker('Content Creator','content-creator','Draft answer capsules and FAQs.'),
            worker('Evidence Collector','evidence-collector','Collect public evidence snippets.'),
        ],
        'next': 'Keep producing public-site samples and source-map examples, but prioritize Shadow AI for fastest close.'
    },
    {
        'name': 'Customer Support Knowledge-Base & AI Triage Readiness Sprint',
        'scores': {'startup_cost':10,'speed_to_first_revenue':9,'automation_potential':9,'margin':9,'recurring_revenue_potential':9,'fulfillment_complexity':8,'lead_acquisition_difficulty':10,'fit_with_agency_agents':10},
        'fit': 'Strong zero-cost service for businesses that want AI support later but first need FAQ structure, routing, escalation, transparency, training, and measurement.',
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
        'next': 'Create support checklist, top-25 FAQ template, triage tree, escalation policy, canned responses, and weekly report template.'
    },
    {
        'name': 'Employee AI Training & Prompt SOP Workshop',
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':8,'margin':10,'recurring_revenue_potential':7,'fulfillment_complexity':9,'lead_acquisition_difficulty':8,'fit_with_agency_agents':10},
        'fit': 'Good upsell after governance pain is established. Staff need role-safe prompts, prompt logs, review workflows, and manager scorecards.',
        'icp': 'SMB owners who know staff use AI but need safe repeatable workflows for writing, support, research, proposals, HR/admin, marketing, and operations.',
        'offer': 'Free AI Skills Gap Self-Assessment; $399-$999 Prompt SOP Workshop; $300-$900/mo prompt-library refresh and office-hours retainer.',
        'stack': ['public free training resources','local Markdown/PPT/CSV templates','role-based exercises','no paid course platform','no client data collection'],
        'workers': [
            worker('Corporate Training Designer','corporate-training-designer','Build workshop agenda and exercises.'),
            worker('Prompt Engineer','prompt-engineer','Draft role-safe prompts and testing notes.'),
            worker('Automation Governance Architect','automation-governance-architect','Turn prompt use into approval gates and governance SOPs.'),
            worker('Data Privacy Officer','data-privacy-officer','Embed sensitive-information guardrails.'),
            worker('Document Generator','document-generator','Package deck, handouts, and logs.'),
        ],
        'next': 'Draft one-hour workshop outline, 20 role-safe prompts, prompt review checklist, prompt log, and manager scorecard.'
    }
]

for item in opportunities:
    item['score_total'] = sum(item['scores'].values())
    item['score_average'] = round(item['score_total'] / len(item['scores']), 2)

opportunities.sort(key=lambda x: x['score_total'], reverse=True)
for i, item in enumerate(opportunities, 1):
    item['rank'] = i

scored = {
    'last_updated': TS,
    'revenue': {
        'mrr': mrr,
        'sources_checked': [str(STATE_PATH), '/root/ai-holding-company/businesses/**/*revenue*'],
        'revenue_files_found': revenue_files,
        'evidence': f'RPG Revenue Vault monthlyRevenue is {mrr}; {len(revenue_files)} business revenue files were found under /root/ai-holding-company/businesses.',
        'stage_rule': '$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution' if mrr < 500 else 'Higher revenue stage detected; still no spend/outreach in this cron run.'
    },
    'scoring_scale': '1-10 where 10 is best. For startup_cost, 10 means lowest cost. For fulfillment_complexity and lead_acquisition_difficulty, 10 means easiest.',
    'criteria': ['startup_cost','speed_to_first_revenue','automation_potential','margin','recurring_revenue_potential','fulfillment_complexity','lead_acquisition_difficulty','fit_with_agency_agents'],
    'sources': sources,
    'opportunities': opportunities,
    'selected_for_current_stage': [opportunities[0]['name'], opportunities[1]['name']],
    'fresh_ideas_added_this_run': ['AI Governance Template Micro-Store Assets'],
    'safety_boundary': 'No emails, calls, form submissions, scans, client-system access, paid tools, marketplace/payment signups, cron scheduling, or spending were performed.'
}

(IDEAS / 'scored-opportunities.json').write_text(json.dumps(scored, indent=2) + '\n')

backlog = f"""# Business Research Backlog

Last updated: {TS}
Revenue stage: ${mrr} MRR from RPG Revenue Vault; {len(revenue_files)} business revenue files found.
Rule applied: $0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution.

## Current best opportunity: Shadow AI Policy & Tool Inventory Sprint

Market: SMBs whose employees already use ChatGPT, Copilot, Claude, browser agents, and embedded AI without a written policy, tool inventory, sensitive-data rules, or human-review workflow. Positioning: fast, practical AI policy and Shadow AI inventory sprint; not legal advice, cybersecurity certification, penetration testing, managed security, or AI software implementation.

Offer: free 12-question Shadow AI Risk Self-Check; $499-$1,200 sprint; $500-$1,500/mo quarterly refresh/training/evidence-log retainer after first sale. Exclusions: no scans, no credential access, no legal/security guarantees, no paid tooling before revenue, no outbound execution.

Why now / sources:
- GCS Technologies says many SMBs did not formally decide to adopt AI; employees started using it before policies, approvals, or visibility existed.
- Microsoft says active agents are scaling faster than companies can observe/govern them, and agents should be treated like employees or service accounts with visibility, least privilege, and accountability.
- Digital-product research confirms governance templates can later become high-margin assets, but service-first remains better at $0 MRR because marketplace/payment setup needs approval.

Workers: Data Privacy Officer, Legal Compliance Checker, Security Architect, Compliance Auditor, Document Generator.

Next safe action: build the six-template Shadow AI pack locally. No outreach, scans, client system access, paid tools, marketplace setup, or legal/security guarantees.

---

## Best adjacent opportunity: AI Agent Observability & Inventory Lite Sprint

Why it stays high: Microsoft’s 2026 agent-risk framing creates a specific SMB service: list every AI agent/automation/custom GPT, assign an owner, map what data it touches, define what it can do, and create a light evidence log. This requires no logins, no scans, and no paid monitoring tools.

Offer: free AI Agent Visibility Checklist; $599-$1,500 Observability & Inventory Lite Sprint; $750-$1,750/mo quarterly agent inventory/evidence-log refresh after first sale.

Workers: Automation Governance Architect, Agentic Identity & Trust Architect, Security Architect, Data Privacy Officer, Analytics Reporter, Document Generator.

Next safe action: draft agent inventory CSV, owner/permission map, data-touch checklist, approval/rollback matrix, evidence-log template, and executive briefing locally.

---

## Fresh idea added this run: AI Governance Template Micro-Store Assets

Digital-product sources show templates, planners, business templates, and education assets can have 85-95% margins and no inventory/shipping. For Brian, the safe version is not opening a marketplace yet; it is packaging the Shadow AI/observability templates as local assets and listing copy that can become a $19-$79 template bundle later after a sales/payment channel is approved.

Workers: Document Generator, Content Creator, Legal Compliance Checker, Prompt Engineer, Pricing Analyst.

Next safe action: package template files and listing draft only; do not open Etsy/Gumroad/Shopify/payment accounts.

---

## Keep active: AI Search Visibility & LLM Source-Map Retrofit Snapshot

AEO/GEO guidance reinforces direct answers, structured credible content, and source-worthy proof. Keep it as a public-site snapshot offer only: no ranking or citation guarantees. Workers: AI Citation Strategist, AEO Foundations Architect, SEO Specialist, Content Creator, Evidence Collector.

---

## Other scored opportunities
- Customer Support KB & AI Triage Readiness Sprint: FAQ structure, triage tree, escalation policy, canned-response pack.
- Employee AI Training & Prompt SOP Workshop: role-safe prompts, prompt log, review checklist, manager scorecard.

## Scoreboard

| Rank | Idea | Score | Stage fit |
|---:|---|---:|---|
"""
for opp in opportunities:
    stage = 'Selected' if opp['rank'] <= 2 else ('Fresh asset' if opp['name'] == 'AI Governance Template Micro-Store Assets' else 'Runner-up')
    backlog += f"| {opp['rank']} | {opp['name']} | {opp['score_total']}/80 | {stage} |\n"
(IDEAS / 'backlog.md').write_text(backlog)

quests = [
    {
        'id': 'research_shadow_ai_policy_inventory_20260627_1653',
        'name': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'title': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'desc': 'Create Shadow AI self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton. No scans, no client system access, no legal/security guarantees, no paid tools, and no outreach execution.',
        'reward': '+190 research XP',
        'target': 6,
        'current': 0,
        'status': 'active',
        'assigned_agent': 'Data Privacy Officer',
        'source': 'business_research_agent',
        'updated_at': TS,
        'next_step': 'Draft the six local templates; route legal/security decisions to human review.'
    },
    {
        'id': 'research_ai_governance_template_micro_store_20260627_1653',
        'name': 'Package AI Governance Template Micro-Store Assets',
        'title': 'Package AI Governance Template Micro-Store Assets',
        'desc': 'Package Shadow AI/observability templates and listing copy for a future approved digital-product sales channel. Do not open marketplace accounts, payment accounts, ad accounts, or spend money.',
        'reward': '+120 research XP',
        'target': 5,
        'current': 0,
        'status': 'queued',
        'assigned_agent': 'Document Generator',
        'source': 'business_research_agent',
        'updated_at': TS,
        'next_step': 'Create local template bundle and listing draft only after service templates are proven.'
    }
]
(GAME / 'research_quests.json').write_text(json.dumps({'last_updated': TS, 'quests': quests}, indent=2) + '\n')

# Non-destructive game_state update: append one new quest if missing and update Business Research Agent status.
existing_ids = {q.get('id') for q in state.get('quests', [])}
quest_to_add = quests[1]
if quest_to_add['id'] not in existing_ids:
    state.setdefault('quests', []).append(quest_to_add)
for agent in state.get('agents', []):
    if agent.get('name') == 'Business Research Agent':
        agent['status'] = 'working'
        agent['current_task'] = 'Confirmed Shadow AI Policy as best $0-MRR opportunity; added AI Governance Template Micro-Store as a safe digital-product asset path. No outreach or spend.'
        agent['last_seen'] = TS
        agent['last_message'] = 'Best idea remains Shadow AI Policy & Tool Inventory. Fresh add: AI Governance Template Micro-Store assets, prepared locally only.'
state['timestamp'] = TS
state.setdefault('events', []).append({
    'timestamp': TS,
    'type': 'business_research_update',
    'agent': 'Business Research Agent',
    'message': 'Researched 2026 AI governance, AI search, and digital-product sources; selected Shadow AI Policy plus AI Agent Observability; queued local-only AI Governance Template Micro-Store asset quest.',
    'source': 'business_research_agent',
    'safety': 'No outreach, scans, signups, spend, or client-system access.'
})
STATE_PATH.write_text(json.dumps(state, indent=2) + '\n')

latest = f"""# Business Research Agent Report — {TS}

## Revenue check
- Current tracked MRR: ${mrr}
- Evidence: RPG Revenue Vault monthlyRevenue={mrr}; {len(revenue_files)} business revenue files found.
- Stage rule: $0-$500 MRR, so only zero-cost/no-account/local-first opportunities were selected.

## Best idea
**Shadow AI Policy & Tool Inventory Sprint** — $499-$1,200 setup + $500-$1,500/mo refresh/training/evidence-log retainer after first sale.

Why: current SMB guidance shows AI use often entered through employees before policy/approval/visibility existed. This is urgent, sellable remotely, high-margin, and can be fulfilled with local templates plus agent review only.

## Runner-up
**AI Agent Observability & Inventory Lite Sprint** — $599-$1,500 setup + $750-$1,750/mo quarterly refresh after first sale.

Why: Microsoft’s 2026 agent-risk framing says AI agents need observability, governance, owners, least privilege, and evidence logs. This is a natural upsell to Shadow AI policy.

## Fresh idea added
**AI Governance Template Micro-Store Assets** — prepare local template bundle/listing copy now; future marketplace/payment channel only after approval. Digital-product sources confirm high-margin template demand, but at $0 MRR we should not open accounts or spend.

## Agent workers needed
- Data Privacy Officer
- Legal Compliance Checker
- Security Architect
- Compliance Auditor
- Document Generator
- Automation Governance Architect
- Agentic Identity & Trust Architect
- Analytics Reporter
- Content Creator
- Prompt Engineer
- Pricing Analyst

All are existing Agency Agents; no custom role needed.

## Next safe action
Build the Shadow AI six-template pack locally: self-check, tool inventory CSV, approved/prohibited matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton. No outreach, scans, account signups, client access, or spend.

## Artifacts updated
- `business-research-agent/ideas/backlog.md`
- `business-research-agent/ideas/scored-opportunities.json`
- `business-research-agent/reports/latest.md`
- `business-research-agent/game/research_quests.json`
- RPG game state received non-destructive quest: `research_ai_governance_template_micro_store_20260627_1653`
"""
(REPORTS / 'latest.md').write_text(latest)

print(json.dumps({
    'updated': [str(IDEAS/'backlog.md'), str(IDEAS/'scored-opportunities.json'), str(REPORTS/'latest.md'), str(GAME/'research_quests.json'), str(STATE_PATH)],
    'mrr': mrr,
    'opportunities_scored': len(opportunities),
    'selected': scored['selected_for_current_stage'],
    'new_game_quest': quest_to_add['id'],
    'workers_missing': [w for opp in opportunities for w in opp['workers'] if not w['exists']]
}, indent=2))
