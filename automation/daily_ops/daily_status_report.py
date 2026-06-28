#!/usr/bin/env python3
from pathlib import Path
from datetime import date
import csv

root = Path(__file__).resolve().parent.parent.parent
today = date.today()
lines = [f'RRD Daily Ops Status — {today.isoformat()}']
for biz in ['appointment-setting', 'lead-generation-broker', 'recruiting']:
    dst = root / f'businesses/{biz}/data/daily_batch_{today.isoformat()}.csv'
    rev = root / f'businesses/{biz}/data/revenue.csv'
    lines.append(f'[{biz}]')
    if dst.exists():
        with dst.open() as f:
            lines.append(f'  daily batch: {sum(1 for _ in f) - 1} leads')
    else:
        lines.append('  daily batch: not generated')
    if rev.exists():
        month_total = 0.0
        with rev.open() as f:
            for r in csv.DictReader(f):
                if r.get('date','').startswith(today.strftime('%Y-%m')):
                    try: month_total += float(r.get('amount',0) or 0)
                    except: pass
        lines.append(f'  month revenue: ${month_total:.2f}')
    lines.append('')
print('\n'.join(lines))
