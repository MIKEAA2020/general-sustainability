# A005 two-pool specialization test — Edwards San Antonio Pool

**Object:** the H1 two-pool discrete specialization of the A005 groundwater
template, scored at the test level on the locked Wave E panel
(`data/annual_panel.csv`, years 1934–2023, `sha256
d6d725db57af5c820d3f62506aa2d5fcd862da3206824d0fa8beb06478706019`).

**Status of this document:** a scored falsification test under the A005
protocol ("the two-pool model should be selected only if it improves held-out
state, service, or safety prediction … 'improves' requires preregistered
metrics and margins"; "leakage must not absorb residual mismatch"). It does
not promote a module. The admitted forecast object for this system remains
the H0 one-pool affine approximation (`admission/R04_Cor2_edwards_H0.md`).

---

## 1. The object

State \((H_f, H_s)\): fast-pool and slow-pool head, ft AMSL, annual step.
\(H_f\) is observed exactly as the J-17 calendar-year mean (`H_mean`);
\(H_s\) is latent. The locked panel's observed range of `H_mean` on
1934–2023 is \([623.151,\ 691.960]\) ft, interior to the declared clip band
\([610, 710]\) ft, so clipping binds only on forecast extrapolation, exactly
as in H0.

The model (linear specialization of the template balances
\(C_f\dot H_f = R_{\rm nat} - q_p - \ell_{fs} - L_f\),
\(C_s\dot H_s = \ell_{fs} - q_{ps} - L_s\),
\(\ell_{fs} = \kappa(H_f - H_s)\)):

\[
H_{f,t+1} = c_0 + c_R R_t + c_P P_t + c_F H_{f,t} + c_L\,(H_{s,t} - H_{f,t}),
\qquad [H_{f,t+1}]_{[610,\,710]},
\]
\[
H_{s,t+1} = d_0 + d_F H_{f,t} + d_S H_{s,t}, \qquad d_F = 1 - d_S,
\]

with \(R\) = `R_total` and \(P\) = `P_wells` (10³ acre-ft yr⁻¹), the same
drivers and the same causal origin convention as the H0 ladder: forecasts
issued at the last training year persist the last training \((R, P)\)
(identical to M2).

The restriction \(d_F = 1-d_S\) is the template's own structure ("the slow
pool has no direct recharge — it fills by leakage"): with no slow pumpage and
a constant slow loss, the slow balance's only head coupling is the leakage
term, so \(d_F = \kappa\Delta t/C_s\) and \(d_S = 1-\kappa\Delta t/C_s\).
The constant slow loss is \(d_0 \le 0\) in the template's sign.

**Declared normalizations (identification).** The leakage law
\(\ell_{fs} = \kappa(H_f - H_s)\) requires both heads on one datum. On a
single-well record two non-identifiabilities are exact:

- *Scale.* The map \(H_s \to \beta H_s\) with \(d_F \to \beta d_F\),
  \(c_L \to c_L/\beta\) leaves the \(H_f\) process exactly invariant. The
  restriction \(d_F = 1-d_S\) fixes \(\beta = 1\).
- *Datum.* At fixed \(d_S\), the design column carrying \(H_s\) contains the
  vector \(d_S^{\,t}\), which lies **exactly** in the span of the intercept
  and the cumulative-loss column \(w_t = (1-d_S^{\,t})/(1-d_S)\); the
  likelihood is exactly flat along \(H_s \to H_s + \gamma\) (with
  compensating \(c_0, d_0\)). The equilibrium initialization
  \(H_{s,0} = H_{f,0}\) is therefore declared: no initial leakage
  disequilibrium is asserted, and no free transient parameter is granted to
  absorb early-window residual mismatch.

What the record identifies without these normalizations is only
\(\psi = c_F - c_L\) (fast own-persistence net of leakage) and the product
\(c_L d_F\) (§4, eliminated-form cross-check).

### Template-blocker dispositions at the test level

| Template item | Disposition in this test |
|---|---|
| Storage domains/units | Head ft AMSL, annual step; \(R, P\) in 10³ acre-ft yr⁻¹; storage constitutive of head. Implied coefficients \(C_f = 1/c_R\), \(C_s = c_L C_f/d_F\), \(\kappa = c_L C_f\) are reported as fitted quantities, not independently constrained. |
| \(\chi\) state | Removed (undefined in the A005 source). |
| Policy class | Historical pumpage replay: \(P_t\) enters as an exogenous driver under the causal origin convention. A forecast-level object; no governance operator, no \(\Gamma(B_k,h_k)\). |
| \(q_{\rm rel}\) (V-A005-04) | Not routed; not represented at the annual discrete level. |
| Leakage limiter (V-A005-05) | The **linear** bidirectional specialization \(\ell_{fs} = \kappa(H_f-H_s)\) is declared (the donor/recipient limiter \([\cdot]_+\psi_i(A_i)\) is dropped). Its nonnegativity content is replaced by preregistered admissibility conditions: \(0 < c_L \le 1\) (the annual exchange closes at most all of the head gap), real stable poles (no oscillatory exchange), and the leakage-magnitude discipline of §5. |
| Total-storage identity (V-A005-06) | Holds by summation of the two discrete balances: \(\Delta(H_f + H_s)\) equals total flux less leakage (which cancels) less losses; no hybrid jumps. |
| Solute balances (V-A005-08/09) | Out of scope: no solute data in the locked panel. |
| Safety set | The 660 ft institutional threshold (post-2007 Stage I) is the Brier target only. No viability kernel, no erosion certificate; \(K^*_{\rm phys} \approx 618\) ft is not scored here. |
| Observation model (V-A005-11) | `H_mean` observes \(H_f\) exactly (no observation-error term); \(H_s\) latent. No set-valued \(B_k\), no compatible-state topology. |

The panel column `R_east` (eastern-basin recharge) is stored and **not**
used: the template forbids direct slow recharge, and `R_east` is not a
slow-pool head observation. `Q_comal` remains the out-of-assessment fibre
and cannot promote or demote anything here.

---

## 2. Identification requirements and their status

The A005 protocol requires, for the fast/slow split, **independent**
geological, multi-depth, pumping-test, tracer/isotope, water-age, and
recharge information. **This requirement is unmet by the single-well annual
record.** No multi-depth head, no tracer or water-age data, and no
independent slow-pool storage estimate exists in the locked panel. The slow
pool is identifiable only through the dependence structure of the one
observed head series. This is a declared identification limitation; the
scored comparison below is the falsifiable test the template's protocol
demands at this data level, not a discharge of the identification
requirement.

Two consequences are recorded as findings of the test (numbers in §4):

1. The leakage split is weakly determined: in every window the fit drives
   \((c_F, c_L)\) to large opposite-sign values whose difference
   \(\psi = c_F - c_L\) is the only well-determined combination; the design
   condition numbers are \(9.4\times10^4\) to \(2.7\times10^7\).
2. The unrestricted eliminated form identifies only \(\psi\) and the product
   \(c_L d_F\); the sign of that product is **window-inconsistent**
   (§4), so the record carries no stable template-sign evidence for the
   cross-pool coupling.

---

## 3. Preregistered retention rule

Stated before any held-out score was generated; the committed runner
implements it mechanically.

> H1 (the two-pool specialization) is retained as an admitted object ONLY IF
> on held-out data it (i) beats naive persistence AND the retained
> output-only model M1 AND the one-pool H0 (both the last-flux M2 and
> training-mean M2m variants) on RMSE of `H_mean` in at least 3 of the 4
> fixed windows, with a ≥5% RMSE margin relative to the best of those
> baselines in each winning window; AND (ii) the fitted parameters are
> physically admissible in all four windows; AND (iii) the
> residual-discipline check passes: the leakage term's contribution does not
> exceed the residual standard error in any window (leakage is not absorbing
> unexplained residuals) and the residual lag-1 autocorrelation does not
> increase relative to H0 by more than 0.1. Otherwise H1 is NOT retained and
> the verdict is the negative certificate: the two-pool structure is not
> supported on the single-well annual record.

Operational details, all fixed in the runner:

- **Windows** (identical to the frozen Wave E ladder): dor_drawdown
  1934–1950 → 1951–1956; dor_recovery 1934–1956 → 1957–1961; prepermit_wet
  1980–1990 → 1991–1995; cpm_era 1997–2014 → 2015–2023.
- **Margin:** \(\mathrm{RMSE}(H1) \le 0.95\,\min\) over the four baselines.
- **Estimator:** conditional least squares on the one-step fast equation
  (the conditional expectation of \(H_f\) given the observed \(H_f\) path),
  profiled over the slow pole \(d_S\) on the fixed grid
  \(0.005, 0.010, \dots, 0.995\) under the declared normalizations; fit on
  the training window only.
- **Admissibility conditions (A1–A8), per window:** A1 \(0 < d_S < 1\);
  A1b \(d_S^*\) interior of the grid (\([0.015, 0.985]\); a boundary
  optimum is an identification finding); A2 \(0 < c_L \le 1\); A3
  \(d_F = 1-d_S > 0\) (imposed by the template reading); A4 \(c_R > 0\)
  and \(c_P < 0\); A5 \(0 < c_F \le 1\); A6 both system poles real and
  \(|\lambda| < 1\); A7 \(d_0 \le 0\); A8 \(C_f > 0\), \(C_s > 0\),
  \(\kappa > 0\). Any inadmissible fit is H1 rejection evidence for that
  window.
- **Residual standard error:** \(\hat\sigma = \sqrt{SSE/(n_{\rm obs}-7)}\)
  with \(n_{\rm obs}\) one-step training observations and 7 fitted
  parameters \((c_0, c_R, c_P, c_F, c_L, d_0, d_S)\).
- **Leakage contribution:** \(\mathrm{RMS}_t\, c_L(H_{s,t} - H_{f,t})\) over
  the training steps under the declared normalization; the datum-invariant
  de-meaned RMS is reported alongside so the check is not an artifact of
  the normalization.
- **Lag-1 autocorrelation:** \(\sum_t \varepsilon_t\varepsilon_{t-1} /
  \sum_t \varepsilon_t^2\), computed raw (unclipped) on in-sample residuals
  for H1 (fast-balance residuals) and for H0 (the one-pool \(\Delta H\)
  residuals of the M2 fit).

---

## 4. Scored results

All numbers are artifact-exact from `results/twopool_results.json` and
`results/twopool_fixed_window_scores.csv` (scores rounded to 3 decimals
here; the artifacts carry full precision). The H0/baseline side reproduces
`run_ladder.py` exactly: all 16 baseline rows match
`results/fixed_window_scores.csv` to \(<10^{-9}\) ft.

### Held-out scores

| window | model | n | RMSE (ft) | MAE (ft) | Brier(660) | direction |
|---|---|---|---|---|---|---|
| dor_drawdown | naive_persist | 6 | 23.748 | 22.203 | 0.000 | 0.00 |
| dor_drawdown | M1 | 6 | 30.941 | 29.154 | 1.000 | 0.20 |
| dor_drawdown | M2 | 6 | 18.105 | 16.862 | 0.000 | 0.80 |
| dor_drawdown | M2m | 6 | 27.441 | 25.689 | 1.000 | 0.20 |
| dor_drawdown | **H1_two_pool** | 6 | **45.251** | 41.759 | 0.833 | 0.60 |
| dor_recovery | naive_persist | 5 | 43.623 | 41.340 | 0.800 | 0.00 |
| dor_recovery | M1 | 5 | 56.243 | 54.491 | 0.800 | 0.00 |
| dor_recovery | M2 | 5 | 55.321 | 52.755 | 0.800 | 0.00 |
| dor_recovery | M2m | 5 | 37.741 | 35.769 | 0.800 | 0.75 |
| dor_recovery | **H1_two_pool** | 5 | **55.940** | 54.227 | 0.800 | 0.25 |
| prepermit_wet | naive_persist | 5 | 30.131 | 27.043 | 0.800 | 0.00 |
| prepermit_wet | M1 | 5 | 20.019 | 15.497 | 0.800 | 0.25 |
| prepermit_wet | M2 | 5 | 16.670 | 11.537 | 0.000 | 0.25 |
| prepermit_wet | M2m | 5 | 23.471 | 19.560 | 0.800 | 0.25 |
| prepermit_wet | **H1_two_pool** | 5 | **17.115** | 13.552 | 0.400 | 0.75 |
| cpm_era | naive_persist | 9 | 27.413 | 24.253 | 0.667 | 0.00 |
| cpm_era | M1 | 9 | 15.622 | 12.879 | 0.556 | 0.25 |
| cpm_era | M2 | 9 | 23.373 | 20.671 | 0.667 | 0.25 |
| cpm_era | M2m | 9 | 14.794 | 11.094 | 0.333 | 0.25 |
| cpm_era | **H1_two_pool** | 9 | **36.545** | 34.506 | 0.667 | 0.75 |

### Condition (i): RMSE versus the baselines

H1 wins **no window** (required: at least 3 of 4). Excess of H1 RMSE over
the best baseline in each window:

| window | best baseline (RMSE) | H1 RMSE | excess |
|---|---|---|---|
| dor_drawdown | M2 (18.105) | 45.251 | +149.9% |
| dor_recovery | M2m (37.741) | 55.940 | +48.2% |
| prepermit_wet | M2 (16.670) | 17.115 | +2.7% |
| cpm_era | M2m (14.794) | 36.545 | +147.0% |

No window satisfies even the "beats all four baselines" clause without the
margin. Condition (i) **fails** (0 winning windows).

### Fitted H1 parameters (per window)

\(n_{\rm obs}\) = one-step training observations; df = \(n_{\rm obs}-7\);
\(\psi = c_F - c_L\); \(\kappa\), \(C_f\), \(C_s\) in 10³ acre-ft yr⁻¹
ft⁻¹ and 10³ acre-ft ft⁻¹ respectively.

| quantity | dor_drawdown | dor_recovery | prepermit_wet | cpm_era |
|---|---|---|---|---|
| \(n_{\rm obs}\) / df | 16 / 9 | 22 / 15 | 10 / 3 | 17 / 10 |
| \(c_0\) | 8115.921 | 1508.032 | 181523.030 | 153.691 |
| \(c_R\) | −0.004594 | 0.004785 | −0.010008 | 0.014013 |
| \(c_P\) | −0.837683 | −0.496403 | −0.036216 | +0.059367 |
| \(c_F\) | −10.972787 | −1.173953 | −272.605595 | 0.717338 |
| \(c_L\) | −11.599472 | −1.542889 | −272.520984 | 0.700613 |
| \(\psi = c_F - c_L\) | 0.626685 | 0.368935 | −0.084611 | 0.016724 |
| \(d_0\) | −0.706720 | −2.050889 | +0.010608 | −1.942998 |
| \(d_S\) | 0.925 | 0.930 | 0.995 | 0.155 |
| \(d_F = 1-d_S\) | 0.075 | 0.070 | 0.005 | 0.845 |
| poles | 0.775843 ± 0.920713 i | 0.649468 ± 0.171184 i | 0.455195 ± 1.034995 i | −0.686665, 0.858389 |
| max \|pole\| | 1.204012 | 0.671649 | 1.130671 | 0.858389 |
| \(C_f\) | −217.664 | 209.002 | −99.918 | 71.361 |
| \(\kappa\) | 2524.784 | −322.467 | 27229.748 | 49.997 |
| \(C_s\) | 33663.789 | −4606.666 | 5445949.657 | 59.167 |
| design condition no. | 3.41×10⁶ | 1.04×10⁶ | 2.67×10⁷ | 9.40×10⁴ |
| \(d_S\) 1%-profile band | [0.905, 0.935] | [0.905, 0.950] | [0.990, 0.995] | [0.055, 0.255] |

### Condition (ii): physical admissibility

**No window is admissible** (0 of 4 required). Failed conditions per window:

| window | failed conditions |
|---|---|
| dor_drawdown | A2 (\(c_L=-11.599<0\)); A4 (\(c_R=-0.004594<0\)); A5 (\(c_F=-10.973\)); A6 (poles complex, \(\|\lambda\|_{\max}=1.204>1\)); A8 (\(C_f<0\)) |
| dor_recovery | A2 (\(c_L=-1.543<0\)); A5 (\(c_F=-1.174\)); A6 (poles complex); A8 (\(\kappa<0\), \(C_s<0\)) |
| prepermit_wet | A1b (\(d_S^*=0.995\), the grid boundary); A2 (\(c_L=-272.521<0\)); A4 (\(c_R<0\)); A5 (\(c_F=-272.606\)); A6 (poles complex, \(\|\lambda\|_{\max}=1.131>1\)); A7 (\(d_0=+0.0106>0\)); A8 (\(C_f<0\)) |
| cpm_era | A4 (\(c_P=+0.059367>0\)) |

Identification findings attached to condition (ii):

- **Weak leakage identification (all windows).** \((c_F, c_L)\) diverge in
  opposite directions while only their difference \(\psi\) stays bounded
  (0.626685, 0.368935, −0.084611, 0.016724). The record determines the
  fast pool's net own-persistence, not the leakage split.
- **prepermit_wet is not estimable at this parameterization.** 10 usable
  one-step observations against 7 parameters (df = 3); \(d_S^*\) runs to the
  grid boundary 0.995 with a 1%-profile band of width 0.005, the design
  condition number is \(2.67\times10^7\), and the implied slow storage
  \(C_s = 5.45\times10^6\) 10³ acre-ft ft⁻¹ is three orders of magnitude
  beyond any Edwards storativity reading.
- **cpm_era** is the near-admissible fit (A1–A3, A5–A8 pass; \(c_L = 0.7006\),
  real stable poles, \(C_f = 71.36\), \(C_s = 59.17\), \(\kappa = 50.0\)) and
  fails only the pumpage sign A4 (\(c_P = +0.0594\)). The one-pool H0 fit in
  the same window carries the same wrong-signed pumpage coefficient
  (\(\gamma = +0.008978\) in the M2 map): in the CPM era, permit reductions
  co-occur with drought, so the in-window flux–head confounding defeats the
  sign at both pool levels. The preregistered admissibility gate applies to
  H1 as fitted; the sign failure is recorded as such.
- **Unrestricted eliminated-form cross-check** (restricted ARX(2) profiled
  over the slow pole; identification diagnostic, not the scored fit): the
  profiled slow pole sits at the grid floor 0.005 in three of four windows
  (dor_drawdown, dor_recovery, cpm_era) and at 0.800 in prepermit_wet; the
  identified cross-pool product \(c_L d_F\) is −0.133912, +0.077378,
  −1.979768, +0.602072 across the four windows — **negative in two,
  positive in two**. The single-well record therefore contains no stable
  template-sign evidence for the leakage coupling, in either the
  unrestricted or the normalized reading.

---

## 5. Residual-discipline report

| window | leakage RMS (ft/yr) | residual SE (ft/yr) | ratio | de-meaned leakage RMS | H0 lag-1 | H1 lag-1 | change |
|---|---|---|---|---|---|---|---|
| dor_drawdown | 76.020 | 4.184 | 18.2 | 58.224 | −0.148681 | −0.164609 | −0.015928 |
| dor_recovery | 17.925 | 3.972 | 4.5 | 13.163 | −0.225668 | +0.060258 | +0.285926 |
| prepermit_wet | 3457.885 | 9.548 | 362.2 | 3432.736 | −0.103448 | −0.590814 | −0.487365 |
| cpm_era | 8.456 | 13.217 | 0.6 | 8.431 | −0.639673 | +0.069471 | +0.709143 |

- **Leakage magnitude:** the leakage term's contribution exceeds the
  residual standard error in 3 of 4 windows (18.2×, 4.5×, 362.2×; passes
  only in cpm_era at 0.6×). The de-meaned (datum-invariant) RMS confirms
  the failure is not an artifact of the declared datum normalization. Under
  the A005 residual discipline, the leakage term is absorbing structure the
  identified fluxes do not explain — this is model error attributed to
  leakage, which the template forbids.
- **Lag-1 autocorrelation:** the H1 fast-balance residual autocorrelation
  increases relative to H0 by more than 0.1 in 2 of 4 windows
  (+0.285926 in dor_recovery, +0.709143 in cpm_era).

Condition (iii) **fails** on both clauses.

---

## 6. Verdict

**H1 is NOT retained.** The preregistered rule is evaluated mechanically:

- (i) held-out RMSE with margin: **0 winning windows** (required ≥ 3) —
  H1 loses to the best baseline in all four windows (+2.7% to +149.9%
  excess);
- (ii) physical admissibility: **0 of 4 windows admissible**;
- (iii) residual discipline: leakage exceeds the residual standard error in
  3 of 4 windows; lag-1 autocorrelation increases by more than 0.1 in 2 of
  4 windows.

**Negative certificate.** The two-pool structure is not supported on the
single-well annual record: at this data level the additional state does not
improve held-out prediction, its fitted parameters are not physically
admissible in any window under the template's sign and stability structure,
and the leakage term operates as a residual sink rather than an identified
flux. The verdict is a property of the record and the declared
parameterization, not of the template: the identification evidence the A005
protocol demands (geological geometry, multi-depth heads, pumping tests,
tracer/isotope and water-age data) is absent, and the test cannot discharge
it.

Consequences for the register:

- The admitted object for this system remains the **H0 one-pool affine
  approximation** (`admission/R04_Cor2_edwards_H0.md`), mapping type
  `APPROXIMATION`; nothing here changes that row.
- The A005 two-pool module remains **conditionally admissible** with its
  exact-specialization blockers open; this test closes the *scored-test*
  item at the single-well level with a negative result and does not close
  the module.
- Reopening requires data, not refitting: multi-depth head or water-age
  evidence identifying a slow mode, a solute layer, or an independent
  storage/leakage constraint.

## 7. Reproducibility

- Runner: `wave_e_edwards/src/run_twopool.py`; executed as
  `python3 run_twopool.py` from `wave_e_edwards/src`. Dependencies:
  numpy, pandas only. No network access, no random number generation.
- Determinism: fixed grid \(d_S \in \{0.005, \dots, 0.995\}\) step 0.005;
  equilibrium initialization \(H_{s,0}=H_{f,0}\); `numpy.linalg.lstsq`;
  ties broken by grid order. A repeat execution produced byte-identical
  artifacts (sha256-verified).
- Locked panel: `wave_e_edwards/data/annual_panel.csv`, sha256
  `d6d725db57af5c820d3f62506aa2d5fcd862da3206824d0fa8beb06478706019`.
- H0/baseline reproduction: the naive_persist, M1, M2 and M2m rows of
  `results/twopool_fixed_window_scores.csv` match the frozen
  `results/fixed_window_scores.csv` to \(<10^{-9}\) ft in all four windows
  (recorded in `results/twopool_results.json`,
  `h0_reproduction_check.all_baseline_rows_match = true`).
- Artifacts: `results/twopool_fixed_window_scores.csv` (window × model ×
  metrics), `results/twopool_results.json` (full record: fitted parameters,
  implied leakage/storage coefficients, poles, profile diagnostics,
  eliminated-form cross-check, admissibility verdicts, residual-discipline
  numbers, rule evaluation, verdict).
