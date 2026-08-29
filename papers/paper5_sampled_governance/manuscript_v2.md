# Sampled Governance, Empirical Identification, and Falsification Design: The Sample-and-Hold Model of Periodic Review, Spectral and Power Screens, and the Northern Cod Case at Its Exact Causal Status

**Paper 5 of the programme's five-paper publication architecture (general-sustainability, A001–A025).** Every concordance-sourced statement is stated at its row-verified status; the sampled-data model, its positivity proposition, and the prospective designs are stated in full; empirical records carry their source-specific evidentiary level; diagnostics are never promoted to causal claims; no status is promoted.

*Second edition (batch-5 corrections, 2026-08-29): the Schaefer specialisation sentence of §6.2 is corrected (the Schaefer model is the degenerate member of the depensation family, not a parameter value of it); the case-search sentence of §6.1 dates La Mancha Oriental's relapse; the scored-empirics inventory counts the four Wave E manuscripts; the status ledger's one cross-reference identifier is marked; in-text citation hooks are attached at the data-, method-, and lineage-bearing points. The adjudication record is `BATCH5_JOINT_AUDIT_EVALUATION.md`; no theorem, number, claim status, or row count changes.*

---

## Abstract

This article develops the empirical and methodological layer of a typed theory of sustainability: how periodic review, observation timing, implementation delay, and uncertainty alter an extractive-feedback mechanism, and how that alteration can be identified and falsified. The representation is a sample-and-hold model of periodic review — between reviews a logistic resource stock evolves under held effort, a filtered nonnegative deficit signal carries institutional memory, and a projected explicit effort update (the extractive controller SD-E-B3, an explicit controller discretisation and not a generic harvest-control rule) resets effort at each review, with assessment separated from observation and latent state. The sampled state space is forward invariant: positivity, signal nonnegativity, and effort admissibility hold by induction over review intervals. The rapid-review limit is a finite-horizon consistency statement that establishes neither stability at any positive review interval nor the reported response regions. Delayed-recruitment calculations, classified from long-horizon trajectories rather than Poincaré-map multipliers, locate exploratory response regions near 3–4 yr (anchovy-class) and 6–12 yr (sprat-class) review intervals, with cod-class convergence over the tested 1–20 yr grid; the windows are zeros of the stage-structured review map, a different operator from the continuous-delay and hold maps, and the two-operator discipline governs every transfer. A multiplicity-controlled Lomb–Scargle screen of a 42-stock annual-review cohort found no robust target-band peak, and injected-signal power on 100–200 yr synthetic records is high only in favourable noise and record-length regimes; the null is a selected-cohort consistency check, not a causal test. A structured search across more than thirty resource and produced-capital systems returned zero eligible cases under four criteria that exclude confounded tests. The northern cod case (NAFO 2J3KL) is carried at its exact causal status: the positive result is the two-window split — crash interpretation formulation-dependent, non-recovery unexplained in both formulations — with the scalar-autonomous phase-line obstruction as the mathematics and every unreproduced quantity stated as a reproduction target. The paper's constructive content is its falsification programme: governance-event panels, quasi-experimental timing, out-of-sample mechanism comparison under a displacement discipline, randomized human-in-the-loop experiments, and closed-loop management strategy evaluation crossing review interval, decision and deployment lags, controller sign, and uncertainty class; five declared outcomes count against the mechanism. Every claim carries its concordance provenance at its closed status.

---

## 1 Introduction

### 1.1 The question this paper answers

**How do periodic review, observation, implementation delay, and uncertainty alter the scarcity-mobilising mechanism, and how can the alteration be identified and falsified empirically?**

Two failure modes motivate the question. The first is *architecture substitution*: a continuous delay differential equation assumes a delayed signal entering a continuously evolving control law, while many real institutions observe or assess a resource at discrete times, choose a rule-based action, and hold that action until the next review; replacing one architecture by the other can move or delete stability boundaries, so the governance architecture itself must be tested, not merely re-parameterised. The second is *causal promotion*: spectral peaks, cohort cycles, and crisis-driven monitoring records circulate as evidence for institutional-delay mechanisms when they carry no controller-sign information at all. This paper builds the layer that resists both failures: the review interval is treated as an operator with its own spectrum, every diagnostic is typed, and every empirical record carries its evidentiary level with its restrictions on the line.

### 1.2 What enters this paper

Paper 5 is the empirical-identification and falsification-design paper of the five-paper series. Its retained set consists of the 57 concordance rows routed to it by the programme's destination pass: the periodic-review source's model family, response regions, robustness and spectral diagnostics, screen, power analysis, and case search (A011 — 23 rows, the empirical core); the northern cod case (A014 — 10 rows); the eligible adaptive-capacity and distributive-measurement material (A016 — 6 rows); the dimensionless identifiability chart and the empirical screen of the unified applied source (A018 — 2 rows); the observation and epistemic layer (A001 — 4 rows; A002 — 3 rows; A006 — 5 rows; A010 — 1 row; A024 — 2 rows); and the sampled-review variant registration (A003 — 1 row). Per-row provenance identifiers (`CC-A0XX-YYY`) link every statement to the 409-row concordance inventory (source location, canonical module, mapping type, evidence status, destination). Six manuscript-native entries carry the paper's own local content: the governance-time ontology, the forward-invariance (positivity) proposition, the SD-E-B3 instance of the finite-horizon consistency statement, the four prospective identification designs, the closed-loop management-strategy-evaluation design, and the falsification criteria (§10). Four further manuscript-native entries restate source-declared content that carries no concordance row: the architecture-level empirical hypotheses (§5.2), the assessment-table values of the cod case's two windows (§6.3), the alternative-mechanism enumeration behind the case-search criteria (§6.1), and the fixed-$\tau$ idealisation caveat (§7.1).

### 1.3 Claim-status discipline

Every statement below carries a status label from the programme's hierarchy (the A002 source's own table, adopted programme-wide):

| Status | Admission rule |
|---|---|
| Axiom/definition | Declares an object, domain, type, or convention; asserts no empirical truth |
| Identity | Follows by construction or direct algebra |
| Theorem | Complete proof under explicit mathematical assumptions |
| Conditional theorem | Complete implication whose hypotheses are not established for every intended application |
| Conjecture | Precise unproved statement with a declared proof gap and disproof route |
| Counterexample/limit | An explicit construction establishing that an implication fails |

Empirical and computational records additionally carry their source-specific evidentiary level, stated per record and never relaxed:

| Evidentiary level | Meaning |
|---|---|
| Defined source object | A definition or declared object verified in the source; no empirical truth asserted |
| Source-specific empirical status | A computational or empirical record whose source-declared restrictions govern its use (exploratory finite-grid classification, author calculations, conditional simulations) |
| Source status accepted, artifact pending | The source's statement is accepted at face value; the reproduction artifact is declared and not attached |
| Status crosswalk required | The record's claim type must be restated at the governing classification before use (e.g. formulation attribution, background-only content) |
| Conditional/open | Hypothesis, conjecture, or open problem with declared test requirements |

Two rules govern this article. **No promotion:** a conditional theorem is never stated as a theorem; an exploratory response region is never stated as a stability boundary; an arithmetic transformation is never stated as an independent observation; a formulation attribution is never stated as a causal claim. **No silent transfer:** a status proven for one model class does not transfer to extensions, reductions, or applications without a declared map, and the diagnostic no-transfer rule of the architecture is binding throughout — **a diagnostic is not a causal claim** [CC-A002-005, Paper 1 owner].

### 1.4 Provenance and auditability

All 57 of this paper's concordance rows are row-closed at content level (`row_verified`, dated scientific passes over full source reads: A001, A002, and A011 on 2026-08-27; A003, A006, A010, A014, A016, A018, and A024 on 2026-08-28); they are stated below at exactly those statuses, with no promotion. Content-level acceptance means the row's existence, kind, proof presence, module, and mapping type were verified against the source; it is not a theorem-status promotion, and the cross-module interface contract remains an open obligation recorded per row. Of the 409-row concordance, 354 rows are row-verified; the 27 rows that remain open are exactly the three conditional-paper sources (A021, A022, A023) — none of them behind this paper.

### 1.5 Relationship to the programme

This is Paper 5 of five assured papers. Paper 1 owns the typed canonical architecture, including the diagnostic types and their no-transfer rule; this paper carries a Minimal Working Realization of the observation–governance objects it needs and never transfers a status across modules. Paper 2 owns the theorem atlas: the sampled, hybrid, and information-state kernel family (F05) and the observation and epistemic-viability family (F03) are stated and proved there, and where this paper needs one of those objects it states the local instance and cross-references the owning entry — the atlas is the map, this paper owns the empirical identification and falsification layer. Paper 3 owns the conserved-material ledgers, the componentwise depletion diagnostics, and the worked fisheries ledger cases; the spectral screen's input cohort is an analysis-side criterion, not a ledger example, and the boundary is stated at the screen (§5.3). Paper 4 owns the named retarded systems, their bifurcation analysis, and the delayed-recruitment registration object; the response-region outputs read here ride that registration at its declared status (§3.4). The programme's four scored Wave E manuscripts are outside this paper's scope; they enter as programme context at the cod case (§6.3) and in the admission-standard discussion (§9). No paper depends on another for a locally load-bearing definition: the sampled model, its conventions, the screen, and the designs are stated in full here.

---

## 2 The sample-and-hold model of periodic review (Minimal Working Realization)

### 2.1 Governance time: seven objects and the no-collapse rule

The model's declaration layer separates the time objects of governance [MS-Native-1]:

| Object | Definition |
|---|---|
| Observation interval $T_{\rm obs}$ | Time between raw measurements |
| Assessment interval $T_{\rm assess}$ | Time between formal state estimates |
| Review interval $T_r$ | Time between opportunities to change the command |
| Decision lag $\tau_{\rm dec}$ | Assessment completion to formal decision |
| Deployment lag $\tau_{\rm dep}$ | Decision to implemented change in extraction pressure |
| Ecological response lag $\tau_{\rm eco}$ | Implementation to detectable ecological response |
| Memory timescale $\tau_m$ | Relaxation time of a filtered institutional signal; not a discrete delay |

These quantities are not collapsed into one "governance lag" unless the empirical record cannot resolve them and the aggregation rule is declared: reviews can be annual while deployment is delayed, and observations can be frequent while decisions are legally fixed for several years. The separation is not itself an identifiability result — stock and realised-effort series alone may identify only a combined closed-loop phase shift, and separate estimation of assessment, decision, and deployment delays requires dated observation releases, assessment products, commands, and implementation records, or a proved structural-identifiability argument for the declared observation model. The review opportunity is not the same as response sign: the extractive command studied here raises effort in response to a perceived decline; a protective controller that lowers effort is a different model and enters as a comparator (§2.3).

### 2.2 Process, observation, and assessment equations

Let review times be $t_n=nT_r$. Between reviews, extractive effort is held at $E_n$ and the resource stock follows the logistic process under held effort [CC-A011-001]:

$$
\dot N(t)=rN(t)\left(1-\frac{N(t)}{K}\right)-qE_nN(t),
\qquad t\in[t_n,t_{n+1}),
\tag{1}
$$

while the institutional signal $Z$ is the filtered nonnegative deficit [CC-A011-002]:

