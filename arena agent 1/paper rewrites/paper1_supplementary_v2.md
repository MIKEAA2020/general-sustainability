# Supplementary Material — The Limits of Compensatory Aggregation

*Accompanies: "The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment."*

This supplementary file carries the framework extensions that the main article states only at partial or conditional status. The main article separates weak from strong sustainability assessment by isolating what compensatory aggregation can and cannot license; the extensions collected here make the underlying machinery explicit without altering the separation theorem itself. Each section below declares its status — framework extension, conditional result, conjecture, or interpretive note — so that what is established, what is conditional, and what remains a research programme is visible at a glance. The separation theorem of the main article does not depend on any item in this file.

---

## S1. Extended Framework Definitions

The canonical tuple $S = (T, Z, S_{st}, B_{out}, V, \Gamma, O, A, C, R, D, K, P)$ (main text, Section 2.2) is expanded here with the full definitions of its thirteen slots and the four uncertainty levels. The slots below record what a sustainability-assessment model must declare before any invariance, viability, or aggregation claim can be transferred between models.

*Notation.* We write $S = (T, Z, S_{st}, B_{out}, V, \Gamma, O, A, C, R, D, K, P)$ for the canonical tuple (the thirteen-slot framework object defined in the main text, Section 2.2); its slots are itemized below. A constructor (a map on the system data representing a governance instrument) is written $\mathsf{C}$, with declared support $\operatorname{supp}(\mathsf{C})$. Existential viability kernels are written $\mathrm{Viab}(V; U, F)$. The accepted-state notation $\mathcal{V}[\cdot]$ follows the main text and is distinct from the policy class $P$. Generation-indexed constraint sets are written $V^{(k)}$.

- **Type system $T$.** Named types with units; moieties (conserved substances) are the only types admitting addition. Bridge types (services, thresholds, information states, institutional variables) are distinct.
- **State space $Z$.** Typed product of stock, service, and information coordinates.
- **Stock–flux structure $S_{st}$.** Per-moiety conservation laws; typed flux maps between stocks of the same moiety.
- **Boundary interface $B_{out}$.** Declared external fluxes (harvest, emission, recharge) with owners.
- **Constitutive laws $V$.** Growth, conversion, and transformation laws on typed stocks.
- **Service–technology correspondence $\Gamma$.** Which services each architecture delivers and at what intensity.
- **Observation operator $O$.** What each decision authority observes, with declared error structure.
- **Assessment operator $A$.** The mapping from observations to verdicts; the subject of the main article.
- **Command architecture $C$.** Who may select which actions, on what information, at what timing.
- **Deployment/reset architecture $R$.** Endpoint resets and their costs (as in the witness datum).
- **Disturbance class $D$.** Declared set of admissible disturbance trajectories.
- **Safe-and-just set $K$.** The constraint set, with floors typed by provenance.
- **Policy class $P$.** The set of causal feedback policies; distinct from the accepted-state notation $\mathcal{V}[\cdot]$.

**Uncertainty levels.** (U1) Parameter uncertainty: fixed-but-unknown parameters in known structure. (U2) Observation/assessment uncertainty: error between state and assessment inputs. (U3) Process disturbance: the declared class $D$. (U4) Structural model uncertainty: the model itself is one of several candidates. Each level carries a fixed quantifier discipline; no claim mixes levels without a declared bridge.

**Model maps.** (M1) Specialisation: a model is an instance of a more general model class. (M2) Exact projection: a semiconjugacy preserving the relevant invariants. (M3) Approximation: a declared residual bound. (M4) Singular reduction: a limit with declared validity region. The four maps are not interchangeable; claims transfer only along declared maps.

For composite-index construction, the implication of S1 is that any aggregation claim carries a tuple of declared slots and a declared uncertainty level; absent those declarations, the claim has no fixed meaning and cannot be checked against a typed assessment.

---

## S2. Governance Extension: Constructors with Declared Support

**Status.** Framework extension; the constructor algebra and the implementability ladder are stated at partial status. The obstruction theorem is a source-summarized conditional result, with the proof conditions made explicit.

