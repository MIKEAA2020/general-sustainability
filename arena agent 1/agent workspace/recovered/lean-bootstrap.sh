#!/usr/bin/env bash
# Re-provision the Lean environment under /var/tmp (NOT persisted across turns).
# Usage:  source /home/user/lean-bootstrap.sh
# After this:  cd /var/tmp/lean/gs/lean && lake build
set -e

export ELAN_HOME=/var/tmp/lean/elan
export LAKE_HOME=/var/tmp/lean/elan/lake
export XDG_CACHE_HOME=/var/tmp/lean/xdgcache
mkdir -p /var/tmp/lean

# 1. elan (idempotent: skipped if the binary is already there)
if [ ! -x "$ELAN_HOME/bin/elan" ]; then
  echo "== installing elan =="
  curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \
    | sh -s -- -y --no-modify-path --default-toolchain none
fi
export PATH="$ELAN_HOME/bin:$PATH"

# 2. the repo (depth 1; the paper tree is only needed for reading)
if [ ! -d /var/tmp/lean/gs/.git ]; then
  n=$(ls /var/tmp/lean/gs/lean/Formalizations/*.lean 2>/dev/null | wc -l)
  if [ -f /var/tmp/lean/gs/lean/Formalizations.lean ] && [ "$n" -ge 20 ]; then
    echo "== reusing existing tree at /var/tmp/lean/gs ($n modules; no .git; push via API) =="
  else
    echo "== cloning general-sustainability @ lean-audit-v4 =="
    mkdir -p /var/tmp/lean/gs
    git -c advice.detachedHead=false clone --depth 1 --branch lean-audit-v4 \
        https://github.com/MIKEAA2020/general-sustainability.git /var/tmp/lean/gs
  fi
fi

# 3. toolchain pinned by the repo (dependency-free: no mathlib, so no cache get)
echo "== toolchain =="
cd /var/tmp/lean/gs/lean
cat lean-toolchain
lake --version

echo "== ready =="
