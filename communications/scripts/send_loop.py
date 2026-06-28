#!/usr/bin/env python3
import csv, time, json
from pathlib import Path
from datetime import datetime
from email.mime.text import MIMEText
import imaplib, smtplib, re

WORKDIR = Path('/root/ai-holding-company')
OUTBOX = WORKDIR / 'communications' / 'outbox'
LOGS = WORKDIR / 'communications' / 'logs'
STATE = WORKDIR / 'communications' / 'state.json'
LEAD_FILE = WORKDIR / 'first-business-missed-call-recovery' / 'data' / 'florida_hvac_first_call_batch_150.csv'
OUTBOX.mkdir(parents=True, exist_ok=True)
LOGS.mkdir(parents=True, exist_ok=True)

SMTP_HOST = '127.0.0.1'
SMTP_PORT = 25
FROM_ADDR = 'bharmon1215@gmail.com'
FROM_NAME = 'Brian Hamilton'

IMAP_HOST = '127.0.0.1'
IMAP_PORT = 143
IMAP_USER = 'revenue-rescue'
IMAP_PASS = 'RevenueRescue2026!'

WEEKDAYS = list(range(0, 5))
BUSINESS_START = 9
BUSINESS_END = 17

TEMPLATE = (
    "Hi {contact},\n\n"
    "I came across {company} in {city} and had a quick question about how you currently handle missed calls.\n\n"
    "I run a small client-response service for HVAC shops and was wondering if you ever lose jobs because someone didn't answer the phone.\n\n"
    "If that's ever a problem, I can show you a simple way to recover those missed bookings — no software to buy, no long-term commitment.\n\n"
    "Are you open to a 2-minute call this week?\n\n"
    "If now isn't a good time, just let me know and I'll follow up in a week.\n\n"
    "Thanks,\n{from_name}\n{from_addr}"
)


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding='utf-8'))
    return {'last_run': None, 'skipped_no_email': 0}


def save_state(state):
    STATE.write_text(json.dumps(state, indent=2), encoding='utf-8')


def log_csv(path, row):
    exists = path.exists()
    with path.open('a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(['timestamp', 'business', 'contact', 'company', 'to_addr', 'subject', 'status', 'error'])
        w.writerow(row)


def render(row):
    company = (row.get('company') or '').strip() or 'your shop'
    contact = (row.get('owner_or_manager') or '').strip() or 'there'
    city = (row.get('city') or '').strip() or 'Florida'
    return TEMPLATE.format(contact=contact, company=company, city=city, from_name=FROM_NAME, from_addr=FROM_ADDR)


def now_ok():
    n = datetime.now()
    return n.weekday() in WEEKDAYS and BUSINESS_START <= n.hour < BUSINESS_END


def send_one(to_addr, subject, body):
    msg = MIMEText(body)
    msg['From'] = f'{FROM_NAME} <{FROM_ADDR}>'
    msg['To'] = to_addr
    msg['Subject'] = subject
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.send_message(msg)


def check_inbound():
    try:
        m = imaplib.IMAP4(IMAP_HOST, IMAP_PORT)
        m.login(IMAP_USER, IMAP_PASS)
        m.select('INBOX', readonly=True)
        typ, data = m.search(None, 'UNSEEN')
        ids = data[0].split() if data[0] else []
        print('inbox_unseen=' + str(len(ids)))
        m.logout()
    except Exception as e:
        print('inbox_error=' + repr(e))


def process_batch():
    if not LEAD_FILE.exists():
        print('no_lead_file')
        return
    with open(LEAD_FILE, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    sent = 0
    skipped = 0
    state = load_state()
    for row in rows:
        status = (row.get('status') or 'New').strip()
        if status != 'New':
            continue
        email_addr = (row.get('email_client') or row.get('email') or '').strip()
        business_name = (row.get('company') or '').strip() or 'business'
        contact = (row.get('owner_or_manager') or '').strip() or 'there'
        if not email_addr:
            state['skipped_no_email'] = state.get('skipped_no_email', 0) + 1
            skipped += 1
            continue
        subject = f'Quick question about HVAC at {business_name}'
        body = render(row)
        try:
            send_one(email_addr, subject, body)
            ts = datetime.now().isoformat()
            log_csv(LOGS / 'sent_emails.csv', [ts, 'appointment-setting', contact, business_name, email_addr, subject, 'sent', ''])
            out = OUTBOX / f'{datetime.now().strftime("%Y%m%d%H%M%S")}.txt'
            out.write_text(body, encoding='utf-8')
            row['status'] = 'sent'
            sent += 1
            time.sleep(1)
        except Exception as e:
            ts = datetime.now().isoformat()
            log_csv(LOGS / 'sent_emails.csv', [ts, 'appointment-setting', contact, business_name, email_addr, subject, 'failed', str(e)])
    with open(LEAD_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    state['last_run'] = datetime.now().isoformat()
    save_state(state)
    print('processed_now=' + str(sent) + ' skipped_no_email=' + str(skipped) + ' hour_' + str(datetime.now().hour))


def main_loop():
    print('started=2026-06-25 sender=bharmon1215@gmail.com')
    while True:
        if now_ok():
            check_inbound()
            process_batch()
        time.sleep(60)


if __name__ == '__main__':
    main_loop()
