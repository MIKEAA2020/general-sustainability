# Toward a General Theory of Sustainability
## Robust Viability in Dependency-Closed Ecological, Economic, and Social Systems

**Comprehensive working manuscript, Version 0.2**  
**Date:** 14 August 2026  
**Scope note:** This version incorporates all valid substantive material developed during the preceding theory-building dialogue. Rejected or qualified claims are retained and explicitly evaluated rather than silently omitted.  
**Author:** [Author name]

---

## Abstract

Sustainability is invoked across ecology, economics, governance, infrastructure, organizations, and social policy, yet its meaning changes across domains and is often reduced either to biophysical persistence, economic continuity, resilience, or an aggregate indicator. This manuscript develops a candidate domain-general theory in which sustainability is understood as **robust controlled invariance of an explicitly valued, causally closed, augmented state space**. A system is sustainable, relative to a specified identity, constraint set, environment, disturbance class, policy set, affected population, and time horizon, when an admissible adaptive or transformative policy can preserve its essential functions and values within a joint viability region without progressively eroding the internal or external capacities on which that viability depends or impermissibly shifting burdens across populations, places, domains, or generations. The framework integrates viability theory, resilience thinking, social–ecological systems analysis, ecological economics, safe-operating-space approaches, control theory, and compositional assume–guarantee reasoning. It distinguishes physical constraints, empirical hypotheses, modelling assumptions, definitions, logical consequences, and normative postulates; formalizes sustainability as a dependency-closed viability problem; derives necessary conditions involving stock balance, rate limits, slack, response delay, externalization, growth, and subsystem compatibility; and proposes modular contracts for composing ecological, economic, and social models without reducing them to identical mechanisms. A canonical coupled model illustrates the framework, while transition sustainability is formulated as a reach–avoid–maintain problem with cumulative-harm and irreversibility constraints. The manuscript concludes with sustainability and impossibility certificates, testable hypotheses, an empirical research program, and an AI-assisted protocol for rigorous theory development. The proposal is a first formal synthesis rather than a validated universal law; its value depends on whether it yields nontrivial exclusions, leading indicators, and better interventions across heterogeneous cases.

**Keywords:** sustainability; viability theory; resilience; social–ecological systems; ecological economics; robust control; systems theory; strong sustainability; adaptive governance; assume–guarantee contracts

---

## 1. Introduction

The ambition to formulate a general theory of sustainability confronts a fundamental tension. A theory sufficiently abstract to apply to forests, firms, cities, public institutions, economies, and societies risks becoming vacuous. A theory sufficiently concrete to generate predictions usually becomes domain-specific. The central problem is therefore not to write one immense model containing every ecological, economic, and social variable. It is to identify a small formal structure that every adequate sustainability model must instantiate while permitting each domain to supply its own mechanisms, evidence, variables, and value judgments.

The widely used definition of sustainable development—meeting present needs without compromising the ability of future generations to meet their own needs—correctly joins current provision to future capacity (World Commission on Environment and Development, 1987). It does not, however, by itself specify system boundaries, essential variables, disturbance classes, thresholds, distributions, institutional feasibility, or proof obligations. Similar ambiguity appears when sustainability is equated with persistence, equilibrium, resilience, efficiency, circularity, economic growth, or ecological integrity. These concepts are related but not interchangeable.

A dictatorship may persist while violating the values a sustainability assessment is intended to protect. A profitable industry may continue by degrading an ecosystem on which it ultimately depends. An ecosystem may preserve aggregate productivity while losing species or functions judged essential. A national economy may improve territorial environmental indicators by relocating extraction and pollution abroad. A technically viable policy may be politically unavailable, strategically unstable, or procedurally illegitimate. A transition may promise a desirable future while imposing irreversible or unjust harm on the way. These cases imply that sustainability is neither a purely physical property nor a synonym for desirable persistence.

This manuscript proposes that sustainability is best treated as a qualified relation among a system, a protected identity, a set of constraints, supporting dependencies, disturbances, available actions, affected populations, and a time horizon. In compressed form:

> **A system is sustainable relative to a specified identity, set of values, environment, disturbance class, policy set, affected population, and time horizon when it can remain within an acceptable viability region without progressively destroying the internal or external conditions on which that viability depends.**

The corresponding formal thesis is:

> **Sustainability is robust controlled invariance of an explicitly valued, causally closed, augmented state space.**

“Robust” introduces disturbances and uncertainty. “Controlled” recognizes action, governance, adaptation, and transformation. “Invariant” requires essential constraints to remain satisfied. “Explicitly valued” prevents persistence from silently determining desirability. “Causally closed” requires relevant dependencies and displaced burdens to be included. “Augmented” requires future-enabling capacities and distributions—not only current outputs—to enter the state description.

This proposal is a meta-theoretical kernel rather than a claim that ecological, economic, and social systems obey the same substantive equations. The proposed commonality is formal: all can be represented using states, flows, capacities, constraints, feedback, disturbances, dependencies, actions, and values. Whether this common grammar has explanatory and predictive power is an empirical question.

The manuscript makes six contributions. First, it introduces an epistemic discipline that distinguishes definitions, logical consequences, physical constraints, empirical hypotheses, modelling assumptions, and normative postulates. Second, it develops a domain-general ontology and viability formulation. Third, it derives necessary conditions and impossibility results. Fourth, it introduces modular assume–guarantee contracts for composing large cross-domain models. Fifth, it formalizes transition sustainability and certification. Sixth, it identifies testable hypotheses and a research workflow, including safeguards for AI-assisted theory construction.

---

## 2. Intellectual foundations and the remaining gap

### 2.1 Viability theory

Viability theory asks whether a dynamical system can remain within a constraint set through admissible controls. Its central object is the viability kernel: the set of initial states from which at least one admissible trajectory remains within the constraint set (Aubin, 2009; Aubin, Bayen, & Saint-Pierre, 2011). This supplies the mathematical backbone of the present framework. Sustainability, however, requires more than a local constraint set. The boundary must include affected dependencies, the constraints must distinguish physical and normative content, the control set must be institutionally realistic, and the state must include capacities and distributions.

### 2.2 Resilience and transformation

Holling (1973) distinguished ecological resilience—the ability to absorb disturbance while preserving relationships—from narrow equilibrium stability. Subsequent resilience scholarship emphasized alternative regimes, adaptive capacity, and transformability (Walker et al., 2004; Folke et al., 2010). The present framework treats resilience as disturbance-relative capacity to preserve a declared viability region. Resilience is not identical to sustainability because an undesirable or externally damaging regime can be resilient.

### 2.3 Social–ecological systems

Ostrom’s (2009) social–ecological systems framework organizes analysis around resource systems, resource units, users, governance systems, interactions, and outcomes. It provides a rich diagnostic ontology and rejects one-size-fits-all institutional prescriptions. The current proposal complements this tradition by supplying a general dynamic criterion: joint viability of coupled ecological, economic, and social states under implementable policies and explicit constraints.

### 2.4 Ecological economics, critical natural capital, and scale

Ecological economics emphasizes that economies are materially embedded in ecosystems, that throughput is physically constrained, and that distribution and scale cannot be reduced to allocative efficiency. Strong-sustainability approaches identify critical natural capital that cannot be assumed substitutable by produced capital (Ekins et al., 2003; Neumayer, 2013). The present theory represents strong sustainability through independent, non-compensable viability constraints and requires each substitution claim to demonstrate functional adequacy, scale, rate, uncertainty, distribution, and reversibility.

### 2.5 Safe operating spaces and social foundations

Planetary-boundary research identifies Earth-system processes and control variables relevant to a safe operating space for humanity (Rockström et al., 2009; Steffen et al., 2015). Raworth (2012, 2017) combined ecological ceilings with social foundations, producing the idea of a safe and just space. The sustainability corridor developed below generalizes this lower-bound/upper-bound structure and makes it dynamic, capacity-dependent, disturbance-aware, and institutionally implementable.

### 2.6 Systems and control

Systems thinking contributes stocks, flows, feedback, delay, nonlinearity, and leverage points (Meadows, 2008). Control theory contributes observability, controllability, robustness, delay, and invariant sets. Contract-based and assume–guarantee reasoning shows how system-level guarantees can be assembled from component-level proof obligations. These tools are essential for rigor, but they do not decide which states ought to be protected, whose welfare counts, or which actions are legitimate.

### 2.7 The gap

Existing traditions provide many of the necessary pieces. The remaining gap is a compact architecture that simultaneously:

1. expresses sustainability as a dynamic viability property;
2. includes ecological, economic, social, and institutional constraints without conflation;
3. prevents externalized burdens from disappearing at the model boundary;
4. distinguishes current output from future-enabling capacity;
5. treats distribution and legitimacy explicitly;
6. incorporates uncertainty, strategic action, and transformation;
7. supports modular verification rather than requiring a monolithic model.

---

## 3. Epistemic discipline

A general theory becomes unreliable when empirical expectations, moral commitments, and mathematical consequences are all called “axioms.” Every substantive statement should therefore carry one of the following labels:

