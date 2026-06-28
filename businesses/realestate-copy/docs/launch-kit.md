# Launch Kit Checklist — AI Real Estate Listing Copy
## From build to first live listing

### Week 0: Pre-launch build

- [x] Business definition: README
- [x] Positioning: POSITIONING.md
- [x] Pricing: pricing.md
- [x] Website copy: website/COPY.md
- [x] Order form: templates/order-form.md
- [x] Listing copy template: templates/listing-copy-template.md
- [x] SOP: docs/sop-operations.md
- [x] Automation stub: scripts/automation_scheduler.py + scripts/cli.py
- [x] Lead sources: LEAD-SOURCES.md
- [x] Workforce roster: agent-roster/producer.md
- [ ] Stripe product set up for $499 subscription + $29/$79 one-time
- [ ] Email provider + list configured (prefer transactional that won’t flag outreach)
- [ ] Domain + landing page live
- [ ] Cal.com or equivalent scheduling for training/team onboarding
- [ ] Boilerplate registry created for first 3 target states
- [ ] CRM: Notion, Airtable, or light CRM with order pipeline + client folders

### Day 1: Proof of concept

- [ ] Produce 3 real listings (or redacted comps) to verify voice modes.
- [ ] Showcase before/after to 2–3 agents. Use as case study + ask for referral.
- [ ] Publish 1 short social post showing a rewritten description + outcome.

### Week 1: Pipeline fill

- [ ] 30 expired listing outreaches sent.
- [ ] 2 partnership conversations started (brokerage marketing director + TC).
- [ ] Lead magnet: “5 Listing Description Teardowns” built and live at squeeze page.

### Week 2–4: Validation loop

- [ ] Close first 3 paying clients.
- [ ] Check order size by voice mode and tighten template if one mode dominates.
- [ ] Gather feedback; update SOP and template if QA rejects spike on particular issue.
- [ ] If on-time rate < 95%, add second production agent or move rush cutoff earlier.

### Month 2+: Scale

- [ ] Add paid ads only after offer conversion proven organically.
- [ ] Expand boilerplate registry per state growth.
- [ ] Train second copy production agent on voice calibration.
- [ ] Launch team plan to first brokerage target.
- [ ] Introduce quarterly brand audit as upsell.

### Agency Agents Workforce activation

1. **Intake Agent** — validate form fields, create client folder via:
   ```
   python -m scripts.cli intake --name "Agent Name" --tier subscription --voice luxury
   ```
2. **Route Agent** — hand order to production:
   ```
   python -m scripts.cli route --order-id RC-2026-0001
   ```
3. **Production Agent** — read `templates/listing-copy-template.md`, write outputs, save to
   `/clients/<client_id>/<order_id>/draft.md`
4. **QA Agent** — run checklist in `docs/sop-operations.md §4.4`, approve or reject.
5. **Delivery Agent** — deliver approved assets, archive to `final.zip`, mark complete in orders log.

### Do not do this (no-side-effect policy)
- Do not send emails to contacts you haven’t explicitly authorized.
- Do not cold-call or scrape MLS data without a permissible purpose.
- Do not modify a client’s listing on their behalf; only draft copy for them to publish.
- Do not store client payment card data; use Stripe Checkout / invoicing.
