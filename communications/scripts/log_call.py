#!/usr/bin/env python3
import csv, sys, argparse
from pathlib import Path
from datetime import datetime

p=argparse.ArgumentParser()
p.add_argument('--company', required=True)
p.add_argument('--phone', required=True)
p.add_argument('--contact', default='')
p.add_argument('--disposition', required=True)
p.add_argument('--notes', default='')
p.add_argument('--next-action', default='')
p.add_argument('--file', default='/root/ai-holding-company/communications/logs/call_log.csv')
args=p.parse_args()
path=Path(args.file); path.parent.mkdir(parents=True, exist_ok=True)
exists=path.exists()
fields=['timestamp','company','phone','contact','disposition','notes','next_action']
with path.open('a', newline='') as f:
    w=csv.DictWriter(f, fields)
    if not exists: w.writeheader()
    w.writerow({'timestamp':datetime.now().isoformat(timespec='seconds'), 'company':args.company, 'phone':args.phone, 'contact':args.contact, 'disposition':args.disposition, 'notes':args.notes, 'next_action':args.next_action})
print(f'logged call: {args.company} | {args.disposition}')
