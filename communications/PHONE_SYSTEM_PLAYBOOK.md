# Phone System Playbook

## Current Status

Calling scripts and call logging are ready. Actual outbound calling requires a phone line or VoIP/SIP account.

## $0 Start

Use Brian's existing phone or a free/low-cost existing number manually.

Hermes handles:

- call list generation
- opener/script
- objection handling
- call notes
- next actions
- follow-up email drafting
- CRM updates

## Professional Call Flow

### Opening

```text
Hi, is this [Company]?

This is [Name] with Revenue Rescue Desk. We help Florida HVAC companies during summer call spikes by following up with missed calls and quote requests so more AC jobs actually get booked.

Quick question — when calls go to voicemail or web requests come in after hours, do you have a reliable follow-up process, or does it depend on who has time that day?
```

### If Busy

```text
No problem. Is there a better time today or tomorrow for a quick 5-minute call? I only wanted to ask about missed calls and quote requests during peak AC season.
```

### If Interested

```text
What we usually look for is simple: missed calls, voicemail, after-hours forms, and quote requests that sit too long. We help follow up, qualify the homeowner, and get the appointment on the calendar — then show you a weekly report of what was recovered.

Would a quick missed-revenue audit be useful?
```

### If They Ask "Are You AI?"

```text
We use automation and AI-assisted workflows behind the scenes, but the service is simple: faster follow-up, better tracking, and more booked jobs. You do not need to change your phone system to test it.
```

### Voicemail

```text
Hi [Name], this is [Name] with Revenue Rescue Desk. We help Florida HVAC companies recover missed calls and quote requests during summer call spikes. I had one quick idea for [Company]'s follow-up process. I'll send a short note as well. Again, [Name] with Revenue Rescue Desk, [phone].
```

## Call Dispositions

- No Answer
- Left Voicemail
- Gatekeeper
- Not Interested
- Asked for Email
- Interested — Follow Up
- Discovery Booked
- Bad Number
- Do Not Contact

## Follow-Up Timing

| Disposition | Next Action |
|---|---|
| No Answer | call again in 2 business days |
| Left Voicemail | send email same day if email available |
| Asked for Email | send summary immediately |
| Interested | schedule discovery or follow up within 24h |
| Not Interested | mark closed unless they invited later follow-up |
| Do Not Contact | suppress immediately |