### S2.1 Constructors

Governance instruments enter the framework as **constructors** (a map on the system data representing a governance instrument). A constructor does not, in general, alter exactly one tuple component: a harvest cap may alter the action correspondence, the dynamics, and the enforcement model; a tax may alter the effort law, the policy class, and the equilibrium; an observation reform may alter both the observation operator and the feedback law. Each primitive constructor $\mathsf{C}$ therefore carries a declared support
$$\operatorname{supp}(\mathsf{C}) \;\subseteq\; \{ T, Z, S_{st}, B_{out}, V, \Gamma, O, A, C, R, D, K, P \},$$
the set of tuple components it may alter. Any induced change outside the declared support must be represented explicitly or prohibited. This makes constructor composition auditable: for constructors $\mathsf{C}_1, \mathsf{C}_2$, one may prove commutation or noncommutation
$$\mathsf{C}_1 \circ \mathsf{C}_2 \;\neq\; \mathsf{C}_2 \circ \mathsf{C}_1$$
when, for example, an observation change alters the implementable policy class before versus after an action restriction.

The primitive constructors: $\mathsf{Cap}(Q)$ (upper harvest bound), $\mathsf{Floor}(H_{\min})$ (output floor), $\mathsf{Tax}(\tau)$ (price entry in the effort law), $\mathsf{Excl}$ (excluding a competing predator or agent), $\mathsf{Leak}(h)$ (unreported/illegal harvest), $\mathsf{Obs}(I, \Psi)$ (replacing the observation map and feedback law), $\mathsf{Rest}(\cdot)$ (any other restriction of the control correspondence). Each must declare its support.

### S2.2 Action-set monotonicity and the implementability ladder

Restriction of the action correspondence obeys one-sided monotonicity: $U_1(x) \subseteq U_2(x)$ for every $x$ implies $\mathrm{Viab}(V; U_1, F) \subseteq \mathrm{Viab}(V; U_2, F)$ for existential viability under the same dynamics and information structure. The family of correspondences with nonempty existential viability kernel is upward closed and closed under unions; intersections are not generally preserved. This monotonicity concerns the **action correspondence**; it is separate from monotonicity of the **policy class**, which also depends on information, timing, authority, strategic equilibrium, observability, and implementation mechanisms.

The action correspondence is layered along an **implementability ladder** (a chain of nested action correspondences ordered by what an agent can actually do at each layer of abstraction):
$$U_{\mathrm{impl}}(z) \;\subseteq\; U_{\mathrm{inst}}(z) \;\subseteq\; U_{\mathrm{tech}}(z) \;\subseteq\; U_{\mathrm{theor}}(z),$$
with the parallel policy-class ladder $P_{\mathrm{impl}} \subseteq P_{\mathrm{inst}} \subseteq P_{\mathrm{tech}} \subseteq P_{\mathrm{theor}}$. Within-architecture viability quantifies over the implementable class; a viability result over a technological or theoretical class does not transfer downward, because restriction of the correspondence can empty the kernel even where enlargement preserves it.

### S2.3 Management vocabularies as representations

Some instruments admit a canonical representation by primitive constructors; the representation is valid only after proving the induced component changes. A total allowable catch is representable as $\mathsf{Cap}$; a harvest control rule as $\mathsf{Obs}$; a landing subsidy as $\mathsf{Tax}(-\sigma)$; unreported harvest as $\mathsf{Leak}$; a closed season as a periodic $\mathsf{Cap}$. Each representation is valid conditional on its declared support being discharged. A tax is not merely a price entry if it changes incentives, equilibrium controls, compliance, enforcement, revenue and redistribution, or the disturbance law; a predator exclusion can alter trophic dynamics; an observation reform can change the admissible policy class. The representation claim is a theorem about the instrument, not a rename.

### S2.4 The commons obstruction (finite-time result with boundary-exit condition)

**Theorem S2.1 (Commons Obstruction).** *Suppose the following hypotheses hold.*

