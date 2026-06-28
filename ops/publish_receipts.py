#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone
from ai_holding_company.payouts.receipts_email import send_receipts

if __name__ == '__main__':
    send_receipts(weekly=True)
