# R04.Cor2 approximation row — Northern cod governed surplus object

This row admits the **governed surplus-production object** of `wave_e_cod`
(the intervention-selection leg, `protocol_intervention.md`, executed in
`src/run_intervention.py`). It is the cod-side analogue of the Edwards
kernel-level row (`wave_e_edwards/admission/R04_Cor2_edwards_kernel.md`) and
the kernel-level sibling of the A001/A014 class admission the forecast ladder
already carries: same data object (the locked NCAM M-shift SSB series, the
ladder's own surplus class), now with the governance-operator family, the
declared uncertainty classes, the declared safe set, and the Cor2/Cor5 erosion
conversion invoked in the form the fitted map admits — here the **expansive**
form, the first object in this programme for which the contraction form is
provably inapplicable at the declared safe set. It does **not** transfer E5
numbers, does **not** promote or demote any forecast module, and produces **no
Ω_xte row**.

## Maps

| Certificate field | This object |
|---|---|
| (1) type/unit | SSB in kt; catch in kt yr\(^{-1}\). The ladder's M2 class: \(S_{t+1}=[S_t+rS_t(1-S_t/K)-C_t+e_t]_+\), Allee off (\(\mathfrak s=0\)). |
| (2) phase-space \(\varphi\) | \(S \mapsto S\) on the declared model domain \([10^{-3}, 10^4]\) kt. No age structure, no migration, no spatial pools (A014 defect list). |
| (3) dynamics | One-step least squares on 1983–2007 with Schijns annual catch (the ladder's own `fit_params`): \(r = 0.2369\), \(K = 5000\) — **pinned at the optimization bound** (the series never approaches carrying capacity; upper-edge statements inherit this; the LRP-boundary results depend chiefly on the identified \(r\)). Fit residual SD 135.0; OOS audit 2008–2015 (8 transitions) max 47.1 kt — the declaration is **not** exceeded out-of-window (the Edwards object's was). |
| (4) safe set | Declared \([\mathrm{N}]\), scored not certified: \(K^* = \mathrm{LRP} = 884.6\) kt (the 1983–1989 mean of Table A2). Ω_2016 declares **no second threshold** — there is no cod analogue of the Edwards phys/inst pair; the 2023 40% \(B_{\mathrm{MSY}}\) LRP belongs to Ω_xte and is not pooled. |
| (5) policy/information | Causal origin: \(S_t\) known through year \(t\); catch decided from \(S_t\) (annual granularity). Declared family: BAU \(C \equiv 5\) kt (moratorium-level, the declared implementable \(U\) post-1992); flat caps \(\rho \cdot 240\) kt, \(\rho \in \{1.0, 0.75, 0.5, 0.25, 0.0\}\); S1 — the DFO-2009 critical-zone rule at a declared 60 kt cap (\(C = 60\) above the LRP, 0 below); cpm cascade (60/30/5/0 kt at LRP/0.75·LRP/0.5·LRP/below — the sub-LRP stages are declared \([\mathrm{N}]\) scenarios). Disturbance: persistent additive productivity floors from the fit-window residual distribution (UC-min −460.0 / UC-q05 −318.8 / UC-q10 −114.8 kt yr\(^{-1}\)) — the same measured quantity as the defect declaration in a second role (no independent input channel exists; disclosed, not repaired). |

## Blocking items, this object only

| Item | Disposition here |
|---|---|
| Certified long-horizon kernel | **Not earned.** The closed loop is **expansive at the safe-set boundary** (\(F'(K^*) = 1.153 > 1\)); the contraction form of the erosion conversion is inapplicable, the expansive form gives \(r_T\) growing without bound, and the certified kernel is empty beyond \(T = 5\) yr for every policy in the family (zero catch included). |
| Productivity-class viability | **Negative certificate (nominal level).** Under UC-min and UC-q05 the worst-case map has **no positive fixed point for any catch level, zero included** (\(g_{\max} = rK/4 = 296\) kt yr\(^{-1}\) < the persistent floor): every trajectory declines monotonically. The infinite-horizon kernel is empty for every policy — the LRP is protected by good years, not by catch management. |
| Reactive-architecture retention | **Negative selection (nominal level).** No declared policy is retained under the frozen rule: S1/cpm are strictly less protective than BAU at the boundary (their 60 kt cap removes catch exactly where the moratorium already sits at 5 kt), and they improve on BAU at no reading. The mirror image of the Edwards positive result. |
| Boundary viability of nonzero caps | Every nonzero cap lifts the kernel's lower edge above the LRP (flat-25/S1/cpm at q10: 886.7 kt at \(T=1\), 900.3 at \(T=\infty\)); the **maximal robust flat catch is 57.6 kt** (24% of the historical 240 kt) under UC-q10, and no positive catch is robust under UC-q05/UC-min. |
| Observation-model separation | **Withheld.** The residual conflates productivity shocks and Schaefer-class model error; the UC floors and the defect ε are the same measured quantity in two roles. |

## Cor2 triple (computed, not merely declared)

- **Defect \(\varepsilon\)**: \(\max_{\text{train}}|\text{residual}| = 460.0\) kt yr\(^{-1}\) (1983–2007 fit window; the 1992 collapse transition; residual SD 135.0). **Out-of-sample audit: NOT exceeded** — \(\max_{\text{2008–2015}}|\text{residual}| = 47.1\) kt yr\(^{-1}\). The uniform declaration holds out-of-window on this object (the Edwards object's did not).
- **Horizon \(T\)**: certified content exists only at \(T \le 5\) yr, for every policy. No uniform-in-time claim.
- **Safety erosion \(r_T\)**: \(a_{\max} = \sup_{[K^*, S_{\mathrm{HI}}]} F' = 1.153\) (attained **at the LRP**; \(F'\) decreases in \(S\)), so the **expansive** form applies: \(r_T = \varepsilon(a_{\max}^T - 1)/(a_{\max} - 1)\) — \(r_1 = 460.0\), \(r_2 = 990.5\), \(r_3 = 1602.1\), \(r_5 = 3120.5\), \(r_8 = 6385.9\) kt, \(r_\infty\) unbounded. The certified kernel is the nominal kernel of \(K^* + r_T\); at \(T = 5\) that is the interval \([4005, 10^4]\) — above the entire observed range of the stock.

Mapping type: `APPROXIMATION`. Never `EXACT_SPECIALIZATION` of A001/A014, and
never a transfer of the E5 linear-toy numbers (R04.Thm1's converse forbids it;
the E5 margins are the linear module's, not NCAM SSB's). The nominal-level
kernels (no erosion) are reported alongside and are labelled nominal
everywhere.

## What the leg adds to the programme's empirical map

With this row, the §15 intervention-selection leg has now been exercised on
**both** scored systems, with opposite verdicts at the reactive-architecture
question: **retained** on Edwards (S1/cpm match flat-cap protection at +3.3% to
+50.6% water — the first positive selection result), **not retained** on cod
(the reactive rules cut exactly where the moratorium already protects; the
flat-cap analytic boundary 57.6 kt is the constructive content). Which
governance architecture earns its complexity is system-dependent; the theory's
claim is the scored comparison itself, not a universal architecture verdict.

## What would revoke this row

Silent use of \(F\) or \(M\) as drivers; pooling any Ω_xte row into this
object; promoting the survey-start variant, capelin modules, or any forecast
module; asserting a certified kernel beyond \(T = 5\); asserting that any
catch policy holds the LRP under UC-min or UC-q05 (none does, zero catch
included); treating the bound-pinned \(K\) as identified; treating the
sub-LRP cascade stages as verified institutions (they are declared
\([\mathrm{N}]\)); or reading the maximal-robust-flat-catch number (57.6 kt)
as a quota recommendation — it is certification geometry at one declared
shock class, not a harvest rule.
