# Article 010 Evaluation and Verification

## Bibliographic identity

**Source file:** `uploads/paper4_perspective.txt`  
**Title:** *A Research Architecture for Sustainability: Typed Fluxes, Governance, and Robust Viability*  
**Format:** LaTeX perspective article  
**Length:** approximately 6,701 words, 534 lines  
**Formal content:** two proved theorems, typed architecture, theorem programme, two conjectures, ten-state admissibility audit, computational provenance record, empirical hypotheses  
**Evaluation status:** evaluated; integration not yet executed; substantial supersession by Article 002 expected

## Executive assessment

This is a strong research-architecture perspective. Its two proved theorems—the observation-fibre certification criterion and local threshold-horizon bound—are correct under their stated assumptions. Its ten-state analysis is unusually valuable because it demonstrates, by direct algebra and boundary checks, that formal mass cancellation does not imply positivity, closure, realizability, or a unique spectral problem.

The article is also largely a predecessor to Article 002. Article 002 contains a richer typed canonical system, fuller conservation and positivity results, the same observation-fibre and local-horizon results, constructive sampled/information/hybrid kernels, projectability, ecological reduction, coarse-graining, and more explicit scope tables. Under the minimum-paper rule, Article 010 does not presently merit a separate perspective paper. Its unique ten-state admissibility audit, stage-structure interpretation, computational reproduction targets, and selected empirical hypotheses should be preserved in a supplement or model-audit module. The architectural and theorem material should use Article 002 as the likely canonical source after source-selection review.

---

## 1. Candidate canonical architecture

The architecture correctly separates:

- typed physical amounts;
- non-conserved functional states;
- service possibility sets;
- observation and assessment;
- command, deployment, and realized pressure;
- protective and extractive feedback signs;
- safe-and-just constraints;
- causal policy classes and disturbance classes;
- state-indexed and information-state viability;
- diagnostics, thresholds, recovery, and intergenerational continuation.

### Required clarifications

1. The term \(d_x\) in
   \[
   \dot x=S_{\mathcal T}v+B_{\mathcal T}u_\partial+d_x
   \]
   must be typed. If it is a physical disturbance or omitted boundary transfer, it enters the material balance. If it is structural model discrepancy, it must not be interpreted as physical creation or destruction.
2. The incidence operator \(S_{\mathcal T}\) can contain signed entries even though primitive fluxes satisfy \(v\ge0\); this should be stated.
3. Boundary matrix \(B_{\mathcal T}\) and boundary cut notation must be harmonized with the master architecture.
4. The policy class and information pattern are well distinguished and should be retained.

Article 002 provides an expanded and more canonical version of this architecture.

---

## 2. Service and substitution architecture

The service correspondence

\[
\Gamma(x,y)\subseteq\mathbb R_+^n
\]

and finite linear pathway set

\[
\Gamma(x,y)
=
\{s\ge0:\exists a\ge0,
Ra\le x,
Qa\ge s,
Ea\le e_{max}\}
\]

are appropriate. They make substitution a pathway-feasibility question rather than an inference from one elasticity.

The text correctly limits the proposed Farkas result to a finite linear approximation. Article 002 contains the completed Farkas theorem and should be the canonical source after its verification action `V-A002-05` is discharged.

---

## 3. Observation-fibre theorem

### Statement

An exact deterministic observation-only classifier exists if and only if safety membership is constant on each observation fibre.

### Verification

The theorem and proof are correct. The construction of \(c(y)\) on \(\mathcal O(D)\) is well defined under fibre constancy, and arbitrary values outside the observation image are harmless.

The article correctly states that static aliasing does not imply dynamic output-feedback impossibility: distinct latent states may share a common safe action.

Article 002 contains the same result with additional saturation and certainly-safe-set consequences. Canonical-source selection should prevent duplicate publication.

---

## 4. Robust viability and information-state distinction

The robust quantifier order

\[
\exists\pi\in\mathbb P
\quad\forall d\in\mathcal D
\]

is correct for one causal policy against every declared disturbance. The article correctly distinguishes:

- actual-policy safety;
- viability under some policy;
- robust viability;
- state-indexed kernels;
- compatibility-set/knowledge kernels.

It also correctly distinguishes attractor containment from viability. A safe attractor can have unsafe transients or an unsafe basin, and a viability kernel need not be an attractor.

The abstract architecture does not itself prove existence or compactness of a knowledge kernel; Article 002’s restricted constructions address this gap.

---

## 5. Diagnostic and threshold taxonomies