$$
\dot Z(t)=\frac{\Phi\bigl(qE_nN(t)-S(N(t))\bigr)-Z(t)}{\tau_m},
\qquad \tau_m>0,
\tag{2}
$$

with $S(N)=rN(1-N/K)$ the surplus production and $\Phi\ge 0$ a nonnegative signal map with memory timescale $\tau_m$. The assessment available at review $n$ is

$$
\widehat Z_n=\mathcal A_n\!\left(\{Y_j:t_j\le t_n-\tau_{\rm dec}\}\right),
\qquad
Y_j=\mathcal O\bigl(N(t_j)\bigr)+\varepsilon_j,
\tag{3}
$$

which separates the latent process $N$, the observations $Y$, and the assessments $\widehat Z$; measurement and assessment errors need not be independent or Gaussian.

### 2.3 The review map and the controller family

The review map is the projected explicit step [CC-A011-003]:

$$
E^{\rm cmd}_{n+1}=\Pi_{[0,E_{\max}]}\left\{E_n+T_rF_B(E_n,\widehat Z_n)\right\},
\tag{4}
$$

with the effort law

$$
F_B(E,Z)=\left(1-\frac{E}{E_{\max}}\right)
\left[
\eta E\left(\frac{Z}{\Delta_{\rm ref}}-\frac{E}{E_{\max}}\right)
+\delta_0\frac{Z}{Z_{\rm ref}+Z}
\right],
$$

together with the shifted, floored softplus signal map

$$
\Phi_k(s)=\max\left\{0,\ \frac{1}{k}\log\!\bigl(1+e^{ks}\bigr)-\frac{\log 2}{k}+\delta\right\}.
$$

Equations (1)–(4) with $\Phi=\Phi_k$ constitute the extractive controller **SD-E-B3** [CC-A011-004] — the sample-and-hold counterpart of the M3-B extractive mobilisation law of the registered delay family (Paper 4 owns the continuous family). It is an explicit controller discretisation, not a generic harvest-control rule and not a model of protective quota reduction. Alternative controllers receive distinct identities [CC-A011-005]: **SD-P** (protective update, response to decline entering with the opposite sign), **SD-F** (fixed multi-year plan with no state-responsive update between scheduled resets), and **SD-H** (hybrid controller with limits on annual change, emergency triggers, or legal overrides). SD-P, SD-F, and SD-H are declared comparators for the prospective management-strategy evaluation (§7.5), not completed numerical experiments; a fixed plan and a state-responsive plan with the same nominal review period are not the same intervention.

### 2.4 Registration conventions and the sampled representation as the default

The deterministic record fixes a one-step flow-then-update convention: $E_n$ is held on $[t_n,t_{n+1})$ and the assessment indexed by $n$ defines the next command; assessments are contemporaneous and exact, $\tau_{\rm dec}=\tau_{\rm dep}=0$, no decision or deployment queue is present, and multiplicative assessment error enters only the designated robustness experiment; a positive $\tau_{\rm dep}$ requires an explicitly registered hold or interpolation rule [CC-A011-018]. These are registration requirements declared by the source and not discharged: the solver configuration and initial histories are not attached, and until the computational record is complete the stage-output values carry exploratory status rather than the status of reproducible numerical propositions (§11).

The sampled-governance representation is the default institutional form of the programme's institutional-feedback model class: at review times institutions observe data and update prescriptions, and the implemented control is held or dispatched by a stated rule until the next review [CC-A003-013]. The registered bridge discipline is binding: a continuous-delay approximation to the effort equation is admissible only after specifying the review interval, hold rule, implementation lag, and approximation error — a sampled map can exhibit flip, Neimark–Sacker, or border-collision behaviour not captured by continuous-delay Hopf terminology. The sampled-review variant itself is a registered obligation at the stress-test registry's no-artifact status (Paper 4 owns the registry; this row rides the sampled-governance paper). The formal safety objects for this architecture — the sampled robust-viability kernel and the inter-sample-safe held-control tube kernel — are the atlas's [Paper 2, family F05: CC-A002-021, CC-A002-025]; this paper states the model and its conventions, and the kernel constructions are cited, not reproduced.

---

## 3 Positivity and the review-interval spectrum

### 3.1 Forward invariance of the sampled process

**Proposition (forward invariance) [MS-Native-2].** Suppose $N(0)\ge 0$, $Z(0)\ge 0$, $E_0\in[0,E_{\max}]$, and $\Phi$ is non-negative. Let every effort command be projected by $\Pi_{[0,E_{\max}]}$, and let any between-review deployment interpolation remain in the convex interval joining consecutive commands. Then $N(t)\ge 0$, $Z(t)\ge 0$, and $E(t)\in[0,E_{\max}]$ for every time at which the sampled solution exists.

*Proof.* Proceed by induction over review intervals. Suppose at a review time $t_n$ that $N(t_n)\ge 0$, $Z(t_n)\ge 0$, and the command to be held or interpolated lies in $[0,E_{\max}]$. Projection places the next command in the same closed interval; a hold retains an endpoint of that interval, and any convex interpolation $E(t)=(1-\theta(t))E_n+\theta(t)E_{n+1}$ with $0\le\theta(t)\le 1$ also remains in $[0,E_{\max}]$. On $[t_n,t_{n+1}]$, Eq. (1) is $\dot N=N[r(1-N/K)-qE(t)]$, so for a positive initial value

$$
N(t)=N(t_n)\exp\left\{\int_{t_n}^{t}\left[r\left(1-\frac{N(s)}{K}\right)-qE(s)\right]ds\right\}>0,
$$

while if $N(t_n)=0$, uniqueness gives the identically zero solution on the interval; $N$ cannot become negative. Set $\nu(t)=\Phi(qE(t)N(t)-S(N(t)))\ge 0$. Variation of constants in Eq. (2) with $\tau_m>0$ gives

$$
Z(t)=e^{-(t-t_n)/\tau_m}Z(t_n)+\frac{1}{\tau_m}\int_{t_n}^{t}e^{-(t-s)/\tau_m}\nu(s)\,ds\ \ge 0 .
$$

All three inequalities therefore hold through $t_{n+1}$; they hold at $t_0=0$ by hypothesis, and induction proves them on every review interval for which the sampled solution exists. ∎

Positivity, boundedness, persistence above a threshold, and viability are distinct properties; the proposition establishes positivity and effort admissibility only.

### 3.2 The rapid-review limit and what it does not establish

Define $u=(N,Z,E)$ and the continuous no-delay system

$$
\dot u=G(u)=
\begin{pmatrix}
S(N)-qEN\\[2pt]
\bigl[\Phi(qEN-S(N))-Z\bigr]/\tau_m\\[2pt]
F_B(E,Z)
\end{pmatrix}.
$$

**Remark (finite-horizon rapid-review consistency, SD-E-B3 instance) [MS-Native-3].** The formal coverage of this statement is the atlas's conditional theorem on finite-time sample-and-hold convergence [CC-A002-034, Paper 2 owner], in the sampled-data tradition of convergence to the underlying continuous-time system via approximate discrete-time models (Nešić and Teel 2004); the instance reads as follows. Suppose $G$ is continuously differentiable with bounded derivative on a compact neighbourhood containing the compared trajectories on $[0,T]$, assessments equal the contemporaneous state, no additional decision or deployment queue is present, projection is inactive, and the sampled and continuous systems share the initial state. The frozen-effort flow followed by the explicit effort step then has a one-step defect of order $O(T_r^2)$ relative to the exact flow of $G$; the usual discrete Gronwall estimate yields an $O(T_r)$ review-time error and uniform convergence on every fixed finite horizon as $T_r\to 0$.

This is a numerical-approximation property, not a finite-review stability theorem. It gives no uniform-in-time estimate, does not preserve stability automatically, and does not control any trajectory-classified response region reported below. It excludes active projection, delayed or erroneous assessment, a deployment queue, and stochastic updates. In particular, it neither identifies a finite $T_r$ with a continuous discrete delay nor implies that sufficiently small positive $T_r$ is stable when the continuous target is unstable.

### 3.3 Sampled-data stability terminology

For a deterministic sampled system, the inter-review flow and the review update combine into a Poincaré map $X_{n+1}=\mathcal P_{T_r}(X_n)$, where $X_n$ includes the ecological state, memory, held command, and any explicitly modelled queue. A fixed point is locally asymptotically stable if and only if every eigenvalue of $D\mathcal P_{T_r}(X^*)$ lies inside the unit disk. A verified crossing through the unit circle as the fixed parameter $T_r$ changes is a **sampled-data parameter bifurcation**; it is not rate-induced tipping, which requires a nonautonomous parameter path (such as $\dot\mu=\epsilon$) and a loss of tracking as the ramp speed changes (the tipping taxonomy: Ashwin, Wieczorek, Vitolo, and Cox 2012). The calculations reported below did not evaluate $D\mathcal P_{T_r}$, a monodromy matrix, or Floquet multipliers: classification used long-horizon trajectories, tail amplitudes, multiple histories, and integration-step refinement, so the reported bands are finite-grid, trajectory-classified response regions and no Neimark–Sacker, flip, or other multiplier-crossing classification is claimed. A future boundary calculation must report the exact flow/update ordering and information pattern, all observation and deployment lags, the derivative construction for $\mathcal P_{T_r}$, multiplier trajectories and crossing directions, nonlinear trajectories on both sides, and numerical refinement — the requirements that distinguish a located bifurcation boundary from a trajectory summary.

### 3.4 The response-region records

The delayed-recruitment records are labelled SD-E-DR-AN, SD-E-DR-SP, SD-E-DR-CO, and SD-E-DR-SL (anchovy-, sprat-, cod-, and slow-stock classes) — the delayed-recruitment oscillation lineage of population ecology (Gurney, Blythe, and Nisbet 1980) supplies their classical reference point. The labels separate these records from SD-E-B3 and do not by themselves complete a model registration: reproduction requires the companion registration stating the complete delayed-recruitment equations and state dimension, each class-specific parameter vector, the effort gate, $\Phi$, the initial history, the flow/update order, and the numerical and tail-classification conventions [CC-A011-017, Paper 4 owner]; the SD-E-B3 Candidate-A/B vectors live in the companion model registry. Because that complete stage registration is absent from the model record, the values below are exploratory computational summaries, not attributed to SD-E-B3 and not reproducible numerical propositions.

- **SD-E-DR-AN** [CC-A011-006]: persistent tail oscillation near $T_r\approx 3$–$4$ yr, with a weak response at $T_r=2$ yr; annual-review trajectories converge over the tested grids for every tested effort-response value.
- **SD-E-DR-SP** [CC-A011-007]: persistent tail oscillation near $T_r\approx 6$–$12$ yr.
- **SD-E-DR-CO** [CC-A011-008]: trajectories converge to equilibrium for every tested $T_r\in[1,20]$ yr, although the corresponding continuous-delay calculation has an oscillatory interval — a convergence-over-tested-grid record, not a stability theorem for every history.
- **SD-E-DR-SL** [CC-A011-009]: for $r\in(0.01,0.05)$ yr$^{-1}$, oscillation over part of the tested grid below approximately 20–30 yr and convergence at longer review intervals, with transition brackets between approximately 30 and 50 yr depending on $r$. This one-sided pattern does not contradict rapid-review consistency: the continuous no-delay M3-B target is itself unstable over part of the slow-$r$ regime, so small-$T_r$ trajectories may approximate an unstable target on finite horizons. The record is conditional on the delayed-recruitment variant and is not a general claim that slower review stabilises governance; the dominant timescales are centuries, beyond the length needed to resolve multiple cycles in most institutional records.

