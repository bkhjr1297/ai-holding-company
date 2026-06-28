# Launch Kit — AI Resume Writing Agency

Complete startup package for the AI Resume Writing agency, part of the AI Holding Company.

## Structure

```
.
├── pricing.md               # Pricing tiers and upsells
├── website-copy.md          # Landing pages, hero, FAQ, social proof
├── order-form.md            # Client intake + internal order record
├── SOP.md                   # Standard Operating Procedures v1
├── automation-script-stub.py # Worker pipeline (mock execution)
├── lead-sources.md          # Paid, organic, partnership, outbound
└── templates/
    ├── ats-optimized-resume.md  # ATS-safe resume template
    └── cover-letter.md          # Cover letter structure
```

## How to Use

1. Read `SOP.md` for the operational playbook.
2. Use `pricing.md` for Stripe / CMS pricing setup.
3. Insert `website-copy.md` into the site generator.
4. Wire `order-form.md` fields into your order intake.
5. Run `python automation-script-stub.py` to validate the pipeline (mock mode).
6. Deploy `lead-sources.md` to your growth team for immediate execution.

## Notes
- No side effects in the automation stub; it only prints.
- All templates are Markdown for easy conversion to DOCX/HTML.
- Persona: Agency Agents workforce style (captions, doc-r, processed, monitored).
