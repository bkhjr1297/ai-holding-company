#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/root/ai-holding-company')
RESEARCH = ROOT / 'business-research-agent'
IDEAS = RESEARCH / 'ideas'
REPORTS = RESEARCH / 'reports'
GAME = RESEARCH / 'game'
STATE_PATH = ROOT / 'rpg-command-center/engine/public/game_state.json'
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
DATE = NOW[:10].replace('-', '')
for p in [IDEAS, REPORTS, GAME]:
    p.mkdir(parents=True, exist_ok=True)

state = json.loads(STATE_PATH.read_text())
mrr = int(state.get('buildings', {}).get('revenue_vault', {}).get('monthlyRevenue', 0) or 0)
rev_files = sorted(str(p) for p in (ROOT / 'businesses').glob('**/*revenue*')) if (ROOT / 'businesses').exists() else []
stage_rule = '$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution' if mrr < 500 else 'Revenue above $500 MRR; allow low-cost tools only after explicit ROI and owner approval.'

sources = [
    {
        'name': 'CrowdStrike - State of SMB Cybersecurity Survey',
        'url': 'https://www.crowdstrike.com/en-us/resources/reports/state-of-smb-cybersecurity-survey/',
        'note': 'SMB leaders report high cyber-risk awareness but execution gaps: only 42% provide regular security training, only 47% of micro-businesses have a security plan, two-thirds say cost blocks security upgrades, and 70% rely on outside experts. Supports an affordable document/checklist security-readiness service.'
    },
    {
        'name': 'NSA / international partners - Careful Adoption of Agentic AI Services',
        'url': 'https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4475134/nsa-joins-the-asds-acsc-and-others-to-release-guidance-on-agentic-artificial-in/',
        'note': '2026 agentic-AI guidance highlights risks around over-privileged agents, insecure provisioning, unpredictable behavior, expanded attack surfaces, monitoring, accountability, and human oversight.'
    },
    {
        'name': 'Digital Applied - Agentic AI for Small Business: Integration Guide for 2026',
        'url': 'https://www.digitalapplied.com/blog/agentic-ai-small-business-integration-guide-2026',
        'note': 'Frames SMB agent adoption around semi-autonomous workflows, 90-day implementation, lead follow-up, invoice processing, support triage, and human approval for sensitive decisions. Useful demand signal for AI workflow-readiness and policy packages, but live integrations should wait until revenue.'
    },
    {
        'name': 'Inkfluence AI - 31 Trending Digital Products to Sell in 2026',
        'url': 'https://www.inkfluenceai.com/blog/best-digital-product-niches-2026',
        'note': 'Digital products remain low-cost with near-zero marginal cost; strongest categories include AI productivity guides, Notion/planner templates, AI-skills courses for non-technical professionals, and role-specific professional development. Good secondary/non-retainer option.'
    },
    {
        'name': 'Omnius - Best Answer Engine Optimization Agencies in 2026',
        'url': 'https://www.omnius.so/blog/best-answer-engine-optimization-agencies',
        'note': 'AEO is being packaged as a dedicated agency service around AI crawler access, LLMs.txt, AI mentions/citations, natural-language queries, and AI-answer benchmarking; small businesses can benefit.'
    },
    {
        'name': 'Installed Agency Agents roster',
        'url': '/root/agency-agents/integrations/codex/agents',
        'note': 'Verified local workers include security-architect, compliance-auditor, data-privacy-officer, legal-compliance-checker, document-generator, automation-governance-architect, operations-manager, ai-citation-strategist, seo-specialist, content-creator, evidence-collector, sales-outreach, pricing-analyst, and corporate-training-designer.'
    }
]

