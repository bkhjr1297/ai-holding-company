# First 30 Minutes Of Cold Calling

This is the exact first session. Do not improvise.

## Minute 0-5 — Warm Up

Read the opener out loud 5 times:

```text
Hi, is this [Company]?

This is Brian with Revenue Rescue Desk. We help Florida HVAC companies during summer call spikes by following up with missed calls and quote requests so more AC jobs actually get booked.

Quick question — when calls go to voicemail or web requests come in after hours, do you have a reliable follow-up process, or does it depend on who has time that day?
```

## Minute 5-10 — Open The Console

Run:

```bash
/root/ai-holding-company/communications/scripts/guided_call_console.py --start 1 --count 5
```

## Minute 10-25 — Make 5 Calls

For each call:

1. Dial the number manually.
2. Read the opener exactly.
3. Stop talking after the question.
4. Use the objection menu if needed.
5. Pick a disposition.
6. Type notes.
7. Move to the next call.

## Minute 25-30 — Review

Look at:

```bash
/root/ai-holding-company/communications/logs/call_log.csv
```

Count:

- calls made
- conversations
- voicemails
- asked for email
- follow-ups needed

## Success Criteria

The first session is successful if you make 5 calls and log them.

It does not matter if nobody buys.
It does not matter if you feel awkward.
It does not matter if you get rejected.

The win is starting the machine.