(H1) A scalar stock $S$ obeys the dynamics $\dot S = g(S) - H$.
(H2) Under the implemented Nash feedback, there exist constants $a > 0$ and $\varepsilon > 0$ such that
$$g(S) - H^{\mathrm{Nash}}(S) \;\le\; -\varepsilon \qquad \text{for every } S \in [S_{\min}, S_{\min} + a].$$
(H3) Every relevant trajectory enters this strip.

*Then every trajectory entering the strip reaches $S_{\min}$ within at most $a/\varepsilon$ time. If, in addition, the same strict negative-drift condition persists at the boundary and solutions are forward complete, the trajectory subsequently exits below $S_{\min}$.*

*Status.* Summarized from the source's proof; the uniform margin $\varepsilon > 0$ is load-bearing — strictly negative drift without a uniform margin does not by itself imply finite-time exit. The theorem requires a defined scalar stock dynamics and an explicit quantifier over Nash trajectories. Reaching the boundary is not identical to exiting below it; the second sentence requires the additional boundary condition.

**Remark (Monitoring is not automatic).** Observation error $\|\hat x - x\| \le \delta$ does not by itself make a desired feedback law implementable. One needs a robust-feedback theorem certifying a control law whose robust admissibility holds for all states in the observation fibre. Otherwise monitoring may improve knowledge without producing a safe common prescription.

For governance design, the implication of S2 is that instrument names must be discharged by support declarations before any invariance or viability claim can be transferred, and that finite-time obstruction results require an explicit uniform margin rather than a pointwise drift condition.

---

## S3. Intergenerational Extension

**Status.** Framework extension. The nested-impossibility theorem is stated with its proof conditions made explicit. The "every finite segment satisfiable" phenomenon requires a separate example and is not implied by the theorem as stated.

### S3.1 Generation structure

A generation structure is a sequence $0 = t_0 < t_1 < \cdots \to \infty$ of generation boundaries with closed per-generation constraint sets $V^{(k)}$; intergenerational viability requires $x(t) \in V^{(k)}$ for $t \in [t_k, t_{k+1})$.

### S3.2 Stationary equivalence (with conditions)

If $V^{(k)} = V$ for all $k$, intergenerational viability reduces to ordinary viability. This immediate equivalence holds only under several restrictions: the generation intervals must cover the same infinite horizon; the policy class must be unchanged across generations; there must be no resets or inherited variables; the equality $V^{(k)} = V$ must be exact; and the intergenerational criterion must be simply $x(t) \in V^{(k)}$. If inheritance, reset, age structure, or generation-specific policy restrictions exist, stationary set equality alone may not reduce the model to ordinary viability.

### S3.3 Nested-impossibility theorem

**Theorem S3.1 (Nested Impossibility).** *Assume the following hypotheses.*

(H1) Trajectories are forward complete.
(H2) Every trajectory is confined to one common compact set $K$.
(H3) Each $V^{(k)}$ is closed.
(H4) The generation sets are nested decreasing with empty intersection, $\bigcap_k V^{(k)} = \varnothing$.

*Then no intergenerationally viable path exists.*

*Proof.* Suppose a viable path $x(t)$ exists with $x(t) \in V^{(k)}$ for all $t \ge t_k$. Since the trajectory is confined to the compact set $K$ and is forward complete, it has an $\omega$-limit point $x^*$. Because each $V^{(k)}$ is closed and the trajectory lies in $V^{(k)}$ for all sufficiently large $t$, $x^* \in V^{(k)}$ for every $k$. Hence $x^* \in \bigcap_k V^{(k)}$, contradicting emptiness. □

**What the theorem does not establish.** It proves no infinite path exists when the intersection is empty. It does not prove that every finite horizon is satisfiable. The phenomenon
$$\mathrm{Viab}_N \neq \varnothing \ \ \forall N, \qquad \mathrm{Viab}_\infty = \varnothing$$
requires a separate explicit example — for instance $V^{(k)} = [0, 1/k]$ with dynamics and initial conditions making every finite prefix feasible but no point belonging to all sets. Until such an example is supplied, the claim is only the infinite-horizon impossibility.

For long-horizon sustainability assessment, the implication of S3 is that intergenerational viability claims cannot be lifted from finite-horizon satisfiability alone; a separate argument is required whenever generations carry distinct constraint sets.

