#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional

TRIBE_STATE = Path('/root/ai-holding-company/tribe/state/tribe.json')
RETIREMENT_STATE = Path('/root/ai-holding-company/tribe/state/retirement.json')
LEDGER = Path('/root/ai-holding-company/tribe/logs/ledger.jsonl')

RETIREMENT_AGE = 65
EARLY_WITHDRAWAL_PENALTY = 0.10
MIN_RETIREMENT_CONTRIBUTION_PCT = 0.05  # 5% of eligible income
MAX_RETIREMENT_CONTRIBUTION_PCT = 0.15  # 15% cap
RETIREMENT_INVESTMENT_PROFILE = {
    'conservative': {'bonds': 0.6, 'dividend_equities': 0.3, 'cash': 0.1},
    'moderate': {'bonds': 0.4, 'dividend_equities': 0.4, 'growth_equities': 0.15, 'cash': 0.05},
    'aggressive': {'bonds': 0.2, 'dividend_equities': 0.3, 'growth_equities': 0.45, 'cash': 0.05},
}
DEFAULT_INVESTMENT_PROFILE = 'moderate'

def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default

def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2))

def log_event(kind: str, detail: str) -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'event': kind,
        'detail': detail,
    }
    with LEDGER.open('a') as f:
        f.write(json.dumps(entry) + '\n')

def get_tribe_state() -> dict:
    return load_json(TRIBE_STATE, {})

def get_retirement_state() -> dict:
    default = {
        'accounts': {},
        'total_assets': 0.0,
        'settings': {
            'retirement_age': RETIREMENT_AGE,
            'min_contribution_pct': MIN_RETIREMENT_CONTRIBUTION_PCT,
            'max_contribution_pct': MAX_RETIREMENT_CONTRIBUTION_PCT,
            'default_investment_profile': DEFAULT_INVESTMENT_PROFILE,
        },
    }
    return load_json(RETIREMENT_STATE, default)

def save_retirement_state(state: dict) -> None:
    save_json(RETIREMENT_STATE, state)

def ensure_account(state: dict, member: str) -> dict:
    if member not in state['accounts']:
        state['accounts'][member] = {
            'balance': 0.0,
            'contributions': 0.0,
            'gains': 0.0,
            'investment_profile': DEFAULT_INVESTMENT_PROFILE,
            'allocation': RETIREMENT_INVESTMENT_PROFILE[DEFAULT_INVESTMENT_PROFILE].copy(),
            'retirement_age': RETIREMENT_AGE,
            'status': 'active',
            'opened_at': datetime.now(timezone.utc).isoformat(),
        }
    return state['accounts'][member]

def contribute(state: dict, member: str, amount: float) -> dict:
    account = ensure_account(state, member)
    account['balance'] += amount
    account['contributions'] += amount
    log_event('retirement_contribution', json.dumps({'member': member, 'amount': amount, 'balance': account['balance']}))
    return account

def rebalance(state: dict, member: str, profile_name: Optional[str] = None) -> dict:
    account = ensure_account(state, member)
    profile = profile_name or account['investment_profile']
    if profile not in RETIREMENT_INVESTMENT_PROFILE:
        raise ValueError(f'Unknown profile: {profile}')
    account['investment_profile'] = profile
    account['allocation'] = RETIREMENT_INVESTMENT_PROFILE[profile].copy()
    log_event('retirement_rebalance', json.dumps({'member': member, 'profile': profile, 'allocation': account['allocation']}))
    return account

def simulate_growth(state: dict, member: str, rate: float) -> float:
    account = ensure_account(state, member)
    if account['status'] == 'retired':
        growth = account['balance'] * rate
        account['gains'] += growth
        account['balance'] += growth
        log_event('retirement_growth', json.dumps({'member': member, 'rate': rate, 'growth': growth}))
        return growth
    return 0.0

def withdraw(state: dict, member: str, amount: float) -> dict:
    account = ensure_account(state, member)
    tribe = get_tribe_state()
    age = tribe.get('members_ages', {}).get(member, 0)

    if account['status'] != 'retired' and age < RETIREMENT_AGE:
        penalty = amount * EARLY_WITHDRAWAL_PENALTY
        net = amount - penalty
        account['balance'] -= amount
        log_event('retirement_early_withdrawal', json.dumps({
            'member': member, 'amount': amount, 'penalty': penalty, 'net': net
        }))
        return account

    if amount > account['balance']:
        raise ValueError('Insufficient retirement balance')

    account['balance'] -= amount
    log_event('retirement_withdrawal', json.dumps({'member': member, 'amount': amount, 'balance': account['balance']}))
    return account

def recalc_total(state: dict) -> float:
    total = sum(acc['balance'] for acc in state['accounts'].values())
    state['total_assets'] = total
    return total

def add_retirement_member(member: str, age: int, profile: Optional[str] = None) -> dict:
    tribe = get_tribe_state()
    if 'members_ages' not in tribe:
        tribe['members_ages'] = {}
    tribe['members_ages'][member] = age

    ret = get_retirement_state()
    account = ensure_account(ret, member)
    if profile and profile in RETIREMENT_INVESTMENT_PROFILE:
        account['investment_profile'] = profile
        account['allocation'] = RETIREMENT_INVESTMENT_PROFILE[profile].copy()
    if age >= RETIREMENT_AGE:
        account['status'] = 'retired'
    save_retirement_state(ret)

    save_json(TRIBE_STATE, tribe)
    recalc_total(ret)
    save_retirement_state(ret)
    log_event('retirement_account_opened', json.dumps({'member': member, 'age': age, 'profile': account['investment_profile']}))
    return account

def get_summary() -> dict:
    tribe = get_tribe_state()
    ret = get_retirement_state()
    total = recalc_total(ret)
    return {
        'retirement_age': RETIREMENT_AGE,
        'total_assets': total,
        'accounts': {
            member: {
                'balance': round(acc['balance'], 2),
                'status': acc['status'],
                'profile': acc['investment_profile'],
                'allocation': acc['allocation'],
            }
            for member, acc in ret['accounts'].items()
        },
    }

if __name__ == '__main__':
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'summary'
    if cmd == 'summary':
        print(json.dumps(get_summary(), indent=2))
    elif cmd == 'add':
        member = sys.argv[2]
        age = int(sys.argv[3])
        profile = sys.argv[4] if len(sys.argv) > 4 else None
        print(json.dumps(add_retirement_member(member, age, profile), indent=2))
    elif cmd == 'withdraw':
        member = sys.argv[2]
        amount = float(sys.argv[3])
        ret = get_retirement_state()
        account = withdraw(ret, member, amount)
        save_retirement_state(ret)
        print(json.dumps(account, indent=2))
    else:
        print('Commands: summary | add <member> <age> [profile] | withdraw <member> <amount>')
