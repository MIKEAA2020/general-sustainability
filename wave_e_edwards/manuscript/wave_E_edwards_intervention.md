# Wave E — Edwards Aquifer intervention-selection ladder: governance operators and viability kernels

Version 1 (2026-08-26). Scored leg under `protocol_intervention.md`
(locked before scores were generated; the forecast-ladder protocol
`protocol.md` and its retention decisions are untouched). Companion
manuscript: `wave_E_edwards_forecast_ladder.md` (prediction leg).
Admission row: `admission/R04_Cor2_edwards_kernel.md` (Cor2,
`APPROXIMATION`).

## 1. Question

The prediction leg returned a negative certificate: persistence beats the
causal ladder on J-17, and the oracle water-balance gap (7.55 vs 13.23 ft)
locates the missing rent in the information layer. The intervention leg
asks the question the architecture exists for: **does a declared
governance operator change the viability kernel of a real system, and at
what water cost?** This is the §15 intervention-selection leg — never
before exercised on a real system in this programme.

## 2. Object, dynamics, information

Same locked object as the forecast ladder: J-17 annual-mean head
\(z_t\) (ft AMSL), San Antonio Pool, 1934–2023, from the locked
`annual_panel.csv`. \(z\) is a measured well level, not an assessment
inversion. Recharge \(R\) (USGS/EAA estimated) and pumpage \(P\) (EAA
Table 1, San Antonio Pool wells) are the fluxes. No new data.

Dynamics: the ladder's M2 stock-flow class, one pool, affine —

\[
\Delta H_t = \alpha + \beta R_t + \gamma P_t + \delta H_{t-1},
\]

fitted by OLS on 1934–1990 (57 transitions). OLS fit:
\(\alpha = 163.49\), \(\beta = 0.0198\) ft per \(10^3\) acre-ft,
\(\gamma = -0.02844\) ft per \(10^3\) acre-ft,
\(\delta = -0.2539\), \(a = 1+\delta = 0.7461\) — a contraction with a
25.4%-per-year mean reversion. Residual SD 5.60 ft, max 15.41 ft
(training). Out-of-sample (1991–2023, audit only): SD 8.40, max 21.81 ft.

Information pattern: the manager ends year \(t\) knowing
\((H_t, R_t, P_t)\) and sets \(P_{t+1} = \pi(H_t)\); \(R_{t+1}\) is
unknown at decision time and is treated adversarially within a declared
persistent floor (UC-min = 43.7, UC-q05 = 166.5, UC-q10 = 179.1
\(10^3\) acre-ft yr\(^{-1}\); the 1956 drought-of-record year is UC-min).
These floors are certification geometry — harsher than any recorded
drought — not recharge forecasts.

Safe sets (declared [N], from the ladder protocol): \(K^*_{\mathrm{phys}}
= 618\) ft (Comal cessation proximity) and \(K^*_{\mathrm{inst}} = 660\)
ft (post-2007 Stage I trigger; not applied to pre-2007 history).

Governance family: BAU (\(P \equiv \bar P = 282.2\), training mean); flat
caps \(\rho\bar P\), \(\rho \in \{0.9, 0.8, 0.7, 0.6, 0.5, 0\}\); the
Stage-I reactive rule (20% cut when \(H < 660\), the in-repo-verified
reduction); and a CPM cascade (cumulative 20/30/35/40% cuts at
\(H < 660/650/640/630\) — Stage I verified, stages II–IV **declared [N]**
scenarios).

## 3. Erosion (R04.Cor2 / R03.Cor5, discrete-contraction form)

With uniform defect \(\varepsilon = 15.41\) ft (training max) and
contraction \(a = 0.7461\), trajectory deviation over \(T\) years is
bounded by \(r_T = \varepsilon (1-a^T)/(1-a)\): \(r_1 = 15.41\),
\(r_3 = 35.49\), \(r_5 = 46.66\), \(r_\infty = 60.70\) ft. The certified
kernel at horizon \(T\) is the nominal kernel of \(K^* + r_T\). The
out-of-sample defect max (21.81 ft) **exceeds** the declared
\(\varepsilon\): the certified rows below are optimistic out-of-window,
and this is recorded rather than repaired (no refitting, per protocol).

## 4. Results

### 4.1 Worst-case attractors and the minimal cut

The worst-case (UC floor) attractor of the closed loop, by policy:

| Policy | UC-min | UC-q05 | UC-q10 |
|---|---:|---:|---:|
| BAU | 615.72 | 625.31 | 626.29 |
| flat-90% | 618.88 | 628.47 | 629.45 |
| flat-80% | 622.04 | 631.63 | 632.61 |
| S1 (reactive 20% < 660) | 622.04 | 631.63 | 632.61 |
| cpm cascade | 628.36 | 636.37 | 637.35 |
| flat-0 (zero pumping) | 647.32 | 656.91 | 657.90 |

Under a perpetual 1956-recharge floor, BAU's attractor (615.72 ft) sits
**below** the physical threshold; the smallest flat cut whose attractor
clears 618 ft is **7.2%**. The Stage-I reactive rule's attractor equals
flat-80%'s (the cut is active on the entire attractor branch).

### 4.2 Nominal kernels (no erosion)

Physical reading (618 ft), UC-min: BAU's kernel boundary climbs
618.8 (T=1) → 625.6 (T=5) → 658.4 (T=10) and the kernel is **empty**
beyond \(T \approx 14\) years — BAU is not robustly viable against a
perpetual drought-of-record. Every cut policy in the family (a 10% flat
cap, S1, cpm, and deeper) makes \([618, 710]\) **robustly invariant**:
the whole declared safe set is the kernel at every horizon, including the
infinite horizon. Under UC-q05/q10 the safe set is already invariant at
BAU (attractors 625.3 / 626.3 ft): governance differentiates the kernel
only in the drought-floor reading.

