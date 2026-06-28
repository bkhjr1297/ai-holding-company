# RPG Command Center — Revenue Rescue Desk

## Concept
A Clash of Clans-style web dashboard where every user action triggers real business operations.
Built with free/open-source tools, playable in browser, and always synced to backend data.

## Core Loop
1. User taps "Send Outreach" in the game.
2. Game triggers real email batch generation and log update on the backend.
3. Game shows animated troops = business agents.
4. User collects resources = real leads, appointments, revenue.

## Game Screens
- Base view: portfolio businesses as upgradable buildings
- Campaign map: lead lists as attack waves
- Agent barracks: Agency Agents roster
- Clan hall: dashboard with revenue, leads, clients
- Workshop: upgrade tools when thresholds met
- Settings: connect email, phone, CRM

## Backend Mapping
- Outreach batch -> /businesses/*/data/daily_batch_*.csv
- Revenue -> /businesses/*/data/revenue.csv
- Agents -> /businesses/*/agent_roster/agents.json
- Daily ops -> /automation/daily_ops/*.py
- Reports -> /communications/reports/*.txt

## Tech Stack
- Frontend: HTML + CSS + JS (served by Open Design daemon or static server)
- Backend: Python scripts already in place
- Assets: Farm RPG assets + pixel-agents repo
- Hosting: local or free static host

## Monetization
- Not a game you sell.
- You play the game to manage real businesses.
- Fun visual layer over real operations.

## Next Steps
1. Finalize game map and sprite style from itch.io assets
2. Build frontend skeleton
3. Wire frontend buttons to backend scripts
4. Add revenue threshold events
5. Add portfolio view when multiple businesses launch
