#!/usr/bin/env python3
from pathlib import Path
from datetime import date
import csv

root = Path(__file__).resolve().parent.parent.parent
today = date.today()
report = []
for biz in ['appointment-setting', 'lead-generation-broker', 'recruiting']:
    src = root / f'businesses/{biz}/data/next_outreach_batch.csv' if biz != 'recruiting' else root / f'businesses/{biz}/data/candidates_template.csv'
    dst = root / f'businesses/{biz}/data/daily_batch_{today.isoformat()}.csv'
    rows = []
    if src.exists():
        with src.open(newline='') as f:
            rows = [r for r in csv.DictReader(f) if any(v.strip() for v in r.values())]
    rows = rows[:5]
    with dst.open('w', newline='') as f:
        w = csv.DictWriter(f, rows[0].keys() if rows else [])
        w.writeheader()
        for r in rows:
            w.writerow(r)
    report.append(f'{biz}: {len(rows)} rows -> {dst}')
print('\n'.join(report))
