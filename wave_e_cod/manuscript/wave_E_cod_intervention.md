# Does catch governance protect the limit reference point? An intervention-selection test on Northern cod (Ω_2016)

**Wave E empirical paper — intervention leg — working manuscript**

*Companion to `wave_E_cod_forecast_ladder.md` (prediction leg; not re-litigated here) and the cod-side analogue of `wave_E_edwards_intervention.md`. Protocol: `protocol_intervention.md`, frozen 2026-08-26 before any kernel, boundary, replay, or retention score was computed. Admission row: `admission/R04_Cor2_cod_kernel.md` (`APPROXIMATION`).*

## Abstract

The general theory's §15 requires intervention selection to be scored, not asserted: a governance module is kept only if it improves a preregistered protection-and-supply outcome. The prediction leg on this object ended in a negative certificate (persistence beats the surplus ladder). This paper runs the intervention leg on the same locked series: robust viability kernels of the 2016 limit reference point (LRP, 884.6 kt) for a declared catch-policy family under persistent productivity-shock floors, with the Cor2/Cor5 erosion conversion applied in the form the fitted map admits.

**Verdicts.** (1) *Productivity negative certificate:* under the perpetual-worst and 5th-percentile persistent shock classes, no catch policy — zero catch included — holds the LRP: the worst-case map has no positive fixed point for any catch level, and every infinite-horizon kernel is empty. The LRP is protected by good years, not by catch management. (2) *Negative selection:* no declared policy is retained under the frozen rule; the reactive rules (the critical-zone rule and a cascade) are strictly less protective than the moratorium at the boundary and improve on it at no reading — the mirror image of the Edwards Aquifer result, where the reactive architecture was retained. (3) *Constructive boundary:* the maximal robust flat catch is 57.6 kt (24% of the pre-1992 240 kt level) under the 10th-percentile class, and no positive catch is robust under the harsher classes. (4) *Certified layer:* the governed surplus map is expansive at the LRP (F′ = 1.153 > 1), so the contraction form of the erosion conversion is inapplicable; the expansive form empties every certified kernel beyond T = 5 years — the first object in this programme where the binding obstruction to certified intervention claims is the expansion rate itself.

## 1. Object

The governed surplus-production object of `wave_e_cod`: the ladder's own M2
class $S_{t+1}=[S_t+rS_t(1-S_t/K)-C_t+e_t]_+$ (Allee off) fit by one-step
least squares on 1983–2007 with Schijns annual catch — $r = 0.2369$,
$K = 5000$ (pinned at its optimization bound; the series never approaches
carrying capacity — a declared defect; the LRP-boundary results depend
chiefly on the identified $r$). Residual SD 135.0 kt; defect declaration
$\varepsilon = 460.0$ kt yr$^{-1}$ (the 1992 collapse transition);
out-of-sample audit 2008–2015: max 47.1 kt — **not exceeded**, unlike the
Edwards object. Safe set: the single declared threshold $K^* = $ LRP
$= 884.6$ kt. No Ω_xte row is produced; the 2023 LRP belongs to the other
specification and is not pooled.

The disturbance classes are persistent additive productivity floors from the
fit-window residual distribution: UC-min $=-460.0$ (the perpetual worst
observed one-step shock), UC-q05 $=-318.8$, UC-q10 $=-114.8$ kt yr$^{-1}$.
Because this object has no independent input channel (unlike Edwards'
recharge), the disturbance classes and the defect declaration are the same
measured quantity in two roles — disclosed, not repaired.

The governance family: BAU $C \equiv 5$ kt (moratorium-level inshore
removals, the declared implementable use post-1992); flat caps
$\rho\cdot 240$ kt; S1, the DFO-2009 critical-zone rule at a declared 60 kt
cap (60 above the LRP, 0 below); and a cascade (60/30/5/0 kt at
LRP/0.75LRP/0.5LRP/below — sub-LRP stages declared [N]).

## 2. Results

### 2.1 Kernels (nominal)

| Policy | UC-min $T{=}1$ | UC-q05 $T{=}1$ | UC-q10 $T{=}1$ | UC-q10 $T{=}\infty$ |
|---|---:|---:|---:|---:|
| BAU (5 kt) | 1141.0 | 1016.5 | **884.6** | **884.6** |
| flat 240 kt | 1351.1 | 1224.4 | 1043.8 | empty |
| flat 120 kt | 1243.4 | 1117.8 | 938.8 | 1363.0 |
| flat 60 kt / S1 / cpm | 1189.9 | 1064.9 | 886.7 | 900.3 |
| flat 0 kt | 1136.6 | 1012.1 | **884.6** | **884.6** |

Lower boundaries of the robust kernels (kt); "empty" = no state is robustly
viable. Under UC-q10 the moratorium (BAU) and zero catch hold the **entire**
safe set $[884.6, 10^4]$ at every horizon. Every nonzero cap lifts the
kernel's lower edge above the LRP — the 60 kt rules by 2.1 kt at $T=1$ and
15.7 kt at $T=\infty$. Under UC-min and UC-q05 the infinite-horizon kernel is
empty for **every** policy: the worst-case map has no positive fixed point
($g_{\max} = rK/4 = 296$ kt yr$^{-1}$ is below the persistent floor), so
every trajectory declines monotonically.

