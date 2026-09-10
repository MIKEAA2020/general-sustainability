# Critical assessment of ECOMOD-26-1191
## "Overcoming the productivity illusion with delayed feedbacks and emergent carrying capacity" (A. Abaee)

**Scope of this assessment.** I re-derived the analytical results and re-implemented the model
(Equations 1–9) independently, then ran all six scenarios, the single-delay and two-delay
stability analyses, the debt‑repayment variant, and the Scenario‑B Hopf calculation. Below,
"verified" means I reproduced the paper's claim with my own code; "contradicted" or
"not supported" means I did not.

---

## 0. What checks out (so the review is fair)

These are **correct** and internally consistent:

- **The model and all six scenario table entries reproduce exactly.** Re-implementing
  Eqs. (1)–(9) with the stated parameters (ρ=1.5, M_max=1.2, γ=1.0, b₀=0.5, r_opt=1.0,
  r=0.02, α=0.5, τ_M=30, τ_P=25, f=1.15, Δb=0.3, κ=0.1, T=600 yr, dt=0.5 yr) reproduces the
  table values to 3 decimals: A→(0.800, 0.400, 0.000, Ω=1.00); B→(1.194, 0.007, 8.847, 4.55);
  C→(1.193, 0.009, 8.507, 5.66); D→(0.000, 0.000, 4.826); E→(0.000, 0.000, 5.240);
  F→(0.970, 0.243, 0.000, 0.60). The figures are consistent with the table.
- **The characteristic equation (13) is correct.** I re-derived the linearization in
  Appendix A (including the sign of the ∂/∂M term of the demographic equation) and confirmed
  the matrix, the determinant expansion, and Eq. (13).
- **The two single-delay polynomials are correct** (up to a harmless scalar factor):
  for τ_P=0, ω²(10 000ω² + 2504)=0; for τ_M=0, ω²(2500ω⁴ + 1199ω² + 143.5)=0. Both have strictly
  positive coefficients, so no positive-frequency Hopf root for the baseline set.
- **No single delay destabilizes the baseline** (numerically confirmed; Re λ < 0 for all
  single-delay values up to 150 yr).
- **Scenario-B one-delay Hopf at τ_M ≈ 83 yr, ω ≈ 0.026 rad yr⁻¹** is correct and robust;
  additional crossings every ~2π/ω ≈ 242 yr, as stated.
- **The two-mechanism division is supported.** With α=0 (debt neutralized), the constant
  overshoot subsystem at (30,25) still drives M→0 from the standard IC (M=1.0, P=0.1) even
  though the equilibrium (0.740, 0.37) is locally stable; with only one or no delay it does
  not. So "delays alone can collapse M via transient" (Scenario D) and "debt drives the
  small-delay collapse" (Scenarios B/C) are both real. The debt‑repayment test (η=10) still
  collapses M, matching the paper.
- **Dimensions are consistent.** For Eq. (1), γ must be dimensionless (as the footnote says),
  and Eq. (11)/(12)/(13) are all dimensionally consistent. I found no unit error here.

The issues that follow are the substantive ones.

---

## 1. The headline "≈80 yr" instability threshold is disconnected from, and marginal in, the results

This is the biggest internal-consistency problem.

**(a) The threshold governs no scenario shown.** The "both delays required, threshold at
τ_M+τ_P ≈ 80 yr" result is a *linear*-stability statement about the *sustainable,
constant-parameter* subsystem (Scenario A, e=r_opt, α=0). But:

- Scenario A itself is run **with no lags** (sum = 0), nowhere near 80 yr.
- Scenario D is the scenario that both delays, and it is explicitly **linearly stable** at
  the baseline (30,25): Re λ = −0.0083. Its "total collapse" is attributed to *nonlinear
  transient/basin* dynamics — i.e., **not** to the 80-yr linear threshold.
- Therefore the flamboyant "80 yr" figure is a property of a subsystem that **no simulation
  actually probes**. The abstract, intro, and conclusion all present it as the paper's central
  quantitative result, but it does not explain any of the curves in Figures 1–5.

