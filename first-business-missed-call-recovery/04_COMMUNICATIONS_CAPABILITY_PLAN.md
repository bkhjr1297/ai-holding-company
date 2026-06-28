# Communications Capability Plan

Requirement from Brian: the company must be able to cold call, send email outreach, manage customers, and project the image of a larger professional company.

## Current Live Capability Status

| Capability | Current Status | Evidence / Note | Next Step |
|---|---|---|---|
| Draft cold emails | Ready | Hermes can generate and personalize copy | Use templates in this kit |
| Send cold emails | Not connected | Google Workspace not authenticated; Himalaya not configured | Connect Gmail/Workspace or install/configure Himalaya |
| Cold call scripts | Ready | Scripts included | Use manual dialing first |
| Place phone calls autonomously | Not connected | No Twilio/SIP/telephony account available | Start manual; later add Google Voice/SIP/Twilio if justified |
| CRM/customer tracking | Ready as CSV | CSV schemas included | Use CSV immediately; migrate to EspoCRM later |
| Customer support inbox | Not installed | FreeScout/Zammad/osTicket available options | Install when first client signs |
| Scheduling | Manual-ready | Calendar link/channel needed | Use existing calendar; later Cal.com |

## Email Setup Options

### Option A — Fastest $0 Validation

Use an existing Gmail/Outlook mailbox manually.

- Hermes writes emails.
- Brian reviews/sends manually.
- CRM CSV tracks sent/replies.
- No setup cost.

### Option B — Gmail/Google Workspace Through Hermes

Requires Google OAuth setup.

- Best if Brian wants Hermes to search/send/reply via Gmail and manage Calendar/Sheets.
- Current check: `NOT_AUTHENTICATED`.
- Setup requires Google OAuth client credentials and token.

### Option C — Himalaya IMAP/SMTP

- Free CLI-based email operations.
- Requires `himalaya` installed and mailbox IMAP/SMTP/app-password configured.
- Current check: command not installed.

## Calling Setup Options

### Option A — Manual Dialing From Existing Phone

Best for $0 start.

- Hermes builds lead lists, scripts, objection handling, call notes, and follow-up tasks.
- Brian or a human dials.
- Hermes logs outcomes and writes follow-up emails.

### Option B — Google Voice / Existing VoIP

Potentially low/no cost if Brian already has it.

- Use for professional caller ID.
- Calls still likely manual unless API access is available.

### Option C — Asterisk/FreePBX/VICIdial + SIP trunk

Software is open-source, but SIP trunk/phone numbers usually cost money.

Use only after validated revenue.

### Option D — Twilio/paid API

Fast automation, but not zero startup cost. Defer until first customer revenue funds it.

## Compliance Guardrails

- Check DNC rules before cold calling consumers; focus B2B/business numbers first.
- Respect opt-outs immediately.
- Do not use deceptive caller ID or misrepresent company size.
- Cold emails must include accurate identity and a simple opt-out path.
- Track every touch and response.
- Do not mass-send generic cold emails; use researched, personalized outreach.

## Immediate Operating Mode

Until channels are connected:

1. Hermes researches leads and drafts scripts/messages using free/open data.
2. Use no-account/local tooling first: CSV, Markdown, scripts, browser automation for public pages.
3. Brian approves target niche and sending/calling identity.
4. Manual outreach begins from existing channels.
5. Hermes tracks pipeline and writes follow-ups.
6. First revenue funds domain/mailbox/phone/hosting if needed.

## Low / No-KYC Rule

Prioritize tools that require no account, no payment method, no business documents, and no phone verification. Avoid paid telecom APIs, ad accounts, payment processors, and other KYC-heavy systems until the business has validated demand or revenue. Do not bypass KYC/CAPTCHA/anti-abuse systems; use self-hosted and public-data workflows instead.
