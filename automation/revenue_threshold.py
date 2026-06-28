#!/usr/bin/env python3
from pathlib import Path
from datetime import date
import csv, os

root = Path(__file__).resolve().parent.parent
biz = os.environ.get('RRD_BUSINESS', 'appointment-setting')
rev_file = root / f"businesses/{biz}/data/revenue.csv"

def current_month():
    return date.today().strftime('%Y-%m')

rows = []
if rev_file.exists():
    with rev_file.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('date','').startswith(current_month()):
                rows.append(row)

total = round(sum(float(r.get('amount',0) or 0) for r in rows), 2)
months = int(os.environ.get('RRD_CONSECUTIVE_MONTHS', '3'))
threshold = 1000.0 * months

print(f"Business={biz}")
print(f"Month total={total}")
print(f"Threshold={threshold}")
