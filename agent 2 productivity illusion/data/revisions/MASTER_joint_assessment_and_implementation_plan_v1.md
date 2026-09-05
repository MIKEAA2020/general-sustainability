# MASTER JOINT ASSESSMENT & IMPLEMENTATION PLAN
## ECOMOD-26-1191 — the single consolidated source of truth across every audit and every joint assessment

**What this is.** This is the final, master document. It folds together, and adjudicates, **every**
independent critique of the manuscript produced in this whole exercise — the two original model audits
(Claude, Grok), the human-reviewer comments, my own reviews/upgrades/findings register/root-cause
analysis, the joint assessments that reconciled them, **and the two additional orchard/hens-audit
analyses** (Grok's and Claude's audits of my orchard response, plus my own orchard/hens analysis).
It re-verifies nothing that wasn't already verified line-level; it **consolidates**, **reconciles**,
and — most importantly — converts the accumulated critique into a **single, sequenced
implementation plan** an author can execute. Where two sources genuinely disagree, those forks are
listed with a decision and a default.

**Sources folded in:** `ECOMOD-26-1191_review.md`, `ECOMOD-26-1191_proposed_upgrades.md`,
`ECOMOD-26-1191_findings_register.md`, `response_to_human_reviewer.md`, `grok audit ecomod.txt`,
`claude audit ecomod.txt`, `profound upgrades.txt` (the grok:/claude: meta-audits), `human
reviewer.txt`, `evaluation_of_model_audits.md`, `ECOMOD_26_1191_root_cause_analysis.md`,
`JOINT_assessment_all_sources.md`, `JOINT_root_cause_assessment.md`,
`JOINT_root_cause_assessment_ADDENDUM.md`, `JOINT_root_cause_assessment_FINAL.md`,
`JOINT_orchard_analogy_assessment.md`, `grok, claude my orchard.txt` (orchard round 1: the two
audits of my orchard response), **and `orchard.txt` (orchard round 2: my earlier orchard/hens
response, plus Claude's and Grok's *second, deeper* orchard audits)**. **Part 11 folds in the two
round-2 audits and refines the recommendation — see the note below the verdict.**

**Abbreviations:** **E** = "equations primary" (keep Eqs. 1–8, rewrite prose); **N** = "narrative
primary" (keep the contributions, change the failing equations); **C** = "conceptual model" epistemic
label. **S0** = the constant-parameter subsystem (α = 0); the full model is three delayed states.
**RC1–RC6** = Claude's root causes.

---

## PART 1 — THE DEFINITIVE VERDICT (stable across every source; nothing reverses it)

> **The manuscript's algebra is sound; its narrative is not implemented by its equations; and the
> deepest cause is that the ontology of the environmental stock M (RC1) was never fixed, which makes
> the headline decomposition B = b·M non-identifiable and leaves a depletion term that mis-books
> biocapacity and depletion in two different "books" (B2). The fix is Paper N′ + C with a separable
> A and b — and, per the round-2 audits (Part 11), best realised as a unified stock–flow model
> (1‴) that contains both the orchard (flow-yield) limit and the manuscript's increment-harvest
> limit.**

This verdict is the fixed point. Every joint assessment produced in this exercise converges on it,
and the final orchard analysis *strengthens* (never reverses) it. Everything below is either
(a) the supporting detail, (b) a recommendation the audits did make, or (c) a live fork awaiting the
author's decision. **NOTE:** Part 11 (the round-2 analyses) refines the paper choice from "Paper N
(orchard-only)" to **"Paper N′ + C (unified stock–flow)"**, which is a *generalisation* of Paper N and
of the manuscript's own equations — see Part 11 for the adjudication of the Grok-vs-Claude conflict.

**The two strongest results now available (both verified):**
1. **A classification of which single delay destabilises the system, as a function of
   χ = q/(ρ−2q):** χ > 1 (Λ > 0) ⇒ **τₘ-only** Hopf (ω = r√(χ²−1), τₘ* = arccos(−1/χ)/ω); χ < 1
   (Λ < 0) ⇒ **τₚ-only** Hopf (ω = r√(1−χ²), τₚ* = arccos(−χ)/ω); χ = 1 (Λ = 0, i.e. ρ = 3q) ⇒ the
   two-delay boundary s = π/ω, ω = 2r·cos(ωd/2) → s ≈ π/(2r) ≈ 78.5 yr at d → 0. *The sign structure
   is exact (from the |Q| = |P| elimination); only ω*, τ* are O(r/ρ) approximate.*
2. **A proof that the "productivity illusion" is necessarily transient:** d ln B/dt = d ln b/dt +
   d ln A/dt, with d ln b/dt bounded (technology saturates) and d ln A/dt unboundedly negative under
   the stock-liquidation cycle.

**The corrected sign rule (I had it reversed in three of my docs).** Λ > 0 (χ > 1) ⇒ τₘ-only;
Λ < 0 (χ < 1) ⇒ τₚ-only. Scenario B: χ = 1.643 ⇒ τₘ*, τₘ ≈ 85.4 yr (paper 83). ρ = 1.6: χ = 0.833 ⇒
τₚ*, τₚ ≈ 231 yr (paper ~225).

---

## PART 2 — CONSOLIDATED, CORRECTED ROOT-CAUSE TABLE (the spine)

The three taxonomies (Grok's 4, Claude's 6, my 5) are **nested, not competing**; everything nests
inside Claude's six. Deepest first.

| Root | Correct resolution (global, not a patch) | Kills |
|------|------------------------------------------|-------|
| **RC1 — ontology of M never fixed** (deepest) | Define **A** (ha) separately from **b = B/A** (gha·ha⁻¹); B = b·A (gha); E = e·P (gha); D = ∫(E−B)₊dt (gha·yr); γ in ha·(gha·yr)⁻¹. Non-dimensionalize. | units 3-way clash, γ = 1, B2, productivity-illusion identifiability |
| **RC2 — timescale inversion is generative** | Keep ρ large but present **χ = q/(ρ−2q)** as the organising parameter; report departure from the reduced picture as ρ/r falls. | false "a₁₁ < 0", the knife-edge, the "≈80 yr" mis-explanation |
| **RC3 — two incompatible equilibria coexist** | Add **−ηD** in the base model → D* = (f−1)B*/η; or use K = B/e. **Treat η as primary, not a robustness check.** | B10, B11, Scenario-D "locally stable" |
| **RC4 — narrative-first, no claims ledger** | Decide **Paper N′ + C** (unified stock–flow); add a claims ledger; mechanism↔equation map. | the whole B2–B5 regeneration |
| **RC5 — verification asserted, not exhibited** | Repository with solver, full scenario table, A→0 treatment, step-size convergence, spectral method; every "verified" claim carries its protocol + any discrepancy. | "verified to machine precision," my §1.5 |
| **RC6 — process optimised for attribution** | Restructure as a decision document; attribution in an appendix. | my attribution bookkeeping |