---

## S4. Composition Extension

**Status.** Framework extension at conditional / incomplete status. The displayed formulas require equations and proofs that are not provided here; each item is marked.

### S4.1 Effort-scale invariance (requires equations)

In the registered delay-dynamics family, the effort-scale transformation $E' = aE$, $E'_{\max} = aE_{\max}$, $q' = q/a$, $\delta_0' = a\delta_0$ is claimed to leave the $(N, Z)$ trajectories invariant. **Status: conditional.** Invariance cannot be assessed without the registered equations: the transformed equations must be displayed and verified term by term, and the paper must distinguish parameter nonidentifiability, state-coordinate scaling, observational equivalence, and dynamical conjugacy, which are not identical. The architectural role is identifiability discipline: effort scales are not separately identifiable from the stock dynamics, so calibration claims must quotient by the transformation.

### S4.2 Yield-gap soft-minimum (unsupported as written)

At the Liebig limit, the yield gap is claimed to obey $\pi_j \le w_{\min}^{-1} e^{-\rho \Delta_y}$, with the coupled system decoupling with error $\|X - X^k\| \le C_T \varepsilon_c$, $\varepsilon_c = C e^{-\rho \Delta_y} + \varepsilon_{\mathrm{phys}}$. **Status: conditional / unsupported as written.** This requires definitions of $w_{\min}$, $\pi_j$, $\Delta_y$, the yield functions, the normalization, the domain, and the assumptions under which the exponential estimate holds; the error estimate requires a stability or Lipschitz theorem, initial-condition matching, a finite time horizon, and a specified norm. It should be converted into a proposition with a complete assumption list and proof, or marked as a conditional source result.

### S4.3 Coupling creates viability (not reproducible as written)

An example with $g_i(s) = s(1-s)$ and coupling $d = 0.2$, referring to "equilibrium-defined harvest floors," is claimed to show that coupling can create viability. **Status: not reproducible as written.** To stand as a formal result it requires the coupled equations, the control/action set, the disturbance set, the safe set, the exact floor definition, the decoupled comparison system, the kernel calculation, and a proof or exact numerical certificate. Until supplied, this belongs in a motivating example, not in the formal framework. The two-sided lesson — composition can create or destroy viability — is retained as the architectural point, with unrestricted composition not licensed.

### S4.4 Exergy, quality grades, and nonsmooth transformation feasibility

**Status: declared research programme, not a theorem set.** Transformation feasibility under exergy and quality-grade constraints, where the feasible set is nonsmooth (grades induce kinks), is the declared frontier of the transformation operator. No status is asserted beyond programme.

For composite-index construction under composition, the implication of S4 is that composition can either create or destroy viability, and that any invariance claim across composed subsystems must be supported by equations and proofs rather than by assertion.

---

## S5. Application Note: Planetary Boundaries

**Status.** Interpretive note; no theorem. The main article makes no claim about planetary boundaries.

The typed operator $E_{\mathrm{typ}}$ provides a formal idealization of the separate-boundary reading underlying the Planetary Boundaries framework (Rockström et al., 2009; Steffen et al., 2015), which is organized around nine boundary processes in the current standard formulation, with additional proposed indicators and extensions in the wider literature. The framework's operational logic is reasonably read as treating each boundary separately. Planetary-boundary assessments also involve uncertainty, control variables, regional disaggregation, interactions, justice considerations, aggregation of risk, and boundary-transgression severity. We therefore state only that the typed operator provides a formal model of the separate-boundary reading, not that it captures the framework's full operational logic.

**What the main theorem does and does not contribute.** Theorem 5 shows that a particular compensatory assessment can accept a transition rejected by a typed assessment. It provides a formal model of *one reason a noncompensatory stance may be adopted* — namely, that per-weight compensation can license weight-dependent plans no single one of which respects all floors. It does not prove that planetary boundaries ought to be noncompensatory; that is a normative and scientific-design question. Nor does the witness's rescue mechanism generalize automatically: the witness has an explicit STAGED action funded by a scalar stock $x$, whereas many boundary violations have no single identifiable bridging resource. The rescue implication is conditional on the presence of a typed rescue action controlled by a resource margin.