The corresponding continuous-delay calculations locate response regions near $rg\approx 1.5$–$1.6$: for $g=2$ yr, $r\in(0.77,0.81)$ yr$^{-1}$ at $\eta=0.914$ with a delay interval of approximately 2.6–7.8 yr; for $g=1$ yr, the high-$r$ interval is approximately 1.565–1.585 yr$^{-1}$ with a delay interval of 1.6–3.5 yr. These are finite-grid trajectory summaries, not closed analytical stability regions.

### 3.5 Robustness and diagnostic spectra

Multiplicative assessment-error experiments retain the anchovy-class trajectory region through 30% error and produce no noise-induced persistent tail oscillation at annual review in the tested ensemble [CC-A011-010]. This is a robustness summary for the declared multiplicative perturbation only, not a guarantee under arbitrary observation error.

The archived diagnostics carry observable-specific dominant peaks — approximately 4 yr in anchovy-class biomass with 12 yr in effort, and approximately 8 yr in sprat-class biomass with 60 yr in effort [CC-A011-011]. These are retained only as observable-specific dominant peaks over the analysed windows: components of one stationary periodic orbit cannot have different fundamental periods, and harmonics, subharmonics, modulation, or transient spectral content are unresolved; no decomposition has established whether the baseline $\delta_0$ term, signal regularisation, or another controller component dominates these responses. The archived amplitudes indicate percent-scale biomass excursions and order-one effort excursions relative to equilibrium; the exact percentages are not used as effect-size estimates, because the available convention does not distinguish peak-to-peak range from half-range and the approach to the large effort response contains a long transient.

### 3.6 Two review-map operators

The continuous delay equation and the sample-and-hold map are the same feedback loop under two delay operators: changing the operator can move or delete a crossing, and that relocation is a property of the review map's spectrum, not a demolition of the loop [CC-A018-018]. On the logistic hold-map core, the undelayed equilibrium is already unstable, so annual review is unstable and the sampled equilibrium restabilises only at $T_r^{\rm NS}=47.54$ yr; on the stage-structured review map, annual review is stable at every tested response value, the anchovy-class window relocates to $T_r\approx 3$–$4$ yr, and the sprat-class window to $T_r\approx 6$–$12$ yr, robust to 30% multiplicative assessment error. Both statements are $\det(M-e^{i\theta}I)=0$ on the map to which they refer; neither transfers to the other operator. Two consequences follow. First, the institutional signal is carried by effort and quota utilisation (80–240% of the equilibrium effort), not by biomass (1–2% of the equilibrium stock); on decadal records the observable is the growth transient in effort after a review-cycle change. Second, no real small-pelagic system currently operates a responsive 3–4 yr review, so the window prediction is untested, not falsified; the corresponding qualitative test for slow-regenerating resources is whether a responsive multi-year plan, adjusted against measured change, produces large-amplitude extraction cycles that a frozen multi-year cap does not (§7).

---

## 4 Observation, implementation delay, and the epistemic layer

### 4.1 The observation-fibre certification limit

**Theorem (observation-fibre certification) [CC-A010-001].** Let $D$ be a set of admissible latent states, $\mathcal O:D\to\mathcal Y$ an observation map, and $K\subseteq D$ a safety set. A deterministic observation-only certificate $c:\mathcal Y\to\{0,1\}$ with $c(\mathcal O(z))=\mathbf 1_K(z)$ for every $z\in D$ exists if and only if membership in $K$ is constant on every observation fibre: $\mathcal O(z_1)=\mathcal O(z_2)$ implies $\mathbf 1_K(z_1)=\mathbf 1_K(z_2)$.

*Proof (verified present; reproduced).* If $c$ exists and $\mathcal O(z_1)=\mathcal O(z_2)$, then $\mathbf 1_K(z_1)=c(\mathcal O(z_1))=c(\mathcal O(z_2))=\mathbf 1_K(z_2)$. Conversely, under fibre constancy define $c(y)=\mathbf 1_K(z)$ for any $z$ with $\mathcal O(z)=y$ — well defined by fibre constancy — and arbitrarily off the image; then $c(\mathcal O(z))=\mathbf 1_K(z)$ on $D$. ∎

The theorem concerns current latent-state membership certification only. It does not imply that observation-based robust control is impossible whenever a fibre contains distinct states: those states may admit a common safe action, and a dynamic impossibility theorem must show incompatibility of every admissible causal policy over observationally indistinguishable histories. The canonical statement of the same criterion is the atlas's [CC-A002-017, Paper 2 owner]; this row is the predecessor statement, cited at the seam. Its identification content is direct: aggregate-only certification misclassifies component safety exactly when the operational aggregate's fibres cross component-safety boundaries — the observation-aggregation hypothesis of §5.2 tests precisely this.

### 4.2 Information monotonicity

**Proposition (information monotonicity of recovery time) [CC-A001-013].** If $\mathcal I_1\succeq\mathcal I_2$ ($\mathcal I_1$ more informative), then $\tau_{\mathcal E}^{\mathcal I_1}(B)\le\tau_{\mathcal E}^{\mathcal I_2}(B)$ whenever both are compared from corresponding initial information states.

*Proof (verified present; reproduced).* Any policy implementable under the coarser structure $\mathcal I_2$ is implementable under the finer structure $\mathcal I_1$ by applying the garbling map; hence the optimal worst-case recovery time under $\mathcal I_1$ is no larger. ∎

The companion statement for kernels is the information-refinement monotonicity: if $\mathcal I_1$ causally refines $\mathcal I_2$ while dynamics, authority, implementation, uncertainty class, and safety constraints are unchanged, then $\operatorname{IViab}^{\mathcal I_2}_T\subseteq\operatorname{IViab}^{\mathcal I_1}_T$ — a controller with finer information can ignore it and implement a coarser-information strategy [CC-A006-007]. The inclusion requires the two kernels represented in a common physical initial-state space or a declared map between belief-state spaces; the fuller information-refinement theorem of the primary source is the canonical form (atlas, family F03). For the sampled-governance layer these are the formal counterparts of the review cadence question: coarsening the information structure (longer $T_{\rm obs}$, delayed assessments) can only shrink what is achievable, and by exactly how much is a kernel-level question, not a parameter drift.

### 4.3 Informational failure modes

Two constructions delimit what observation structure can and cannot do, both stated with the observation and epistemic family in the atlas and read here for their empirical content.

**Example (hidden-mode conflict) [CC-A001-027 · counterexample/limit].** Let an unobserved parameter satisfy $\theta\in\{-1,+1\}$, with $\dot z=\theta u$, $u\in\{-1,+1\}$, $z\ge 0$. At $z=0$: if $\theta=+1$ only $u=+1$ is safe; if $\theta=-1$ only $u=-1$ is safe. Both states are individually robustly viable, but $B=\{(0,+1),(0,-1)\}$ admits no common safe action, so $B\notin\operatorname{ERViab}$. This is a purely informational failure — no stochasticity or estimation quality is involved — and it is an impossibility witness for common-action viability, not a positive specialisation.

**Theorem (delayed-information obstruction) [CC-A001-028 · counterexample/limit].** If every possible action at belief $B_0$ allows a disturbance and a compatible state to reach a locally nonviable boundary point before the next informative observation time $T_{\rm obs}$, then $B_0\notin\operatorname{ERViab}$. A sufficient condition is the existence of a constraint function $q$ and $\varepsilon>0$ with $\inf_{x\in B_t}\inf_{d}D^{+}q(x;f(x,u,d))\le-\varepsilon$ throughout an uncertainty branch and $T_{\rm obs}>\inf_{x\in B_0}q(x)/\varepsilon$. Information may be accurate but arrive too late.

*Proof (verified present; summary).* Fix an action and an uncertainty branch; the Dini inequality integrates to $q(x_t)\le\inf_{x\in B_0}q(x)-\varepsilon t$, so the constraint is violated by time $t^*=\inf q/\varepsilon<T_{\rm obs}$, before any informative observation can alter the control; since this holds for every action and branch, no observation-based policy can save $B_0$. ∎

The delay in this obstruction is the observation interval $T_{\rm obs}$ — information timing, the review-interval spectrum's object — not a retarded functional differential equation (Paper 4 owns the RFDE family). The empirical reading: review cadence enters the safety question at the kernel level, and an accurate assessment delivered too late is operationally equivalent to no assessment within the window in which the constraint is lost.

### 4.4 The ideal benchmark and the epistemic-institutional kernel at its status

For a finite-dimensional fully observed ODE module with a closed, sufficiently regular state-safe set, the conditional full-information viability benchmark holds: if at every boundary state there exists a common admissible control for all active constraints and all disturbances, the safe-control correspondence admits an appropriate regular selection or viable solution concept, and solutions exist on $[0,T]$, then standard controlled-invariance results establish full-information viability on that horizon [CC-A006-003]. This is an ideal ODE benchmark — not a theorem for delayed, sampled, partially observed institutions; the canonical theorem of the invoked family is the robust-tangency characterization [CC-A001-023, Paper 2 owner], and the benchmark is cited here as the ideal limit of the sampled-governance comparison.

The institutional object against which the benchmark is read is the joint institutional information state $(B,h)$ — compatible physical histories and parameters together with an institutional mode — with prescription authority $a\in\Gamma(B,h)$, implementation correspondence $u\in\mathcal E(B,h,a)$, and the lower-game quantifier order: a non-anticipative prescription strategy exists against every admissible implementation, disturbance, parameter, and observation branch. The finite-horizon epistemic-institutional kernel satisfies the safe-base recursion $\mathfrak K_{n+1}=\mathcal T(\mathfrak K_n):=\mathfrak S\cap\operatorname{Pre}_{\mathfrak I}(\mathfrak K_n)$, whose monotone operator has a greatest fixed point by Tarski's theorem; under the additional $\omega$-continuity-from-above and strategy-closure hypotheses the countable intersection $\bigcap_n\mathfrak K_n$ is that fixed point, and without them the greatest fixed point is obtained by transfinite descending iteration [CC-A006-006, Paper 2 owner — stated at exactly that conditional status]. The kernel object is one across its ODE and sampled instantiations; the atlas owns the construction, and this paper's use is the comparison structure it fixes: physical feasibility, information, authority, and implementation are jointly represented, and none is reducible to another.

### 4.5 Value of information, informational recovery, and normative monotonicity

Three template results organise the epistemic layer's content for design.

**Robust information value** [CC-A006-012]: for a noncompensatory safety margin $q(X,u)=\min_i m_i(X,u)$, define, when the optimization is well posed, $V^{\mathcal I}_T(B,h)=\sup_{\Pi\in\Pi_{\mathcal I}}\inf_{\rm compatible\ branches}\min_{0\le t\le T}q(X(t),u(t))$. A nonnegative value is equivalent to finite-horizon robust safety only when the supremum is attained or the relevant viability closure is used; for an information refinement, the difference $V^{\mathcal I_1}_T-V^{\mathcal I_2}_T$ is a safety-margin value of information, not an entropy metric.

