"""
AI Automation Agency — automation stub.

This file documents the interfaces and entrypoints that ops or engineering
would wire to:
- Web form / submission intake
- CRM integration when approved
- Retainer health check reporter
- Weekly pipeline report

No side-effect actions are performed: no email sends, no CRM writes, and
no third-party API calls are made from this stub.
"""

from __future__ import annotations

import csv
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BASE_DIR = Path(
    os.getenv(
        "AI_AUTOMATION_BASE",
        "/root/ai-holding-company/businesses/ai-automation-agency",
    )
)
CLIENTS_DIR = BASE_DIR / "clients"
ORDERS_LOG = BASE_DIR / "docs" / "orders_log.csv"
METRICS_LOG = BASE_DIR / "docs" / "weekly_metrics.csv"


def ensure_dirs() -> None:
    CLIENTS_DIR.mkdir(parents=True, exist_ok=True)
    ORDERS_LOG.parent.mkdir(parents=True, exist_ok=True)
    METRICS_LOG.parent.mkdir(parents=True, exist_ok=True)


def new_client_id(name: str) -> str:
    slug = "".join(c if c.isalnum() else "-" for c in name).strip("-").lower()[:40]
    uid = uuid.uuid4().hex[:6]
    return f"{slug}-{uid}"


def new_order_id() -> str:
    count = 1
    if ORDERS_LOG.exists():
        count = sum(1 for _ in ORDERS_LOG.open()) if ORDERS_LOG.exists() else 0
    return f"AUTO-{datetime.now(timezone.utc):%Y}-{str(count).zfill(4)}"


def create_order(
    client_name: str,
    industry: str = "",
    outcome_goal: str = "",
    **fields: Any,
) -> dict[str, Any]:
    ensure_dirs()
    client_id = new_client_id(client_name)
    order_id = new_order_id()
    dir_path = CLIENTS_DIR / client_id / order_id
    dir_path.mkdir(parents=True)
    intake_path = dir_path / "intake.json"
    intake = {
        "client_name": client_name,
        "client_id": client_id,
        "order_id": order_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "industry": industry,
        "outcome_goal": outcome_goal,
        **fields,
    }
    intake_path.write_text(json.dumps(intake, indent=2) + "\n")
    _append_orders_log(order_id, client_id, client_name, intake)
    return {
        "status": "created",
        "order_id": order_id,
        "client_id": client_id,
        "client_name": client_name,
        "path": str(dir_path),
    }


def _append_orders_log(
    order_id: str,
    client_id: str,
    client_name: str,
    intake: dict[str, Any],
) -> None:
    file_exists = ORDERS_LOG.exists()
    with ORDERS_LOG.open("a", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "order_id",
                "client_id",
                "client_name",
                "created_at",
                "industry",
                "outcome_goal",
                "retainer_interest",
                "source",
            ],
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {
                "order_id": order_id,
                "client_id": client_id,
                "client_name": client_name,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "industry": intake.get("industry", ""),
                "outcome_goal": intake.get("outcome_goal", ""),
                "retainer_interest": intake.get("retainer_interest", ""),
                "source": intake.get("source", ""),
            }
        )


def route_to_delivery(order_id: str) -> dict[str, Any]:
    """Stub delivery router. In production this would emit to the agency-agents
    queue, post to Slack, or call an internal delivery endpoint.
    """
    return {"status": "queued", "order_id": order_id, "assigned_to": "delivery-agent"}


if __name__ == "__main__":
    demo = create_order(
        client_name="Demo Smb Co",
        industry="Trades",
        outcome_goal="Reduce missed leads from 25% to under 5%",
        retainer_interest="yes",
        source="partner",
    )
    print(demo)
