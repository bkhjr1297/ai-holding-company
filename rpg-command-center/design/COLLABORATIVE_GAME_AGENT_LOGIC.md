# Collaborative Game + Agent Logic Workflow

Brian works periodically throughout the night on game logic, agent logic, and how the RPG world maps to real AI/business operations. Treat Brian's overnight inputs as the source of truth for game behavior.

## Operating Rule

Do not overwrite Brian's intended logic with generic dashboard assumptions. The Agent Farm must evolve as a collaborative operating system:

- Brian defines how the world should feel and how interactions should work.
- Hermes/RPG Build Agent turns that into working code, assets, state, and backend actions.
- Business Research Agent turns discovered businesses into in-game quests, buildings, and workers.
- Every spawned agent becomes an in-game NPC with name, role, task, personality, and status.

## Interaction Model

The game should work like a Stardew-style farm RPG:

1. Brian moves around the farm/world.
2. Workers visible in the world are real AI agents.
3. Brian approaches/clicks/presses Space on an agent.
4. A dialog/status window opens.
5. Brian can ask what the agent is doing, give feedback, or redirect work.
6. The agent response reflects its Agency Agents persona.
7. Important interactions create backend events, task logs, or real safe actions.
8. Real backend work updates the game state and NPC status.

## Game-to-AI Mapping

| In-game action | Backend/AI meaning |
|---|---|
| Talk to worker | Ask/redirect an AI agent |
| Visit bank | Review model spend, revenue, cash, and cost controls |
| Visit market | Evaluate tools/assets/business opportunities before spending |
| Visit research hut | Ask Business Research Agent for new opportunities |
| Visit outreach office | Prepare safe outreach assets; no sending without valid channel and permission |
| Visit workshop | Build websites, automations, SOPs, or fulfillment systems |
| Complete quest | Mark a real task/business milestone complete |
| Spawn worker | Register new AI agent as an NPC in `game_state.json` |

## Overnight Build Priority

When Brian is not actively steering, improve one safe subsystem at a time:

1. Stable movement/collision/camera.
2. More convincing farm/pixel-art assets.
3. Agent NPC placement and persona dialogs.
4. Action-to-backend event logging.
5. Business/research quests visible in game.
6. Buildings that correspond to real company functions.
7. Tests and verification.

## Safety

- No unauthorized email/calls/outreach.
- No paid tools or purchases.
- No fake business claims.
- No overwriting Brian's logic notes; append/update with timestamps instead.
