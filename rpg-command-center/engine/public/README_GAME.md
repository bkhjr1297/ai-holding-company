# Revenue Rescue Desk — Command Center

## Quick Start

1. Make sure the real backend data is in place:
   - `/root/ai-holding-company/first-business-missed-call-recovery/data/florida_hvac_first_call_batch_150.csv`
   - `/root/ai-holding-company/businesses/appointment-setting/data/lead_batch_first_25.csv`
   - `/root/ai-holding-company/communications/templates/florida_hvac_initial_email.txt`

2. Start the backend:
   ```bash
   python3 /root/ai-holding-company/rpg-command-center/engine/backend_api.py
   ```

3. Open the game:
   ```bash
   firefox http://127.0.0.1:7457/frontend_index.html
   ```

## Real Actions in the Game

- `Generate Daily Batch` runs the real appointment-setting daily batch and updates leads/gold from real files
- `Collect Revenue` checks real revenue CSVs and tracks monthly streaks
- `Accept Quest` grants gold to simulate quest rewards
