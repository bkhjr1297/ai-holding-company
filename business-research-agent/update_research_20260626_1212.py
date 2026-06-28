#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('/root/ai-holding-company')
RESEARCH = ROOT / 'business-research-agent'
IDEAS = RESEARCH / 'ideas'
REPORTS = RESEARCH / 'reports'
GAME = RESEARCH / 'game'
STATE_PATH = ROOT / 'rpg-command-center/engine/public/game_state.json'
UPDATED = '2026-06-26T12:12:23Z'

IDEAS.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)
GAME.mkdir(parents=True, exist_ok=True)

with STATE_PATH.open() as f:
    state = json.load(f)
current_mrr = int(state.get('buildings', {}).get('revenue_vault', {}).get('monthlyRevenue') or 0)
revenue_files = []
for p in (ROOT / 'businesses').glob('**/*revenue*'):
    if p.is_file():
        revenue_files.append(str(p))

stage_rule = '$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution'

def worker(role, slug, responsibility):
    return {
        'role': role,
        'path': f'/root/agency-agents/integrations/codex/agents/{slug}.toml',
        'responsibility': responsibility,
    }

sources = [
    {
        'name': 'GCS Technologies - AI Security Policy Guide for Small Businesses (2026)',
        'url': 'https://www.gcstechnologies.com/ai-security-policy-guide/',
        'note': 'Current SMB AI policy guidance emphasizes approved tools, data-handling rules, shadow AI visibility, review steps, tool evaluation, and incident handling.'
    },
    {
        'name': 'Kenosha.com - 10 AI Privacy Concerns Your Business Should Be Aware Of in 2026',
        'url': 'https://www.kenosha.com/local/10-ai-privacy-concerns-your-business-should-be-aware-of-in-2026/',
        'note': 'Small-business AI privacy coverage highlights shadow AI, data privacy, compliance, and uncontrolled AI use as practical 2026 concerns.'
    },
    {
        'name': 'Adobe Business - SEO in 2026: How AI is reshaping search fundamentals',
        'url': 'https://business.adobe.com/blog/seo-in-2026-fundamentals',
        'note': 'AI search optimization shifts from only rankings to extractability, trust, and citation-worthiness in AI-generated answers.'
    },
    {
        'name': 'Yotpo - What Is LLMs.txt? The Guide To AI Search & GEO',
        'url': 'https://www.yotpo.com/blog/what-is-llms-txt/',
        'note': 'Ecommerce and content teams are being educated that llms.txt and AI-readable source guidance are emerging AI search/GEO practices.'
    },
    {
        'name': 'U.S. Chamber of Commerce - AI training guide for small business',
        'url': 'https://www.uschamber.com/co/start/strategy/ai-training-guide-small-business',
        'note': 'Small businesses need practical AI skills across leadership, marketing, HR, and operations; training can start with free/low-cost resources.'
    },
    {
        'name': 'McKinsey - Superagency in the workplace',
        'url': 'https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work',
        'note': 'Most companies invest in AI but very few report maturity, supporting demand for adoption playbooks, training, governance, and measurement.'
    },
    {
        'name': 'CMIT Solutions - Best AI Automation Tools for SMBs (2026)',
        'url': 'https://cmitsolutions.com/blog/ai-automation-tools/',
        'note': 'SMBs are using ChatGPT, Copilot, Zapier, HubSpot, Asana, Notion AI, Mailchimp, scheduling and CRM tools; opportunity is tool-selection and workflow readiness, not paid implementation at $0 MRR.'
    },
    {
        'name': 'Kittl - 25 Best Digital Products to Sell in 2026',
        'url': 'https://www.kittl.com/blogs/digital-products-to-sell-dsi/',
        'note': 'Digital products such as templates, planners, ebooks, SVG files, and AI prompt packs remain low-cost product opportunities, but marketplace setup/competition makes them slower than B2B service sprints.'
    },
    {
        'name': 'Installed Agency Agents roster',
        'url': '/root/agency-agents/integrations/codex/agents',
        'note': 'Local workers confirmed: data-privacy-officer, legal-compliance-checker, security-architect, compliance-auditor, document-generator, automation-governance-architect, corporate-training-designer, operations-manager, customer-success-manager, pricing-analyst, ai-citation-strategist, seo-specialist, content-creator, business-strategist.'
    },
]

