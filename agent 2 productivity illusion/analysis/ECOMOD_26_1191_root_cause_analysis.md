# Root-Cause Analysis of ECOMOD-26-1191
## Why the manuscript fails the way it does — and the global resolutions that eliminate the failure modes at the source

**Purpose.** The prior reviews (mine + the two audits + the human reviewer) enumerate ~40 discrete
findings. This document does something different and more useful: it asks **why** so many flaws
occur together, identifies the **small number of structural design decisions** that generate them,
and proposes **global resolutions** — fixes that remove *entire classes* of flaws by construction,
rather than a long list of point patches. Where a resolution is a redesign rather than a repair,
that is stated plainly.

**Method note.** Every root cause below is grounded in either an exact algebraic identity or a
re-verified computation. Two things from the verification passes are stated up front because they
are load-bearing: (1) the *correction* to my own earlier units verdict — the manuscript is
internally consistent under its own stated convention, **but** its γ = 1 flow-into-stock coupling
is a genuine mechanism-level flaw and is the origin of the deepest narrative contradiction; and
(2) the zero-delay stability condition is `a11 < r`, **not** `a11 < 0`, which corrects both the
paper and an earlier note of mine. I also found that a quick numerical integrator I built for the
"canonical" model had an indexing bug and made it crash for the sustainable case; I discarded those
numbers and grounded the arguments in the exact algebra instead, which I have checked and which is
not vulnerable to integration error.

---

## The core diagnosis in one paragraph

The manuscript was built in two directions that were never reconciled. The **narrative** was
written top-down — a compelling orchard metaphor, a weak-vs-strong-sustainability reconciliation,
an overshoot-and-collapse story — and the **model** was constructed bottom-up, chosen for analytical
tractability and for its ability to *produce* overshoot-and-collapse from a hand-picked parameter
set. Nothing enforced that each sentence's mechanism actually appears in an equation, that the
accounting (stock/flow/units) was defined once and used consistently, that the results were stated
only at the level of generality at which they hold, or that the model was well-posed at its own
boundary. Every one of the ~40 findings traces back to **four root causes** that follow from these
four missing disciplines. Fix them and the flaws stop being a list and start being a handled class.

---

## ROOT CAUSE 1 — No mechanism-traceability constraint (the narrative and the equations diverge)

**Statement.** The paper promises certain mechanisms in prose and implements *different* (or no)
mechanisms in the equations. This single cause generates nearly the whole "model–narrative
inconsistency" set — the most damaging group of findings.

**Exact demonstration (the headline case, finding B2).**
§1 says: "When the footprint exceeds biocapacity, an ecological deficit occurs… the deficit draws
down the stock." But Eq. (1) is:

> dM/dt = ρM(1 − M/Mₘₐₓ) − γE ,  γ = 1,  and **B = bM never appears.**

Because the drain term is the **full footprint E**, not the deficit (E − B), the sustainable portion
of demand also destroys stock. Algebraically, for any E (even E ≤ B where there is *no* deficit),
dM/dt has a −E term. The orchard metaphor — "take the apples, keep the tree" — is therefore not
implemented; in the model, *every apple harvested removes a tree.*

**All symptoms attributable to this root cause (each verified):**

| # | Symptom | The promised mechanism vs. what's implemented |
|--:|---------|---------------------------------------------|
| B2 | Full-E vs deficit | "deficit drains stock" vs. `−γE` with `γ=1` |
| B3 | Delay justification | "extraction is immediate; delay is a shortcut" vs. **no** immediate term at all |
| B4 | Demographic delay | "people respond to conditions they knew" ⇒ delayed **K**; implemented `P(t−τₚ)/K(t)` = delayed P, current K |
| B5 | Asymmetry | "debt compounds, tech saturates, so collapse wins" vs. additive `b=b₀e^{−αD}+T` floors `b ≥ T` |
| B6 | co-evolving rₒₚₜ | promised; `rₒₚₜ(t), e(t)` constant in every scenario |
| B7 | "general γ" | footnote advertises it; only γ=1 used |
| B9 | @Half-Earth bookkeeping | "caps biocapacity at half," but D uses full B and Ω is vs full B (so Ω=0.575 means 115% of the half) |
| B10 | debt-repayment | "qualitative conclusions unchanged" vs. "collapse→persistent oscillation" (a qualitative change) |
| B11 | Scenario-D stability | "equilibrium locally stable" asserted for a model (full overshoot, α>0) that has **no** interior equilibrium (E\*=1.15B\*>B\* ⇒ dD/dt>0 forever) |