def opp(rank, name, scores, fit, icp, offer, workers, next_action, zero_cost=None):
    total = sum(scores.values())
    return {
        'rank': rank,
        'name': name,
        'score_total': total,
        'score_average': round(total / 8, 2),
        'scores': scores,
        'current_stage_fit': fit,
        'beachhead_icp': icp,
        'offer': offer,
        'zero_cost_stack': zero_cost or ['public research', 'local Markdown/CSV/JSON templates', 'manual review', 'no paid tools', 'no client credentials before sale', 'human approval for outreach'],
        'agent_workers': workers,
        'next_safe_action': next_action
    }

opportunities = [
    opp(1, 'SMB AI Agent Safety & Cyber Readiness Checklist',
        {'startup_cost': 10, 'speed_to_first_revenue': 9, 'automation_potential': 8, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 10},
        'Best fresh $0-MRR opportunity this run: current cybersecurity and agentic-AI guidance creates urgent SMB demand, and the first deliverable is a policy/checklist/risk-register package requiring no scans, software, credentials, or paid tooling.',
        '5-50 employee professional-service firms, agencies, clinics, local services, and B2B operators using ChatGPT/Copilot/browser agents without written AI rules, security basics, permission maps, or human approval gates.',
        'Free 10-question AI Agent Safety Self-Check; $399-$999 readiness package including AI-use policy, permission map, risk register, training checklist, incident/escalation plan, and human-approval workflow; $500-$1,500/mo quarterly governance/training retainer after first sale.',
        [
            {'role': 'Security Architect', 'path': '/root/agency-agents/integrations/codex/agents/security-architect.toml', 'responsibility': 'Translate cybersecurity and agentic-AI risks into practical SMB controls.'},
            {'role': 'Compliance Auditor', 'path': '/root/agency-agents/integrations/codex/agents/compliance-auditor.toml', 'responsibility': 'Turn controls into an audit-friendly checklist and evidence log.'},
            {'role': 'Data Privacy Officer', 'path': '/root/agency-agents/integrations/codex/agents/data-privacy-officer.toml', 'responsibility': 'Flag sensitive-data, retention, and tool-permission risks.'},
            {'role': 'Legal Compliance Checker', 'path': '/root/agency-agents/integrations/codex/agents/legal-compliance-checker.toml', 'responsibility': 'Keep claims conservative; route legal/security decisions to humans.'},
            {'role': 'Document Generator', 'path': '/root/agency-agents/integrations/codex/agents/document-generator.toml', 'responsibility': 'Assemble policy, self-check, risk register, and readiness report.'}
        ],
        'Build the self-check, one-page report, and risk-register templates locally. No client scans, no credential access, no legal/security guarantees.'),
    opp(2, 'AI Search Visibility & LLMs.txt Retrofit Snapshot',
        {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 9, 'fit_with_agency_agents': 10},
        'Still excellent at $0 MRR: public website review plus local deliverables; no paid GEO/AEO tools, no client credentials, and a clear retainer path. Already partially launched, so keep feeding samples and refinement rather than switching away.',
        'Local service businesses and small B2B firms with thin service pages, weak FAQs, unclear proof, and no AI-readable summary/canonical-source guide.',
        'Free 5-point AI Search/LLMs.txt Readiness Snapshot; $299-$799 retrofit plan with answer capsules, FAQ gaps, proof sections, internal-link recommendations, and draft llms.txt map; $300-$900/mo refresh/reporting retainer.',
        [
            {'role': 'AI Citation Strategist', 'path': '/root/agency-agents/integrations/codex/agents/ai-citation-strategist.toml', 'responsibility': 'Score answerability, source clarity, entity clarity, and AI-citation readiness.'},
            {'role': 'SEO Specialist', 'path': '/root/agency-agents/integrations/codex/agents/seo-specialist.toml', 'responsibility': 'Review crawlability, service intent, internal links, and page hygiene.'},
            {'role': 'Content Creator', 'path': '/root/agency-agents/integrations/codex/agents/content-creator.toml', 'responsibility': 'Draft answer capsules, FAQs, proof sections, and llms.txt page descriptions.'},
            {'role': 'Evidence Collector', 'path': '/root/agency-agents/integrations/codex/agents/evidence-collector.toml', 'responsibility': 'Collect public evidence snippets and before/after notes.'},
            {'role': 'Offer & Lead Gen Strategist', 'path': '/root/agency-agents/integrations/codex/agents/offer-lead-gen-strategist.toml', 'responsibility': 'Package the snapshot, pilot, and approval-only outreach queue.'}
        ],
        'Add 3 more public-site samples to the existing snapshot system and sharpen the retainer upsell; no outreach execution.'),
    opp(3, 'SMB Lead Follow-Up Agent Readiness Audit',
        {'startup_cost': 10, 'speed_to_first_revenue': 7, 'automation_potential': 9, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 7, 'lead_acquisition_difficulty': 8, 'fit_with_agency_agents': 9},
        'Digital Applied highlights lead follow-up/nurturing as a highest-ROI SMB agent workflow, but integrations can require paid tools and accounts. At $0 MRR, sell only the readiness audit, script library, approval workflow, and ROI plan.',
        'Owner-operated service businesses with slow web-form replies, manual CRM updates, no structured follow-up, and lost quote requests.',
        'Free lead-response gap checklist; $399-$999 follow-up readiness pack with intake questions, qualification rules, human-approval email/SMS scripts, CRM field map, and ROI model; implementation retainer only after revenue and approved tooling.',
        [
            {'role': 'Automation Governance Architect', 'path': '/root/agency-agents/integrations/codex/agents/automation-governance-architect.toml'},
            {'role': 'Operations Manager', 'path': '/root/agency-agents/integrations/codex/agents/operations-manager.toml'},
            {'role': 'Sales Outreach', 'path': '/root/agency-agents/integrations/codex/agents/sales-outreach.toml'},
            {'role': 'Customer Success Manager', 'path': '/root/agency-agents/integrations/codex/agents/customer-success-manager.toml'},
            {'role': 'Pricing Analyst', 'path': '/root/agency-agents/integrations/codex/agents/pricing-analyst.toml'}
        ],
        'Draft a lead-follow-up readiness worksheet and ROI calculator. Do not connect email, SMS, CRM, or automations yet.'),
    opp(4, 'Role-Specific AI Productivity Mini-Products',
        {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 9, 'margin': 10, 'recurring_revenue_potential': 5, 'fulfillment_complexity': 8, 'lead_acquisition_difficulty': 6, 'fit_with_agency_agents': 9},
        'Digital products are cheap and high-margin; AI productivity guides/templates for non-technical professionals are trending. Downside: less recurring revenue and marketplace competition, so use as a cash/lead-magnet side channel rather than core business.',
        'Non-technical professionals who need role-specific AI prompt packs, checklists, SOPs, and Notion/Markdown templates: realtors, recruiters, lawyers, consultants, and local-service owners.',
        '$9-$49 prompt/template packs; $49-$199 workshop-in-a-box; upsell to AI Safety or AI Workflow Readiness services. Start with Gumroad/Ko-fi/manual delivery only after channel approval; first build local assets.',
        [
            {'role': 'Content Creator', 'path': '/root/agency-agents/integrations/codex/agents/content-creator.toml'},
            {'role': 'Corporate Training Designer', 'path': '/root/agency-agents/integrations/codex/agents/corporate-training-designer.toml'},
            {'role': 'Document Generator', 'path': '/root/agency-agents/integrations/codex/agents/document-generator.toml'},
            {'role': 'UI Designer', 'path': '/root/agency-agents/integrations/codex/agents/ui-designer.toml'},
            {'role': 'Pricing Analyst', 'path': '/root/agency-agents/integrations/codex/agents/pricing-analyst.toml'}
        ],
        'Create one local sample pack, landing-page copy, and price ladder. Do not open paid marketplaces or buy design tools.'),
    opp(5, 'Missed-Call & AI Receptionist Readiness Audit',
        {'startup_cost': 10, 'speed_to_first_revenue': 8, 'automation_potential': 8, 'margin': 9, 'recurring_revenue_potential': 9, 'fulfillment_complexity': 7, 'lead_acquisition_difficulty': 8, 'fit_with_agency_agents': 8},
        'Demand remains strong, but live voice/telephony is paid and compliance-sensitive. Keep it document-only until there is revenue and a compliant phone path.',
        'Appointment-based local services with high missed-call risk: dental, med spas, towing, home services, auto repair, and clinics.',
        'Free public missed-call readiness snapshot; $299-$699 receptionist-readiness package with FAQ, intake script, triage tree, after-hours response plan; future $500-$1,500/mo implementation only after compliant phone stack exists.',
        [
            {'role': 'Customer Service', 'path': '/root/agency-agents/integrations/codex/agents/customer-service.toml'},
            {'role': 'Customer Success Manager', 'path': '/root/agency-agents/integrations/codex/agents/customer-success-manager.toml'},
            {'role': 'Content Creator', 'path': '/root/agency-agents/integrations/codex/agents/content-creator.toml'},
            {'role': 'Legal Compliance Checker', 'path': '/root/agency-agents/integrations/codex/agents/legal-compliance-checker.toml'}
        ],
        'Build a missed-call readiness worksheet and sample intake script; no calls, no AI voice, no telephony claims.'),
    opp(6, 'Google Business Profile Reputation Freshness Sprint',
        {'startup_cost': 10, 'speed_to_first_revenue': 7, 'automation_potential': 8, 'margin': 9, 'recurring_revenue_potential': 8, 'fulfillment_complexity': 7, 'lead_acquisition_difficulty': 6, 'fit_with_agency_agents': 9},
        'Public-profile diagnostics are zero-cost, but actual review response/profile work requires client permission and account access. Keep as a backup local-service offer.',
        'Local businesses with stale photos/posts, unanswered reviews/questions, weak service descriptions, and inconsistent public listing information.',
        'Free GBP freshness diagnostic; $199-$399 cleanup plan; $300-$750/mo review-response/profile freshness retainer after permission.',
        [
            {'role': 'AI Citation Strategist', 'path': '/root/agency-agents/integrations/codex/agents/ai-citation-strategist.toml'},
            {'role': 'Customer Success Manager', 'path': '/root/agency-agents/integrations/codex/agents/customer-success-manager.toml'},
            {'role': 'Evidence Collector', 'path': '/root/agency-agents/integrations/codex/agents/evidence-collector.toml'},
            {'role': 'Content Creator', 'path': '/root/agency-agents/integrations/codex/agents/content-creator.toml'}
        ],
        'Prepare public-profile diagnostic checklist only; no review scraping, fake reviews, profile edits, or account access.')
]

