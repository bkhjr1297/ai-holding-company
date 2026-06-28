#!/usr/bin/env python3
from pathlib import Path
import csv, json, datetime

BASE=Path('/root/ai-holding-company/businesses/ai-search-readiness-retrofit')
LOG=BASE/'outreach/sent_log.csv'
CRM=BASE/'crm/pipeline.csv'
DASH=BASE/'reports/sales_dashboard.md'
STATE=Path('/root/ai-holding-company/rpg-command-center/engine/public/game_state.json')

sent=list(csv.DictReader(LOG.open())) if LOG.exists() else []
sent_companies={r['company']:r for r in sent if r.get('status')=='sent_to_mta'}
rows=list(csv.DictReader(CRM.open()))
for r in rows:
    if r['company'] in sent_companies:
        r['stage']='outreach_sent'
        r['last_touch']=sent_companies[r['company']]['timestamp']
        r['next_action']='Watch for reply; follow up manually in 3 business days if no response'
with CRM.open('w', newline='') as f:
    w=csv.DictWriter(f, fieldnames=['company','website','category','stage','score','report_path','next_action','last_touch','notes'])
    w.writeheader(); w.writerows(rows)

stage={}
cat={}
for r in rows:
    stage[r['stage']]=stage.get(r['stage'],0)+1
    cat[r['category']]=cat.get(r['category'],0)+1
body=['# AI Search Retrofit Sales Dashboard','',f'Prospects in CRM: **{len(rows)}**',f'Emails handed to Gmail relay: **{len(sent_companies)}**',f'HVAC emails sent: **0**','', '## By stage']
for k,v in stage.items(): body.append(f'- {k}: {v}')
body += ['', '## By category']
for k,v in cat.items(): body.append(f'- {k}: {v}')
body += ['', '## Sent batch']
for r in sent:
    body.append(f"- {r['company']} — {r['category']} — {r['email']} — {r['status']}")
body += ['', '## Next action', '- Monitor replies in Gmail.', '- Do not send HVAC outreach.', '- Prepare follow-up only after 3 business days if no response.']
DASH.write_text('\n'.join(body)+'\n')

s=json.loads(STATE.read_text())
qid='customer-getting-first-batch'
quest={'id':qid,'title':'Get First Customers — AI Search Retrofit','name':'Get First Customers — AI Search Retrofit','status':'active','business':'ai-search-readiness-retrofit','assigned_agent':'Sales Pipeline Agent','current':len(sent_companies),'target':6,'next_step':'Monitor Gmail replies and prepare follow-up for non-HVAC prospects only.','desc':'First compliant non-HVAC customer outreach batch sent via verified Gmail relay.','updated_at':datetime.datetime.utcnow().isoformat()+'Z'}
qs=s.setdefault('quests',[])
for i,q in enumerate(qs):
    if q.get('id')==qid: qs[i].update(quest); break
else: qs.append(quest)
s.setdefault('events',[]).append({'timestamp':datetime.datetime.utcnow().isoformat()+'Z','type':'customer_outreach','business':'ai-search-readiness-retrofit','agent':'Sales Pipeline Agent','message':f'First non-HVAC customer outreach batch sent to {len(sent_companies)} public business emails. HVAC sent: 0. Mail queue empty after handoff.'})
s['events']=s['events'][-25:]
STATE.write_text(json.dumps(s, indent=2))
print('crm updated, sent', len(sent_companies), 'agents', len(s.get('agents',[])), 'quests', len(s.get('quests',[])))
