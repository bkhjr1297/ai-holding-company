#!/usr/bin/env python3
import csv, smtplib, time, json
from pathlib import Path
from datetime import datetime, timedelta
from email.mime.text import MIMEText
import imaplib

BUSINESSES = Path('/root/ai-holding-company/businesses')
LOG_DIR = Path('/root/ai-holding-company/communications/logs')
OUT_DIR = Path('/root/ai-holding-company/communications/outbox')
OUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

SMTP_HOST = '127.0.0.1'
SMTP_PORT = 25
FROM_ADDR = 'bharmon1215@gmail.com'
FROM_NAME = 'Brian Hamilton'
IMAP_HOST = '127.0.0.1'
IMAP_PORT = 143
IMAP_USER = 'revenue-rescue'
IMAP_PASS = 'RevenueRescue2026!'

WEEKDAY_START = 9
WEEKDAY_END = 17


def business_hours_window():
    now = datetime.now()
    if now.weekday() >= 5:
        return None
    start = now.replace(hour=WEEKDAY_START, minute=0, second=0, microsecond=0)
    end = now.replace(hour=WEEKDAY_END, minute=0, second=0, microsecond=0)
    if now < start or now > end:
        return None
    remaining = (end - now).total_seconds()
    return max(remaining, 0)


def render_template(template, row):
    company = row.get('company') or row.get('business_name') or 'your business'
    contact = row.get('owner_or_manager') or row.get('owner_name') or 'there'
    city = row.get('city') or ''
    state = row.get('state') or ''
    niche = row.get('niche') or 'HVAC'
    subject_tpl = 'Quick question about {company}'
    body_tpl = (
        'Hi {contact},\n\n'
        'I came across {company} in {city}, {state} and had a quick question about how you currently handle missed calls.\n\n'
        'I run a small client-response service for {niche} shops and was wondering if you ever lose jobs because someone didn\'t answer the phone.\n\n'
        'If that\'s ever a problem, I can show you a simple way to recover those missed bookings — no software to buy, no long-term commitment.\n\n'
        'Are you open to a 2-minute call this week?\n\n'
        'If now isn\'t a good time, just let me know and I\'ll follow up in a week.\n\n'
        'Thanks,\n{from_name}\n{from_addr}'
    )
    subject = subject_tpl.format(company=company)
    body = body_tpl.format(contact=contact, company=company, city=city, state=state, niche=niche, from_name=FROM_NAME, from_addr=FROM_ADDR)
    return subject, body, contact, company


def log_row(path, row):
    exists = path.exists()
    with path.open('a', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(['timestamp','business','contact','company','email','subject','status','error'])
        w.writerow(row)


def send_business(business):
    today = datetime.now().strftime('%Y-%m-%d')
    batch = business / 'data' / f'daily_batch_{today}.csv'
    if not batch.exists():
        return 0, 0
    template_path = Path('/root/ai-holding-company/communications/templates') / f'{business.name}_initial_email.txt'
    template = template_path.read_text(encoding='utf-8') if template_path.exists() else None
    sent = 0
    skipped = 0
    with batch.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = (row.get('email') or '').strip()
            if not email:
                skipped += 1
                continue
            try:
                if template:
                    subject = template.format(**{k: row.get(k,'') for k in ['company','contact','city','state','niche']})
                else:
                    subject, body, contact, company = render_template('', row)
            except Exception:
                subject, body, contact, company = render_template('', row)
            msg = MIMEText(body)
            msg['From'] = f'{FROM_NAME} <{FROM_ADDR}>'
            msg['To'] = email
            msg['Subject'] = subject
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
                s.send_message(msg)
            log_row(LOG_DIR / 'email_log.csv', [datetime.now().isoformat(), business.name, contact, company, email, subject, 'sent', ''])
            out = OUT_DIR / f'{datetime.now().strftime("%Y%m%d%H%M%S")}_{business.name}.json'
            out.write_text(json.dumps({'to': email, 'subject': subject, 'body': body, 'business': business.name}, ensure_ascii=False), encoding='utf-8')
            sent += 1
            time.sleep(1)
    return sent, skipped