**References.** Rockström, J., et al. (2009). A safe operating space for humanity. *Nature*, 461, 472–475. Steffen, W., et al. (2015). Planetary boundaries: Guiding human development on a changing planet. *Science*, 347(6223), 1259855. Dearing, J. A., et al. (2014). Safe and just operating spaces for regional social-ecological systems. *Global Environmental Change*, 28, 227–238.

For composite-index construction in the planetary-boundaries setting, the implication of S5 is that the typed operator supplies a formal model of the separate-boundary reading only; whether the framework ought to be noncompensatory is a normative and scientific-design question that the main theorem does not settle.

---

## S6. Declared Conjectures and Falsification Designs

**Status.** Conjecture and design status; none executed; none carries an empirical finding.

Nine conjectures: (C1) compositional sustainability — viability is preserved under the composition of two viable subsystems exactly when their interaction map lies in a declared class; (C2) transformability — architecture transitions admit a resource-cost characterization analogous to the rescue threshold $r^*$; (C3) capacity-leading failure — the binding floor in an assessment sequence is the one with smallest slack at the earliest discharge; (C4) bottleneck–robustness — robustness margins concentrate in bottleneck subsystems; (C5) boundary-expansion reversal — expanding a constraint boundary can contract the viability kernel if the expansion admits a new attractor; (C6) distributional dynamics — the false-positive gap of Theorem 5 is largest when floors are negatively correlated across the disturbance class; (C7) correlated-disturbance amplification — correlated disturbances across moieties amplify the gap; (C8) maintenance suppression — aggregate indices suppress maintenance investment signals relative to per-floor reporting; (C9) efficiency–scale interaction — the rescue threshold $r^*$ is nonconvex in system scale.

Each conjecture is governed by preregistration restrictions: no conjecture is rescued by arbitrary post-hoc state augmentation; each study preregisters system class, specification, candidate indicators, excluded variables, predicted direction, acceptable model revisions, and the observations that count against the conjecture; and the unrestricted claim that every sustainability failure is representable at an "adequate scale and resolution" is excluded as too elastic to falsify. Each candidate leading indicator's predictive advantage over simpler outcome indicators is an empirical requirement, not a guarantee of definition.

For sustainability-assessment research design, the implication of S6 is that conjectures must be preregistered with their falsification conditions before any empirical claim of leading-indicator advantage can be entertained.

---

## S7. Verification Artifact Details

The companion artifact implements the witness datum of the main article (Section 4.5) in exact integer arithmetic at scale 40: no floating point, no tolerances, no randomness. It (i) computes the four actions' worst-case tubes and successors for every state on a 29,791-state grid; (ii) evaluates the typed, weighted, and physical admissibility predicates; (iii) checks the region identities $\mathcal{V}_{\mathrm{typ}}$, $\mathcal{V}_{\mathrm{weak}}$, $\mathcal{V}_{\mathrm{phys}}$, $R$, $I$, $\mathrm{FP}_{\mathrm{agg}}$ of Theorem 5; (iv) checks the threshold identities for $\rho_1, \rho_2$ at the analytically identified critical ratios and their midpoints; and (v) checks the propagation identities of Theorem 6 on a hold-prefixed horizon. All 25 checks pass; re-execution reproduces outputs exactly. The artifact is deposited with a stable identifier, software version, execution command, and expected output hashes. Its certification level is exact finite rational verification — rigorous for the finite rational computation, and distinct from the analytic proof of the continuum theorems, which rests on the displayed proofs in the main article.


---

## S8. The 25-Check Enumeration (Wave-4 Deposit)