The distinction among throughput excess, stock drawdown, threshold proximity, resilience loss, and service shortfall is valid and should be retained.

The threshold taxonomy is also sound:

- physical boundary;
- ecological functional threshold;
- service floor;
- harm/rights ceiling;
- policy trigger;
- statistical detection threshold.

A trigger or detector is not automatically a physical tipping point.

---

## 6. Capture and intergenerational scope

The capture-basin definition is mathematically coherent. The hitting time may depend on the disturbance branch while the policy rule remains common and causal.

The statement that irreversibility is relative to target, envelope, horizon, policy class, and disturbance class is correct.

The intergenerational continuation criterion is conceptually strong: terminal aggregate stock alone does not establish a viable inheritance. Generation-specific service, harm, and continuation-kernel conditions are needed.

Articles 001–002 contain stronger recoverability and intergenerational results.

---

## 7. Claim-dependent modules

The stage, spatial, nonsmooth, distributed-memory, polycentric-agent, energy/exergy, and justice modules are appropriately conditional on the claim being made.

### Verified formulas

The logistic aggregation identity

\[
\mathbb E[rX(1-X/K)]
=
r\mu_X(1-\mu_X/K)
-
\frac rK\operatorname{Var}(X)
\]

is exact.

The curvature bound

\[
|\mathbb E[f(X)]-f(\mathbb E[X])|
\le
\frac12\|f''\|_\infty\operatorname{Var}(X)
\]

is correct under the stated support and regularity conditions.

The article correctly says neither result closes the variance dynamics.

### Scope correctness

The warnings concerning exact minima, switching, smooth approximations, point versus distributed delay, informational versus material cascade states, polycentric delay heterogeneity, and quality/exergy constraints are valid.

---

## 8. Local threshold-horizon theorem

The theorem assumes an absolutely continuous stock, positive current net-depletion rate, and a rate tube

\[
(1-\varepsilon)v_0
\le
-\dot A(t)
\le
(1+\varepsilon)v_0.
\]

The proof correctly establishes existence of a crossing and

\[
\frac{H_0}{1+\varepsilon}
\le H\le
\frac{H_0}{1-\varepsilon}.
\]

The absolute-error bound

\[
|H-H_0|
\le
\frac{\varepsilon}{1-\varepsilon}H_0
\]

is also correct.

The theorem is local and conditional; it fails when rates reverse, approach zero, or leave the assumed tube. Article 002 contains a near-identical theorem and should likely be canonical.

---

## 9. Periodic-fold and exergy conjectures

### Periodic-orbit-fold persistence

The conjecture is directionally appropriate but says persistence holds if “normal hyperbolicity” and other conditions hold. At the fold orbit itself, ordinary normal hyperbolicity fails in the critical fold direction. The condition should instead specify:

- a generic fold after quotienting the trivial phase multiplier;
- an additional simple critical multiplier;
- nondegeneracy and transversality;
- spectral separation from all remaining multipliers;
- suitable smoothness of the infinite-dimensional Poincaré map;
- persistence of the unfolding under typed coupling.

This conjecture should be merged with Articles 002, 003, and 006.

### Exergy-gated suppression

The conjecture may be useful for a specific autocatalytic extractive controller, but it is not universal. Low deployable exergy can also disable protective monitoring, enforcement, and restoration. The admissible controller class, gain, gate, and safe set must be declared.

---

## 10. Ten-state material cancellation

The displayed six-state material block exactly cancels:

\[
\frac{d}{dt}
(\bar X_A+X_J+P+U+A+G)=0.
\]

Direct term-by-term verification confirms cancellation of:

- maturation;
- adult and juvenile mortality;
- harvested product and waste fractions;
- product decay;
- internal recycling;
- birth transfer;
- target exchange between \(A\) and \(G\).

The article correctly refuses to treat this identity as proof of physical admissibility.

### 10.1 Geological/support-pool boundary failure

At \(G=0\) and \(A<A^{eq}\),

\[
\dot G=-\omega_A(A^{eq}-A)<0.
\]

Thus the nonnegative boundary is not invariant. Separate donor-limited fluxes are required. This criticism is correct.

### 10.2 Variance closure failure

At \(V_N=0\),

\[
\dot V_N
=-2q\bar X_A\operatorname{Cov}(E,\bar X_A),
\]

which may be negative. The covariance is not determined by the ten states. Therefore the variance equation is neither closed nor guaranteed to remain realizable. Correct.

### 10.3 Undefined output closure

The capital/exergy equation contains \(Q\) without a constitutive relation or state equation. Different choices for \(Q\) produce different equilibria and spectra. Correct.

