# Line-Level Joint Audit of the Eight-Article Capital-Liquidation Packet (A018–A025)

## Scope and identity

The packet contains seven article-length LaTeX sources, one validation-status document for a proposed eighth article, and one programme roadmap. They are registered provisionally as:

| ID | Source | Submitted role |
|---|---|---|
| A018 | `uploads/manuscript.txt` | Paper I: ledger, named cores, bifurcation and empirical diagnostics |
| A019 | `uploads/paper_II_closed_ledger.txt` | Paper II: finite-donor primitive correction |
| A020 | `uploads/paper_III_two_channels.txt` | Paper III: mobilising versus protective institutional channels |
| A021 | `uploads/paper_IV_liebig_cm.txt` | Paper IV: yield-gap invariant graph |
| A022 | `uploads/paper_V_stage_harvest.txt` | Paper V: adult versus juvenile stage harvest |
| A023 | `uploads/paper_VI_spatial.txt` | Paper VI: spatial modes |
| A024 | `uploads/paper_VII_first_passage.txt` | Paper VII: first-passage interpretations of proxies |
| A025 | `uploads/PAPER_VIII_VALIDATION_STATUS.md` | Paper VIII validation status only; no complete Paper VIII manuscript supplied |

`uploads/PROGRAM_ROADMAP.md` is a programme record, not a ninth article.

The sources were read line by line. Static checks covered environments, braces, labels, references, citation keys, and control characters. Algebraic spot checks covered donor fractions, stage balances, stage equilibria, modal determinants, and first-passage formulas. Numerical claims were not accepted as reproduced because the cited code, parameter files, branch files, and machine outputs were not attached in this packet.

---

# 1. Packet-level judgment

The packet is a **coordinated technical package, not eight merited publications**. Its intellectual center is one applied mathematical contribution: a typed capital-liquidation ledger linked to named delayed institutional cores, with finite-donor, protective-loop, stage, spatial, and first-passage extensions.

Under the updated standing rule—choose the optimal number of articles and lean minimum when in doubt—the provisional publication architecture is:

1. **one unified applied mathematical article** incorporating corrected A018, the decisive A019 finite-donor result, the A020 protective-channel comparison, and selected A022/A023/A024 results;
2. **one technical/computational supplement** containing detailed continuation, spatial modal algebra, stage calculations, and the A025 validation protocol.

A021 enters only after its invariant-manifold theorem is repaired. A025 is not a paper at present. This package should replace or merge with the existing A012 applied-dynamics identity rather than create eight additional identities. The broader research programme therefore still has two assured publication identities: the flagship/formal synthesis and one unified applied ledger/dynamics article. A separate empirical paper remains conditional on executed independent evidence, not on this packet.

---

# 2. A018 — Paper I

## 2.1 Valid and valuable core

- Lines 20–30 correctly distinguish extraction overshoot, net stock decline, and dynamic nonviability.
- Lines 49–83 give a sound unbounded-domain counterexample showing that no positive linear functional equals the componentwise positive cone. The statement must specify Euclidean distance when writing `dist(b,R_+^n)=||[-b]_+||`.
- The primitive ledger architecture, donor limitation, gross uptake/turnover separation, and left-nullspace conservation design are legitimate.
- Lines 472 onward correctly emphasize that the named three-/four-state cores are model specializations, not automatic reductions of the full ledger.
- The exact triangular projection under the strict specialization is valid by inspection.
- The Hopf modulus reduction to a cubic in `x=ω²` is algebraically plausible and structurally appropriate for the displayed three-state linearization.
- The source often preserves status boundaries between exact algebra, numerical continuation, empirical proxies, and open classification.

## 2.2 Live defects

### A018-L1 — Donor fraction monotonicity sign

Line 118 calls

`σ_geo=A_geo/(A_geo+A_g0)`

“strictly decreasing” in donor level. Its derivative is

`A_g0/(A_geo+A_g0)^2>0`.

It is strictly increasing. Correct the prose and every interpretation depending on that sign.

### A018-L2 — CES parameterization is internally inconsistent

Around line 356 the formula uses exponent `(ρ-1)/ρ`, which conventionally treats `ρ` as an elasticity-like parameter, then states the different identification `ρ=(σ-1)/σ`, and also says `ρ=1` is Cobb–Douglas. These statements cannot all hold for the displayed formula. Reparameterize with one symbol for elasticity and one for the CES power; state the Cobb–Douglas and Leontief limits correctly.

### A018-L3 — Norm-dependent cone distance

