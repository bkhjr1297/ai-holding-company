#!/usr/bin/env python3
import csv, argparse
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--n', type=int, default=25)
p.add_argument('--source', default='/root/ai-holding-company/first-business-missed-call-recovery/data/florida_hvac_first_call_batch_150.csv')
args=p.parse_args()
with open(args.source, newline='') as f:
    rows=list(csv.DictReader(f))
for i,r in enumerate(rows[:args.n],1):
    print(f"{i}. {r.get('company','')} | {r.get('phone_normalized','')} | {r.get('city','')} | {r.get('owner_or_manager','')} | {r.get('region','')}")
