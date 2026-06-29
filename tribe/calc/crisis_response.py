#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/root/ai-holding-company/tribe")
STATE = BASE / "state/tribe.json"
LOG = BASE / "logs/crisis_responses.jsonl"

DEFAULTS = {
    "crisis": {
        "active": False,
        "last_triggered_at": None,
        "last_assessment": None,
        "last_outcome": None,
        "contacts": [],
        "location": {
            "address": "",
            "lat": None,
            "lng": None,
            "notes": "",
        },
        "councils": [
            {"name": "triage-1", "model": "fast"},
            {"name": "triage-2", "model": "balanced"},
        ],
    }
}


def load() -> dict:
    if STATE.exists():
        data = json.loads(STATE.read_text())
    else:
        data = {}
    data.setdefault("crisis", {})
    for key, value in DEFAULTS["crisis"].items():
        if isinstance(value, dict):
            data["crisis"].setdefault(key, {k: v for k, v in value.items()})
        else:
            data["crisis"].setdefault(key, value)
    return data


def save(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2))


def log(event: str, detail: dict) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **detail}
    with LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def assess_llm_council(message: str, context: dict) -> dict:
    """Placeholder council assessment.

    In production this routes the message through multiple models
    and returns a consensus severity/action. For now it returns a
    deterministic fallback assessment so the rest of the pipeline
    can be validated end-to-end.
    """
    text = (message or "").lower()
    crisis_keywords = ["suicide", "kill", "hurt", "harm", "hospital", "emergency", " crisis"]
    is_crisis = any(k in text for k in crisis_keywords)
    if is_crisis:
        return {
            "severity": "high",
            "recommended_action": "escalate_to_authorities",
            "reason": "crisis keywords detected",
            "councils": [
                {"name": "triage-1", "verdict": "high"},
                {"name": "triage-2", "verdict": "high"},
            ],
        }
    return {
        "severity": "low",
        "recommended_action": "annabelle_handle",
        "reason": "no crisis indicators",
        "councils": [
            {"name": "triage-1", "verdict": "low"},
            {"name": "triage-2", "verdict": "low"},
        ],
    }


def handle_council_result(state: dict, assessment: dict, message: str, sender: str) -> dict:
    action = assessment.get("recommended_action", "annabelle_handle")
    crisis = state.setdefault("crisis", {})
    crisis["last_triggered_at"] = datetime.now(timezone.utc).isoformat()
    crisis["last_assessment"] = assessment
    location = crisis.get("location", {}) or {}
    address = location.get("address", "")
    if action == "escalate_to_authorities":
        crisis["active"] = True
        crisis["last_outcome"] = "authorities_notified"
        log("crisis_escalation", {
            "sender": sender,
            "message": (message or "")[:500],
            "assessment": assessment,
            "location": address,
        })
        # In production this would actually call emergency services
        # and play a synthesized voice briefing.
        payload = {
            "status": "authorities_alerted",
            "location": address,
            "brief": "Mental health crisis reported by family contact. Subject may be incapacitated. Nearest hospital transport requested.",
        }
        crisis["last_outcome"] = json.dumps(payload)
        save(state)
        return {"action": "escalate_to_authorities", "payload": payload}
    crisis["active"] = False
    crisis["last_outcome"] = "annabelle_handled"
    log("crisis_routine", {"sender": sender, "message": (message or "")[:300], "assessment": assessment})
    save(state)
    return {"action": "annabelle_handle", "message": "Annabelle has this under control."}


def run(message: str, sender: str) -> dict:
    state = load()
    assessment = assess_llm_council(message, state)
    result = handle_council_result(state, assessment, message, sender)
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sender": sender,
        "assessment": assessment,
        "result": result,
    }


if __name__ == "__main__":
    import sys
    msg = sys.argv[1] if len(sys.argv) > 1 else ""
    sender = sys.argv[2] if len(sys.argv) > 2 else "unknown"
    print(json.dumps(run(msg, sender), indent=2))
