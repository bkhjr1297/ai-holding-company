#!/usr/bin/env python3
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent.parent
jobs = [
    root / 'businesses/appointment-setting/scripts/generate_outreach_batch.py',
    root / 'businesses/lead-generation-broker/scripts/generate_lead_batch.py',
    root / 'businesses/recruiting/scripts/generate_candidate_list.py',
    root / 'communications/scripts/process_call_logs.py',
]
for job in jobs:
    if job.exists():
        print('Running:', job)
        subprocess.run(['python3', str(job)], check=False)