*Appended at the wave-4 revision (main-text v20), on the joint audit's "which 25 checks?" item. The machine checks of the verification artifact (main-text Section 4.9; S7 above) are enumerated here one by one. Each entry quotes the check's recorded name verbatim from the committed results file (`research_program/paper1_instantiation/typed_false_positive_instantiation.json`, execution of 2026-08-28, deterministic, exact integer arithmetic at scale 40, exit 0) and states the main-text claim it maps to. Nothing is recomputed here and no value is new; every check's recorded pass status is True (25/25). Two naming notes: the artifact's own tokens "FP" and "FP0" name the discrepancy region $\mathcal{Q}$ of the main text's v20 notation (formerly $\mathrm{FP}_0$), and where S7's existing text says "Theorem 6" the v20 status relabel reads Remark 6 — the statement numbers are unchanged, so every reference resolves by number.*

1. *FAST breakpoint table exact (dip at t=1/2, recovery at t=1)* — the FAST row of the main-text Section 4.5 action table.
2. *STAGED breakpoint table exact (linear spend/growth)* — the STAGED row of the same table.
3. *per-coordinate exact ranges = breakpoint extremes (piecewise monotone)* — Section 4.5's declaration that every worst-case tube is the exact visited set.
4. *worst-case dip constants: benign 3/2, adverse 2, floor threshold 2* — Section 4.5's disturbance convention (worst-case dip of fixed depth 2; the artifact's benign 3/2 scaling is part of its configuration).
5. *machine typed-feasibility == {x>=1} ∪ {s1>=2} ∪ {s2>=2} on every grid state* — Theorem 5(1).
6. *machine all-weights admissibility == {x>=1} ∪ {s1+s2>=2} on every grid state* — Theorem 5(2).
7. *FAST/SLOW per-weight safety biconditionals confirmed on every grid state (dense r-grid)* — Theorem 5(6).
8. *boundary weights exact: FAST safe at r=rho_1, SLOW safe at r=rho_2 (witness state (1/2, 6/5, 6/5))* — Theorem 5(6), with the boundary conventions of Section 4.6.
9. *machine endpoint-only feasibility == all of X_0 on every grid state* — Theorem 5(3) (the physical endpoint operator).
10. *typed ⇒ all-weights-aggregate ⇒ endpoint-only (no violations on the grid)* — the hierarchy of Proposition 3(i).
11. *false-positive set nonempty on the grid* — Theorem 5(4); the artifact records 1,900 grid states in the set.
12. *interior witness (1/2, 6/5, 6/5): aggregate-feasible for every critical weight, typed-INfeasible, endpoint-feasible* — Theorem 5(4)–(5), first strictness.
13. *witness is an interior point (all ±0.1 neighbors remain in FP)* — Theorem 5(4)'s nonempty open interior.
14. *endpoint-only witness (1/2, 1/10, 1/10): endpoint-feasible, aggregate-INfeasible (no action safe at w=(1,1))* — Theorem 5(5), second strictness.
15. *aggregate-vs-typed strictness witness (the FP interior point above)* — Theorem 5(5).
16. *r=1/2: SLOW-only (FAST unsafe, SLOW safe)* — Theorem 5(6), per-weight plan disagreement.
17. *r=1: both plans safe* — Theorem 5(6).
18. *r=2: FAST-only (SLOW unsafe, FAST safe)* — Theorem 5(6).
19. *E_typ = ∩_w E_w = ∅ machine-verified (no action serves every critical weight)* — Proposition 3(ii) on the witness.
20. *R witness (3/2, 6/5, 6/5): typed-transformable via STAGED (bridging plan at physical cost c=1)* — Theorem 5(7), the rescue.
21. *I witness (1/2, 6/5, 6/5): all four actions rejected, each with its exhibited violated constraint (negative-certificate form)* — Theorem 5(7), the impossibility.
22. *rescue split verified on the whole grid: FP0∩{x>=1} typed-feasible via STAGED; FP0∩{x<1} typed-infeasible* — Theorem 5(4) and (7).
23. *stage-0 hierarchy holds and regions are preserved through two hold intervals (every grid state)* — Remark 6.
24. *FP strictness witness survives the holds at stage 0* — Remark 6(ii).
25. *endpoint-only strictness witness survives the holds at stage 0* — Remark 6(ii).

Every recorded pass status is True, and re-execution reproduces the outputs exactly (S7). The main text keeps the count and the pointer; this deposit is the enumeration.
