#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('/root/ai-holding-company')
RESEARCH = ROOT / 'business-research-agent'
GAME_STATE = ROOT / 'rpg-command-center/engine/public/game_state.json'
TS = '2026-06-26T16:16:18Z'

revenue = {
    'mrr': 0,
    'sources_checked': [
        str(GAME_STATE),
        '/root/ai-holding-company/businesses/**/*revenue*'
    ],
    'revenue_files_found': [],
    'evidence': 'RPG Revenue Vault monthlyRevenue is 0; 0 business revenue files found under /root/ai-holding-company/businesses.',
    'stage_rule': '$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution'
}

sources = [
    {
        'name': 'Optro - Shadow AI stats for 2026',
        'url': 'https://optro.ai/blog/shadow-ai-stats',
        'note': 'Search result reports widespread shadow-AI usage and a governance/adoption gap, reinforcing demand for tool inventories and AI-use policies.'
    },
    {
        'name': 'GCS Technologies - AI Security Policy Guide for Small Businesses (2026)',
        'url': 'https://www.gcstechnologies.com/ai-security-policy-guide/',
        'note': 'SMB AI policy guidance centers on approved tools, data handling rules, shadow AI, review steps, tool evaluation, and incident handling.'
    },
    {
        'name': 'U.S. Chamber of Commerce - AI Is Powering Small Business Growth in 2026',
        'url': 'https://www.uschamber.com/co/run/technology/ai-powered-growth-engines',
        'note': 'Search result says 57% of small businesses believe AI will improve daily work, supporting practical governance/training offers.'
    },
    {
        'name': 'NextPhone - AI receptionist statistics 2026',
        'url': 'https://www.getnextphone.com/blog/ai-receptionist-statistics',
        'note': 'Search result cites call-analysis data where many business calls are real leads and a meaningful share arrive after hours; useful for a docs-only missed-call readiness audit.'
    },
    {
        'name': 'Resonate AI - AI Receptionists 2026 statistics',
        'url': 'https://www.resonateapp.com/resources/ai-receptionists-statistics',
        'note': 'Search result highlights revenue impact from missed calls and voicemail abandonment, validating missed-call/call-flow diagnostics without needing telecom setup.'
    },
    {
        'name': 'Gaazzeebo - GEO Search Visibility Guide 2026',
        'url': 'https://gaazzeebo.net/topics/geo-ai-visibility',
        'note': 'AI-search/GEO education now includes llms.txt, AEO, schema, and AI search visibility, supporting public-site AI-search readiness snapshots.'
    },
    {
        'name': 'MyDesigns - Digital Products to Sell on Etsy: 30 Ideas for 2026',
        'url': 'https://mydesigns.io/blog/digital-products-to-sell-on-etsy/',
        'note': 'Digital downloads such as templates and printables remain high-margin, but channel/account setup makes them secondary until an approved marketplace/payment path exists.'
    },
    {
        'name': 'Installed Agency Agents roster',
        'url': '/root/agency-agents/integrations/codex/agents',
        'note': 'Confirmed local workers include data-privacy-officer, legal-compliance-checker, security-architect, compliance-auditor, document-generator, corporate-training-designer, prompt-engineer, tool-evaluator, operations-manager, customer-success-manager, content-creator, seo-specialist, ai-citation-strategist, sales-outreach, and outbound-strategist.'
    }
]

def worker(role, slug, responsibility):
    return {'role': role, 'path': f'/root/agency-agents/integrations/codex/agents/{slug}.toml', 'responsibility': responsibility}

