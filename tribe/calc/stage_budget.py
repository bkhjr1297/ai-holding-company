#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional

BASE = Path('/root/ai-holding-company/tribe')

# NYC weekly costs
NYC = {
    'rent': {'studio': 600, '1br': 750, '2br': 950, '3br': 1200, '4br': 1400},
    'per_adult_weekly': 245,  # utilities + food + transport + phone + health + personal
    'per_child_weekly': 100,  # food + transport_extra + activities + clothing + health
    'buffer_pct': 0.20,
}

def default_rent_for_stage(stage: int, member_type: str = 'wife') -> float:
    if member_type == 'sister':
        return NYC['rent']['1br']
    if stage <= 2:
        return NYC['rent']['1br']
    elif stage == 3:
        return NYC['rent']['2br']
    else:
        return NYC['rent']['3br']

def stage_requirements(stage: int, children_per_wife: dict[int, int], sister: bool = True) -> dict:
    """
    Stage 0: Single (Brian + optional sister)
    Stage 1: Brian + Wife 1 (separate places)
    Stage 2: Brian + Wife 1, first child born
    Stage 3: Add Wife 2
    Stage 4: Add Wife 3
    Stage 5: Add Wife 4
    """
    weekly = 0.0
    members = []
    breakdown = {}
    
    # Brian always present
    brian_rent = NYC['rent']['1br']  # Already budgeted place
    brian_needs = NYC['per_adult_weekly']
    weekly += brian_rent + brian_needs
    breakdown['brian'] = {'rent': brian_rent, 'needs': brian_needs, 'total': brian_rent + brian_needs}
    members.append('brian')
    
    # Sister (always covered by fund)
    if sister:
        s_rent = NYC['rent']['1br']
        s_needs = NYC['per_adult_weekly']
        weekly += s_rent + s_needs
        breakdown['sister'] = {'rent': s_rent, 'needs': s_needs, 'total': s_rent + s_needs}
        members.append('sister')
    
    # Wives
    total_children = 0
    stage_wives = min(stage, 4) if stage >= 1 else 0
    for w in range(1, stage_wives + 1):
        wid = w
        children = children_per_wife.get(wid, 0)
        total_children += children
        rent = default_rent_for_stage(stage, 'wife')
        needs = NYC['per_adult_weekly']
        child_cost = NYC['per_child_weekly'] * children
        total = rent + needs + child_cost
        weekly += total
        breakdown[f'wife_{w}'] = {
            'rent': rent,
            'needs': needs,
            'children': children,
            'child_cost_weekly': child_cost,
            'total_weekly': total,
        }
        members.append(f'wife_{w}')
    
    buffer = round(weekly * NYC['buffer_pct'], 2)
    total_with_buffer = round(weekly + buffer, 2)
    
    return {
        'stage': stage,
        'stage_name': stage_name(stage),
        'members': members,
        'breakdown': breakdown,
        'total_children': total_children,
        'total_weekly_needs': round(weekly, 2),
        'buffer_20pct': buffer,
        'total_required_weekly': total_with_buffer,
        'child_support_50pct_of_income': None,  # requires income
        'notes': 'Rent paid by tribe fund first. 20% buffer saved.'
    }

def stage_name(stage: int) -> str:
    names = {
        0: 'Single',
        1: 'Wife 1 only',
        2: 'Wife 1 + first child',
        3: 'Wife 1 + child + Wife 2',
        4: 'Wife 1 + child + Wife 2 + Wife 3',
        5: 'Wife 1-4 (max)',
    }
    return names.get(stage, f'Stage {stage}')

def required_weekly_income(stage: int, children_per_wife: dict[int, int], sister: bool = True) -> float:
    """
    Minimum weekly income to cover needs + buffer at given stage.
    This is the floor we must earn to stay solvent.
    """
    req = stage_requirements(stage, children_per_wife, sister)
    return req['total_required_weekly']

def child_support_schedule(weekly_income: float, children_per_wife: dict[int, int]) -> dict:
    pool = round(weekly_income * 0.50, 2)
    total_children = sum(children_per_wife.values())
    if total_children <= 0:
        return {'pool': 0, 'per_child': 0, 'per_wife': {wid: 0 for wid in children_per_wife}}
    per_child = round(pool / total_children, 2)
    per_wife = {wid: round(per_child * count, 2) for wid, count in children_per_wife.items() if count > 0}
    return {'pool': pool, 'per_child': per_child, 'per_wife': per_wife, 'total_children': total_children}

# Default scenario: current single stage, no children yet
def write_current_stage():
    out = BASE / 'calc/stage_schedule.json'
    stage = 0
    children_per_wife = {}
    req = stage_requirements(stage, children_per_wife, sister=True)
    out.write_text(json.dumps(req, indent=2))
    print(json.dumps(req, indent=2))

if __name__ == '__main__':
    write_current_stage()
