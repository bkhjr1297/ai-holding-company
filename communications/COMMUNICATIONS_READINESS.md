# Communications Readiness — Revenue Rescue Desk

Goal: make outbound calling, email outreach, customer management, and client-facing operations look professional and established while staying truthful and low-cost.

## Operating Posture

We present as a structured response-desk operation with defined departments, scripts, SLAs, QA, reporting, and customer-success workflows.

We do **not** fabricate company age, client count, certifications, offices, or historical results. Professional image comes from process maturity, not false claims.

## Current Tool Status

| Capability | Status | Tool / Path | What Remains |
|---|---|---|---|
| Email CLI | Installed | `/usr/local/bin/himalaya` | Needs mailbox IMAP/SMTP credentials/config |
| Google Workspace | Available but not authenticated | Hermes `google-workspace` skill | Needs Google OAuth client/token if chosen |
| Email drafting | Ready | templates in `communications/templates` | None |
| Cold calling scripts | Ready | `PHONE_SYSTEM_PLAYBOOK.md` | Need phone line / caller ID |
| Call logging | Ready | `scripts/log_call.py` | None |
| Lead queue | Ready | Florida HVAC CSV | None |
| Customer tracking | Ready | customer CSV + SOPs | None |
| Professional identity | Ready | `PROFESSIONAL_IDENTITY_SYSTEM.md` | Need chosen email/phone/domain |

## Minimum Channel Requirements To Actually Send/Call

To let Hermes send email directly, provide one of:

1. **IMAP/SMTP mailbox** with app password or password command for Himalaya.
2. **Gmail/Google Workspace OAuth** credentials for the Hermes Google Workspace skill.

To let Hermes place calls directly, provide one of:

1. Existing phone line handled manually by Brian/human operator.
2. SIP trunk / VoIP account usable by Asterisk/FreePBX/softphone.
3. Paid API like Twilio only after revenue justifies it.

## Recommended $0 Start

1. Use existing phone manually for calls.
2. Use existing email manually or configure Himalaya with an app password.
3. Hermes prepares scripts, emails, notes, follow-ups, and logs all outcomes.
4. First client revenue funds domain/mailbox/phone if needed.