opportunities = [
    {
        'rank': 1,
        'name': 'Shadow AI Policy & Tool Inventory Sprint',
        'score_total': 76,
        'score_average': 9.5,
        'scores': {'startup_cost':10,'speed_to_first_revenue':10,'automation_potential':8,'margin':10,'recurring_revenue_potential':9,'fulfillment_complexity':9,'lead_acquisition_difficulty':10,'fit_with_agency_agents':10},
        'current_stage_fit': 'Still the best $0-MRR opportunity. Demand is driven by employees already using AI tools while owners lack tool inventory, data rules, human-review rules, and incident/escalation paths. Fulfillment is documents/interviews only: no scans, no credentials, no paid software, no legal/security guarantees.',
        'beachhead_icp': '5-50 employee professional-service firms, agencies, clinics, accountants, consultants, law-adjacent offices, and local-service operators using ChatGPT/Copilot/Claude for emails, proposals, marketing, support, admin, or client work without a written AI policy.',
        'offer': 'Free 12-question Shadow AI Risk Self-Check; $499-$1,200 AI Policy & Tool Inventory Sprint with current-use worksheet, tool inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, tool intake form, incident/escalation path, and owner briefing; $500-$1,500/mo quarterly policy refresh/training/evidence-log retainer after first sale.',
        'zero_cost_stack': ['public guidance','local Markdown/CSV templates','manual interview worksheet','manual review','no paid SaaS','no client credentials','human approval before any outreach'],
        'agent_workers': [
            worker('Data Privacy Officer','data-privacy-officer','Define sensitive-data categories, retention concerns, privacy-safe tool questions, and vendor-risk prompts.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep claims conservative and route legal decisions to qualified humans.'),
            worker('Security Architect','security-architect','Translate shadow-AI and agentic-AI risks into practical SMB controls.'),
            worker('Compliance Auditor','compliance-auditor','Create evidence log, approval trail, and policy review checklist.'),
            worker('Document Generator','document-generator','Assemble worksheets, policy skeleton, matrices, and briefing pack.')
        ],
        'next_safe_action': 'Build the six-template Shadow AI pack locally: self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page policy skeleton.'
    },
    {
        'rank': 2,
        'name': 'Employee AI Training & Prompt SOP Workshop',
        'score_total': 73,
        'score_average': 9.13,
        'scores': {'startup_cost':10,'speed_to_first_revenue':9,'automation_potential':8,'margin':10,'recurring_revenue_potential':8,'fulfillment_complexity':9,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'current_stage_fit': 'Best natural upsell after the Shadow AI policy. Sources support SMB interest in AI, but employees still need practical guardrails, approved prompts, prompt logs, review workflows, and manager scorecards.',
        'beachhead_icp': 'SMB owners who know staff are using AI but need safe, repeatable workflows for writing, customer replies, research, proposals, HR/admin, marketing, and operations.',
        'offer': 'Free AI Skills Gap Self-Assessment; $399-$999 role-based Prompt SOP Workshop with safe-use rules, 20 approved prompts, review checklist, prompt log, role exercises, and manager scorecard; $300-$900/mo monthly prompt-library refresh and office-hours retainer after first sale.',
        'zero_cost_stack': ['public free training resources','local Markdown/PPT/CSV templates','role-based exercises','no paid course platform','no paid AI seats provisioned','no client data collection'],
        'agent_workers': [
            worker('Corporate Training Designer','corporate-training-designer','Build workshop agenda, learning objectives, role exercises, and manager scorecard.'),
            worker('Prompt Engineer','prompt-engineer','Create safe reusable prompt templates and prompt-improvement SOPs.'),
            worker('Data Privacy Officer','data-privacy-officer','Embed data-handling and sensitive-information guardrails.'),
            worker('Document Generator','document-generator','Package deck, handouts, logs, and prompt-library templates.'),
            worker('Business Strategist','business-strategist','Position training as practical adoption/ROI, not abstract AI education.')
        ],
        'next_safe_action': 'Draft a one-hour workshop outline, 20 role-safe starter prompts, prompt review checklist, and manager scorecard locally.'
    },
    {
        'rank': 3,
        'name': 'AI Search Visibility & LLMs.txt Retrofit Snapshot',
        'score_total': 72,
        'score_average': 9.0,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':9,'fulfillment_complexity':8,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'current_stage_fit': 'Already launched and still strong. Current GEO/AEO/llms.txt education supports demand for extractable, trustworthy, AI-readable content. Public-site review and sample reports require no paid tools or site access.',
        'beachhead_icp': 'Local service businesses and small B2B firms with thin service pages, weak FAQs, unclear proof, no clear source map, and no llms.txt guidance.',
        'offer': 'Free 5-point AI Search/LLMs.txt Readiness Snapshot; $299-$799 retrofit plan with answer capsules, FAQ gaps, proof-section recommendations, internal-link plan, and draft llms.txt/source map; $300-$900/mo refresh/reporting retainer.',
        'zero_cost_stack': ['public website review','local Markdown/CSV/JSON templates','manual scoring','no paid tools','no form submissions','no ranking/citation guarantees'],
        'agent_workers': [
            worker('AI Citation Strategist','ai-citation-strategist','Score answerability, source clarity, entity clarity, and AI-citation readiness.'),
            worker('SEO Specialist','seo-specialist','Review crawlability, service intent, internal links, and page hygiene.'),
            worker('Content Creator','content-creator','Draft answer capsules, FAQs, proof sections, and llms.txt page descriptions.'),
            worker('Evidence Collector','evidence-collector','Collect public evidence snippets and before/after notes.')
        ],
        'next_safe_action': 'Add three public-site samples and one before/after source-map example; no outreach execution.'
    },
    {
        'rank': 4,
        'name': 'SMB AI Tool Stack Rationalization Sprint',
        'score_total': 71,
        'score_average': 8.88,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':8,'fulfillment_complexity':8,'lead_acquisition_difficulty':9,'fit_with_agency_agents':10},
        'current_stage_fit': 'Adjacent to Shadow AI. Owners are juggling ChatGPT, Copilot, Zapier, CRM, scheduling, support, and productivity tools and need a no-login tool inventory plus workflow-fit roadmap before implementation.',
        'beachhead_icp': 'SMBs using disconnected AI/productivity tools or unsure which workflows should be automated first.',
        'offer': 'Free AI Tool Sprawl Checklist; $399-$899 Tool Stack Rationalization Sprint with tool inventory, use-case map, duplicate-cost flags, workflow priority matrix, risk notes, and 30-day adoption plan; later $500-$1,500/mo implementation governance after approved tools/channels exist.',
        'zero_cost_stack': ['client-provided tool list only after sale','public tool docs','local CSV templates','manual workflow mapping','no SaaS login','no paid implementation'],
        'agent_workers': [
            worker('Tool Evaluator','tool-evaluator','Compare tools, fit, risk, duplicate spend, and no/low-cost alternatives.'),
            worker('Operations Manager','operations-manager','Map workflows, bottlenecks, handoffs, and owner time savings.'),
            worker('Pricing Analyst','pricing-analyst','Estimate monthly savings and ROI from consolidation.'),
            worker('Document Generator','document-generator','Package tool inventory, recommendations, and adoption roadmap.')
        ],
        'next_safe_action': 'Draft tool-inventory CSV, workflow priority matrix, duplicate-cost worksheet, and 30-day adoption plan locally.'
    },
    {
        'rank': 5,
        'name': 'Missed-Call Revenue Leak & AI Receptionist Readiness Audit',
        'score_total': 70,
        'score_average': 8.75,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':8,'margin':9,'recurring_revenue_potential':9,'fulfillment_complexity':8,'lead_acquisition_difficulty':9,'fit_with_agency_agents':9},
        'current_stage_fit': 'Fresh docs-only opportunity from current AI receptionist/missed-call research. It captures urgent local-service pain without requiring phone APIs, AI voice, autodialing, telecom spend, or outbound calling. At $0 MRR, sell readiness and call-flow documentation only.',
        'beachhead_icp': 'Local home-service, med-spa, dental, legal intake, real estate, and appointment-based businesses where missed calls or after-hours inquiries can cost real revenue.',
        'offer': 'Free Missed-Call Leak Checklist; $299-$799 Call Flow & AI Receptionist Readiness Audit with intake worksheet, routing map, after-hours script, FAQ/call dispositions, escalation rules, manual call log, and implementation requirements; $500-$1,500/mo later only after a phone channel/tool is approved and justified by ROI.',
        'zero_cost_stack': ['public website/contact-path review','local call-flow templates','manual scripts','manual call log','no AI/prerecorded outbound calls','no phone API spend','no auto-dialing','no telecom setup'],
        'agent_workers': [
            worker('Operations Manager','operations-manager','Map call flows, routing rules, escalation paths, and manual fallback SOPs.'),
            worker('Sales Outreach','sales-outreach','Draft compliant inbound-response scripts and appointment-setting handoffs; no outbound execution.'),
            worker('Customer Success Manager','customer-success-manager','Define caller experience, response SLAs, and post-call follow-up standards.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Guard against unauthorized AI/prerecorded outbound calls, autodialing, spoofing, or telecom/KYC shortcuts.'),
            worker('Document Generator','document-generator','Package intake worksheet, call-flow map, scripts, and readiness report.')
        ],
        'next_safe_action': 'Draft a call-flow readiness template and sample missed-call revenue-leak checklist locally; no calls, phone APIs, or outreach.'
    },
    {
        'rank': 6,
        'name': 'Customer Support Knowledge-Base & Triage Readiness Sprint',
        'score_total': 69,
        'score_average': 8.63,
        'scores': {'startup_cost':10,'speed_to_first_revenue':8,'automation_potential':9,'margin':9,'recurring_revenue_potential':8,'fulfillment_complexity':8,'lead_acquisition_difficulty':8,'fit_with_agency_agents':9},
        'current_stage_fit': 'Strong but slightly behind because fulfillment may need client-specific support data. Zero-cost version is public FAQ/support-page review, triage tree, canned-response pack, and escalation rules, not helpdesk integration or chatbot claims.',
        'beachhead_icp': 'Small SaaS, ecommerce stores, agencies, clinics, and local-service teams with repeated questions, inconsistent replies, weak FAQ pages, and no escalation rules.',
        'offer': 'Free support FAQ gap checklist; $299-$799 support readiness sprint with top-25 FAQ outline, triage tree, escalation policy, canned replies, and weekly reporting template; $500-$1,200/mo KB refresh/reporting retainer.',
        'zero_cost_stack': ['public FAQ/site review','client-provided docs only after sale','local Markdown/CSV templates','no helpdesk login','no live chatbot claims'],
        'agent_workers': [
            worker('Customer Success Manager','customer-success-manager','Define support outcomes, triage priorities, and support-health metrics.'),
            worker('Content Creator','content-creator','Draft FAQ entries and canned replies.'),
            worker('Operations Manager','operations-manager','Build triage and escalation workflow.'),
            worker('Evidence Collector','evidence-collector','Collect public support-page gaps and examples.')
        ],
        'next_safe_action': 'Create KB/triage readiness checklist and sample triage tree locally; no helpdesk integrations.'
    },
    {
        'rank': 7,
        'name': 'B2B AI Governance Template Micro-Store',
        'score_total': 65,
        'score_average': 8.13,
        'scores': {'startup_cost':9,'speed_to_first_revenue':6,'automation_potential':9,'margin':10,'recurring_revenue_potential':6,'fulfillment_complexity':9,'lead_acquisition_difficulty':6,'fit_with_agency_agents':10},
        'current_stage_fit': 'Digital products are low-cost/high-margin, but marketplace setup, payment channel setup, competition, and distribution make it slower than direct B2B service sprints. Best now as derivative assets after service templates are proven.',
        'beachhead_icp': 'Consultants, agencies, fractional COOs, and SMB owners who want downloadable AI policy/training/tool-inventory templates.',
        'offer': '$19-$79 template pack: AI-use policy skeleton, shadow-AI tool inventory, prompt log, sensitive-data rules, training checklist, and manager review scorecard; later bundle with service sprint.',
        'zero_cost_stack': ['local docs','static landing page copy','manual checkout later only with approved payment channel','no Etsy/store signup from cron','no paid design tools'],
        'agent_workers': [
            worker('Document Generator','document-generator','Create clean PDF/DOCX/CSV templates.'),
            worker('Content Creator','content-creator','Write listing copy and buyer instructions.'),
            worker('Legal Compliance Checker','legal-compliance-checker','Keep disclaimers clear: templates are not legal advice.'),
            worker('Pricing Analyst','pricing-analyst','Test bundles and price points after a selling channel is approved.')
        ],
        'next_safe_action': 'Park as a derivative asset; do not open marketplaces or payment accounts until Brian approves a channel.'
    }
]

scored = {
    'last_updated': TS,
    'revenue': revenue,
    'scoring_scale': '1-10 where 10 is best. For startup_cost, 10 means lowest cost. For fulfillment_complexity and lead_acquisition_difficulty, 10 means easiest.',
    'criteria': ['startup_cost','speed_to_first_revenue','automation_potential','margin','recurring_revenue_potential','fulfillment_complexity','lead_acquisition_difficulty','fit_with_agency_agents'],
    'sources': sources,
    'opportunities': opportunities,
    'selected_for_current_stage': ['Shadow AI Policy & Tool Inventory Sprint','Employee AI Training & Prompt SOP Workshop'],
    'fresh_ideas_added_this_run': ['Missed-Call Revenue Leak & AI Receptionist Readiness Audit'],
    'safety_boundary': 'No emails, calls, form submissions, scans, client-system access, paid tools, marketplace/payment signups, or spending were performed.'
}

quests = [
    {
        'id': 'research_shadow_ai_policy_inventory_20260626_1616',
        'name': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'title': 'Build Shadow AI Policy & Tool Inventory Sprint',
        'desc': 'Research quest: create Shadow AI self-check, tool-inventory CSV, approved/prohibited-use matrix, sensitive-data rules, human-review checklist, and one-page AI policy skeleton. No scans, no client system access, no legal/security guarantees, no paid tools, and no outreach execution.',
        'reward': '+170 research XP', 'target': 6, 'current': 0, 'status': 'active',
        'assigned_agent': 'Data Privacy Officer', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Draft the six local templates; route legal/security decisions to human review.'
    },
    {
        'id': 'research_employee_ai_training_prompt_sop_20260626_1616',
        'name': 'Draft Employee AI Training & Prompt SOP Workshop',
        'title': 'Draft Employee AI Training & Prompt SOP Workshop',
        'desc': 'Research quest: create one-hour AI training outline, 20 role-safe starter prompts, prompt log, data-safety rules, review checklist, and manager scorecard. No client data collection, no paid course platform, no outbound execution.',
        'reward': '+145 research XP', 'target': 6, 'current': 0, 'status': 'active',
        'assigned_agent': 'Corporate Training Designer', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Draft local training assets as an upsell to the Shadow AI policy sprint.'
    },
    {
        'id': 'research_missed_call_receptionist_readiness_20260626_1616',
        'name': 'Draft Missed-Call Revenue Leak & AI Receptionist Readiness Audit',
        'title': 'Draft Missed-Call Revenue Leak & AI Receptionist Readiness Audit',
        'desc': 'Research quest: create missed-call leak checklist, intake worksheet, call-routing map, after-hours response script, escalation rules, and manual call log. No AI/prerecorded outbound calls, no phone API spend, no auto-dialing, no telecom setup, and no outreach execution.',
        'reward': '+130 research XP', 'target': 6, 'current': 0, 'status': 'queued',
        'assigned_agent': 'Operations Manager', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Draft call-flow/readiness templates locally only; do not place calls or connect telecom tools.'
    },
    {
        'id': 'research_ai_tool_stack_rationalization_20260626_1616',
        'name': 'Draft SMB AI Tool Stack Rationalization Sprint',
        'title': 'Draft SMB AI Tool Stack Rationalization Sprint',
        'desc': 'Research quest: create AI tool inventory CSV, duplicate-cost worksheet, workflow priority matrix, risk notes, and 30-day adoption roadmap. No SaaS logins, no paid tools, no client system access, no outbound execution.',
        'reward': '+125 research XP', 'target': 5, 'current': 0, 'status': 'queued',
        'assigned_agent': 'Tool Evaluator', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Draft local worksheets only; do not connect to client tools.'
    },
    {
        'id': 'research_support_kb_triage_20260626_1616',
        'name': 'Draft Support KB & Triage Readiness Sprint',
        'title': 'Draft Support KB & Triage Readiness Sprint',
        'desc': 'Research quest: create support FAQ gap checklist, top-25 FAQ template, triage tree, escalation policy, canned-response pack, and weekly support report template. No helpdesk access, no chatbot setup, no client data handling, and no outbound execution.',
        'reward': '+105 research XP', 'target': 6, 'current': 0, 'status': 'queued',
        'assigned_agent': 'Customer Success Manager', 'source': 'business_research_agent', 'updated_at': TS,
        'next_step': 'Draft sample templates from public/site-visible support patterns only.'
    }
]

backlog = f"""# Business Research Backlog

Last updated: {TS}
Revenue stage: $0 MRR from RPG Revenue Vault; 0 business revenue files found.
Rule applied: $0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution.

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
- 2026 shadow-AI and SMB AI-policy sources show the pain is practical: uncontrolled AI use, missing approved-tool lists, unclear data handling, weak training, and no incident path.
- U.S. Chamber-style SMB AI research signals owners expect AI to improve work, which makes policy + training a cash-oriented compliance/adoption wedge.
- This remains narrower and easier to sell than broad cyber consulting because the first deliverable is policy and inventory documentation only.

**Agent workers found in /root/agency-agents**
- Data Privacy Officer: `/root/agency-agents/integrations/codex/agents/data-privacy-officer.toml`
- Legal Compliance Checker: `/root/agency-agents/integrations/codex/agents/legal-compliance-checker.toml`
- Security Architect: `/root/agency-agents/integrations/codex/agents/security-architect.toml`
- Compliance Auditor: `/root/agency-agents/integrations/codex/agents/compliance-auditor.toml`
- Document Generator: `/root/agency-agents/integrations/codex/agents/document-generator.toml`

**Next safe action**
Build the six-template Shadow AI pack locally. No outreach, scans, client system access, paid tools, or legal/security guarantees.

---

## Current runner-up: Employee AI Training & Prompt SOP Workshop

**Why it stays high**
- It pairs naturally with Shadow AI: first create rules, then train staff to use approved prompts safely.
- Zero-cost fulfillment: workshop outline, prompt library, prompt log, review checklist, role-play exercises, and manager scorecard.

**Offer**
- Free AI Skills Gap Self-Assessment.
- Paid pack: $399-$999 role-based Prompt SOP Workshop with 20 approved prompts, data-safety rules, review checklist, prompt log, and manager scorecard.
- Retainer: $300-$900/mo prompt-library refresh and office-hours after first sale.

**Workers:** Corporate Training Designer, Prompt Engineer, Data Privacy Officer, Document Generator, Business Strategist.

**Next safe action:** draft workshop outline, 20 role-safe starter prompts, prompt review checklist, and manager scorecard locally.

---

## Fresh opportunity added this run: Missed-Call Revenue Leak & AI Receptionist Readiness Audit

**Why it is worth tracking**
- Current AI receptionist/missed-call search results show a strong buyer pain around real leads, after-hours calls, voicemail drop-off, and missed-call revenue leakage.
- At $0 MRR we can sell the diagnostic/readiness layer only: call-flow map, scripts, escalation, manual logs, and implementation requirements.
- This avoids the expensive/risky parts until justified: no AI voice, no prerecorded outbound calls, no phone APIs, no autodialing, no telecom/KYC setup.

**Offer**
- Free Missed-Call Leak Checklist.
- Paid audit: $299-$799 Call Flow & AI Receptionist Readiness Audit with intake worksheet, routing map, after-hours script, FAQ/call dispositions, escalation rules, manual call log, and implementation requirements.
- Future retainer: $500-$1,500/mo only after a verified phone channel/tool is approved and ROI is clear.

**Workers:** Operations Manager, Sales Outreach, Customer Success Manager, Legal Compliance Checker, Document Generator.

**Next safe action:** draft the call-flow readiness template and missed-call checklist locally; no calls, phone APIs, or outreach.

---

## Keep scaling: AI Search Visibility & LLMs.txt Retrofit Snapshot

Still a strong already-started zero-cost service. Current GEO/AEO/AI-search sources show AI search is reshaping SEO toward extractability, trust, citations, and AI-readable source guidance. Keep producing public website samples and sharpen the monthly retainer. Do not claim ranking/citation guarantees.

**Workers:** AI Citation Strategist, SEO Specialist, Content Creator, Evidence Collector, Offer & Lead Gen Strategist.

**Next safe action:** score 3 more public websites and create a short before/after llms.txt/source-map example.

---

## Other scored opportunities

### SMB AI Tool Stack Rationalization Sprint
- Offer: free AI tool sprawl checklist; $399-$899 tool-stack rationalization sprint; later implementation governance after approved channels/tools.
- Workers: Tool Evaluator, Operations Manager, Pricing Analyst, Document Generator.
- Safe next action: draft tool-inventory CSV and workflow priority matrix; no SaaS logins or paid tools.

### Customer Support Knowledge-Base & Triage Readiness Sprint
- Offer: free FAQ gap checklist; $299-$799 support readiness sprint; $500-$1,200/mo KB refresh/reporting retainer after sale.
- Workers: Customer Success Manager, Content Creator, Operations Manager, Evidence Collector.
- Safe next action: create KB/triage readiness checklist and sample triage tree locally; no helpdesk integrations.

### B2B AI Governance Template Micro-Store
- Offer: $19-$79 downloadable AI governance template pack after a channel is approved.
- Workers: Document Generator, Content Creator, Legal Compliance Checker, Pricing Analyst.
- Safe next action: park as derivative assets; do not open marketplaces/payment accounts from cron.

## Scoreboard

| Rank | Idea | Score | Stage fit |
|---:|---|---:|---|
| 1 | Shadow AI Policy & Tool Inventory Sprint | 76/80 | Best $0-MRR opportunity |
| 2 | Employee AI Training & Prompt SOP Workshop | 73/80 | Best natural upsell |
| 3 | AI Search Visibility & LLMs.txt Retrofit Snapshot | 72/80 | Already launched and still strong |
| 4 | SMB AI Tool Stack Rationalization Sprint | 71/80 | Adjacent governance/workflow offer |
| 5 | Missed-Call Revenue Leak & AI Receptionist Readiness Audit | 70/80 | Fresh docs-only local-service diagnostic |
| 6 | Customer Support Knowledge-Base & Triage Readiness Sprint | 69/80 | Good, but more client-data dependent |
| 7 | B2B AI Governance Template Micro-Store | 65/80 | High-margin derivative, slower channel |
"""

report = f"""# Business Research Agent — Latest Report

Updated: {TS}

## Revenue check
- Current MRR: **$0**.
- Evidence: RPG Revenue Vault monthlyRevenue is 0; 0 business revenue files found under /root/ai-holding-company/businesses.
- Rule applied: **$0-$500 MRR: zero-cost businesses only; no paid SaaS/tools, no outbound execution**.

## Best idea now
**Shadow AI Policy & Tool Inventory Sprint** — **76/80**

Why it wins:
- Most direct $0-MRR path: document/interview deliverables only, no scans, no credentials, no paid SaaS, no legal/security guarantees.
- Current 2026 SMB AI-policy/shadow-AI sources validate the pain: owners need approved-tool lists, data rules, review rules, shadow-AI visibility, and incident handling.
- Strong retainer path: quarterly policy refresh, staff training, approved-tool evidence log, and governance review.
- Strong Agency Agents fit: Data Privacy Officer, Legal Compliance Checker, Security Architect, Compliance Auditor, Document Generator.

## Runner-up to build next
**Employee AI Training & Prompt SOP Workshop** — **73/80**

Why it is worth building:
- Natural upsell after policy: once rules exist, staff need approved prompts, review workflows, prompt logs, and manager scorecards.
- Zero-cost fulfillment: local workshop deck, role-safe prompt library, prompt log, review checklist, and manager scorecard.

## Fresh idea added
**Missed-Call Revenue Leak & AI Receptionist Readiness Audit** — **70/80**

Why it is worth tracking:
- Current AI receptionist/missed-call search results validate a local-business pain around real leads, after-hours calls, voicemail drop-off, and missed-call revenue leakage.
- Safe at $0 MRR if kept docs-only: readiness worksheet, call-flow map, after-hours scripts, escalation rules, and manual call log.
- Blocked actions: no AI/prerecorded outbound calls, no phone API spend, no auto-dialing, no telecom setup, no outreach execution.

## Keep active
**AI Search Visibility & LLMs.txt Retrofit Snapshot** — **72/80**

Why it stays active:
- Already partially launched and still fits $0 MRR.
- Current AI-search/GEO/llms.txt sources show commercial education around extractability, trust, AEO, and AI-readable source maps.
- Public-site review + local reports can create samples without paid tools or client access.

## Scored ideas
1. Shadow AI Policy & Tool Inventory Sprint — 76/80
2. Employee AI Training & Prompt SOP Workshop — 73/80
3. AI Search Visibility & LLMs.txt Retrofit Snapshot — 72/80
4. SMB AI Tool Stack Rationalization Sprint — 71/80
5. Missed-Call Revenue Leak & AI Receptionist Readiness Audit — 70/80
6. Customer Support Knowledge-Base & Triage Readiness Sprint — 69/80
7. B2B AI Governance Template Micro-Store — 65/80

## Game-ready quests prepared
- Build Shadow AI Policy & Tool Inventory Sprint — assigned to Data Privacy Officer.
- Draft Employee AI Training & Prompt SOP Workshop — assigned to Corporate Training Designer.
- Draft Missed-Call Revenue Leak & AI Receptionist Readiness Audit — assigned to Operations Manager.
- Draft SMB AI Tool Stack Rationalization Sprint — assigned to Tool Evaluator.
- Draft Support KB & Triage Readiness Sprint — assigned to Customer Success Manager.

## Next safe action
Build the Shadow AI six-template pack locally, then draft the Employee AI Training workshop outline. Keep the missed-call/receptionist idea as a docs-only local-service diagnostic. Do **not** contact prospects, submit forms, access client systems, run scans, place calls, send emails, connect SaaS/phone tools, open marketplaces, or spend money.

## Artifacts updated
- `/root/ai-holding-company/business-research-agent/ideas/backlog.md`
- `/root/ai-holding-company/business-research-agent/ideas/scored-opportunities.json`
- `/root/ai-holding-company/business-research-agent/reports/latest.md`
- `/root/ai-holding-company/business-research-agent/game/research_quests.json`
- `/root/ai-holding-company/rpg-command-center/engine/public/game_state.json` updated non-destructively with research quests/status/event.
"""

(RESEARCH / 'ideas').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'reports').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'game').mkdir(parents=True, exist_ok=True)
(RESEARCH / 'ideas/backlog.md').write_text(backlog)
(RESEARCH / 'ideas/scored-opportunities.json').write_text(json.dumps(scored, indent=2) + '\n')
(RESEARCH / 'reports/latest.md').write_text(report)
(RESEARCH / 'game/research_quests.json').write_text(json.dumps({'last_updated': TS, 'quests': quests}, indent=2) + '\n')

