#!/usr/bin/env python3
from __future__ import annotations
import json, smtplib, textwrap
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

BASE = Path('/root/ai-holding-company')
STATE = BASE / 'tribe/state/tribe.json'
RECEIPTS = BASE / 'receipts'
LOG = BASE / 'tribe/logs/ledger.jsonl'
ROTATION_LOG = BASE / 'tribe/logs/rotation.jsonl'

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'bharmon1215@gmail.com'
SMTP_PASS = 'dygwbuvziyepwaka'
TO_ADDR = 'bharmon1215@gmail.com'


def _load_json(path: Path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def _latest_lines(path: Path, n: int = 5):
    if not path.exists():
        return []
    lines = path.read_text(errors='ignore').splitlines()
    return lines[-n:]


def build_report():
    state = _load_json(STATE)
    weekly = float(state.get('financial', {}).get('ssi_base', 943)) + float(state.get('financial', {}).get('side_income_est', 600))
    payout_allowed = state.get('payout_allowed')
    block_reason = state.get('payout_block_reason')
    stage = state.get('stage')
    rot = _load_json(BASE / 'tribe/state/tribe.json').get('rotation', {})
    current = rot.get('order', [])[rot.get('cursor', 0) % max(len(rot.get('order', [])), 1)]

    lines = [
        f"WEEKLY TRIBE SUMMARY — {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
        "=" * 50,
        f"Stage : {stage}",
        f"Payout allowed : {payout_allowed}" + (f" ({block_reason})" if block_reason else ""),
        f"Weekly income  : ${weekly:.2f}",
        f"Wife rotation  : {current}",
        "",
        "RECENT LEDGER",
    ]
    lines.extend(f"  - {x}" for x in _latest_lines(LOG))
    lines += [
        "",
        "RECENT ROTATIONS",
    ]
    lines.extend(f"  - {x}" for x in _latest_lines(ROTATION_LOG))
    body = "\n".join(lines) + "\n"

    now = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    msg = EmailMessage()
    msg['From'] = SMTP_USER
    msg['To'] = TO_ADDR
    msg['Subject'] = f"[Tribe] Weekly Summary {now}"
    msg.set_content(body)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.ehlo()
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)
    return {"status": "sent", "to": TO_ADDR, "subject": msg['Subject']}


if __name__ == '__main__':
    print(json.dumps(build_report(), indent=2))