- **[D] Definition:** fixes the use of a term.
- **[L] Logical consequence:** follows from definitions or prior propositions.
- **[P] Physical constraint:** follows from an accepted physical law under stated conditions.
- **[E] Empirical hypothesis:** requires observational, experimental, or comparative support.
- **[M] Modelling assumption:** simplifies a particular model.
- **[N] Normative postulate:** states what is to be protected, prohibited, or distributed.

For example, conservation of energy is a physical constraint; the claim that diversity increases resilience in a given class of systems is empirical; a minimum-rights threshold is normative; and the definition of a viability region is semantic. A finite critical stock subject to permanent positive net depletion eventually crosses any positive lower bound is a logical consequence of the stock equation.

This classification serves two purposes. It prevents values from being presented as if derived from physics, and it prevents empirical regularities from being mistaken for logical necessities. A rigorous manuscript should maintain a claim ledger listing each proposition, its type, assumptions, evidence, and current status.

---

## 4. Ontology

### 4.1 System and boundary

**[D]** A system is an observer-specified collection of components, relations, processes, and boundaries treated as a coherent object for a stated purpose:

\[
S=(X,R,F,B),
\]

where \(X\) denotes components or state variables, \(R\) relations, \(F\) processes and flows, and \(B\) the operational boundary. Boundaries may be spatial, organizational, legal, demographic, functional, informational, or temporal. They are justified by the research question, not discovered as uniquely correct objects.

### 4.2 Identity

**[D]** System identity is the subset of structures, functions, relationships, or values whose continuity permits later states to count as states of the same relevant system. Let

\[
I=\{I_1,\ldots,I_m\}
\]

be the identity criteria. Component persistence, structural persistence, functional persistence, and normative continuity must be distinguished. A forest can replace organisms; an economy can replace firms; a society can revise institutions. Transformation may alter lower-level identity to preserve higher-level functions or values.

### 4.3 State and essential variable

**[D]** A state \(x_t\) is the information treated as sufficient to characterize the system at time \(t\) for the current model. An essential variable is one whose departure from an admissible range causes loss of a specified identity, function, dependency, right, or viability condition:

\[
z_i^{\min}\le z_i(t)\le z_i^{\max}.
\]

The source of each bound must be recorded as physical, biological, empirical, legal, normative, or precautionary.

### 4.4 Viability region

**[D]** The viability region is the set of states satisfying all necessary constraints:

\[
K=K_P\cap K_F\cap K_N,
\]

where \(K_P\) contains physically feasible states, \(K_F\) functionally viable states, and \(K_N\) normatively acceptable states. A desirable but physically impossible trajectory, a physically possible but functionally unstable trajectory, and a stable but normatively prohibited trajectory all fail for different reasons.

### 4.5 Stock and flow

**[D]** A stock is an accumulated quantity; a flow is a rate changing that stock. A generic balance is

\[
\dot s_i=I_i+G_i-O_i-D_i,
\]

where \(I_i\) is external input, \(G_i\) internal generation or regeneration, \(O_i\) output or extraction, and \(D_i\) degradation or loss. The structure is general, but its interpretation is domain-specific. Soil carbon is a material stock; productive equipment is a capital stock; “trust” should be treated as a stock only when a defensible operational accumulation process exists.

### 4.6 Capacity, load, buffer, and slack

**[D]** Capacity is the maximum sustainable rate or magnitude at which a system can perform a process under specified conditions. Source, regeneration, sink, processing, buffering, coordination, information, and adaptive capacities should be distinguished. Capacity is generally state-dependent:

\[
C_i=C_i(x_t,e_t).
\]

**[D]** Load is a demand, disturbance, extraction, waste stream, or coordination requirement imposed on a process. A simple stress ratio is

\[
\rho_i(t)=\frac{L_i(t)}{C_i(t)}.
\]

Instantaneous \(\rho_i<1\) is not sufficient for sustainability because cumulative damage, uncertainty, threshold effects, correlated loads, delays, distribution, and capacity erosion may remain.

**[D]** A buffer is a reserve that temporarily absorbs deviations. Slack is unused capacity available under uncertainty. A system permanently optimized to its nominal maximum may be efficient but non-robust.

### 4.7 Feedback, disturbance, adaptation, and transformation

A feedback mechanism observes or estimates state and changes action:

\[
u_t=\pi(\hat x_{t-\tau}),
\]

where \(\hat x\) is the estimated state, \(\tau\) a delay, and \(\pi\) a policy. Sustainability can therefore depend on observability, communication, authority, response speed, enforcement, and learning.

A disturbance class \(W\) must specify magnitude, duration, frequency, correlation, spatial extent, and uncertainty. Adaptation changes parameters or behavior while preserving the current higher-level identity. Transformation changes structures, rules, lower-level identities, or the admissible action set to preserve higher-order functions or values.

### 4.8 Dependency and causal closure

**[D]** System \(S_a\) depends on \(S_b\) with respect to function \(q\) if loss of a service or condition generated by \(S_b\) causes \(S_a\) to leave its viability region:

\[
S_a\xleftarrow{q}S_b.
\]

Dependencies form a directed network. The dependency closure of a focal system is

\[
D^*(S)=S\cup D(S)\cup D(D(S))\cup\cdots.
\]

Absolute closure is impossible. The practical requirement is **bounded causal closure**: every excluded process capable of reversing the conclusion at the required confidence level must be included explicitly or represented by a justified interface condition.


### 4.9 Four dimensions of sustainability

The ontology generates four distinct but jointly relevant dimensions.

**State sustainability** asks whether essential variables are presently inside their acceptable bounds:

\[
z(t)\in K^*.
\]

**Process sustainability** asks whether the processes changing those variables are compatible with continued viability. A lake may currently satisfy a water-quality threshold while a persistent pollutant inflow commits it to later failure. A firm may be solvent while accumulating obligations faster than its capacity to repay them.

**Capacity sustainability** asks whether regenerative, adaptive, monitoring, maintenance, and governance capacities are themselves being preserved. A system can maintain current output by consuming the capacity that makes future output possible.

**Relational sustainability** asks whether the focal system remains viable without making necessary supporting systems or affected populations nonviable. This dimension separates genuine sustainability from local persistence achieved through displacement.

These dimensions should not be collapsed. Current state compliance can coexist with an unsustainable process; acceptable current output can coexist with capacity erosion; and local viability can coexist with relational failure.

### 4.10 Recursive sustainability and the dependency graph

Sustainability is recursive because every focal system is embedded in supporting and affected systems. Let

\[
G=(V,E)
\]

be a dependency graph whose vertices are systems and whose directed edges represent material dependence or consequential impact. Assessment propagates through the graph until an omitted dependency is shown to be negligible for the decision, represented by a justified boundary condition, or incorporated explicitly.

The recursive requirement does not imply that every supporting system must remain unchanged. It requires that the functions on which declared viability depends remain available without violating their own critical constraints. This distinction permits adaptation and substitution while preventing the disappearance of damage at arbitrary accounting boundaries.

### 4.11 Scale consistency

Let \(S_i\subset S_j\), where \(S_i\) is a subsystem of \(S_j\). In general,

\[
\operatorname{Sust}(S_i)\not\Rightarrow\operatorname{Sust}(S_j)
\]

and

\[
\operatorname{Sust}(S_j)\not\Rightarrow\operatorname{Sust}(S_i).
\]

A profitable firm may depend on globally unsustainable extraction. A stable national economy may contain populations below minimum social constraints. A stable aggregate ecosystem measure may conceal species loss. Conversely, a larger system may remain viable by sacrificing a subsystem unless the subsystem’s constraints are included explicitly.

Assessments should therefore identify a scale lattice—for example individual, household, organization, community, region, nation, and planetary system—and test relevant upward and downward implications.

### 4.12 Temporal consistency and latent liabilities

Sustainability over one horizon does not imply sustainability over a longer one:

\[
\operatorname{Sust}_{T}(S)\not\Rightarrow\operatorname{Sust}_{T+\Delta T}(S).
\]

Deferred maintenance, ecological debt, financial obligations, health burdens, infrastructure deterioration, and institutional distrust may preserve present indicators while constraining future action. Let \(\lambda(t)\) denote latent liability:

\[
\dot\lambda=\text{unresolved burden creation}-\text{burden resolution}.
\]

A complete viability region must include an upper bound \(\lambda\le\lambda_{\max}\). Otherwise deferred damage is misclassified as current success.


---

## 5. Formal core

### 5.1 Augmented state

Let

\[
z(t)=\begin{bmatrix}x(t)\\c(t)\\e(t)\\d(t)\\\lambda(t)\end{bmatrix},
\]

where \(x\) contains focal-system states, \(c\) enabling capacities, \(e\) supporting-system states, \(d\) the distribution of benefits, burdens, rights, and risks, and \(\lambda\) latent or deferred liabilities. Define

\[
K^*=K_x\cap K_c\cap K_e\cap K_d\cap K_\lambda.
\]

The dynamics are

\[
\dot z=F(z,u,w;M),
\]

where \(u\) is an intervention, \(w\in W\) a disturbance, and \(M\) a model or model class.

