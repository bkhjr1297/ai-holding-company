#!/usr/bin/env python3
from __future__ import annotations
import os, json, smtplib, textwrap
from email.message import EmailMessage
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path('/root/ai-holding-company/payout-ledger.jsonl')
RECEIPTS_DIR = Path('/root/ai-holding-company/receipts')

DEFAULT_TO = 'bharmon1215@gmail.com'
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'bharmon1215@gmail.com'
SMTP_PASS = 'dygwbuvziyepwaka'

def send_receipt(to_addr: str, subject: str, body_text: str, body_html: str | None = None):
    msg = EmailMessage()
    msg['From'] = SMTP_USER
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.set_content(body_text)
    if body_html:
        msg.add_alternative(body_html, subtype='html')

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.ehlo()
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)

def record_event(event_type: str, data: dict):
    entry = {'timestamp': datetime.now(timezone.utc).isoformat(), 'event': event_type, **data}
    with LEDGER.open('a') as f:
        f.write(json.dumps(entry) + '\n')

def build_receipt_markdown(entry: dict) -> str:
    return textwrap.dedent(f"""
    PAYMENT RECEIPT
    ===============

    Timestamp : {entry.get('timestamp', 'N/A')}
    Event     : {entry.get('event', 'N/A')}
    Recipient : {entry.get('recipient', 'N/A')}
    Amount USD: {entry.get('amount_usd', 'N/A')}
    Amount ETH: {entry.get('amount_eth', 'N/A')}
    Tx Hash   : {entry.get('tx_hash', entry.get('hash', 'N/A'))}
    Note      : {entry.get('note', '')}
    """).strip() + "\n"

def save_receipt(entry: dict) -> Path:
    folder = RECEIPTS_DIR / 'brian'
    folder.mkdir(parents=True, exist_ok=True)
    fname = f"receipt_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.md"
    p = folder / fname
    p.write_text(build_receipt_markdown(entry))
    return p

def send_test(to_addr: str = DEFAULT_TO):
    entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'event': 'system_ready',
        'recipient': to_addr,
        'amount_usd': '0.00',
        'amount_eth': '0.000000',
        'note': 'Test receipt confirming email delivery',
    }
    subject = f"[Receipt] Test delivery - {datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
    body_text = build_receipt_markdown(entry)
    send_receipt(to_addr, subject, body_text)
    save_receipt(entry)
    record_event('receipt_sent', {'to': to_addr, 'subject': subject, 'file': str(save_receipt(entry))})

if __name__ == '__main__':
    send_test()
