# Email System Setup

## Installed Tool

Himalaya CLI is installed:

```bash
/usr/local/bin/himalaya
himalaya --version
```

## Option A — Himalaya IMAP/SMTP

Best low/no-KYC path if Brian already has a mailbox.

Create:

```text
~/.config/himalaya/config.toml
```

Use the template:

```text
/root/ai-holding-company/communications/config/himalaya.config.template.toml
```

Then verify:

```bash
himalaya account list
himalaya folder list
himalaya envelope list --page-size 5
```

Send test only after explicit approval:

```bash
/root/ai-holding-company/communications/scripts/send_email_himalaya.sh recipient@example.com "Test" /path/to/body.txt
```

## Option B — Gmail/Google Workspace Hermes Skill

Current status: not authenticated.

Check:

```bash
python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --check
```

Needs Google OAuth client JSON and browser approval.

## Deliverability Setup When Domain Exists

For professional sending, configure:

| Record | Purpose |
|---|---|
| SPF | authorizes mail servers |
| DKIM | cryptographic signing |
| DMARC | policy + reporting |
| MX | inbound mail routing |

Cold outreach safety:

- Start low volume.
- Personalize emails.
- Include accurate sender identity.
- Track opt-outs.
- Do not blast generic templates.
- Keep daily volume conservative until domain/mailbox has history.

## Suggested Mailboxes

If/when domain exists:

- hello@domain — general inquiries
- response@domain — response desk
- support@domain — customers
- scheduling@domain — booked appointments
- brian@domain or first-name@domain — founder/owner identity

Start with one mailbox if cost must stay near zero.