scored = {
    'last_updated': NOW,
    'revenue': {
        'mrr': mrr,
        'sources_checked': [str(STATE_PATH), '/root/ai-holding-company/businesses/**/*revenue*'],
        'revenue_files_found': rev_files,
        'evidence': f'RPG Revenue Vault monthlyRevenue is {mrr}; {len(rev_files)} business revenue files found.',
        'stage_rule': stage_rule
    },
    'scoring_scale': '1-10 where 10 is best. For startup_cost, 10 means lowest cost. For fulfillment_complexity and lead_acquisition_difficulty, 10 means easiest.',
    'criteria': ['startup_cost', 'speed_to_first_revenue', 'automation_potential', 'margin', 'recurring_revenue_potential', 'fulfillment_complexity', 'lead_acquisition_difficulty', 'fit_with_agency_agents'],
    'sources': sources,
    'opportunities': opportunities,
    'selected_for_current_stage': [opportunities[0]['name'], opportunities[1]['name']]
}
(IDEAS / 'scored-opportunities.json').write_text(json.dumps(scored, indent=2) + '\n')

score_rows = '\n'.join([f"| {o['rank']} | {o['name']} | {o['score_total']}/80 | {o['current_stage_fit'].split('.')[0]} |" for o in opportunities])
backlog = f"""# Business Research Backlog

Last updated: {NOW}
Revenue stage: ${mrr} MRR from RPG Revenue Vault; {len(rev_files)} business revenue files found.
Rule applied: {stage_rule}.

## Current best opportunity: SMB AI Agent Safety & Cyber Readiness Checklist

**Business identity**
- Market: small professional-service firms and owner-operated SMBs adopting ChatGPT, Copilot, browser agents, workflow agents, and AI automations without security/process maturity.
- Buyer pain: leaders know cyber/AI risk exists but lack the time, budget, policies, training, and permission controls to manage it.
- Positioning: practical, affordable AI-agent safety and cybersecurity readiness documentation; not penetration testing, legal advice, or managed security tooling.

**Offer**
- Free lead magnet: 10-question AI Agent Safety Self-Check.
- Paid pilot: $399-$999 readiness package: AI-use policy, permission map, risk register, employee training checklist, human-approval gates, and incident/escalation plan.
- Retainer: $500-$1,500/mo for quarterly governance refresh, staff training updates, tool inventory review, and evidence-log maintenance after first sale.
- Exclusions: no scans, no credential access, no legal/security guarantees, no compliance certification, no paid tooling before revenue.

**Why now / sources**
- CrowdStrike: 94% of SMB leaders say they know cyber threats, but only 42% provide regular training, 47% of micro-businesses have a security plan, and 70% rely on outside experts.
- NSA/international guidance: agentic AI introduces over-privileged agents, insecure provisioning, unpredictable behavior, expanded attack surfaces, and monitoring/accountability needs.
- Digital Applied: SMBs are adopting semi-autonomous AI workflows; human approval remains necessary for sensitive decisions.

**Agent workers found in /root/agency-agents**
- Security Architect: `/root/agency-agents/integrations/codex/agents/security-architect.toml`
- Compliance Auditor: `/root/agency-agents/integrations/codex/agents/compliance-auditor.toml`
- Data Privacy Officer: `/root/agency-agents/integrations/codex/agents/data-privacy-officer.toml`
- Legal Compliance Checker: `/root/agency-agents/integrations/codex/agents/legal-compliance-checker.toml`
- Document Generator: `/root/agency-agents/integrations/codex/agents/document-generator.toml`

**Next safe action**
Build the self-check, report template, and risk register locally. No outreach, scans, client system access, paid tools, or legal/security guarantees.

---

## Keep scaling: AI Search Visibility & LLMs.txt Retrofit Snapshot

This remains the strongest already-started zero-cost service. Keep producing public website samples and sharpen the monthly retainer. Do not claim ranking/citation guarantees.

**Workers:** AI Citation Strategist, SEO Specialist, Content Creator, Evidence Collector, Offer & Lead Gen Strategist.

**Next safe action:** score 3 more public websites and create a short before/after llms.txt/source-map example.

---

## Other scored opportunities

### SMB Lead Follow-Up Agent Readiness Audit
- Offer: free lead-response gap checklist; $399-$999 readiness pack; future implementation retainer after revenue/tool approval.
- Workers: Automation Governance Architect, Operations Manager, Sales Outreach, Customer Success Manager, Pricing Analyst.
- Safe next action: worksheet + ROI calculator only; no CRM/email/SMS connections.

### Role-Specific AI Productivity Mini-Products
- Offer: $9-$49 prompt/template packs; $49-$199 workshop-in-a-box; upsell to AI Safety or AI Workflow Readiness.
- Workers: Content Creator, Corporate Training Designer, Document Generator, UI Designer, Pricing Analyst.
- Safe next action: create one local sample pack and landing copy; no paid marketplace/tools.

### Missed-Call & AI Receptionist Readiness Audit
- Offer: $299-$699 document-only receptionist-readiness package; future implementation only after compliant phone stack.
- Workers: Customer Service, Customer Success Manager, Content Creator, Legal Compliance Checker.
- Safe next action: worksheet + intake script only; no calls or AI voice.

### Google Business Profile Reputation Freshness Sprint
- Offer: $199-$399 cleanup plan; $300-$750/mo retainer after permission.
- Workers: AI Citation Strategist, Customer Success Manager, Evidence Collector, Content Creator.
- Safe next action: public-profile diagnostic checklist only.

## Scoreboard

| Rank | Idea | Score | Stage fit |
|---:|---|---:|---|
{score_rows}
"""
(IDEAS / 'backlog.md').write_text(backlog)

