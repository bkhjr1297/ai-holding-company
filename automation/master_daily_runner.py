#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys, json, csv
from datetime import date

root = Path(__file__).resolve().parent.parent

jobs = [
    {
        "name": "appointment-setting",
        "script": root / "businesses/appointment-setting/scripts/daily_batch_runner.py",
        "revenue_file": root / "businesses/appointment-setting/data/revenue.csv",
    },
    {
        "name": "lead-generation-broker",
        "script": root / "businesses/lead-generation-broker/scripts/daily_batch_runner.py",
        "revenue_file": root / "businesses/lead-generation-broker/data/revenue.csv",
    },
    {
        "name": "recruiting",
        "script": root / "businesses/recruiting/scripts/daily_batch_runner.py",
        "revenue_file": root / "businesses/recruiting/data/revenue.csv",
    },
    {
        "name": "comms",
        "script": root / "communications/scripts/daily_comms_processor.py",
        "revenue_file": None,
    },
]

summary = []
for job in jobs:
    script = job["script"]
    summary.append(f"{job['name']}: {'found' if script.exists() else 'missing script'}")

print('\n'.join(summary))