### 5.2 Sustainability specification

A complete sustainability claim is indexed by

\[
\Omega=(S,I,B,K,W,U,T,\mathcal D,\mathcal N),
\]

where \(S\) is the focal system, \(I\) protected identity, \(B\) boundary, \(K\) constraints, \(W\) disturbance class, \(U\) admissible interventions, \(T\) horizon, \(\mathcal D\) dependency and impact closure, and \(\mathcal N\) the normative authority or procedure used to choose social constraints.

### 5.3 Robust sustainability

**[D]** A system is robustly sustainable under \(\Omega\) if

\[
\exists\pi\in U\quad\forall w\in W:\quad z^{\pi,w}(t)\in K^*\quad\forall t\in T.
\]

The set of initial states from which this is possible is the sustainability kernel:

\[
\operatorname{Sus}(K^*,W)=\{z_0\in K^*: \exists\pi\;\forall w\in W,\; z^{\pi,w}(t)\in K^*\;\forall t\in T\}.
\]

For probabilistic disturbances, a weaker criterion is

\[
\Pr[z(t)\in K^*\;\forall t\in T]\ge 1-\varepsilon.
\]

The risk tolerance \(\varepsilon\), and the distribution of that risk, require explicit justification.

### 5.4 The sustainability corridor

Systems usually face both lower requirements and upper capacities:

\[
a(t)\ge a_{\min}(z)
\]

for minimum provision or function, and

\[
a(t)\le a_{\max}(z)
\]

for source, sink, ecological, institutional, or risk capacity. A feasible corridor exists only if

\[
a_{\min}(z)\le a_{\max}(z).
\]

If \(a_{\min}>a_{\max}\), no optimization inside the existing architecture can satisfy all constraints. Demand, distribution, efficiency, technology, capacity, organization, or legitimately revisable objectives must change.

### 5.5 Constraint slack

For each lower-bound constraint, define normalized slack

\[
\sigma_i(t)=\frac{z_i(t)-z_i^{\min}}{z_i^{\mathrm{ref}}-z_i^{\min}},
\]

with an analogous expression for upper bounds. The bottleneck margin is

\[
M(t)=\min_i\sigma_i(t).
\]

This is not an aggregate welfare index. It is a non-compensatory diagnostic. A surplus in one essential dimension cannot cancel violation of another.

A robustness margin may be defined as

\[
\Gamma(z_0)=\sup\{\gamma:\exists\pi\;\forall w\in W_\gamma,\;z^{\pi,w}(t)\in K^*\}.
\]

---

## 6. Minimal axioms

### Axiom 1: Specification

Every meaningful sustainability claim must identify what is to continue, for whom, under which constraints, disturbances, boundary, and horizon. Without these qualifications, the claim is underdetermined.

### Axiom 2: Joint viability

All constraints designated as jointly necessary must remain satisfied:

\[
z(t)\in K^*\quad\forall t\in T.
\]

### Axiom 3: Causal closure

Every process materially necessary for, or materially affected by, the focal system must be represented within the model or through an explicit interface whose capacities and effects are accounted for.

### Axiom 4: Dynamic attainability

Acceptable states must be dynamically reachable and maintainable under admissible actions and specified disturbances:

\[
\exists\pi\in U\quad\forall w\in W:\quad z^{\pi,w}(t)\in K^*.
\]

These axioms supply meaning, criterion, closure, and dynamics. Physical laws, empirical models, and normative postulates determine their substantive contents.

---

## 7. Necessary conditions and candidate theorems

### 7.1 Average-balance condition

For an essential stock

\[
\dot s=I+R-O-D,
\]

indefinite sustainability with bounded \(s\) requires

\[
\liminf_{T\to\infty}\frac{1}{T}\int_0^T(I+R-O-D)\,dt\ge0,
\]

unless the lost stock is replaced by an adequate substitute for every essential function. This is necessary but not sufficient because averages can conceal temporary threshold violations.

### 7.2 Rate-limit condition

If a critical process has capacity \(C(t)\) and load \(L(t)\), and \(L>C\) persists long enough to exhaust buffers before corrective action becomes effective, at least one dependent constraint must be violated.

### 7.3 Zero-slack condition

If a necessary process operates continuously at \(L=C\), it cannot be robust to a positive disturbance that raises load or lowers capacity unless another buffer or sufficiently fast response exists.

### 7.4 Delayed-response condition

Let

\[
T_r=T_{\mathrm{detection}}+T_{\mathrm{decision}}+T_{\mathrm{implementation}}+T_{\mathrm{effect}}
\]

and let \(T_c\) be time to a critical threshold without effective intervention. If \(T_r\ge T_c\) and no adequate buffer exists, feedback cannot prevent threshold crossing.

### 7.5 Dependency-closure condition

If system \(A\) requires system \(B\), and policy \(\pi_A\) drives \(B\) outside its viability region without an adequate substitute for the required function, \(\pi_A\) cannot sustain \(A\) indefinitely.

### 7.6 Non-compensation condition

If \(g_i(z)\ge0\) is a non-substitutable hard constraint, improvement in another criterion does not compensate for \(g_i<0\). Unconstrained weighted sums are therefore inappropriate when some dimensions are inviolable.

### 7.7 Conditional limit to unbounded growth

Suppose output \(Y\) imposes burden

\[
L(Y)\ge\alpha Y
\]

for persistent \(\alpha>0\), while admissible capacity is bounded by \(\bar C\). Since sustainability requires \(L(Y)\le C\),

\[
Y\le\frac{\bar C}{\alpha}.
\]

Unbounded growth is impossible under these assumptions. This is not a claim that every measure of economic value must cease growing; it makes the burden-intensity and capacity assumptions explicit.

---

## 8. Derived concepts

### 8.1 Resilience

Resilience is the size and structure of the disturbance set under which the relevant identity and constraints can be preserved. It is relative to the disturbance, identity, and response set and is neither universal nor automatically desirable.

### 8.2 Regeneration and maintenance

Regeneration restores an essential stock or capacity toward its viable region. Maintenance preserves enabling capacity. Current provision achieved by suppressing maintenance may temporarily improve visible outcomes while shrinking the future sustainability kernel.

### 8.3 Adaptation and transformation

Adaptive capacity consists of permissible policy changes that preserve or enlarge the sustainability kernel. Transformation changes some part of \((F,U,B,I)\) when

\[
\operatorname{Sus}(K^*,W)=\varnothing
\]

under the current architecture.

### 8.4 Efficiency and sufficiency

Efficiency is output per unit input or burden:

\[
\eta=\frac{Y}{L}.
\]

Total load is \(L_{\mathrm{total}}=Y_{\mathrm{total}}/\eta\); therefore efficiency does not imply sustainability when scale grows faster than efficiency. Sufficiency addresses the level and distribution of demand so that minimum provision remains compatible with upper capacities.

### 8.5 Circularity

If material demand is \(m\) and the recovered fraction is \(\chi\), virgin input is approximately

\[
m_{\mathrm{virgin}}=(1-\chi)m+\text{quality and process losses}.
\]

Circularity can reduce throughput but does not eliminate energy requirements, dissipation, collection losses, or scale constraints.

### 8.6 Justice

Justice enters both the viability region and the admissible action set. For groups \(g\),

\[
y_g\ge y_g^{\min},\qquad b_g\le b_g^{\max},\qquad r_g\le r_g^{\max}.
\]

Procedural requirements constrain \(U\), including rights, participation, consent, and due process where adopted as normative postulates. Physics cannot determine these thresholds, but a sustainability theory must prevent them from disappearing inside aggregate averages.


### 8.7 Strong and weak sustainability

Weak sustainability permits deterioration in one capacity if gains in another are judged compensatory:

\[
\sum_i w_i C_i(t)\ge C_{\min}.
\]

Strong sustainability identifies critical capacities that must independently remain above thresholds:

\[
C_i(t)\ge C_i^{\min}\qquad \forall i\in\mathcal C_{\mathrm{critical}}.
\]

The general theory should not assume perfect substitutability or universal non-substitutability. Every proposed substitution should carry an explicit test:

1. Which function of the original stock or capacity is essential?
2. What substitute supplies that function?
3. Does it supply all essential functions or only a priced output?
4. At what spatial and temporal scale does it operate?
5. Can it be deployed at the required rate?
6. What energy, material, institutional, and informational inputs does it require?
7. Which new wastes, risks, and dependencies does it create?
8. Who receives the substitute and who bears its burdens?
9. Is the substitution reversible if it fails?
10. What evidence supports performance under disturbance and uncertainty?

A substitution is adequate only relative to the full function set protected by the specification. Monetary equivalence alone is not functional equivalence.

### 8.8 Persistence, equilibrium, resilience, and sustainability

Four concepts must remain separate:

- **Persistence:** some recognizable system continues.
- **Equilibrium or stability:** the system remains near or returns toward a reference state under specified dynamics.
- **Resilience:** the system absorbs or recovers from a specified disturbance while preserving a declared identity.
- **Sustainability:** the protected identity and values remain viable without erosion of necessary capacities or impermissible displacement.

