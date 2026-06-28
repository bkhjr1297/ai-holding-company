# Low / No-KYC Tool Policy

Brian's operating constraint: each portfolio business should launch as close to $0 startup cost as possible, using free/open-source and low/no-KYC tools first.

## Policy

Prioritize tools in this order:

1. **No-account local files** — CSV, Markdown, SQLite, static HTML, local scripts.
2. **Open-source self-hosted tools** — can run locally or on existing infrastructure without vendor approval.
3. **Free accounts with minimal identity friction** — only when needed for customer-facing presence or delivery.
4. **Paid tools only after validation** — first customer revenue should fund them.
5. **KYC-required tools last** — avoid banking, payment processing, telecom APIs, ad accounts, or regulated platforms until necessary.

## Guardrails

- Do not bypass KYC, CAPTCHA, platform anti-abuse systems, paywalls, or account restrictions.
- Do not create accounts that require Brian's legal identity, payment method, phone verification, or business documents without asking.
- Do not misrepresent company size, location, identity, or ownership.
- Use automation for legitimate setup, QA, public-data research, and operations — not abuse.
- Respect opt-outs, robots/terms, rate limits, and anti-spam laws.

## Setup Priority For New Businesses

| Need | First Choice | Later Upgrade |
|---|---|---|
| CRM | CSV/SQLite | EspoCRM/SuiteCRM |
| Website | Static HTML generated locally | Free static host / VPS |
| Email drafting | Hermes | Mailbox integration |
| Email sending | Existing mailbox/manual | Gmail OAuth / Himalaya / SMTP |
| Calling | Existing phone/manual dialing | SIP trunk, FreePBX, Twilio only after revenue |
| Scheduling | Manual calendar link | Cal.com self-host |
| Support | CSV/shared mailbox | FreeScout/Zammad/osTicket |
| Automation | Scripts | n8n/Activepieces self-host |
| Browser automation | Playwright / Playwright stealth | Keep compliant; no bypassing KYC/CAPTCHA |

## Playwright Stealth Install Status

Python:

```bash
python3 -m pip install playwright playwright-stealth
python3 -m playwright install chromium
```

Verified API:

```python
from playwright_stealth import Stealth
stealth = Stealth()
await stealth.apply_stealth_async(page)
```

Node workspace:

```bash
cd /root/ai-holding-company/tools/playwright-stealth-node
node verify-stealth.mjs
```

Verified output: `navigator.webdriver` is `false`.