**(b) In Figure 6, Scenario D's own point sits in the "stable" (blue) region, yet Scenario D
collapses.** The (30,25) diamond is marked on the Scenario-A map, which is stable there. The
paper then needs a separate, non-linear explanation for D's collapse. That is not a formal
error, but it means Fig. 6 and the collapse narrative are **two disconnected results** and the
reader is not told how the one bears on the other.

**(c) The instability is only ever marginal.** Across the entire two-delay plane (0–160 yr
each), the largest growth rate I found is **Re λ ≈ +0.007 yr⁻¹** (at τ_M, τ_P ≈ 100–120 yr).
Near "τ_M+τ_P = 80," Re λ is of order 10⁻³–10⁻⁴ — i.e. within numerical noise of zero (the
paper itself notes "Re(λ) < 0.01"). A growth rate of 0.007 yr⁻¹ is a ~150-year e-folding
time: an essentially neutral, barely-unstable oscillation (period ≈ 2π/0.03 ≈ 200 yr). This is
not the dramatic "destabilization" the abstract implies.

**(d) The boundary is not aligned with constant total delay.** The claim "approximately aligned
with contours of constant total delay" is contradicted by the eigenvalue structure. Examples at
the *same* total delay but different stability: (50,40) sum 90 → Re +0.0021 (unstable);
(90,20) sum 110 → Re −0.0014 (stable); (60,50) sum 110 → Re +0.0043 (unstable). The threshold
is **strongly ratio-dependent**, not a function of τ_M+τ_P. The "80 yr" number is thus an
approximation of a boundary that is really curve-shaped and noise-dominated.

*(This is why I'd push back on the abstract's phrasing: "instability requires both delays to
interact, with the threshold at a combined delay of approximately 80 yr." The "interaction"
part is defensible; the "≈80 yr" part is an overstatement of a marginal, ratio-dependent,
noise-level boundary.)*

---

## 2. The central finding — the "productivity illusion" — is asserted but never demonstrated

The paper's stated contribution is that *rising biocapacity can mask depletion* (weak
sustainability) with the illusion breaking down in the long run. Yet:

- **B(t) is never plotted.** Figures 1–5 show M, P, K, Ω, and D only. The quantity the entire
  thesis is about — the biocapacity trend B = b·M — is not shown as a time series (K = B/r_opt,
  so Figure 3 is proportional to B, but it is neither labeled nor interpreted that way).
- **Every overshoot scenario ends in collapse.** B, C, D, E all crash (in D/E, M→0; in B/C,
  P→0). No figure shows a *rising-biocapacity, declining-stock* regime.
- The paper concedes this: "The model can also reproduce a rising‑biocapacity phase … That
  regime is **not shown here**." So the paper's headline phenomenon is described, not
  demonstrated. In the abstract and conclusion it is stated as if it were a result
  ("Rising biocapacity need not signal improving environmental health"), when it is actually an
  untested assertion about a parameter regime never presented.
- I checked whether the illusion is even reachable. With the paper's Scenario-E wave
  (Δb=0.3, t_wave=150) it is *not*: b never exceeds ~0.5 (b₀), since b = b₀e^{−αD} + T and
  T→0.3 < b₀. Only with a far stronger/earlier wave (Δb≥2, t_wave≈50) does B rise above its
  initial value — and then M still ends at 0. So the model can produce the illusion, but only
  in a regime the paper never presents and with parameters it never assigns to a scenario.

---

## 3. Half-Earth extension does not actually cap biocapacity at half

Eq. (9): K_Half-Earth = 0.5·B/r_opt. This caps **population**, but consumption runs at
**e = 1.15·r_opt** (an overshoot lifestyle that the scenario inherits). The realized footprint is

> E* = e·P* = 1.15·r_opt · (0.5·B/r_opt) = **0.575·B**,  i.e. Ω_HE = 0.575,