**The root cause, precisely:** the author selected equations for tractability, then wrote a story
that the equations do not encode. Each mismatch is an instance of the same failure: **no rule that
every mechanism named in prose must be literally present in, and only in, an equation that
implements it.**

**Global resolution (eliminates B2–B11 as a class, by construction).** Adopt a
**mechanism-traceability discipline**: annotate every paragraph's mechanism with "implemented by
Eq. (X)" and require a bijective mapping — a mechanism either has an equation that realizes it, or
it is explicitly labelled "analogy, not implemented." Then **repair the account** so the two stated
mechanisms are actually present:

- **Deficit-driven depletion (fixes B2, and makes the orchard metaphor true):**
  `dA/dt = ρA(1 − A/Aₘₐₓ) − γ [E(t−τₘ) − θB(t−τₘ)]`, θ ∈ [0,1]. With θ=1 only the *deficit* (E−B)
  liquidates stock; a surplus accrues as regrowth ("interest vs. principal"). This is exact: at
  θ=1 and E ≤ B, the bracket is ≤ 0, so dA/dt ≥ ρA(1−A/Aₘₐₓ) ≥ 0 — the stock never decreases from
  harvest. θ=0 recovers the paper's gross-depletion form as a special case. I verified this
  algebraically (no simulation needed).
- **Multiplicative debt (fixes B5, and makes the asymmetry a theorem):**
  `b = [b₀ + T_b(t)]·e^{−αD}`. Then `lim_{D→∞} b = 0` *regardless of T_b* (any finite amplitude),
  and since T_b is bounded (logistic) while D is unbounded under persistent overshoot (η small),
  `b → 0` necessarily. The "tech saturates, debt compounds" asymmetry is a derived result, not an
  assertion. In the additive form it is simply false (verified: `lim b = T_b > 0`).

---

## ROOT CAUSE 2 — The accounting layer and the dynamics layer are conflated

**Statement.** The manuscript never fixes one convention for *what is a stock, what is a flow,
what units each carries, and what is conserved*, so it oscillates between conventions and mislabels
its own objects. This generates the units ambiguity, the gamma coupling, the state-variable miscall,
the dimension miscount, and several presentation errors.

**The three consequences in detail.**

