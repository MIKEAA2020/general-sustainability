# Deep-Reading Notes: Error Bounds, Viability Kernels, and Nature Sustainability Landmarks

*Prepared for the sustainability-assessment paper (*p1.txt* / humanized v2). Three parts: (1) the full error-bounds paper, (2) the attached Aubin & Catté (2002) viability-kernels paper, (3) landmark & highly relevant *Nature Sustainability* articles. Each ends with "why it matters for your paper."*

---

# Part 1 — Full read: "Error Bounds: Necessary and Sufficient Conditions"

> **Fabian, M. J., Henrion, R., Kruger, A. Y., & Outrata, J. V.** *Set-Valued Anal.* **18**, 121–149 (2010). DOI 10.1007/s11228-010-0133-0. (Full PDF read from WIAS Berlin; 29 pp.)

## 1.1 What the paper is about

An **error bound** says: *how far you are from the feasible set is controlled by how badly you violate the constraint.* Formally, for a closed set A = {x : f(x) ≤ 0} and a point x̄ ∈ A, does there exist a neighborhood U and constants c, β > 0 with

> d(x, A) ≤ c·[f(x)]₊^β for all x ∈ U ?   *(β = 1 is the usual case)*

This is one of the central quantitative ideas in variational analysis, going back to **Hoffman** (linear systems) and **Łojasiewicz** (analytic geometry). The paper's contribution is a **general classification scheme** that organizes *all* known necessary and sufficient conditions for the error-bound property — in terms of "slopes" (primal-space derivative-like objects) and subdifferentials (dual-space objects) — and shows exactly how they interrelate (their Figs. 3–6 are literal implication diagrams).

## 1.2 Why error bounds matter (their own roadmap)

The error-bound property is equivalent to a cluster of central notions:

| Notion | Definition (in words) | Reference |
|---|---|---|
| **Metric subregularity** | d(x, F⁻¹(ȳ)) ≤ c·d(ȳ, F(x)) — small constraint violation ⟹ proportionally small distance to solutions | Ioffe; extended to multifunctions |
| **Calmness** (of a multifunction M at a graph point) | d(x, M(ȳ)) ≤ k·d(y, ȳ) for (y, x) near the graph point | Ye & Ye; term coined in Rockafellar–Wets |
| **Weak sharp minima** | a solution set that "sticks out" — being ε-close in value forces ε-close in distance | Burke–Ferris, Polyak |

Crucially: *F is metrically subregular at (x̄,ȳ) ⟺ F⁻¹ is calm at (ȳ,x̄), with the same constant.* So error bounds, subregularity, and calmness are three faces of one property — and this is the modern language of **constraint qualifications** and **convergence rates** for optimization algorithms.

## 1.3 The core machinery: slopes (primal) and subdifferentials (dual)

**The (strong) slope** (De Giorgi–Marino–Tosques):
> |∇f|(x̄) = lim sup_{x→x̄} (f(x̄) − f(x))₊ / ‖x − x̄‖.

