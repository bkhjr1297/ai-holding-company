# Tribe Coordination System

Implements the Federated Tribe Blueprint rules extracted from the PDF.

## Structure
- 5 wife slots across 4 phases
- Separate space philosophy until merge
- Rent pooling + tribe fund
- Weekly tribe dinners
- Sleeping rotation
- Conflict / rules system
- Money requests tracked and logged

## Data
- `/root/ai-holding-company/tribe/state/` - role and phase status
- `/root/ai-holding-company/tribe/inbox/` - requests and messages
- `/root/ai-holding-company/tribe/logs/` - conflict, rotation, payout logs

## Retirement
- `/root/ai-holding-company/tribe/state/retirement.json` - per-member retirement accounts
- `/root/ai-holding-company/tribe/calc/retirement.py` - contributions, rebalancing, withdrawals, growth simulation
- Rules:
  - Retirement age: 65
  - Contribution range: 5-15% of eligible income
  - Investments: conservative / moderate / aggressive profiles
  - Early withdrawals penalized at 10%
  - Locked until retirement status triggers
