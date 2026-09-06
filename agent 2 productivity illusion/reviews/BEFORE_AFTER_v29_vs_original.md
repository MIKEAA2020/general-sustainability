# Before / After — Latest Revision (v29) vs. Original ECOMOD-26-1191 Submission

This note compares the **last (current) revision** — `data/revisions/IMPLEMENTED_revision_ECOMOD_v29.md` — with the **original submission** (`/tmp/ecomod_full.txt`, re-extracted from `ECOMOD-26-1191.pdf`). The purpose is to make explicit what changed and why. Section numbers on the "after" side refer to v29 / v30.

**Note on versions.** A following revision (v30) has since been produced; the changes it introduces are *referencing and supplementary-handling only* (nine companion manuscripts cited by DOI, a units-reconciliation note added to §2.1, and a "Supplementary material" statement). The scientific content compared here is identical between v29 and v30. Where a difference is a v30-only change it is marked **(v30)**.

---

## 1. High-level summary

| | Original submission | v29 (current revision) |
|---|---|---|
| **Title** | *Overcoming the productivity illusion with delayed feedbacks and emergent carrying capacity* | *Emergent Carrying Capacity, the Biocapacity Ratio, and the Productivity Illusion: Deficit-Driven Collapse in a Delayed Coupled Human–Environment Model* |
| **Abstract** | ~800-word essay-style | 300-word standalone (word count as declared; ≤315) |
| **Keywords** | carrying capacity; biocapacity; ecological footprint; overshoot; delay differential equations; environmental debt; stability boundary; productivity illusion | carrying capacity; ecological footprint; biocapacity; time delay; ecological debt; sustainability; delayed feedback |
| **Section structure** | 6 sections (Intro, Model Development, Analytical Results, Numerical Simulations, Discussion, Conclusion) | 14 sections (adds Assumptions, Falsifiable Predictions, Presentation, Numerics/Verification, Demonstration, Model Scope, Limitations, and a dedicated analytic core) |
| **Central result framed as** | single "productivity illusion" narrative | an operating boundary `R_B = 1`, a leading-but-non-causal `R_A = 1`, and a narrow, deficit-bounded illusion |
| **Empirical status** | parameters illustrative; delays asserted | τ_g field-banded from independent studies; scope declared "conceptual, not a forecast"; restrictions on the 1961–2022 series |

---

## 2. Title

- **Before:** *Overcoming the productivity illusion with delayed feedbacks and emergent carrying capacity*
- **After:** *Emergent Carrying Capacity, the Biocapacity Ratio, and the Productivity Illusion: Deficit-Driven Collapse in a Delayed Coupled Human–Environment Model*

The new title (i) puts "Emergent Carrying Capacity" first, so the reader knows immediately that carrying capacity is the *output* of the model rather than an input; (ii) names the **biocapacity ratio** and the **productivity illusion** — the two concepts the reviewer should focus on; and (iii) states the **mechanism** (deficit-driven collapse) and the **tool** (a delayed coupled human–environment model).

## 3. Abstract

- **Before:** ~800-word essay-style abstract, written in continuous prose, leading with the debate and the two-timescale framing. It used the phrases "Hopf," "imaginary-axis," and "linear-stability" style language in body and reported the delay threshold as "approximately 80 yr."
- **After:** **300-word standalone abstract** (≤315), designed to be self-contained and jargon-free in the body. It states three results in plain technical terms and restores short technical signposts:
  - the one-parameter equilibrium family `P = B(A)/e` (no isolated attractor) and that every interior point is **monotonically unstable** (a positive real eigenvalue for every delay, no imaginary-axis crossing);
  - the **operating boundary `R_B = 1`** (footprint = total biocapacity) and the flow-yield ratio **`R_A = 1`** as a leading but non-causal signal;
  - the **productivity illusion** as real but **narrow** (a ~five-year window for small initial deficits, vanishing beyond modest overshoot).

The abstract now also **distinguishes biocapacity (a flow) from the capital stock** explicitly, and it does not use "eigenvalue/Hopf/imaginary-axis" language in the body (those appear only in the body of the paper, §4.3/§8). The mathematics is kept as LaTeX in `supplementary/ABSTRACT_submission.tex` for the submitted manuscript and as backtick-math in the `.md`.

## 4. Keywords

- **Before:** carrying capacity, biocapacity, ecological footprint, overshoot, delay differential equations, environmental debt, stability boundary, productivity illusion
- **After:** carrying capacity; ecological footprint; biocapacity; time delay; ecological debt; sustainability; delayed feedback

