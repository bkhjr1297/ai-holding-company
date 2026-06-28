set -euo pipefail

APIBASE_MCP_CMD="apibase-mcp"
PINCH_CMD="pinch"
AGENTCASH_CMD="agentcash"
APIBASE_URL="https://apibase.pro/mcp"
CONFIG_DIR="$HOME/.ai-holding"
AGENTCASH_DIR="$HOME/.agentcash"
PINCH_DIR="$HOME/.pinch"

echo "[stabilize-tools] checking requirements"

# 1. ensure apibase environment/config
if [ ! -d "$CONFIG_DIR" ]; then
  mkdir -p "$CONFIG_DIR"
fi
if ! grep -q "APIBASE_MCP_URL" "$CONFIG_DIR/.env" 2>/dev/null; then
  {
    echo "APIBASE_MCP_URL=${APIBASE_URL}"
    echo "APIBASE_API_KEY="
  } >> "$CONFIG_DIR/.env"
fi

# 2. ensure agentcash wallet
if [ ! -d "$AGENTCASH_DIR" ]; then
  mkdir -p "$AGENTCASH_DIR"
fi
$AGENTCASH_CMD balance || true

# 3. ensure pinch wallet skeleton for agent 'hermes'
AGENT_NAME="hermes"
WALLET_DIR="$PINCH_DIR/wallets/$AGENT_NAME"
if [ ! -d "$WALLET_DIR" ]; then
  $PINCH_CMD create --agent="$AGENT_NAME" --provider=coinbase --limit=100 || true
fi

# 4. smoke tests
echo "[stabilize-tools] smoke tests"
$APIBASE_MCP_CMD --help >/dev/null 2>&1 || echo "[stabilize-tools] apibase-mcp help failed"
$PINCH_CMD --help >/dev/null 2>&1 || echo "[stabilize-tools] pinch help failed"
$AGENTCASH_CMD --help >/dev/null 2>&1 || echo "[stabilize-tools] agentcash help failed"

echo "[stabilize-tools] complete"
