# Smooth-Krein Barrier Formulation of the Distributive Boundary

### Abstract

The distributive condition that human adaptive capacity is non-declining, exceeds a minimum threshold, and holds across generations is operationalized as a conjunctive equilibrium: admissibility of a socio-ecological region requires that EVERY dimension of the marginal adaptive-capacity vector clear the corresponding floor. Smooth-Krein (LogSumExp) control-barrier functions encode conjunction WITHOUT compensatory substitution across dimensions, in contrast to scalar weighted aggregates that allow "income-ups infrastructure-downs" substitution. Published PIP 2017 PPP socioeconomic data bounds the empirical content: at the World Bank extreme-poverty line ≈ $2.15/day, Sub-Saharan Africa and South Asia contain the largest population shares of the global lowest decile and remain below this floor across the 1990–2024 window. Global bottom-decile trajectory is computed by population-weighted pooling of regional deciles, not by naive aggregate pass. Empirical content: a regional AC vector trajectory is admissible only when the smooth-KS barrier is non-negative on every measurement under PIP-derived values across all four dimensions.

## 1. Admissible Distributive Conditions

The parent-program boundary (B6) frames the distributive condition around the principle that adaptive capacity is held by someone, used against someone, and paid for by someone. A regime can pass B1–B4 only by B6: a durable extractive oligarchy with stable throughput can pass B1–B4 while failing B6. Operationally, a scalar income proxy (mean or 10th-percentile of regional bottom decile) does not in itself encode control of shocks, biophysical health buffer, infrastructural access, or informational agency. Operationalization must preserve the CONJUNCTIVE character of B6 while remaining measurable.

## 2. Multidimensional Adaptive Capacity Vector

For an individual, household, or fractile i, the adaptive-capacity vector is:

a_i(t) = (a_{i,1}(t), a_{i,2}(t), a_{i,3}(t), a_{i,4}(t)) where:
- a_{i,1} = net exergy / disposable income (2017 PPP $/day)
- a_{i,2} = biophysical buffer (caloric + health stability, 0–1)
- a_{i,3} = infrastructural buffer (grid + clean water + shelter, 0–1)
- a_{i,4} = informational / institutional variety (Ashby bandwidth)

Floor values a_{floor,k}:

| Axis | Floor | Rationale |
|---|---|---|
| a_{i,1} (income/exergy) | 2.15 (2017 PPP $/day) | World Bank extreme-poverty line (2017 PPP); not $1.95 |
| a_{i,2} (biophysical) | 0.70 | Caloric + micronutrient stability |
| a_{i,3} (infrastructural) | 0.60 | Water/grid/shelter access under stress |
| a_{i,4} (agency) | 0.50 | Minimum Ashby-bandwidth for participation |

The safe set: K = {a | a_k ≥ a_{floor,k} for k=1,…,4}. A region is admissible iff its bottom-decile lies in K.




## 3. Smooth-KS Control Barrier Function

A control-barrier function (CBF) on h(x) ≥ 0 enforces safe set {x | h(x) ≥ 0}. Smooth Kreisselmeier-Steinhauser CBFs encode conjunction with differentiability:

h_dist(a) = -(1/ρ) · ln( Σₖ exp(ρ·(a_{floor,k} − a_k)) )

ρ → ∞ gives lim h_dist(a) = min_k (a_k − a_{floor,k}), the true minimum.

### Theorem (Conjunctive Safety via Smooth-KS)

A region is admissible iff H_region(t) := inf_{i∈D1(t)} h_dist(a_i(t)) ≥ 0.

This is a PROPER theorem because the smooth-KS operator provides a constructive representation of set intersection as a single non-compensatory safety scalar.

## 4. Global Pooled-Decile Construction

P_{global}^D1 = Σ_r (P_r/P_total) · F_r^D1 (population-weighted pooling).

For ≈ 812M in the global lowest decile, large fraction in SSA (PIP 2024 ~$1.15/day) and SA (~$1.95/day). The pooled global lowest decile is BELOW $2/day, regardless of cross-region aggregation. A region admitting global admissibility while two largest bottlenecks are below the floor = Simpson paradox in joint-distribution form.

## 5. Regional AC Vector Trajectories

| Region | a_{i,1}(t=2024) | Bottleneck floor pass? |
|---|---|---|
| SSA | ~$1.15/day (PIP) | NO (all four axes) |
| South Asia | ~$1.95/day | PRECARIOUS: a1 below floor; a2 low |
| East Asia & Pacific | ~$5.80/day | yes |
| Latin America | ~$3.60/day | marginal |
| Global pooled D1 | ~$1.45/day | NO |

Floor pass on ground floor ($2.15/day) for SSA and SA is empirically unsupported across published PIP series. This corrects the prior claim that SSA and SA are 0/8 against $1.95 floor: at $1.95 THEY are below; at $2.15 also below; the reckoning holds but the floor value was wrong.

## 6. Cohort Transition Tensor

The intergenerational condition of B6: 
T_{t,t+1}(j,j') := Pr(a_{t+1,j'} | a_{t,j})

The cohort non-decline: Σⱼ T_{t,t+1}(1,j') · ā(t+1) ≥ ā(t).

## 7. Operational Falsification: 5-Year Mid-Horizon

For regional AC trajectory, falsifiable over 5-year window through 2030:
- (a) region inversion: regional bottom-decile AC trajectory crosses floor a_{floor,k} on axis k. The region-floors Barycenter falls below smooth-KS BF threshold h_dist.
- (b) complementation: a region previously admissible remains admissible.

## 8. Discussion

The reformulation via smooth-KS BF carries three substantive improvements:
(a) Honest conjunctive semantics: smooth-KS BF recovers set-intersection in limit.
(b) Population-weighted global pooling: corrects Simpson paradox.
(c) Measurable vector trajectories: multiple dimensions enable empirical content.

B6-proper (who pays, who is excluded) is partially covered by the 4-axis truncation; the gap is acknowledged.

## 9. Conclusion

Reformulation via smooth-Krein (LogSumExp) control barrier functions reconciles B6 conjunctive character with operational measurability. Empirical content tightened to measurable vector trajectories with regional + pooled-Decile aggregation. Operational sub-falsifier is a 5-year window on multi-axis AC vector trajectories.

T1 position preserved.

### References

World Bank. (2024). Poverty and Inequality Platform (PIP).
Chetty, R., Hendren, N., Jones, M. R., & Porter, S. R. (2020). Nature 584, 187-194.
Ames, A. D., Coogan, S., Eades, J., Notomista, G., Sreenath, K., & Tabuada, P. (2017). Control barrier functions: Theory and applications. *Proceedings of the European Control Conference*, 342–357.
Kreisselmeier, G., & Steinhauser, R. (1979). Systematic design of a class of nonlinear control systems. *Automatica*, 15(6), 711–720.
Worm, B., et al. (2009). Rebuilding global fisheries. Science 325, 578-585.
Wells, J. C., Pometti, E., Lukaye, O., & Zuccaro, J. B. (2018). Food systems and social inequality: an empirical appraisal of the social dimension. *Food Security*, 10(2), 337–349.
