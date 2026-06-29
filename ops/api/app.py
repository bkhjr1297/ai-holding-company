#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse

app = FastAPI(title="AIHQ Mission Control")

DASHBOARD_HTML = (Path(__file__).resolve().parent.parent / "dashboard/index.html").read_text()
WIFE_PORTAL_HTML = (Path(__file__).resolve().parent.parent / "tribe-portal/index.html").read_text()


def _safe_import(module_path: str):
    try:
        import importlib
        mod = importlib.import_module(module_path)
        if hasattr(mod, "run"):
            return mod.run()
        if hasattr(mod, "load"):
            return mod.load()
        return {"status": "loaded", "module": module_path}
    except Exception as exc:  # pragma: no cover - defensive handler
        return {"status": "error", "module": module_path, "error": str(exc)[:200]}


@app.get("/api/tribe/state")
async def tribe_state() -> JSONResponse:
    state = _safe_import("tribe.calc.safeguards")
    return JSONResponse(state)


@app.get("/api/safeguards")
async def safeguards() -> JSONResponse:
    state = _safe_import("tribe.calc.safeguards")
    return JSONResponse(state)


@app.get("/api/rotation/current")
async def rotation_current() -> JSONResponse:
    state = _safe_import("tribe.calc.rotation")
    return JSONResponse(state)


@app.get("/api/services")
async def services() -> JSONResponse:
    import json
    manifest = json.loads(Path("/root/ai-holding-company/ops/ops-manifest.json").read_text())
    return JSONResponse(manifest.get("services", {}))


@app.get("/api/revenue")
async def revenue() -> JSONResponse:
    ledger = Path("/root/ai-holding-company/tribe/logs/ledger.jsonl")
    latest = ""
    if ledger.exists():
        lines = ledger.read_text(errors="ignore").splitlines()
        if lines:
            latest = lines[-1]
    return JSONResponse({"latest_batch": latest[:120], "revenue": 0.0})


@app.get("/", response_class=HTMLResponse)
async def dashboard() -> HTMLResponse:
    return HTMLResponse(DASHBOARD_HTML)


@app.get("/tribe-portal/", response_class=HTMLResponse)
async def wife_portal() -> HTMLResponse:
    return HTMLResponse(WIFE_PORTAL_HTML)


@app.get("/favicon.ico", include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse(Path(__file__).resolve().parent / "favicon.ico", media_type="image/x-icon")


@app.post("/api/location/update")
async def location_update(payload: dict) -> JSONResponse:
    try:
        member_id = str(payload.get("member_id", "brian"))
        lat = float(payload.get("lat", 0))
        lng = float(payload.get("lng", 0))
        address = str(payload.get("address", ""))
    except Exception as exc:
        return JSONResponse({"status": "error", "error": str(exc)}, status_code=400)
    from tribe.calc.location_router import update_location
    result = update_location(member_id, lat, lng, address)
    return JSONResponse({"status": "ok", "location": result})


@app.get("/api/location/nearest")
async def location_nearest(lat: float = 40.7128, lng: float = -74.006) -> JSONResponse:
    from tribe.calc.location_router import run_nearest
    result = run_nearest(lat, lng)
    return JSONResponse(result)


@app.post("/api/crisis/assess")
async def crisis_assess(payload: dict) -> JSONResponse:
    from tribe.calc.crisis_response import run as crisis_run
    sender = str(payload.get("sender", "unknown"))
    message = str(payload.get("message", ""))
    try:
        result = crisis_run(message, sender)
    except Exception as exc:
        return JSONResponse({"status": "error", "error": str(exc)}, status_code=500)
    return JSONResponse({"status": "ok", **result})