state = json.loads(GAME_STATE.read_text())
existing_ids = {q.get('id') for q in state.get('quests', [])}
for q in quests:
    if q['id'] not in existing_ids:
        state.setdefault('quests', []).append(q)

# Update Business Research Agent visible status if present.
for agent in state.get('agents', []):
    if agent.get('name') == 'Business Research Agent':
        agent['status'] = 'working'
        agent['current_task'] = 'Confirmed Shadow AI Policy & Tool Inventory Sprint as best $0-MRR opportunity; added Missed-Call Revenue Leak & AI Receptionist Readiness as a docs-only local-service runner-up. No outreach or spend.'
        agent['last_seen'] = TS
        agent['last_message'] = 'Best $0-MRR idea remains Shadow AI Policy & Tool Inventory Sprint. Fresh idea added: Missed-Call Revenue Leak & AI Receptionist Readiness Audit.'

state['timestamp'] = TS
state.setdefault('events', []).append({
    'timestamp': TS,
    'type': 'research_update',
    'agent': 'Business Research Agent',
    'message': 'Confirmed Shadow AI Policy & Tool Inventory Sprint as best $0-MRR opportunity; added Missed-Call Revenue Leak & AI Receptionist Readiness as a docs-only local-service runner-up. Safe quests only; no outreach or spend.',
    'source': 'business_research_agent'
})
GAME_STATE.write_text(json.dumps(state, indent=2) + '\n')

print('updated artifacts')
print('opportunities', len(opportunities))
print('quests', [q['id'] for q in quests])