**Informational recovery** [CC-A006-013]: recovery is an information-state property — a strategy keeps the physical trajectory in the emergency envelope $\mathcal E_X$ until time $T$ and reaches a viable information state $(B_T,h_T)\in\mathfrak K_\infty$. Physical recoverability therefore does not imply institutional recoverability: the belief must itself be epistemically viable, which is the requirement that makes observation architecture part of the recovery question.

**Normative monotonicity** [CC-A006-015]: if two declared constraint systems satisfy $\mathcal C_X(\lambda_1)\subseteq\mathcal C_X(\lambda_2)$ and $\mathcal A(\cdot;\lambda_1)\subseteq\mathcal A(\cdot;\lambda_2)$, then the corresponding viability kernels (Aubin 1991; Aubin, Bayen, and Saint-Pierre 2011) are nested in the same direction under aligned dynamics, information, and uncertainty classes. This exposes the feasibility consequences of normative choices without purporting to derive or justify them — the scope discipline that the distributive layer of §8 inherits.

### 4.6 Model objects and empirical proxies

The observation and identification discipline separates model objects from public-data objects [CC-A024-001]. The model hitting time $T^{\rm dep}=\inf\{t>0:A(t)\le\varepsilon A(0)\}$ lives on trajectories of the mass-conserved ledger or a named reduced system and is not computed in the empirical tables; the instantaneous diagnostics (gross and net active-pool horizons) measure support use and decline and are not identified with empirical regression statistics; the constructed proxies (the groundwater trend-to-window-minimum ratio, the fisheries logarithmic horizon, the reserve-life ratio) are the public-data objects. None of the three is interchangeable with the others, and no empirical statistic is identified with a model object without a declared map.

Where distributional statements are attached to such proxies, their uncertainty boundary is part of the content [CC-A024-008]. The first-passage results owned by the ledger paper — the inverse-Gaussian groundwater passage and the geometric-Brownian fisheries passage [CC-A024-003, CC-A024-006, Paper 3 owner] — condition on the drift, the barrier, and the noise scale: the drift is estimated from a finite, potentially autocorrelated record; the barrier is selected from that same record; measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks, and common climatic drivers are separate uncertainties. Integrating out uncertainty in the drift, the barrier, or the noise scale gives a predictive distribution that is generally a mixture rather than a single inverse-Gaussian law, and a residual scale from the same window would not identify process noise. No calibrated predictive distribution is claimed. This is boundary-only content — it states what the distributional statements do not provide — and it governs every power and detectability statement of §5.4.

### 4.7 An open observation problem

**Open problem (binary-sensor threshold discretization) [CC-A001-096].** State the conditions under which the binary-sensor observation model is a threshold discretization of the continuous observation model. The problem is open; no partial result is claimed here.

---

## 5 Identification and power

### 5.1 The dimensionless identifiability chart

**Theorem (dimensionless identifiability) [CC-A018-012 · proof verified present].** In the three-state gated core, let $e=E/E_{\max}$, $n=N/K$, and

$$
\varrho=\frac{qE_{\max}}{r},\qquad
a=\frac{\delta}{\Delta_{\rm ref}},\qquad
b=\frac{\delta_0\delta}{\eta E_{\max}(Z_{\rm ref}+\delta)} .
$$

At an interior equilibrium, $e^*=(a+\sqrt{a^2+4b})/2$ and $N^*/K=1-\varrho e^*$. After scaling time by $r^{-1}$, the local Hopf delays $r\tau_\pm$ depend on $(\varrho,\lambda_F,a,b,Z_{\rm ref}/\delta,\eta/r,r\tau_m)$ and on $\operatorname{sp}_k'(0)=1/2$, where $\lambda_F=rK/\Delta_{\rm ref}$ is the flow-scale group. The four combinations $(qE^*,\ E^*/E_{\max},\ \eta E^*/\Delta_{\rm ref},\ \delta_0/\eta)$ do **not** determine the characteristic function: the coupling entry $-qN^*$ still contains $q$ separately unless effort is scaled by $E_{\max}$. Two calibrated parameter points are two points in $(\eta/r,\varrho)$, not one class.

*Proof (verified present; summary).* At an interior rest the surplus argument vanishes and $Z^*=\delta$; the effort equilibrium reduces to $e^2-ae-b=0$ with the displayed root, and $N^*/K=1-\varrho e^*$. After the time change $s=rt$, every entry of the linearisation scales into the listed groups; the characteristic function is homogeneous in these entries, so its roots — the dimensionless frequencies and delays — are functions of the groups only. ∎

Two qualifications ride the parameters: Hopf points are invariant under the softplus sharpness $k\in\{5,10,20,40\}$ at fixed $\delta$, not at fixed $\delta/k$ (the equilibrium memory $Z^*=\delta$ itself depends on $k$ at the baseline calibration); and criticality is not $k$-invariant, since the first Lyapunov coefficient contains $\operatorname{sp}_k''(0)=k/4$. The chart is complementary to the effort-scale non-identifiability transformation [CC-A012-009, Paper 1 §8.1 statement; Paper 4 owns the family]: the separate effort scale is not identifiable from the stock–signal pair alone, and the chart states the groups that do fix the equilibrium ratio and the dimensionless delays once effort is scaled by $E_{\max}$. The calibration consequence is binding for everything below: parameter claims must be stated in the chart's groups, and two calibrated systems are comparable only through those groups — never through raw effort scales.

### 5.2 Empirical hypotheses with declared tests

The architecture-level distinctions have prospective empirical consequences; each hypothesis carries its test requirements on the line [CC-A002-045, CC-A002-046, CC-A002-047].

**Observation aggregation** [CC-A002-045]. In systems where independent component measurements reveal safety-crossing fibres for the operational aggregate indicator, aggregate-only certification will produce nonzero component-safety misclassification under prospective validation. The test must freeze the aggregate, the component thresholds, the candidate population, the observation model, and the error metric before validation; finding no safety-crossing fibre in the declared domain counts against the hypothesis for that application. The certification limit of §4.1 is the mechanism.

**Governance phase ordering** [CC-A002-046]. After controlling declared ecological and market confounders, extractive and protective controllers will exhibit opposite signed phase relations between assessed decline and realised extraction, and measured deployment delay will shift that relation in the direction predicted by the registered controller. Contradictory causal ordering, or absence of the preregistered phase relation at adequate power, rejects the mechanism for that population. The frequency-domain caveat governs short records: where a predicted endogenous period is unresolvable, the test estimates gain and phase over resolvable frequencies from exogenous excitation, a dated intervention, or a justified closed-loop identification design (the closed-loop identification literature: Forssell and Ljung 1999) — a stock–effort cross-spectrum alone does not identify the open-loop transfer operator or separate ecological, assessment, decision, and deployment lags.

**Substitution certificate** [CC-A002-047]. For a frozen linear technology approximation, dual infeasibility certificates will predict service shortfalls under held-out resource/capacity scenarios more reliably than an unconstrained aggregate elasticity. A fair test compares out-of-sample scenarios and records pathway changes that invalidate the frozen technology matrix.

Three further architecture-level hypotheses are declared at the same status — testable through restricted models, each with its test requirement on the line, none executed [MS-Native-7] (A010, §12). **Stage-composition discrimination.** Models with explicit juvenile compartments outperform adult-only models when recruitment suppression is the dominant pressure; the test is an out-of-sample forecast comparison across the two model classes on the same series. **Spatial-aggregation failure.** Spatially aggregated predictions fail systematically where measured variance places the nonlinear moment correction outside its uncertainty bound; the test compares aggregated and spatially explicit predictions against withheld spatial data. **Exergy/capacity constraint effects.** Exergy/capacity constraints alter deployment and threshold risk in directions predicted before fitting the outcome; the test is intervention trials with and without the capacity constraint under preregistered directional outcomes. Each hypothesis requires a registered minimal model, data-generating process, estimator, and falsification rule, and the full architecture is not fitted merely because a smaller model fails.

### 5.3 The cross-sectional spectral screen and its input layer

The screen's input layer is the frozen 42-stock cohort of the RAM Legacy Stock Assessment Database v4.66 (Ricard et al. 2012), selected by a separate annual-review eligibility screen [CC-A011-012]. The release records stock and assessment metadata and series such as biomass, fishing mortality or exploitation rate, total allowable catch, catch advice, and effort; it does not encode controller sign, the decision rule, or dated decision and deployment queues. The annual-review designation is therefore an analysis-side cohort criterion, not a database classification of a stock as extractive or protective. The cohort and its eligibility table are the screen's input layer — the RAM stock identifiers and the annual-review eligibility table are a registration requirement, declared and not attached [CC-A011-020] — and the worked fisheries ledger cases of the ledger paper are separate objects (Paper 3); fragmenting the screen's inputs from its analysis would split one analysis across papers.

For each eligible biomass and exploitation/effort proxy series, the analysis detrends according to a declared rule, computes a Lomb–Scargle periodogram, integrates power in the predeclared bands (4–8 yr biomass, 12–60 yr effort), and compares it with a per-series AR(1) red-noise null, with familywise interpretation across stocks, observables, and bands (false-discovery-rate control in the Benjamini–Hochberg sense); a peak is classified as robust only if it survives the null comparison, the multiplicity adjustment, and sensitivity to detrending and endpoint choices [CC-A011-013, with the processed series and spectral routines a declared, unattached registration requirement — CC-A011-021]. **The result is a spectral null: no stock has a peak in the declared biomass or effort band meeting all robustness criteria** (Baltic sprat, for example, has biomass coefficient of variation 0.40, but its variation is low-frequency and regime-dominated rather than a robust target-band peak). The null carries its three-way restriction on the line: it is not proof of absence, not a comparison of controller signs, and not causal evidence that annual review stabilises anything. On the stage-structured review map, annual-review stability at every tested response value is consistent with this null [CC-A018-018]; consistency is not a test.

### 5.4 Power and detectability

Power experiments inject the model-generated effort signal into AR(1)-type noise and apply the same band-power statistic [CC-A011-014] (conventional power-analysis framing: Cohen 1988). On 100–200 yr synthetic records, the sprat-class signal has estimated power 1.0 at noise scale $\sigma=0.1$ and approximately 0.24–0.58 at $\sigma=0.3$; the anchovy-class effort signal has power approximately 0.02–0.14 over the tested horizons and noise levels — its longer effort peak and slow amplitude growth can offset its larger relative excursion. These are conditional simulations: no minimum-power guarantee holds per empirical stock, and the 100–200 yr horizons exceed many eligible series. The anchovy-class null is consequently weakly informative under the declared test, and the sprat-class result is informative only in favourable noise and record-length regimes; the empirical screen is a selected-cohort consistency check and the baseline for a prospective design, not a general test of the extractive mechanism. The power simulation code and seeds are a registration requirement not discharged [CC-A011-022].

The evidentiary separation is total: the stage-dependent regions, noise experiments, and power estimates do not establish population-wide frequencies or policy effects and cannot be transferred to SD-E-B3 or to protective control. A prospective test defines the candidate universe, controller eligibility, primary endpoint, spectral band, null model, multiplicity control, and minimum power before outcomes are examined. A complementary design estimates resolvable gain and phase rather than waiting for several complete endogenous cycles: for a locally linear registered model, the empirical target is the frequency response from an independently timed assessment or command perturbation to realised effort and stock response over the annual-to-decadal band the data support; identification requires exogenous excitation, an intervention design, or a justified closed-loop method; the analysis reports phase margin and uncertainty, compares alternative ecological and controller factorizations, and rejects the mechanism when no admissible factorization reproduces the preregistered gain–phase curve. This design can test feedback architecture even when century-scale periods are unobservable, but it cannot separately identify lag components without the dated records of §7.1.

