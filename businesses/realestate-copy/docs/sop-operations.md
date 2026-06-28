# SOP: Listing Copy Service
## Standard Operating Procedure — AI Real Estate Listing Copy Agency
Version: 1.0
Owner: Operations
Audience: Sales / Intake → Copy Production → QA → Delivery

---

## 1. Purpose
To deliver MLS-ready, brand-aligned, Fair-Housing-compliant listing copy on time, every time, with zero compliance incidents.

## 2. Scope
Applies to all orders — subscription unlimited, à la carte, rush, team, brokerage.

## 3. Roles

| Role | Responsibility |
|------|----------------|
| **Sales / Intake Agent** | Qualify lead, capture intake form, confirm payment, assign order ID, hand to Production |
| **Copy Production Agent** | Write copy to template, verify facts, check disclaimers, assign to QA |
| **QA Agent** | Fair Housing check, booster compliance, tone match, deliver or reject |
| **Delivery Agent** | Send final assets to client via agreed channel, archive in client folder |
| **Revise Agent** (if needed) | Apply one round of revision requested by client |

---

## 4. Order lifecycle

```
Intake → Fact-check → Draft → QA → Client review → Delivery → Archive
```

### 4.1 Intake (SLA: 2 hours Mon–Sat)
1. Receive intake form via order form or Stripe invoice webhook.
2. Verify order ID format: `RC-YEAR-####`.
3. Verify payment status:
   - Subscription active: proceed.
   - À la carte unpaid: pause, send payment link, do not assign.
4. Assign priority:
   - Rush: 90 minutes.
   - Standard: end-of-business.
5. Create client folder:
   ```
   /clients/<client_id>/<order_id>/
     ├── intake.json
     ├── draft.md
     ├── final.zip
     └── revision.log
   ```
6. Hand to Production with `ASSIGN_PRODUCTION(order_id)`.

### 4.2 Fact-check (SLA: 15 minutes)
1. Verify price, beds, baths, sqft against intake fields.
2. Cross-check neighborhood claims for accuracy.
3. Confirm required disclosure language attached to intake form.
4. If any field missing or inconsistent, return to Sales with a "needs info" flag.

### 4.3 Drafting (SLA: 30 minutes for standard; 15 minutes for rush)
Write in this order:
1. Opening line tied to the property's strongest emotional hook.
2. Body structured as: feature → benefit → proof. Avoid vague adjectives.
3. Neighborhood context (school quality, commute access, HOA, tax rate).
4. Call-to-action that does NOT repeat "schedule a showing" verbatim.

Platform-specific outputs:
- **MLS:** 250–350 words, minimal formatting, plain text.
- **Zillow / Realtor.com:** Custom description field; can be up to 1,000 chars, advantage taken.
- **Instagram:** Hook + 3 bullet assets + CTA + 5–7 hashtags.
- **Email:** Subject line (≤ 60 chars) + 2 short paragraphs + CTA.

### 4.4 QA checklist (SLA: 15 minutes)
- [ ] No pricing / factual errors
- [ ] Fair Housing: no protected class references (familial status, religion, race, etc.)
- [ ] State disclosure language included exactly as provided
- [ ] MLS system character limit not exceeded
- [ ] No banned superlatives per local MLS rules
- [ ] Voice calibration matches selected mode
- [ ] All requested platform outputs included

### 4.5 Delivery (SLA: 10 minutes per approved item)
- Deliver final + client revision instructions via agreed channel.
- If order is subscription, archive to `COMPLETED/` and confirm back to billing.
- If order is à la carte, send one-click "Approve & Release" button or reply-to-confirm flow.
- Attach a one-paragraph summary of changes if this is a revision.

### 4.6 Revision loop
- Each subscription listing: one complimentary revision.
- Rush / à la carte: one revision at no additional cost within 48 hours of first delivery.
- After one revision, further changes billed at $25/round.

---

## 5. Boilerplate registry
Every state requires specific disclosures and advertised brokerage language. Maintain a `boilerplates/` directory keyed by state.

Required fields for each state:
- Agency disclosure sentence
- Equal Housing logo requirement note (if any)
- Default disclaimer
- Broker name + license format

---

## 6. Quality standards
- Rejection rate target: < 5% of delivered listings require revision.
- Standard on-time rate: ≥ 95%.
- Rush on-time rate: ≥ 98%.
- Fair Housing incident rate: zero tolerance.
- Client satisfaction score target: ≥ 4.6/5 from post-delivery survey.

---

## 7. Escalation rules
- If reproduced facts cannot be verified within SLA, escalate to Sales to contact client immediately.
- If Fair Housing language is ambiguous, escalate to Operations lead.
- If client voice preference conflicts with platform rules (e.g., luxury voice vs. banned words), QA selects the compliant alternative and flags with rationale.

---

## 8. Reporting
Run weekly metrics from the archive:
- Orders completed per day
- Average delivery time by tier (standard vs. rush)
- Revision rate by voice mode
- Word count per property type
- Any compliance flags
