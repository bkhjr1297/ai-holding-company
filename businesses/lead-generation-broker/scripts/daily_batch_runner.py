#!/usr/bin/env python3
from pathlib import Path
from datetime import date, timedelta

root = Path(__file__).resolve().parent.parent
print(f"Running lead-generation-broker daily batch for", date.today().isoformat())