**(a) Stock/flow/units convention is never fixed (the three-way disagreement).** Two conventions
are each internally self-consistent — the manuscript's (M in gha; E, B in gha·yr⁻¹; D = gha;
α = gha⁻¹) and the GFN one (gha is already annual; D = gha·yr; α = (gha·yr)⁻¹). The manuscript
never says which it uses, and **γ = 1 couples a flow (E, gha·yr⁻¹) directly to a stock (M, gha)
one-for-one.** That coupling is physically dubious and is the *same* mis-step that causes B2. So
the units issue is not cosmetic — it is the mechanism-level root of the orchard contradiction.
This **refines my earlier verdict**, which had called the (b) units comment simply "wrong": the
manuscript is internally consistent, but it conflicts with GFN's own convention and never declares
its own. A single "Units and GFN convention" table + one paragraph fixes the whole class (this is
also the constructive fix for the human reviewer's points (b) and (f)).

**(b) Object misclassification.** K = B/rₒₚₜ = bM/rₒₚₜ is an **algebraic** quantity, yet §1 calls it
"an emergent **state variable**." Only M, P (and in the full model D) are integrated state
variables. This is a category error, and it compounds the "two-dimensional" vs. three-ODE miscount
(B1): the full model has states (M, P, D) = 3 ODEs; only the α=0 subsystem is 2-D. Calling K a
state and the system "two-dimensional" are the same failure to distinguish algebraic slaved
variables from dynamic states.

**(c) Incorrect process labels.** Eq. (6) `dD/dt = max(E−B, 0)` is called "a first-order process,"
but without a `−ηD` term it is a **pure integrator** (no decay), so "first-order" is wrong. The
"max Ω not reported" footnote and the "Ω diverges as B→0" reading are the same accounting-confusion
fault, as is the Mₘₐₓ/2 "threshold" being called a "logistic regeneration threshold" (see Root
Cause 3).

**Global resolution.** Introduce a single **canonical units/object table** used everywhere — define
`A` (physical productive area, ha, stock), `b` (bioproductivity, gha·ha⁻¹), `B = bA` (biocapacity,
gha·yr⁻¹, flow), `E = eP` (footprint, gha·yr⁻¹, flow), `D = ∫(E−B)₊dt` (accumulated deficit,
gha·yr), `K = B/rₒₚₜ` (population, **algebraic**, not a state), and give γ, α, ρ, r, η, κ proper
units and the non-dimensionalization. This one table kills (a), (b), (c), the "two-dimensional vs
three-ODE" miscount, the "K is a state variable" error, and the "first-order process" mislabel.
The non-dimensionalization (below) is the mechanism-level fix that also resolves Root Cause 3.

---

## ROOT CAUSE 3 — Local facts stated at the level of global laws (no genericity check)

**Statement.** The paper derives results at one hand-picked point of parameter space and presents
them as general theorems. This generates the knife-edge "two delays required" result, the false
sufficiency condition, the incorrect stability "condition," the fabricated Mₘₐₓ/2 threshold, and
the polynomial-degree error. It is the same root cause in five guises: **no non-dimensionalization
and no check that the result is generic.**

**Evidence (exact).**

- **The knife-edge is real and specific.** The baseline satisfies `ρ = 3γeb₀/rₒₚₜ = 1.5`, which
  forces `M*/Mₘₐₓ = 2/3` and `r²a₁₁² = (γea₂₁)² = 1.0×10⁻⁴`. That is why both single-delay
  polynomials factor `ω²` (constant term exactly 0) and why "no single delay destabilizes."
- **The correct general statement is a classification, not a special case.** `Λ ≡ γe·a₂₁ − r|a₁₁|`:
  `Λ < 0` ⇒ the environmental lag τₘ alone Hopfs (Scenario B's ≈83 yr is this case); `Λ > 0` ⇒ the
  demographic lag τₚ alone Hopfs (verified: ρ=1.6 ⇒ ω≈0.0114, τₚ≈225 yr); `Λ = 0` ⇒ neither (the
  measure-zero surface the baseline sits on). **Generically exactly one lag is individually
  destabilizing.** The paper's stated condition `r²a₁₁² ≥ (γea₂₁)²` is false — strict `>` actually
  *guarantees* a τₚ-only Hopf.
- **`a11 < 0` is not the zero-delay stability condition.** The correct Routh–Hurwitz condition on
  the coupled non-delayed system is `a11 < r` (trace), with `det = rρM*/Mₘₐₓ > 0` identically.
  The paper's `M* > Mₘₐₓ/2` ("upper branch") is (i) derived for the wrong object (M-equation with
  p≡0), (ii) not a "branch" (a logistic has no bistable branches), and (iii) only sufficient for the
  coupled system, not necessary. **This corrects my own earlier note too.**
- **The Mₘₐₓ/2 "irreversible threshold" is fabricated.** `ρM(1−M/Mₘₐₓ) > 0` for *every* 0 < M <
  Mₘₐₓ; 0.6 is the *maximal-growth* point, not a separatrix. There is no bistability or
  irreversibility in a plain logistic. §4/§5's "irreversible threshold" directly contradicts §5's
  own Limitations ("the logistic recovery model neglects hysteresis and irreversible thresholds").
  This is a **newly-surfaced flaw** I had not documented before.
- **The τₘ=0 polynomial is degree-4, not degree-6.** The clean modulus condition gives
  `ω²(1250ω²+287) = ω²(ω² + a₁₁² − r² − 2γea₂₁)·(ω² + a₁₁²)`; the extra `(ω²+a₁₁²)` is a spurious
  factor. Claude is right; Grok's main-text degree-6 is wrong (his own appendix says degree-4).
- **"≈80 yr" is really the Hutchinson threshold.** `π/(2r) = 78.54` yr for r = 0.02 — the classical
  delayed-logistic Hopf. The "two delays required at τₘ+τₚ ≈ 80 yr" is far more likely the ordinary
  single-lag Hutchinson result, masked by the Λ=0 cancellation (which suppresses it only at τₘ=0
  exactly).

**Global resolution.** **Non-dimensionalize** (`t̂ = rt`, `a = A/Aₘₐₓ`, `p = P·rₚₑᵣc/(b₀Aₘₐₓ)`) so
the constant-parameter subsystem depends only on the dimensionless set `s = ρ/r`, `g = γb₀f/ρ`
(`f = e/rₒₚₜ`), `θ`, and scaled delays `τ̂ₘ = rτₘ`, `τ̂ₚ = rτₚ`. Then:

1. **State every result as a condition on these dimensionless groups, never as a fact about one
   baseline.** The "single delay can't destabilize" becomes "generically exactly one lag
   destabilizes, and the sign of Λ selects which."
2. **Replace the "≈80 yr" law** with "the stability boundary in the (τ̂ₘ, τ̂ₚ) plane; the
   single-lag component is governed by rτ ≈ π/2 (Hutchinson)."
3. **Use full-spectrum/bifurcation tooling** (DDE-BIFTOOL, or a spectral solver) and report
   stability-crossing *curves*, not a single-branch grid scan.
4. **If the narrative needs a threshold, put one in the model, not in the logistic.** Add an Allee
   term `ρA(A/M_A − 1)(1 − A/Aₘₐₓ)`, `0 < M_A < Aₘₐₓ`. Exact analysis shows fixed points at
   A = 0, M_A, Aₘₐₓ; for 0 < A < M_A the growth term is negative (a genuine extinction basin) and
   for M_A < A < Aₘₐₓ positive (persistence basin). This is a *real* separatrix and gives the
   "basin-of-attraction shrinks" narrative of Scenario D a rigorous object.

---

## ROOT CAUSE 4 — The model is not well-posed at its own boundary (singular, clamped collapse)

**Statement.** The model's collapse endpoint is never analyzed; it is an artifact of clamping.
This generates the singularity, the method-dependence of all reported numbers in the collapse
regime, and the "interpolation is moot" / Euler-stiffness concerns.

**Exact demonstration.** Eq. (4) is `dP/dt = rP(t)[1 − P(t−τₚ)/K(t)]` with `K = bM/rₒₚₜ`. As M → 0,
K → 0 and the ratio P/K → ∞, so the right-hand side is **unbounded / non-Lipschitz** — a singular
blow-up, not a smooth approach to an attractor. The exact point at which P reaches 0, and therefore
how much further debt accumulates, depends on the ad-hoc clamping in the discretisation. This is why
I obtained D_final = 4.83, 5.26, or 6.74 for the same scenario depending on how the K→0 endpoint
was handled. Related: `ρΔt = 0.75` with a large delayed depletion term can overshoot M negative in
one step, and the "interpolation for delayed quantities" is a **no-op** because τₘ = 30 and τₚ = 25
are exact integer multiples of Δt = 0.5 (verified).

**Global resolution.** Make the boundary well-posed by construction:

- **With deficit-driven (θ=1) depletion, A = 0 IS an equilibrium** — `dA/dt = 0` at A = 0 when
  E ≤ B = 0 — so "collapse" is a genuine model feature, not a clamp. Add an explicit
  **extinction floor** `A_ext > 0` (equivalently the Allee M_A) or, better, **report time-to-
  collapse** and state the extinction threshold. This removes the non-Lipschitz singularity.
- **Use a proper time-domain DDE solver** (method of steps + RK45/stiff, e.g. `dde23`/`pydelay`),
  not bare Euler, and **report results at two step sizes** (a Δt-convergence table). This is cheap
  and pre-empts a reviewer objection.
- **Declare the regime taxonomy quantitatively:** report stable / oscillatory / collapse with
  explicit thresholds (the paper's "heuristic thresholds" are not enough) and state the history
  functions on [−max τ, 0] and the initial condition (currently (1.0, 0.1) "appears only in
  passing").

---

## ROOT CAUSE 5 — Epistemic conflation (sufficiency presented as support/forecast)

**Statement.** The model is a *mechanism/sufficiency* model (if this feedback exists, it can
produce collapse), but it is presented as *carrying empirical support* and as a *forecast*. This
generates the "self-referential" charge, the unsupported 1961–2022 claim, and the parameter
assertion.

**Symptoms.** The §5 sentence "The global data from 1961–2022 are consistent with this
interpretation: biocapacity grew modestly while ecological overshoot persisted" presents **no data,
no figure, no citation**, and the same section defers empirical decomposition to future work. The
paper builds in the debt feedback `dD/dt = max(E−B,0)` and the productivity erosion, then shows
overshoot → collapse — a *sufficiency* argument, not evidence that it does so in reality. The
parameter set (γ, ρ, α, the lags, and the knife-edge γ·e·b₀/rₒₚₜ = ρ/3) is asserted, not estimated.

**Global resolution.** **Separate imposed from emergent, and declare the epistemology:**
- *Imposed*: logistic regeneration, bounded technology, the two lags, the accounting identity,
  the Allee threshold (if added). *Emergent and falsifiable*: (i) which lag destabilizes (sign of
  Λ), (ii) the oscillation period near onset ≈ 4× the dominant lag, (iii) the productivity illusion
  has a **computable peak-biocapacity time** t_peak with the signature "B rising while A falls,"
  (iv) the model predicts that reducing a policy lag τₑ matters comparably to reducing overshoot.
  State that what is emergent is *not* built into any equation, so the model is not circular.
- **Rewrite the 1961–2022 sentence** as a qualifying observation or fold it into the Discussion
  with the GFN-limitations caveat (accounts are conservative: biocapacity likely overstated,
  overshoot understated). Better: replace it with a statement of what the model *can* test — the
  A/b decomposition of biocapacity change using independent A-proxies (land cover, soil carbon,
  NPP) — which is exactly the test the paper says it defers.
- **Label the paper's status** in the abstract: a *conceptual model with illustrative
  calibration*, not a forecast, whose purpose is to make explicit the logic connecting accounting,
  deficit, lags, and the stock/yield decomposition. This is the honest and defensible framing, and
  it is what preserves the ambition rather than undercutting it.

---

## Global resolutions, consolidated (one per root cause)

| Root cause | Global resolution | Class of flaws eliminated | Severity |
|-----------|-------------------|--------------------------|:--------:|
| 1. No mechanism traceability | Bijective mechanism↔equation map; deficit-driven depletion (θ) + multiplicative debt | B2–B11 | High |
| 2. Accounting/dynamics conflated | Single canonical units & object table + non-dimensionalization; A vs b vs B vs D; K algebraic | units 3-way, γ-coupling, "K is a state," "2-D vs 3-ODE," "first-order process," Ω footnote | High |
| 3. Local facts as global laws | Non-dimensionalize; Λ-classification theorem; full-spectrum tooling; explicit Allee for a real threshold | knife-edge, false sufficiency, a11<0, Mₘₐₓ/2 threshold, poly-degree-6 | High |
| 4. Ill-posed boundary | θ=1 ⇒ A=0 is an equilibrium; extinction floor / time-to-collapse; proper DDE solver + Δt-convergence | singularity, method-dependence, interpolation no-op, Euler stiffness | Medium–High |
| 5. Epistemic conflation | Imposed-vs-emergent; rewrite 1961–2022 with caveats; label as conceptual model | self-referential, unsupported empirical claim, parameter assertion | Medium |

**The defensive version of this (a "minimal repair" that keeps the current equations and six
scenarios).** If the author prefers not to change the model structure, the global resolutions
degrade into a smaller but still self-consistent set of corrections: (i) state `a11 < r` (not
`a11 < 0`) as the zero-delay condition; (ii) drop the Mₘₐₓ/2 "irreversible threshold" language and
replace it with honest committed-degradation language; (iii) replace "no single delay destabilizes"
with the Λ-classification; (iv) correct the τₘ=0 polynomial to degree-4; (v) fix the Half-Earth cap
to `K = 0.5·B/e` and note Ω = 0.575; (vi) state the units convention and note K is algebraic; (vii)
reduce-scan to large enough τₚ (≳250 yr) before asserting "no single-delay Hopf"; (viii) switch to a
proper DDE solver. This is a genuine fix that removes the contradictions, but it leaves the two
*structural* weaknesses (B2's full-E depletion, B5's additive floor) unaddressed. The full global
resolution is the only path that makes every mechanism real.

---

## Which "resolution" to choose: a decision, not a menu

There is a real fork, and it should be made explicitly, because it changes the paper's identity:

- **Option A — Minimal repair (recommended if the paper must keep its exact model and six
  scenarios).** Low risk, removes the internal contradictions and the false claims, all analytic
  results become parameter-dependent statements that are true. Does not fix B2/B5 (the two deepest
  mechanism gaps) — those are softened into caveats.
- **Option B — Global refactor (recommended if the ambition is the priority).** Adopt the canonical
  model (deficit-driven depletion, multiplicative debt, delayed-conditions demographic lag, Allee
  for a real threshold, non-dimensionalized parameterization). This is Claude's "redesign" spirit
  but I treat it as the *natural* endpoint of the root-cause fixes rather than an optional add-on,
  because it makes the mechanisms real and turns the two weakest original claims (the knife-edge
  "two delays required" and the false technology/debt asymmetry) into its two *strongest* results
  (a classification of which lag is dangerous, and a proof that the productivity illusion is
  necessarily transient). It is a new model, so it is a bigger lift.
- **Option C — Reframe as a conceptual/thought-experiment paper with illustrative calibration.**
  Orthogonal to A/B but necessary regardless: declare the epistemology, separate imposed from
  emergent, and withdraw the 1961–2022 inference. This is what makes the paper defensible as a
  *modeling* contribution rather than a claim about the world.

**Recommendation.** Do **B** (global refactor) for the model core and **C** (epistemic reframing)
for the framing. If scope is a hard constraint, do **A + C**. Do **not** do A alone and leave B2/B5
as caveats, because they are the mechanisms the paper is about.

---

## What I corrected in my own analysis, and why this document is honest about it

- **Units verdict refined.** I earlier wrote the reviewer's "(b) units" point was simply "wrong."
  That is too strong: the manuscript is internally consistent under its own convention, but it
  conflicts with GFN's convention and its γ=1 flow-into-stock coupling is the origin of B2. I now
  frame it as convention-ambiguity + a real coupling flaw.
- **`a11 < r` correction.** The zero-delay stability condition is `a11 < r`, not `a11 < 0`; this
  corrects the paper *and* an earlier note of mine.
- **Numerical-integrator caution.** A quick integrator I wrote for the canonical model had an
  indexing bug and crashed for the sustainable case. I did not use those numbers; I grounded the
  deficit-driven and multiplicative-debt claims in exact algebra, which I verified and which is
  not vulnerable to integration error. (The reported D_final = 4.83 / 5.26 / 6.74 spread *is*
  genuine — it is the B11/A3 singularity, not the integrator bug.)
- **The canonical model retains the paper's ambitions.** The global refactor keeps emergent
  carrying capacity, GFN accounting as the driver, two interacting lags, cumulative debt, bounded
  technology waves, the weak/strong-sustainability reconciliation, and the Half-Earth lever — it
  merely makes each one a real property of the equations instead of a rhetorical claim.
