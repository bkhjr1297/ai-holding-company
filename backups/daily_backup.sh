#!/bin/bash
set -euo pipefail
REPO_DIR="/root/ai-holding-company"
BACKUP_LOG="/root/ai-holding-company/backups/backup.log"
BACKUP_LOG_DIR="$(dirname "$BACKUP_LOG")"
mkdir -p "$BACKUP_LOG_DIR"
cd "$REPO_DIR"
{
  echo "=== Backup started at $(date -u +"%Y-%m-%dT%H:%M:%SZ") ==="
  git add -A
  git diff --cached --quiet && echo "No changes to commit" || git commit -m "Daily backup: $(date -u +%Y-%m-%d)"
  REMOTE_URL="$(git remote get-url origin 2>/dev/null || true)"
  if [ -n "$REMOTE_URL" ]; then
    git push -u origin master
    echo "Push completed"
  else
    echo "No remote configured; skipping push"
  fi
} >> "$BACKUP_LOG" 2>&1
