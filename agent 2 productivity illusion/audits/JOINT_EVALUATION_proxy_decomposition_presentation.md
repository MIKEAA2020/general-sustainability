# Joint evaluation: proxy-decomposition presentation (two audits)

**Decision implemented: Option 3 — share-weighted decomposition + caveat.**
Both audits recommend Option 3, and I agree. This document records the joint adjudication and the
numerical verification for `manuscript_ECOMOD_v33.tex`.

---

## 1. Where the two audits agree (all adopted)

1. **Raw component log-changes are NOT additive.** `dln A_f = +0.160`, `dln b_f = +1.128`,
   `dln B_c^res = −0.404` do **not** sum to `dln B = +0.207` (they sum to `+0.884`), because the components
   enter weighted by their shares, and the "residual" is a log of an accounting residual.
2. **Do not show a "total" that implies additivity** alongside raw rows.
3. **The residual is an accounting residual, not independent ecological capital.** It mixes grazing, forestry,
   fishing, built-up land, equivalence-factor effects and calibration effects. Label it a **proxy residual**,
   never "capital-book residual" unqualified.
4. **Report weighted contributions that sum to `dln B`**, and show the raw log-changes only as diagnostics.
5. **Check the weighted yield contribution is the dominant positive term before asserting it.** (It is:
   `+0.393` vs area `+0.056`.)

## 2. Where the audits differ (and why I choose Audit 2's exact method)

- **Audit 1** offers base-year *or* average-period shares, and its skeleton shows a "Total = dlnB" cell. With
  simple **average** shares (`s̄_X = 0.375`, `s̄_C = 0.625`) the contributions sum to **+0.231**, i.e. an
  **+11% error** against `dlnB = +0.207`. Audit 1's table as drawn would therefore *not* actually sum to
  `dlnB` — a residual inconsistency.
- **Audit 2** is more rigorous: it flags the approximation error of simple-average shares and provides the
  **exact log-mean (Divisia) weights** when both components are strictly positive, plus a **level
  decomposition** fallback if the residual is non-positive. Audit 2 also gives the strongest, correct residual
  caveat.

**Verdict:** use **Audit 2's exact log-mean weighting** (it reproduces `dlnB` to displayed precision) while
keeping Audit 1's clear recommendation. Do **not** use simple-average shares alone, because they introduce the
very non-additivity the audits warn about.

## 3. Validation (world, 1961–2022; NFA `B` + proxy construction)

Inputs: `B(1961)=9.7553e9`, `B(2022)=1.1997e10` gha → `dlnB = +0.2069`. Proxy log-changes verified:
`dln A_f=+0.160`, `dln b_f=+1.128`, `dln C=−0.404`. Calibration `α_crop=0.19` ⇒ `X(1961)=α·B(1961)`.
Both components strictly positive (`C(1961)=7.90e9`, `C(2022)=5.28e9`), so the log decomposition is valid
(no level-decomposition fallback needed; noted that this positivity was checked).

| Component | Raw Δln | Log-mean weight | **Contribution** |
|---|---:|---:|---:|
| Fast-book yield `b_f` | +1.128 | w_X=0.349 | **+0.393** |
| Fast-book area `A_f` | +0.160 | w_X=0.349 | **+0.056** |
| Residual (proxy, non-cropland) `C` | −0.404 | w_C=0.600 | **−0.242** |
| **Total** | | | **+0.207** = dlnB |

- Log-mean weights: `L(X)=3.778e9`, `L(C)=6.501e9`, `L(B)=1.084e10`; `w_X=0.349`, `w_C=0.600`.
- Exact-sum check: `w_X·(1.288) + w_C·(−0.404) = +0.2067 ≈ dlnB` (residual of order `1e-4`, rounding only).
- **Simple-average check (audit-1 method):** `0.375·1.128 + 0.375·0.160 + 0.625·(−0.404) = +0.231`,
  error `+0.024` (~11%) vs `dlnB` — **rejected**.

### Honest share caveat
`w_X = 0.349` is the log-mean fast-book share; the instantaneous share `s_X` rises from `0.19` (1961) to
`0.56` (2022). That rise is a consequence of the calibration `b_f(1961)=α·B/A_f` plus applying the crop-yield
index to the full fast book; the **absolute split is a proxy and is not identified**. Only the **growth/index
decomposition and its sign ordering** are defensible, exactly as the manuscript already states. The
calibration-driven share increase further justifies the caveat that this is a proxy, not a structural
identification.

## 4. What was changed / kept
- Manuscript proxy decomposition replaced with the exact share-weighted (log-mean) formulation and table;
  raw log-changes kept as a diagnostic row / footnote; residual relabelled **proxy residual (non-cropland
  biocapacity)**.
- Added: share-weighted equation, log-mean weight definition, exact-sum check, and the residual
  accounting caveat.
- Keyword table and interpretation updated so the "yield channel is dominant" claim is made *after*
  weighting (it survives: `+0.393`).

**Sources / status.** Data from `data/nfa/GFN_world_biocapacity_footprint_population_1961_2022.csv`; proxy
construction from `model_sims/twoland_nfa_proxy.py`. All numbers above computed in-session from that data.

---

## Addendum (turn-17): alpha-sensitivity robustness + audit point (b) fallback

**1. Robustness to the calibration alpha.** The absolute split turns on the unidentified calibration
`alpha` (base-year cropland share of B). Recomputing the weighted decomposition over `alpha in [0.10,0.34]`
(reproducible: `model_sims/twoland_nfa_proxy_sensitivity.py`):

| alpha | wX | wC | yield | area | residual | sum | dominant |
|---|---:|---:|---:|---:|---:|---:|---|
| 0.10 | 0.183 | 0.795 | +0.207 | +0.029 | −0.029 | +0.207 | yield |
| 0.15 | 0.275 | 0.689 | +0.310 | +0.044 | −0.148 | +0.207 | yield |
| **0.19** | **0.349** | **0.600** | **+0.393** | **+0.056** | **−0.242** | **+0.207** | yield |
| 0.25 | 0.459 | 0.457 | +0.517 | +0.073 | −0.384 | +0.207 | yield |
| 0.30 | 0.550 | 0.315 | +0.621 | +0.088 | −0.502 | +0.207 | yield |
| 0.34 | 0.622 | 0.087 | +0.702 | +0.100 | −0.594 | +0.207 | yield |

- **Qualitative claim robust:** the weighted identity sums to `d ln B = +0.207` exactly at every admissible alpha,
  and yield is the dominant positive term in every row. Claims to assert: sign ordering only.
- **Quantitative split NOT robust:** `wX` spans 0.183→0.622; `s_X(2022)` spans ≈0.30→≈1.00; raw residual
  `d ln C` spans ≈−0.04→≈−6.8. Magnitudes must not be quoted.

**2. Audit point (b) made active.** The log-mean weighting requires `X,C>0` in both end years. That fails once
`alpha >= ~0.339` (i.e. `C(2022) <= 0`), so the fallback is not merely academic. Implemented an explicit
**level decomposition** `ΔB = ΔX + ΔC`, valid for any alpha, reproducing `ΔB = +2.242e9` gha directly, with the
same sign statement (fast book up, residual down). Both log and level decompositions now appear in the
manuscript with a validity gate.

**Status of the three audit points.** (a) residual-accounting footnote — done; (c) yield-dominance-after-weighting
— done; (b) level-decomposition fallback — now done (was flagged, now fully written with the threshold and
formula).
