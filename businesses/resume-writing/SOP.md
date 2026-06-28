# SOP — AI Resume Writing Agency

## V1.0

### 1. Order Intake
1. Receive order via webhook (mock).
2. Store order in `orders/` directory with ID `ORD-YYYYMMDD-XXXX`.
3. Verify payment status: if unpaid, delay processing.

### 2. Triage & Assign
- Route by tier:
  - Starter → Junior Consultant (L1)
  - Professional → Senior Consultant (L2)
  - Executive → Principal Consultant (L3)

### 3. AI Drafting Pipeline
1. Ingest client resume + target job description.
2. Extract entities (skills, companies, education).
3. Run LLM rewrite prompt (see prompt library folder).
4. Generate scorecard: ATS compatibility, keyword density, readability.

### 4. Human Review
- L1/L2/L3 review based on tier.
- Check for hallucinated titles, dates, metrics.
- Apply branding / design layer if add-on ordered.

### 5. Delivery
1. Export to PDF (.docx fallback if requested).
2. Upload to client portal (s3 mock path).
3. Send notification (webhook stub).

### 6. Revision Loop
- Client requests revisions via form.
- Re-run token-budgeted rewrite on affected sections.
- Max 3 revisions for Starter/Pro; unlimited 7 days for Executive.

### 7. Quality Gates
- Every resume must pass:
  - ATS Score ≥ 85
  - No ai-slop phrases ("passionate about", "synergy", "think outside the box")
  - Consistent date formatting
  - Action-verb lead on every bullet
