#!/usr/bin/env bash
# Auto-sync the workspace copy into the git clone and push to the designated remote.
# The git clone (with the push token) lives at $GIT_CLONE, defaulting to /tmp/gs.
# The remote is MIKEAA2020/general-sustainability @ main/agent 2 productivity illusion.
#
# Usage:  ./push_to_remote.sh ["commit message"]
set -euo pipefail

SRC="/home/user/agent 2 productivity illusion"
CLONE="${GIT_CLONE:-/tmp/gs}"
MSG="${1:-Auto-sync of scan_revision audit work (agent 2 productivity illusion)}"

if [ ! -d "$CLONE/.git" ]; then
  echo "ERROR: git clone not found at $CLONE (set GIT_CLONE). Cannot push." >&2
  exit 1
fi

# Copy workspace -> clone, excluding build/cache/generated junk.
tar -C "$SRC" \
  --exclude='__pycache__' --exclude='*.egg-info' --exclude='.pytest_cache' \
  --exclude='*.pyc' --exclude='.venv' --exclude='build' --exclude='dist' \
  --exclude='*.pdf' -cf - . | tar -C "$CLONE/agent 2 productivity illusion" -xf -

cd "$CLONE"
if [ -z "$(git status --porcelain -- 'agent 2 productivity illusion')" ]; then
  echo "No changes to push."
  exit 0
fi
git add "agent 2 productivity illusion"
git commit -q -m "$MSG"
git push origin main
echo "Pushed: $(git log --oneline -1)"
