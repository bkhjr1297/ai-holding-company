#!/usr/bin/env python3
import csv
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'communications' / 'logs' / 'call_log.csv'
out = Path(__file__).resolve().parent.parent / 'communications' / 'reports' / 'daily_call_summary.txt'
out.parent.mkdir(parents=True, exist_ok=True)
text = p.read_text(errors='ignore') if p.exists() else ''
out.write_text(text)
print('Processed call log summary to', out)
