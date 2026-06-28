# Client Request Blueprint
## Mapping specific SMB requests to agent roles and delivered outcomes

| Client Request | Matched Role(s) | Primary Outcome | Typical Workflow |
|---|---|---|---|
| **"New leads aren't getting replied to fast enough."** | intake_coordinator, automation_architect, integration_builder, ai_behaviors_designer, qa_automation_tester | Faster lead response workflow with routing rules | intake_coordinator collects source, channels, SLA -> automation_architect designs webhook-to-notification flow -> integration_builder wires apps -> ai_behaviors_designer drafts reply templates/classification -> qa_automation_tester validates happy path, spam, overflow |
| **"I want AI support handling inbound messages."** | automation_architect, ai_behaviors_designer, copywriter, integration_builder, qa_automation_tester | Deflected tickets and consistent branded replies | automation_architect maps ticket schema -> ai_behaviors_designer builds intent classifier/escalation rules -> copywriter writes tone-aligned reply templates -> integration_builder connects helpdesk -> qa_automation_tester checks ignores, fallbacks, handoff rules |
| **"Build an automated email/SMS nurture sequence."** | campaign_runner, copywriter, ai_behaviors_designer, integration_builder | Scheduled triggered sequences with personalized copy | campaign_runner maps triggers and delays -> copywriter writes copy variants -> ai_behaviors_designer adds dynamic fields/short-circuit conditions -> integration_builder connects ESP / CRM |
| **"Automate appointment confirmations and reminders."** | automation_architect, integration_builder, campaign_runner, qa_automation_tester | No-shows reduced via confirmation + reminder flows | automation_architect defines trigger events -> integration_builder connects calendar/scheduling tool -> campaign_runner builds message cadence -> qa_automation_tester validates reschedules/cancellations/duplicate sends |
| **"We need lead scraping and enrichment."** | outbound_growth_operator, automation_architect, qa_automation_tester | Targeted lead list with verified fields and outreach plan | outbound_growth_operator defines ideal targets -> automation_architect designs source checks + enrichment pipeline -> qa_automation_tester audits accuracy, duplicates, opt-out handling |
| **"Our CRM is a mess; clean it and auto-update fields."** | automation_architect, integration_builder, qa_automation_tester | Cleaned, deduped CRM with reliable sync rules | automation_architect defines normalization rules -> integration_builder creates write-back workflows -> qa_automation_tester validates field mappings, retries, rollback behavior |
| **"Create a daily/weekly report automatically."** | automation_architect, integration_builder, qa_automation_tester | Scheduled reports with consistent metrics and distribution | automation_architect chooses data sources/metrics -> integration_builder schedules extraction and distribution -> qa_automation_tester validates formatting, timezones, missing data |
| **"Add AI chatbot to website and Slack."** | ai_behaviors_designer, copywriter, integration_builder, automation_architect, support_guardian | Always-on assistant that routes accurately and escalates safely | ai_behaviors_designer authorizes scope/guardrails -> copywriter crafts tone -> integration_builder connects channels -> automation_architect defines fallback/escalation paths -> support_guardian owns monitoring/SLA |

## Intake intake form fields
- Existing tools and data sources
- Target outcome and success metric
- Preferred schedule/cadence
- Tone/brand constraints
- Budget/retainer ceiling
- Escalation contact and hours

## Handoff contract
`intake_coordinator` produces intake.json -> `operations_owner` schedules kickoff -> architect assigns builder -> QA signs off -> `operations_owner` schedules 30/60/90 review with `finance_pricing_controller` if usage or scope drift.

## Expansion triggers
- Client asks for a second automation in the same stack
- Client asks for analytics/reporting layer
- Client asks to move from build-only to managed
- Client refers peer company in same workflow category
