#!/usr/bin/env python3
from pathlib import Path
from datetime import date
import csv

root = Path(__file__).resolve().parent.parent.parent
today = date.today()
rows = []
for biz in ['appointment-setting', 'lead-generation-broker', 'recruiting']:
    rev_file = root / f'businesses/{biz}/data/revenue.csv'
    if rev_file.exists():
        with rev_file.open() as f:
            for r in csv.DictReader(f):
                if r.get('date','') == today.isoformat():
                    rows.append((biz, r.get('source',''), r.get('amount','0'), r.get('type',''), r.get('notes','')))
out = root / f'communications/reports/daily_revenue_{today.isoformat()}.txt'
out.parent.mkdir(parents=True, exist_ok=True)
with out.open('w') as f:
    if not rows:
        f.write(f'Daily revenue report for {today.isoformat()}:\nNo revenue yet. Keep pushing outreach.\n')
    else:
        f.write(f'Daily revenue report for {today.isoformat()}:\n')
        for biz,source,amount,typ,notes in rows:
            f.write(f'- {biz}: ${amount} from {source} ({typ}) | {notes}\n')
print('Wrote', out)
