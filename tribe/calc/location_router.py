#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/root/ai-holding-company/tribe")
STATE = BASE / "state/tribe.json"
LOG = BASE / "logs/location_routing.jsonl"


DEFAULT_MEMBERS = {
    "brian": {"label": "Brian", "lat": None, "lng": None, "address": "", "role": "self"},
    "sister": {"label": "Sister", "lat": None, "lng": None, "address": "", "role": "sister"},
    "wife1": {"label": "Wife 1", "lat": None, "lng": None, "address": "", "role": "wife"},
    "wife2": {"label": "Wife 2", "lat": None, "lng": None, "address": "", "role": "wife"},
    "wife3": {"label": "Wife 3", "lat": None, "lng": None, "address": "", "role": "wife"},
    "wife4": {"label": "Wife 4", "lat": None, "lng": None, "address": "", "role": "wife"},
    "wife5": {"label": "Wife 5", "lat": None, "lng": None, "address": "", "role": "wife"},
}


def load() -> dict:
    if STATE.exists():
        data = json.loads(STATE.read_text())
    else:
        data = {}
    data.setdefault("locations", {})
    for key, value in DEFAULT_MEMBERS.items():
        data["locations"].setdefault(key, dict(value))
    return data


def save(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2))


def log(event: str, detail: dict) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = {"timestamp": datetime.now(timezone.utc).isoformat(), "event": event, **detail}
    with LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def update_location(member_id: str, lat: float, lng: float, address: str = "") -> dict:
    state = load()
    locs = state.setdefault("locations", {})
    if member_id not in locs:
        locs[member_id] = dict(DEFAULT_MEMBERS.get(member_id, {"label": member_id, "role": "unknown"}))
    locs[member_id].update({"lat": lat, "lng": lng, "address": address, "updated_at": datetime.now(timezone.utc).isoformat()})
    state["locations"] = locs
    save(state)
    log("location_updated", {"member_id": member_id, "lat": lat, "lng": lng})
    return locs[member_id]


def nearest_safe_location(target_lat: float, target_lng: float, exclude: list[str] | None = None) -> dict:
    state = load()
    locs = state.get("locations", {})
    candidates = []
    exclude = exclude or []
    for member_id, loc in locs.items():
        if member_id in exclude:
            continue
        if member_id == "brian":
            continue
        if loc.get("lat") is None or loc.get("lng") is None:
            continue
        dlat = (loc["lat"] - target_lat) ** 2
        dlng = (loc["lng"] - target_lng) ** 2
        dist = (dlat + dlng) ** 0.5
        candidates.append({
            "member_id": member_id,
            "label": loc.get("label", member_id),
            "role": loc.get("role", "unknown"),
            "distance_deg": dist,
            "address": loc.get("address", ""),
            "lat": loc.get("lat"),
            "lng": loc.get("lng"),
        })
    candidates.sort(key=lambda x: x["distance_deg"])
    return candidates[0] if candidates else {}


def run_nearest(target_lat: float, target_lng: float, exclude: list[str] | None = None) -> dict:
    result = nearest_safe_location(target_lat, target_lng, exclude)
    if not result:
        return {"status": "no_destination_known"}
    log("nearest_requested", {"target_lat": target_lat, "target_lng": target_lng, "result": result})
    return {"status": "ok", "destination": result}


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        lat, lng = float(sys.argv[1]), float(sys.argv[2])
    else:
        lat, lng = 40.7128, -74.0060
    print(json.dumps(run_nearest(lat, lng), indent=2))