Sustainable systems need not be static. They may fluctuate, reorganize, learn, and transform. Conversely, harmful institutions can be persistent and resilient. Sustainability is therefore viability constrained by declared values and dependency closure, not equilibrium plus time.

### 8.9 General operational principles

The four minimal axioms generate a broader set of operational principles that should remain visible in applied work:

1. **Boundary principle:** every claim requires an explicit boundary.
2. **Dependency principle:** persistence depends on internal or external stocks, flows, structures, or services.
3. **Dynamic-balance principle:** persistent outflow and degradation cannot exceed replenishment for a finite essential non-substitutable stock.
4. **Capacity principle:** sources, sinks, institutions, and adaptive processes have finite state-dependent capacities and rates.
5. **Viability principle:** essential variables must remain within bounds, not merely acceptable averages.
6. **Feedback principle:** sensing and response must be adequate relative to system dynamics.
7. **Disturbance principle:** robustness claims require a specified disturbance class.
8. **Nested-systems principle:** a subsystem is not sustainable if it destroys a necessary containing or supporting system.
9. **Burden-displacement principle:** shifting risk or depletion across space, population, domain, or time does not remove it from the complete account.
10. **Adaptive-capacity principle:** changing conditions require sufficient robustness, adaptation, or transformation.
11. **Plural-value principle:** non-commensurable essential values require vector constraints rather than automatic scalar aggregation.
12. **Legitimacy principle:** social viability regions and admissible actions require explicit normative and procedural justification.

These are not all “indubitable truths.” They are definitions, logical implications, physical constraints, empirical requirements, and normative postulates of different types. Their role is operational completeness.


---

## 9. Modular composition

### 9.1 Module contracts

A universal theory should be implemented as modules rather than one monolithic model. Let

\[
M_i=(X_i,U_i,Y_i,A_i,G_i,F_i),
\]

where \(A_i\) denotes assumptions and \(G_i\) guarantees. Each contract has the form

\[
A_i\Rightarrow G_i.
\]

An ecological module may assume bounded extraction and pollution and guarantee resource flows and assimilation capacity. An economic module may assume material, labour, ecological, and institutional inputs and guarantee goods, livelihoods, and maintenance investment. A social module may assume minimum provision, environmental quality, information, and participatory channels and conditionally guarantee labour, knowledge, cooperation, and social reproduction. A governance module may assume resources, observability, authority, and manageable workload and guarantee monitoring, enforcement, dispute resolution, and adaptive response.

These are not equivalent mechanisms. The contract interface supplies the common formal language while preserving domain specificity.

### 9.2 Compatibility

A composed system is feasible only when module guarantees satisfy other modules’ assumptions:

\[
\bigwedge_{j\ne i}G_j\Rightarrow A_i\quad\forall i.
\]

If \(v\) denotes intermodule flows and each module induces \(v_i\in\Phi_i(v_{-i})\), a compatible configuration requires

\[
v^*\in\Phi(v^*).
\]

A sustainable fixed point must also satisfy \(v^*\in K^*\). Individual module viability does not imply compositional viability because modules may compete for inputs, generate incompatible timing requirements, export instability, or violate global distribution constraints.

### 9.3 Contract slack

For each module assumption, define slack as available input minus required input, or permissible load minus actual load. The system margin is the minimum across essential interfaces. The robustness of a composed system is constrained by its least robust critical interface rather than its average performance.

### 9.4 Candidate composition result

If every essential module begins inside its local viability region, fulfils its contract, receives inputs satisfying its assumptions, supplies outputs satisfying dependent assumptions, remains robust under the joint disturbance set, and satisfies global distribution and non-displacement constraints, then the composed system remains in the intersection of local viability regions. The abstract result is simple; its value lies in localizing proof obligations and exposing incompatible interfaces.


### 9.5 Expanded ecological contract

An ecological module may take inflowing energy, material pools, climate, extraction, restoration, and pollutant load as inputs. Its assumptions include disturbance bounds, extraction limits, and sink limits. Its guarantees include resource flows, habitat conditions, regeneration rates, and waste assimilation only within stated confidence bounds. Its failure modes include stock depletion, rate overload, threshold crossing, trophic cascade, and loss of regenerative capacity.

### 9.6 Expanded economic contract

An economic module assumes material and energy inputs, labour and care, ecological services, infrastructure, information, enforceable institutions, and finance. It conditionally guarantees provisioning, maintenance investment, inventories, livelihoods, and contributions to restoration and governance. Its failure modes include insolvency, shortage, capacity depreciation, concentration of access, ecological externalization, and suppression of maintenance to preserve current output.

### 9.7 Expanded social contract

A social module assumes minimum material provision, acceptable environmental conditions, safety, information, care, and channels for participation. Its outputs may include capabilities, knowledge, cooperation, labour, social reproduction, and legitimacy. These are not physical flows and should be operationalized through context-appropriate indicators. Failure modes include deprivation, exclusion, conflict, rights violations, loss of legitimacy, and overload of care or coordination systems.

### 9.8 Expanded governance contract

A governance module assumes administrative resources, observability, legal authority, procedural legitimacy, minimum compliance, and manageable workload. It conditionally guarantees monitoring, rule implementation, conflict resolution, learning, and adaptation. Its failure modes include delayed detection, enforcement incapacity, capture, strategic manipulation of indicators, backlog cascades, and rules that are technically sound but politically or normatively unavailable.

### 9.9 Interdependence fixed-point conjecture

The module architecture motivates a second central conjecture:

> A complex system is sustainable only if its essential subsystem contracts admit at least one dynamically maintainable, normatively acceptable, robustly compatible fixed point.

This is stronger than separate module sustainability. Two individually viable modules may demand the same scarce input, rely on incompatible timings, or generate loads exceeding each other’s guarantees. Conversely, a non-autonomous module may be viable within a mutually supportive composition.


---

## 10. Transition sustainability

Many real systems begin outside the desired region. Their problem is not invariance but **reach–avoid–maintain**.

Let \(K_{\mathrm{target}}\) be the sustainable target region, \(F\) forbidden states, \(K_{\mathrm{transition}}\) the temporary transition region, and \(T^*\) a deadline. A transition is sustainable if an admissible policy:

1. avoids \(F\) at all times;
2. remains within transition constraints before \(T^*\);
3. reaches \(K_{\mathrm{target}}\) by \(T^*\); and
4. remains there thereafter.

Formally,

\[
z(t)\notin F\quad\forall t,
\]

\[
z(t)\in K_{\mathrm{transition}}\quad 0\le t<T^*,
\]

\[
z(T^*)\in K_{\mathrm{target}},
\]

\[
z(t)\in K_{\mathrm{target}}\quad\forall t\ge T^*.
\]

Cumulative harm must also be constrained:

\[
\int_0^{T^*}h_g(t)\,dt\le H_g^{\max}.
\]

Irreversible outcomes belong to a forbidden set \(F_{\mathrm{irr}}\), with risk bounded where uncertainty remains. A credible transition claim therefore requires a target, deadline, pathway, intermediate constraints, resources, responsibility, milestones, and correction rules.


### 10.1 Restoration, adaptation, transition, and transformation

The intervention vocabulary should distinguish four cases:

- **Restoration** moves a degraded state toward a previously viable region without changing the basic architecture.
- **Adaptation** changes behavior or parameters to remain viable under altered conditions.
- **Transition** follows a time-bounded pathway from one regime or constraint status to another.
- **Transformation** changes structures, rules, technologies, boundaries, objectives, or lower-level identity because the existing architecture has no viable policy.

These responses should be diagnosed rather than treated as interchangeable labels. If the sustainability kernel is nonempty but shrinking, adaptation or restoration may suffice. If it is empty under the current dynamics and action set, transformation is required.

### 10.2 Transition-delay test

The language of transition can legitimize indefinite postponement. A valid transition claim must state a target, deadline, pathway, interim constraints, investment source, responsible actors, milestones, and correction triggers. A promise without these elements is not a trajectory model.

### 10.3 Just-transition constraints

A transition must not be evaluated solely by its endpoint. Group-specific provision, burdens, rights, displacement, participation, and cumulative harm must remain within explicit bounds during the pathway. An ecologically successful endpoint reached through prohibited deprivation or irreversible damage fails the joint viability criterion.


---

## 11. Canonical coupled model

Consider a community whose economy depends on a renewable resource and creates pollution. This model is illustrative, not calibrated.

### 11.1 Ecological module

Let \(R\) be a renewable-resource stock, \(P\) pollution, and \(E\) regenerative capacity:

\[
\dot R=r(E)R\left(1-\frac{R}{K_R(E)}\right)-H-\phi(P)R+w_R,
\]

\[
\dot P=\epsilon_Y Y-A-\lambda(E)P+w_P,
\]

\[
\dot E=J_E-\delta_EE-\psi_H(H,R)-\psi_P(P).
\]

Constraints are

\[
R\ge R_{\min},\qquad P\le P_{\max},\qquad E\ge E_{\min}.
\]

### 11.2 Economic module

Let \(K\) be productive capital, \(I\) essential inventory, \(Y\) output, and \(C_g\) provision to group \(g\):