**Appendix-equivalence map (my roots → Claude's):** 1→RC4; 2→RC1; 3→RC2(+); 4→RC5/numerical;
5→RC5. Grok's four (stock–flow/units; additive tech unreachable by debt; delay placement swapped;
claims asserted for a model the sim lacks) all sit beneath Claude's RC1/RC3/RC4/RC5.

---

## PART 3 — THE COMPLETE FINDINGS, CONSOLIDATED (what must be fixed and why)

Layer 1 — **units & accounting** (Part A of `JOINT_assessment_all_sources`): the manuscript is
internally self-consistent under its own stated convention, **but** this conflicts with GFN's
convention and is never stated; γ = 1 couples an annual flow to a land stock one-for-one (this *is*
B2). **Fixed verdict:** with A/b separation, **GFN convention is mandatory** and **D is in gha·yr**
(the reviewer's "(b)" is correct given the fix). The γ = 1 "housekeeping" point is a *symptom* of RC1,
not the diagnosis.

Layer 2 — **model–narrative inconsistencies** (the heart, B2–B12):
- **B2** subtracts the full footprint E, not the deficit (E−B). [The orchard analogy makes this the
  single constraint. → deficit-driven term `(E − σbA)₊/V`.]
- **B1/Routh–Hurwitz**: zero-delay condition is **a₁₁ < r** (trace), det = r·ρ·M*/M_max > 0
  identically — **not** a₁₁ < 0. (Corrects my own prior review.)
- **B3/B4** delay placement swapped vs. prose; either match the prose or rewrite it. (Under the
  analogy, τ_m moves to **recruitment** τ_g.)
- **B5** additive b = b₀e^{−αD}+T floors productivity at T ⇒ the "debt compounds, technology
  saturates" claim is false; it is a theorem only under multiplicative b = (b₀+T_b)e^{−αD}. **But**
  under pure liquidation a D→b channel is **optional** (Claude), so this is demoted from central to
  a conditional.
- **B8/B10/B11** ρ ≈ 1.5 yr⁻¹ implausible; "locally stable" asserted for Scenario D; "both delays
  required" asserted for a model with no interior equilibrium. → no local-stability claim for D;
  add the sustainable-with-lags row; state ρ justification.
- **B12** the balanced-with-lags Hopf is *inferred* from Eq. (13), not *shown*. The gap is larger
  than first stated.

Layer 3 — **the no-equilibrium problem (RC3)**: the full overshoot model has **no** interior
equilibrium (E* = (e/r_opt)B* > B* ⇒ dD/dt > 0 forever). Fix: **−ηD** in the base model (D* =
(f−1)B*/η) or K = B/e. **η is not a robustness check; it decides whether an equilibrium exists.**
(η → 0 is the singular collapse.)

Layer 4 — **the delays / two-delay theorem**: only S0 is 2-D; the fast–slow scalar reduction
(χ) is valid only where a₁₁ ≤ 0; in the dangerous band use the full 2-D transcendental equation and
the M-mode can oscillate. The "≈80 yr" boundary is *closed-form* (χ = 1) and is *not* the Hutchinson
continuation. **Hutchinson (1948)** is the correct ancestor if τ_p sits on K or P.

Layer 5 — **Half-Earth**: cap the human-available flow at σB; compute debt and **Ω against the
allocated half** `(E − σbA)₊`, not full B; state whether lags/T(t) are on. Then "Ω = 0.575 / D = 0"
is impossible.

Layer 6 — **the 1961–2022 sentence** is unsupported and over-interpreted; GFN accounts are
conservative (GFN itself states biocapacity likely overestimates, the footprint underestimates, and
the accounts miss soil erosion, deforestation, groundwater depletion).

Layer 7 — **didactics / honesty**: symbol table; assumption-before-equation; feedback diagram with a
**switch** (fruit harvest vs. capital liquidation); thought-experiment label; parameter justification
(ρ large; γ, α, τ lumped); NFA data limitations; **Euler/clamping and K → 0** because liquidation can
drive the stock through zero in one step.

---

## PART 4 — THE ORCHARD/HENS ANALOGY: FINAL JOINT POSITION (the new work)

This is the piece the **two audits** (`grok, claude my orchard.txt`) **and** my own response jointly
settle. The mapping **number of trees × average productivity = total productivity** maps to
**A × b = B**, and it is a correct, sharp instance of RC1. I re-derived every load-bearing claim —
**all verified.**

**Confirmed algebra.**
- `γ = 1/V` (V = salvage value, standing biomass ÷ annual production, 20–100 yr) — measurable.
- Emergent threshold `A_c(E) = [(ρ+b/V) − √((ρ+b/V)² − 4ρE/(V·A_max))]·A_max/(2ρ)` (verified vs. the
  quadratic root), with saddle-node `E_sn = V·A_max(ρ+b/V)²/(4ρ) ≥ b·A_max` (AM–GM) — an MSY-like limit.
- Self-sustaining vicious cycle condition **`(2f−1)ν > 1`, ν = b/(ρV)**; equivalently
  `a₁₁ = −ρ + (2f−1)b/V > 0`. Estimable; the dangerous band is not exotic.
- Yield-technology rebound: `A* = A_max[1 − (f−1)b/(ρV)]`, `dA*/db = A_max(1−f)/(ρV) < 0` for f > 1.
- `det = r·ρ·A*/A_max > 0` survives; zero-delay stability again a₁₁ < r.
- Deficit term `∂(−(E−bA)/V)/∂A = +b/V > 0` (positive feedback); gross form `∂(−γE)/∂A = 0` (none).

**The joint decisions (from Part 7–8 of `JOINT_orchard_analogy_assessment.md`).**
1. Depletion is **deficit-driven**, immediate, `(E − σbA)₊/V`; gross `γE` retained only as a named
   "land-conversion / biomass-harvest" supplement variant.
2. Collapse threshold is **emergent** A_c(E) (saddle-node E_sn) → **drop the Allee term**.
3. The vicious cycle is **real positive feedback**, with two amplifiers: stock-liquidation (cut A)
   and yield-degradation (cut b). The paper **misattributes it to the logistic hump** (M_max/2
   fallacy) instead of the stock-dependence of the deficit.
4. **τ_m → recruitment τ_g** ≈ 20–80 yr (forest maturation / soil formation); τ_p ≈ 25–30 yr
   (generation length) — answers reviewer (e) on empirical lag justification.
5. **D is redundant** under pure liquidation (D = V × cumulative trees killed, already carried by A);
   default is to **drop D** → the model is genuinely **2-D**, resolving **B1**, with
   `b = b₀ + T(t)`. Keep D only as a documented separate *degradation* channel (soil fertility loss).
   **Multiplicative debt becomes optional.**
6. **Non-smoothness / one-sided stability** at E = B (both audits agree): sustainability is a
   **boundary of the deficit regime**, not an interior point; report one-sided stability or use a
   smooth ramp of stated width.
7. Recompute the **characteristic equation, table, and all figures**; organise the stability chart by
   `(f, ν, rτ_g, rτ_p)`; the fast–slow scalar reduction is valid only where a₁₁ ≤ 0.
8. Frame the reconciliation as **two masks**: technology (B rises as A falls) vs. liquidation
   (E steady as A falls).

**What the analogy does NOT change:** the Λ/χ Hopf classification (orthogonal to gross-vs-deficit);
the core verdict; and it is the **strongest** argument for **Paper N**, not E — because the vicious
cycle cannot survive gross depletion.

---

## PART 5 — RECONCILIATION OF ALL JOINT ASSESSMENTS (nothing contradicts; each adds one thing)

| Joint assessment | Role / unique contribution | Status |
|------------------|----------------------------|--------|
| `JOINT_assessment_all_sources.md` | Union of Claude + Grok + human reviewer + my reviews; the units resolution; the B2–B12 model–narrative register; Part G coverage map | **superseded** by FINAL + MASTER |
| `evaluation_of_model_audits.md` | Claim-by-claim adjudication of the two model audits; **catches my own a₁₁<r and O(1.5yr) errors**; one genuinely new flaw | **confirmed** |
| `JOINT_root_cause_assessment.md` | Reconciliation of the three root-cause taxonomies; consensus list | carries the **wrong Λ sign** |
| `JOINT_root_cause_assessment_ADDENDUM.md` | A1–A7 (Claude), B1–B5 (Grok), C1–C3 (mine) | **folded into FINAL** |
| `JOINT_root_cause_assessment_FINAL.md` | The authoritative root-cause document: head-line results, taxonomy, Part 10 orchard verification | **authoritative root-cause** (Λ sign correct) |
| `JOINT_orchard_analogy_assessment.md` | The two orchard audits + my orchard response; Parts 7–8 add the remaining points & the joint decisions | **authoritative orchard**; supersedes FINAL Part 10 |
| `orchard.txt` (round 2) | My orchard/hens response + Claude's **unified stock–flow (1‴)** + Grok's orchard-only defence | **extended by** this MASTER's Part 11; yields Paper N′ |

**Guarantee.** After this master, **no point from any source — the two model audits, the human
reviewer, the two meta-audits, my own reviews/upgrades/findings/root-cause, the joint assessments, the
two orchard audits, and the granular findings in the findings register / all-sources assessment —
remains unincorporated.** Every item is either resolved, assigned to a fork, explicitly deferred, or
carried in **Part 12** (the line-level completion pass).

---

## PART 6 — LIVE FORKS: the authorial decisions (each with a default)

These are the points where two sources *genuinely* disagree and the author must choose. The default
is the one the analogy and the evidence favour.

| # | Fork | Option A | Option B | Recommendation / default |
|---|------|----------|----------|--------------------------|
| F1 | **Paper E vs Paper N** | keep Eqs. 1–8, rewrite prose | keep contributions, change failing equations | **Paper N′ + C** (unified stock–flow); E would gut the thesis |
| F2 | **Depletion term** | gross `γE` | deficit `(E−σbA)₊/V` | **deficit** (with gross as a supplement variant) |
| F3 | **Hard max vs smooth ramp** | hard `max(E−B,0)` | smooth ramp of stated width | **hard max**, but state one-sided/boundary stability |
| F4 | **Keep D or drop it** | keep D, route into b (multiplicative) | drop D → model is 2-D | **drop D** (resolves B1; keep only as a documented degradation channel) |
| F5 | **τ_m home** | lagged depletion (Grok) | recruitment τ_g (Claude) | **recruitment τ_g** (liquidation is immediate) |
| F6 | **Technology–debt law** | additive b = b₀e^{−αD}+T | multiplicative b = (b₀+T_b)e^{−αD} | **multiplicative** if D kept; moot if D dropped |
| F7 | **Equilibrium well-posedness** | K = B/e (true carrying capacity) | add −ηD (D* finite) | **−ηD** with K = B/e as the f = 1 case |
| F8 | **Units convention** | manuscript's own (gha) | GFN (D in gha·yr) | **GFN** (mandatory under A/b separation) |
| F9 | **Allee threshold** | impose an Allee term | emergent A_c(E) | **emergent** (drop Allee) |
| F10 | **Stock model** (round 2) | orchard-only, deficit-liquidation (Grok) | unified `B = bA + b_G G(A)` (Claude) | **unified (1‴)**; orchard as the ψ→1 didactic case |

---

## PART 7 — IMPLEMENTATION PLAN (sequenced, executable)

> **Single global repair, not a list of patches.** One equation and one new empirical parameter
> implement the deficit mechanism, the vicious cycle, the emergent threshold, the delay-dependent
> collapse, the yield-technology rebound, and the liquidation mask, while removing one state variable
> and two ad hoc ingredients. This is the version of the paper the orchard was always describing.

**Step 0 — Decide the forks (Part 6). Do this first; everything else depends on it.** (Recommended
defaults: F1 = N+C, F2 = deficit, F3 = hard max + boundary caveat, F4 = drop D, F5 = τ_g, F6 =
multiplicative, F7 = −ηD, F8 = GFN, F9 = emergent.)

**Step 1 — Rewrite the environmental (stock) equation (Eq. 1) — unified stock–flow form.**
```
G(A) = ρA(1 − A/A_max)                        (recruitment / regeneration)
B    = b·A + b_G·G(A)                         (biocapacity = flow-yield + increment)
dA/dt = G(A(t−τ_g)) − (E(t) − σ·b·A(t))₊ / b_G   (1‴)
```
with A in ha; `b = b_A` in gha·ha⁻¹ (flow yield per ha, e.g. crop/grazing); `b_G` = value of standing
stock in gha·yr (the orchard's V); γ = 1/b_G; the `max` taken on the deficit (demand met from flow,
then increment, then capital); and the gross `γE` form moved to a supplement as the
"land-conversion / biomass-harvest" variant (the ψ → 0 limit). Be explicit about the **lag switch**:
the deficit term is immediate; the delayed response is **(recruitment) τ_g**, and τ_p is the
demographic lag. Add the **flow-share `ψ = bA*/B*`** as a control parameter and state its regime
dependence (ψ → 0 = manuscript's increment picture; ψ → 1 = the orchard). **This is the
round-2 refinement (Part 11); it supersedes the earlier orchard-only `(1″)`.**

**Step 2 — Decide the debt/technology treatment.**
- If **drop D** (default): the model is genuinely 2-D (A, P); `b = b₀ + T(t)`. The productivity
  illusion survives as "B = bA rising while A falls"; B1 resolved. State the weak/strong
  sustainability reconciliation as **two masks**.
- If **keep D**: define it explicitly as a separate *degradation* channel (soil-fertility loss on
  continuously cropped land) and use **multiplicative** `b = (b₀+T_b)e^{−αD}` so the "technology
  saturates, debt compounds" claim is a theorem.

**Step 3 — Make the equilibrium well-posed.** Add `−ηD` in the base (demographic) equation →
`D* = (f−1)B*/η`; treat **η as a primary parameter** (it decides whether an equilibrium exists, not a
robustness check). K = B/e as the f = 1 (true carrying-capacity) special case.

**Step 4 — Re-derive the analytic core for the new S0.**
- Existence: sustainable (e = r_opt) ⇒ A* = A_max (zero harvest drain); overshoot (f > 1) ⇒
  `A* = A_max[1 − (f−1)b/(ρV)]` if `(f−1)b/(ρV) < 1`; fixed-liability ⇒ separatrix `A_c(E)` and
  saddle-node `E_sn`.
- Stability: det = r·ρ·A*/A_max > 0 (never a saddle); zero-delay condition a₁₁ < r; but **a₁₁ can be
  positive** — the environment's own mode is locally runaway when `(2f−1)ν > 1`.
- Delays: the sign structure of the χ-classification is **retained** (one-delay quartic constant
  terms remain opposite sign) but the **fast–slow scalar reduction is valid only where a₁₁ ≤ 0**; in
  the dangerous band use the **full 2-D transcendental** equation — the M-mode can oscillate.
- State the **non-smoothness / one-sided stability** at E = B.
- Recompute the **characteristic equation, the numerical table, and all figures** (they are not
  cosmetic). Replace the grid stability scan with exact crossing-curve methods (Hale & Huang 1993;
  Gu, Niculescu & Chen 2005).

**Step 5 — Correct the two head-line claims.**
- The knife-edge χ = 1 ⇔ ρ = 3q is the statement g_M = g_P, not an accident. Present χ as the
  organising parameter; the "≈80 yr" boundary is `s = π/ω, ω = 2r·cos(ωd/2) → π/(2r)` (closed-form,
  **not** Hutchinson continuation).
- Drop **every** "M_max/2 point of no return." The real threshold is A_c(E) if one is needed.

**Step 6 — Half-Earth.** Cap human-available flow at σB; compute debt and **Ω against the allocated
half** `(E − σbA)₊`; state whether lags/T(t) are on. Then "Ω = 0.575 / D = 0" is impossible.

**Step 7 — Numerical & verification section (RC5).** Publish the solver and history functions; state
the integrator and **clamping / K → 0** handling (liquidation can drive the stock through zero in one
step); show step-size convergence; compute the spectrum with an exact method. Every "verified" claim
carries its protocol **and any discrepancy from the manuscript's numbers** (e.g. my b_final = 0.317
⇒ D ≈ 6.76 vs. the paper's 5.240 ⇒ b ≈ 0.336; τₘ* = 85.4 vs. 83; τₚ* = 231 vs. 225).

**Step 8 — Didactics.** Symbol table; assumption-before-equation; a feedback diagram with a **switch**
(fruit harvest vs. capital liquidation); thought-experiment label (the orchard/hens framing is the
best available intuition); parameter justification (ρ large; γ, α, τ lumped); NFA data limitations.
Rewrite the **1961–2022 sentence** as a qualified observation (GFN accounts are conservative;
overshoot is likely *larger* than documented).

**Step 9 — Structure as a decision document (RC4/RC6).** Precise the mechanism↔equation map (the
B2–B9 table is the ready-made instance); a claims ledger; attribution in an appendix. Reorganise the
Discussion around the **two masks** and their observable **B rising with A falling (technology) vs.
E steady with A falling (liquidation)**.

**Step 10 — Epistemic label (C).** State the paper is a **conceptual/stylised model** — the lags, γ,
α, and τ are lumped, ρ is large, and GFN/land-cover data are cited, not fitted. That is honest and
defensible; it is *not* a forecast calibrated to national accounts.

**Definition of done.** The model reproduces its own stated narrative (deficit-driven erosion,
bounded tech vs. unbounded debt, response to past conditions); the orchard metaphor is *implemented*
rather than contradicted; the characteristic equation, table, and figures are recomputed and match; an
equilibrium exists (η); the two-delay classification is correct (χ sign); and no claim is asserted
without a protocol.

---

## PART 8 — RESIDUAL RISKS & WHAT WE CANNOT CONCLUDE

- **We cannot conclude** the paper's parameter values or scenarios are *right*; we can only conclude
  the *algebra* is correct and the *narrative* is not implemented. The numerical table must be
  recomputed under the corrected model.
- **Data limits:** real biocapacity/footprint values, salvage values V, degradation rates, and lag
  lengths are uncertain; the "dangerous band (2f−1)ν > 1" is *estimated*, not measured, from plausible
  ranges. Do not over-claim empirical support.
- **ρ ≈ 1.5 yr⁻¹ is implausibly fast**; the fast–slow reduction that makes χ a scalar control is
  valid only at such extremes. At realistic ρ (0.02–0.1 yr⁻¹) the reduction fails — use the full
  transcendental equation.
- **The "no equilibrium" singularity:** if η → 0 the model collapses (D* → ∞). η must be set to a
  physical (non-zero) value and justified; it is not a free robustness dial.
- **Non-smoothness:** the (E−B)₊ switch means the sustainable equilibrium is a boundary; one-sided
  stability is real and must be stated, or a smooth ramp used.
- **Priority/literature:** the Hutchinson early-result point is *unsupported* (not disproven); do not
  claim priority without evidence. GFN's own caveats limit how much the 1961–2022 claim can say.

---

## PART 9 — WHAT TO TELL THE AUTHOR FIRST (elevator summary)

> "The mathematics is right, but the model doesn't do what the story says it does. Your orchard
> analogy — one tree times its yield = fruit — is the correct decomposition, and it's the very
> decomposition the model destroys by putting the stock in gha. Two concrete fixes, one conceptual:
> make the depletion term subtract only the **deficit** (what the orchard can't cover) not the whole
> harvest, and keep the number-of-trees and yield-per-tree **separate** so B = A·b is even defined.
> The best form of the fix is slightly richer than the orchard alone: real biocapacity is partly
> *fruit* (crops — separable from the stock) and partly *increment* (forest growth, fish recruitment —
> a steady harvest keeps the stock below its unmanaged maximum), so write the biocapacity as
> B = bA + b_G·G(A) and let demand be met first from flow, then from increment, then from capital.
> That single equation reproduces your orchard (the flow limit), reproduces the manuscript's own
> equation (the increment limit), keeps the 'vicious cycle' and the moving carrying-capacity ceiling,
> and adds one measurable parameter (the value of standing stock) and one interpretable one (the
> flow-share ψ). The result is a smaller, cleaner, and more faithful model — I'd rewrite as Paper N′
> and label it a conceptual model."

---

## PART 10 — DOWNLOADABLE ACTION CHECKLIST (copy into the revision)

**Model changes:** [ ] **unified `dA/dt = G(A(t−τ_g)) − (E−bA)₊/b_G`** (round-2; supersedes the
orchard-only form — see Part 11) · [ ] `B = bA + b_G G(A)` · [ ] A and b separated (A in ha) ·
[ ] τ_g in recruitment · [ ] drop D (default) or re-justify as a **degradation** channel ·
[ ] multiplicative b if D kept · [ ] −ηD in the base equation · [ ] gross γE → named supplement variant ·
[ ] add flow-share `ψ = bA*/B*` and its regime dependence.
**Analytics:** [ ] recompute characteristic equation · [ ] recompute table + all figures ·
[ ] χ classification (sign structure) but full transcendental where a₁₁ > 0 · [ ] state
non-smoothness / one-sided stability · [ ] drop all M_max/2 · [ ] A_c(E) + E_sn reported ·
[ ] (2f−1)ν > 1 reported · [ ] exact crossing-curve methods.
**Headline claims:** [ ] “algebra correct, narrative unimplemented” · [ ] χ = 1 ⇔ ρ = 3q ·
[ ] closed-form ≈ 80 yr (not Hutchinson) · [ ] productivity illusion necessarily transient.
**Demonstrate the illusion (12A):** [ ] add scenario + figure: α = 0.5, Δb = 0.3, t_wave = 100 → B 0.5→0.618 while M→0.847 ·
[ ] note paper's Scenario E reaches 0.5588 only via rising M (no mask) · [ ] state the wave must outpace the debt build-up.
**Ill-posed endpoint (12A/12C):** [ ] state the P/K → ∞ blow-up at K → 0 (non-Lipschitz; add a min-viable-K or rescale) ·
[ ] state the D_E figure is method-dependent (5.26/6.74/18.70; direction robust, 5.240 not) ·
[ ] state the M ≥ 0 clamp · [ ] interpolation is a no-op (τ_m, τ_p integer multiples of Δt) · [ ] state the grid range · [ ] normalise “barely positive” by r · [ ] complete the scenario/parameter table.
**Knife-edge (12A/12B):** [ ] justify (or move off) the γ, e, b₀ set at r²a₁₁² = (γea₂₁)² = 10⁻⁴ · [ ] B6: endogenise or declare constant r_opt, e · [ ] B7: use a γ ≠ 1 case or drop “general γ” · [ ] re-label K as an algebraic (not state) variable.
**Literature/hygiene (12D):** [ ] cite Hutchinson (1948); soften Haberl & Aubauer priority/novelty · [ ] correct Brander–Taylor (1998) · [ ] add the GFN reference list (Wackernagel, Borucke 2013, Lin 2018, Galli 2016, critical exchange) ·
[ ] remove “antibiotic resistance” · [ ] fix the elevator/“sudden break” metaphor (B–C are asymptotic) · [ ] fix footnote-1 “per year” double-count · [ ] reconcile γ “carries units” vs. dimensionless · [ ] give units for M_max, b₀, Δb · [ ] clean tense/draft language · [ ] fix the truncated “when *ted…” sentence.
**Falsifiable predictions (12G.1):** [ ] state that which-lag (sign of Λ/χ) · [ ] oscillation period ≈ 4× dominant lag · [ ] computable t_peak with “B rising while A falls” signature · [ ] reducing a policy lag τ_e ≈ reducing overshoot.
**Measured basin (12G.2/12G.5):** [ ] report stable-fraction 0.506 → 0.042 (std IC flips) · [ ] add basin_shrinkage.png · [ ] state the (20,20) recovers / (30,25) collapses boundary · [ ] state B/C = “environment recovers, humans collapse” explicitly.
**Generalisation (12G.3):** [ ] present the full dimensionless set (s, g, f, θ, τ̂_M, τ̂_P) alongside χ.
**Second masking set (12G.7):** [ ] e=1.15, α=0.2, Δb=0.8, t_wave=100, κ=0.05 → B 0.711→0.832 while M→0.834 (118 sets found).
**Model consistency (12G.7):** [ ] name the tech→more-debt feedback a “Jevons-type rebound” · [ ] add a debt lag τ_D or justify the asymmetry · [ ] analyse trivial equilibrium (M,P)=(0,0) & no-recovery region · [ ] switch to Shampine & Thompson / dde23 · [ ] Δt-convergence table · [ ] note ω=0 is a spurious root · [ ] reconcile “max Ω not reported” footnote (Ω peaks ~5.0 D / ~4.1 E).
**Submissions hygiene (12G.6):** [ ] cite or remove the orphan May (1973) reference · [ ] unify “Modeling”/“Modelling” · [ ] reconcile the abstract-page vs manuscript keyword lists · [ ] provide code as .py and report as .pdf (not .docx) · [ ] strip PDF metadata “233” · [ ] strip submission-system URL + right-margin callout grid.
**Verification (RC5):** [ ] publish solver + history functions · [ ] clamping / K → 0 ·
[ ] step-size convergence · [ ] protocol + discrepancy for every “verified” claim.
**Didactics:** [ ] symbol table + assumption-before-equation · [ ] feedback diagram with switch ·
[ ] thought-experiment label · [ ] parameter justification · [ ] NFA limits ·
[ ] rewrite 1961–2022 sentence · [ ] two masks with discriminating observable.
**Process (RC4/RC6):** [ ] decide Paper N′ + C (unified stock–flow) · [ ] claims ledger · [ ] mechanism↔equation map ·
[ ] attribution in appendix.
**My own corrections:** [ ] Λ sign (three docs) · [ ] units verdict → GFN mandatory ·
[ ] a₁₁ < r (not a₁₁ < 0) · [ ] endorse Paper N′ + C (unified stock–flow), a generalisation of Paper N.

---

## PART 11 — ROUND-2 AUDITS (orchard round 2): adjudication of Grok vs. Claude

**Source.** `orchard.txt` contains (a) **my earlier orchard/hens response** (the "agent's response"),
(b) **Claude's second orchard audit**, and (c) **Grok's second orchard audit**. These are the "two
more audits" requested. They go deeper than round 1 and raise a genuine, consequential disagreement:
Grok argues the deficit-orchard analogy **is** the model; Claude argues it is **one limit** of a
unified stock–flow model whose other limit is the manuscript's own equation. I verified every claim.

### 11.1 Where the two round-2 audits AGREE (already consolidated in Parts 4/7/8)
- The deficit-orchard analogy is the *precise conceptual content of B2*; implementing it (not patching
  γE) is what makes narrative and equations the same object.
- γ = 1/V measurable; emergent A_c(E) and E_sn; τ_g in recruitment; the liquidation mask; closed-form
  rebound. **Apply the rest of the joint assessment on top** (units, equilibrium η, delays,
  verification, didactics). Recomputation is mandatory either way.

### 11.2 The point of GENUINE disagreement
| | Grok | Claude |
|---|---|---|
| The stock equation | deficit-liquidation **only** (the orchard); A_max at sustainability | **unified**: `B = bA + b_G G(A)`; `dA/dt = G(A(t−τ_g)) − [E−bA]₊/b_G` (1‴) |
| The manuscript's γE | the error to be removed | **correct in its limit** (increment-harvest: forest timber, fish recruitment); the real error is *bookkeeping*, not direction |
| Re-diagnosis of B2 | "wrong depletion term" | "**bookkeeping error** — biocapacity in the flow-book (B=bM), depletion in the increment-book (E)" |
| Re-introducing A*<A_max | = a shallower, inconsistent "conventional harvest DDE" | = the legitimate ψ→0 limit; not shallow, and it preserves deficit language + moving ceiling |
| Most profound version | the orchard itself | **the unified model** that contains both |

### 11.3 Adjudication — Claude wins; the unified model DOMINATES
I re-derived every load-bearing claim from Claude's round-2 audit symbolically; **all verified**:
- `dA/dt = G(A(t−τ_g)) − [E−bA]₊/b_G = (B − E)/b_G` when E > bA — the "**deficit = stock decline**"
  identity, exact, no ramp needed.
- **b → 0** limit ⇒ `dA/dt = ρA(1−A/A_max) − (1/b_G)E` = **the manuscript's Eq. (1), with γ = 1/b_G**.
- `a₁₁ = ρ(1−2A*/A_max) + b/b_G`; at b → 0 this is the manuscript's `ρ(1−2A*/A_max)`; at b_G·G ≪ bA
  (flow-dominant) it is `+b/b_G` (the orchard's liquidation feedback).
- **E > B ⇒ dA/dt < 0**: the moving ceiling is preserved (B falls with A ⇒ K = B/r_opt falls), and the
  bank-account / deficit language is preserved.
- `ψ = bA*/B*` is a genuine, GFN-faithful decomposition (cropland/grazing yield vs. forest/fishery
  increment) with direct empirical content and a **testable prediction**: small ψ → smooth decline
  stabilised by demographic feedback; large ψ → overshoot invisible until demand exceeds flow yield,
  then liquidation with a threshold.

**Claude's deeper diagnosis is more correct and more charitable.** The manuscript's depletion term was
**not flatly wrong** — it is the increment-harvest limit. The actual error is bookkeeping: it defines
B = bM (flow-book) while depleting with E (increment-book). The unified model fixes the bookkeeping
and *reproduces* the manuscript in the ψ → 0 limit, so the manuscript is "correct-but-mislabelled,"
not "wrong."

**Grok's objection misfires, but one part is valid.** Grok attacks "keep γE and upgrade per the other
audits" — but that is the **b → 0 special case**, *not* the unified model; the unified model keeps the
deficit-driven `[E−bA]₊/b_G`, so it does **not** discard the deficit language, the moving ceiling, or
the bank-account metaphor. **However**, Grok is right that the orchard is the *cleaner didactic*
"minimal mechanistic illustration," and that the unified model is less simple to present. So the
orchard (ψ → 1) remains the best **pedagogic device**, while the unified model is the more **faithful
and more profound** representation of real biocapacity and of the paper's own empirical message.

### 11.4 Refined recommendation
> **Paper N′ + C (unified stock–flow, model 1‴)** — a generalisation that contains both the orchard
> (flow limit, ψ → 1) and the manuscript's increment model (ψ → 0). It re-diagnoses B2 as a
> bookkeeping error, is the most faithful to GFN, and is the cheapest (one equation, one added
> measurable parameter `b_G`, one interpretable dimension `ψ`, no ad hoc ingredients). **Paper N
> (orchard-only) is a special case** (ψ → 1) and remains a defensible didactic choice for a
> "minimal mechanistic illustration."

### 11.5 Effect on the verdicts
- **RC1 (ontology of M)** — still the deepest. The unified model *completes* the A/b separation by
  fixing M's unit (ha) and adding the second flow quantity `b_G G(A)`; both bA and b_G G(A) become
  separable.
- **B2** — refined from "deficit vs. gross" to "**flow-book vs. increment-book**; the unified model is
  the correct bookkeeping." More precise, more charitable.
- **RC3 (no equilibrium)** — unchanged; add −ηD or K = B/e.
- **B5 (asymmetry)** — the degradation channel is retained as a **third, separately-evidenced
  ingredient** (b declines under sustained overuse of the *surviving* stock). Claude/Grok agree this
  is what the analogy alone lacks and what makes the paper's strongest empirical message (accounted
  biocapacity is overstated) real. Present it as such — **not** as "ecological debt doing the work
  that A already does."
- **The two prior assessments** — nothing reversed; the root-cause spine (RC1 → options → decision →
  affected sections → risks) stands. The orchard (Part 4) remains the best intuition; the unified
  model refines the *implementation*.

### 11.6 Implementation-plan deltas (supersede the orchard-only items where they conflict)
- Replace `(1″)` with **`(1‴)`**: `dA/dt = G(A(t−τ_g)) − [E − bA]₊/b_G`, with `G(A) = ρA(1−A/A_max)`.
- Define **`B = bA + b_G G(A)`**; γ = 1/b_G for the increment component; V = b_G is the standing-stock
  value in gha·yr.
- Add the **flow-share `ψ = bA*/B*`** as a new control parameter. Report the ψ-dependence:
  ψ → 0 (increment, manuscript-like: interior A*, χ-classification applies); ψ → 1 (flow, orchard:
  A_max at sustainability, liquidation mask, vicious cycle); **in-between** (interior A* *and*
  liquidation feedback, `a₁₁ = ρ(1−2A*/A_max) + b/b_G`).
- Keep the degradation channel as a separately-evidenced third ingredient.
- Recompute the characteristic equation, table, and figures for `(1‴)` — not cosmetic.

---

## PART 12 — LINE-LEVEL COMPLETION PASS: granular points carried (final gap-closure)

A systematic line-level scan of **every** joint assessment and source document (the two model audits,
the two meta-audits, the human reviewer, `JOINT_assessment_all_sources.md` Parts A–G, the findings
register Parts A–G, `evaluation_of_model_audits.md`, the root-cause addendum, and the two orchard
rounds) surfaced a set of **specific, mostly non-narrative points** not explicitly carried in Parts
1–11. Each is listed with its source and how it slots in. **I verified the numerics; several are
concrete, actionable additions to the implementation plan.** None reverses any verdict.

### 12A. Concrete, verified numerics (highest value — add to the plan)
1. **The productivity illusion IS demonstrable with the paper's own parameters** (`findings_register`
   A1, A4): use **α = 0.5 (baseline), Δb = 0.3 (the paper's own amplitude), t_wave = 100 yr** ⇒
   **B 0.5 → 0.618 while M → 0.847** (a genuine masking illusion). Two caveats that sharpen it:
   (i) in the paper's **own** Scenario E (Δb = 0.3, t_wave = 150), B does reach 0.5588 but **because M
   is rising** (logistic overshoot from the low starting P = 0.1), *not* because of the masking
   mechanism — so "no shown scenario exhibits the illusion" holds; (ii) the illusion needs the wave to
   **outpace the debt build-up** (arrive while M is still high and D still small); with t_wave = 150
   the wave just props up a falling b. **Action: add a scenario + figure of the illusion using the
   α=0.5/Δb=0.3/t_wave=100 set** (this directly answers reviewer (e) and turns the headline thesis into
   a demonstrated result).

2. **The population equation is singular / non-Lipschitz at K → 0** (`findings_register` A3): with
   K = b·M/r_opt → 0, P/K → ∞, so dP/dt → −∞. "Total collapse to P = 0" is **not** a smooth approach
   to an attractor — it is a **blow-up**; the exact termination point (and hence further debt) depends
   on the ad-hoc clamp. **Action: state this (a minimum-viable-K or carrying-capacity floor, or a
   rescaling) as a limitation, alongside the M ≥ 0 clamp** (this is my root-4 "ill-posed boundary"
   made precise). It is the deeper cause of the next point.

3. **The reported debt figure is method-dependent** (`findings_register` A2): D_E was reproduced as
   **5.26, 6.74, and 18.70** depending on whether the population is `frozen`, `crashed`, or left
   un-clamped once K → 0. The direction (D_E > D_D) is **robust**; the specific **5.240** is **not**.
   **Action: state that the .240-place number is an artifact of the endpoint convention** — a classic
   RC5 "present the protocol and the discrepancy" item.

4. **The parameters are set exactly at the knife-edge** (`findings_register` #26; reviewer (e)):
   γ, e, b₀ are chosen so that **r²a₁₁² = (γ·e·a₂₁)² = 1.0×10⁻⁴** (Λ = 0) — the *measure-zero*
   surface. This is **non-generic and unexplained**, and it is precisely why "no single delay
   destabilises" holds. **Action: justify this, or perturb off the knife-edge and report the generic
   result** (which Part 11 shows is "exactly one lag destabilises, by the sign of Λ").

### 12B. Model points not yet explicitly carried
5. **B6 — "co-evolving per-capita requirement" is promised but never modeled** (`JOINT_assessment_all_sources`
   Part B): r_opt(t) and e(t) carry time arguments yet are constant in every analysis and scenario
   (the human reviewer's (c); register #28). **Action: either endogenise them or state explicitly that
   they are held constant as a baseline choice.**

6. **B7 — "dynamics for general γ" is advertised but only γ = 1 is used** (footnote 1). **Action: use a
   γ ≠ 1 case or drop the "general γ" claim.**

7. **E1 — K is a state-**algebraic** variable, not an "emergent state variable"**: K = B/r_opt = bM/r_opt
   is a *function of state* (an algebraic observable), not an integrated state. **Action: re-label** —
   only (A, P, and — if kept — D) are states; K is derived. (Grok's "K is an algebraic observable,
   not a state" — B4 of the addendum — is the same point.)

### 12C. Numerics / reporting rigour (Part D of `JOINT_assessment_all_sources`)
8. **The advertised "interpolation for delayed quantities" is a no-op for the stated parameters**:
   τ_m = 30 and τ_p = 25 are exact integer multiples of Δt = 0.5 (60 and 50 steps), so no interpolation
   occurs. **Action: either state that no interpolation is needed, or use a genuinely non-multiple step.**
9. **The 41×41 grid's range is never stated**, and "barely positive (Re λ < 0.01)" is not "barely"
   relative to r = 0.02. **Action: state the range and normalise the margin by r.**
10. **Scenario definitions are incomplete**: which e, which lags, and whether T(t) is active are given
    only for some rows; F is undetermined. **Action: make the scenario/parameter table complete.**

### 12D. Literature & presentation hygiene
11. **E2 — Haberl & Aubauer (1992) "first introduced time delay into human population dynamics" is
    unsupportable**: the delayed-logistic stability result is **Hutchinson (1948)**, ~44 years earlier.
    Also do **not** claim novelty for a two-lag DDE. **Action: cite Hutchinson (1948) as the ancestor;
    soften the novelty claim.**
12. **E3 — Brander & Taylor (1998) is mischaracterised**: the manuscript says it differs from models
    that "assume a fixed resource growth function and constant harvesting effort," but it *does* use a
    fixed logistic and constant per-capita e, and Brander–Taylor actually **endogenises effort**.
    **Action: correct the characterisation.**
13. **Recommended literature (adopt Claude's GFN reference list)**: Wackernagel & Rees;
    Wackernagel et al. 2002 (PNAS); Borucke et al. 2013; Lin et al. 2018; Galli et al. 2016; and the
    critical exchange Blomqvist / van den Bergh & Grazi / Giampietro & Saltelli. **Action: add these**
    (answers reviewer (d) — the "limitations" references as well as the account reference).
14. **Presentation / misc (E5)**: "antibiotic resistance" is a non-sequitur overshoot symptom; the
    "elevator cable / sudden break" metaphor contradicts the model's own *asymptotic* B–C decay;
    footnote 1's "…per year" double-counts; §2.1 says γ "carries the units required" while the footnote
    says γ is dimensionless; M_max = 1.2, b₀ = 0.5, Δb = 0.3 are given **without units** while r_opt, r,
    α are given with units, and P values are dimensionless (the gha bookkeeping is abandoned in §4
    without comment); draft/backward tense ("We will introduce…"); and the truncated sentence
    "**when \*ted near the notional equilibrium**" (§4). **Action: clean all of these.**

### 12E. What to PRESERVE (the verified-correct list; do not "fix")
For completeness, and so the author does not "fix" anything that is already right (`findings_register`
B1): all six scenario-table entries reproduce to 3 decimals; the characteristic equation (13) and the
Appendix A linearisation are correct; both single-delay polynomials are correct modulo a harmless
scalar factor; no single delay destabilises on the Λ = 0 surface; the Scenario-B one-delay Hopf at
τ_M ≈ 83 yr, ω ≈ 0.026 is correct; the two-mechanism division (debt-driven vs. delay-transient) is
sound. **These are the "keep" items; only the interpretation (narrative-implementation) and the
non-generic framing are the problems.**

### 12F. Net effect of this pass
These are **completions, not reversals**: they add a specific, verified demonstration set (12A.1),
make the ill-posedness (12A.2) and the endpoint method-dependence (12A.3) explicit, flag the
non-generic knife-edge parameter choice (12A.4), and close the remaining model (12B), numerics (12C),
and literature/hygiene (12D) gaps. With this pass, **no point from any source remains
unincorporated.** The master's verdict (Part 1), fork table (Part 6), and implementation plan
(Part 7) are **unchanged** in direction; 12A–12D refine *specific steps* (add a scenario and figure
for the illusion; state the K→0 singularity and the endpoint convention; cite the correct literature;
clean the presentation).

### 12G. Second-pass completions (from re-reading review.md, proposed_upgrades.md, root-cause analysis)

A second full re-read of `ECOMOD-26-1191_review.md`, `ECOMOD-26-1191_proposed_upgrades.md`,
`ECOMOD_26_1191_root_cause_analysis.md`, and the `profound upgrades.txt` meta-audit surfaced **more
points** not yet in Parts 1–11 or 12A–12F. All verified in this session. None alter any verdict;
they are the last granular items.

**12G.1 — The falsifiable / emergent predictions (the strongest *positive* contribution; `root-cause`
RC5).** The model is not merely "sufficiency"; it makes **four emergent, falsifiable** predictions
(listed as such, none built into any equation, so the model is not circular):
(i) **which lag destabilises** (the sign of Λ / χ);
(ii) the **oscillation period near onset ≈ 4× the dominant lag**;
(iii) the **productivity illusion has a computable peak-biocapacity time `t_peak`**, with the
signature "**B rising while A falls**";
(iv) the model predicts that **reducing a policy lag τ_e matters comparably to reducing the overshoot**.
**Action: state these as the paper's testable predictions** (this is what the Discussion's "deferred
empirical decomposition" should point toward; it is the honest, non-circular version of the 1961–2022
claim). These also give the "two masks" (Part 4) concrete, measurable signatures.

**12G.2 — The measured basin-shrinkage result (a strong, defensible number; `proposed_upgrades` §7).
**The qualitative "basin of attraction shrinks" (Scenario D) is **quantifiable and dramatic**, and
should be reported as a measured quantity, not asserted: the stable fraction of the (M₀, P₀)
initial-condition plane for the overshoot constant-parameter subsystem falls from **0.506 (no delays)
→ 0.042 (baseline (30,25))**, and the standard IC (1.0, 0.1) **flips from stable to collapse**. A
two-panel basin figure (`basin_shrinkage.png`) exists. **Action: report the stable-fraction as a
function of (τ_M, τ_P) and add the figure** — this is arguably the paper's most defensible numeric
contribution. *Note: the orchard round-2 (Part 11) offers an alternative/complementary framing —
Claude's time-to-separatrix `A_c(E)` criterion — so present both: the measured fraction (empirical)
and the separatrix criterion (closed-form).*

**12G.3 — The dimensionless group set (the complete generality statement; `root-cause` RC3).**
Alongside the single control χ = q/(ρ−2q), carry the **complete** non-dimensionalization: `t̂ = rt`,
`a = A/A_max`, `p = P·r_opt/(b₀A_max)`, and groups **`s = ρ/r`, `g = γb₀f/ρ`, `f = e/r_opt`, `θ`**,
plus scaled delays **`τ̂_M = rτ_M`, `τ̂_P = rτ_P`**. χ is the cleanest single control (matches the
scalar two-gain picture); the 6-group set is the full generality statement. Present both — they are
complementary.

**12G.4 — Scenario B/C is "environment recovers, humans collapse" (`review` §5; register #18).**
The paper never states that in Scenarios B and C **M rebounds to ≈1.19 (near M_max) while P and the
harvest B collapse** — a "humans die, orchard survives" outcome that is the **opposite of the orchard
framing** in the abstract, and it should be stated explicitly (or the framing reconciled).

**12G.5 — The Scenario-D collapse is a threshold-crossing accident, not a clean result (`review` §5).**
The D/not-D boundary is **near-critical**: a transient that dips just below M_max/2 = 0.6 collapses,
while one that stays above recovers. Concretely: **(20,20) gives min M = 0.631 and recovers;
(30,25) gives min M < 0.6 and collapses.** **Action: state this and report the actual basin boundary,
not a single point** (`basin_shrinkage.png` is the fix); it also explains why the result is
method-sensitive (bare Euler, clamping).

**12G.6 — Editorial / submission hygiene (`review` §8):**
- **Orphan reference:** May, R.M., 1973, "Stability and Complexity in Model Ecosystems" appears in the
  reference list but is **never cited** in the body. Cite it (relevant to stability/complexity) or
  remove it.
- **Journal name inconsistency:** "Ecological **Modeling**" (cover letter) vs. "Ecological
  **Modelling**" (title page/header).
- **Keyword list differs** between the abstract page and the manuscript.
- **Supplementary material is packaged as Word documents** (`python.docx`, `verification report.docx`)
  rather than `.py`/`.pdf` — awkward for reproducible-software review; provide the code as `.py` and the
  report as `.pdf`.
- **PDF metadata author = "233"** (submission artifact).
- **Submission-system artifacts embedded**: the "Click here to access/download" link and the
  numbered-right-margin callout grid — strip both from a clean manuscript.

**12G.7 — Additional fine points (`proposed_upgrades`, `review`):**
- The **second** technology-masking demonstration set (besides 12A.1): **e = 1.15, α = 0.2, Δb = 0.8,
  t_wave = 100, κ = 0.05** ⇒ **B 0.711 → 0.832 while M → 0.834** (then M → 0, D ≈ 307). The search
  found **118 parameter sets** with a "B rises while M falls" window. Either set demonstrates the
  illusion.
- **Name the technology→more-debt feedback as a "Jevons-type rebound"** explicitly (as the honest
  framing of D_E > D_D), not a silent inconsistency.
- **Debt-lag option:** to make the delay structure consistent, either add a debt lag
  (`dD/dt = max(E(t−τ_D) − B(t), 0)` and/or `b = b₀e^{−αD(t−τ_D)} + T`) **or** justify the asymmetry
  explicitly (depletion immediate; functional degradation a separate, slower state). The master's Part
  6 F5 (τ_g) covers the stock-delay choice; τ_D is a *third* lag option to keep on the table.
- **Analyse the trivial equilibrium (M, P) = (0, 0)** and the **no-recovery region (M < M_max/2)**;
  recommend a **proper time-domain DDE solver** (Shampine & Thompson 2001; `dde23`/`pydelay`) plus a
  **Δt-convergence table**.
- **Spurious ω = 0 root** in the single-delay polynomials is an artifact of squaring through the
  Pythagorean identity (at λ = 0 the characteristic = −r·a₁₁ + γ·e·a₂₁ = 0.02 ≠ 0, so λ = 0 is **not**
  an eigenvalue); do not present the "trivial root" as trivial.
- **"max Ω not reported" footnote is arbitrary:** Ω peaks at ~5.0 (D) and ~4.1 (E) and is plotted in
  Fig. 4 (clipped at 8.5), yet the table declares them "not reported"; reconcile the footnote with the
  figure.

### 12H. Completion status (final)
With 12G folded in, **every** point across this whole exercise — the two model audits, the two
meta-audits, the human reviewer (b)–(g), my review (`review.md` §0–§9), my proposed upgrades
(`proposed_upgrades.md` §0–§10), my root-cause analysis (RC1–RC5 + the minimal-repair and
A/B/C-option lists), the findings register (Parts A–G), the all-sources assessment (Parts A–G), the
root-cause assessment/ADDENDUM/FINAL, the orchard rounds 1–2, and this scan of every joint assessment
— is now carried in the master. The master is the single authoritative, self-consistent, executable
specification: **Paper N′ + C (unified stock–flow), deficit-driven depletion, A/b separation, τ_g in
recruitment, η for well-posedness, GFN convention, correctly-signed Λ/χ classification, recomputed
equations/table/figures, the four falsifiable predictions, the measured basin-shrinkage result, and a
full hygiene pass.**
