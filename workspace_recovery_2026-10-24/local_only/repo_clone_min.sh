#!/usr/bin/env bash
# Minimal, budget-safe access to MIKEAA2020/general-sustainability (never clone the full repo: >10k files).
# Creates ./gs2 as a blob:none, depth-1, NO-CHECKOUT clone and fetches the tips of all branches (≈1 MB).
# NOTE: workspace snapshots drop .git/config, so re-run this script at the start of every new session.
#
#   source secrets/github_pat.env; bash repo_clone_min.sh
#   git -C gs2 ls-tree -r --name-only origin/<branch> | grep <pattern>          # list files (no blob download)
#   git -C gs2 show origin/<branch>:"<path>" > local_copy                        # fetch ONE file
#   To commit without checking anything out: git read-tree origin/<branch>; copy files in; git add <paths>; git commit; git push origin HEAD:<branch>
set -euo pipefail
: "${GITHUB_PAT:?set GITHUB_PAT (source secrets/github_pat.env)}"
URL="https://x-access-token:${GITHUB_PAT}@github.com/MIKEAA2020/general-sustainability.git"
rm -rf gs2
git clone --filter=blob:none --no-checkout --depth 1 --branch main "$URL" gs2 2>&1 | sed "s/${GITHUB_PAT}/<PAT>/g"
cd gs2
git config user.name "MIKEAA2020"
git config user.email "63320461+MIKEAA2020@users.noreply.github.com"
for b in $(git ls-remote --heads origin | awk '{print $2}' | sed 's|refs/heads/||'); do
  [ "$b" = main ] && continue
  git fetch -q --depth 1 origin "+refs/heads/$b:refs/remotes/origin/$b"
done
git branch -r
du -sh .git