\[
Y=F(K,H,L_b),
\]

\[
\dot K=J_K-\delta_KK-\chi(P,R)K,
\]

\[
\dot I=Y-\sum_gC_g-J_E-J_K-J_G-A-\operatorname{loss}(I).
\]

With distribution shares \(\theta_g\), \(C_g=\theta_gC\), \(\sum_g\theta_g=1\). Constraints include

\[
K\ge K_{\min},\qquad I\ge I_{\min},\qquad C_g\ge C_g^{\min}\;\forall g.
\]

### 11.3 Social and governance module

Let \(Q\) be unresolved governance workload and \(G\) governance capacity. Incoming workload may be

\[
\Lambda=\Lambda_0+\alpha_PP+\alpha_I\max(0,I_{\min}-I)+\alpha_DD_{\mathrm{ineq}}.
\]

Then

\[
\dot Q=\Lambda-\mu(G,Q),
\]

\[
\dot G=J_G-\delta_GG-\Phi_G(Q/G).
\]

Actual extraction may differ from authorized extraction when governance is weak:

\[
H_{\mathrm{actual}}=H_{\mathrm{authorized}}+H_{\mathrm{unregulated}}(G,\text{incentives}).
\]

The sign and form of this relationship are empirical. Social constraints may include

\[
Q\le Q_{\max},\qquad G\ge G_{\min},\qquad V_g\le V_g^{\max}.
\]

### 11.4 Joint problem

The policy vector is

\[
u=(H,A,J_E,J_K,J_G,\theta_1,\ldots,\theta_n).
\]

The joint viability region is the intersection of all ecological, economic, social, and governance constraints. The central question is whether

\[
\exists\pi\quad\forall w\in W:\quad z^{\pi,w}(t)\in K^*\quad\forall t\in T.
\]

Necessary steady-state conditions require extraction not to exceed net resource regeneration, pollution generation not to exceed abatement plus assimilation, and maintenance investment not to fall below depreciation and damage for ecological, productive, and governance capacities. These conditions are not sufficient because stability, delay, transition paths, strategic behavior, and uncertainty remain.

### 11.5 Predicted failure loops

The model represents several recurrent patterns:

- **Extraction–capacity spiral:** extraction lowers resource and regenerative capacity, which lowers renewal and raises future pressure.
- **Pollution–production spiral:** production raises pollution, ecological and productive capacities decline, and fewer resources remain for abatement.
- **Underinvestment spiral:** current provision pressure suppresses maintenance, which lowers future capacity and intensifies later provision pressure.
- **Inequality–governance spiral:** unequal burdens may raise conflict and workload, lower governance capacity, weaken compliance, and increase ecological and distributional pressure. This is an empirical hypothesis.
- **False-success trajectory:** aggregate output rises while ecological, governance, or group-specific constraints deteriorate.


### 11.6 Minimal domain-agnostic stock–capacity–support model

Before domain-specific equations, a minimal model contains one essential stock \(s\), one internal capacity \(c\), one support-system state \(e\), and one activity decision \(a\):

\[
\dot s=R(s,c,e)-U(a)-D_s(s,w),
\]

\[
\dot c=I_c(a)-\delta_c c-\Phi_c(a,c,w),
\]

\[
\dot e=R_e(e)-B_e(a,e,w).
\]

Require

\[
s\ge s_{\min},\qquad c\ge c_{\min},\qquad e\ge e_{\min},
\]

and minimum provision

\[
P(s,c,e,a)\ge y_{\min}.
\]

This model distinguishes stock depletion, capacity erosion, support-system degradation, and underprovision. It also represents cascades in which support degradation lowers renewal, shrinking the stock and overloading capacity.

### 11.7 Separate ecological instantiation

For a managed grassland, let \(B\) be vegetation biomass, \(N\) soil condition, and \(H\) harvest or grazing pressure:

\[
\dot B=r(N)B\left(1-\frac{B}{K(N)}\right)-H-D_B(w),
\]

\[
\dot N=R_N(N,B)-E_N(H,w).
\]

The system must satisfy ecological lower bounds while providing a minimum yield. This creates \(H_{\min}\le H\le H_{\max}(B,N,w)\). The example shows that ecological sustainability is not maximum conservation or maximum harvest but viability within a dynamic corridor.

### 11.8 Separate economic instantiation

A schematic economy may track productive capital \(K\), inventories \(I\), debt \(D\), ecological support \(E\), output \(q\), and group-specific consumption \(c_g\):

\[
\dot K=\operatorname{Inv}(q)-\delta K-\Phi_K(q,K),
\]

\[
\dot I=q-\sum_g c_g-\operatorname{loss}(I),
\]

\[
\dot D=r_DD+\operatorname{borrowing}-\operatorname{repayment},
\]

\[
\dot E=R_E(E)-\operatorname{burden}(q).
\]

Output growth alone cannot certify sustainability. Provision, solvency, productive maintenance, ecological capacity, and distribution must be jointly viable.

### 11.9 Separate social-institutional instantiation

For a public health service, let \(Q\) be unresolved cases, \(C\) treatment capacity, \(A_g\) access, \(T_g\) waiting time, \(V_g\) procedural violations, and \(\lambda\) incoming demand:

\[
\dot Q=\lambda(t)-\mu(C,Q),
\]

\[
\dot C=I_C-\delta C-\Phi_C(Q/C).
\]

Constraints include group-specific access and waiting-time bounds, maximum violations, and minimum capacity. This case demonstrates that a social system can share the abstract grammar of load, capacity, feedback, and distribution without treating health, rights, or legitimacy as thermodynamic substances.

### 11.10 Physical ecological foundation and its limits

Ecological systems are materially constrained. Any model must respect mass balance, energy conservation, finite processing rates, and entropy production. Open ecosystems maintain organized structure through energy throughput and material exchange; local material cycling is never perfectly closed. Carbon, nitrogen, phosphorus, sulfur, water, biomass, and waste sinks may be represented through explicit balances.

Non-equilibrium thermodynamics, stoichiometry, enzyme kinetics, transport constraints, and temperature dependence may supply domain-specific bounds. However, the maximum entropy production principle is not adopted here as an indubitable universal axiom, and Onsager reciprocal relations or Carnot efficiency should not be applied indiscriminately to whole ecological, economic, or social systems. Their use requires demonstrated scope conditions. Thermodynamics constrains social systems through physical embodiment but does not derive legitimacy, justice, rights, or institutional meaning.

A physical ecological module may expose interfaces such as energy flux, temperature, finite material pools, regenerated biomass, degraded heat, and waste. Economic and social modules must respect those interfaces, but they also require irreducible informational, institutional, and normative descriptions.


---

## 12. Observability, power, and strategic action

### 12.1 Observability

Decision-makers observe

\[
\hat z=z+\varepsilon
\]

and act on delayed information:

\[
u(t)=\pi(\hat z(t-\tau)).
\]

A viable path may exist physically but remain unavailable if the system cannot distinguish states requiring different actions. Each critical indicator should record the underlying construct, proxy, threshold, delay, uncertainty, resolution, manipulability, and associated response.

### 12.2 Implementable control

The action set is nested:

\[
U_{\mathrm{theoretical}}\supseteq U_{\mathrm{technical}}\supseteq U_{\mathrm{institutional}}\supseteq U_{\mathrm{implementable}}.
\]

Viability analysis should use the actually implementable set while transformation analysis asks how that set can be changed.

### 12.3 Strategic behavior and power

Actors \(i\) may choose

\[
a_i\in\arg\max_{a_i}U_i(a_i,a_{-i},z).
\]

The collectively sustainable action may not be an equilibrium of current incentives. Technical feasibility must therefore be intersected with legal admissibility, political implementability, incentive compatibility, and normative legitimacy. Power affects who defines constraints, who controls action, whose burdens are visible, and which data or alternatives are considered.


### 12.4 Measurement architecture

Each critical indicator should be recorded as

\[
\mathcal I_i=(z_i,\hat z_i,\theta_i,\tau_i,\sigma_i,\rho_i),
\]

where \(z_i\) is the underlying variable, \(\hat z_i\) the estimate, \(\theta_i\) its threshold, \(\tau_i\) measurement delay, \(\sigma_i\) uncertainty, and \(\rho_i\) spatial, temporal, or demographic resolution.

An indicator is inadequate when it measures the wrong construct, arrives after effective action is impossible, aggregates away vulnerable groups, is readily manipulated, or reacts only after irreversible damage.

### 12.5 Observability audit

For every critical state, an assessment should ask: Is it directly measurable? If not, what proxy is used? What is the causal relation between proxy and construct? What are error and delay? Can actors manipulate the measure? Does aggregation hide local failure? Is measurement frequent relative to system dynamics? Which action changes when the threshold is crossed?

### 12.6 Control-authority audit

For each intervention, record the responsible actor, legal authority, required resources, implementation delay, affected interests, resistance, enforcement, unintended effects, and reversal conditions. Theoretical controls should not be placed in the policy set merely because an equation permits them.

### 12.7 Adaptive monitoring and certificate revision

Let