Institutional reading (660 ft): **negative certificate.** Every declared
policy's robust kernel equals BAU's at every horizon — the boundaries
(675.1 at T=1, 695.3 at T=2 under UC-min; empty from T=3) lie strictly
above the deepest CPM trigger (660 ft), so no declared demand-management
rule activates in the viable region and the kernel is policy-invariant.
Demand management buys **years, not invariance**: even zero pumping has
an empty nominal kernel beyond \(T \approx 6\) (UC-min) / \(T \approx 11\)
(UC-q10), because its worst-case attractor (647.3 / 657.9 ft) still sits
below 660 ft. The institutional threshold is protected by wet years, not
by the declared pumping family — which is exactly the frequency-management
rationale the actual CPM rule implements, and that rationale is outside
the robust-kernel frame.

### 4.3 Certified kernels (eroded)

With the erosion of §3 applied, **every** policy in the family has an
empty certified kernel beyond \(T = 3\) years at the physical threshold
and beyond \(T = 1\) year at the institutional threshold (zero pumping:
\(T = 5\) under UC-q05/q10, physical reading only). The certified
boundaries at T=3 / UC-min / 618 ft: flat-0 662.2 < flat-80 697.8 <
BAU = S1 = cpm 706.7. The binding constraint on certified intervention
claims is the **model defect, not the governance** — the same
information-layer rent the prediction leg found, now measured on the
intervention leg.

### 4.4 Supply and retention

Mean prescribed pumping (actual-head replay, 1934–1990):

| Policy | Supply (\(10^3\) acre-ft yr\(^{-1}\)) | Cut active |
|---|---:|---:|
| BAU | 282.16 | 0% |
| flat-90% | 253.94 | 100% |
| flat-80% | 225.73 | 100% |
| **S1** | **262.36** | 35.1% |
| **cpm** | **254.93** | 35.1% |
| flat-60% | 169.29 | 100% |

Retention rule (frozen): at least as protective as BAU everywhere, and
more water than the most protective flat cap with matched protection.

- **S1: RETAINED (nominal, UC-min/618 ft reading).** It matches the flat
  caps' robust invariance (kernel = whole safe set, all horizons) while
  supplying 262.4 vs flat-90%'s 253.9 (**+8.4 \(10^3\) acre-ft
  yr\(^{-1}\), +3.3%**) and flat-80%'s 225.7 (+36.6, +16.2%). The
  reactive architecture earns its complexity: the same protection at
  strictly more water.
- **cpm: RETAINED (nominal, same reading).** Attractor 628.4 (equal to
  flat-60%'s) at supply 254.9 vs flat-60%'s 169.3 (+50.6%).
- **Certified level:** S1 and cpm remain retained against their
  dominating flat caps (S1 vs flat-80: +36.6 supply at every certified
  horizon; cpm vs flat-60: +85.6), but only over the \(T \le 3\)
  horizons where their certified kernels are nonempty.
- **Institutional reading: nothing retained** (all policies ≡ BAU).

### 4.5 Classification and stress replays

T=5 nominal kernel (UC-min, 618 ft): BAU excludes exactly one actual year
from its viable set — **1956**, the drought-of-record year (623.15 ft
annual mean). S1 and cpm exclude none: the entire 90-year actual record
is robustly 5-year viable under the cut rules. The T=5 **certified**
kernels are empty, so no actual year is certified 5-year viable under any
policy — the honest boundary of this exercise.

1950s open-loop diagnostic (model with actual \(R, P\) vs actual heads,
1951–1956): the affine map under-predicts the drought decline — model
659.5 → 631.3 vs actual 659.5 → 623.2, max error 8.1 ft, biased high.
The 1950s model-based policy replays (from the observed 1950 head) keep
all policies above 618 ft (BAU min 629.7, S1 634.9, cpm 637.1), but the
open-loop bias means the true margins are thinner than the replay
suggests; this is recorded, not corrected.

## 5. Reading

For the first time on a real system, the full loop runs end-to-end:
measured state, calibrated stock-flow map, declared governance operators,
declared uncertainty classes, viability kernels with an explicit
admission erosion, held-out defect audit, and a frozen retention rule —
and the loop returns a **positive selection result** (the reactive
architecture matches flat-cap protection at 3–50% more water, and a 7.2%
mean cut secures the physical threshold against a perpetual
drought-of-record where BAU fails) together with two honest negatives:
the institutional threshold is not demand-manageable to invariance under
the declared classes, and the certified content is defect-bound to
\(T \le 3\) years. The missing rent is again the information layer: the
12.8-vs-7.55 ft oracle gap is what the erosion eats.

## 6. Limitations

Nominal kernels carry no defect margin; certified kernels use a training
defect that the out-of-sample audit exceeds (15.4 vs 21.8 ft). The map is
one-pool affine on annual means; the actual CPM triggers are 10-day
averages, so the annual-mean rule is a coarse relative of the real
institution. Stage II–IV reductions are declared scenarios, not verified.
San Antonio + Uvalde are lumped (inherited defect). Observation error is
not separated from model defect. The UC floors are certification
geometry, not forecasts; the 1950s replay is biased high by 8.1 ft. No
independent rerun has been performed: every number here is first-run.
Nothing in this leg promotes or demotes any forecast module, and no
two-pool, karst, or solute claim is made.

## 7. Reproduction

```
python3 src/run_intervention.py
```

writes `results/intervention_results.json` and
`results/intervention_boundaries.csv` (deterministic; no randomness).
Machine-readable verdicts: `retention` (nominal),
`retention_certified`, `certified_horizon_nonempty` in the JSON.