### 2.2 The two negative certificates

**Productivity.** Under UC-min/UC-q05 no catch policy — zero catch included —
holds the LRP. This is the cod analogue of the Edwards institutional
negative certificate, here at the primary safe set and driven by
productivity: the reference point is protected by good years, not by demand
management.

**Selection.** Under the frozen retention rule (at least as protective as
BAU everywhere; improves somewhere; more catch than every matched flat cap)
**nothing is retained**. S1/cpm fail clause (a): their 60 kt cap removes
catch exactly where the moratorium already sits at 5 kt, so their kernels are
strictly smaller at the boundary; they improve on BAU at no reading. The
Edwards leg retained its reactive rules at +3.3% to +50.6% water; this leg
retains none. Which governance architecture earns its complexity is
system-dependent — the theory's deliverable is the scored comparison, not a
universal architecture verdict.

### 2.3 Constructive content

The maximal robust flat catch — the largest constant catch whose worst-case
low equilibrium stays at or below the LRP — is **57.6 kt** under UC-q10
(24% of the pre-1992 240 kt level; $g(K^*) - |e_{q10}| = 172.5 - 114.8$).
Under UC-q05/UC-min it is zero: no positive catch is robust. This is
certification geometry at one declared shock class, not a harvest rule.

Supply replays (mean allowed catch over the observed 1983–2006 states):
BAU 5 kt; S1 10.0 kt (the critical-zone cut is active in 83% of observed
years — the stock was below the LRP for almost the entire history); cpm
16.3 kt; flat-60 60 kt; flat-0 0 kt.

### 2.4 Certified layer: the expansion obstruction

The Cor2/Cor5 erosion conversion needs the closed loop's contraction rate.
Here $F'(S) = 1 + r(1-2S/K)$ is **increasing as S falls**, and at the LRP
$F'(K^*) = 1.153 > 1$: the governed surplus map is expansive at the declared
safe set (it only contracts above $K/2 = 2500$ kt). The contraction form of
the conversion is therefore **inapplicable**; the expansive form
$r_T = \varepsilon(a_{\max}^T-1)/(a_{\max}-1)$ grows without bound
($r_1 = 460$, $r_5 = 3121$, $r_8 = 6386$ kt), and the certified kernel —
the nominal kernel of $K^*+r_T$ — is empty beyond **T = 5 years** for every
policy. At $T=5$ the certified set is $[4005, 10^4]$ kt, above the entire
observed range of the stock. On this object the binding obstruction to
certified intervention claims is the expansion rate itself, not the defect
magnitude — a qualitatively different failure mode from the Edwards leg
(there: a contracting map, defect-bound to $T \le 3$ yr).

### 2.5 Stress replay and classification

Closed-loop replay from the observed 1990 SSB (861.9 kt — already below the
LRP) with the **observed** 1991–1995 residuals: every policy falls below the
LRP by 1992 (BAU to 611.5 kt in 1992 and 366.3 kt by 1994; zero catch only
delays the exit to 1993 at best) — the crash is a productivity event, not a
catch event, exactly as the prediction leg's catch-insufficiency certificate
found.

T=5 classification: under UC-q10 only the 1980s peak years (1985, 1987,
1989; 1988 additionally for BAU) of the 33 observed states lie inside BAU's
T=5 nominal kernel; the entire post-1990 history and most of the 1980s are
outside. Under UC-min/UC-q05 all 33 are outside.

## 3. Limitations

The map is one-pool surplus production on annual means — no age structure,
migration, or survey catchability (the ladder's [M] limitations carry over).
$K$ is pinned at its optimization bound. The residual conflates productivity
shock and model error (no observation-model separation). The persistent-shock
classes are deliberately harsh (a perpetual floor, not an i.i.d. draw); the
q10 reading is the mildest class with any content. Sub-LRP cascade stages are
declared [N] scenarios, not verified institutions. The certified layer is
vacuous at observed stock levels. Nothing here promotes or demotes any
forecast module, transfers E5 numbers, or pools Ω_xte.

## 4. Reproduction

```
cd wave_e_cod && python3 src/run_intervention.py
```

Deterministic (no randomness). Outputs: `results/intervention_results.json`,
`results/intervention_boundaries.csv`. Frozen protocol:
`protocol_intervention.md`. First run 2026-08-26; rerun NONE at publication of
this manuscript.

## References

DFO. 2009. A fishery decision-making framework incorporating the Precautionary Approach.

DFO. 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016. CSAS Science Advisory Report 2016/026.

Schijns, R., et al. 2021. Five centuries of cod catches in Eastern Canada. *ICES Journal of Marine Science* 78: 2675–.

Programme documents cited by ID: general theory §15; R03; R04 (Thm1 converse); R04.Cor2/R03.Cor5 (erosion conversion); A014 (defect list); `wave_e_cod` prediction leg; `wave_e_edwards` intervention leg.
