#!/usr/bin/env python3
from pathlib import Path

prospects = Path(__file__).resolve().parent.parent / 'data' / 'appointment_setting_prospects_template.csv'
text = prospects.read_text(errors='ignore')
print('Dry-run email sequence engine')
print('Loaded prospects file:', prospects)
print('Lines:', len(text.splitlines()))