not 0.5·B. The paper states the cap "caps human-usable biocapacity at half of the total," but
the simulated Half-Earth uses **57.5%** of total biocapacity. To cap the *footprint* at half
one would need K = 0.5·B/e, not 0.5·B/r_opt. The mismatch (r_opt in the divisor, e in the
consumption) is an internal inconsistency. It also means the result is not really Wilson's
"Half-Earth": it is a "keep the population at a level that *would* need half the Earth at the
*optimal* footprint, while actually consuming at 1.15× optimum."

---

## 4. The "no single delay can destabilize" proof rests on a knife-edge parameter choice

The proof is valid only under r²a₁₁² ≥ (γ·e·a₂₁)², and the paper says this is "satisfied for
the baseline parameters." But for the chosen values it holds with **exact equality**:

> r²a₁₁² = (0.02)²(−0.5)² = 1.0×10⁻⁴ ; (γ·e·a₂₁)² = (1.0·1.0·0.01)² = 1.0×10⁻⁴.

The inequality is **not strict**; it sits precisely on the boundary. Consequently (i) the
single-delay polynomials have a degenerate (double) trivial root, and (ii) the "cannot
destabilize" conclusion flips with any small perturbation that makes r²a₁₁² < (γea₂₁)² (a
slightly larger γ, e, b₀, or a smaller a₁₁). This is a fragile, non-generic parameterization
that underwrites the central analytical result. A reviewer should ask whether the parameters
were reverse-engineered to hit this equality — and how robust the "80 yr" result is to any
realistic change (e.g., the real-world γ≪1 that the footnote itself anticipates).

---

## 5. Component findings worth flagging

- **"Basin of attraction shrinks" is asserted, not shown.** No basin-volume/separatrix
  computation, reference to a computed basin, or set of perturbed-IC sweeps is provided; the
  claim in Scenarios D is qualitative. Given that the equilibrium is *barely* stable
  (Re ≈ −0.008), the distinction the paper draws between "basin shrinkage" (D) and "debt
  driven" (B/C) is supported only by the two α=0 runs, not by an actual basin analysis. It is
  also fragile to numerical method: collapse/recovery depends on whether the transient dips a
  hair below M_max/2 = 0.6 (e.g., (20,20) gives min M = 0.631 and *recovers*; (30,25) gives
  min M < 0.6 and collapses), so the D/not-D boundary is close to a threshold-crossing accident.
- **Scenario B/C outcome is "environment recovers."** In B and C the population collapses and
  M rebounds to ≈1.19 (near M_max=1.2). This is a "humans collapse, planet recovers" outcome,
  arguably the *opposite* of the degradational narrative in the abstract's orchard framing. Not
  an inconsistency, but the text never states this clearly.
- **The "max Ω not reported" footnote is arbitrary.** Ω for D and E reaches a finite peak
  (~5.0 and ~4.1) before B→0; Figure 4 plots these (clipped at 8.5). Declaring them "not
  reported" in the table is inconsistent with the figure and with the fact they are computable.

---

## 6. Unsupported empirical claim

The Discussion asserts "the global data from 1961–2022 are consistent with this
interpretation: biocapacity grew modestly while ecological overshoot persisted." This appears
with **no data, figure, or reference**, and it sits awkwardly beside the paper's repeated
stance that "empirical calibration is explicitly deferred to future work." Either the claim is
unsupported, or the calibration is not deferred. It is also a factual claim about the GFN
record that should be cited if retained.

---

## 7. Additional line-level findings (from a second, close re-read)

The checks below were produced by re-reading the manuscript line by line and re-running the
relevant pieces. Where they refine an earlier section, the refinement supersedes it.

### 7.1 The "productivity illusion" never occurs in any shown scenario — not even transiently

This is the sharpest form of flaw #2. I traced Scenario B (overshoot, no lags) explicitly:

