#!/usr/bin/env python3
"""
Automation script stub: Podcast production intake router.

Expected behavior:
- Watch a `/watched/` folder for new client intake form submissions.
- Validate form fields against required schema.
- Create a project record in the internal CRM/DB.
- Assign PM and provision client shared storage.
- Log every action to an audit trail.
- Do NOT send emails; route for human review.
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("intake-router")

WATCHED_DIR = Path(os.getenv("PODCAST_WATCHED_DIR", "./watched"))
AUDIT_TRAIL = Path(os.getenv("INTAKE_AUDIT_TRAIL", "./intake_audit.jsonl"))


def audit(**event):
    record = {"ts": datetime.now(timezone.utc).isoformat(), **event}
    with open(AUDIT_TRAIL, "a") as f:
        f.write(json.dumps(record) + "\n")


def validate_form(form: Dict[str, Any]) -> List[str]:
    missing = []
    required = [
        "full_name",
        "business_name",
        "email",
        "show_title",
        "selected_plan",
    ]
    for field in required:
        if not form.get(field):
            missing.append(field)
    if form.get("selected_plan") not in {"Spark", "Ignite", "Blaze"}:
        missing.append("selected_plan (invalid value)")
    return missing


def provision_project(form: Dict[str, Any]) -> Dict[str, Any]:
    project = {
        "client_name": form.get("business_name"),
        "contact": form.get("email"),
        "show_title": form.get("show_title"),
        "plan": form.get("selected_plan"),
        "status": "provisioned",
        "requested_at": datetime.now(timezone.utc).isoformat(),
        "assigned_pm": "PENDING_PM_ASSIGNMENT",
        "artifacts": {
            "notes": "",
            "shared_folder": "",
            "rss": "",
        },
    }
    # TODO: Write to internal CRM/DB here
    logger.info("Project record created (stub): %s", project)
    return project


def handle_new_form(form_path: Path):
    logger.info("New form detected: %s", form_path)
    audit(event="form_detected", path=str(form_path))

    try:
        form = json.loads(form_path.read_text())
    except Exception as exc:
        logger.error("Failed to parse form %s: %s", form_path, exc)
        audit(event="form_parse_error", error=str(exc), path=str(form_path))
        return

    missing = validate_form(form)
    if missing:
        logger.warning("Form %s missing fields: %s", form_path, missing)
        audit(event="form_validation_failed", missing=missing, path=str(form_path))
        return

    project = provision_project(form)
    audit(event="project_provisioned", project=project)
    logger.info("Intake processed for %s", form.get("business_name"))


def watch_loop():
    logger.info("Watching directory: %s", WATCHED_DIR)
    WATCHED_DIR.mkdir(parents=True, exist_ok=True)
    seen = set()
    while True:
        files = sorted(WATCHED_DIR.glob("*.json"))
        new_files = [f for f in files if f not in seen]
        if new_files:
            for f in new_files:
                handle_new_form(f)
            seen.update(new_files)
        # In production use proper filesystem watcher (watchdog / inotify).
        # This polling loop is a stub for demonstration.
        import time
        time.sleep(5)


if __name__ == "__main__":
    # For a single run on a provided file (CI/setup):
    if len(sys.argv) > 1:
        handle_new_form(Path(sys.argv[1]))
    else:
        watch_loop()
