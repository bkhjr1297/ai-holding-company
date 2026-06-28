#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from ai_holding_company.payouts.runtime import observe_and_publish

if __name__ == '__main__':
    observe_and_publish()
