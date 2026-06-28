#!/usr/bin/env python3
import json
from pathlib import Path

path = Path('/root/ai-holding-company/rpg-command-center/engine/public/game_state.json')
ts = '2026-06-25T15:39:26Z'
state = json.loads(path.read_text())
quests = state.setdefault('quests', [])
quest_id = 'research_ai_search_snapshot_20260625_1539'
quest = {
    'id': quest_id,
    'name': 'Build AI Search Readiness Snapshot Template',
    'desc': 'Research quest: create a reusable one-page AI Search Readiness Snapshot and score 3 public local-business websites. No outreach, no paid tools, no forms submitted.',
    'reward': '+110 research XP',
    'target': 3,
    'current': 0,
    'status': 'active',
    'assigned_agent': 'AI Citation Strategist',
    'source': 'business_research_agent',
    'updated_at': ts,
    'next_step': 'Build the template and sample report from public pages only.'
}
for i, existing in enumerate(quests):
    if existing.get('id') == quest_id:
        quests[i] = {**existing, **quest}
        break
else:
    quests.append(quest)

# Update Business Research Agent visible status if present.
for agent in state.get('agents', []):
    if agent.get('name') == 'Business Research Agent':
        agent['status'] = 'working'
        agent['current_task'] = 'Queued AI Search Readiness Snapshot template quest; no outreach or spend.'
        agent['last_seen'] = ts
        agent['last_message'] = 'Best $0-MRR idea: AI Search Visibility & Agent-Readable Content Retrofit.'
        break

state.setdefault('events', []).append({
    'timestamp': ts,
    'type': 'research_update',
    'agent': 'Business Research Agent',
    'message': 'Selected AI Search Visibility & Agent-Readable Content Retrofit as the best $0-MRR opportunity and queued a snapshot-template quest.',
    'source': 'business_research_agent'
})
state['timestamp'] = ts
path.write_text(json.dumps(state, indent=2) + '\n')
print(f'updated {path}: quests={len(state.get("quests", []))}, events={len(state.get("events", []))}')