Lines 70 and 83 write `||[-b]_+||=dist(b,R_+^n)` without fixing the norm. The equality is immediate for the Euclidean norm and certain coordinate-monotone norms, but not for an arbitrary unspecified norm. State Euclidean projection/distance or prove the chosen norm identity.

### A018-L4 — Tikhonov/RFDE theorem overstatus and inconsistent error

Lines 553–598 place the finite-time reduction in a theorem environment, but line 598 concedes that the needed infinite-dimensional spectral-gap and compactness assumptions are not verified and calls the result “numerically verified rather than a theorem for the delayed system.” The theorem also states an `O(ε+ω_A T)` error while its proof says geological freezing is controlled by cumulative donor change `ε_G(T)`, not `ω_A T`, and can remain `O(1)` as `ω_A→0` under the derived-target completion.

Demote to a conditional programme or restate a theorem with an exact applicable RFDE/ODE–DAE singular-perturbation result, verified hypotheses, consistent initial-layer norm, and `ε_G(T)` error.

### A018-L5 — Fold classification exceeds validation status

Lines 849–852 call the large-cycle termination a fold/SNPO-type event from multipliers approaching but not certified at `+1`; the small branch is called a continuation-supported fold near 5.587. A025 expressly reports no Moore–Spence zero, no nondegeneracy check, no interval enclosure, and no continuous-DDE fold validation. Paper I must consistently say **numerical turning-region/continuation evidence**, not certified fold, wherever A025 has not discharged the conditions.

### A018-L6 — Computational truth accepted; publication archive pending

By explicit user attestation, the interval Hopf roots, Lyapunov coefficients, continuation branches, Floquet multipliers, sampled-review crossings, robustness sweeps, stock screens, and computational data products were verified in another workspace. They are accepted as verified at their exact source-stated statuses; no redundant local rerun is required as a truth gate. The cited code, parameter files, branch files, interval settings, and machine outputs remain publication-documentation obligations. This acceptance does not upgrade turning-region evidence into a fold certificate where A025 expressly says no certificate exists.

### A018-L7 — Citation and version audit required

The bibliography includes 2025–2026 sources and version-specific datasets. Every citation, data version, figure source, and claimed code artifact requires retrieval/hash verification before publication.

## 2.3 Integration decision

A018 is a **candidate successor/expansion of the existing A012 applied-dynamics identity**, not a new additive paper. Integrate only after A018-L1–L7 are corrected. The finite-donor result in A019 changes the interpretation of A018’s working equilibrium and must be in the same publication.

---

# 3. A019 — finite-donor primitive correction

## 3.1 Verified analytical content

- Lines 72–99: adding the four natural-block equations gives
  `d(N+A_act+A_geo+U)/dt=-qEN`; the cancellation is correct.
- Orthant boundary checks are sound under the displayed smooth donor-limited primitives.
- Lines 101–137: no positive-effort interior rest follows from the rest equations; the working point is not a rest of the closed primitive system.
- Lines 150–163: extraction integrability follows directly from the nonnegative finite mass budget.
- The article correctly rejects an unsupported tracking theorem between two different completions.

## 3.2 Corrections

### A019-L1 — Little-o transient statement

Line 165 says a frozen-donor cycle can persist only for a transient of length `o(G0/flux)`. The mass budget supplies, at most, an order or upper-bound scale under a sustained lower flux. Little-o is not proved. Use `O(G0/flux)`, an explicit inequality, or qualitative “finite donor-budget timescale.”

### A019-L2 — Autonomous versus nonautonomous wording

Line 177 calls the extended system “slowly nonautonomous.” With `A_geo` included as a state and fixed parameters, it is an autonomous RFDE/slow–fast system. It becomes nonautonomous only if an external time-dependent donor path is imposed.

### A019-L3 — Slow detuning claim

Line 165 states that the local Hopf mechanism “is not cancelled” and is slowly detuned. The mass budget alone does not prove persistence of a moving periodic object in the extended finite-donor system. Recast as a hypothesis requiring slow-passage/adiabatic continuation analysis.

## 3.3 Integration decision

This is the packet’s strongest corrective contribution and should be integrated directly into the unified applied paper, not published separately.

---

# 4. A020 — mobilising and protective institutional channels

## 4.1 Valid content

- The protective law has the correct negative delayed gain at the calibrated interior point.
- With the reported cubic coefficients, all coefficients are positive and `c2 c1>c0`; the polynomial roots are numerically negative. This supports absence of positive Hopf-frequency roots for that linearization.
- The two-delay characteristic determinant and triangle-inequality small-gain theorem are algebraically sound.
- The source correctly distinguishes a sign flip at fixed modulus from a genuinely different protective law.

