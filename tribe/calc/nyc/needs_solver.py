#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import json

BASE = Path('/root/ai-holding-company/tribe')
NYC = {
  'rent_per_week': {
    'studio': 600,
    '1br': 750,
    '2br': 950,
    '3br': 1200,
    '4br': 1400,
  },
  'per_person_weekly': {
    'utilities': 55,
    'food': 80,
    'transport': 35,
    'phone_internet': 30,
    'health_baseline': 20,
    'clothing_personal': 25,
  },
  'per_child_weekly': {
    'food': 40,
    'transport_extra': 15,
    'activities': 20,
    'clothing': 15,
    'health': 10,
  }
}

def calculate_tribe_needs(wives: dict, sister: dict | None = None, brian_rent: float = 750.0) -> dict:
    """
    Calculate total weekly tribe needs based on NYC costs.
    Every adult needs: rent + utilities + food + transport + phone + health + personal.
    Every child needs: food + transport_extra + activities + clothing + health.
    Sister is treated as an additional adult whose needs must be covered.
    """
    per_adult = sum(NYC['per_person_weekly'].values())
    per_child = sum(NYC['per_child_weekly'].values())
    
    total_weekly = 0.0
    breakdown = {
        'brian': {'rent': brian_rent, 'per_person': per_adult, 'total': brian_rent + per_adult},
        'wives': {},
        'sister': None,
        'children': {}
    }
    
    total_weekly += brian_rent + per_adult
    
    for wid, w in wives.items():
        rent = float(w.get('rent', NYC['rent_per_week']['1br']))
        children = int(w.get('children', 0) or 0)
        child_cost = per_child * children
        total = rent + per_adult + child_cost
        breakdown['wives'][wid] = {
            'name': w.get('name', wid),
            'rent': rent,
            'per_person_costs': per_adult,
            'children': children,
            'per_child_weekly': per_child,
            'child_cost_weekly': child_cost,
            'total_weekly': total
        }
        total_weekly += total
    
    if sister:
        s_rent = float(sister.get('rent', NYC['rent_per_week']['1br']))
        s_total = s_rent + per_adult
        breakdown['sister'] = {
            'name': sister.get('name', 'Sister'),
            'rent': s_rent,
            'per_person_costs': per_adult,
            'total_weekly': s_total
        }
        total_weekly += s_total
    
    # Tribe buffer = 20% of total needs for emergencies/savings
    buffer = round(total_weekly * 0.20, 2)
    
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'location': 'NYC',
        'per_adult_weekly_base': per_adult,
        'per_child_weekly_base': per_child,
        'tribemembers': breakdown,
        'total_weekly_needs': round(total_weekly, 2),
        'recommended_buffer_20pct': buffer,
        'total_with_buffer': round(total_weekly + buffer, 2),
        'child_support_pool_50pct_of_income': None,  # filled by caller if income known
        'surplus_deficit_notes': 'Add income to determine surplus/deficit'
    }

def generate_budget_template() -> dict:
    return {
        'brian': {'name':'Brian Harmon','rent':750,'role':'lead'},
        'wives': {
            '1': {'name':'Wife 1','rent':750,'children':1},
            '2': {'name':'Wife 2','rent':750,'children':2},
        },
        'sister': {'name':'Sister','rent':750},
        'notes': 'Adjust rent values to match actual apartment sizes/locations'
    }

if __name__ == '__main__':
    out = BASE / 'calc/nyc/needs_schedule.json'
    template = generate_budget_template()
    result = calculate_tribe_needs(
        wives=template['wives'],
        sister=template['sister'],
        brian_rent=template['brian']['rent']
    )
    out.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
