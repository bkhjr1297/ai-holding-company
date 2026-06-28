# RPG Tile Interpretation — 5-Tile Vertical Command Tower

## Source
User-provided pixel art: 5 identical square tiles stacked vertically on solid black background.

## Visual Breakdown
- Tile 1 (top): lime green textured border, white center cutout
- Tile 2: white tile, thin black border, white center cutout
- Tile 3: orange/terracotta textured border, white center cutout
- Tile 4: same as Tile 3 (orange, textured)
- Tile 5 (bottom): same as Tile 1 (lime green, textured)

All tiles share:
- Identical square shape and size
- Identical centered square white hole/cutout
- Black mask blocks covering corners and mid-left/mid-right edges

## Game Mapping
| Tile | Color | Game Meaning |
|---|---|---|
| 1 (top) | Green | Roof / antenna / growth |
| 2 | White | Bright command level / main UI floor |
| 3 | Orange | Fulfillment/operations floor |
| 4 | Orange | Revenue/cash floor |
| 5 (bottom) | Green | Foundation / growth base |

Center white hole on each tile = agent slot / window / interactive point where agents appear or user clicks.

## How This Shapes the Command Center
- The base building is a 5-floor tower.
- Each floor is one tile from this strip.
- Top and bottom floors are “growth” floors (green).
- Middle three floors are white/orange operations layers.
- Agents occupy the center windows.
- Clicking a tile/floor opens that floor’s business module.

## Frontend Spec
- Tower rendered as 5 stacked square tiles.
- Repeat the user’s exact color/mask pattern.
- Center cutout is clickable and shows agent status.
- Scrolling or clicking changes floors.
- Each floor corresponds to a real business module:

| Floor | Business Module | Backend File |
|---|---|---|
| 1 (top) | Agent Barracks | `/businesses/*/agent_roster/agents.json` |
| 2 | Outreach / Campaigns | `/businesses/*/data/daily_batch_*.csv` |
| 3 | Fulfillment / Ops | `/automation/daily_ops/*.py` |
| 4 | Revenue / Cash | `/businesses/*/data/revenue.csv` |
| 5 (bottom) | Foundation / Clients | `/communications/logs/*.csv` |

## Asset Path
- Design reference: `/root/ai-holding-company/rpg-command-center/assets/user-submitted/img_52da852ac558.png`
- Game sprite implementation will redraw this pattern using the pixel-agents and Farm RPG tile sets.