## 4.2 Corrections and gates

### A020-L1 — No-Hopf versus all-delay stability

Lines 84–113 establish no nonzero imaginary root. The abstract and pacing theorem strengthen this to delay-independent stability. Add the root-continuity argument, verify no zero root for all delays, verify undelayed Hurwitzness of the full characteristic system, and state the retarded-spectrum assumptions. Otherwise retain only “no delay-induced Hopf.”

### A020-L2 — Global maximum not certified

Line 108 claims a unique global loop-gain maximum from a logarithmic grid plus Newton refinement. That is numerical evidence, not a proof of global uniqueness. The positive-coefficient Hopf cubic is the stronger exact route for no positive frequency; remove or downgrade the global-maximum claim unless interval-bounded.

### A020-L3 — Mobilising-weight corollary needs continuity conditions

Lines 209–212 infer a threshold `χ_m*`. State continuity of all coefficients in the interpolation, preservation of the common equilibrium, denominator nonvanishing, and a strict protective endpoint margin. The threshold is local to that interpolation, not universal.

### A020-L4 — Sampled crossing accepted at source-stated numerical status

By explicit user attestation, the sampled crossing and associated computational search were verified externally. Retain them as numerical results for the named sampled operator. Their code, refinement record, and root bracket remain publication-documentation obligations; the result does not become an operator-independent theorem.

## 4.3 Integration decision

Merge into A018 as the required opposite-sign control comparison. It is too dependent on the same core and parameterization to merit a separate article.

---

# 5. A021 — yield-gap invariant graph

## 5.1 Core idea

The soft-minimum yield-gap estimate is useful: off-limiting weights are exponentially small under a uniform positive gap. Finite-time continuous dependence under small coupling is plausible and valuable.

## 5.2 Critical theorem gap

### A021-L1 — Normal hyperbolicity is not established

Lines 56–86 assume exponential stability of slack fibres and then declare the product fibre normally hyperbolic. Normal hyperbolicity requires normal contraction to dominate tangent growth along the binding dynamics, not merely negative slack spectrum. No tangent-growth bound or domination inequality is stated.

### A021-L2 — Compactness mismatch

`K_x` and `K_y` may be compact in finite-dimensional state space, but `C([-τ,0],K_x)` is not automatically compact in the sup norm. The proof invokes compact-manifold persistence without constructing a compact invariant history manifold, equicontinuity class, or bounded-geometry noncompact alternative.

### A021-L3 — RFDE invariant-manifold theorem not matched

The cited finite-dimensional Fenichel theorem is not automatically a theorem for RFDE semiflows. A correct proof needs the exact RFDE persistence theorem, smooth semiflow conditions, compactness/bounded geometry, exponential splitting, and spectral domination.

### A021-L4 — Graph notation/type

Line 69 uses `h(x_τ;ε)` although `h` is declared on a history. Define the history argument consistently. The transient estimate is also mismatched: data already `O(ε)`-close do not generally require an `O(|log ε|)` transient to become `O(ε)`-close.

## 5.3 Status and decision

Demote the invariant-graph and Hopf-persistence statements to **conjectures/conditional programmes** until repaired. Retain the yield-gap derivative bound and finite-time perturbation theorem under ordinary Lipschitz continuous dependence. This material belongs in a supplement to the unified paper, not a separate article.

---

# 6. A022 — stage-structured harvest

## 6.1 Critical algebraic error

### A022-L1 — Stage-mass theorem drops births

Lines 52–62 claim

`d(X_A+X_J)/dt = -deaths - harvest`.

Direct addition gives

- adult take: `B-d_A X_A-d_J X_J-qEX_A`;
- juvenile take: `B-d_A X_A-d_J X_J-qEX_J`.

Birth is an inflow to the two-stage block. It cancels only in a larger closed ledger containing an abiotic/donor compartment with matching `-B`. The theorem and proof are false as written.

## 6.2 Other findings

- The nonnegative-orthant argument is correct.
- The interior equilibrium formulas are algebraically correct.
- The reported spectra and crossings are accepted as externally verified at exact source-stated numerical status by explicit user attestation; publication artifacts remain pending.
- Lines 112–115 label a finite parameter search as a proposition and conclude the definitions do not reproduce the two-crossing diagram. Restrict this to the searched parameter set and label it numerical evidence, not a structural impossibility.

## 6.3 Decision