\[
\varepsilon(t)=z_{\mathrm{observed}}(t)-z_{\mathrm{predicted}}(t).
\]

If \(\|\varepsilon(t)\|\) exceeds a stated tolerance or a key assumption leaves its validated range, the certificate must be reviewed, narrowed, suspended, or replaced. Sustainability conclusions are conditional and revisable.

### 12.8 Multi-model uncertainty

Let \(\mathfrak M=\{M_1,\ldots,M_n\}\) be plausible models. A model-robust policy satisfies constraints across the credible model set. Where none does, the theory recommends adaptive pathways, reversible experiments, monitoring that discriminates among models, and precaution around irreversible states. Uncertainty changes decision architecture; it should not merely add an error bar to a preferred forecast.


---

## 13. Sustainability and impossibility certificates

### 13.1 Sustainability certificate

A qualified sustainability claim should include:

1. the complete specification \(\Omega\);
2. a causal model or model set;
3. justification for each threshold;
4. dependency and impact closure;
5. at least one policy witness;
6. robustness and sensitivity evidence;
7. group-specific distribution and risk;
8. monitoring and trigger rules; and
9. a revision procedure.

Certification can be graded from assertion, through accounting and nominal constraint consistency, to dynamic viability, robust viability, dependency-closed viability, and empirically validated adaptive viability. “Sustainable” should not be asserted solely because a nominal balance sheet closes.

### 13.2 Impossibility certificate

It may be easier to show that an arrangement cannot be sustainable under stated assumptions. Relevant contradictions include:

- persistent net depletion of a finite essential stock;
- \(a_{\min}>a_{\max}\);
- waste generation above assimilation plus maximum abatement;
- response time exceeding time to threshold without a buffer;
- incompatible module contracts;
- insufficient total provision to satisfy all non-negotiable minima;
- technically viable policies that are all institutionally unavailable;
- transition paths that all cross forbidden irreversible states.

An impossibility certificate identifies which assumptions, capacities, distributions, or structures must change; it does not imply impossibility under every conceivable architecture.


### 13.3 Certification levels

Certificates should communicate evidential strength:

- **Level 0 — Assertion:** no explicit model or evidence.
- **Level 1 — Accounting consistency:** principal stocks and flows balance.
- **Level 2 — Constraint consistency:** the nominal trajectory satisfies identified bounds.
- **Level 3 — Dynamic viability:** at least one policy maintains constraints in a dynamic model.
- **Level 4 — Robust viability:** viability survives a justified disturbance and uncertainty set.
- **Level 5 — Dependency-closed viability:** external supports, displaced burdens, distribution, and delayed liabilities are included.
- **Level 6 — Empirically validated adaptive viability:** predictions, interventions, monitoring, and revisions have demonstrated performance over time or across comparable cases.

Passing a lower level does not establish a higher one.

### 13.4 Six proof obligations

Every rigorous claim must satisfy, to an appropriate degree:

1. **Semantic obligation:** critical terms are operationally defined.
2. **Accounting obligation:** stocks, flows, and burdens balance.
3. **Dynamic obligation:** the trajectory can arise from the stated dynamics.
4. **Closure obligation:** omitted dependencies cannot plausibly reverse the result.
5. **Robustness obligation:** the conclusion survives justified uncertainty and disturbance.
6. **Legitimacy obligation:** the source and authority of social constraints and risk tolerances are explicit.

### 13.5 Twelve-step diagnostic algorithm

1. Specify the system, identity, boundary, horizon, disturbance class, and normative procedure.
2. Identify essential outputs, functions, and rights.
3. Identify essential states and thresholds.
4. Identify enabling regenerative, maintenance, adaptive, informational, and governance capacities.
5. Map supporting dependencies and affected systems.
6. Construct module assumptions, guarantees, and failure conditions.
7. Test whether contracts can be satisfied simultaneously.
8. restrict the policy set to technically feasible, legally admissible, institutionally available, and implementable action.
9. Stress-test delays, uncertainty, correlated shocks, strategic defection, and boundary alternatives.
10. Compute or approximate the viability kernel, bottleneck slack, and transition pathways.
11. Conduct adversarial counterexample searches.
12. Issue a qualified conclusion: robustly sustainable, conditionally sustainable, transitionally sustainable, fragile, recoverable, structurally unsustainable under the current architecture, or indeterminate.


---

## 14. Leading indicators and testable hypotheses

The theory predicts that current output is often a lagging indicator. Candidate leading indicators include declining minimum slack, falling capacity-to-load ratios, increasing recovery time, increasing control effort required to maintain the same state, greater dependence on buffers, rising response-time/time-to-threshold ratios, and increasing transfer of burdens across domains or populations.


### 14.1 Why the leading indicators should work

A declining minimum slack indicates approach to the first binding essential constraint. A falling capacity-to-load ratio indicates that a system is losing room to respond even if output remains stable. Increasing recovery time suggests weakening restorative dynamics. Rising control effort means more intervention is needed to hold the same state and may expose hidden deterioration. Greater reserve dependence indicates that recurrent loads are being financed by finite buffers. A rising response-time/time-to-threshold ratio indicates that governance is becoming dynamically too slow. Increasing burden transfer indicates apparent local improvement achieved through relational degradation.

None of these is universally predictive in isolation. Their value is as theory-derived candidates to be compared with simpler outcome indicators.


Eight hypotheses follow:

**H1: Capacity indicators lead outcome failure.** Declining regenerative, maintenance, or governance capacity predicts sustainability failure earlier than current output measures.

**H2: Minimum slack predicts vulnerability.** Systems with smaller bottleneck slack experience constraint violations under weaker disturbances, other things equal.

**H3: Correlated disturbances dominate isolated ones.** Models treating ecological, economic, and social shocks as independent systematically underestimate joint failure where shocks share drivers or feedbacks.

**H4: Maintenance suppression produces delayed nonlinear failure.** Persistent diversion of maintenance toward current output initially improves visible performance but later accelerates risk.

**H5: Boundary expansion reverses some rankings.** Some systems classified as sustainable under territorial or organizational accounting are reclassified when imported resources, exported waste, affected populations, and delayed liabilities are included.

**H6: Distribution affects dynamics.** Unequal provision and burden alter health, compliance, conflict, and governance sufficiently to change the viability kernel in at least some systems.

**H7: Efficiency without scale control may fail.** Efficiency improvements do not reliably reduce total burden when growth and rebound exceed efficiency gains.

**H8: Kernel loss predicts transformation need.** When the current architecture’s sustainability kernel becomes empty, optimizing existing controls cannot restore viability without structural change.

---

## 15. Empirical program

The framework should be tested comparatively rather than illustrated only with confirming examples. For each case, construct four nested models:

1. an output-only model;
2. a stock-and-flow resource model;
3. a resilience model with disturbance and recovery;
4. the full framework with capacities, dependencies, distribution, institutions, and transformation.

The full theory earns its complexity only if it improves early warning, out-of-sample prediction, explanation of cross-domain failure, or intervention selection.

A first test suite should include:

- a renewable-resource commons such as a fishery or watershed;
- an infrastructure provisioning system such as water, energy, or public health;
- an economy or region dependent on imported materials and exported burdens;
- an institution facing overload and unequal access;
- a recovery or transition case in which transformation was attempted.

For each case, researchers should preregister the boundary, protected identity, constraints, disturbance set, candidate policies, and expected leading indicators. Alternative models should be maintained where causal uncertainty is material. Policies should be tested across the model set rather than optimized against one preferred model.

Theory performance should be judged by scope, nontriviality, operationality, predictive utility, intervention utility, transparency, parsimony, and falsifiability. Failure to outperform simpler models should lead to removal or revision of added structure.


### 15.1 Falsification sweeps

The empirical program should include deliberate attempts to break the theory.

**Persistence counterexample:** Identify systems that persist indefinitely but appear unsustainable. If the distinction is explained only by retroactively adding a value, the normative specification procedure needs strengthening.

**Sacrifice counterexample:** Identify a subsystem that remains viable by sacrificing another. Test whether bounded causal closure detects the failure prospectively.

**Transformation counterexample:** Identify cases in which lower-level identity disappears while higher-level values remain. Test whether the identity hierarchy correctly classifies the transition.

**Innovation counterexample:** Examine innovations claimed to remove a constraint. Map new energy, material, institutional, distributional, and risk dependencies instead of assuming limits are either fixed or abolished.

**Conflict counterexample:** Examine incompatible group-specific viability regions. The theory must represent disagreement, bargaining, constitutional constraints, and power without pretending dynamics derive a unique moral solution.

**Unknowability counterexample:** Examine systems whose thresholds or probabilities cannot be estimated reliably. Determine whether scenario, precaution, and adaptive monitoring remain decision-useful.

**Vacuity counterexample:** Attempt to explain failure without adding variables after the event. If the framework requires unlimited post hoc augmentation, it is not a predictive theory.

### 15.2 Comparative model ladder

For every case, compare an output-only model, a stock-and-flow model, a disturbance-and-resilience model, and the full dependency-closed viability model. Complexity is justified only by improvement in prediction, diagnosis, or intervention.


