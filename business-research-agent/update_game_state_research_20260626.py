#!/usr/bin/env python3
import json
from pathlib import Path

p = Path('/root/ai-holding-company/rpg-command-center/engine/public/game_state.json')
now = '2026-06-26T04:01:56Z'
state = json.loads(p.read_text())
quests = state.setdefault('quests', [])
existing = {q.get('id'): q for q in quests}
new_quests = [
    {
        "id": "research_smb_ai_agent_safety_templates_20260626",
        "name": "Build SMB AI Agent Safety Template Pack",
        "title": "Build SMB AI Agent Safety Template Pack",
        "desc": "Research quest: create AI-agent safety self-check, policy skeleton, permission map, readiness report, and risk register using public guidance only. No scans, no client system access, no legal/security guarantees, no paid tools, no outreach.",
        "reward": "+150 research XP",
        "target": 5,
        "current": 0,
        "status": "active",
        "assigned_agent": "Security Architect",
        "source": "business_research_agent",
        "updated_at": now,
        "next_step": "Draft the five local templates and route legal/security decisions to human review."
    },
    {
        "id": "research_ai_search_llms_samples_20260626",
        "name": "Add AI Search + LLMs.txt Source-Map Samples",
        "title": "Add AI Search + LLMs.txt Source-Map Samples",
        "desc": "Research quest: produce 3 public-site AI Search/LLMs.txt readiness samples and one before/after source-map example. No outreach, no paid tools, no form submissions, no ranking guarantees.",
        "reward": "+125 research XP",
        "target": 4,
        "current": 0,
        "status": "active",
        "assigned_agent": "AI Citation Strategist",
        "source": "business_research_agent",
        "updated_at": now,
        "next_step": "Use public pages only; save local samples and improvement notes."
    },
    {
        "id": "research_invoice_admin_readiness_20260626",
        "name": "Draft Invoice & Admin Workflow Readiness Audit",
        "title": "Draft Invoice & Admin Workflow Readiness Audit",
        "desc": "Research quest: create invoice/admin workflow worksheet, approval matrix, data-field checklist, exception rules, and ROI calculator. No bank/accounting credentials, no AP tool connections, no spend.",
        "reward": "+110 research XP",
        "target": 5,
        "current": 0,
        "status": "queued",
        "assigned_agent": "Operations Manager",
        "source": "business_research_agent",
        "updated_at": now,
        "next_step": "Build local templates only; no accounting access or live integrations."
    }
]
for q in new_quests:
    if q['id'] in existing:
        existing[q['id']].update(q)
    else:
        quests.append(q)

# Update visible Business Research Agent if present.
for agent in state.get('agents', []):
    if agent.get('name') == 'Business Research Agent':
        agent['status'] = 'working'
        agent['current_task'] = 'Queued AI Agent Safety templates, AI Search/LLMs.txt samples, and invoice/admin readiness research; no outreach or spend.'
        agent['last_seen'] = now
        agent['last_message'] = 'Best $0-MRR idea remains SMB AI Agent Safety & Cyber Readiness; fresh runners-up: invoice/admin workflow readiness and support KB triage.'
        break

state['timestamp'] = now
state.setdefault('events', []).append({
    "timestamp": now,
    "type": "research_update",
    "agent": "Business Research Agent",
    "message": "Selected SMB AI Agent Safety & Cyber Readiness as the best $0-MRR opportunity, kept AI Search/LLMs.txt active, and added invoice/admin workflow readiness plus support KB triage as fresh queued research. Safe quests only; no outreach or spend.",
    "source": "business_research_agent"
})
p.write_text(json.dumps(state, indent=2) + '\n')
print(f"updated {p}")
print(f"quests={len(state.get('quests', []))} events={len(state.get('events', []))}")
