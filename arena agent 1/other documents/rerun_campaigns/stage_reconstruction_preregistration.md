# Stage-map reconstruction — pre-registered plan (frozen 2026-09-01, before any run)

**Status.** This plan is the pre-registration for the stage-structured review-map reconstruction of P5 (`paper5_sampled_governance_v4.md`). It was written and dated before any simulation of the reconstruction was executed. Parameter values below are frozen; code bugs may be fixed freely, but no parameter or criterion may be changed after the first complete comparison run without recording the change as a deviation.

**Why a reconstruction.** The original stage-structured map's computational record (equations, parameter sets, solver configuration, initial histories) is not in the repository — confirmed by the turn-44 sweep (full GitHub tree, 2,935 entries; local find/grep; 0 stage-map code; the deleted `file_archive/` held 1,318 documents and 0 code files). Only the legacy exploratory response regions are on record (P5 original §3.3). Writing code that claims to be the original object would be fabrication. This plan therefore declares a **new** stage-structured plant, parameterized from the ecological literature only, coupled to the paper's own declared controller (P5 v4 §2.1, eqs. (1)–(4)), and compares its complete multiplier/trajectory record against the legacy windows **once, post hoc**. The reconstruction is a new labelled object; it is not claimed to be the object that produced the legacy numbers.

**Independence discipline.** (1) Every parameter below is sourced from the cited literature or from the paper's own declared controller — none was chosen with reference to the legacy windows. (2) The model structure is a standard delayed-recruitment stage map from the lineage the paper itself names (Gurney, Blythe, and Nisbet, 1980). (3) No parameter will be adjusted to make the legacy windows appear; a mismatch is reported as such. (4) The comparison criteria are fixed below, before the run.

---

## 1. The plant (new declared object)

Two-stage map with delayed recruitment, annual steps:

A_{t+1} = s_A A_t + s_J J_t − q E A_t,
J_{t+1} = f(A_{t−τ}),
f(A) = αA/(1+βA)  (Beverton–Holt),

with s_A = s_J = e^{−M} (single natural mortality M applied to both stages — the lumped two-stage convention), τ = age at 50% maturity (recruitment delay), and the parameterization

c = 4h/(1−h),  β = (c−1)/A_0,  α = c(1−s_A)/s_J,

i.e. steepness h and unfished abundance A_0 fix the Beverton–Holt pair; A_0 = 100 is the declared scale, matching the logistic core's carrying capacity so the paper's controller parameters keep their meaning (scale convention, not a fitted value). Surplus production at stock A is S(A) = s_J f(A) − (1−s_A)A, the discrete analogue of the paper's surplus in the deficit signal.

**Class parameter sets (literature sources; representative values inside the published ranges):**

| Class | M (yr⁻¹) | source | τ (yr) | source | h | source |
|---|---|---|---|---|---|---|
| Anchovy | 0.90 | Pauly and Tsukayama (1987); IFOP (2020) range 0.85–1.2 | 1 | Pauly and Tsukayama (1987): maturity ≈ 1 yr | 0.75 | declared default steepness convention |
| Sprat | 0.40 | Baltic SMS keyrun mid-range (ICES IBPBASH 2022); Gulf of Riga constant 0.2 (ICES 2024a) | 2 | ICES WGBFAS maturity ogives: Baltic sprat 50% mature at age 2 | 0.75 | same convention |
| Cod | 0.20 | ICES (2021): fixed M = 0.2 standard for Atlantic cod assessments | 5 | DFO (2011/037): northern cod (2J+3KL) age at 50% maturity ≈ 5.0 | 0.75 | same convention |
| Slow-stock | 0.045 | Branch (2001): orange roughy M = 0.045–0.064 | 25 | Branch (2001): maturity 22–40 yr; age at 50% maturity 25–27.5 yr | 0.75 | same convention |

The steepness convention h = 0.75 is the standard default when no stock-specific estimate is available (used across MSE practice); a declared sensitivity layer h ∈ {0.6, 0.9} accompanies the primary record. No legacy window was consulted in fixing these values.

