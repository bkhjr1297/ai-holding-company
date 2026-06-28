#!/usr/bin/env python3
"""
Register spawned worker agents into Agent Farm RPG game_state.json.
Every agent/process/cron/delegated worker should become an in-game NPC.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/root/ai-holding-company')
STATE_PATH = ROOT / 'rpg-command-center/engine/public/game_state.json'
REGISTRY_PATH = ROOT / 'rpg-command-center/engine/spawned_agents_registry.json'

DEFAULT_POSITIONS = [
    (7, 7), (14, 6), (20, 8), (10, 12), (17, 13), (23, 11),
    (6, 14), (13, 3), (21, 4), (4, 10), (15, 10), (24, 14),
]

EMOJI_BY_ROLE = {
    'research': '🔎',
    'business': '💼',
    'sales': '🎯',
    'support': '🎧',
    'operations': '⚙️',
    'finance': '💰',
    'game': '🎮',
    'rpg': '🎮',
    'asset': '🎨',
    'design': '🎨',
    'code': '💻',
    'engineering': '💻',
    'default': '🤖',
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text())
    except Exception:
        return fallback


def save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2))


def agent_id(name: str, source: str) -> str:
    raw = f'{source}:{name}'.encode()
    return hashlib.sha1(raw).hexdigest()[:12]


def infer_emoji(role: str, task: str) -> str:
    combined = f'{role} {task}'.lower()
    for key, emoji in EMOJI_BY_ROLE.items():
        if key in combined:
            return emoji
    return EMOJI_BY_ROLE['default']


def position_for(agent_key: str, current_count: int):
    h = int(hashlib.sha1(agent_key.encode()).hexdigest(), 16)
    if current_count < len(DEFAULT_POSITIONS):
        return DEFAULT_POSITIONS[current_count]
    return 4 + (h % 21), 3 + ((h >> 8) % 11)


def register(name: str, role: str, task: str, source: str, status: str):
    state = load_json(STATE_PATH, {'buildings': {}, 'agents': [], 'quests': [], 'resources': {}})
    registry = load_json(REGISTRY_PATH, {'agents': [], 'updated_at': now()})
    agents = state.setdefault('agents', [])
    reg_agents = registry.setdefault('agents', [])

    aid = agent_id(name, source)
    existing = next((a for a in agents if a.get('id') == aid or a.get('name') == name), None)
    if existing:
        existing.update({
            'id': aid,
            'name': name,
            'role': role or existing.get('role', 'Worker Agent'),
            'status': status,
            'current_task': task or existing.get('current_task', 'Standing by'),
            'source': source,
            'emoji': infer_emoji(role, task),
            'last_seen': now(),
            'spawned': True,
        })
    else:
        x, y = position_for(aid, len(agents))
        agents.append({
            'id': aid,
            'name': name,
            'role': role or 'Worker Agent',
            'status': status,
            'current_task': task or 'Standing by',
            'source': source,
            'emoji': infer_emoji(role, task),
            'x': x,
            'y': y,
            'spawned': True,
            'created_at': now(),
            'last_seen': now(),
            'dialogue': [
                f"I'm {name}. I'm working on {task or 'the current company mission'}.",
                "Talk to me to change priorities or ask for a status update.",
            ],
        })

    reg_existing = next((a for a in reg_agents if a.get('id') == aid), None)
    record = {
        'id': aid,
        'name': name,
        'role': role,
        'current_task': task,
        'source': source,
        'status': status,
        'last_seen': now(),
    }
    if reg_existing:
        reg_existing.update(record)
    else:
        record['created_at'] = now()
        reg_agents.append(record)

    registry['updated_at'] = now()
    state['timestamp'] = now()
    save_json(STATE_PATH, state)
    save_json(REGISTRY_PATH, registry)
    print(json.dumps({'registered': name, 'id': aid, 'agents_total': len(agents)}, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--role', default='Worker Agent')
    parser.add_argument('--task', default='Working on the active mission')
    parser.add_argument('--source', default='manual-spawn')
    parser.add_argument('--status', default='working')
    args = parser.parse_args()
    register(args.name, args.role, args.task, args.source, args.status)


if __name__ == '__main__':
    main()
