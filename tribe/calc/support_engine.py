#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

BASE = Path('/root/ai-holding-company/tribe')

def load_state():
    p = BASE / 'state/tribe.json'
    return json.loads(p.read_text()) if p.exists() else {}

def weekly_income() -> float:
    state = load_state()
    return float(state.get('financial', {}).get('ssi_base', 943)) + float(state.get('financial', {}).get('side_income_est', 600))

def child_support_total(wives: dict, weekly_income: float | None = None) -> float:
    """
    Total child support pool = 50% of eligible weekly income.
    Split equally among all children across all wives/mothers.
    """
    if weekly_income is None:
        weekly_income = weekly_income()
    total_children = sum(int(w.get('children', 0) or 0) for w in wives.values())
    if total_children <= 0:
        return 0.0
    return round(weekly_income * 0.50, 6)

def child_support_for(wives: dict, weekly_income: float | None = None) -> dict:
    """
    Returns per-wife child support amount.
    Each child gets an equal share of the 50% pool.
    """
    pool = child_support_total(wives, weekly_income)
    total_children = sum(int(w.get('children', 0) or 0) for w in wives.values())
    if total_children <= 0:
        return {wid: 0.0 for wid in wives}
    per_child = round(pool / total_children, 6)
    return {wid: round(per_child * int(w.get('children', 0) or 0), 6) for wid, w in wives.items()}

def rent_and_needs(wives: dict, sister_rent: float = 0.0) -> dict:
    total_rent = sum(float(w.get('rent', 0) or 0) for w in wives.values()) + sister_rent
    return {
        'total_rent': total_rent,
        'sister_rent': sister_rent,
        'total_weekly_needs': total_rent,
        'income': weekly_income(),
        'surplus_deficit': weekly_income() - total_rent,
    }

def build_schedule(wives: dict, sister_wallet: str | None = None, sister_rent: float = 0.0) -> dict:
    weekly = weekly_income()
    per_wife_child_support = child_support_for(wives, weekly)
    rent_info = rent_and_needs(wives, sister_rent)
    schedule = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'weekly_income': weekly,
        'tribe_fund_first': True,
        'payments': []
    }
    for wid, w in wives.items():
        rent = float(w.get('rent', 0) or 0)
        schedule['payments'].append({
            'wife_id': wid,
            'name': w.get('name', wid),
            'wallet': w.get('wallet', ''),
            'rent': rent,
            'children': int(w.get('children', 0) or 0),
            'child_support_total': per_wife_child_support.get(wid, 0.0),
            'child_support_per_child': round(per_wife_child_support.get(wid, 0.0) / max(1, int(w.get('children', 0) or 0)), 6) if int(w.get('children', 0) or 0) > 0 else 0.0,
            'personal_buffer': 0.0,
            'notes': 'Rent paid from tribe fund first'
        })
    if sister_wallet and sister_rent > 0:
        schedule['payments'].append({
            'wife_id': 'sister',
            'name': 'Sister',
            'wallet': sister_wallet,
            'rent': sister_rent,
            'children': 0,
            'child_support_total': 0.0,
            'child_support_per_child': 0.0,
            'personal_buffer': 0.0,
            'notes': 'Rent covered by tribe fund'
        })
    schedule['summary'] = {
        'total_rent_burden': rent_info['total_weekly_needs'],
        'remaining_after_rent': round(weekly - rent_info['total_weekly_needs'], 6),
        'child_support_pool': round(child_support_total(wives, weekly), 6),
        'brian_keep': round((weekly - rent_info['total_weekly_needs']) * 0.5, 6),
        'tribe_buffer': round((weekly - rent_info['total_weekly_needs']) * 0.5, 6),
    }
    return schedule

if __name__ == '__main__':
    out = BASE / 'calc/schedule.json'
    example = {
        'wives': {
            '1': {'name':'Wife 1','wallet':'0x','rent':700,'children':1},
            '2': {'name':'Wife 2','wallet':'0x','rent':700,'children':2},
        },
        'sister_wallet':'0x',
        'sister_rent':0
    }
    schedule = build_schedule(example['wives'], example['sister_wallet'], example['sister_rent'])
    out.write_text(json.dumps(schedule, indent=2))
    print(json.dumps(schedule, indent=2))