**Three new "uniform strict slopes"** (the paper's main new objects, eqs. 6–8) — all computed only at points *outside* the level set [f ≤ f(x̄)], i.e. where f(x) > f(x̄):
- **lower** −|∇f|⋄(x̄): descent rate measured with balls strictly inside the feasible set's distance;
- **upper** +|∇f|⋄(x̄): descent rate with balls of radius α ↓ d(x, [f ≤ f(x̄)]);
- **middle** ◦|∇f|⋄(x̄): descent rate over all u with f(u) ≥ f(x̄).

**Theorem 1:** −|∇f|⋄ ≤ ◦|∇f|⋄ ≤ +|∇f|⋄, with equality of all three if f is Lipschitz near x̄. (Each inequality can be strict — three counterexamples given.)

**Theorem 2 (the anchor).** The **error-bound modulus** Er f(x̄) sits between the middle and upper slopes:
> **(i)** Er f(x̄) ≤ +|∇f|⋄(x̄) *(always)*;
> **(ii)** if X is Banach and f is lower semicontinuous, Er f(x̄) ≥ ◦|∇f|⋄(x̄) *(via the Ekeland variational principle)*.

So on a Banach space with f lsc: **◦|∇f|⋄(x̄) ≤ Er f(x̄) ≤ +|∇f|⋄(x̄)**, and all three coincide for Lipschitz f. This immediately yields the first classification:
- **NC1** +|∇f|⋄(x̄) > 0 — *necessary* condition;
- **C1** ◦|∇f|⋄(x̄) > 0 — *sufficient*;
- **C2** −|∇f|⋄(x̄) > 0 — *sufficient*;
with **C2 ⇒ C1 ⇒ NC1**.

## 1.4 The full classification ladder

**Primal (slope) criteria** (for lsc f on a Banach space), built from three further slopes — strict slope |∇f|(x̄), strict outer slope |∇f|>(x̄), and internal slope |∇f|0(x̄):

- **C3** |∇f|(x̄) > 0
- **C4** |∇f|>(x̄) > 0
- **C5** |∇f|0(x̄) > 0

with implications C3 ⇒ C4 ⇒ C2, and C5 ⇒ C1; **C5 is independent of C3/C4**, so the authors recommend the "combined" criteria max(|∇f|, |∇f|0) > 0 and max(|∇f|>, |∇f|0) > 0. (Fig. 3.)

**Dual (subdifferential) criteria**, using the Fréchet subdifferential ∂f and its "slope" |∂f|(x̄) = inf{‖x*‖ : x* ∈ ∂f(x̄)}, plus strict/outer/internal variants:

- **C6** |∂f|(x̄) > 0
- **C7** |∂f|>(x̄) > 0
- **C8** |∂f|0(x̄) > 0
- **NC2** |∂f|⋄(x̄) > 0 *(necessary)*

Key bridge: **Proposition 5(ii)** — in **Asplund** spaces (a large class including every reflexive space), |∇f|(x̄) = |∂f|(x̄) and |∇f|>(x̄) = |∂f|>(x̄), via the *fuzzy (semi-Lipschitzian) sum rule*. Three ingredients used: (1) 0 ∈ ∂f(x) at local minima; (2) Fréchet = convex subdifferential for convex f; (3) the semi-Lipschitzian sum rule — the one place Asplundity enters. Replacing Fréchet by **Clarke** subdifferentials gives versions valid in *arbitrary* normed spaces (Prop. 6), at the cost of weaker (often strict) inequalities. (Fig. 4.)

**Finite-dimensional refinements** (Prop. 11–14, Thm 4):
- If f is merely **continuous** near x̄ in finite dimensions, *all three* slopes already coincide with Er f(x̄).
- The strict subdifferential slopes equal the distance of 0 to the **limiting (Mordukhovich) subdifferential** ∂f(x̄), the limiting outer subdifferential ∂>f(x̄), and a new uniform limiting subdifferential ∂⋄f(x̄). Hence the crisp criteria:
  - **C9** 0 ∉ ∂f(x̄)
  - **C10** 0 ∉ ∂>f(x̄)
  - **C11** 0 ∈ int ∂f(x̄)
  - **NC3** 0 ∉ ∂⋄f(x̄)
  - **C12** 0 ∉ bd ∂f(x̄) *(if f is lower regular; = the Henrion–Jourani–Outrata criterion)*
- For **semismooth** f, C11 ⇒ C10 (so the internal and outer conditions chain).
- **Theorem 4:** a chain rule for the outer subdifferential of a composition f = φ∘F (F C¹, φ a Lipschitz "distance-like" function with φ(y)=0 ⟺ y ∈ C): ∂>f(x̄) ⊂ ∇F(x̄)*·Limsup ∂φ(F(x)), with equality under surjectivity of ∇F(x̄) or lower regularity of φ. This is how you *compute* the criteria for concrete constraint systems.

**Convex case** (Thm 5): everything collapses — Er f(x̄) = −|∇f|⋄ = ◦|∇f|⋄ = +|∇f|⋄ = |∇f|> = |∂f|> = |∂f|⋄, and |∇f| = |∂f|. Only **two** criteria survive: **C4** and **C13** (0 ∉ ∂f(x̄)); C4 is necessary here and can be strictly weaker than C13. Conditions C11 and C13 are mutually exclusive and merge into **C12**, which (per Ngai–Kruger–Théra) characterizes a strictly *stronger* property than the mere existence of an error bound — namely **stability of the error bound under small perturbations of f**.

## 1.5 Why this matters for your paper

1. **The thresholds ρ₁, ρ₂ and κ\* = 1 − x are error-bound-modulus objects.** In *p1.txt*, the per-weight licensing thresholds ρ₁ = (2−s₁)/s₂ and ρ₂ = s₁/(2−s₂), and the rescue threshold κ\* = 1 − x, are exactly statements of "how far a state sits from the boundary of the accepted set." The Fabian–Henrion–Kruger–Outrata framework is the general theory that quantifies such boundaries: the error-bound modulus is *the* measure of how robustly a feasibility property holds as the state (or weight) moves. A natural extension of your paper would phrase the rescue/impossibility split in terms of the **modulus of the typed acceptance property**, i.e. d(z, V_typ) ≤ c·[violation]₊.
2. **Calmness/subregularity = the "resource margin" in quantitative form.** Your STAGED action's feasibility is controlled by the reserve x, with threshold x ≥ 1. That is precisely a *calmness* statement: a small shortfall in x (below 1) is "paid for" by the augmentation κ = 1 − x. Error-bound/calmness theory is the standard toolkit for turning such statements into rates.
3. **Criterion C12 and perturbation stability.** The observation that C12 (0 ∉ bd ∂f) characterizes error bounds *stable under perturbation* mirrors your Remark 6 (persistence under hold-prefix extension) and Theorem 7 (erasure under architecture change): both papers are about *when a feasibility certificate survives modification of the problem*, which is exactly what stability of the error bound formalizes.

---

# Part 2 — Full read: Aubin & Catté (2002), viability kernels and capture basins

> **Aubin, J.-P., & Catté, F.** "Bilateral fixed-points and algebraic properties of viability kernels and capture basins of sets." *Set-Valued Analysis* **10**, 379–416 (2002). (Attached PDF read in full; 38 pp.)

## 2.1 The objects

For a differential inclusion x′ ∈ F(x), an environment K and a target C ⊂ K:
- **Viability kernel** Viab(K,C) — states from which *at least one* trajectory stays in K forever, or until it reaches C in finite time. With C = ∅: Viab(K).
- **Capture basin** Capt(K,C) — states from which C is reached in finite time *before possibly leaving K*.
- **Invariance kernel** Inv(K,C) — states from which *all* trajectories stay viable/invariant.
- **Absorption basin** Abs(K,C); **invariance envelope** Env(C) = Capt of the *backward* dynamics (also: Poincaré's "shadow" of K is K \ Viab(K)).

## 2.2 The algebraic core (the paper's thesis)

All these objects obey a tiny set of **order-theoretic laws**, which is the real content of the paper:

- The maps (K, C) ↦ A(K, C) are **pre-openings in K** (increasing + antiextensive, A(K,C) ⊂ K) and **pre-closings in C** (increasing + extensive, C ⊂ A(K,C)). Idempotence upgrades them to genuine **openings / closings** — the language of mathematical morphology.
- **Bilateral (minimax) fixed point:** the viability kernel is the *unique* D with C ⊂ D ⊂ K and
  > D = Viab(K, D) = Viab(D, C),
  i.e. D is "viable outside C" and "isolated in K." This is why the object is canonical: it is simultaneously a largest fixed point in one variable and a smallest fixed point in the other.
- **Matheron's theorem** (Thm 5.2): given the two monotonicity laws, there are canonical maps A♯ (the *opening* associated with a pre-opening — the largest fixed point) and A♭ (the *closing* associated with a pre-closing). The viability kernel is *exactly* the opening A♯ of the map K ↦ C ∪ (K ∩ Φ⁻¹(K)) for a discrete system with set-valued map Φ.
- **Galois transform** (upper/lower residuals): adjoint relationships between openings and closings, giving duality results (e.g. the Galois transform of the invariance-kernel map yields the invariance envelope).

## 2.3 The algorithms (why it's actionable)

- **Saint-Pierre viability-kernel algorithm** (Thm 6.3 + Prop 6.4): start K₀ := K and iterate
  > K_{n+1} := C ∪ (K_n ∩ Φ⁻¹(K_n)).
  Then Viab(K,C) ⊆ ⋂ K_n, with **equality** under closedness and upper-semicompactness of Φ restricted to K. This is *the* workhorse algorithm for computing viability kernels of discrete systems — a backward-recursion / fixed-point iteration.
- The **capture-basin algorithm** is the dual iteration (Thm 6.6–6.7).
- **Cardaliaguet's algorithm** (Thm 8.9) computes **discriminating kernels** in dynamical games — the game-theoretic analog (a "viability kernel" against an adversary), again shown to be a fixed-point construction.
- All of these are instances of the same algebraic scheme, so correctness proofs reduce to the abstract fixed-point theorems rather than ad-hoc arguments.

## 2.4 Why this matters for your paper

1. **Your backward recursion is a Saint-Pierre iteration.** *p1.txt*'s exact-tube operators ("safe iff *every* state on the path satisfies the constraints") and its §3 backward induction are a typed instance of exactly the viability-kernel/capture-basin fixed-point recursion studied here — as your own §5.2 acknowledges. Aubin & Catté give the cleanest statement of *why* that recursion converges to the right set (largest fixed point / opening), which is the structural backbone your paper could cite to justify the recursion's well-foundedness.
2. **The "no single action serves every weight" phenomenon is a fixed-point failure.** The acceptance gap FP_agg = V_weak \ V_typ is, in the paper's language, the difference between *per-weight* acceptance (an intersection of fixed points of different maps E_w) and *common-plan* acceptance (a fixed point of the intersection ⋂_w E_w). Aubin & Catté's bilateral-fixed-point framework is the right vocabulary for stating precisely when these coincide — your Remark 1 ("common selector exists") is the general form of their largest-fixed-point characterization.
3. **Game-theoretic reading.** Your assessor–planner reading (pure vs mixed strategies) is literally the *discriminating kernel* setup: Cardaliaguet's discriminating kernel is the viability kernel under an adversary. Your Theorem 8 (blend/convexification collapses the gap) is the mixed-strategy closure of a discriminating-kernel problem.

---

# Part 3 — Landmark & highly relevant work in *Nature Sustainability*

*Nature Sustainability (launched 2018) is the flagship venue for empirical sustainability-science results. The papers below are its landmark statements of precisely the "separately binding floors vs. aggregated ceilings" idea that your paper formalizes.*

## 3.1 O'Neill, Fanning, Lamb & Steinberger (2018) — "A good life for all within planetary boundaries"

> *Nat. Sustain.* **1**, 88–95. DOI 10.1038/s41893-018-0021-4. *(Read via the accepted-version PDF at White Rose.)*

**What it does.** Operationalizes the "doughnut" = a **safe and just space**: **7 biophysical ceilings** (downscaled planetary boundaries: climate, land-system change, freshwater use, biogeochemical flows, plus ecological & material footprint) and **11 social floors** (nutrition, sanitation, education, income, life satisfaction, etc.), then checks whether *any* country sits inside the doughnut.

**Key findings.**
- **No country** meets basic needs at a globally sustainable level of resource use.
- **Physical needs** (nutrition, sanitation, electricity, ending extreme poverty) *could* plausibly be met for everyone within boundaries.
- **Qualitative goals** (e.g. high life satisfaction) would require resource use **2–6× the sustainable level** under current relationships.
- The remedy is **sufficiency + equity** in provisioning systems.

**Why it's the landmark twin of your paper.** This is the empirical statement of *separately binding constraints*: 11 social thresholds and 7 biophysical ceilings are each checked **separately** — a country "fails" if *any* floor is unmet or *any* ceiling is breached, with **no compensation across them** (meeting more social goals does not excuse breaching a boundary). Your paper's typed floors sᵢ ≥ 0 with exact-tube safety are the *formal* version of the doughnut's logic; conversely, a weighted-aggregate index (your E_w) is exactly what O'Neill et al. deliberately refuse to construct. The doughnut's "no country is inside" is the real-world echo of your impossibility region being nonempty.

## 3.2 Lade, Steffen, de Vries, Carpenter, Donges, Gerten, Hoff, Newbold, Richardson & Rockström (2020) — "Human impacts on planetary boundaries amplified by Earth system interactions"

> *Nat. Sustain.* **3**, 119–128. DOI 10.1038/s41893-019-0454-4.

**What it does.** Surveys and provisionally quantifies **interactions among the planetary-boundary processes** (climate, biosphere integrity, biogeochemical flows, land, freshwater, etc.) and asks what they mean for governance.

**Key findings.**
- The boundaries form a **dense network** of interactions (cascades and feedbacks).
- These interactions **predominantly amplify** human impacts — meaning the effective **safe operating space is smaller** than treating each boundary separately would suggest.
- Governance must be **integrated**; a dashboard of independent boundaries is insufficient.

**Why it's highly relevant to your paper.** This is the *empirical* counterpart of your §5.3 scope limit — **"No separation under coupled all-floor shocks."** You note that if disturbances couple simultaneous dips across all floors, the per-weight licensing structure degenerates and the compensatory/noncompensatory divergence collapses into universal rejection. Lade et al. show that in the real Earth system, exactly such **coupling is the norm**, not the exception: crossing one boundary pushes others. So your theorem's scoping to an action-indexed (uncoupled) disturbance class, and your explicit flagging of the coupled case as an open/different regime, is the correct formal boundary — and Lade et al. is the canonical empirical reference for *why* the coupled case matters.

## 3.3 Fanning, O'Neill, Hickel & Roux (2022) — "The social shortfall and ecological overshoot of nations"

> *Nat. Sustain.* **5**, 26–36. DOI 10.1038/s41893-021-00799-z.

**What it does.** The **dynamic** follow-up to 3.1: tracks 11 social indicators and 6 biophysical indicators across **>140 countries, 1992–2015**, plus business-as-usual projections to 2050.

**Key findings.**
- **No country** met minimum social thresholds within biophysical boundaries at any point in the period, and **none is on track** to do so by 2050.
- Countries tend to **transgress boundaries faster than they meet social thresholds**.
- Patterns differ by income: low-income countries need social acceleration within boundaries; high-income countries need radical resource reduction without social harm; Costa Rica is the standout efficiency case.

**Why it matters for your paper.** This is the **dynamic** question your paper formalizes — *can a trajectory be certified during a transition?* — measured empirically: the paper's "exact-tube" requirement (safe at every point of the path, not just the endpoint) is exactly what a *time series* of doughnut positions checks, and Fanning et al.'s finding that countries leave the safe space *along the way* (not just at the endpoint) is the empirical instantiation of your "the endpoints are the photograph; the tube is the trajectory." Their trajectory plots are, in effect, empirical tubes.

## 3.4 Context and connection

- The conceptual chain: **Rockström et al. 2009** ("A safe operating space for humanity," *Nature* 461) and **Steffen et al. 2015** ("Planetary boundaries," *Science* 347) supply the *ceiling* side; **Raworth's doughnut** supplies the *floor* side; the three *Nature Sustainability* papers above supply the *data*. Your paper supplies the missing *formal logic*: what exactly goes wrong when a weighted aggregate is used to certify a transition across separately binding floors, and under what conditions (resource margin, menu convexification) the certification can be repaired.
- Also note the 2023 update **Richardson et al., "Earth beyond six of nine planetary boundaries"** (*Sci. Adv.* 9, eadh2458) and **Rockström et al. 2023, "Safe and just Earth system boundaries"** (*Nature* 619, 102–111) — the latter makes explicit that "safe" and "just" are **two separate sets of boundaries**, i.e. two typed families of floors, which is precisely the multi-floor structure of your datum.

---

## Consolidated reading list (for your References / related work)

**Set-Valued & Variational Analysis (journal):**
1. Fabian, Henrion, Kruger, Outrata (2010). *Error bounds: necessary and sufficient conditions.* Set-Valued Anal. 18, 121–149.
2. Aubin & Catté (2002). *Bilateral fixed-points and algebraic properties of viability kernels and capture basins of sets.* Set-Valued Anal. 10, 379–416.
3. Combettes & Pesquet (2012). *Primal-dual splitting…* Set-Valued Var. Anal. 20, 307–330.
4. Davis & Yin (2017). *A three-operator splitting scheme…* Set-Valued Var. Anal. 25, 829–858.
5. Gfrerer (2013). *On directional metric regularity…* Set-Valued Var. Anal. 21, 151–176.

**Nature Sustainability:**
6. O'Neill, Fanning, Lamb, Steinberger (2018). *A good life for all within planetary boundaries.* Nat. Sustain. 1, 88–95.
7. Lade et al. (2020). *Human impacts on planetary boundaries amplified by Earth system interactions.* Nat. Sustain. 3, 119–128.
8. Fanning, O'Neill, Hickel, Roux (2022). *The social shortfall and ecological overshoot of nations.* Nat. Sustain. 5, 26–36.

**Adjacent (context, cited by the above):**
9. Rockström et al. (2009). *A safe operating space for humanity.* Nature 461, 472–475.
10. Steffen et al. (2015). *Planetary boundaries: guiding human development on a changing planet.* Science 347, 1259855.
11. Rockström et al. (2023). *Safe and just Earth system boundaries.* Nature 619, 102–111.
12. Richardson et al. (2023). *Earth beyond six of nine planetary boundaries.* Sci. Adv. 9, eadh2458.