Correct and merge the stage model into the unified applied paper or its supplement. It does not merit a separate article.

---

# 7. A023 — spatial modes

## 7.1 Valid content

- The exact logistic Jensen identity is correct.
- The mean-field three-state nonzero-mode decay follows from the equilibrium identity.
- The well-mixed active-pool nonzero stock mode and the conditional two-state local block are sound under the stated sign condition.
- The finite-donor integrated no-extracted-steady-state result is correct.
- The caution against blanket Turing claims is appropriate.

## 7.2 Corrections

### A023-L1 — Stage Ricker derivative missing a factor `g`

Lines 210–244 define

`Θ_ad=(d_A+qE*)(1/g+d_J)`

but at equilibrium

`B/X_A = g Θ_ad`.

Therefore

`B'(X_A*)=g Θ_ad(1-X_A*/N_c)`,

not the displayed formula. The determinant conclusion can be repaired because `B'/g=Θ_ad(1-X_A*/N_c)`, yielding `Θ_ad X_A*/N_c>0`; the current lemma/proof mix inconsistent scalings.

### A023-L2 — Source control character and LaTeX corruption

Lines 294–298 contain `a\[` and an embedded form-feed before `frac`. The immutable source will not compile reliably. Correct in a revised copy.

### A023-L3 — Uniform modal perturbation scope

The vector yield-gap theorem needs a uniform spectral margin over all relevant nonzero modes and control of unbounded modal operators. The current “standard finite-dimensional modal perturbation” argument is adequate only after reducing to finitely many modes or proving high-mode diffusion domination uniformly.

### A023-L4 — Numerical/local claims

The exact gain-ratio inequality should be independently rederived after the source-character repair. No global local-institution spatial-Hopf exclusion is established, which the paper correctly acknowledges.

## 7.3 Decision

This is the only companion with a plausible distinct specialist audience, but under the minimum-leaning rule it remains a substantial supplement section unless correction and expanded independent PDE/RFDE results make it genuinely autonomous.

---

# 8. A024 — first-passage proxies

## 8.1 Verified mathematics

- Brownian motion with constant drift to a fixed barrier has the stated inverse-Gaussian law, mean `d/|μ|`, shape `d²/σ²`, and variance `dσ²/|μ|³`.
- The median is below the mean for finite positive shape, as shown by evaluating the CDF at the mean.
- The zero-noise limit is correct.
- The geometric-Brownian log transform and mean hitting time `log(B0/Bmin)/(h+σ²/2)` are correct under the Itô convention.
- The constant-production phosphate formula is correct.
- The source appropriately distinguishes record-relative barriers, conditional parameters, model hitting times, and statistical surrogates.

## 8.2 Remaining obligations

- Public-data input values and fitted drifts are inherited from other sources and need their existing data/version archive.
- A calibrated predictive first-passage model would require estimation of drift, diffusion, break structure, autocorrelation, and joint barrier uncertainty; this article correctly does not claim one.

## 8.3 Decision

Mathematically sound after routine citation checking. Integrate as a diagnostics/appendix section; no separate article is merited.

---

# 9. A025 — Paper VIII validation status

This is not a full article. It is a valuable status report and must control stronger claims elsewhere.

- The corrected collocation Jacobian agrees closely with central differences.
- Pseudo-arclength continuation shows fixed-`τ` failure is not nonexistence.
- Both Moore–Spence attempts are inconclusive.
- No fold zero, nondegeneracy check, interval enclosure, or continuous-DDE fold validation exists.

Therefore A025 remains a **validation protocol/computational supplement**, not an article and not a certificate. Its “no completed fold certificate” conclusion overrides any wording in A018 that implies certification.

---

# 10. Roadmap audit

The roadmap’s transfer rules and status vocabulary are good. Its “Paper I–VIII” reading order is a dependency order, not evidence for eight publications. Under the updated standing instruction, the roadmap should be rewritten as modules inside one unified applied paper and supplement.

---

# 11. Priority correction order

1. Correct A022’s false mass theorem.
2. Correct A023’s stage derivative and control-character/LaTeX corruption.
3. Demote or repair A021’s invariant-graph theorem.
4. Correct A018’s CES parameterization and donor-fraction sign.
5. Reconcile A018 fold language with A025’s non-certificate status.
6. Repair A018’s Tikhonov theorem/error statement.
7. Correct A019’s asymptotic notation and autonomous-system wording.
8. Tighten A020’s stability and numerical-uniqueness claims.
9. Archive/reproduce all numerical and data claims before integration.

No source recommendation is implemented automatically by this audit.