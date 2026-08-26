# R04.Cor2 approximation row — Edwards governed kernel object

This row admits the **governed one-pool stock-flow object** of
`wave_e_edwards` (the intervention-selection leg,
`protocol_intervention.md`, executed in `src/run_intervention.py`). It is
the kernel-level sibling of the H0 forecast-map row
(`R04_Cor2_edwards_H0.md`): same data object, same affine dynamics class,
now with the governance-operator family, the declared uncertainty classes,
the declared safe sets, and — for the first time in this programme on a
real system — the **Cor2 erosion conversion actually invoked** (R03.Cor5,
discrete-contraction form). It does **not** close A005 as an exact
specialization, does **not** change R04.Tab3's "conditionally admissible"
verdict for the two-pool module, and does **not** upgrade any forecast
module's retention.

## Maps

| Certificate field | This object |
|---|---|
| (1) type/unit | Head ft AMSL; recharge and pumpage in \(10^3\) acre-ft yr\(^{-1}\). Storage constitutive of head (\(\Delta A = C\Delta H\)); \(C\) absorbed into \((\alpha,\beta,\gamma,\delta)\), not identified. San Antonio + Uvalde recharge/pumpage lumped (inherited H0 defect). |
| (2) phase-space \(\varphi\) | \(H \mapsto H\) on the declared model domain \([610, 710]\) ft (the ladder's clip bounds). A005's \(Z=(H_f,H_s,M_{q,f},M_{q,s},\sigma_{\mathrm{sal}})\) not used; solute/salinity omitted. |
| (3) dynamics | Discrete affine closed loop \(H_{t+1} = \alpha + \beta R_{t+1} + \gamma \pi(H_t) + aH_t\), \(a = 1+\delta = 0.7461\) (OLS on 1934–1990; \(\beta > 0\), \(\gamma < 0\), \(0 < a < 1\) verified). Defects relative to A005: one pool, no two-pool leakage, no distributed karst, no impulse jumps, spring loss not a separate flux, annual-mean granularity versus the 10-day CPM triggers. |
| (4) safe set | Declared \([\mathrm{N}]\), scored not certified: \(K^*_{\mathrm{phys}} = 618\) ft (Comal cessation proximity), \(K^*_{\mathrm{inst}} = 660\) ft (post-2007 Stage I; not applied pre-2007). The constraint is the lower threshold only; upward exits above 710 ft are model-domain exits, not violations. |
| (5) policy/information | Causal origin \((H_t, R_t, P_t)\) known through year \(t\); \(P_{t+1} = \pi(H_t)\) (annual-mean approximation of the intra-year CPM adjustment); \(R_{t+1}\) unknown at decision time, treated adversarially within the declared floors UC-min / UC-q05 / UC-q10 (persistent recharge floors 43.7 / 166.5 / 179.1 \(10^3\) acre-ft yr\(^{-1}\), training-window statistics). No set-valued \(B_k\); no \(\mathsf{I}_q\) branches; the policy class is the declared family (BAU, flat caps \(\rho \in \{0.9,\dots,0.0\}\), Stage-I reactive 20% below 660 ft, CPM cascade 660/650/640/630 with stages II–IV reductions **declared [N]**). |

## Blocking items, this object only

All H0 blocking dispositions carry over unchanged (V-A005-04/05/06/07/08/09/02/10/11 as listed there). Additional, kernel-specific:

| Item | Disposition here |
|---|---|
| Two-pool / karst / solute kernel | **Not claimed.** All kernel statements are one-pool affine `APPROXIMATION` rows. |
| Certified long-horizon kernel | **Not earned.** Under the uniform defect declaration the certified kernel is empty beyond \(T = 3\) yr at \(K^*_{\mathrm{phys}}\) and beyond \(T = 1\) yr at \(K^*_{\mathrm{inst}}\), for every policy in the family (zero pumping included). |
| Institutional-threshold governance | **Negative certificate (nominal level).** Every declared policy's robust kernel at \(K^*_{\mathrm{inst}}\) equals BAU's at every horizon: the declared CPM triggers (≤ 660 ft) lie strictly below every policy's robust boundary, so no declared demand-management rule differentiates the institutional kernel. Even \(P \equiv 0\) has an empty nominal kernel beyond \(T \approx 6\) (UC-min) / \(T \approx 11\) (UC-q10). |
| Observation-model separation | **Withheld.** The residual defect conflates model error and measurement error; no separate observation-noise model is identified. |

## Cor2 triple (computed, not merely declared)

- **Defect \(\varepsilon\)**: \(\max_{\text{train}}|\text{residual}| = 15.41\) ft yr\(^{-1}\) (1934–1990 fit window; residual SD 5.60). **Out-of-sample audit: EXCEEDED** — \(\max_{\text{1991–2023}}|\text{residual}| = 21.81\) ft yr\(^{-1}\); the uniform declaration is optimistic out-of-window and the certified rows below inherit that optimism (recorded, not repaired by refitting — the protocol forbids refitting).
- **Horizon \(T\)**: certified content exists only at \(T \le 3\) yr (physical reading) and \(T \le 1\) yr (institutional reading). No uniform-in-time claim.
- **Safety erosion \(r_T\)**: \(r_T = \varepsilon(1-a^T)/(1-a)\) with \(a = 0.7461\) — the discrete-contraction form of the R03.Cor5 conversion: \(r_1 = 15.41\), \(r_3 = 35.49\), \(r_5 = 46.66\), \(r_\infty = 60.70\) ft. The certified kernel is the nominal kernel of \(K^* + r_T\). The feasible-interval caveat applies with force: the conversion certifies almost nothing at horizons the management question actually cares about — that is the row's principal finding, not a defect of the conversion.

Mapping type: `APPROXIMATION`. Never `EXACT_SPECIALIZATION` of A005. The
nominal-level kernels (no erosion) are reported alongside and are labelled
nominal everywhere.

## What would revoke this row

Everything that revokes the H0 row (silent use of Comal, GRACE, or J-27 as
\(z\); pooling Uvalde and San Antonio as one primary; promoting M2_oracle
or the fibre; asserting a two-pool kernel), plus: claiming a certified
kernel beyond the horizons above; treating the SD reading (5.60 ft) as a
uniform defect bound; applying \(K^*_{\mathrm{inst}}\) to pre-2007
history; treating the UC floors as recharge forecasts rather than
declared certification geometry; asserting that any declared policy makes
the institutional threshold robustly invariant (it does not); or reading
the Stage II–IV cascade reductions as externally verified (they are
declared [N]).
