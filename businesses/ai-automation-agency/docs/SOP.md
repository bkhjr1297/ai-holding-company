# SOP: AI Automation Delivery
Version: 1.0  
Owner: Operations  
Audience: Intake → Architecture → Build → QA → Launch → Handoff

---

## 1. Purpose
Deliver automated workflows that reduce manual work, prevent dropped tasks, and keep the client in control. We ship only no-side-effect automations unless the client explicitly authorizes outbound contact, writing, or publishing.

## 2. Scope
Every automation engagement — discovery, build, launch, review, and retainer.

## 3. Roles
| Role | Responsibility |
|------|----------------|
| Intake Coordinator | Qualify lead, collect intake fields, propose package, create order record |
| Automation Architect | Design workflow map, toolchain, access plan, and runbook |
| Integration Builder | Build and test workflow integrations |
| AI Behaviors Designer | Write prompts, intents, escalation rules, tone guards |
| Copywriter | Draft customer-facing messages for the automation |
| Campaign Runner | Build scheduled sequences and triggered campaigns |
| QA Automation Tester | Test happy path, edge cases, failures, and validate acceptance criteria |
| Operations Owner | Manage schedule, handoffs, reporting, and client communication |
| Finance Pricing Controller | Estimate resource usage, align quoting/retainer, watch usage creep |
| Support Guardian | Monitor reliability, SLA/uptime, and triage incidents |

## 4. Order lifecycle
```
Intake → Discovery → Architecture → Build → QA → Demo → Handoff → Retainer Review
```

### 4.1 Intake (SLA: 4 business hours)
1. Receive intake via intake form or referral.
2. Confirm three truth tests:
   - Outcome clarity: one measurable goal.
   - Tool access: who owns credentials and permissions.
   - Scope boundary: what is explicitly not included.
3. Assign order ID and status.
4. Route to delivery planning.

### 4.2 Discovery (SLA: 1–2 business days)
1. Map current state:
   - existing tools, channels, data formats, and handoffs
   - failure modes and exceptions
2. Map desired state:
   - triggers, actions, success metrics, and fallback rules
3. Produce a short blueprint with success metrics, risks, and rollout order.

### 4.3 Architecture (SLA: 1–2 business days)
1. Choose low-risk, maintainable toolchain.
2. Define:
   - auth model and access controls
   - trigger source and payload
   - action chain and branching rules
   - error handling and retries
   - logging and audit fields
3. Document data handling rules:
   - PII fields and retention
   - opt-out behavior
   - escalation contact

### 4.4 Build (SLA: 3–10 business days depending on package)
Build in this order:
1. Core logic and integration paths.
2. Customer-facing content and guardrails.
3. Scheduling, routing, and fallback logic.
4. Minimal logging and observability hooks.
5. One-click pause/kill switch.

### 4.5 QA checklist (SLA: 2 business days)
- [ ] Trigger fires under intended conditions
- [ ] Action completes within expected latency
- [ ] Edge cases handled: empty input, invalid format, missing field, timeout, auth failure
- [ ] No duplicate sends or unintended repeats
- [ ] Fallback/escalation path works
- [ ] Logs contain enough context to debug
- [ ] No unauthorized third-party sends or data sharing
- [ ] Opt-out/unsubscribe behavior works
- [ ] Performance acceptable under reasonable load

### 4.6 Demo and launch
1. Record a 5–7 minute demo in the client environment.
2. Provide a short runbook with:
   - what to change if inputs change
   - how to pause the automation
   - how to read logs
3. Launch with monitoring window for 48–72 hours.

### 4.7 Handoff
1. Deliver:
   - blueprint diagram
   - runbook
   - prompt/rules pack where applicable
   - success metrics baseline
2. Schedule 30/60/90 day retainer review.

### 4.8 Retainer review
- Check on automation health, usage patterns, and failure rate.
- Recommend optimizations priced as add-ons.
- Adjust monitoring or coverage as client needs change.

## 5. Quality standards
- On-time rate: ≥ 90% for standard; ≥ 95% for rush
- QA sign-off required before launch
- Zero unauthorized outbound sends
- Zero data leakage to unapproved services
- Client satisfaction target: ≥ 4.5/5 after handoff

## 6. Escalation rules
- Missing credentials or permissions: escalate to client within 2 hours.
- Ambiguous client requirements: pause build and clarify before test.
- Tool outage or rate limit: notify client and propose workaround.
- Data exception or compliance flag: stop affected path immediately.

## 7. Reporting metrics
- Orders per week and package mix
- Average delivery time by package
- QA rejection rate and cause categories
- Automation uptime in first 30 days after launch
- Support incidents and resolution time during monitoring window

## 8. No-side-effect rules
- Do not send emails, SMS, or social posts outside the agreed scope.
- Do not write to client CRM, calendar, or other production systems without explicit test approval.
- Do not store payment card or health data.
- Do not modify existing client automations without a written change request.