## 2. The controller (the paper's declared object, unchanged)

The P5 v4 §2.1 sample-and-hold controller, in annual discrete form: effort E held between reviews; the institutional signal updated per year by

Z_{t+1} = Z_t + (1/τ_m)( Φ_k(q E A_t − S(A_t)) − Z_t ),  Φ_k(s) = max{0, (1/k)log(1+e^{ks}) − (log 2)/k + δ},

and at each review the projected forward-Euler command (eq. (4)) with the effort law F_B, contemporaneous exact assessment Ẑ = Z at the review instant. Controller parameters are the logistic hold-map core's declared values, unchanged: r-class scale conventions aside, q = 0.001, E_max = 30, η = 0.914, Δ_ref = 1, δ₀ = 0.01, Z_ref = 1, τ_m = 5, k with δ = (ln 2)/10. The extractive (mobilising) channel is the primary object, matching the paper's studied controller; the protective channel is computed as a secondary record with the paper's opposite-sign response law. A declared catchability-sensitivity layer q = 0.1 accompanies the primary q = 0.001 (the paper declares no q for the stage map; both are reported, neither was chosen against the windows).

## 3. Records computed

1. **Multiplier record:** review-map Jacobian M(T_r) = DP_{T_r}(X*) by central finite differences (step 1e−6, declared derivative construction), state X = (A, J, A_{t−1}…A_{t−τ}, Z, E); spectral radius ρ(T_r) on the integer grid T_r ∈ {1, …, 50} yr (annual internal steps — the reconstruction is a discrete map, so the scan is finite-grid by construction); crossings of the unit circle flagged with eigenvalue character (real/complex) and crossing direction.
2. **Trajectory classification:** 2000 review-steps from the declared initial condition (plant at the unfished equilibrium, memory filled, Z = δ, E = 0.5E*); tail = last 500 review-steps; classification by relative tail standard deviation of A: persistent oscillation ≥ 2%, weak response in [0.1%, 2%), convergence < 0.1%. Reported per class and T_r.
3. **Diagnostics:** dominant spectral periods of A and E tail series (FFT); effort and biomass percent excursions (max−min)/mean over the tail; 30% multiplicative assessment-error robustness (Ẑ_n = 1.3·Z at reviews) re-running the classification at each class's window.
4. **Comparison** against the legacy windows, fixed criteria below.

## 4. Comparison criteria (fixed before the run)

Legacy windows (P5 original §3.3): anchovy persistent oscillation at T_r ≈ 3–4 yr with weak response at 2 yr and annual convergence; sprat persistent oscillation at T_r ≈ 6–12 yr; cod convergence for every T_r ∈ [1, 20]; slow-stock oscillation over part of [1, 20] with convergence at longer intervals and transition brackets ≈ 30–50 yr; diagnostic peaks ≈ 4 yr (biomass) / 12 yr (effort) for anchovy and ≈ 8 yr / 60 yr for sprat; effort excursions 80–240% vs biomass 1–2%.

A criterion MATCHES if the reconstruction's classification agrees within the integer grid (e.g. persistent oscillation at T_r = 3 or 4 for anchovy; convergence for every integer T_r in [1, 20] for cod). Peaks and excursion magnitudes are reported as consistency checks, not match criteria (the legacy amplitudes carry an unrecorded convention — half-range versus peak-to-peak — so a threshold test is not well-defined). The verdict is reported per criterion as MATCH / MISMATCH / NOT-TESTED, once, with no re-run after parameters are frozen.

## 5. Provenance statement (to be printed in the paper and repository)

"The original stage-map record is not in the repository. The record below is a new reconstruction declared in the pre-registration of 2026-09-01: a delayed-recruitment two-stage Beverton–Holt map parameterized from the cited literature, coupled to the paper's declared controller. It is labelled as a new object and is not claimed to be identical to the original. The legacy exploratory windows keep their exploratory status; a match is a consistency statement for the legacy record, and a mismatch adjudicates nothing about the legacy numbers, whose generating object remains unavailable."
