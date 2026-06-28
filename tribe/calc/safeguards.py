#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

STATE = Path('/root/ai-holding-company/tribe/state/tribe.json')
LEDGER = Path('/root/ai-holding-company/tribe/logs/ledger.jsonl')

DEFAULTS = {
    'stage': 0,
    'members': ['brian', 'sister'],
    'min_reserve_eth': 0.0001,
    'min_reserve_usdc': 5.0,
    'weekly_income_required': 2388.0,
    'buffer_pct': 0.20,
    'balances': {
        'cashclaw_eth': 0.0,
        'agentcash_usdc': 0.0,
        'pinch_usdc': 0.0,
    },
}

def load() -> dict:
    if STATE.exists():
        data = json.loads(STATE.read_text())
    else:
        data = {}
    # Merge with defaults so missing keys don’t break checks
    merged = {**DEFAULTS, **data}
    merged['balances'] = {**DEFAULTS['balances'], **data.get('balances', {})}
    return merged

def save(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2))

def log(kind: str, detail: str) -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'event': kind,
        'detail': detail,
    }
    with LEDGER.open('a') as f:
        f.write(json.dumps(entry) + '\n')

def enforce_stage(state: dict) -> dict:
    # Scale down if income drops; don’t auto-advance
    total = (
        float(state['balances']['cashclaw_eth'] or 0)
        + float(state['balances']['agentcash_usdc'] or 0)
        + float(state['balances']['pinch_usdc'] or 0)
    )
    if total < 6690:
        state['stage'] = 0
        state['members'] = ['brian', 'sister']
        state['weekly_income_required'] = 2388.0
    elif total < 3582:
        state['stage'] = 1
        state['members'] = ['brian', 'sister', 'wife1']
        state['weekly_income_required'] = 3582.0
    elif total < 4776:
        state['stage'] = 2
        state['members'] = ['brian', 'sister', 'wife1']
        state['weekly_income_required'] = 4776.0
    elif total < 6690:
        state['stage'] = 3
        state['members'] = ['brian', 'sister', 'wife1', 'wife2']
        state['weekly_income_required'] = 6690.0
    return state

def can_payout(state: dict) -> tuple[bool, str]:
    eth = float(state['balances']['cashclaw_eth'] or 0)
    usdc = float(state['balances']['agentcash_usdc'] or 0) + float(state['balances']['pinch_usdc'] or 0)
    required = float(state['weekly_income_required'])
    required = required or 2388.0
    min_eth = float(state['min_reserve_eth'] or 0.0001)
    min_usdc = float(state['min_reserve_usdc'] or 5.0)

    if eth < min_eth:
        return False, f'ETH below reserve floor: {eth} < {min_eth}'
    if usdc < min_usdc:
        return False, f'USDC below reserve floor: {usdc} < {min_usdc}'
    if (eth + usdc) < required:
        return False, f'Total {eth + usdc} < weekly requirement {required}'
    buffer = required * float(state.get('buffer_pct', 0.20))
    if (eth + usdc) < (required + buffer):
        return False, f'Total {eth + usdc} would breach 20% buffer after payouts'
    return True, 'OK'

def run() -> dict:
    state = load()
    state = enforce_stage(state)
    ok, reason = can_payout(state)
    state['last_check'] = datetime.now(timezone.utc).isoformat()
    state['payout_allowed'] = ok
    state['payout_block_reason'] = reason if not ok else None
    save(state)
    log('safeguard_check', json.dumps({
        'ok': ok,
        'reason': reason,
        'stage': state['stage'],
        'weekly_required': state['weekly_income_required'],
    }))
    return state

if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
