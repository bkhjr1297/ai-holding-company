#!/usr/bin/env python3
from __future__ import annotations
import json, smtplib, textwrap
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

from tribe.calc.safeguards import can_payout, load as load_state
from tribe.calc.support_engine import build_schedule
from scripts.send_email_receipt import send_receipt, record_event

STATE = Path('/root/ai-holding-company/tribe/state/tribe.json')

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'bharmon1215@gmail.com'
SMTP_PASS = 'dygwbuvziyepwaka'
RECIPIENT = 'bharmon1215@gmail.com'

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
    folder = Path('/root/ai-holding-company/receipts/brian')
    folder.mkdir(parents=True, exist_ok=True)
    fname = f"receipt_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.md"
    p = folder / fname
    p.write_text(build_receipt_markdown(entry))
    return p

def send_email(subject: str, body_text: str, to_addr: str = None) -> None:
    to_addr = to_addr or RECIPIENT
    msg = EmailMessage()
    msg['From'] = SMTP_USER
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.set_content(body_text)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.ehlo()
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)

def email_receipt(entry: dict) -> None:
    subject = f"[Receipt] {entry.get('event', 'payout')} - {datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
    body = build_receipt_markdown(entry)
    send_email(subject, body)
    save_receipt(entry)
    record_event('receipt_sent', {
        'to': RECIPIENT,
        'subject': subject,
        'file': str(save_receipt(entry)),
    })

def run_payout() -> dict:
    state = load_state()
    ok, reason = can_payout(state)
    result = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'payout_allowed': bool(ok),
        'block_reason': reason if not ok else None,
        'stage': state.get('stage'),
    }
    if not ok:
        return result
    schedule = build_schedule(
        wives={
            '1': {'name': 'Wife 1', 'wallet': '0x', 'rent': 700, 'children': 1},
        },
        sister_wallet='0x',
        sister_rent=0,
    )
    total_brian = schedule.get('summary', {}).get('brian_keep', 0.0)
    entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'event': 'weekly_payout',
        'recipient': 'Brian Harmon',
        'amount_usd': round(float(total_brian), 2),
        'amount_eth': 0.0,
        'note': 'Email receipt only; actual transfer gated by funding/safeguards.',
    }
    try:
        email_receipt(entry)
        result['receipt_sent'] = True
        result['email_to'] = RECIPIENT
    except Exception as exc:  # pragma: no cover - defensive email handling
        result['receipt_sent'] = False
        result['receipt_error'] = str(exc)[:300]
    return result

if __name__ == '__main__':
    print(json.dumps(run_payout(), indent=2))
