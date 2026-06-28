#!/usr/bin/env bash
set -euo pipefail
if [ "$#" -lt 3 ]; then
  echo "Usage: $0 recipient@example.com 'Subject' /path/to/body.txt" >&2
  exit 2
fi
TO="$1"
SUBJECT="$2"
BODY_FILE="$3"
FROM="${REVENUE_RESCUE_FROM:-}"
if [ ! -f "$BODY_FILE" ]; then echo "Body file not found: $BODY_FILE" >&2; exit 2; fi
if ! command -v himalaya >/dev/null; then echo "himalaya not installed" >&2; exit 2; fi
TMP=$(mktemp)
{
  [ -n "$FROM" ] && echo "From: $FROM"
  echo "To: $TO"
  echo "Subject: $SUBJECT"
  echo
  cat "$BODY_FILE"
} > "$TMP"
cat "$TMP" | himalaya template send
rm -f "$TMP"
