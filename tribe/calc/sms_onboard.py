#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any

from tribe.calc.onboarding import onboard_person, get_member

STATE = Path("/root/ai-holding-company/tribe/state/tribe.json")
LOG = Path("/root/ai-holding-company/tribe/logs/sms_onboarding.jsonl")
SESSIONS: dict[str, dict[str, Any]] = {}

STEP_WELCOME = "Welcome to the family circle. Reply with your first name."
STEP_RELATIONSHIP = "Are you a wife, sister, or mom? Reply: wife, sister, or mom."
STEP_WALLET = "Send your Trust Wallet address (starts with 0x)."
STEP_DONE = "You're in. Annabelle will text you when you're on rotation or if there's an emergency."


def log_sms(entry: dict) -> None:
    entry["timestamp"] = datetime.now(timezone.utc).isoformat()
    with LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def ensure_member(phone: str) -> dict:
    found = get_member(phone)
    if found:
        return found["member"]
    SESSIONS.setdefault(phone, {"step": "name", "data": {}})
    return {"phone": phone, "status": "pending"}


class SmsHandler(BaseHTTPRequestHandler):
    def do_POST(self):  # noqa: N802
        length = int(self.headers.get("content-length", 0))
        form_bytes = self.rfile.read(length)
        form = {}
        for pair in form_bytes.decode("utf-8", "ignore").split("&"):
            if "=" in pair:
                k, v = pair.split("=", 1)
                form[k] = v

        phone = form.get("From", "unknown")
        body = (form.get("Body") or "").strip()
        log_sms({"type": "inbound", "phone": phone, "body": body})

        member = ensure_member(phone)
        if member.get("status") == "active":
            response = "You're already in. Text HELP if you need anything."
        else:
            session = SESSIONS.setdefault(phone, {"step": "name", "data": {}})
            step = session.get("step", "name")
            data = session.setdefault("data", {})

            if step == "name":
                data["name"] = body
                session["step"] = "relationship"
                response = f"Nice, {body}. {STEP_RELATIONSHIP}"
            elif step == "relationship":
                rel = body.lower()
                if rel not in ("wife", "sister", "mom"):
                    response = "Please reply: wife, sister, or mom."
                else:
                    data["relationship"] = rel
                    session["step"] = "wallet"
                    response = STEP_WALLET
            elif step == "allet":
                    if not body.startswith("0x") or len(body) < 20:
                        response = "Please send a valid Trust Wallet address starting with 0x."
                    else:
                        data["trust_wallet"] = body
                        relationship = data.get("relationship", "wife")
                        try:
                            result = onboard_person(
                                role=relationship,
                                phone=phone,
                                name=data.get("name", phone),
                                trust_wallet=body,
                            )
                            session["step"] = "done"
                            name = result.get("member", {}).get("name", data.get("name", phone))
                            response = f"Welcome, {name}. {STEP_DONE}"
                        except Exception as exc:
                            response = f"Something went wrong saving your info. Try again. ({exc})"
            else:
                response = STEP_WELCOME

        log_sms({"type": "outbound", "phone": phone, "body": response})
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

    def do_GET(self):  # noqa: N802
        if self.path == "/sms/status":
            body = json.dumps({
                "sessions_active": len(SESSIONS),
                "total_onboarded": len(getattr(self.server, "state", {})),
            }).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
            return
        self.send_response(404)
        self.end_headers()


def run(host: str = "0.0.0.0", port: int = 7979):
    server = HTTPServer((host, port), SmsHandler)
    server.state = {"ok": True}
    print(f"SMS onboarding on {host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