| t (yr) | M (gha) | b (yr⁻¹) | B = b·M (gha/yr) |
|------:|--------:|---------:|-----------------:|
| 0     | 1.000   | 0.5000   | 0.5000           |
| 50    | 1.016   | 0.5000   | **0.5089**       |
| 100   | 0.866   | 0.5000   | 0.4337           |
| 140   | 0.786   | 0.3764   | 0.2955           |
| 600   | 1.194   | 0.0060   | 0.0072           |

Biocapacity B bumps from 0.500 to only **0.509** (+1.8%) at t≈50 — and at that instant **M is
rising** (1.016), not falling. There is **no time** at which B rises while M declines. From
t≈100 onward B collapses monotonically to ≈0.007. So the paper's defining phenomenon — *a
stable or rising harvest that masks a depleting stock* — is simply **absent from all six
scenarios**. The actual pattern is the opposite of the orchard metaphor: in Scenarios B and C
the **stock M recovers to ≈1.19 (near M_max) while the harvest B and the productivity b crash**.
The orchard metaphor ("killing trees") does not match the results (the trees survive; the
harvesters die).

The only scenarios with a *constant* B are A (B=0.4) and F (B=0.485), both stable; the only
scenarios with *rising* anything collapse immediately. The illusion is a claim, never a curve.

### 7.2 The technology scenario produces MORE cumulative debt than the no-technology scenario

From the paper's own table: **D_E = 5.240 vs D_D = 4.826.** Scenario E is identical to D except
it adds the productivity-boosting wave T(t) (Δb=0.3). Since B = b·M and b is larger with T, the
debt source (E−B) is smaller *pointwise* for a fixed trajectory — so raising technology should
*reduce* debt. The only way E ends with more debt is the feedback loop the paper does not
discuss: **higher b ⇒ higher K ⇒ higher sustainable population ⇒ higher footprint E ⇒ more
debt.** This sits in direct tension with the paper's central claim that technology "raises
output per unit of natural capital faster than debt erodes it" — i.e. that technology *offsets*
debt. In the model as reported, technology increases cumulative debt and still collapses, and
the text never reconciles this. (My own integration of E gives 5.26, matching the paper's 5.24;
the difference from D is robust.)

### 7.3 The environmental delay is applied asymmetrically

The paper centralizes τ_M as the *environmental response delay*: the stock-depletion channel
γE(t−τ_M) is lagged (Eq. 1). But the **debt** channel, which the paper itself identifies as the
dominant collapse driver for small/no delays (Scenarios B–C), uses **instantaneous** E and B:
dD/dt = max(E(t) − B(t), 0), and b(t) responds to D(t) with zero lag (Eqs. 6–7). So the "delay"
that is the paper's headline mechanism is applied to the *less* important channel, while the
*dominant* channel (debt→productivity) is treated as instantaneous. Indeed B (no delays) and C
(only τ_M) both collapse purely from instantaneous debt feedback — i.e. **without needing any
delay at all.** This is an internal inconsistency in how the central delay is deployed, and it
undercuts the framing that lags are what make overshoot dangerous.

### 7.4 "Total biospheric collapse" (M = 0) is reached only by clamping, not by the model's dynamics

Eq. (1) contains no M ≥ 0 floor. At M = 0, dM/dt = −γE(t−τ_M) < 0 whenever E > 0, so an
unconstrained trajectory would push M **negative** (negative gha — unphysical). The "collapse
to zero, then hold at zero" in Figures 1 and 5 is therefore a numerical clamp (`max(0,·)`), not a
result of the ODE. The trivial equilibrium (M, P) = (0, 0) is never analyzed, and the model has
no mechanism other than clamping to hold M at exactly zero. Consequently "total biospheric
collapse" is a boundary/fixed-point of the discretized code, not a dynamically-reached attractor
of Eq. (1).

### 7.5 The debt-repayment "persistent oscillation" claim is not generic