quests = [
    {
        'id': f'research_smb_ai_agent_safety_{DATE}',
        'name': 'Build SMB AI Agent Safety Self-Check',
        'desc': 'Research quest: create a 10-question AI-agent safety and cyber-readiness self-check, one-page readiness report, and simple risk register using public guidance only. No scans, no client system access, no legal/security guarantees, no paid tools, and no outreach execution.',
        'reward': '+140 research XP',
        'target': 3,
        'current': 0,
        'status': 'active',
        'assigned_agent': 'Security Architect',
        'business_stage': f'${mrr} MRR / zero-cost only',
        'safe_next_action': 'Draft self-check, report, and risk-register templates locally; route legal/security decisions to human review.'
    },
    {
        'id': f'research_ai_search_llms_samples_{DATE}',
        'name': 'Add AI Search + LLMs.txt Sample Reports',
        'desc': 'Research quest: produce 3 more public-website AI Search/LLMs.txt readiness samples and a before/after source-map example. No outreach, no paid tools, no form submissions, no ranking guarantees.',
        'reward': '+120 research XP',
        'target': 3,
        'current': 0,
        'status': 'active',
        'assigned_agent': 'AI Citation Strategist',
        'business_stage': f'${mrr} MRR / zero-cost only',
        'safe_next_action': 'Use public pages only; save local samples and improvement notes.'
    },
    {
        'id': f'research_lead_followup_readiness_{DATE}',
        'name': 'Draft Lead Follow-Up Agent Readiness Worksheet',
        'desc': 'Research quest: create a worksheet and ROI calculator for SMB lead-response automation readiness. Do not connect CRM, email, SMS, calendar, or paid automation tools.',
        'reward': '+100 research XP',
        'target': 1,
        'current': 0,
        'status': 'queued',
        'assigned_agent': 'Automation Governance Architect',
        'business_stage': f'${mrr} MRR / zero-cost only',
        'safe_next_action': 'Build local templates only; no live integrations or outbound.'
    }
]
(GAME / 'research_quests.json').write_text(json.dumps(quests, indent=2) + '\n')