---

## 6 Case screening and the northern cod case

### 6.1 The structured search and its zero count

The case search considered more than 30 systems spanning fisheries, aquaculture, groundwater, surface water, rangeland, wildlife harvest, forestry, and produced-capital markets, under four criteria: (i) a responsive institutional feedback rather than a one-time cap or ban; (ii) an independently dateable response or implementation lag; (iii) no major environmental, biological, or structural driver capable of generating the same outcome; and (iv) individual-resource or individual-station data rather than an aggregate series [CC-A011-015]. **No candidate satisfied all four criteria after primary-source and station-level review.** Behind criterion (iii) stands a named enumeration of the alternative mechanisms that can mimic or replace an institutional cycle — stage/maturation delays and cohort resonance; recruitment suppression versus stock culling; support-pool/nutrient limitation; pollution/waste feedback; predator–prey or climatic forcing; and direct abiotic mining and slow-store exhaustion — with the rule that a candidate institutional mechanism must be compared with these alternatives rather than identified from periodicity alone [MS-Native-9] (A003, §5). The criteria themselves prevent the zero count from serving as independent disconfirmation: because eligibility deliberately excludes any major competing driver, the null is a property of the searched candidate set, not a statistical test against the mechanism. Bangkok (durably) and La Mancha Oriental (on the stabilising side before its 2019–2023 extraction relapse) are the closest cases; the unconfounded delay oscillators identified in produced-capital systems (livestock and electricity-capacity cycles) do not contain the autonomously regenerating stock the resource model assumes.

The case-level coefficients, correlations, periods, and lag estimates are author calculations from registered input series, not source-reported values [CC-A011-016]: Sheridan-6 groundwater shows a decline–recovery–decline pattern with precipitation explaining approximately half the index-well variance ($R^2\approx0.47$), and the official programme record establishes a 55 acre-inch block allocation over the five-year first period rather than a continuously adjusted feedback; Bangkok pumping declines after 1999, but subsidence and recovery contain spatially heterogeneous consolidation and rainfall effects; La Mancha Oriental extraction rose again in 2019–2023 to an author-calculated average of approximately 312 hm³ yr⁻¹, with crop composition, evapotranspiration, and surface-water substitution complicating attribution; Icelandic cod under the 1995 harvest-control rule (annual total allowable catch at 25% of fishable biomass, subject to a minimum catch provision) has an author-calculated post-rule coefficient of variation 0.387 with a 10–15 yr fluctuation, but the estimated implementation lag is approximately 0.2–0.3 yr — a lag that is not a review interval and is not inserted into the sampled model as $T_r$ — and cohort resonance supplies an alternative mechanism, its period 15–25 times shorter than the four-state prediction [CC-A018-018]; Icelandic haddock under a related rule has a post-implementation coefficient of variation of 0.143, lower despite higher recruitment variability. Peruvian anchoveta provides a further discriminator: the 1950–2019 catch series has a robust period near 3.7 yr, consistent with ENSO recurrence, and cross-correlation gives $|r|\approx0.31$ with ENSO leading catch; the correlation is retained as exploratory pending exact identification of the ENSO product, and the subannual review regime lies below the anchovy-class response region — but controller nonclassification prevents that comparison from testing the mechanism. The case-screening table and query log are a registration requirement not discharged [CC-A011-023].

Two structural reasons explain the null [CC-A018-018]: the long records needed to test the claim exist primarily for visible crises, and visibility is correlated with a fast non-institutional driver; and at any regeneration rate inside the instability window the predicted period is centuries, longer than any institution has held a fixed response rule. The visible-record pattern — long series repeatedly associated with climate variability, cohort effects, infrastructure changes, or emergency interventions — is consistent with a selection mechanism in which systems receive intensive monitoring after complex crises, but the retrospective search does not causally identify selection bias.

### 6.2 The constitutive model and the phase-line obstruction

The northern cod case (NAFO 2J3KL) is carried as a bounded empirical object with the strong-Allee surplus equation as its illustrative constitutive model [CC-A014-001]:

$$
\frac{dS}{dt}=rS\left(1-\frac{S}{K}\right)\frac{S-\mathfrak s}{K-\mathfrak s}-C(t),
$$

with $S$ the spawning stock biomass, $r$ the intrinsic growth rate, $K$ the unexploited carrying capacity, $\mathfrak s$ the unstable threshold, and $C(t)$ the removals. The Schaefer model is the degenerate member of this family in which the factor $(S-\mathfrak s)/(K-\mathfrak s)$ is replaced by $1$: no value of $\mathfrak s$ makes the displayed factor identically $1$ (it tends to $1$ only in the limit $\mathfrak s\to-\infty$), so the Schaefer comparison is a change of growth law, not a parameter specialisation. The constitutive assumption stands as such — the equation is an illustrative model, not a fit — and the obstruction class is the one-dimensional autonomous equation with fixed parameters and fixed removals: the displayed equation is autonomous exactly when removals are fixed.

**Proposition (scalar-autonomous phase-line obstruction) [CC-A014-004 · theorem, proof verified present].** A nonconstant solution of a locally Lipschitz scalar autonomous ODE is monotone between equilibria and cannot cross an equilibrium in either direction. Consequently, an exact path that repeatedly rises and falls across a common interval is incompatible with any single fixed scalar autonomous model.

*Proof (verified present; reproduced).* Let $\dot x=f(x)$ with $f$ locally Lipschitz. If $x$ is nonconstant on an interval and $x(t_1)=x(t_2)$ with $t_1<t_2$, then $x$ attains an interior extremum at some $\tau$, where $\dot x(\tau)=0$, i.e. $f(x(\tau))=0$; by uniqueness the solution through $(\tau,x(\tau))$ is the constant equilibrium solution, a contradiction. So every solution is strictly monotone or constant. If a trajectory met an equilibrium value $x^*$ at any time it would be constant thereafter and, by uniqueness applied backwards, before; hence a nonconstant solution never attains an equilibrium value and cannot cross one in either direction. A path that rises and falls across a common interval attains some level twice with opposite directions, contradicting monotonicity. ∎

The obstruction is stronger and cleaner than a threshold-location trichotomy, and narrower: it concerns exact trajectories, not noisy estimates or forced systems. On this proposition rests the case's incompatibility result [CC-A014-003 · counterexample/limit]: any autonomous fixed-$(r,K,\mathfrak s)$ version is incompatible with the non-monotonic post-moratorium trajectory — the series that both rises and falls across tens of thousands of tonnes after 1992 cannot remain in one basin of the threshold and cannot cross the threshold in both directions. Two scope statements govern the result. The reliable contradiction is repeated direction reversal: convergence toward $K$ can be arbitrarily slow near degeneracy, so failure to reach an unspecified biomass by an unspecified deadline is not a contradiction. And the obstruction must be separated from rejection under measurement error, process noise, age structure, migration, time-varying mortality, and state-space observation models — the incompatibility is a property of the exact trajectory class, nothing broader.

**Lemma (extra-loss threshold shift, conditional) [CC-A014-002].** In the constitutive model with an additional constant loss ($C>0$) or extra mortality ($M_x>0$), the effective threshold satisfies $\mathfrak s_{\rm eff}>\mathfrak s$ — conditional on the modified positive equilibria existing and the loss lying below the relevant production maximum; larger losses eliminate the positive basin entirely.

The lemma is conditional, with the coalescence/disappearance case and the per-capita analog part of the statement; an effective threshold is not automatically a shifted structural parameter.

### 6.3 The two-window split and the formulation dependence

The case's positive result is a descriptive partition [CC-A014-008]: **the exact data split the phenomenon into two events — the crash interpretation is formulation-dependent, and the non-recovery is unexplained in both formulations. The split is the positive result, not a new mechanism.**

The crash window (1991–1995) is documented by the assessment table (DFO CSAS SAR 2016/026, Table A2): spawning stock biomass 735, 382, 101, 31, 10 kt across 1991–1995 with estimated natural mortality 1.002, 2.214, 2.575, 2.331, 0.288 yr⁻¹ — the crash-window mortality 2.2–2.6 is roughly ten times pre-collapse levels [CC-A014-006]. These are rounded renderings of the assessment table (the underlying values are 381.95, 101.05, 30.55 kt, and so on), and the survival column is $\exp(-M)$ after rounding — a transformation of the reported instantaneous mortality estimate, not an independently observed survival series.

The interpretation of the crash is a formulation attribution, not a causal claim [CC-A014-007]: the NCAM M-shift formulation allocates most estimated mortality to natural death — NCAM's $M$ is an estimated unobserved-death component conditional on model structure, and assessment-framework proceedings explicitly caution that unreported fishing deaths may enter de-facto $M$ — while the constrained-M formulation attributes the crash to unreported catch. The constrained-M quantities (crash window $M=0.46$, $F=1.37$, unreported catch 257.8 kt yr⁻¹ — 102.5% of mean spawning biomass; non-recovery window $M=0.43$, $F=0.25$, 3.7 kt yr⁻¹) are unreproduced: they are reproduction targets requiring equations, source series, code, units, windows, and uncertainty, registered on the open-problem docket and stated here as hypotheses, not results [CC-A014-009, docket owner].

The assessment table's later rows give the two windows their empirical grounding [MS-Native-8] (A014, assessment table): in the non-recovery window the estimated spawning stock biomass is 16.05 kt (1996), 34.42 kt (2000), and 20.07 kt (2004), with estimated natural mortality 0.341, 0.717, and 0.362 yr⁻¹ — low and non-monotonic, rising and falling across a common interval, the repeated direction reversal of the §6.2 obstruction — and in the recovery window 25.18 kt (2005), 96.91 kt (2010), and 298.65 kt (2015), with natural mortality 0.288, 0.696, and 0.278 yr⁻¹, the substantial increase after the mid-2000s. These are the assessment table's reported estimates (DFO CSAS SAR 2016/026, Table A2, NCAM M-shift formulation — the state-space assessment model of Cadigan 2016); the corresponding survival entries — 0.711, 0.488, and 0.696 in the non-recovery window, 0.750, 0.499, and 0.757 in the recovery window — are $\exp(-M)$ after rounding, transformations of the reported instantaneous mortality estimates rather than an independently observed survival series.

The non-recovery window (1996–2004) remains unexplained in both formulations: residual catch is first-order at low biomass, weak depensation is a live alternative, and the predator-pit and assessment-bias discriminants are untested. Programme context, one sentence: the programme's cod forecast-ladder paper applies preregistered persistence-benchmark scoring to this case, and its negative certificate — the persistence benchmark was not defeated — is that paper's result and is not transferred here.

### 6.4 Ecosystem context and the toy test

The ecosystem context is background only [CC-A014-010]: between 1985–87 and 2013–15, harp seal biomass rose from 49,600 t to 161,183 t (a 3.2-fold increase) and capelin biomass fell from 13.77 to 4.97 t km⁻² (a 64% decline) in the mass-balance record (Tam and Bundy 2019). These are descriptive mass-balance inputs, not causal tests; the statements that the predator pit is unsupported and that no capelin correlation exists would each require a defined estimator, interval, lag structure, and uncertainty quantification, and are kept untested and exploratory until reproduced.

