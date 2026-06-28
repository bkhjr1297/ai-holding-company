#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

BASE = Path('/root/ai-holding-company/tribe')
STATE = BASE / 'state/tribe.json'
LOG = BASE / 'logs/rotation.jsonl'

DEFAULT_ORDER = [f"wife{n}" for n in range(1, 6)]


def load_state() -> dict:
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2))


def log_event(event: str, detail: dict) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **detail}
    with LOG.open('a') as f:
        f.write(json.dumps(entry) + '\n')


def normalize_rotation(state: dict) -> dict:
    state.setdefault('rotation', {})
    state['rotation'].setdefault('order', DEFAULT_ORDER)
    state['rotation'].setdefault('cursor', 0)
    state['rotation'].setdefault('exceptions', {
        'wife_hospitalized': True,
        'child_hospitalized': True,
    })
    return state


def current_scheduled_visitor(state: dict) -> dict:
    order = state.get('rotation', {}).get('order', DEFAULT_ORDER)
    cursor = int(state.get('rotation', {}).get('cursor', 0))
    wife_id = order[cursor % max(len(order), 1)]
    return {'wife_id': wife_id, 'cursor': cursor, 'order': order}


def advance_rotation(state: dict, steps: int = 1) -> dict:
    state = normalize_rotation(state)
    order = state['rotation']['order']
    cursor = int(state['rotation']['cursor'])
    cursor = (cursor + max(steps, 1)) % max(len(order), 1)
    state['rotation']['cursor'] = cursor
    save_state(state)
    log_event('rotation_advanced', {'new_cursor': cursor, 'current': order[cursor]})
    return current_scheduled_visitor(state)


def emergency_override(state: dict, reason_type: str) -> dict:
    state = normalize_rotation(state)
    order = state['rotation']['order']
    cursor = int(state['rotation']['cursor'])
    current = order[cursor % max(len(order), 1)]
    # Skip the current scheduled wife and move to the next active one.
    cursor = (cursor + 1) % max(len(order), 1)
    state['rotation']['cursor'] = cursor
    state['rotation']['last_emergency'] = {
        'reason': reason_type,
        'overridden': current,
        'replacement': order[cursor],
        'at': datetime.now(timezone.utc).isoformat(),
    }
    save_state(state)
    log_event('emergency_rotation_override', {
        'reason': reason_type,
        'overridden': current,
        'replacement': order[cursor],
    })
    return current_scheduled_visitor(state)


def set_rotation_order(state: dict, order: list[str]) -> dict:
    state = normalize_rotation(state)
    state['rotation']['order'] = order
    state['rotation']['cursor'] = 0
    save_state(state)
    log_event('rotation_order_set', {'order': order})
    return current_scheduled_visitor(state)


def run() -> dict:
    state = load_state()
    state = normalize_rotation(state)
    save_state(state)
    return current_scheduled_visitor(state)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
