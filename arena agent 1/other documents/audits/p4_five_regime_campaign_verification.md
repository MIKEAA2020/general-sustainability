# P4 five-regime campaign — independent verification memo (2026-09-02)

**Object.** The committed five-regime continuation campaign
(`research_program/validated_computations/p4_five_regime_campaign/`, commits `295d4f4`
execution + `9a26c7e` pre-registration, both 2026-09-02 UTC), downloaded verbatim to
`repo_assets_mirror/p4_five_regime_campaign/` (18 files, sizes byte-identical to the
GitHub content API) and verified here against its own report and against the paper
numbers. This memo is an *independent* check of the committed records; it is not the
independent rerun, which remains a first-run-status open item (the execution report
says the same).

## 1. Internal consistency of the committed archives (independent re-read)

- `p4_branch_archive.csv` = 148 records = 47 small_lower + 55 large_lower + 46
  small_upper + 0 large_upper + 2 honest-failure rows for the upper captured family —
  matches the report's "148 records (47/55/46/0 converged + 2 recorded failures)".
- Multipliers re-read from the CSVs reproduce the report's comparison values:
  large arm μ = 0.2040 at τ = 4.0; 0.9692 at 5.5815; small arm 1.0192 at 5.584;
  0.9942 at 5.587. μ imaginary parts zero (≤1e-16) at every record; μ₁ real at every
  record — the "real at every point" claim checks.
- Coexisting cycles at τ = 5.575: amplitudes 24.91 (large) and 19.94 (small), periods
  322.60 and 308.16 — the separation criterion MATCHES with gaps 4.98 / 14.45.
- Gate-floor facts reproduced: on the large arm near τ = 5.55, E_max ≤ 9.21
  (reported ≤ 9.2) and N_min ≥ 68.6 (reported ≥ 68.7) — the §9.2 no-gate-singularity
  sentence survives on the committed records.
- Basin archive: 81 dt=0.02 runs (27 τ × 3 histories) + 6 dt=0.01 halving runs;
  classifications 40 settles / 30 captured / 17 intermediate; dt-halving at 5.575 and
  148.3 UNCHANGED — matches the report. The 5.575 asymmetry is committed as
  H1 settles / H2 captured / H3 settles (the reverse of the inherited qualitative
  claim).
- Boundary table re-read from `p4_campaign_results.json`: Hopf brackets
  [3.6661490142739, 3.6661490142743] / [150.3584773101408, 150.3584773101421]
  (inherited interval certificates); lower fold [5.587236198663, 5.587236198690]
  (three-order MS, agreement 2.69e-11) with Krawczyk box [5.587236198689, ...691]
  (commit `9a26c7e`); capture onset [148.6, 149.5] (basin grid); interior
  monostability = finite search, six interior grid τ values, all three histories
  settle.

## 2. Consequence for the paper (executed this turn)

P4 v10 built (v9 untouched): the §9.2 lower boundary is rewritten to the single
Krawczyk-certified fold τ_f = 5.5872362 of one S-shaped branch (two arms, one fold);
the inherited two-fold reading is quoted, labelled inherited/exploratory, and
superseded where the records disagree; the five-regime boundary labels become
τ_- / τ_f / [148.6, 149.5] / τ_+; the lower-window basin asymmetry is the committed
reversal (depleted captured); the upper boundary paragraph is replaced by the basin
grid bracket + the two honest collocation failures of the E≈Emax face cycle + the
NOT-TESTED status of the inherited "interior large family"; the M3-B register,
the certification-hierarchy paragraph, the early-warning discussion, and the
conclusion are updated. New figure: `figs_p4/fig2_five_regime_topology.png`
(+ script), four panels, drawn ONLY from the committed CSVs/JSON; no inherited
number is drawn. Abstract rebalanced to ≤250 words (240). Data-availability section
now names the deposit locations.

**Comparison verdicts carried into v10 verbatim (5 MATCH / 6 MISMATCH /
1 NOT-TESTED)** — the mismatch list is the paper's honest supersession record:
large-branch multiplier at 4.0 (0.2040 vs 0.240); small-arm multiplier at 5.584
(1.0192 vs 1.0514); the lower-boundary bracket (5.5872362 vs [5.574, 5.576]);
the upper-boundary bracket ([148.6, 149.5] vs [148.125, 148.438]); the H1/H2 basin
asymmetry (REVERSED at 5.575); the basin-grid agreement (53/81). NOT-TESTED: the
interior large family's amplitude window (independence discipline forbids seeding
from inherited numbers).

## 3. What remains open after the campaign (unchanged statuses)

- Independent rerun of the campaign (first-run status) — registry.
- The upper captured family's collocation record (Fourier resolution blocked at
  m=64/128; honestly recorded) — registry.
- The continuum off-grid residual stage of the fold certificate (lost; the rebuilt
  Krawczyk stage certifies the discrete m=64 system only) — registry.
- The legacy "interior large family" — NOT-TESTED, still open.
- Manuscript insertion of the topology figure — owner-gated venue decision; this
  turn built and referenced the figure in v10, which the owner can drop at the
  venue pass (the addendum un-gates the figure's availability, not its insertion).

## 4. Disposition

MATCH/MISMATCH/NOT-TESTED recorded above is the pre-registered one-shot comparison;
no re-runs were (or will be) performed to change verdicts. The committed archive is
left verbatim; local mirror `repo_assets_mirror/p4_five_regime_campaign/` matches
remote byte-for-byte.