---

## 16. Central conjectures

### 16.1 General sustainability conjecture

> Every persistent sustainability failure can be represented, at an adequate scale and resolution, as the loss or anticipated loss of robust controlled invariance in a causally closed augmented state space—through constraint violation, capacity erosion, support-system degradation, feedback inadequacy, strategic obstruction, or impermissible distribution of benefits, burdens, and risks.

The conjecture is weakened if a genuine sustainability failure cannot be represented without inventing ad hoc variables after the fact. Prospective identification of recurrent structures is therefore essential.

### 16.2 Interdependence fixed-point conjecture

> A complex system is sustainable only if its essential subsystem contracts admit at least one dynamically maintainable, normatively acceptable, robustly compatible fixed point.

This conjecture focuses attention on the compatibility of subsystem requirements rather than separate subsystem performance.

---

## 17. Limitations

First, the current proposal may be a formal framework rather than a substantive universal theory. Robust invariance is mathematically powerful but can become tautological if the constraint set is defined after observing failure. The empirical program must therefore specify constraints and predictions prospectively.

Second, social variables resist reduction to conserved stocks or stable functions. Trust, legitimacy, rights, identity, and power require context-sensitive operationalization and cannot be derived from thermodynamics. Physical laws constrain social systems through material embodiment but do not determine social meaning or justice.

Third, boundaries and protected identities are observer- and purpose-relative. The specification discipline makes these choices visible but does not eliminate disagreement.

Fourth, high-dimensional viability kernels are computationally difficult. Modular contracts, conservative approximations, scenario discovery, and local verification may reduce but not remove this problem.

Fifth, implementable policy sets are endogenous. Institutions, technologies, preferences, and power can change, meaning that the model itself evolves. Transformation must therefore be represented as model or architecture change, not only movement within a fixed state space.

Sixth, irreducible uncertainty limits certification. A sustainability conclusion should remain conditional and revisable rather than being treated as permanent proof.

---

## 18. AI-assisted theory development and verification

Large language models can accelerate synthesis, translation between formal languages, decomposition, counterexample generation, and code production. They also favor plausible continuations, familiar patterns, compressed summaries, and locally convenient repairs. These tendencies create a risk of elegant but shallow theory.

A rigorous workflow should separate roles:

1. **Architect:** a human or accountable research team defines the problem, normative commitments, and final acceptance criteria.
2. **Generator:** an AI system converts conceptual claims into definitions, equations, dependency graphs, or proof obligations.
3. **Adversary:** a separate context or model searches only for missing assumptions, counterexamples, boundary failures, and incompatible definitions.
4. **Verifier:** formal tools, numerical checks, data, and domain experts test the generated claims.

The workflow should proceed through layers:

\[
\text{conceptual intuition}\rightarrow\text{semantic ontology}\rightarrow\text{formal specification}\rightarrow\text{computational model}\rightarrow\text{empirical test}.
\]

Natural-language terms should not be treated as formal variables until their measurement and role are specified. Complex claims should be decomposed into atomic propositions. Models should be asked to falsify before they are asked to repair. The same AI instance should not be treated as an independent evaluator of its own proposal. Formal syntax, unit tests, dimensional checks, model checking, simulation, and proof assistants should replace prose confidence wherever possible.

The modular contract architecture aligns with these safeguards. AI can work on localized assumptions and guarantees while independent reviewers test interfaces. Every generated statement should enter the claim ledger with a type and status. AI output is evidence neither of empirical truth nor of normative legitimacy.


### 18.1 Alignment with LLM strengths

The workflow should exploit broad synthesis, format translation, pattern matching, decomposition, and rapid generation of candidate counterexamples. Raw conceptual material can be compressed into a small set of relations, mapped to established formal frameworks, and expressed as dependency graphs, equations, pseudocode, or contracts. Localized “fill the missing interface” and “debug this broken contract” tasks align better with language-model strengths than the unbounded request to “invent a general theory.”

### 18.2 Controlling shortest-path behavior

Language models often produce the shortest plausible continuation: familiar terminology, smooth prose, and locally convenient repairs. Controls include:

- separate generation from evaluation;
- prohibit undefined abstract nouns in formal phases;
- require explicit input, output, assumption, and guarantee signatures;
- decompose claims until each has one principal inference;
- ask for counterexamples before repairs;
- prevent new variables from being introduced silently;
- require units, limiting cases, and edge cases;
- maintain unresolved gaps rather than bridge them rhetorically;
- use independent sessions or models for adversarial review;
- verify with data, code, model checking, proof assistants, and domain experts.

### 18.3 Layered rigor

Theory development should progress through:

1. conceptual intuition in ordinary language;
2. semantic definitions and ontology;
3. explicit claim typing;
4. symbolic or computational formalization;
5. local verification of modules;
6. compositional verification of interfaces;
7. simulation and sensitivity analysis;
8. empirical testing and revision.

A model should not jump directly from intuition to purported theorem. Each layer has distinct proof obligations.

### 18.4 Axiomatic funnel, qualified

Highly certain physical or logical constraints can be treated as fixed inputs within their valid scope, and lower-level propositions can be required to inherit only explicitly permitted terms. This “axiomatic funnel” reduces hallucinated complexity. It must not, however, label contested empirical claims or normative choices as indubitable. The funnel should therefore begin with a typed premise register rather than an undifferentiated axiom list.

### 18.5 Forest-to-trees and trees-to-forest validation

Top-down work decomposes the general architecture into modules and atomic claims. Bottom-up work checks whether independently validated module relations compose into the claimed general result. Repeated movement in both directions is required. Top-down work alone risks abstraction without evidence; bottom-up work alone risks detailed models without a general theory.


---

## 19. Conclusion

This manuscript proposes a first version of a general theory of sustainability applicable, at a formal level, to ecological, economic, and social systems. Its central definition is relational and qualified: sustainability concerns whether an explicitly specified identity and set of essential values can remain viable under stated disturbances and admissible actions without undermining the capacities and supporting systems required for that viability or impermissibly transferring harm.

The theory can be compressed into four operations:

1. specify what must remain viable, for whom, under what disturbances and horizon;
2. represent critical states, capacities, dependencies, distributions, and deferred liabilities;
3. determine whether an admissible policy can keep the augmented state within the joint viability region; and
4. if it cannot, identify the structural transformation required to make the sustainability kernel nonempty.

In state-space form:

\[
\exists\pi\;\forall w:\quad z^{\pi,w}(t)\in K^*.
\]

In modular form:

\[
A_i\Rightarrow G_i,
\qquad
\bigwedge_{j\ne i}G_j\Rightarrow A_i.
\]

The state-space form specifies the dynamic property. The contract form makes large cross-domain verification tractable and exposes hidden assumptions. Transition sustainability extends the approach to systems currently outside the desired region. Certificates and impossibility results convert vague claims into proof obligations.

The framework should not yet be presented as an established universal theory. Its decisive test is whether capacity erosion, shrinking bottleneck slack, feedback inadequacy, and hidden burden transfer prove to be recurrent leading structures of unsustainability across heterogeneous systems—and whether modelling them improves prediction and intervention beyond simpler alternatives.

---

## References

Aubin, J.-P. (2009). *Viability theory*. Birkhäuser. https://doi.org/10.1007/978-0-8176-4910-4

Aubin, J.-P., Bayen, A. M., & Saint-Pierre, P. (2011). *Viability theory: New directions*. Springer. https://doi.org/10.1007/978-3-642-16684-6

Chen, Y., Anderson, J., Kalsi, K., Low, S. H., & Ames, A. D. (2019). Compositional set invariance in network systems with assume–guarantee contracts. In *Proceedings of the American Control Conference*.

Ekins, P., Simon, S., Deutsch, L., Folke, C., & de Groot, R. (2003). A framework for the practical application of the concepts of critical natural capital and strong sustainability. *Ecological Economics, 44*(2–3), 165–185.

Folke, C., Carpenter, S. R., Walker, B., Scheffer, M., Chapin, T., & Rockström, J. (2010). Resilience thinking: Integrating resilience, adaptability and transformability. *Ecology and Society, 15*(4), 20. https://doi.org/10.5751/ES-03610-150420

Holling, C. S. (1973). Resilience and stability of ecological systems. *Annual Review of Ecology and Systematics, 4*, 1–23. https://doi.org/10.1146/annurev.es.04.110173.000245

Meadows, D. H. (2008). *Thinking in systems: A primer*. Chelsea Green.

Neumayer, E. (2013). *Weak versus strong sustainability: Exploring the limits of two opposing paradigms* (4th ed.). Edward Elgar.

Ostrom, E. (2009). A general framework for analyzing sustainability of social-ecological systems. *Science, 325*(5939), 419–422. https://doi.org/10.1126/science.1172133

Raworth, K. (2012). *A safe and just space for humanity: Can we live within the doughnut?* Oxfam Discussion Paper.

Raworth, K. (2017). *Doughnut economics: Seven ways to think like a 21st-century economist*. Chelsea Green.

