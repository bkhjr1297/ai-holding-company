#!/usr/bin/env python3
from __future__ import annotations
import csv, re, subprocess
from pathlib import Path

BIZ=Path('/root/ai-holding-company/businesses/ai-search-readiness-retrofit')
PROSPECTS=BIZ/'data/prospects.csv'
if not PROSPECTS.exists(): PROSPECTS=BIZ/'data/prospects_seed.csv'
QUEUE=BIZ/'outreach/approval_queue.csv'
CRM=BIZ/'crm/pipeline.csv'
GEN=BIZ/'scripts/generate_snapshot.py'

def safe_slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-') or 'prospect'

def first_line(company, category):
    return f'I reviewed {company}\'s public website for {category} service clarity, local proof, FAQ readiness, and quote-path friction.'

def body(company, category, report):
    return f"""Hi,

I prepared a short public-website snapshot for {company}. It looks at whether AI-assisted buyers can quickly understand your {category} services, service area, proof, FAQs, and quote/contact path.

No login was used and no forms were submitted. If useful, Brian can manually send the snapshot and the top fixes.

Report file: {report}

— Revenue Rescue Desk
""".strip()

def score_report(path):
    txt=Path(path).read_text() if Path(path).exists() else ''
    m=re.search(r'scored (\d+)/25', txt)
    return int(m.group(1)) if m else ''

def main():
    rows=[]; crm=[]
    with PROSPECTS.open() as f:
        for r in csv.DictReader(f):
            if not r.get('website'): continue
            company=r['company']; website=r['website']; category=r.get('category','Local service')
            report=BIZ/'reports/samples'/f'{safe_slug(company)}-snapshot.md'
            subprocess.run(['python3', str(GEN), '--business-name', company, '--website', website, '--category', category, '--output', str(report)], check=False, capture_output=True)
            sc=score_report(report)
            rows.append({'company':company,'website':website,'category':category,'score':sc,'subject':f'quick AI-search snapshot for {company}','first_line':first_line(company, category),'body':body(company, category, report),'report_path':str(report),'status':'needs_human_approval'})
            crm.append({'company':company,'website':website,'category':category,'stage':'snapshot_ready','score':sc,'report_path':str(report),'next_action':'Human review; do not send automatically','last_touch':'','notes':r.get('source','')})
    with QUEUE.open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=['company','website','category','score','subject','first_line','body','report_path','status'])
        w.writeheader(); w.writerows(rows)
    with CRM.open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=['company','website','category','stage','score','report_path','next_action','last_touch','notes'])
        w.writeheader(); w.writerows(crm)
    print('queue', QUEUE, len(rows))
    print('crm', CRM, len(crm))

if __name__=='__main__': main()