The new set adds **time delay** and **delayed feedback** as primary index terms (the model's central tool) and **sustainability**, and drops "stability boundary" (which is a result rather than a topic).

## 5. Structure and coverage

| Original | v29 |
|---|---|
| §1 Introduction | §1 Introduction (orchard framing, elevator analogue, literature) |
| §2 Model Development (2.1 dynamics, 2.2 biocapacity/carrying-capacity, 2.3 population lag, 2.4 ecological debt, 2.5 policy) | §2 Model formulation (2.1 variables & units, 2.2 governing equations) · §3 Assumptions (nine explicit modelling choices) |
| §3 Analytical results (3.1 steady state, 3.2 linear stability) | §4 Analytic results (4.1 MSY/emergent ceiling, 4.2 fixed-liability threshold, 4.3 stability & vicious cycle, 4.4 dimensionless groups, 4.5 macro-ratio safe-operating space) |
| §4 Numerical simulations (stylized) | §5 Results: principal claims · §8 Numerics, verification, well-posedness · §10 Demonstration |
| §5 Discussion | §12 Discussion (12.1 structural properties & negative results, 12.2 recovery dynamics, 12.3 robustness) |
| §6 Conclusion | §14 Conclusions |
| — | §6 Falsifiable predictions (8 predictions) · §7 Presentation · §9 Policy extensions · §11 Model scope · §13 Limitations |

Two additions are worth flagging as substantive, not just reorganization:

1. **§6 Falsifiable predictions (eight).** The original reported results; v29 states them *as testable hypotheses* (e.g. prediction 6 ties the recovery/collapse switch to a field-banded regeneration-lag interval ≈18–20 yr). This is a direct answer to the reviewer's "self-referential" and "too assertive" concerns.
2. **§13 Limitations and §11 Model scope.** v29 declares the model "conceptual / stylised... not a forecast," states the NFA data limitations, and gives the honesty caveats (fit-defect disclosure, interval discipline) and the information-layer limit. The original did not have these.

## 6. Scientific content changes

These are the substantive differences, most of which respond to the two reviewer themes of *clarity/rigour* and *empirical grounding*.

### 6.1 The operating boundary: `R_B = 1`, not a single stability locus
- **Before:** the paper's analytic results centred on the steady state and linear stability of the constant-parameter version, and on the two-delay interaction threshold.
- **After:** v29 identifies the **biocapacity ratio `R_B = 1`** as the operating boundary, and shows (from the deficit identity `dA/dt = (B̃ − E)/b_G`) that `dA/dt < 0 ⟺ E > B̃`. The flow-yield ratio **`R_A = 1`** is shown to be *necessary but not sufficient* — a leading, non-causal signal — and the **flow share `ψ = bA/B`** is identified as the "master parameter" separating the two. This is a monitoring result (what a policy-maker can watch) that was not present in the original framing.

### 6.2 The productivity illusion is narrow and deficit-bounded
- **Before:** the illusion was presented as a general or even dominant outcome ("technology can temporarily mask environmental decline").
- **After:** §10 (Demonstration) **quantifies** it: the B-rises-while-A-falls window is ~5.4 yr at deficit `E − b₀A₀ = 0.06`, collapses to zero at deficit ≈0.075 (≈15 % of the initial flow yield), and is converged under RK4. §13 states it is "small-deficit only, not generic" and §11 gives the information-layer reason it is not identifiable contemporaneously. This is a strengthening of the original claim by bounding it, and it answers the reviewer's concern about over-claiming.

### 6.3 The stability result is recast as structural, not Hopf
- **Before:** the original reported a delay-based instability (the "80 yr threshold").
- **After:** v29 shows that on the constant-parameter subsystem there is **no isolated interior attractor** — the equilibrium set is the one-parameter family `P = B(A)/e`, every interior point is **monotonically unstable** (leading eigenvalue ≈ +0.62, no imaginary-axis crossing), and the onset is a **structural vicious cycle** rather than a delay-ratio Hopf. The §4.3 classification explicitly states the fast–slow Hopf classification does not *transfer* to this subsystem, and the "baseline sits at a knife-edge" (`χ = 1`) is disclosed. The original did not establish (or distinguish) this.

### 6.4 Regime-conditionality of the MSY and the fold
- **Before:** the interior maximum-sustainable-yield and the fold/saddle-node were asserted as general.
- **After:** §4.1/§4.2 state that `A* < A_max` holds **only in the capital-dominated regime** (`b_G ρ > b`, `ψ → 0`), and that at the baseline (`b_G ρ = 0.04 < b = 0.5`) `B(A)` is monotone and the stable object is the boundary `A_max`. The fold is "regime-scoped" and **must not be conflated with the `τ_g` cliff** (which is a basin-boundary crisis with no critical-slowing-down precursor). This is a genuine correction and sharpening.

### 6.5 Empirical grounding of the regeneration lag
- **Before:** the delays were asserted as modelling features.
- **After:** §8 gives an **operational definition** of `τ_g` (time to ~50 % of pre-disturbance productive capacity), a **field-derived band** (Poorter et al. 2016; Poeplau et al. 2011; Hutchings & Reynolds 2004; Neubauer et al. 2013), a fine sweep **resolving an ≈18–20 yr transition band**, a demonstration that the cliff is **`τ_p`-independent** across a 4× range, and a **calibration outlook/honesty caveat** stating it is literature-banded, not fitted. This is the main empirical-grounding addition.

### 6.6 NFA data limitation and the 1961–2022 statement
- **Before:** "The global data from 1961–2022 are consistent with this interpretation: biocapacity grew modestly while ecological overshoot persisted, suggesting that technology has been outpacing degradation." (Read as evidence.)
- **After:** §11 states the accounts are **conservative** (biocapacity likely overstated, overshoot understated) and that the series is "**consistent with** the illusion reading but **does not demonstrate it**," i.e. it is a *qualified observation*, not evidence. This is the direct response to the reviewer's point (d). The NFA literature itself is cited in §7 (Wackernagel & Rees 1996; Wackernagel et al. 2002; Borucke et al. 2013; Lin et al. 2018; Blomqvist et al. 2013; Giampietro & Saltelli 2014; van den Bergh & Grazi 2015; Galli et al. 2016).

### 6.7 Clarity, assumptions, and limits
- **Before:** the assumptions were distributed across the model-development section and not enumerated.
- **After:** §3 enumerates **nine explicit modelling choices** (logistic regeneration; additive flow+capital growth; held-constant per-capita footprint; deficit-driven immediate depletion; demographic delay; `K` algebraic; debt accrues only in overshoot; degradation erodes surviving yield; bounded technology), including the **stated reason for each** (e.g. why `e` is constant — to isolate the stock–flow–demand feedbacks; why degradation is multiplicative — it makes the debt-compounding asymmetry a theorem). §13 lists the limitations (boundary equilibrium, one-sided stability, small-deficit-only illusion, parameters-not-estimated, `η → 0` singular case). §12.1 tabulates the phenomena that are **absent** (critical slowing down before the cliff, hysteresis, endogenous limit cycles, Allee rescue threshold) and why each is structural.

### 6.8 Robustness record
- **Before:** qualitative statements about basin shrinkage.
- **After:** quantitative robustness (recover fraction robust to `b_G` over 3×; leading eigenvalue independent of `ρ`; coarse-vs-fine grid dependence bounded; the fast–slow reduction valid only for `ρ ≫ r`, so the full `D(s)=0` is always used; `τ_p`-independence of the cliff). Report the recover fraction on the fine mesh only.

### 6.9 Referencing of companion work
- **Before / v29:** a single generic entry — *"Abaee, A. Various companion manuscripts. Cited where their methods or framing are used (compensatory aggregation; typed flux ledgers; incomplete-observation viability; mobilising vs. protective controller sign; negative-certificate and interval-discipline methods; surplus-production forecast scoring)."*
- **v30 (current):** that entry is replaced by **nine full references** with titles and Zenodo DOIs (all `10.5281/zenodo.<id>`), each carrying the method-attribution (e.g. *The Limits of Compensatory Aggregation…* → compensatory aggregation; *Typed Flux Ledgers and Depletion Arithmetic…* → typed flux ledgers; *An Obstruction Calculus for Viability under Incomplete Observation* → incomplete-observation viability; *Delay-Induced Regime Change…* → mobilising vs. protective controller sign; *Robust viability of the 2J3KL limit reference point…* → policy scoring, negative-certificate and interval-discipline methods; *Does a surplus-production ladder…* → surplus-production forecast scoring). This makes the companion methods findable and separately citable.

---

## 7. What did *not* change (continuity)

- The orchard / elevator framing and the core coupled DDE structure (two delays, ecological debt, degradation channel) are retained.
- The weak- vs. strong-sustainability framing and the conclusion that the two positions are valid at different timescales are retained (now stated via `R_A`/`R_B` and the flow share).
- The National Footprint Accounts data source remains the empirical anchor, now with its limitations and its non-evidential status made explicit.

## 8. Summary of the value added by the revision

The revision moves the paper from a *descriptive* essay ("here is a model and an intriguing result") to a *structured, falsifiable* framework with: an explicit operating boundary (`R_B = 1`) and a leading-but-non-causal signal (`R_A = 1`); a bounded, quantified productivity illusion; a regime-scoped MSY/fold; a field-banded, honest `τ_g`; an explicit model-scope and limitation section; and a robustness record. Where the original over-claimed (the 1961–2022 series, the generality of the illusion, the general MSY), the revision qualifies and bounds the claim, and it converts the model's interpretive results into testable predictions.

The two reviewer concerns the revision most directly addresses are **rigour/clarity** (nine enumerated assumptions, one-sided stability, per-equation assumptions, honesty caveats, disclosure of the knife-edge and fit defects) and **empirical grounding** (field-banded `τ_g`, NFA data limitations, the 1961–2022 qualification, and the specified and honest empirical programme in §11).
