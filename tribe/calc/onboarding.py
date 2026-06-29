#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/root/ai-holding-company")
TRIBE = BASE / "tribe"
STATE = TRIBE / "state" / "tribe.json"
ONBOARD_LOG = TRIBE / "logs" / "onboarding.jsonl"

STATE.parent.mkdir(parents=True, exist_ok=True)
ONBOARD_LOG.parent.mkdir(parents=True, exist_ok=True)


def load_state() -> dict:
    if STATE.exists():
        try:
            return json.loads(STATE.read_text())
        except Exception:
            pass
    return {"members": {}}


def save_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, indent=2))


def log_onboarding(entry: dict) -> None:
    entry["timestamp"] = datetime.now(timezone.utc).isoformat()
    with ONBOARD_LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def onboard_wife(phone: str, name: str, trust_wallet: str, relationship: str = "wife") -> dict:
    state = load_state()
    members = state.setdefault("members", {})
    key = f"{relationship}_{phone}"
    members[key] = {
        "phone": phone,
        "name": name,
        "trust_wallet": trust_wallet,
        "relationship": relationship,
        "onboarded_at": datetime.now(timezone.utc).isoformat(),
        "status": "active",
        "rotation_enabled": True,
        "emergency_contact": True,
        "notify_preferences": ["telegram", "sms"],
    }
    save_state(state)
    entry = {
        "action": "onboard",
        "key": key,
        "phone": phone,
        "name": name,
        "trust_wallet": trust_wallet,
        "relationship": relationship,
    }
    log_onboarding(entry)
    return {"status": "onboarded", "member": members[key]}


def onboard_mom(phone: str, name: str, trust_wallet: str) -> dict:
    return onboard_wife(phone, name, trust_wallet, relationship="mom")


def onboard_person(role: str, phone: str, name: str, trust_wallet: str) -> dict:
    role = role.lower()
    if role in ("wife", "sister", "mom"):
        if role == "wife":
            return onboard_wife(phone, name, trust_wallet, relationship="wife")
        if role == "sister":
            return onboard_sister(phone, name, trust_wallet)
        if role == "mom":
            return onboard_mom(phone, name, trust_wallet)
    raise ValueError("Role must be 'wife', 'sister', or 'mom'")
    state = load_state()
    members = state.get("members", {})
    for key, member in members.items():
        if member.get("phone") == phone:
            return {"key": key, "member": member}
    return None


def list_onboarded() -> dict:
    state = load_state()
    return {"members": state.get("members", {}), "total": len(state.get("members", {}))}


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 onboarding.py <wife|sister> <phone> <name> <trust_wallet>")
        sys.exit(1)
    role = sys.argv[1]
    phone = sys.argv[2]
    name = sys.argv[3]
    wallet = sys.argv[4]
    if role == "wife":
        result = onboard_wife(phone, name, wallet)
    elif role == "sister":
        result = onboard_sister(phone, name, wallet)
    else:
        print("Role must be 'wife' or 'sister'")
        sys.exit(1)
    print(json.dumps(result, indent=2))
