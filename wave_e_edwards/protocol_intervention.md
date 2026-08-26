# Wave E — Edwards San Antonio Pool. Intervention-selection protocol

**Locked 2026-08-26, before the intervention scores were generated.**
Companion to `protocol.md` (the forecast-ladder protocol, locked 2026-08-25).
This is the §15 **intervention-selection leg** — never before exercised on a
real system in this programme. It shares the locked data object of
`protocol.md` and adds a governance-operator comparison with viability
kernels. It does **not** reopen any forecast-ladder retention decision.

## Protocol sentence (frozen)

Intervention retention is decided solely by robust viability kernels and
replayed supply under the declared uncertainty classes, against the
business-as-usual baseline. No forecast module is promoted or demoted by
this leg; the fibre and the oracle stay excluded; no two-pool claim is made.

## Object (unchanged from `protocol.md`)

| Field | Contents | Type |
|---|---|---|
| \(S\) | Edwards Aquifer, San Antonio Pool, as indexed by well J-17 | D |
| \(z_t\) | Calendar-year mean of daily-high J-17 elevation, ft AMSL | D |
| \(B\) | San Antonio Pool management region; calendar years 1934–2023 | D |
| Data | `data/annual_panel.csv` only (locked 20-column panel); no new data | D |
| \(K^*_{\mathrm{phys}}\) | 618 ft (Comal cessation proximity; declared, not certified) | N / E |
| \(K^*_{\mathrm{inst}}\) | 660 ft (post-2007 Stage I trigger; not applied pre-2007) | N |
| Not \(z\) | Comal, GRACE, J-27, San Marcos, MODFLOW/GWSIM heads | D |

## Dynamics (the scored ladder's M2 class, one pool, affine)

\[
\Delta H_t = \alpha + \beta R_t + \gamma P_t + \delta H_{t-1},
\qquad a = 1+\delta,
\]
fitted by ordinary least squares on the training window 1934–1990
(transitions with both endpoints \(\le\) 1990). Out-of-sample years
1991–2023 are used **only** for the defect audit; no refitting.

Model domain (declared compact set, the ladder's clip bounds):
\(H \in [610, 710]\) ft. Upward exits above 710 ft under extreme recharge
are out-of-domain for the *model* and are not violations of the
lower-threshold constraint; this caveat is carried in the admission record.

## Information pattern (causal, matches the H0 record's map (5))

At the end of year \(t\) the manager observes \((H_t, R_t, P_t)\) and sets
next year's pumping \(P_{t+1} = \pi(H_t)\) (annual-mean approximation to the
intra-year CPM adjustment). Next year's recharge \(R_{t+1}\) is unknown at
decision time and is treated adversarially.

## Uncertainty classes (declared, robust, persistent recharge floors)

Computed on the training window only:

| Class | Declaration | Value (10³ acre-ft yr⁻¹) |
|---|---|---|
| UC-min | \(R \ge \min_{\text{train}} R\) (1956 drought-of-record year, held forever) | 43.7 |
| UC-q05 | \(R \ge\) 5th percentile of train \(R\) | 166.5 |
| UC-q10 | \(R \ge\) 10th percentile of train \(R\) | 179.1 |

For the lower-threshold constraint the adversarial realisation is the floor
(\(\beta > 0\) verified on the fit). These floors are **persistent**
(forever), which is harsher than any recorded drought; the classes are
declared for certification geometry, not as recharge forecasts.

## Governance operators (declared family)

\( \bar P \) = training-mean pumping (1934–1990). Stage thresholds and the
Stage I reduction are from `data/SOURCES.md`; Stage II–IV reductions are
**declared [N] scenarios**, not verified in-repo.

| ID | Rule | Note |
|---|---|---|
| BAU | \(P \equiv \bar P\) | baseline (the persistence analogue) |
| flat-\(\rho\) | \(P \equiv \rho\,\bar P\), \(\rho \in \{0.9, 0.8, 0.7, 0.6, 0.5, 0.0\}\) | flat caps |
| S1 | \(P(H) = 0.8\,\bar P\) if \(H < 660\), else \(\bar P\) | post-2007 Stage I, 20% (verified) |
| cpm | cumulative cuts 20/30/35/40% at \(H<660/650/640/630\) | cascade, stages II–IV [N] |

## Scores (frozen)

1. **Nominal robust kernel boundary** \(b_T(\pi)\) (ft; lower = more
   protective): the infimum of the \(T\)-year robustly viable set
   \(\mathrm{Viab}_T(\pi, K^*)\) under each UC, computed by backward
   recursion \(K_0 = [K^*, 710]\),
   \(K_{n+1} = \{H \ge K^* : aH + \alpha + \beta R_{\mathrm{lo}} + \gamma\pi(H) \in K_n\}\),
   \(T \in \{1,2,3,5,8,10,15,20,\infty\}\). Empty set recorded as `null`.
2. **Certified boundary** after the R04.Cor2 / R03.Cor5 erosion
   (discrete-contraction form):
   \(b^{\mathrm{cert}}_T = b_T(\pi; K^* + r_T)\) with
   \(r_T = \varepsilon (1-a^T)/(1-a)\),
   \(\varepsilon = \max_{\text{train}} |\text{residual}|\) (uniform defect
   declaration). Audits, not used for certification: the out-of-sample max
   residual (defect-adequacy check) and the training residual SD
   (non-uniform reading).
3. **Supply**: mean annual pumping under (i) the deterministic replay of
   the historical train recharge sequence 1934–1990 from \(H_{1934}\) and
   (ii) the OOS sequence 1991–2023 from \(H_{1990}\) (audit only).
4. **Stress replays**: the 1950–1956 recharge sequence from \(H_{1950}\)
   under each policy — minimum head reached, and whether it stays
   \(\ge 618\) ft; plus classification of the actual 1956 and 2011–2014
   annual states against the nominal and certified kernels.

## Retention rule (frozen; mirrors the ladder's persistence benchmark)

BAU is the baseline. A governance module is **retained** iff

(a) it is at least as protective as BAU on the nominal kernel boundary at
    **every** declared horizon under **every** declared UC and both declared
    \(K^*\) readings (no horizon/class/threshold where it is strictly
    worse), **and**

(b) it supplies strictly more water (train replay) than the most protective
    flat cap with the same nominal protection profile.

Otherwise the flat cap (or BAU) suffices — "complexity not earned".
A module that improves only horizons where BAU is already certified earns
no certified-increment claim. A policy whose certified kernel is empty at
every horizon earns no certified claim at all (a nominal-only row).

## Prohibitions (frozen)

- No forecast-module promotion (M2 stays rejected, M1 thin; oracle and
  Comal fibre stay excluded from every score here).
- No two-pool, karst, or solute claim; no pooling with Northern cod or any
  phosphorus catchment.
- \(K^*_{\mathrm{inst}}\) is not applied to pre-2007 history.
- Nothing here is `EXACT_SPECIALIZATION` of A005; every kernel statement
  carries the Cor2 triple (defect, horizon, erosion) and the
  `APPROXIMATION` mapping type.
