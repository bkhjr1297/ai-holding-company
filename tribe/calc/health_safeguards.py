#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/root/ai-holding-company/tribe")
STATE = BASE / "state/tribe.json"
LOG = BASE / "logs/health_safeguards.jsonl"


DEFAULTS = {
    "health": {
        "medication_adherence_pct": 100.0,
        "glucose_check_required_daily": True,
        "a1c_target": 7.0,
        "fitness_min_weekly_steps": 0,
        "fitness_min_weekly_active_min": 0,
        "mental_health": {
            "therapy_sessions_required_monthly": 0,
            "crisis_plan_required": False,
            "symptom_log_required_daily": False,
        },
        "allowances": {
            "extra_food_budget_if_sedentary": False,
            "budget_override_requires_daily_activity_log": True,
        },
        "flags": {
            "high_risk_diabetes": False,
            "high_risk_mental_health": False,
            "emergency_contacts": [],
        },
    }
}


def load() -> dict:
    if STATE.exists():
        data = json.loads(STATE.read_text())
    else:
        data = {}
    if "health" not in data:
        data["health"] = {}
    for key, value in DEFAULTS["health"].items():
        if isinstance(value, dict):
            data["health"].setdefault(key, {k: v for k, v in value.items()})
        else:
            data["health"].setdefault(key, value)
    return data


def save(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2))


def log(event: str, detail: dict) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **detail}
    with LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def add_health_log(kind: str, detail: dict) -> None:
    health_log = STATE if STATE.exists() else None
    # Separate ledger for health events
    log("health_" + kind, detail)


def check_diabetes(state: dict) -> dict:
    health = state.get("health", {})
    adherence = float(health.get("medication_adherence_pct", 100) or 100)
    a1c = health.get("a1c_last", None)
    flag = adherence < 80.0
    if a1c is not None:
        try:
            flag = flag or float(a1c) > 8.5
        except (TypeError, ValueError):
            pass
    if flag and not bool(health.get("flags", {}).get("high_risk_diabetes", False)):
        health.setdefault("flags", {})["high_risk_diabetes"] = True
        add_health_log("diabetes_risk_raised", {"adherence_pct": adherence, "a1c": a1c})
    elif not flag and bool(health.get("flags", {}).get("high_risk_diabetes", False)):
        health.setdefault("flags", {})["high_risk_diabetes"] = False
        add_health_log("diabetes_risk_cleared", {"adherence_pct": adherence, "a1c": a1c})
    return {"adherence_pct": adherence, "a1c": a1c, "high_risk": bool(health.get("flags", {}).get("high_risk_diabetes", False))}


def check_mental_health(state: dict) -> dict:
    health = state.get("health", {})
    mh = health.get("mental_health", {})
    flag = False
    if mh.get("crisis_plan_required") and not mh.get("crisis_plan_on_file"):
        flag = True
    if mh.get("symptom_log_required_daily") and not mh.get("latest_log_date"):
        flag = True
    if flag and not bool(health.get("flags", {}).get("high_risk_mental_health", False)):
        health.setdefault("flags", {})["high_risk_mental_health"] = True
        add_health_log("mental_health_risk_raised", {"mental_health": mh})
    elif not flag and bool(health.get("flags", {}).get("high_risk_mental_health", False)):
        health.setdefault("flags", {})["high_risk_mental_health"] = False
        add_health_log("mental_health_risk_cleared", {"mental_health": mh})
    return {"mental_health": mh, "high_risk": bool(health.get("flags", {}).get("high_risk_mental_health", False))}


def check_fitness(state: dict) -> dict:
    health = state.get("health", {})
    return {
        "weekly_steps": 0,
        "weekly_active_min": 0,
        "required_steps": health.get("fitness_min_weekly_steps", 0),
        "required_active_min": health.get("fitness_min_weekly_active_min", 0),
        "sedentary": True,
    }


def run() -> dict:
    state = load()
    diabetes = check_diabetes(state)
    mental_health = check_mental_health(state)
    fitness = check_fitness(state)
    health = state["health"]
    apply_strict_mode = diabetes["high_risk"] or mental_health["high_risk"]
    if apply_strict_mode:
        health["allowances"]["extra_food_budget_if_sedentary"] = False
        health["allowances"]["budget_override_requires_daily_activity_log"] = True
    state["health"] = health
    save(state)
    add_health_log("health_check", {"diabetes": diabetes, "mental_health": mental_health, "fitness": fitness})
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "strict_mode": apply_strict_mode,
        "diabetes": diabetes,
        "mental_health": mental_health,
        "fitness": fitness,
        "allowances": health.get("allowances", {}),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
