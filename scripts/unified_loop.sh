#!/bin/bash
set -euo pipefail

BASE=/root/ai-holding-company
TRIBE="${BASE}/tribe"
CASHCLAW=/root/cashclaw

echo "=== Unified Finance & Work Loop ==="
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# 1. Check balances
echo "[1/6] Checking balances..."
echo "--- CashClaw wallet ---"
mltl wallet show
echo "--- AgentCash ---"
agentcash balance || true
echo "--- AgentCash accounts ---"
agentcash accounts || true

# 2. Show current stage requirements
echo
echo "[2/6] Current stage requirements..."
if [ -f "${TRIBE}/calc/stage_schedule.json" ]; then
  cat "${TRIBE}/calc/stage_schedule.json"
else
  echo "No stage schedule found; run stage_budget.py first"
fi

# 3. Marketplace inbox
echo
echo "[3/6] CashClaw inbox..."
mltl inbox || true

# 4. AgentCash status (optional discovery)
echo
echo "[4/6] AgentCash discovery..."
agentcash discover https://stableenrich.dev || true

# 5. Tribal fund ledger
echo
echo "[5/6] Latest ledger events..."
tail -n 5 "${TRIBE}/logs/ledger.jsonl" 2>/dev/null || true
echo
echo "Latest receipts..."
ls -t "${BASE}/receipts"/brian/*.json 2>/dev/null | head -3 || echo "No receipts yet"

# 6. Operability check
echo
echo "[6/6] Operability check..."
MLTL_BALANCE=$(mltl wallet show 2>/dev/null | grep -oE '[0-9]+\.[0-9]+' | head -1 || echo "0")
echo "CashClaw ETH balance: ${MLTL_BALANCE}"
if (( $(echo "$MLTL_BALANCE > 0" | bc -l 2>/dev/null || echo 0) )); then
    echo "STATUS: OPERATIONAL — registration and marketplace tasks available"
else
    echo "STATUS: PENDING FUNDING — send 0.0001-0.001 ETH on Base to $(mltl wallet show | grep Address | awk '{print $2}')"
fi

echo
echo "=== Loop complete ==="