The paper states that η ≥ 0.02 yr⁻¹ "shifts these scenarios from collapse to persistent
oscillation." My runs give a **narrow band only**: at η ≈ 0.02–0.05 there is a decaying/large
oscillation, but by η ≈ 0.2 the tail amplitude is ≈0 and by η ≥ 1 it is essentially a stable
equilibrium with **no** oscillation. "Persistent oscillation" characterizes a specific window,
not "η ≥ 0.02." Overstated.

### 7.6 (Minor) The single-delay polynomials contain a spurious ω = 0 root

The sin²+cos²=1 elimination yields ω=0 as an extraneous solution: at λ=0 the characteristic
function is −r·a₁₁ + γ·e·a₂₁ = 0.02 ≠ 0, so λ=0 is **not** an eigenvalue. The ω=0 factor is an
artifact of squaring through the Pythagorean identity. It does not harm the paper's (correct)
conclusion that no ω>0 root exists, but it means the elimination is not a tight/irreversible
operation, and the "trivial root" should not be presented as trivial.

---

## 8. Editorial / structural errors

- **Orphan reference.** "May, R.M., 1973. Stability and Complexity in Model Ecosystems" appears
  in the reference list but is **never cited** in the body.
- **Journal name inconsistency.** Cover letter: "Ecological **Modeling**"; title page and system
  header: "Ecological **Modelling**."
- **Keyword list differs** between the abstract page ("carrying capacity; biocapacity;
  overshoot; delay differential equations; environmental debt; productivity illusion") and the
  manuscript ("…ecological footprint…, stability boundary, productivity illusion").
- **Supplementary material packaged as Word documents** (`python.docx`, `verification
  report.docx`) rather than `.py`/`.pdf`. "The code … provided as Supplementary Material" being
  inside a `.docx` is awkward for reproducible-software review.
- **PDF metadata author = "233"** (artifact).
- The manuscript embeds a "Click here to access/download" link (a submission-system URL) and
  the numbered-right-margin callout grid, both of which are Editorial-Manager artifacts that
  should be stripped from a clean manuscript.

---

## 9. Bottom line

The mathematics is largely **correct — it is the framing and the interpretation that are
over-claimed.** Specifically:

1. The marquee number **(τ_M+τ_P ≈ 80 yr)** describes a subsystem no simulation uses, sits on
   a marginal (Re<0.007, noise-level) and **ratio-dependent** boundary, and is presented as if
   it were the paper's central result.
2. The paper's actual central phenomenon — **the productivity illusion / rising biocapacity** —
   is **never simulated or plotted**; my trace shows it does not occur even transiently
   (Scenario B: B peaks at 0.509 while M is *rising*, then B collapses to 0.007 while M recovers
   to 1.19). Every presented scenario collapses. The main finding is asserted, not shown.
3. The **technology scenario accrues more debt** than the no-technology scenario (5.240 vs
   4.826), contradicting the claim that technology offsets debt.
4. The **Half-Earth cap** as implemented does **not** cap usage at half (it yields 57.5%).
5. The **"single delay cannot destabilize" proof** is valid only at an **exact equality** of
   parameters — a knife-edge that is unlikely to be robust.

*(For fairness: §3.1's condition is not merely necessary — I verified the non-delayed 2×2
Jacobian is stable whenever a₁₁<0, i.e. M*>M_max/2, since trace = a₁₁−r<0 and det = −r·a₁₁ +
γe·a₂₁ > 0 always. So that part is correct, not under- or over-stated.)*

The strongest, most defensible contribution is actually the **two-mechanism result** (debt
drives small-delay collapse; delay-driven transient drives the both-delay collapse), which I
independently confirmed. I'd recommend the authors (i) reposition this as the head
contribution, (ii) actually simulate and plot the rising-biocapacity regime, (iii) replace the
`0.5·B/r_opt` cap with `0.5·B/e`, (iv) explicitly state the knife-edge parameter dependence,
(v) tighten the "80 yr" claim into "the marginal-stability boundary in the two-delay plane is
ratio-dependent, with Re λ remaining below ~0.01 yr⁻¹," and (vi) reconcile the technology-debt
tension and the asymmetric application of τ_M.