### 10.4 Signed memory and nonsmooth birth floor

\(Z\) is a signed informational filter, not a nonnegative conserved material stock. The maximum in \(g_B\) creates a switching surface, so the interior linearization applies only off that surface. Correct.

---

## 11. Equilibrium formulas

### 11.1 Stage-structured equilibrium

The formula

\[
\bar X_A^*
=
N_c\log\left[
\frac{P_0A^{eq}/(A^{eq}+A_0)}
{\Theta(E^*)}
\right]
\]

with

\[
\Theta(E)
=d_A(1+gd_J)+qE(1+\psi gd_J)
\]

is algebraically consistent with the interior material equilibrium at \(V_N^*=0\).

### 11.2 Effort coefficients

The coefficients

\[
C_Z=h_0g_0\frac{\eta E^*}{\Delta_{ref}},
\qquad
C_K=rac{\mu_EE^*}{K_0}
\frac{1-g_0}{g_0}
\]

follow from the stated effort law and interior equilibrium identity for \(0<g_0<1\). They cannot be extrapolated to \(g_0=0\).

### 11.3 Interior effort bound

The implication

\[
E^*
<
\sqrt{\frac{\delta_0E_{max}}{\eta}}
\]

is correct for a positive interior equilibrium under the displayed effort equation.

The boundary signs at \(E=0\) and \(E=E_{max}\) are also correctly evaluated.

---

## 12. Spectral and numerical status

The article is correct that the ten-state template does not determine a unique autonomous DDE because \(Q\) and the covariance closure are missing. Therefore it cannot determine a unique equilibrium, Jacobian, characteristic equation, delay crossing, or Floquet result.

The recorded crossing near \(\tau\approx43\) and period near 263 time units is not a numerical proposition without:

- closure equations;
- complete parameter vector;
- equilibrium and active branch;
- history and event conventions;
- characteristic-root method;
- tolerances and residuals;
- unstable-root count;
- independent reproduction.

The interpretation of

\[
\frac{d\operatorname{Re}\lambda}{d\tau}<0
\]

as a stabilizing crossing is correct for a simple tracked pair, subject to the absence of other unstable roots. It cannot support a claim that increasing delay creates instability.

---

## 13. Empirical hypotheses

The eight empirical hypotheses are potentially useful but require preregistered minimal models, observables, estimators, uncertainty, and falsifiers.

Particularly strong candidates are:

- assessment-to-deployment lag predicting phase relations after controlling confounders;
- opposite effort–stock phase relations for extractive versus protective controllers;
- juvenile models outperforming adult-only models when recruitment suppression dominates;
- spatial aggregation failure when measured variance/covariance corrections exceed uncertainty;
- component-safety misclassification under aggregate indicators.

The full architecture must not be fitted merely because a smaller model fails.

---

## 14. Publication and source-selection assessment

Article 010 is scientifically careful and contains legitimate results, but most of its architecture and both proved theorems appear in expanded form in Article 002. Maintaining both as separate papers would duplicate contribution and confuse canonical status.

Recommended treatment:

- use Article 002 as the likely canonical architectural/formal source after verification;
- preserve Article 010’s ten-state admissibility audit and computational provenance as a technical supplement or model-audit appendix;
- preserve the stage-structure interpretation and selected empirical hypotheses;
- mark duplicated architecture and theorem statements superseded-but-preserved;
- do not publish Article 010 separately unless the ten-state reconstruction yields a substantial independent validated result.

---

## 15. Verification verdict

### Verified

- observation-fibre theorem;
- local threshold-horizon theorem;
- material cancellation identity;
- noninvariance of \(G\) boundary;
- unclosed/noninvariant variance equation;
- undefined \(Q\) closure diagnosis;
- signed-memory and nonsmooth-branch diagnosis;
- equilibrium \(\bar X_A^*\) and \(\Theta(E)\) formula;
- local effort coefficients under interior assumptions;
- effort upper bound;
- stabilizing interpretation of negative crossing derivative, conditionally.

### Valid after qualification

- canonical architecture and disturbance typing;
- service/substitution programme;
- capture and intergenerational definitions;
- periodic-fold conjecture;
- exergy-gated conjecture;
- empirical hypotheses.

### Not established

- a closed ten-state model;
- positivity or realizability of the ten-state template;
- any ten-state spectral threshold or periodic orbit;
- reduction to lower-dimensional model families;
- a computed robust viability kernel;
- empirical generality.

### Required status

**Integration hold — largely superseded by Article 002; unique model-audit content preserved for supplement.**