The four toy simulations of the appendix — Schaefer growth from $1.2\times10^5$, below-threshold decay to zero, above-threshold convergence to $K$, and the below-threshold monotone no-pulse check at $C=3\times10^3$ — execute as expected [CC-A014-015]. They confirm only that the selected parameterized toy trajectories behave as designed: the test does not fit northern cod and does not validate the constrained-M experiment.

### 6.5 The social-ecological bridge

The case's social-ecological extension is a registered bridge [CC-A014-014]: 43 Newfoundland and Labrador fishing-dependent census subdivisions are identified from Statistics Canada Table 38-10-0167-01, mean income from fishing moves from 32.2% (2016) to 25.6% (2021), and DFO licence and landing data require a NAFO STATLANT filter. The archived table query and the population mapping are required before these social values join the adaptive-capacity material (§8); the bridge itself is the registered obligation, and the values are not carried as results.

The conjecture the bridge would test is stated at its open status [CC-A016-011]: a biomass-only success story can coincide with a declining inshore constituency. The discriminants are declared — if biomass pulses up while the locked human margins stay negative, the conjecture is supported; if the human margins recover with or before the biomass, it is defeated; and if the human series cannot be assembled, the normative object is not operationalized and that is published. The conjecture remains open, and coincidence is not causal effect: comparison populations, confounders, migration, shellfish substitution, transfers, policy timing, and a causal or explicitly descriptive design are all required before the discriminants discriminate.

---

## 7 Prospective designs

The retrospective evidence does not identify the institutional mechanism; the constructive content of this paper is the programme that could. Four identification designs and one closed-loop evaluation design are specified as preregistration targets — none has been executed, and each is preregistered before outcome inspection [MS-Native-4, MS-Native-5].

### 7.1 Governance-event panels

For each resource–jurisdiction unit, construct a source-linked event record containing the raw-observation date, the public or scientific recognition date, assessment completion, scheduled review, formal decision, legal adoption, physical deployment, compliance, realised-pressure change, and subsequent ecological-response dates. Date uncertainty, interval censoring, revisions, missing stages, and overlapping interventions are retained rather than collapsed to one lag. Such a panel estimates component-specific delay distributions only for stages actually observed; otherwise the estimand is a combined interval or a closed-loop phase, not separate $\tau_{\rm dec}$ and $\tau_{\rm dep}$ values. One interpretive caveat rides every delay value such records recover: the fixed-$\tau$ form is a modelling idealisation — real institutions confronting visible scarcity typically change their instrument set entirely (buyouts, engineered transfers, new infrastructure) rather than hold a single continuous response law with a constant delay — so an estimated $\tau$ is a summary of a changing control architecture, not a structural constant [MS-Native-10] (A018, §7). The cod case supplies two dated decision events for such a panel — the 2 July 1992 moratorium announcement and the 26 June 2024 reopening with a total allowable catch of 18 kt [CC-A014-013, negative-register owner: these are the retained verified facts of the institutional-margins record] — and its discipline is negative: no governance lead is inferred from annual biomass data, and a fast response does not establish adequacy.

### 7.2 Quasi-experimental timing

Candidate interventions include staggered adoption, discontinuities in review schedules, rule changes, jurisdictional borders, phased quota systems, and administrative reforms whose timing is plausibly independent of the outcome innovation. An event study, difference-in-differences design, synthetic control, interrupted time series, or state-space intervention model is chosen according to its assumptions, not merely data availability. The protocol predeclares the intervention, the controller sign, treatment and comparison units, the estimand, the event window, anticipation and pretrend tests, spillovers, concurrent ecological or market shocks, and exclusion rules. Two coding rules are binding: a change in implementation lag is not coded as a change in $T_r$, and a nominal schedule change is not a treatment unless it changes a responsive decision opportunity.

### 7.3 Out-of-sample mechanism comparison and the displacement discipline

For each candidate system, compare at least an environmental-forcing model, a cohort- or demographic-resonance model, an institutional-delay model with registered controller sign, a combined model, and a null time-series model. Models make predictions before the held-out block is scored, using declared predictive and calibration criteria; model weights or posterior probabilities require an explicit likelihood and prior, and predictive ranking alone does not identify a causal mechanism. The displacement rule: a delay explanation is weakened when it cannot reproduce the preregistered phase ordering, and it is displaced when a competing mechanism predicts the held-out observations better — complexity is retained only on scored evidence, never by accumulation. The registered domain templates of the ledger paper (phosphorus, groundwater) carry the same discipline for their physical and institutional ladders.

### 7.4 Controlled and randomized human-in-the-loop experiments

A minimum human-in-the-loop design places participants in the same simulated renewable-resource environment and randomizes review cadence and the timing or sign of decision feedback, with ecological shocks held common across arms where appropriate. Primary endpoints include realised pressure, threshold crossings, recovery time, variability, and the gain–phase relation between assessments, commands, and actions. Treatment rules, stopping and safety criteria, sample size, exclusions, and analysis are preregistered. Agent-based institutional experiments, digital-twin exercises, and carefully governed field pilots complement this design; extrapolation from a laboratory or simulated resource to a field institution remains a separate external-validity claim. Mechanism-class precedent exists — controlled population and resource-management experiments show that delay- and parameter-driven transitions can be empirically studied (Costantino et al. 1995), and commons-free fishery-management experiments in which subjects overshoot by approximately 60% from stock-and-flow misperception show the behavioural substrate (Moxnes 1998) — but precedent for the mechanism class is not validation of the institutional equations.

### 7.5 Closed-loop management strategy evaluation

Because retrospective evidence does not identify the mechanism, policy comparison must be conducted in a closed loop that keeps process, observation and assessment, parameter, structural-model, decision, and implementation uncertainty distinct (the management-procedure tradition: Punt and Donovan 2007). Each simulation replicate contains: an operating model (age- or stage-structured or other resource dynamics, environmental forcing, density dependence, structural alternatives); an observation model (survey and catch observations, missingness, bias, autocorrelated error); an assessment model (estimator, update frequency, retrospective bias, uncertainty); a decision rule (SD-E, SD-P, SD-F, or SD-H, including caps on change and emergency clauses); an implementation model (compliance, deployment lag, effort creep, realised versus commanded pressure); and performance metrics (threshold risk, yield and service delivery, variability, closure frequency, effort cost, recovery time, distributional impacts) [MS-Native-5].

The core experimental design crosses

$$
T_r\times\tau_{\rm dec}\times\tau_{\rm dep}\times\text{controller sign}\times\text{observation/assessment error}\times\text{parameter draw}\times\text{operating-model class}\times\text{process-noise regime}.
$$

At minimum, responsive extractive, responsive protective, and fixed-plan controllers are compared; a conclusion that compares only two review intervals inside the extractive class cannot be generalised to governance as a whole. For each cell, enough stochastic replicates are used to estimate tail risk with confidence intervals, common random numbers are predeclared where useful, and failures of the assessment or optimizer are reported. Parameter uncertainty varies quantities within a declared operating model; process uncertainty governs stochastic state evolution; observation and assessment uncertainty govern the information supplied to the rule; and structural uncertainty varies the operating-model class itself, represented by multiple operating models rather than one parameter covariance matrix around a fitted model. Model-class worst-case, distributionally robust, and model-averaged performance answer different questions and are reported separately rather than treated as interchangeable robustness criteria.

---

## 8 Distributive and adaptive-capacity constraints where reproducible

### 8.1 Constituency and measured floors

The distributive layer begins with two definitions. The worst-off relevant population is a modelling choice — a named constituency $G_t$; for the programme's own case the constituency is the registered inshore harvesters and licence holders of NAFO 2J3KL [CC-A016-002]. The declaration is not free: the displayed community-level data are all-resident employment income including aquaculture and processing, so the constituency must either be redefined as the census-subdivision populations or licence-holder microdata or administrative data obtained — the community table is not a licence-holder panel — and the geography crosswalk from census subdivisions to 2J3KL dependence is a separate declared mapping. A measured floor is a pair $(I_k,c_k)$ — an instrument and a cutoff — a measurement object distinct from the norm that motivates it [CC-A016-003]. Non-decline is a normative rule, not automatically an empirically justified floor: baseline, cohort, inflation and purchasing-power treatment, uncertainty, attrition, acceptable variation, authority, and structural diversification all require declaration before a floor measures anything.

### 8.2 The componentwise-margin rule

If several floors are in force, the arrangement fails as soon as any measured margin $m_k(G,t)=I_k(G,t)-c_k$ is negative; the object of record is the vector $m(G,t)$ [CC-A016-004]. The conjunction is exact and admits no compensatory master scalar — this is the measurement-level twin of the noncompensation witnesses owned by the atlas and the ledger paper. The rule is what makes the distributive layer auditable: each margin is reported with its instrument and vintage, and no margin is aggregated away.

### 8.3 Instruments, releases, and vintages

Two external instruments are admitted as world-hooks for deprivation, each retained with release and vintage locks [CC-A016-007]: the global Multidimensional Poverty Index (Alkire–Foster method, OPHI/UNDP releases) as a multidimensional deprivation instrument, and the World Bank Poverty and Inequality Platform for income-axis measurement. Neither instrument exhausts the normative object — adaptive capacity held by someone, used against someone, paid for by someone — and the norm is not filled with a scalar score. The poverty-line vintage is part of the instrument declaration: the current primary international line is $3.00/day at 2021 purchasing-power parity, and the $2.15/day 2017-PPP line is available only for historically vintage-consistent analysis [CC-A016-006, docket owner]; any empirical use must state the line, the welfare aggregate, the PPP year, the population, and the release vintage.

### 8.4 The unreproduced pipelines

