#!/bin/bash
set -euo pipefail

BASE=/root/ai-holding-company
TRIBE="${BASE}/tribe"
CASHCLAW=/root/cashclaw

echo "=== Unified Finance & Work Loop ==="
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# 1. Health + safeguards
echo "[1/7] Health + safeguards..."
python3 "${TRIBE}/calc/safeguards.py" || true
python3 "${TRIBE}/calc/health_safeguards.py" || true

# 2. Location / crisis checks
echo
echo "[2/7] Location and crisis readiness..."
python3 "${TRIBE}/calc/location_router.py" 40.7128 -74.006 || true
python3 "${TRIBE}/calc/crisis_response.py" "check only" "system" || true

# 3. Balances
echo
echo "[3/7] Checking balances..."
echo "--- CashClaw wallet ---"
mltl wallet show || true
echo "--- AgentCash ---"
agentcash balance || true
echo "--- AgentCash accounts ---"
agentcash accounts || true

# 4. Stage requirements
echo
echo "[4/7] Current stage requirements..."
if [ -f "${TRIBE}/calc/stage_schedule.json" ]; then
  cat "${TRIBE}/calc/stage_schedule.json"
else
  echo "No stage schedule found"
fi

# 5. Marketplace / discovery
echo
echo "[5/7] CashClaw inbox / discovery..."
mltl inbox || true
agentcash discover https://stableenrich.dev || true

# 6. Ledger / receipts
echo
echo "[6/7] Tribe ledger..."
tail -n 5 "${TRIBE}/logs/ledger.jsonl" 2>/dev/null || true
echo
echo "Latest receipts..."
ls -t "${BASE}/receipts/brian"/*.* 2>/dev/null | head -3 || echo "No receipts yet"

# 7. MCP / services
echo
echo "[7/7] Service stack..."
BASE="${BASE:-/root/ai-holding-company}"
for m in doordash lyft uber instacart rideshare; do
  dist="${BASE}/mcps/${m}/dist/index.js"
  if [ -f "$dist" ]; then
    echo "[OK] ${m}"
  else
    echo "[MISSING] ${m}: no dist/index.js"
  fi
done

echo
echo "=== Loop complete ==="
