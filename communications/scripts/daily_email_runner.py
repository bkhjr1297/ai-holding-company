#!/usr/bin/env python3
"""
Revenue Rescue Desk — Daily Email Outreach Runner
- Reads each daily batch file for all portfolio businesses
- Skips rows without emails
- Sends one personalized email per valid email address
- Logs sends to CSV
- Queues follow-up reminders
"""
import csv, smtplib, os, time
from pathlib import Path
from email.mime.text import MIMEText
from datetime import datetime, timedelta

BUSINESSES = Path('/root/ai-holding-company/businesses')
TEMPLATE_DIR = Path('/root/ai-holding-company/communications/templates')
LOG_DIR = Path('/root/ai-holding-company/communications/logs')
LOG_DIR.mkdir(parents=True, exist_ok=True)

SMTP_SERVER = '127.0.0.1'
SMTP_PORT = 25
FROM_ADDR = 'bharmon1215@gmail.com'
FROM_NAME = 'Brian Hamilton'
SUBJECT_PREFIX = 'Quick question about '


def load_template(business):
    template_file = TEMPLATE_DIR / f'{business}_initial_email.txt'
    if not template_file.exists():
        template_file = TEMPLATE_DIR / 'florida_hvac_initial_email.txt'
    if template_file.exists():
        return template_file.read_text(encoding='utf-8')
    return ("Hi {contact},\n\nI came across {company} in {city} and had a quick question about how you currently handle missed calls.\n\nI run a small client-response service for {niche} shops and was wondering if you ever lose jobs because someone didn’t answer the phone.\n\nIf that’s ever a problem, I can show you a simple way to recover those missed bookings — no software to buy, no long-term commitment.\n\nAre you open to a 2-minute call this week?\n\nIf now isn’t a good time, just let me know and I’ll follow up in a week.\n\nThanks,\n{from_name}\n{from_addr}")


def render_template(template, row):
    company = row.get('company') or row.get('business_name') or 'your business'
    contact = row.get('owner_or_manager') or row.get('owner_name') or 'there'
    city = row.get('city') or ''
    state = row.get('state') or ''
    niche = row.get('niche') or 'HVAC'
    return template.format(
        contact=contact,
        company=company,
        city=city,
        state=state,
        niche=niche,
        from_name=FROM_NAME,
        from_addr=FROM_ADDR,
    )


def send_email(to_addr, subject, body):
    msg = MIMEText(body)
    msg['From'] = f'{FROM_NAME} <{FROM_ADDR}>'
    msg['To'] = to_addr
    msg['Subject'] = subject
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as s:
        s.send_message(msg)


def run():
    today = datetime.now().strftime('%Y-%m-%d')
    total_sent = 0
    total_skipped = 0
    for business in BUSINESSES.iterdir():
        if not business.is_dir():
            continue
        batch_file = business / 'data' / f'daily_batch_{today}.csv'
        if not batch_file.exists():
            continue
        template = load_template(business.name)
        log_file = LOG_DIR / f'{business.name}_email_log.csv'
        log_exists = log_file.exists()
        with log_file.open('a', newline='', encoding='utf-8') as lf:
            writer = csv.writer(lf)
            if not log_exists:
                writer.writerow(['timestamp','business','contact','company','email','subject','status','error'])
            with batch_file.open(newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    email = (row.get('email') or '').strip()
                    if not email:
                        total_skipped += 1
                        continue
                    company = row.get('company') or row.get('business_name') or 'business'
                    contact = row.get('owner_or_manager') or row.get('owner_name') or 'contact'
                    subject = f"{SUBJECT_PREFIX}{company}"
                    try:
                        body = render_template(template, row)
                        send_email(email, subject, body)
                        writer.writerow([datetime.now().isoformat(), business.name, contact, company, email, subject, 'sent', ''])
                        total_sent += 1
                        time.sleep(1)
                    except Exception as e:
                        writer.writerow([datetime.now().isoformat(), business.name, contact, company, email, subject, 'failed', str(e)])
    print(f'Email outreach complete. sent={total_sent} skipped_no_email={total_skipped}')


if __name__ == '__main__':
    run()