The community-level social values are registered data pipelines and are not carried as results [CC-A016-008, CC-A016-009, docket owners]. The 43 fishing-dependent census subdivisions were identified from Statistics Canada Tables 38-10-0167-01 (2016) and 38-10-0168-01 (2021), with mean income from fishing moving from 32.2% to 25.6%; the community-level table (Bay de Verde 71.7% to 50.7%; Belleoram 58.9% to 56.7%; Fermeuse 57.9% in 2016 only; Hant's Harbour 53.2% to 30.0%; Anchor Point 51.6% to 33.3%; Old Perlican 50.0% to 41.7%; Comfort Cove–Newstead and Greenspond 45.7% to 37.8%; Hermitage–Sandyville 45.5% to 56.5%; Charlottetown (Labrador) 43.9% to 38.5%) is displayed in the source and unreproduced: the locked query, CSV extract, filters, missing-value rules, geography crosswalk, and reproduction code are required. The Statistics Canada method facts are verified (the top-2% census-subdivision definition; the fishing-dependence thresholds 25.1% in 2016 and 21.4% in 2021); every displayed value carries the population mismatch — all-resident employment income, not licence holders — and the extraction must be distinguished from the licence, participation, and recruitment panel that the floors would require, which is not assembled.

### 8.5 The anti-domination residue

What the instruments cannot capture is stated as a boundary and left open [CC-A016-012]: who pays for persistence, who may use remaining variety, whose knowledge counts, and future persons — the part every income-and-amenities box misses. The residue is not filled with a 0–1 "agency" score; the limits that preserve it are part of the record: no household vector is constructed, no far-from-equilibrium thermodynamics is computed, non-Western obligation systems are not consulted, and future persons are not assigned a fictitious income. The responsible-engagement obligation is retained: the cited engagement surface marks where consultation is owed, not its discharge. The tagged normative premises behind this layer and the unoperationalized proposed floors are the architecture paper's [CC-A016-001, CC-A016-010, Paper 1 owners], stated here only as cross-references.

---

## 9 The falsification standard

The model family gains empirical content by specifying the outcomes that count against its mechanism and parameterisation [MS-Native-6]. Five declared outcomes:

1. If independently measured implementation and deployment lags do not covary with the instability bands predicted under fitted resource parameters, the quantitative delay claim is weakened.
2. If an observed oscillation remains after climate, cohort, and regime forcing are modelled, but its phase relation between decline signal, effort, and biomass contradicts the controller's causal ordering, the mechanism is rejected for that case.
3. If sampled-data analysis removes a continuous-delay band under realistic review rules, the continuous model cannot be used for that institution.
4. If a protective controller dominates the extractive controller across uncertainty without inducing the claimed volatility, no anti-regulation conclusion may be retained.
5. If realistic record lengths have low power for the predicted signal, field spectral nulls cannot adjudicate the mechanism; prospective or experimental evidence is required.

Three disciplines frame the list. First, the diagnostic no-transfer rule [CC-A002-005, Paper 1 owner]: a diagnostic is not a causal claim — the spectral null, the response regions, the power values, the case calculations, and the cod split carry their declared types and no more, and no accumulation of diagnostics converts to causal evidence. Second, the admission standard: the programme's scored-forecast methodology — preregistered scoring against declared baselines, with a negative certificate published when a benchmark is not defeated — is the rule the prospective programme inherits, and the programme's four scored Wave E manuscripts (two forecast ladders and two intervention-selection legs on the cod and Edwards systems) are separate papers whose results are not transferred here. Third, the designs of §7 do not convert the retrospective findings into causal evidence; they replace them, and until they are executed the summary of the empirical layer is the one stated in this paper: a well-posed mechanism, an exploratory computational record, a selected-cohort spectral null with limited power, a zero-count case search that is not disconfirmation, and one case whose positive result is a descriptive split.

---

## 10 Status ledger

| ID | statement | status | evidence | destination |
|---|---|---|---|---|
| CC-A001-013 | Information monotonicity of recovery time | theorem (proof verified present) | row-verified 2026-08-27 · proof present, line check | Paper 5 §4.2 (atlas Prop 7.7) |
| CC-A001-027 | Hidden-mode conflict (no common safe action) | example — impossibility witness | row-verified 2026-08-27 · status crosswalk | Paper 5 §4.3 (atlas Ex 6.5) |
| CC-A001-028 | Delayed-information obstruction ($T_{\rm obs}$) | theorem — failure boundary | row-verified 2026-08-27 · proof present, line check | Paper 5 §4.3 (atlas Thm 6.6) |
| CC-A001-096 | Binary-sensor threshold discretization | open problem | row-verified 2026-08-27 · conditional/open | Paper 5 §4.7 |
| CC-A002-045 | Observation aggregation | empirical hypothesis (test requirements declared) | row-verified 2026-08-27 · conditional/open | Paper 5 §5.2 |
| CC-A002-046 | Governance phase ordering (frequency-domain caveat) | empirical hypothesis (test requirements declared) | row-verified 2026-08-27 · conditional/open | Paper 5 §5.2 |
| CC-A002-047 | Substitution certificate | empirical hypothesis (test requirements declared) | row-verified 2026-08-27 · conditional/open | Paper 5 §5.2 |
| CC-A003-013 | Sampled-review variant (registry entry) | registered obligation (no artifact) | row-verified 2026-08-28 · defined source object | Paper 5 §2.4 |
| CC-A006-003 | Conditional full-information viability benchmark | conditional benchmark (ideal ODE limit) | row-verified 2026-08-28 · conditional/open | Paper 5 §4.4 |
| CC-A006-007 | Information-refinement monotonicity | theorem (common-space requirement) | row-verified 2026-08-28 · proof present, line check | Paper 5 §4.2 |
| CC-A006-012 | Robust information value | remark/template (attainment caveat) | row-verified 2026-08-28 · status crosswalk | Paper 5 §4.5 |
| CC-A006-013 | Informational recovery | remark/template (viable-information-state requirement) | row-verified 2026-08-28 · status crosswalk | Paper 5 §4.5 |
| CC-A006-015 | Normative monotonicity | remark (aligned-class nesting) | row-verified 2026-08-28 · status crosswalk | Paper 5 §4.5 |
| CC-A010-001 | Observation-fibre certification criterion | theorem (scope note preserved) | row-verified 2026-08-28 · proof present, line check | Paper 5 §4.1 |
| CC-A011-001 | Between-review logistic process with held effort | definition (model object) | row-verified 2026-08-27 · defined source object | Paper 5 §2.2 |
| CC-A011-002 | Filtered nonnegative deficit signal ($\tau_m>0$) | definition (model object) | row-verified 2026-08-27 · defined source object | Paper 5 §2.2 |
| CC-A011-003 | Projected explicit effort update | definition (model object) | row-verified 2026-08-27 · defined source object | Paper 5 §2.3 |
| CC-A011-004 | Extractive controller SD-E-B3 | definition (named controller; discretisation, not a rule) | row-verified 2026-08-27 · defined source object | Paper 5 §2.3 |
| CC-A011-005 | Comparator classes SD-P, SD-F, SD-H | definition (declared comparators, not experiments) | row-verified 2026-08-27 · defined source object | Paper 5 §2.3 |
| CC-A011-006 | SD-E-DR-AN response near 3–4 yr | exploratory response region (finite grid) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §3.4 |
| CC-A011-007 | SD-E-DR-SP response near 6–12 yr | exploratory response region (finite grid) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §3.4 |
| CC-A011-008 | SD-E-DR-CO convergence over 1–20 yr | convergence-over-tested-grid record | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §3.4 |
| CC-A011-009 | SD-E-DR-SL transition brackets 30–50 yr | exploratory response region (one-sided slow-$r$ pattern) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §3.4 |
| CC-A011-010 | 30% assessment-error robustness | robustness summary (declared perturbation only) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §3.5 |
| CC-A011-011 | Observable-specific spectral peaks | diagnostic spectral record (period caveat preserved) | row-verified 2026-08-27 · source status accepted, artifact pending | Paper 5 §3.5 |
| CC-A011-012 | 42-stock RAM annual-review cohort | empirical cohort definition (screen input layer) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §5.3 |
| CC-A011-013 | Multiplicity-controlled spectral null (three-way restriction) | empirical screen result | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §5.3 |
| CC-A011-014 | Injected-signal power values | power analysis (conditional simulations) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §5.4 |
| CC-A011-015 | More-than-30-system search, zero eligible | case-search record (not disconfirmation) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §6.1 |
| CC-A011-016 | Case-specific calculations ($R^2$, CV, periods, lags) | case calculations (author calculations) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §6.1 |
| CC-A011-018 | Initial histories and solver configuration | registration requirement (not discharged) | row-verified 2026-08-27 · source status accepted, artifact pending | Paper 5 §2.4 |
| CC-A011-019 | Code and machine outputs | reproducibility obligation (not discharged) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §11 |
| CC-A011-020 | RAM stock IDs and eligibility table | registration requirement (screen selection layer) | row-verified 2026-08-27 · source status accepted, artifact pending | Paper 5 §5.3 |
| CC-A011-021 | Processed series and spectral routines | registration requirement (not discharged) | row-verified 2026-08-27 · source status accepted, artifact pending | Paper 5 §5.3 |
| CC-A011-022 | Power simulation code and seeds | registration requirement (not discharged) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §5.4 |
| CC-A011-023 | Case-screening table and query log | registration requirement (not discharged) | row-verified 2026-08-27 · source-specific empirical status | Paper 5 §6.1 |
| CC-A011-024 | Shared bibliography file | declared file dependency (not committed) | row-verified 2026-08-27 · source status accepted, artifact pending | Paper 5 §11 |
| CC-A014-001 | Strong-Allee constitutive model | illustrative constitutive model (not a fit) | row-verified 2026-08-28 · source-specific empirical status | Paper 5 §6.2 |
| CC-A014-002 | Extra-loss threshold-shift lemma | conditional proposition (existence/production-maximum conditions) | row-verified 2026-08-28 · conditional/open | Paper 5 §6.2 |
| CC-A014-003 | Fixed-autonomous-scalar incompatibility | incompatibility result (failure boundary) | row-verified 2026-08-28 · source-specific empirical status | Paper 5 §6.2 |
| CC-A014-004 | Scalar-autonomous phase-line obstruction | theorem (proof verified present) | row-verified 2026-08-28 · proof present, line check | Paper 5 §6.2 |
| CC-A014-006 | SAR 2016/026 Table A2 crash-window series | empirical table (rounded source values; $\exp(-M)$ column) | row-verified 2026-08-28 · source-specific empirical status | Paper 5 §6.3 |
| CC-A014-007 | M-pulse vs constrained-M comparison | NCAM-formulation attribution (formulation-dependent) | row-verified 2026-08-28 · status crosswalk | Paper 5 §6.3 |
| CC-A014-008 | Two-window split | case synthesis (the positive result is the split) | row-verified 2026-08-28 · source-specific empirical status | Paper 5 §6.3 |
| CC-A014-010 | Ecosystem context (harp seal, capelin) | background only (causal use unverified) | row-verified 2026-08-28 · status crosswalk | Paper 5 §6.4 |
| CC-A014-014 | B6 data-collection bridge | registered bridge obligation | row-verified 2026-08-28 · status crosswalk | Paper 5 §6.5 |
| CC-A014-015 | Minimal-embarrassment toy test | supplement (executed; scope limited) | row-verified 2026-08-28 · source-specific empirical status | Paper 5 §6.4 |
| CC-A016-002 | Worst-off constituency (D1) | definition (population/geography requirements) | row-verified 2026-08-28 · defined source object | Paper 5 §8.1 |
| CC-A016-003 | Measured floor (D2) | definition (measurement object) | row-verified 2026-08-28 · defined source object | Paper 5 §8.1 |
| CC-A016-004 | Componentwise-margin rule (M1) | methodological rule (exact conjunction) | row-verified 2026-08-28 · defined source object | Paper 5 §8.2 |
| CC-A016-007 | Global MPI measurement bridge | measurement bridge (release/vintage locks) | row-verified 2026-08-28 · defined source object | Paper 5 §8.3 |
| CC-A016-011 | Social-ecological conjecture (C1) | conjecture (open; coincidence is not causal) | row-verified 2026-08-28 · conditional/open | Paper 5 §6.5 |
| CC-A016-012 | Anti-domination residue | normative limitation record (boundary; must not be filled) | row-verified 2026-08-28 · defined source object | Paper 5 §8.5 |
| CC-A018-012 | Dimensionless identifiability groups | theorem (proof verified present) | row-verified 2026-08-28 · proof present, line check | Paper 5 §5.1 |
| CC-A018-018 | Empirical screen and prospective review-interval hypotheses | empirical screen + prospective hypotheses (two-operator discipline) | row-verified 2026-08-28 · source-specific empirical status | Paper 5 §3.6, §6.1, §7 |
| CC-A024-001 | Model hitting time vs empirical proxy | scoping distinction | row-verified 2026-08-28 · defined source object | Paper 5 §4.6 |
| CC-A024-008 | Parameter/barrier/observation uncertainty cautions | boundary record (what is not provided) | row-verified 2026-08-28 · conditional/open | Paper 5 §4.6 |
| MS-Native-1 | Governance-time ontology (seven objects, no-collapse rule) | definition (source-declared) | stated in full, §2.1 | Paper 5 §2.1 |
| MS-Native-2 | Forward invariance of the sampled process | theorem (proof reproduced in full) | source's complete formal result | Paper 5 §3.1 |
| MS-Native-3 | SD-E-B3 instance of finite-horizon rapid-review consistency | consistency statement with scope exclusions (atlas theorem CC-A002-034 — cross-reference, not a retained row) | source remark, stated in full | Paper 5 §3.2 |
| MS-Native-4 | Four prospective identification designs | preregistration targets (not executed) | source designs, stated in full | Paper 5 §7 |
| MS-Native-5 | Closed-loop MSE crossing design | design (six components; crossing) | source design, stated in full | Paper 5 §7.5 |
| MS-Native-6 | Five falsification criteria | declared outcomes counting against the mechanism | source criteria, stated in full | Paper 5 §9 |
| MS-Native-7 | Architecture-level empirical hypotheses: juvenile-compartment models outperform adult-only models when recruitment suppression is the dominant pressure; spatially aggregated predictions fail systematically where measured variance places the nonlinear moment correction outside its uncertainty bound; exergy/capacity constraints alter deployment and threshold risk in directions predicted before fitting the outcome | declared empirical hypotheses (tests declared; not executed) | source's declared hypothesis list with the registered-minimal-model/estimator/falsification-rule requirement (A010, §12) | Paper 5 §5.2 |
| MS-Native-8 | Assessment-table values for the non-recovery window (SSB 16.05, 34.42, 20.07 kt at $M$ 0.341, 0.717, 0.362 yr⁻¹ for 1996, 2000, 2004) and the recovery window (SSB 25.18, 96.91, 298.65 kt at $M$ 0.288, 0.696, 0.278 yr⁻¹ for 2005, 2010, 2015; survival column $\exp(-M)$) | empirical table (source-reported assessment estimates; $\exp(-M)$ column a transformation) | corrected-article assessment table (A014; DFO CSAS SAR 2016/026 Table A2, NCAM M-shift formulation) | Paper 5 §6.3 |
| MS-Native-9 | Six alternative-mechanism families (stage/maturation delays and cohort resonance; recruitment suppression versus stock culling; support-pool/nutrient limitation; pollution/waste feedback; predator–prey or climatic forcing; direct abiotic mining and slow-store exhaustion) | methodological rule (a candidate institutional mechanism is compared with these alternatives, not identified from periodicity alone) | source's alternative-mechanism enumeration and comparison rule (A003, §5) | Paper 5 §6.1 |
| MS-Native-10 | Fixed-$\tau$ form as a modelling idealisation (institutions change instrument sets rather than hold a response law fixed; an estimated $\tau$ is a summary of a changing control architecture, not a structural constant) | interpretive caveat | source observation (A018, §7) | Paper 5 §7.1 |

No status is promoted anywhere in this ledger; the manuscript-native entries MS-Native-1 through MS-Native-6 are this paper's own statements of source-declared objects, results, and designs, and MS-Native-7 through MS-Native-10 restate source-declared content that carries no concordance row, all at the statuses declared above.

---

## 11 Provenance, reproducibility, and limits

**Provenance.** Every concordance-sourced statement carries its `CC` identifier; the concordance row links the statement to its source location, canonical module, mapping type, evidence status, and destination. The ten sources behind the retained set are A001, A002, A003, A006, A010, A011, A014, A016, A018, and A024, each read in full by the dated scientific passes recorded in the concordance. The manuscript-native entries (§10) carry their declaration on the line: the governance-time ontology and the four designs are source-declared objects, the forward-invariance proposition is the periodic-review source's complete formal result with its proof reproduced in full, the consistency instance rides the atlas's conditional theorem [CC-A002-034 — a cross-reference to the atlas's entry, not a retained row of this paper], and the falsification criteria are the source's declared outcomes. The shared bibliography of the periodic-review source is a declared but uncommitted file dependency, so the bibliography is reconstructed from the cited works at camera-ready [CC-A011-024]. Four manuscript-native entries restate source content that carries no concordance row, at its source-declared status: the A010 architecture-level empirical hypotheses, declared with their tests and not executed (§5.2); the A014 assessment-table values for the non-recovery and recovery windows, source-reported estimates of DFO CSAS SAR 2016/026 Table A2 with an $\exp(-M)$ survival column (§6.3); the A003 alternative-mechanism enumeration as the non-identification rule behind the case-search criteria (§6.1); and the A018-v18 observation that the fixed-$\tau$ form is a modelling idealisation, an interpretive caveat (§7.1).

**Reproducibility.** The empirical and computational records are stated at their source-declared statuses and no higher. The computational record of the periodic-review source is incomplete: until it is complete, the stage-output values have exploratory status rather than the status of reproducible numerical propositions; the code and machine outputs are not committed, and the retrospective computational and data results remain unreproduced [CC-A011-019]. The registration requirements not discharged are: the initial histories and solver configuration [CC-A011-018]; the RAM stock identifiers and eligibility table [CC-A011-020]; the processed series and spectral routines [CC-A011-021]; the power simulation code and seeds [CC-A011-022]; and the case-screening table and query log [CC-A011-023]. On the open-problem docket: the constrained-M reproduction package [CC-A014-009], the community-level social-data pipelines with their locked query, extract, filters, crosswalk, and reproduction code [CC-A016-008, CC-A016-009], the poverty-line vintage correction before any income-axis use [CC-A016-006], and the archived table query and population mapping of the social-ecological bridge [CC-A014-014]. Computational claims in this programme carry a certification hierarchy — nominal result, re-execution-verified, independently re-executed, certified (interval or rigorous arithmetic) — stated per claim and never implied; nothing in this paper reaches beyond the nominal tier, and the statuses above say so.

**Limits.** (i) Diagnostics are not causal claims: the spectral null, the response regions, the power values, the case calculations, and the cod split carry their declared types and no more. (ii) The response regions are exploratory finite-grid, trajectory-classified records pending complete stage registration and multiplier analysis; no Poincaré-map multiplier classification is claimed, and the values are not reproducible numerical propositions until the computational record is complete. (iii) The two review-map operators are distinct: statements computed on the hold map, on the stage-structured map, and on the continuous-delay equation do not transfer to one another, and every review-window statement names its operator. (iv) The screen is a selected-cohort consistency check whose power is high only in favourable noise and record-length regimes; the null is not proof of absence and adjudicates nothing about controller sign. (v) The zero-count case search is not independent disconfirmation under its own eligibility criteria. (vi) The cod case establishes a descriptive partition — the crash interpretation is formulation-dependent, the non-recovery is unexplained in both formulations, and no mechanism is identified; the constrained-M quantities are reproduction targets, and the arithmetic record of the case remains subject to archived recalculation. (vii) The obstruction mathematics concerns exact trajectories of the fixed-parameter, fixed-removals autonomous class and is not a rejection under measurement error, process noise, age structure, migration, time-varying mortality, or state-space observation models. (viii) The social object is not operationalized: the human series is not assembled, the normative floors are unoperationalized, and the gap is the result. (ix) The prospective designs are preregistration targets, not executed studies, and they convert nothing retroactively. (x) The conditional sources (A021, A022, A023) are outside this paper's retained set, and no claim here depends on them.

---

## References

Alkire, S., and Foster, J. 2011. Counting and multidimensional poverty measurement. *Journal of Public Economics* 95: 476–487.

Ashwin, P., Wieczorek, S., Vitolo, R., and Cox, P. 2012. Tipping points in open systems: bifurcation, noise-induced and rate-dependent examples in the climate system. *Philosophical Transactions of the Royal Society A* 370: 1166–1184.

Aubin, J.-P. 1991. *Viability Theory*. Birkhäuser, Boston.

Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. 2011. *Viability Theory: New Directions*. Second edition. Birkhäuser, Boston.

Benjamini, Y., and Hochberg, Y. 1995. Controlling the false discovery rate: a practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society B* 57: 289–300.

Cadigan, N. G. 2016. A state-space stock assessment model for northern cod, including under-reported catches and variable natural mortality rates. *Canadian Journal of Fisheries and Aquatic Sciences* 73: 296–308.

Cohen, J. 1988. *Statistical Power Analysis for the Behavioral Sciences*. Second edition. Lawrence Erlbaum, Hillsdale, New Jersey.

Costantino, R. F., Cushing, J. M., Dennis, B., and Desharnais, R. A. 1995. Experimentally induced transitions in the dynamic behaviour of insect populations. *Nature* 375: 227–230.

DFO. 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016. *Canadian Science Advisory Secretariat Science Advisory Report* 2016/026.

DFO. 2022. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2022. *Canadian Science Advisory Secretariat Science Advisory Report* 2022/041.

Forssell, U., and Ljung, L. 1999. Closed-loop identification revisited. *Automatica* 35: 1215–1241.

Gurney, W. S. C., Blythe, S. P., and Nisbet, R. M. 1980. Nicholson's blowflies revisited. *Nature* 287: 17–21.

Lomb, N. R. 1976. Least-squares frequency analysis of unequally spaced data. *Astrophysics and Space Science* 39: 447–462.

Moxnes, E. 1998. Not only the tragedy of the commons: misperceptions of bioeconomics. *Management Science* 44: 1234–1248.

Nešić, D., and Teel, A. R. 2004. A framework for stabilization of nonlinear sampled-data systems based on their approximate discrete-time models. *IEEE Transactions on Automatic Control* 49: 1103–1122.

Punt, A. E., and Donovan, G. P. 2007. Developing management procedures that are robust to uncertainty: lessons from the International Whaling Commission. *ICES Journal of Marine Science* 64: 603–612.

Ricard, D., Minto, C., Jensen, O. P., and Baum, J. K. 2012. Examining the knowledge base and status of commercially exploited marine species with the RAM Legacy Stock Assessment Database. *Fish and Fisheries* 13: 380–398.

Scargle, J. D. 1982. Studies in astronomical time series analysis. II. Statistical aspects of spectral analysis of unevenly spaced data. *The Astrophysical Journal* 263: 835–853.

Statistics Canada. Tables 38-10-0167-01 and 38-10-0168-01, CANSIM database. Statistics Canada, Ottawa.

Tam, J. C., and Bundy, A. 2019. Mass-balance models of the Newfoundland and Labrador Shelf ecosystem for 1985–1987 and 2013–2015. *Canadian Technical Report of Fisheries and Aquatic Sciences* 3328.

Tarski, A. 1955. A lattice-theoretical fixpoint theorem and its applications. *Pacific Journal of Mathematics* 5: 285–309.

World Bank. Poverty and Inequality Platform. World Bank, Washington, D.C.

Programme sources. The concordance inventory (`research_program/canonical_concordance_A001_A025.csv`; the 57 rows of §10 row-verified) links every `CC`-identified statement to its source location, canonical module, mapping type, evidence status, and destination; the ten sources behind the retained set (A001, A002, A003, A006, A010, A011, A014, A016, A018, and A024) were each read in full by the dated scientific passes recorded in the concordance, as listed in §11 (Provenance).