report = f"""# Business Research Agent — Latest Report

Updated: {NOW}

## Revenue check
- Current MRR: **${mrr}**.
- Evidence: RPG Revenue Vault monthlyRevenue is {mrr}; {len(rev_files)} business revenue files found under `/root/ai-holding-company/businesses`.
- Rule applied: **{stage_rule}**.

## Best idea now
**SMB AI Agent Safety & Cyber Readiness Checklist** — **73/80**

Why it wins:
- CrowdStrike demand signal: SMBs know cyber risk exists, but many lack training, security plans, budget, and execution; 70% rely on outside experts.
- 2026 agentic-AI guidance creates a timely pain: over-privileged agents, sensitive data, human approval, monitoring, and accountability.
- Zero-cost fulfillment: checklist, policy, risk register, and report templates only — no scans, credentials, paid tools, or legal/security guarantees.
- Strong agent fit: Security Architect, Compliance Auditor, Data Privacy Officer, Legal Compliance Checker, Document Generator.

## Runner-up / keep building
**AI Search Visibility & LLMs.txt Retrofit Snapshot** — **72/80**

Why it stays active:
- Already partially launched and still fits $0 MRR perfectly.
- Public-site review + local reports can create samples without paid tools or client access.
- Best workers: AI Citation Strategist, SEO Specialist, Content Creator, Evidence Collector, Offer & Lead Gen Strategist.

## Scored ideas
1. SMB AI Agent Safety & Cyber Readiness Checklist — 73/80
2. AI Search Visibility & LLMs.txt Retrofit Snapshot — 72/80
3. SMB Lead Follow-Up Agent Readiness Audit — 69/80
4. Missed-Call & AI Receptionist Readiness Audit — 67/80
5. Role-Specific AI Productivity Mini-Products — 65/80
6. Google Business Profile Reputation Freshness Sprint — 64/80

## Game-ready quests prepared
- Build SMB AI Agent Safety Self-Check — assigned to Security Architect.
- Add AI Search + LLMs.txt Sample Reports — assigned to AI Citation Strategist.
- Draft Lead Follow-Up Agent Readiness Worksheet — assigned to Automation Governance Architect.

## Next safe action
Build the SMB AI Agent Safety self-check/report/risk-register templates and add 3 public AI Search/LLMs.txt sample reports. Do **not** contact prospects, submit forms, access client systems, run scans, place calls, send emails, connect SaaS tools, or spend money.

## Artifacts updated
- `/root/ai-holding-company/business-research-agent/ideas/backlog.md`
- `/root/ai-holding-company/business-research-agent/ideas/scored-opportunities.json`
- `/root/ai-holding-company/business-research-agent/reports/latest.md`
- `/root/ai-holding-company/business-research-agent/game/research_quests.json`
- `/root/ai-holding-company/rpg-command-center/engine/public/game_state.json` updated non-destructively with research quests/status/event.
"""
(REPORTS / 'latest.md').write_text(report)

