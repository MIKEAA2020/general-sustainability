# R04.Cor2 approximation row — Edwards H0 forecast map

This row admits **only** the discrete one-pool forecast class used in
`wave_e_edwards`. It does **not** close A005 as an exact specialization
and does **not** change R04.Tab3’s “conditionally admissible” verdict
for the two-pool module.

## Maps

| Certificate field | This object |
|---|---|
| (1) type/unit | Head ft AMSL; recharge and pumpage in \(10^3\) acre-ft yr\(^{-1}\). Storage is constitutive of head: \(\Delta A = C\Delta H\). \(C\) is absorbed into \((\alpha,\beta,\gamma,\delta)\), not identified. |
| (2) phase-space \(\varphi\) | \(H\mapsto H\). A005’s \(Z=(H_f,H_s,M_{q,f},M_{q,s},\sigma_{\mathrm{sal}})\) is **not** used. Solute and salinity are omitted. |
| (3) dynamics | Discrete affine map on annual head. Defect relative to A005: no two-pool leakage, no distributed karst, no impulse jumps, San Antonio + Uvalde recharge/pumpage lumped, spring loss not a separate measured flux. |
| (4) safe set | Thresholds are scored, not certified. \(K^*_{\mathrm{phys}}\approx 618\) and \(K^*_{\mathrm{inst}}=660\) (post-2007) are declared **[N]** and are not the same set. |
| (5) policy/information | Causal origin: \((H,R,P)\) known through year \(t\). No set-valued \(B_k\). No \(\mathsf{I}_q\) branches. CPM is visible in \(P_t\), not as a separate kernel claim. |

## Blocking items, this object only

| Item | Disposition here |
|---|---|
| V-A005-04 \(q_{\mathrm{rel}}\) | **Removed.** No managed release in the forecast map. |
| V-A005-05 leakage limiter | **N/A.** H0 has no two-pool leakage. |
| V-A005-06 total storage + jumps | Discrete identity \(\Delta H=\alpha+\beta R+\gamma P+\delta H\). No hybrid jumps. Residual is discrepancy, not a physical destination. |
| V-A005-07 donor/recipient | Forecasts clipped to \([610,710]\). Not a proved invariant cone. |
| V-A005-08/09 solute | **Omitted.** Not in \(z\). |
| V-A005-02/10 \(\chi\) | **Removed.** |
| V-A005-11 compatible-state topology | **Withheld.** No \(B_k\), no closed-graph filter. |

## Cor2 triple

- Defect \(\varepsilon\): one-step training residual SD of the affine map,
  reported per window (feet / year). Not converted to a kernel erosion.
- Horizon \(T\): 1 and 5 years. No uniform-in-time claim.
- Safety erosion: **not claimed.** R03.Cor5 is not invoked. Threshold
  scores are Brier numbers, not viability certificates.

Mapping type: `APPROXIMATION`. Never `EXACT_SPECIALIZATION` of A005.

## What would revoke this row

Silent use of Comal, GRACE, or J-27 as \(z\); pooling Uvalde and San
Antonio as one primary; promoting M2_oracle or the fibre into retention;
asserting a two-pool kernel.
