# How To Run The RPG Command Center

Backend server entrypoint: `/root/ai-holding-company/rpg-command-center/engine/backend_api.py`

Start the backend in one shot:
```bash
/root/ai-holding-company/rpg-command-center/engine/backend_api.py
```

It serves:
- Backend API: `http://127.0.0.1:7457/api/health`
- Game state: `http://127.0.0.1:7457/api/state`
- Frontend UI: `http://127.0.0.1:7457/frontend_index.html`

This path is the source of truth for running the RPG command center; do not add extra startup steps that aren’t here.
