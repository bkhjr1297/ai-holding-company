#!/usr/bin/env python3
import csv, argparse, sys
from pathlib import Path
from datetime import datetime

DEFAULT_LEADS='/root/ai-holding-company/first-business-missed-call-recovery/data/florida_hvac_first_call_batch_150.csv'
CALL_LOG='/root/ai-holding-company/communications/logs/call_log.csv'

OPENING = """Hi, is this {company}?

This is Brian with Revenue Rescue Desk. We help Florida HVAC companies during summer call spikes by following up with missed calls and quote requests so more AC jobs actually get booked.

Quick question — when calls go to voicemail or web requests come in after hours, do you have a reliable follow-up process, or does it depend on who has time that day?"""

VOICEMAIL = """Hi {contact}, this is Brian with Revenue Rescue Desk. We help Florida HVAC companies recover missed calls and quote requests during summer call spikes. I had one quick idea for {company}'s follow-up process. I will send a short note as well. Again, Brian with Revenue Rescue Desk."""

OBJECTIONS = {
 '1': ('We already answer our phones', 'That is good. Most companies do during normal hours. The gap we usually look for is overflow, after-hours requests, or quote forms that do not get followed up quickly. Do you have that covered too?'),
 '2': ('Send me something', 'Absolutely. What is the best email? And just so I send the right thing — is missed calls, after-hours requests, or web quote follow-up the bigger issue for you?'),
 '3': ('How much?', 'It depends on volume, but the pilot is usually designed so one recovered job can justify it. The simple next step is a quick missed-revenue audit first, then we can see if it is even worth discussing price.'),
 '4': ('Not interested', 'No problem at all. I appreciate your time. If missed calls or after-hours follow-up ever become a priority during the summer rush, we are happy to help. Have a good one.'),
 '5': ('Are you AI?', 'We use automation and AI-assisted workflows behind the scenes, but the service is simple: faster follow-up, better tracking, and more booked jobs. You do not need to change your phone system to test it.'),
 '6': ('Book audit', 'That makes sense. The easiest next step is a quick 15-minute missed-revenue audit. We look at where calls or quote requests may be leaking and whether a response desk would pay for itself. Would today or tomorrow be better?'),
 '7': ('Freeze escape line', 'No worries — I do not want to take up your time. I can send a short summary by email and you can decide if it is relevant. What is the best email for you?'),
}

DISPOSITIONS = ['No Answer','Left Voicemail','Gatekeeper','Asked for Email','Interested — Follow Up','Discovery Booked','Not Interested','Bad Number','Do Not Contact']

def append_log(row):
    path=Path(CALL_LOG); path.parent.mkdir(parents=True, exist_ok=True)
    exists=path.exists()
    fields=['timestamp','company','phone','contact','disposition','notes','next_action']
    with path.open('a', newline='') as f:
        w=csv.DictWriter(f, fields)
        if not exists: w.writeheader()
        w.writerow(row)

def main():
    ap=argparse.ArgumentParser(description='Beginner guided cold-call console')
    ap.add_argument('--leads', default=DEFAULT_LEADS)
    ap.add_argument('--start', type=int, default=1, help='1-based lead number')
    ap.add_argument('--count', type=int, default=5)
    args=ap.parse_args()
    rows=list(csv.DictReader(open(args.leads, newline='')))
    subset=rows[args.start-1: args.start-1+args.count]
    if not subset:
        print('No leads in selected range.'); return
    print('\nBEGINNER RULE: Your only job is to read, listen, pick a disposition, and log.\n')
    for idx,r in enumerate(subset, args.start):
        company=r.get('company','').strip()
        phone=r.get('phone_normalized') or r.get('phone') or ''
        contact=r.get('owner_or_manager','').strip() or 'there'
        print('='*80)
        print(f'LEAD #{idx}: {company}')
        print(f'PHONE: {phone}')
        print(f'CONTACT/OWNER: {contact}')
        print(f'CITY/REGION: {r.get("city","")} / {r.get("region","")}')
        print('\nREAD THIS OPENER:\n')
        print(OPENING.format(company=company))
        print('\nIF VOICEMAIL:\n')
        print(VOICEMAIL.format(contact=contact, company=company))
        while True:
            print('\nOBJECTION HELP:')
            for k,(label,_) in OBJECTIONS.items(): print(f'  {k}. {label}')
            print('  d. disposition/log call')
            print('  q. quit')
            choice=input('Choose help, d to log: ').strip().lower()
            if choice in OBJECTIONS:
                print('\nSAY THIS:\n'+OBJECTIONS[choice][1])
            elif choice=='d':
                break
            elif choice=='q':
                return
        print('\nDisposition:')
        for i,d in enumerate(DISPOSITIONS,1): print(f'  {i}. {d}')
        disp_i=input('Pick disposition number: ').strip()
        try: disp=DISPOSITIONS[int(disp_i)-1]
        except Exception: disp=disp_i or 'Unknown'
        notes=input('Notes: ').strip()
        next_action=input('Next action: ').strip()
        append_log({'timestamp':datetime.now().isoformat(timespec='seconds'), 'company':company, 'phone':phone, 'contact':contact, 'disposition':disp, 'notes':notes, 'next_action':next_action})
        print(f'Logged: {company} | {disp}')
    print('\nDone. Call log:', CALL_LOG)

if __name__=='__main__': main()