Rockström, J., Steffen, W., Noone, K., Persson, Å., Chapin, F. S., III, Lambin, E. F., Lenton, T. M., Scheffer, M., Folke, C., Schellnhuber, H. J., Nykvist, B., de Wit, C. A., Hughes, T., van der Leeuw, S., Rodhe, H., Sörlin, S., Snyder, P. K., Costanza, R., Svedin, U., … Foley, J. A. (2009). Planetary boundaries: Exploring the safe operating space for humanity. *Ecology and Society, 14*(2), 32. https://doi.org/10.5751/ES-03180-140232

Steffen, W., Richardson, K., Rockström, J., Cornell, S. E., Fetzer, I., Bennett, E. M., Biggs, R., Carpenter, S. R., de Vries, W., de Wit, C. A., Folke, C., Gerten, D., Heinke, J., Mace, G. M., Persson, L. M., Ramanathan, V., Reyers, B., & Sörlin, S. (2015). Planetary boundaries: Guiding human development on a changing planet. *Science, 347*(6223), 1259855. https://doi.org/10.1126/science.1259855

Walker, B., Holling, C. S., Carpenter, S. R., & Kinzig, A. (2004). Resilience, adaptability and transformability in social–ecological systems. *Ecology and Society, 9*(2), 5. https://doi.org/10.5751/ES-00650-090205

World Commission on Environment and Development. (1987). *Our common future*. Oxford University Press.

---

# Appendix A. Sustainability specification template

## A1. Focal claim

- System:
- Purpose of assessment:
- Protected identity/functions:
- Time horizon:
- Spatial and organizational boundary:
- Affected populations:

## A2. Constraint register

For every constraint, record:

- variable;
- lower or upper bound;
- unit;
- claim type: P, E, M, N, D, or L;
- evidence;
- uncertainty;
- measurement delay;
- affected group or system;
- substitutability status;
- reversibility status.

## A3. Dynamics and action

- state equations or transition rules;
- available actions;
- technically feasible actions;
- institutionally authorized actions;
- actually implementable actions;
- response delays;
- strategic actors and incentives.

## A4. Closure

- imported resources;
- exported waste;
- ecosystem services;
- external labour and care;
- infrastructure dependencies;
- affected populations outside the focal boundary;
- deferred and intergenerational liabilities.

## A5. Uncertainty

- disturbance classes;
- model alternatives;
- parameter uncertainty;
- correlated shocks;
- irreversible risks;
- accepted risk tolerances and who bears them.

## A6. Result

- sustainability kernel or approximation;
- bottleneck constraint;
- robustness margin;
- viable policy witness;
- transition pathway, if needed;
- impossibility certificate, if applicable;
- monitoring and revision rules.

---

# Appendix B. Claim ledger template

| ID | Claim | Type | Assumptions | Evidence or derivation | Counterexamples sought | Status |
|---|---|---|---|---|---|---|
| C1 | [Claim] | D/L/P/E/M/N | [List] | [Source or proof] | [Tests] | Proposed/Supported/Rejected |

---

# Appendix C. AI-assisted verification protocol

1. Freeze the sustainability specification before asking for conclusions.
2. Ask a generator model to translate each claim into variables, constraints, and dependencies.
3. Require it to label every statement D, L, P, E, M, or N.
4. Use a separate adversarial context to search for omitted groups, scales, dependencies, delays, and counterexamples.
5. Convert each accepted relationship into equations, code, or a formal contract.
6. Test dimensional consistency and limiting cases.
7. Simulate counterfactuals and extreme disturbances.
8. Compare multiple model structures rather than one parameterization.
9. Have domain experts review empirical and normative premises.
10. Use formal proof or model checking for claims presented as logical guarantees.
11. Record unresolved gaps rather than allowing prose to bridge them.
12. Revise the claim ledger and manuscript only after the relevant proof obligation is met.


# Appendix D. Traceability matrix for the theory-building dialogue

This appendix records where each valid substantive element developed during the dialogue appears in Version 0.2. It is intended to make omission visible.

| Dialogue element | Manuscript location | Treatment |
|---|---|---|
| Conjecture versus scientific hypothesis | Sections 3, 16 | Converted into typed claims and falsifiable conjectures |
| Generality creates proof gaps | Sections 1, 9, 18 | Addressed through modularity and localized proof obligations |
| Top-down axiomatization | Sections 3, 6, 18 | Retained with claim-type qualification |
| Layered rigor | Section 18.3 | Restored explicitly |
| AI gap filling and separate adversary | Sections 18, Appendix C | Retained with independent verification requirement |
| Simulations and counterexample search | Sections 14–15, 18 | Retained as empirical and adversarial workflow |
| Ecological, economic, and social universality goal | Entire manuscript | Central scope |
| Thermodynamic ecological foundation | Section 11.10 | Retained with limits on MEP, Onsager, and Carnot claims |
| Matter, energy, entropy, and regeneration | Sections 4, 7, 11.10 | Retained as physical/domain-specific constraints |
| Ontology of state, stock, flow, capacity, load, buffer, feedback | Section 4 | Fully retained |
| Forest-to-trees strategy | Section 18.5 | Restored explicitly |
| LLM shortest-path weakness | Sections 18.1–18.2 | Fully retained as workflow design issue |
| Compression, pattern matching, cloze completion, debugging | Sections 18.1–18.2 | Retained as bounded AI task formats |
| Indubitable truths and axiomatic funnel | Sections 3, 18.4 | Retained but epistemically qualified |
| Four sustainability dimensions | Section 4.9 | Restored |
| Robust controlled invariance | Section 5 | Central formal definition |
| Sustainability corridor | Section 5.4 | Retained |
| Minimum slack/weakest link | Sections 5.5, 9.3, 14 | Retained |
| Twelve operational principles | Section 8.9 | Restored |
| Stock, rate, delay, externalization, growth propositions | Section 7 | Retained with assumptions |
| Strong versus weak sustainability and substitution test | Section 8.7 | Restored in full |
| Recursive dependencies | Sections 4.10, 9 | Restored |
| Scale consistency | Section 4.11 | Restored |
| Temporal consistency and latent liabilities | Section 4.12 | Restored |
| Modular assume–guarantee contracts | Section 9 | Fully retained and expanded |
| Ecological, economic, social, governance contracts | Sections 9.5–9.8 | Restored in detail |
| Interdependence fixed point | Section 9.9 | Restored |
| Reach–avoid–maintain transitions | Section 10 | Retained and expanded |
| Cumulative harm and irreversibility | Section 10 | Retained |
| Restoration/adaptation/transition/transformation | Section 10.1 | Restored |
| Generic stock–capacity–support model | Section 11.6 | Restored |
| Separate ecological example | Section 11.7 | Restored |
| Separate economic example | Section 11.8 | Restored |
| Public-service/social example | Section 11.9 | Restored |
| Coupled ecological–economic–social model | Section 11 | Retained |
| Observability and information delay | Section 12 | Retained and expanded |
| Power and strategic action | Section 12.3 | Retained |
| Indicator tuple and measurement audit | Sections 12.4–12.5 | Restored |
| Control-authority audit | Section 12.6 | Restored |
| Adaptive monitoring and model uncertainty | Sections 12.7–12.8 | Restored |
| Sustainability certificate | Section 13.1 | Retained |
| Certification Levels 0–6 | Section 13.3 | Restored |
| Impossibility certificates | Section 13.2 | Retained |
| Six proof obligations | Section 13.4 | Restored |
| Twelve-step diagnostic algorithm | Section 13.5 | Restored |
| Leading indicators and causal rationale | Section 14 | Retained and expanded |
| Eight hypotheses | Section 14 | Retained |
| Full falsification sweep | Section 15.1 | Restored |
| Comparative model ladder | Section 15.2 | Restored |
| General sustainability conjecture | Section 16.1 | Retained |
| AI-assisted theory workflow | Section 18, Appendix C | Expanded |
| Rejected universal MEP/thermodynamic reduction | Sections 11.10, 17 | Included as qualified/rejected claim rather than omitted |
| Sustainability specification worksheet | Appendix A | Retained |
| Claim ledger | Appendix B | Retained |
| AI verification protocol | Appendix C | Retained |

# Appendix E. Expanded classification of conclusions

A completed assessment should avoid an unsupported binary label. Available conclusions include:

- **Robustly sustainable under \(\Omega\):** a policy witness survives the specified disturbance and model set with positive margins.
- **Conditionally sustainable:** viability depends on assumptions that require active monitoring.
- **Nominally viable but fragile:** constraints hold in the baseline model but robustness margins are small or absent.
- **Transitionally sustainable:** a reach–avoid–maintain pathway exists and respects cumulative-harm constraints.
- **Presently unsustainable but recoverable:** current constraints are violated, but restoration can reach the target without prohibited harm.
- **Structurally unsustainable under the current architecture:** the sustainability kernel is empty or a necessary-condition contradiction exists.
- **Relationally unsustainable:** local viability depends on degradation or burden transfer outside the narrow boundary.
- **Normatively contested:** physical and functional viability exist, but the acceptable region or authority to define it remains disputed.
- **Indeterminate:** evidence, observability, model discrimination, or threshold justification is insufficient.
