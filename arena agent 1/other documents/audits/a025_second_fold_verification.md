# Second-fold campaign (τ_f2 ≈ 64.4023272) — independent verification memo (2026-09-02)

**Object.** The committed second-fold campaign
(`research_program/validated_computations/a025_second_fold/`, commits `a3823c5`
pre-registration, `363003b` machinery, `0782880` execution, all 2026-09-02 UTC),
downloaded verbatim to `repo_assets_mirror/a025_second_fold/` (18 files) and verified
here by independent re-reading of the committed records. This memo is an independent
check of the records, not the independent rerun (first-run status stands).

## 1. What the campaign claims (from its own report)

- A second fold of the Candidate-A gated model at τ_f2 ∈ [64.402327203368,
  64.402327203372] yr — interval-Krawczyk-certified on the m=64 Moore–Spence system
  (unique zero, G′ nonsingular, both nondegeneracy constants excluding zero),
  three-order (m=64/96/128) agreement 5.53e-7 ≤ 1e-6.
- The upper branch, carried down from the converged cycle at τ+ − 0.05, neither
  terminates at τ = 130 nor fails collocation; it turns at τ_f2 with amplitude ≈10.5;
  16 pseudo-arclength points past the turn record a STABLE returning arm
  (μ1 = 0.9993 → 0.9435 monotone).
- The stable arm is NOT generically reachable near the fold: 21 basin runs around
  τ_f2 and 21 runs on 133–146 all settle (H1 intermediate at 145–146); the
  148.6–149.5 capture onset is a BASIN boundary inside the mathematically bistable
  window (τ_f2, τ+), not a fold.

## 2. Independent verification of the committed records

| Claim | Record check | Verdict |
|---|---|---|
| 200 branch records = 1 switch + 183 natural + 16 arclength | CSV method counts 1/183/16 | PASS |
| Seed τ = 150.30847731, N_ptp 0.1003, T 159.279, μ1 = 1.0000878, res 6.2e-12 | CSV row 1; source = P4-campaign orbit npz (environment.json) | PASS |
| 183 natural steps 150.308 → stall at 64.402327895, residuals ≤ 3.7e-12 | CSV: stall 64.402327895, residual 2.7e-12; max res over all 200 records 1.0e-9 | PASS |
| Quoted table points (149.989/129.902/99.902/64.702/64.403120/64.402328) | CSV reproduces all τ/N_ptp/T/μ1 values | PASS (one row excepted, see §3) |
| Peak μ1 = 1.27745 at τ = 74.902 | CSV: 1.277446 at 74.90185 | PASS |
| Stable arm: 16 pts, 64.4023279→64.4382854, μ1 0.9993→0.9435, amp 10.538→10.888 | CSV arclength rows | PASS |
| μ1 real everywhere (imag zero) | CSV mu1_im max = 0.0 | PASS |
| Krawczyk: enclosure, ψ^T F_τ ∈ [0.257936, 0.260750], ψ^T D²F[v,v] ∈ [-5.89e-4, -5.88e-4] (negative), sin θ ≤ 2.96e-6, |G| = 1.02e-12, FD battery | krawczyk.json fields | PASS |
| Three-order agreement 5.53e-7 | results.json: m64 64.4023272033699 / m96 ...65316083 / m128 ...65081875, spread 5.526e-7 | PASS |
| Frozen-box failure preserved + deviation recorded | frozenbox.json/.log exist; tau_box_source = "DEVIATION…" | PASS |
| Basin: 45 runs; grid A settles w/ H1 intermediate at 145–146 (RSD 0.0012/0.0017); grid B all settle (RSD ~4e-13); dt-halving at 64.4 unchanged | basin CSV | PASS |
| Pre-registration §7 deviation clause ("recorded as deviations, never silently") | deviation recorded in JSON + logs | PASS |

## 3. Discrepancies found (record-only, not certificate-affecting)

1. **Report table row at τ = 74.902**: the report lists N_ptp = 6.295, T = 83.11
   beside τ = 74.902 and μ1 = 1.27745. The CSV's 74.902 record has N_ptp = 6.035,
   T = 85.163 (μ1 = 1.27745 ✓). The values 6.295/83.51 belong to the τ = 73.402
   record (T = 83.511; the report's "83.11" matches no record — closest 83.51).
   A table-assembly slip mixing two rows; the CSV data is internally consistent and
   the certificate is unaffected. Flagged for the authoring.
2. The report's frozen-box construction imported the m=64-vs-m=96/128 cross-check
   spread into the certificate box (~25× the lower fold's box width) and failed at
   every radii rung; the certified run used the recorded deviation (re-centered
   τ-box ±1e-8). Legitimate under pre-registration §7, and preserved verbatim —
   but note the m=64-vs-m=96/128 gap (5.5e-7) is ~5 orders larger than the lower
   fold's (2.7e-11); the certificate is strictly for the m=64 system (stated).

## 4. Consequence for the paper (executed this turn)

**P4 v11** built (v10 untouched). The two-fold structure is now the paper's record:
both global folds certified at the discrete collocation level (lower S-branch fold
τ_f = 5.5872362; second fold τ_f2 ∈ [64.402327203368, 64.402327203372]); the
148.6–149.5 capture onset is a basin boundary, not a fold — all text that treated
it as a possible fold location is corrected (five-regime regimes (iii)/(iv) relabeled
τ_f/τ_f2/capture-onset; the upper-boundary paragraph rewritten to the second-fold
record; the M3-B register; the certification-hierarchy paragraph; the early-warning
caveat; the conclusion; the abstract, 241 words). The S-branch structure is described
with the reachability caveat (stable arm not generically reachable near the fold).
The four-state "upper fold ≈ 64.4 yr" now matches the certified three-state τ_f2
within 0.05% — the two "upper fold moves from ≈148 to ≈64" sentences (which carried
the old 148 reading) are corrected. Figure regenerated as
`figs_p4/fig2_five_regime_topology_v2.png` (upper S-branch panel + second-fold basin
grids + multiplier inset; the v1 PNG remains untouched on disk).

**Verification verdict: the certified second fold is supported by the committed
records; no defect found that affects the fold location, the certificate, or the
S-branch/stability classification.** First-run status, the 64.438–148.6 gap, and the
continuum/RFDE lift remain open items.
