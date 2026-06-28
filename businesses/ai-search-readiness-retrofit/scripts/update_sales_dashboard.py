#!/usr/bin/env python3
from pathlib import Path
import csv, json
from collections import Counter

BASE=Path('/root/ai-holding-company/businesses/ai-search-readiness-retrofit')
crm=BASE/'crm/pipeline.csv'
queue=BASE/'outreach/approval_queue.csv'
report=BASE/'reports/sales_dashboard.md'
rows=list(csv.DictReader(crm.open())) if crm.exists() else []
qrows=list(csv.DictReader(queue.open())) if queue.exists() else []
stage=Counter(r.get('stage','unknown') for r in rows)
cat=Counter(r.get('category','unknown') for r in rows)
scores=[int(r['score']) for r in rows if str(r.get('score','')).isdigit()]
avg=round(sum(scores)/len(scores),1) if scores else 0
body=['# AI Search Retrofit Sales Dashboard','',f'Prospects in CRM: **{len(rows)}**',f'Outreach drafts awaiting human approval: **{len(qrows)}**',f'Average snapshot score: **{avg}/25**','', '## By stage']
for k,v in stage.items(): body.append(f'- {k}: {v}')
body += ['', '## By category']
for k,v in cat.items(): body.append(f'- {k}: {v}')
body += ['', '## Top prospects ready for review']
for r in sorted(rows, key=lambda x:int(x.get('score') or 0), reverse=True)[:10]:
    body.append(f"- {r['company']} ({r['category']}) — score {r['score']}/25 — {r['website']}")
body += ['', '## Safety', '- These are drafts only.', '- No email sent.', '- No calls placed.', '- Human approval required before any outreach.']
report.write_text('\n'.join(body)+'\n')
print(report)
