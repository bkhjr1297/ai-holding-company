# Agency Agents Workforce Activations
## Real Estate Listing Copy

1. **Intake Agent** — validate form fields, create client folder:
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
