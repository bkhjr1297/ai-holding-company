#!/usr/bin/env python3
import csv
from pathlib import Path

src = Path(__file__).resolve().parent.parent / 'data' / 'appointment_setting_prospects_template.csv'
dst = Path(__file__).resolve().parent.parent / 'data' / 'next_outreach_batch.csv'
rows = []
if src.exists():
    with src.open(newline='') as f:
        rows = [r for r in csv.DictReader(f) if any(v.strip() for v in r.values())]
with dst.open('w', newline='') as f:
    w = csv.DictWriter(f, rows[0].keys() if rows else [])
    w.writeheader()
    for r in rows[:25]:
        w.writerow(r)
print('Wrote', max(0, len(rows[:25])), 'rows to', dst)