opps = [
    {
        'rank': 1,
        'name': 'Shadow AI Policy & Tool Inventory Sprint',
        'score_total': 76,
        'score_average': 9.5,
        'scores': {'startup_cost':10,'speed_to_first_revenue':10,'automation_potential':8,'margin':10,'recurring_revenue_potential':9,'fulfillment_complexity':9,'lead_acquisition_difficulty':10,'fit_with_agency_agents':10},
        'current_stage_fit': 'Best $0-MRR opportunity. The pain is concrete: staff are already using AI tools, but owners lack an approved-tool list, data rules, review rules, and incident path. Fulfillment is document/interview based and can be done without credentials, scans, paid software, or legal guarantees.',
        'beachhead_icp': '5-50 employee professional-service firms, agencies, clinics, local-service operators, accountants, consultants, law-adjacent offices, and B2B teams using ChatGPT/Copilot/Claude for emails, proposals, marketing, support, finance, or client work without a written AI policy.',
        'offer': 'Free 12-question Shadow AI Risk Self-Check; $499-$1,200 AI Policy & Tool Inventory Sprint including current-use worksheet, tool inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, tool intake form, incident/escalation path, and owner briefing; $500-$1,500/mo quarterly policy refresh, training, and evidence-log retainer after first sale.',
        'zero_cost_stack': ['public guidance','local Markdown/CSV templates','manual interview worksheet','manual review','no paid SaaS','no client credentials','human approval before any outreach'],
        'agent_workers': [
            worker('Data Privacy Officer','data-privacy-officer','Define sensitive-data categories, retention concerns, and AI tool/vendor questions.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep language conservative and route legal decisions to qualified humans.'),
            worker('Security Architect','security-architect','Translate shadow-AI and agentic-AI risks into practical SMB controls.'),
            worker('Compliance Auditor','compliance-auditor','Create evidence log, approval trail, and policy review checklist.'),
            worker('Document Generator','document-generator','Assemble the policy, worksheet, tool inventory, and briefing pack.'),
        ],
        'next_safe_action': 'Build the six-template Shadow AI pack locally: self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton.'
    },
    {
        'rank': 2,
        'name': 'Employee AI Training & Prompt SOP Workshop',
        'score_total': 73,
        'score_average': 9.13,
        'scores': {'startup_cost':10,'speed_to_first_revenue':9,'automation_potential':8,'margin':10,'recurring_revenue_potential':8,'fulfillment_complexity':9,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'current_stage_fit': 'Fresh high-fit add-on to the Shadow AI offer. Current small-business AI training sources support practical role-based training, and the deliverable can be local docs, exercises, prompt SOPs, and a 60-minute workshop deck with no paid tools.',
        'beachhead_icp': 'SMB owners who know employees are using AI but need safe, practical workflows for writing, customer replies, research, proposals, HR/admin, and marketing.',
        'offer': 'Free AI Skills Gap Self-Assessment; $399-$999 role-based Prompt SOP Workshop pack with safe-use rules, 20 approved prompts, review checklist, prompt log, and manager scorecard; $300-$900/mo monthly prompt library refresh and office-hours retainer after first sale.',
        'zero_cost_stack': ['public free training resources','local Markdown/PPT/CSV templates','role-based exercises','no paid course platform','no paid AI seats provisioned','no client data collection'],
        'agent_workers': [
            worker('Corporate Training Designer','corporate-training-designer','Build workshop agenda, exercises, learning objectives, and manager scorecard.'),
            worker('Prompt Engineer','prompt-engineer','Create safe reusable prompt templates and prompt-improvement SOPs.'),
            worker('Data Privacy Officer','data-privacy-officer','Embed data-handling and sensitive-information guardrails.'),
            worker('Document Generator','document-generator','Package deck, handouts, logs, and prompt-library templates.'),
            worker('Business Strategist','business-strategist','Position training as a fast adoption/ROI offer, not abstract AI education.'),
        ],
        'next_safe_action': 'Draft a one-hour workshop outline, 20 role-safe starter prompts, prompt review checklist, and manager scorecard locally.'
    },
    {
        'rank': 3,
        'name': 'AI Search Visibility & LLMs.txt Retrofit Snapshot',
        'score_total': 72,
        'score_average': 9.0,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':9,'fulfillment_complexity':8,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'current_stage_fit': 'Already launched and still strong. Current SEO/GEO sources show demand for extractable, trustworthy, AI-readable content and llms.txt guidance. Keep it as runner-up because proof samples can be built from public websites with no paid tools or site access.',
        'beachhead_icp': 'Local service businesses and small B2B firms with thin service pages, weak FAQs, unclear proof, no clear source map, and no llms.txt guidance.',
        'offer': 'Free 5-point AI Search/LLMs.txt Readiness Snapshot; $299-$799 retrofit plan with answer capsules, FAQ gaps, proof-section recommendations, internal-link plan, and draft llms.txt/source map; $300-$900/mo refresh/reporting retainer.',
        'zero_cost_stack': ['public website review','local Markdown/CSV/JSON templates','manual scoring','no paid tools','no form submissions','no ranking/citation guarantees'],
        'agent_workers': [
            worker('AI Citation Strategist','ai-citation-strategist','Score answerability, source clarity, entity clarity, and AI-citation readiness.'),
            worker('SEO Specialist','seo-specialist','Review crawlability, service intent, internal links, and page hygiene.'),
            worker('Content Creator','content-creator','Draft answer capsules, FAQs, proof sections, and llms.txt page descriptions.'),
            worker('Evidence Collector','evidence-collector','Collect public evidence snippets and before/after notes.'),
        ],
        'next_safe_action': 'Add three public-site samples and one before/after source-map example; no outreach execution.'
    },
    {
        'rank': 4,
        'name': 'SMB AI Tool Stack Rationalization Sprint',
        'score_total': 71,
        'score_average': 8.88,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':8,'fulfillment_complexity':8,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'current_stage_fit': 'Fresh adjacent opportunity from SMB automation-tool research. Owners are overwhelmed by ChatGPT/Copilot/Zapier/CRM/scheduling/Notion/Mailchimp choices. At $0 MRR, sell a no-login tool inventory and workflow-fit recommendation, not implementation.',
        'beachhead_icp': 'SMBs using too many disconnected AI/productivity tools or unsure which workflows should be automated first.',
        'offer': 'Free AI Tool Sprawl Checklist; $399-$899 Tool Stack Rationalization Sprint with tool inventory, use-case map, duplicate-cost flags, workflow priority matrix, and 30-day adoption plan; later $500-$1,500/mo implementation governance after approved tools/channels exist.',
        'zero_cost_stack': ['client-provided tool list only after sale','public tool docs','local CSV templates','manual workflow mapping','no SaaS login','no paid implementation'],
        'agent_workers': [
            worker('Tool Evaluator','tool-evaluator','Compare tools, fit, risk, and no/low-cost alternatives.'),
            worker('Automation Governance Architect','automation-governance-architect','Design safe automation priority matrix and approval gates.'),
            worker('Operations Manager','operations-manager','Map workflows, bottlenecks, and owner time savings.'),
            worker('Pricing Analyst','pricing-analyst','Estimate monthly savings and ROI from consolidation.'),
            worker('Document Generator','document-generator','Package tool inventory, recommendations, and adoption roadmap.'),
        ],
        'next_safe_action': 'Draft tool-inventory CSV, workflow priority matrix, duplicate-cost worksheet, and 30-day adoption plan locally.'
    },
    {
        'rank': 5,
        'name': 'Customer Support Knowledge-Base & Triage Readiness Sprint',
        'score_total': 69,
        'score_average': 8.63,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':8,'fulfillment_complexity':8,'lead_acquisition_difficulty':8,'fit_with_agency_agents':9},
        'current_stage_fit': 'Still good but slightly behind AI governance/training because fulfillment often needs client-specific support data. Zero-cost version is a public-site FAQ gap audit, triage tree, canned-response pack, and human escalation rules.',
        'beachhead_icp': 'Small SaaS, ecommerce stores, agencies, clinics, and local-service teams with repeated questions, inconsistent replies, weak FAQ pages, and no escalation rules.',
        'offer': 'Free support FAQ gap checklist; $299-$799 support readiness sprint with top-25 FAQ outline, triage tree, escalation policy, canned replies, and weekly reporting template; $500-$1,200/mo KB refresh/reporting retainer.',
        'zero_cost_stack': ['public FAQ/site review','client-provided docs only after sale','local Markdown/CSV templates','no helpdesk login','no live chatbot claims'],
        'agent_workers': [
            worker('Customer Success Manager','customer-success-manager','Define support outcomes, triage priorities, and support-health metrics.'),
            worker('Content Creator','content-creator','Draft FAQ entries and canned replies.'),
            worker('Operations Manager','operations-manager','Build triage and escalation workflow.'),
            worker('Evidence Collector','evidence-collector','Collect public support-page gaps and examples.'),
        ],
        'next_safe_action': 'Create KB/triage readiness checklist and sample triage tree locally; no helpdesk integrations.'
    },
    {
        'rank': 6,
        'name': 'B2B AI Governance Template Micro-Store',
        'score_total': 65,
        'score_average': 8.13,
        'scores': {'startup_cost':9,'speed_to_first_revenue':6,'automation_potential':9,'margin':10,'recurring_revenue_potential':6,'fulfillment_complexity':9,'lead_acquisition_difficulty':6,'fit_with_agency_agents':10},
        'current_stage_fit': 'Digital products are low-cost/high-margin, but marketplace setup, competition, and distribution make it slower than direct B2B services. Best use now: turn service templates into saleable assets after the first client-facing pack is proven.',
        'beachhead_icp': 'Consultants, agencies, fractional COOs, and SMB owners who want downloadable AI policy/training/tool-inventory templates.',
        'offer': '$19-$79 template pack: AI-use policy skeleton, shadow-AI tool inventory, prompt log, sensitive-data rules, training checklist, and manager review scorecard; later bundle with service sprint.',
        'zero_cost_stack': ['local docs','static landing page copy','manual checkout later only with approved payment channel','no Etsy/store signup from cron','no paid design tools'],
        'agent_workers': [
            worker('Document Generator','document-generator','Create clean PDF/DOCX/CSV templates.'),
            worker('Content Creator','content-creator','Write listing copy and buyer instructions.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep disclaimers clear: templates are not legal advice.'),
            worker('Pricing Analyst','pricing-analyst','Test bundles and price points after a selling channel is approved.'),
        ],
        'next_safe_action': 'Park as a derivative asset; do not open marketplaces or payment accounts until Brian approves a channel.'
    },
]

out = {
    'last_updated': UPDATED,
    'revenue': {
        'mrr': current_mrr,
        'sources_checked': [str(STATE_PATH), '/root/ai-holding-company/businesses/**/*revenue*'],
        'revenue_files_found': revenue_files,
        'evidence': f'RPG Revenue Vault monthlyRevenue is {current_mrr}; {len(revenue_files)} business revenue files found under /root/ai-holding-company/businesses.',
        'stage_rule': stage_rule,
    },
    'scoring_scale': '1-10 where 10 is best. For startup_cost, 10 means lowest cost. For fulfillment_complexity and lead_acquisition_difficulty, 10 means easiest.',
    'criteria': ['startup_cost','speed_to_first_revenue','automation_potential','margin','recurring_revenue_potential','fulfillment_complexity','lead_acquisition_difficulty','fit_with_agency_agents'],
    'sources': sources,
    'opportunities': opps,
    'selected_for_current_stage': ['Shadow AI Policy & Tool Inventory Sprint','Employee AI Training & Prompt SOP Workshop'],
    'fresh_ideas_added_this_run': ['Employee AI Training & Prompt SOP Workshop','SMB AI Tool Stack Rationalization Sprint','B2B AI Governance Template Micro-Store'],
}
(IDEAS / 'scored-opportunities.json').write_text(json.dumps(out, indent=2) + '\n')

score_rows = '\n'.join([f"| {o['rank']} | {o['name']} | {o['score_total']}/80 | {o['current_stage_fit'].split('.')[0]} |" for o in opps])
backlog = f"""# Business Research Backlog

Last updated: {UPDATED}
Revenue stage: ${current_mrr} MRR from RPG Revenue Vault; {len(revenue_files)} business revenue files found.
Rule applied: {stage_rule}.

## Current best opportunity: Shadow AI Policy & Tool Inventory Sprint

**Business identity**
- Market: SMBs whose employees already use ChatGPT, Copilot, Claude, browser agents, and AI writing/research tools without a written policy or tool inventory.
- Buyer pain: owner does not know what tools staff use, what data is being pasted into them, or who reviews AI output before customer/client use.
- Positioning: fast, practical AI policy and Shadow AI inventory sprint; not legal advice, cybersecurity certification, penetration testing, managed security, or AI software implementation.

**Offer**
- Free lead magnet: 12-question Shadow AI Risk Self-Check.
- Paid pilot: $499-$1,200 sprint including current-use worksheet, tool inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, tool intake form, incident/escalation path, and owner briefing.
- Retainer: $500-$1,500/mo quarterly policy refresh, training updates, approved-tool evidence log, and governance review after first sale.
- Exclusions: no scans, no credential access, no legal/security guarantees, no compliance certification, no paid tooling before revenue, no outbound execution from this cron.

**Why now / sources**
- GCS Technologies frames SMB AI security policy around approved tools, data-handling rules, shadow AI visibility, review steps, tool evaluation, and incident handling.
- Current privacy coverage highlights shadow AI, data privacy, and compliance as small-business risks in 2026.
- This is narrower and easier to sell than broad cyber consulting because the first deliverable is policy and inventory documentation only.

**Agent workers found in /root/agency-agents**
- Data Privacy Officer: `/root/agency-agents/integrations/codex/agents/data-privacy-officer.toml`
- Legal Compliance Checker: `/root/agency-agents/integrations/codex/agents/legal-compliance-checker.toml`
- Security Architect: `/root/agency-agents/integrations/codex/agents/security-architect.toml`
- Compliance Auditor: `/root/agency-agents/integrations/codex/agents/compliance-auditor.toml`
- Document Generator: `/root/agency-agents/integrations/codex/agents/document-generator.toml`

**Next safe action**
Build the six-template Shadow AI pack locally. No outreach, scans, client system access, paid tools, or legal/security guarantees.

---

## New runner-up: Employee AI Training & Prompt SOP Workshop

**Why it moved up**
- U.S. Chamber and McKinsey-style workplace AI research supports the gap: many companies are investing in AI, but employees need practical skills, guardrails, and workflows.
- It pairs naturally with Shadow AI: first create rules, then train staff to use approved prompts safely.
- Zero-cost fulfillment: workshop outline, prompt library, prompt log, review checklist, role-play exercises, and manager scorecard.

**Offer**
- Free AI Skills Gap Self-Assessment.
- Paid pack: $399-$999 role-based Prompt SOP Workshop with 20 approved prompts, data-safety rules, review checklist, prompt log, and manager scorecard.
- Retainer: $300-$900/mo prompt-library refresh and office-hours after first sale.

**Workers:** Corporate Training Designer, Prompt Engineer, Data Privacy Officer, Document Generator, Business Strategist.

**Next safe action:** draft workshop outline, 20 role-safe starter prompts, prompt review checklist, and manager scorecard locally.

---

## Keep scaling: AI Search Visibility & LLMs.txt Retrofit Snapshot

Still the strongest already-started zero-cost service. Current SEO/GEO/AI-search sources show AI search is reshaping SEO toward extractability, trust, citations, and AI-readable source guidance. Keep producing public website samples and sharpen the monthly retainer. Do not claim ranking/citation guarantees.

**Workers:** AI Citation Strategist, SEO Specialist, Content Creator, Evidence Collector, Offer & Lead Gen Strategist.

**Next safe action:** score 3 more public websites and create a short before/after llms.txt/source-map example.

---

## Fresh opportunities added this run

### Employee AI Training & Prompt SOP Workshop
- Offer: free skills-gap self-assessment; $399-$999 workshop pack; $300-$900/mo prompt-library refresh/office-hours retainer.
- Why: complements Shadow AI policy, easy to fulfill with agents, no paid tooling.
- Safe next action: draft local training assets only.

### SMB AI Tool Stack Rationalization Sprint
- Offer: free AI tool sprawl checklist; $399-$899 tool-stack rationalization sprint; later implementation governance after approved channels/tools.
- Why: SMBs are juggling ChatGPT/Copilot/Zapier/CRM/scheduling/productivity tools and need a practical map before automation.
- Workers: Tool Evaluator, Automation Governance Architect, Operations Manager, Pricing Analyst, Document Generator.
- Safe next action: draft tool-inventory CSV and workflow priority matrix; no SaaS logins or paid tools.

### B2B AI Governance Template Micro-Store
- Offer: $19-$79 downloadable AI governance template pack after a channel is approved.
- Why: digital products are cheap/high-margin, but distribution is slower than B2B service selling.
- Workers: Document Generator, Content Creator, Legal Compliance Checker, Pricing Analyst.
- Safe next action: park as derivative assets; do not open marketplaces/payment accounts from cron.

---

## Other scored opportunities

### Customer Support Knowledge-Base & Triage Readiness Sprint
- Offer: free FAQ gap checklist; $299-$799 support readiness sprint; $500-$1,200/mo KB refresh/reporting retainer after sale.
- Workers: Customer Success Manager, Content Creator, Operations Manager, Evidence Collector.
- Safe next action: create KB/triage readiness checklist and sample triage tree locally; no helpdesk integrations.

## Scoreboard

| Rank | Idea | Score | Stage fit |
|---:|---|---:|---|
{score_rows}
"""
(IDEAS / 'backlog.md').write_text(backlog)

report = f"""# Business Research Agent — Latest Report

Updated: {UPDATED}

## Revenue check
- Current MRR: **${current_mrr}**.
- Evidence: RPG Revenue Vault monthlyRevenue is {current_mrr}; {len(revenue_files)} business revenue files found under /root/ai-holding-company/businesses.
- Rule applied: **{stage_rule}**.

## Best idea now
**Shadow AI Policy & Tool Inventory Sprint** — **76/80**

Why it wins:
- Most direct $0-MRR path: document/interview deliverables only, no scans, no credentials, no paid SaaS, no legal/security guarantees.
- Current 2026 SMB AI-policy/privacy sources validate the pain: owners need approved-tool lists, data rules, review rules, shadow-AI visibility, and incident handling.
- Strong retainer path: quarterly policy refresh, staff training, approved-tool evidence log, and governance review.
- Strong Agency Agents fit: Data Privacy Officer, Legal Compliance Checker, Security Architect, Compliance Auditor, Document Generator.

## New runner-up
**Employee AI Training & Prompt SOP Workshop** — **73/80**

Why it is worth adding:
- Pairs with Shadow AI: after rules are written, train staff to use approved AI workflows safely.
- Current small-business AI training/workplace AI sources validate demand for practical AI skills and people-in-the-loop workflows.
- Zero-cost fulfillment: local workshop deck, role-safe prompt library, prompt log, review checklist, and manager scorecard.

## Keep active
**AI Search Visibility & LLMs.txt Retrofit Snapshot** — **72/80**

Why it stays active:
- Already partially launched and still fits $0 MRR.
- Current AI-search/SEO/llms.txt sources show commercial education around extractability, trust, GEO/AEO, and AI-readable source maps.
- Public-site review + local reports can create samples without paid tools or client access.

## Scored ideas
1. Shadow AI Policy & Tool Inventory Sprint — 76/80
2. Employee AI Training & Prompt SOP Workshop — 73/80
3. AI Search Visibility & LLMs.txt Retrofit Snapshot — 72/80
4. SMB AI Tool Stack Rationalization Sprint — 71/80
5. Customer Support Knowledge-Base & Triage Readiness Sprint — 69/80
6. B2B AI Governance Template Micro-Store — 65/80

## Game-ready quests prepared
- Build Shadow AI Policy & Tool Inventory Sprint — assigned to Data Privacy Officer.
- Draft Employee AI Training & Prompt SOP Workshop — assigned to Corporate Training Designer.
- Add AI Search + LLMs.txt Source-Map Samples — assigned to AI Citation Strategist.
- Draft SMB AI Tool Stack Rationalization Sprint — assigned to Tool Evaluator.
- Draft Support KB & Triage Readiness Sprint — assigned to Customer Success Manager.
- Package B2B AI Governance Template Micro-Store Assets — assigned to Document Generator.

## Next safe action
Build the Shadow AI six-template pack locally: self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton. Then draft the Employee AI Training workshop outline as the natural upsell. Do **not** contact prospects, submit forms, access client systems, run scans, place calls, send emails, connect SaaS tools, open marketplaces, or spend money.

## Artifacts updated
- `/root/ai-holding-company/business-research-agent/ideas/backlog.md`
- `/root/ai-holding-company/business-research-agent/ideas/scored-opportunities.json`
- `/root/ai-holding-company/business-research-agent/reports/latest.md`
- `/root/ai-holding-company/business-research-agent/game/research_quests.json`
- `/root/ai-holding-company/rpg-command-center/engine/public/game_state.json` updated non-destructively with research quest/status/event.
"""
(REPORTS / 'latest.md').write_text(report)

quests = [
    {
        'id': 'research_shadow_ai_policy_inventory_20260626_1212',
        'name': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'title': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'desc': 'Research quest: create Shadow AI self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page AI policy skeleton. No scans, no client system access, no legal/security guarantees, no paid tools, and no outreach execution.',
        'reward': '+170 research XP',
        'target': 6,
        'current': 0,
        'status': 'active',
        'assigned_agent': 'Data Privacy Officer',
        'source': 'business_research_agent',
        'updated_at': UPDATED,
        'next_step': 'Draft the six local templates; route legal/security decisions to human review.'
    },
    {
        'id': 'research_employee_ai_training_prompt_sop_20260626',
        'name': 'Draft Employee AI Training & Prompt SOP Workshop',
        'title': 'Draft Employee AI Training & Prompt SOP Workshop',
        'desc': 'Research quest: create a one-hour AI training outline, 20 role-safe starter prompts, prompt log, data-safety rules, review checklist, and manager scorecard. No client data collection, no paid course platform, no outbound execution.',
        'reward': '+140 research XP',
        'target': 6,
        'current': 0,
        'status': 'active',
        'assigned_agent': 'Corporate Training Designer',
        'source': 'business_research_agent',
        'updated_at': UPDATED,
        'next_step': 'Draft local training assets as an upsell to the Shadow AI policy sprint.'
    },
    {
        'id': 'research_ai_tool_stack_rationalization_20260626',
        'name': 'Draft SMB AI Tool Stack Rationalization Sprint',
        'title': 'Draft SMB AI Tool Stack Rationalization Sprint',
        'desc': 'Research quest: create AI tool inventory CSV, duplicate-cost worksheet, workflow priority matrix, risk notes, and 30-day adoption roadmap. No SaaS logins, no paid tools, no client system access, no outbound execution.',
        'reward': '+125 research XP',
        'target': 5,
        'current': 0,
        'status': 'queued',
        'assigned_agent': 'Tool Evaluator',
        'source': 'business_research_agent',
        'updated_at': UPDATED,
        'next_step': 'Draft local worksheets only; do not connect to client tools.'
    },
    {
        'id': 'research_b2b_ai_governance_template_store_20260626',
        'name': 'Package B2B AI Governance Template Micro-Store Assets',
        'title': 'Package B2B AI Governance Template Micro-Store Assets',
        'desc': 'Research quest: package derivative AI governance templates and listing copy for future approved sales channel. Do not open marketplace accounts, payment accounts, or spend money.',
        'reward': '+90 research XP',
        'target': 4,
        'current': 0,
        'status': 'queued',
        'assigned_agent': 'Document Generator',
        'source': 'business_research_agent',
        'updated_at': UPDATED,
        'next_step': 'Create local template bundle and listing draft only after service templates are proven.'
    },
]
(GAME / 'research_quests.json').write_text(json.dumps({'last_updated': UPDATED, 'quests': quests}, indent=2) + '\n')

# Non-destructive game_state update: upsert quests by ID, append event, update research agent.
existing = {q.get('id'): i for i, q in enumerate(state.get('quests', [])) if q.get('id')}
state.setdefault('quests', [])
for q in quests:
    if q['id'] in existing:
        state['quests'][existing[q['id']]].update(q)
    else:
        state['quests'].append(q)
state.setdefault('events', []).append({
    'timestamp': UPDATED,
    'type': 'research_update',
    'agent': 'Business Research Agent',
    'message': 'Selected Shadow AI Policy & Tool Inventory Sprint as best $0-MRR opportunity; added Employee AI Training & Prompt SOP Workshop as the strongest fresh runner-up. Safe quests only; no outreach or spend.',
    'source': 'business_research_agent'
})
for a in state.get('agents', []):
    if a.get('name') == 'Business Research Agent':
        a['status'] = 'working'
        a['current_task'] = 'Selected Shadow AI Policy & Tool Inventory Sprint as best $0-MRR opportunity; added Employee AI Training & Prompt SOP Workshop and SMB AI Tool Stack quests. No outreach or spend.'
        a['last_seen'] = UPDATED
        a['last_message'] = 'Best $0-MRR idea: Shadow AI Policy & Tool Inventory Sprint. Runner-up: Employee AI Training & Prompt SOP Workshop.'
state['timestamp'] = UPDATED
STATE_PATH.write_text(json.dumps(state, indent=2) + '\n')
print('updated', IDEAS/'scored-opportunities.json')
print('updated', IDEAS/'backlog.md')
print('updated', REPORTS/'latest.md')
print('updated', GAME/'research_quests.json')
print('updated', STATE_PATH)
print('mrr', current_mrr, 'quests_added_or_updated', len(quests))
