# Wave E intervention-selection protocol — Northern cod (NAFO 2J3KL), Ω_2016

**Frozen 2026-08-26, before any kernel, boundary, replay, or retention score was computed.**
This is the cod-side analogue of `wave_e_edwards/protocol_intervention.md` (G1 Track 2,
G1a). It executes §15's intervention-selection leg on the **governed surplus-production
object** of `wave_e_cod` — the ladder's own model class, not NCAM. The ladder's
forecast verdicts (persistence wins; no module retained) are inputs, not outputs, of
this protocol and are not re-litigated.

## 1. Object (declared)

| Field | Contents | Type |
|---|---|---|
| System | Northern cod 2J3KL as represented by NCAM M-shift SSB, 1983–2015 (the locked Ω_2016 series; not pooled with xteNCAM) | D |
| Map | Discrete surplus with catch: `S_{t+1} = [S_t + r·S_t(1−S_t/K) − C_t + e_t]+` (the ladder's M2 class, Allee off: 𝔰 = 0) | M |
| Fit window | 1983–2007, one-step least squares on Schijns annual catch (the ladder's own `fit_params`, bounds r ∈ (0.001, 2], K ∈ (max train, 5000]) | E |
| OOS audit window | 2008–2015 (recovery era): residuals audited, no refit | E |
| Safe set | K* = LRP = 884.6 kt (the 1983–1989 mean, the declared [N] threshold of Ω_2016). Ω_2016 declares **no second threshold** — there is no cod analogue of the Edwards phys/inst pair, and the 2023 40% B_MSY LRP belongs to Ω_xte and is not pooled | N |
| State domain | [1e-3, 10000] kt (the ladder's clip floor; upper bound declared at twice the fitted K) | M |
| Governance family | §4 below | E/[N] |

**Declared defects carried by the object.** (i) K is expected to pin at its
optimization upper bound (the series never approaches carrying capacity) — all upper
edges inherit it; the LRP-boundary results depend chiefly on r, which is identified.
(ii) The residual conflates productivity shocks and Schaefer-class model error — there
is no independent input channel (unlike Edwards' recharge), so the disturbance classes
and the defect declaration below are the **same measured quantity in two roles**;
disclosed, not repaired. (iii) One pool, no age structure, no migration (A014-L list).

## 2. Defect declaration (Cor2 triple, first element)

ε = max |residual| over the **fit window** 1983–2007, in kt yr⁻¹, together with the
residual SD and the lower-tail quantiles (the UC classes below). The OOS audit
(2008–2015) is reported alongside; no refit is permitted whatever it shows.

## 3. Uncertainty classes (persistent productivity shocks)

Mirroring the Edwards recharge floors (perpetual 1956 / q05 / q10 of training
recharge), the disturbance classes are **persistent additive productivity floors**
drawn from the fit-window residual distribution:

| Class | Floor e (kt yr⁻¹) | Reading |
|---|---|---|
| UC-min | min(fit residuals) | perpetual worst observed one-step productivity shock |
| UC-q05 | 5th percentile of fit residuals | perpetual 5th-percentile shock |
| UC-q10 | 10th percentile of fit residuals | perpetual 10th-percentile shock |

The worst-case closed loop is `F(S) = [S + r·S(1−S/K) − C(S) + e]+` with e the class
floor (a constant — the persistent reading, deliberately harsher than i.i.d.).

## 4. Governance-operator family

| ID | Rule | Type |
|---|---|---|
| BAU | C ≡ 5 kt (moratorium-level inshore removals; the declared implementable U post-1992) | E |
| flat_100 … flat_0 | C ≡ ρ·240 kt, ρ ∈ {1.0, 0.75, 0.5, 0.25, 0.0} (240 kt = pre-1992 directed-fishery level) | E |
| S1 | C = 60 kt if S ≥ LRP, else 0 (DFO 2009 PA critical-zone rule at a modest declared cap) | E/[N] |
| cpm | cascade: C = 60 kt if S ≥ LRP; 30 kt if S ∈ [0.75·LRP, LRP); 5 kt if S ∈ [0.5·LRP, 0.75·LRP); 0 below 0.5·LRP | [N] (declared scenario) |

Stage thresholds below the LRP are declared scenarios, not verified institutions
(the Edwards analogue: stages II–IV declared [N]).

## 5. Kernels

Robust T-step viability kernel of the safe set [K*, S_HI] under the persistent floor:
K_0 = [K*, 10000]; K_{n+1} = {S ∈ K_n : F(S) ∈ K_n} with F the worst-case closed loop
(policies act on the current state; the catch jump thresholds split the domain into
pieces, on each of which F is a concave quadratic — preimages are computed by interval
arithmetic on the quadratic roots). Horizons T ∈ {1, 2, 3, 5, 8, 10, 15, 20, ∞}; the
infinite-horizon kernel is the fixpoint with a one-step stability re-check.

## 6. Certified layer (Cor2/Cor5 erosion conversion)

r_T = ε·(1 − a^T)/(1 − a) if the closed loop contracts with rate a < 1 on the safe
domain; **otherwise** the expansive form r_T = ε·(a_max^T − 1)/(a_max − 1) with
a_max = sup|F'| over the safe domain. The form that applies is computed from the
fitted map and **recorded** — if the map is expansive at the safe-set boundary (as the
Schaefer map is below K/2), the contraction form is inapplicable and the certified
kernel is the nominal kernel of K* + r_T with the expansive r_T. No certified claim at
any horizon where K* + r_T exceeds the nominal kernel's reach.

## 7. Replays

1. **Supply replay** (no dynamics): mean allowed catch C(S_t^obs) over the fit-window
   states 1983–2006, per policy; cut-active fraction reported.
2. **Stress replay** (the 1990s analogue of the Edwards 1950s replay): closed-loop
   model replay from the observed 1990 SSB with the **observed** 1991–1995 residuals,
   per policy; whether the path stays ≥ LRP reported. (The ladder already established
   that catch cannot produce the 1992–94 pulse; this replay records what governance
   does against the *observed* shock class.)
3. **T=5 classification**: which observed SSB values lie outside each policy's T=5
   nominal kernel, per UC class.

## 8. Retention rule (frozen; mirrors the Edwards rule)

A non-BAU policy is **retained** iff:

- (a) its robust kernel is at least as protective as BAU's at **every** (UC, T)
  reading — compared on the kernel lower boundary, empty = worst; and
- (b) it improves on BAU somewhere (strictly lower boundary at some reading); and
- (c) at some reading where it improves, its supply-replay mean catch exceeds that of
  every at-least-as-protective flat cap (the "matched protection" clause).

No forecast module is promoted or demoted. The oracle, the survey-start variant, and
capelin modules play no role. No Ω_xte row is produced.

## 9. Outputs

`results/intervention_results.json` (fit, UC, kernels, steady states, maximal robust
flat catch, supply, stress replay, classification, retention at nominal and certified
levels, certified horizons), `results/intervention_boundaries.csv` (per policy × UC × T
kernel lower boundaries, nominal and certified), admission row
`admission/R04_Cor2_cod_kernel.md`, manuscript `manuscript/wave_E_cod_intervention.md`.
Deterministic; no randomness anywhere.
