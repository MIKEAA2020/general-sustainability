#!/usr/bin/env bash
# Commit the E2 v3 (source-year) deposit.
#
# WHY THIS SCRIPT EXISTS. The repository checkout in the agent workspace is a
# PARTIAL one: 4,892 of the 5,981 blobs tracked in HEAD are absent from
# .git/objects, so `git commit` dies with
#
#   error: invalid object 100644 <sha> for '<path>'
#   error: Error building trees
#
# Git has to build a tree over every tracked file, and most of them are not
# here. Run this from a FULL clone (git clone, not the sparse/partial copy) and
# it will do exactly what was staged and ready in the workspace.
#
#   bash commit_e2_v3.sh /path/to/full/clone
#
# It is idempotent: it stages by path, so a re-run after copying files in is
# safe. It does NOT push -- no remote is configured in the workspace copy.
set -euo pipefail
REPO="${1:?usage: commit_e2_v3.sh <path-to-full-clone>}"
cd "$REPO"
MSG_FILE="$(dirname "$(readlink -f "$0")")/E2_V3_COMMIT_MESSAGE.txt"
[[ -f "$MSG_FILE" ]] || { echo "commit message file not found: $MSG_FILE" >&2; exit 1; }

git checkout -b e2-v3-source-year 2>/dev/null || git checkout e2-v3-source-year
git add \
  "arena agent 1/paper rewrites/figs_e2_v3/fig1_surplus.png" \
  "arena agent 1/paper rewrites/figs_e2_v3/fig2_kernel_vs_catch.png" \
  "arena agent 1/paper rewrites/figs_e2_v3/fig3_reactive_rules.png" \
  "arena agent 1/paper rewrites/figs_e2_v3/fig4_fprime.png" \
  "arena agent 1/paper rewrites/figs_e2_v3/fig5_replay.png" \
  "arena agent 1/paper rewrites/figs_e2_v3/fig6_k_sensitivity.png" \
  "arena agent 1/paper rewrites/figs_e2_v3/fig7_stochastic.png" \
  "arena agent 1/paper rewrites/latex/E2_v3_SOURCE_YEAR_REMEDIATION_REPORT.md" \
  "arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v29.pdf" \
  "arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v29.tex" \
  "arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v29_basis_audit.py" \
  "arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v29_sabotage.py" \
  "arena agent 1/paper rewrites/latex/paperE2_cod_intervention_v29_verification.py" \
  "wave_e_cod/results/e2_families_v3.csv" \
  "wave_e_cod/results/intervention_boundaries_v3.csv" \
  "wave_e_cod/results/intervention_results_v3.json" \
  "wave_e_cod/src/campaign_e2_allee_declared_v3.py" \
  "wave_e_cod/src/campaign_e2_depensation_v3.py" \
  "wave_e_cod/src/campaign_e2_elevation_v3.py" \
  "wave_e_cod/src/campaign_e2_fox_form_v3.py" \
  "wave_e_cod/src/figs_e2_v3/fig1_surplus.png" \
  "wave_e_cod/src/figs_e2_v3/fig2_kernel_vs_catch.png" \
  "wave_e_cod/src/figs_e2_v3/fig3_reactive_rules.png" \
  "wave_e_cod/src/figs_e2_v3/fig4_fprime.png" \
  "wave_e_cod/src/figs_e2_v3/fig5_replay.png" \
  "wave_e_cod/src/figs_e2_v3/fig6_k_sensitivity.png" \
  "wave_e_cod/src/figs_e2_v3/fig7_stochastic.png" \
  "wave_e_cod/src/figures_v3/fig1_surplus.png" \
  "wave_e_cod/src/figures_v3/fig2_kernel_vs_catch.png" \
  "wave_e_cod/src/figures_v3/fig3_replay.png" \
  "wave_e_cod/src/figures_v3/fig4_fprime.png" \
  "wave_e_cod/src/figures_v3/fig5_stochastic_constructive.png" \
  "wave_e_cod/src/figures_v3/fig6_k_sensitivity.png" \
  "wave_e_cod/src/make_figs_v17.py" \
  "wave_e_cod/src/results_forms_v3/campaign_e2_depensation_v3.csv" \
  "wave_e_cod/src/results_forms_v3/campaign_e2_depensation_v3.txt" \
  "wave_e_cod/src/results_forms_v3/e2_allee_rows_v3.csv" \
  "wave_e_cod/src/results_forms_v3/e2_allee_rows_v3.json" \
  "wave_e_cod/src/results_forms_v3/e2_fox_form_v3.csv" \
  "wave_e_cod/src/results_forms_v3/e2_fox_kernels_v3.csv" \
  "wave_e_cod/src/results_srcyear_v3/e2_elevation_bootstrap.csv" \
  "wave_e_cod/src/results_srcyear_v3/e2_elevation_finite_floors.csv" \
  "wave_e_cod/src/results_srcyear_v3/e2_elevation_k_grid.csv" \
  "wave_e_cod/src/results_srcyear_v3/e2_elevation_residuals.csv" \
  "wave_e_cod/src/results_srcyear_v3/e2_elevation_stochastic.csv" \
  "wave_e_cod/src/results_srcyear_v3/e2_elevation_stochastic_constructive.csv" \
  "wave_e_cod/src/run_families_v3.py" \
  "wave_e_cod/src/run_intervention_v3.py" \
  "wave_e_cod/src/superseded_v2/README.md" \
  "wave_e_cod/src/superseded_v2/e2_families_v2.csv" \
  "wave_e_cod/src/superseded_v2/run_families_v2.py" \

# sanity: nothing tracked may be staged as deleted
if git diff --cached --name-status | grep -q '^D'; then
  echo "REFUSING: the staging area deletes tracked files. Check the clone." >&2
  git diff --cached --name-status | grep '^D' >&2
  exit 1
fi
git commit -F "$MSG_FILE"
git --no-pager log --stat --oneline -1 | tail -5
echo
echo "Committed on branch e2-v3-source-year. Not pushed (no remote configured)."
