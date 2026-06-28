# RPG Command Center — Playable Prototype

## How To Play Right Now

Run this inside `/root/ai-holding-company/rpg-command-center/engine`:

1. Open `frontend_index.html` in a browser
2. Click "Run Daily Batch" — frontend is wired to backend logic
3. Watch your base, agents, and campaign screen

## Files

- `frontend_index.html` — main game screen
- `style.css` — dark theme
- `game.js` — frontend actions
- `backend_api.py` — backend data hook stub

## Real Backend Data
The game reads from the real business data folders:
- `/root/ai-holding-company/businesses/*/data/daily_batch_*.csv`
- `/root/ai-holding-company/businesses/*/data/revenue.csv`
- `/root/ai-holding-company/businesses/*/agent_roster/agents.json`

## Adding Itch.io Assets
Put sprites and tiles in:
- `/root/ai-holding-company/rpg-command-center/assets/`
Then update `style.css` and `game.js` to use them.

## Next Game Features To Build
1. Replace buttons with animated sprites
2. Add campaign map tiles from itch.io
3. Add agent movement animations
4. Add notifications when real revenue is recorded
5. Add clan hall revenue meters
