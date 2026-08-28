# A005 two-pool specialization — scored test execution record

**Executed:** the H1 two-pool discrete specialization of the A005 template,
scored at the test level on the locked Edwards Aquifer (San Antonio Pool,
J-17) annual panel, against the one-pool H0 and the retention baselines,
under the A005 falsifiability protocol ("the two-pool model should be
selected only if it improves held-out state, service, or safety prediction
… preregistered metrics and margins"; "leakage must not absorb residual
mismatch").

## What was executed

- **Model.** State \((H_f, H_s)\) ft AMSL, annual step; \(H_f\) observed
  exactly as the J-17 annual mean, \(H_s\) latent;
  \(H_{f,t+1} = c_0 + c_R R_t + c_P P_t + c_F H_{f,t} + c_L (H_{s,t} -
  H_{f,t})\), clipped to [610, 710] (the H0 clip rule);
  \(H_{s,t+1} = d_0 + d_F H_{f,t} + d_S H_{s,t}\) with \(d_F = 1-d_S\) (the
  template's "slow pool fills only by leakage" structure; constant slow
  loss in \(d_0 \le 0\)). Linear bidirectional leakage
  \(\ell_{fs} = \kappa(H_f - H_s)\); donor/recipient limiter dropped and its
  nonnegativity content replaced by preregistered admissibility conditions.
- **Normalizations (identification).** The scale freedom \(H_s \to
  \beta H_s\) is killed by \(d_F = 1-d_S\); the datum freedom is an exact
  flat ridge (at fixed \(d_S\), the \(H_s\) column carries \(d_S^t \in
  \mathrm{span}\{1, w_t\}\)) and is killed by the declared equilibrium
  initialization \(H_{s,0} = H_{f,0}\). Unrestricted, the single-well record
  identifies only \(\psi = c_F - c_L\) and the product \(c_L d_F\).
- **Estimator.** Conditional least squares on the one-step fast equation,
  profiled over \(d_S\) on the fixed grid 0.005…0.995; training windows
  only; the H0/baseline side reproduces `run_ladder.py` exactly (all
  baseline rows match the frozen fixed-window scores to \(<10^{-9}\) ft).
- **Rule (preregistered).** H1 is retained only if it beats naive
  persistence, M1, M2 and M2m on held-out RMSE of `H_mean` in ≥ 3 of the 4
  fixed windows with a ≥ 5% margin over the best baseline in each winning
  window, AND its parameters are physically admissible in all four windows
  (slow pole in (0,1) and interior; \(0 < c_L \le 1\); \(c_R > 0\),
  \(c_P < 0\); \(0 < c_F \le 1\); real stable poles; \(d_0 \le 0\); positive
  implied storage/leakage coefficients), AND the residual discipline passes
  (leakage contribution ≤ residual standard error in every window; lag-1
  residual autocorrelation increase vs H0 ≤ 0.1).

## Verdict

**H1 is NOT retained; the negative certificate is issued.** All three rule
conditions fail:

1. Held-out RMSE: 0 winning windows (H1 excess over the best baseline:
   +149.9% dor_drawdown, +48.2% dor_recovery, +2.7% prepermit_wet, +147.0%
   cpm_era).
2. Admissibility: 0 of 4 windows admissible. Leakage coefficient negative
   in three windows (\(c_L\) = −11.599, −1.543, −272.521; +0.701 in
   cpm_era); complex (oscillatory) poles in three windows; the slow pole
   runs to the grid boundary (0.995) in prepermit_wet, where 10 usable
   observations face 7 parameters (df = 3); cpm_era fails only the pumpage
   sign (\(c_P = +0.059\)), a sign the one-pool H0 fit carries in the same
   window (\(\gamma = +0.009\)) — in-window flux–head confounding, not a
   two-pool artifact.
3. Residual discipline: the leakage term exceeds the residual standard
   error in 3 of 4 windows (up to 362×); lag-1 residual autocorrelation
   increases by more than 0.1 in 2 of 4 windows. The leakage term operates
   as a residual sink — the failure mode the A005 protocol names.

Identification findings recorded with the negative result: the leakage
split is weakly determined (only \(\psi = c_F - c_L\) stays bounded; design
condition numbers \(9.4\times10^4\)–\(2.7\times10^7\)); the unrestricted
eliminated-form profile puts the slow pole at the grid floor in three of
four windows and its identified product \(c_L d_F\) changes sign across
windows (−0.134, +0.077, −1.980, +0.602) — no stable template-sign
cross-pool coupling in the single-well record.

The negative certificate is a property of the single-well annual record and
the declared linear specialization. The admitted object for this system
remains the H0 one-pool affine approximation (R04.Cor2, `APPROXIMATION`);
the A005 two-pool module's "conditionally admissible" status is unchanged.

## Artifacts

- Runner (deterministic, numpy/pandas only, byte-identical rerun verified):
  `wave_e_edwards/src/run_twopool.py`
- Scored table: `wave_e_edwards/results/twopool_fixed_window_scores.csv`
- Full record (parameters, implied leakage/storage coefficients, poles,
  profiles, cross-check, admissibility, discipline, rule evaluation):
  `wave_e_edwards/results/twopool_results.json`
- Formal admission-style test document:
  `wave_e_edwards/admission/A005_twopool_specialization_test.md`
- Locked panel (sha256
  `d6d725db57af5c820d3f62506aa2d5fcd862da3206824d0fa8beb06478706019`):
  `wave_e_edwards/data/annual_panel.csv`

## What remains open at the module level

The single-well scored test cannot discharge the exact-specialization
blockers of the A005 two-pool module; all remain open:

- **Geological identification evidence** (V-A005 identification
  requirements): independent geological geometry, multi-depth heads,
  pumping tests, tracer/isotope and water-age data, and prior ranges for
  \(C_i\) and \(\kappa_{fs}\). Absent in the locked panel; the slow pool
  was identifiable here only through the head record's own dependence
  structure, and that structure did not support the split.
- **Solute layer** (V-A005-08/09): no solute data in the panel; the solute
  balances remain untested and out of scope.
- **Set-valued observation / \(B_k\) structure** (V-A005-11): the test used
  a point observation model (\(H_f\) exact, \(H_s\) latent); the
  compatible-state topology and closed-graph filter remain unimplemented.

Also outside this test: \(q_{\rm rel}\) routing (V-A005-04, removed at the
annual discrete level), the leakage donor/recipient limiter (V-A005-05,
replaced by the linear specialization and its admissibility checks), and
any governance operator (the policy class here is historical pumpage
replay).
