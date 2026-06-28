#!/usr/bin/env python3
from __future__ import annotations
import csv, subprocess, textwrap, time, re, uuid
from pathlib import Path
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

BASE = Path('/root/ai-holding-company/businesses/ai-search-readiness-retrofit')
CONTACTS = BASE / 'outreach/contact_research.csv'
LOG = BASE / 'outreach/sent_log.csv'
BATCH = BASE / 'outreach/first_customer_batch.eml.txt'
FROM = 'Brian Harmon <bharmon1215@gmail.com>'
BAD_EMAILS = {'yourname@gmail.com'}


def load_report(company: str) -> tuple[str, list[str]]:
    slug = re.sub(r'[^a-z0-9]+', '-', company.lower()).strip('-')
    p = BASE / 'reports/samples' / f'{slug}-snapshot.md'
    if not p.exists():
        return '', []
    txt = p.read_text()
    m = re.search(r'scored (\d+/25)', txt)
    score = m.group(1) if m else ''
    fixes = []
    in_fixes = False
    for line in txt.splitlines():
        if line.startswith('## Top 5 Fixes'):
            in_fixes = True
            continue
        if in_fixes:
            if line.startswith('## '): break
            if re.match(r'\d+\. ', line.strip()): fixes.append(line.strip())
    return score, fixes[:3]


def body_for(row):
    company=row['company']; category=row['category']; website=row['website']
    score, fixes = load_report(company)
    cleaned_fixes = [re.sub(r'^\\d+\\. ', '', f) for f in fixes]
    fix_text = '\n'.join(f'- {f}' for f in cleaned_fixes) or '- Add clearer service/FAQ/proof sections for AI-assisted buyers.'
    return f'''Hi — I’m Brian with Revenue Rescue Desk.

I reviewed {company}'s public website ({website}) for {category.lower()} service clarity, local proof, FAQ readiness, and quote/contact flow.

The quick public-page scan came back at {score or 'a partial score'} for AI-search / agent-readiness. The biggest opportunities I saw were:

{fix_text}

No login was used and I did not submit any forms. I can send the 1-page snapshot and practical fix list if useful.

If improving how search engines and AI-assisted buyers understand your services is a priority, reply “send it” and I’ll send the snapshot.

If this is not relevant, reply “no” and I won’t follow up.

Brian Harmon
Revenue Rescue Desk
bharmon1215@gmail.com
'''


def send(row):
    to=row['primary_email'].strip()
    msg=EmailMessage()
    msg['From']=FROM
    msg['To']=to
    msg['Subject']=f"quick website clarity snapshot for {row['company']}"
    msg['Date']=formatdate(localtime=True)
    msg['Message-ID']=make_msgid(domain='gmail.com')
    msg.set_content(body_for(row))
    proc=subprocess.run(['/usr/sbin/sendmail','-t','-oi'], input=msg.as_bytes(), capture_output=True)
    return proc.returncode, proc.stderr.decode(errors='ignore'), msg.as_string()


def main():
    rows=[]
    with CONTACTS.open() as f:
        for r in csv.DictReader(f):
            email=r.get('primary_email','').strip().lower()
            if not email or email in BAD_EMAILS: continue
            if r.get('category') == 'HVAC': continue
            rows.append(r)
    sent=[]; all_msgs=[]
    for r in rows[:6]:
        code, err, raw = send(r)
        sent.append({'timestamp':formatdate(localtime=True),'company':r['company'],'email':r['primary_email'],'category':r['category'],'status':'sent_to_mta' if code==0 else 'sendmail_error','exit_code':code,'error':err[:200]})
        all_msgs.append('\n'+'='*80+'\n'+raw)
        time.sleep(1)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    exists=LOG.exists()
    with LOG.open('a', newline='') as f:
        w=csv.DictWriter(f, fieldnames=['timestamp','company','email','category','status','exit_code','error'])
        if not exists: w.writeheader()
        w.writerows(sent)
    BATCH.write_text('\n'.join(all_msgs))
    print('attempted',len(sent))
    for s in sent: print(s['status'], s['company'], s['email'], s['exit_code'], s['error'])

if __name__ == '__main__': main()