# Non-destructive game state update.
existing_quests = state.setdefault('quests', [])
quests_by_id = {q.get('id'): q for q in existing_quests if isinstance(q, dict)}
for q in quests[:2]:
    compact = {
        'id': q['id'],
        'name': q['name'],
        'title': q['name'],
        'desc': q['desc'],
        'reward': q['reward'],
        'target': q['target'],
        'current': q['current'],
        'status': q['status'],
        'assigned_agent': q['assigned_agent'],
        'source': 'business_research_agent',
        'updated_at': NOW,
        'next_step': q['safe_next_action']
    }
    if q['id'] in quests_by_id:
        quests_by_id[q['id']].update(compact)
    else:
        existing_quests.append(compact)

for agent in state.get('agents', []):
    if agent.get('name') == 'Business Research Agent':
        agent['status'] = 'working'
        agent['current_task'] = 'Queued SMB AI Agent Safety and AI Search/LLMs.txt sample research quests; no outreach or spend.'
        agent['last_seen'] = NOW
        agent['last_message'] = 'Best fresh $0-MRR idea: SMB AI Agent Safety & Cyber Readiness Checklist. Keep building AI Search/LLMs.txt samples.'
        break

state['timestamp'] = NOW
state.setdefault('events', []).append({
    'timestamp': NOW,
    'type': 'research_update',
    'agent': 'Business Research Agent',
    'message': 'Selected SMB AI Agent Safety & Cyber Readiness Checklist as the best fresh $0-MRR opportunity and kept AI Search/LLMs.txt Retrofit active. Queued safe research quests only; no outreach or spend.',
    'source': 'business_research_agent'
})
STATE_PATH.write_text(json.dumps(state, indent=2) + '\n')

for path in [IDEAS / 'scored-opportunities.json', GAME / 'research_quests.json', STATE_PATH]:
    json.loads(path.read_text())
print(json.dumps({
    'updated_at': NOW,
    'mrr': mrr,
    'selected': scored['selected_for_current_stage'],
    'quests_added_or_updated': [quests[0]['id'], quests[1]['id']],
    'artifacts': [str(IDEAS / 'backlog.md'), str(IDEAS / 'scored-opportunities.json'), str(REPORTS / 'latest.md'), str(GAME / 'research_quests.json'), str(STATE_PATH)]
}, indent=2))
