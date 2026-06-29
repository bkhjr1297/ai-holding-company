#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/root/ai-holding-company/tribe")
LOG = BASE / "logs/non_emergency_requests.jsonl"
STATE_FILE = BASE / "state/tribe.json"

DEFAULTS = {
    "non_emergency_line": {
        "active": True,
        "default_response": "Thank you. This is Annabelle. Please tell me if this is for: ride, food, clothing, or other. I'll handle it.",
        "routing_rules": [
            {"keywords": ["ride", "uber", "lyft", "taxi", "car", "bus", "travel"], "category": "ride", "handler": "dispatch_ride"},
            {"keywords": ["food", "hungry", "eat", "groceries", "meal", "doordash"], "category": "food", "handler": "dispatch_food"},
            {"keywords": ["clothes", "clothing", "shirt", "pants", "shoes", "jacket"], "category": "clothing", "handler": "dispatch_clothing"},
            {"keywords": ["other", "help", "assist", "support", "need"], "category": "other", "handler": "dispatch_other"},
        ],
    }
}


def load() -> dict:
    if STATE_FILE.exists():
        data = json.loads(STATE_FILE.read_text())
    else:
        data = {}
    data.setdefault("non_emergency_line", {})
    for key, value in DEFAULTS["non_emergency_line"].items():
        if isinstance(value, dict):
            data["non_emergency_line"].setdefault(key, {k: v for k, v in value.items()})
        else:
            data["non_emergency_line"].setdefault(key, value)
    return data


def save(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def log(event: str, detail: dict) -> None:
    entry = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **detail}
    with LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def classify_intent(message: str) -> dict:
    text = (message or "").lower()
    config = load().get("non_emergency_line", DEFAULTS["non_emergency_line"])
    for rule in config.get("routing_rules", []):
        if any(k in text for k in rule.get("keywords", [])):
            return rule
    return {"category": "unknown", "keywords": [], "handler": "dispatch_unknown"}


def handle_request(sender: str, message: str) -> dict:
    state = load()
    config = state.get("non_emergency_line", {})
    if not config.get("active", True):
        return {"status": "disabled", "message": "Non-emergency line is temporarily disabled."}

    intent = classify_intent(message)
    category = intent.get("category", "unknown")
    handler = intent.get("handler", "dispatch_unknown")

    log("request_received", {"sender": sender, "message": (message or "")[:500], "category": category})

    response = {
        "status": "dispatched",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sender": sender,
        "category": category,
        "handler": handler,
    }

    if handler == "dispatch_unknown":
        response["message"] = config.get("default_response", "I can help with ride, food, or clothing requests. Please say which one you need.")
    else:
        response["message"] = f"Got it — {category} request from {sender}. I'm handling it."

    log("request_dispatched", response)
    state["non_emergency_line"]["last_request"] = {
        "category": category,
        "sender": sender,
        "handler": handler,
        "timestamp": response["timestamp"],
    }
    save(state)
    return response


def run(message: str, sender: str) -> dict:
    return handle_request(sender=sender, message=message)


if __name__ == "__main__":
    import sys
    msg = sys.argv[1] if len(sys.argv) > 1 else ""
    sender = sys.argv[2] if len(sys.argv) > 2 else "unknown"
    print(json.dumps(run(msg, sender), indent=2))
