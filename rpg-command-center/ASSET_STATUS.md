# RPG Asset Status — Revenue Rescue Desk

## Verified Available Locally

### pixel-agents repo
- Cloned to: `/root/ai-holding-company/rpg-command-center/engine/pixel-agents`
- Agent sprites: 6 character PNGs
- Office assets: desk, chair, plant, whiteboard, bookshelf, shelf, TV, sofa, table, PC, clock, cactus, coffee, bin/pot/painting variants
- Floors: 9 floor PNGs
- Walls: 1 wall PNG
- Layout template: `default-layout-1.json`
- Note: this is the TypeScript source repo, not a built runtime. To use it, you need Node installed and then run `npm install && npm run build` in that folder.

## Not Yet Installed Locally

### Farm RPG assets
- Itch.io source: https://maevedevs.itch.io/farm-rpg
- License: free to use in commercial projects; do not resell/redistribute as-is
- Free sample file listed on page: `Farm RPG FREE 16x16 - Tiny Asset Pack.rar` (~44 KB)
- Paid full pack: `Farm RPG - Tiny Asset Pack - (All in One).rar` (~10 MB)
- Download check: the itch page shows the files, but a direct automated download URL was not found in page HTML. The download likely requires a purchase/free download action on itch.io first.

## What Is Ready Now
- RPG design doc and backend API stub
- pixel-agents office asset structure in repo
- Farm RPG integration design pending assets

## What Needs To Happen Next
1. Build/run the pixel-agents backend if you want the animated office view.
2. Get the Farm RPG asset pack from itch.io and attach a download or upload path.
3. Update the game frontend to point to that asset path.
