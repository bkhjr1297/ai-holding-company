# Zero-Cost / Open-Source Operating Stack

Principle: start at $0 using free/open-source, no-account, or low/no-KYC tools and Brian's existing channels. Add paid or KYC-heavy tools only when they unlock revenue or reduce owner dependence after validation.

## Stage 0 — Immediate $0 Stack

| Function | Tool | Cost | Notes |
|---|---|---:|---|
| CRM / pipeline | CSV files in repo, LibreOffice, or Google Sheets if already available | $0 | Start here; no setup drag |
| Lead research | Web search, Google Maps manually, business websites | $0 | Manual first 50-100 leads |
| Email drafting | Hermes + templates | $0 | Sending requires connected mailbox |
| Calling | Manual dialing from existing phone/Google Voice if Brian has one | $0 | Actual PSTN calling is never truly software-only |
| Scheduling | Cal.com free/self-host or Google Calendar if available | $0 | Can begin with manual calendar links |
| Customer tickets | FreeScout, osTicket, Zammad, or CSV initially | $0 | Add once customers exist |
| Automation | n8n community / Activepieces community / scripts | $0 self-host | Do not install until workflow proves demand |
| Docs/SOPs | Markdown files in `/root/ai-holding-company` | $0 | Current operating base |
| Landing page | Static HTML + Open Design | $0 | Host later on free tier if needed |

## Stage 1 — Free/Open-Source Self-Hosted Stack

| Function | Preferred Tool | Alternative | Why |
|---|---|---|---|
| CRM | EspoCRM | SuiteCRM | Open-source CRM for contacts, accounts, opportunities, workflows |
| Marketing automation | Mautic | listmonk | Mautic for campaigns/scoring; listmonk for simpler newsletters/lists |
| Scheduling | Cal.com | Easy!Appointments | Professional scheduling without paid Calendly |
| Customer support | FreeScout | Zammad / osTicket / Chatwoot | Shared inbox/ticketing for customer management |
| Workflow automation | n8n Community | Activepieces Community | Connect CRM, email, forms, calendars, reports |
| Call center/PBX | Asterisk / FreePBX | VICIdial | Open-source call routing/dialing, but still needs a phone number/SIP trunk |
| Website | Static site / Astro / Hugo | WordPress | Low/no hosting cost |
| Analytics | Matomo | Plausible CE | Open-source website analytics |

## Unavoidable / Likely External Costs

| Item | Why It May Be Needed | Free Workaround |
|---|---|---|
| Domain | Professional company image and email deliverability | Use existing domain/account temporarily |
| Mailbox | Sending professional email | Existing Gmail/Outlook account to validate |
| Phone number/SIP trunk | PSTN calling requires carrier access | Existing phone or Google Voice/manual dialing |
| Hosting/VPS | Self-hosted CRM/automation | Local machine first; free tiers where possible |

## Rule For Paid Tools

No paid tool is approved until it passes at least one test:

1. It is required to legally or technically perform the work.
2. It directly enables booked calls or revenue.
3. It replaces repeated manual work after the workflow is proven.
4. The first paying customer funds it.
