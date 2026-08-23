# Toward a General Theory of Sustainability
## An Architectural Kernel and Composition Language for Ecological, Economic, and Social Systems

**Working manuscript**  
**Date:** 14 August 2026  
**Author:** [Author name]

---

## Abstract

Sustainability is invoked across ecology, economics, governance, infrastructure, organizations, and social policy, yet its meaning shifts among physical feasibility, persistence, resilience, justice, and long-term provision. This manuscript proposes a candidate architectural kernel and composition language for a general theory of sustainability. The contribution is deliberately top-down: it specifies the objects, judgment types, operators, interfaces, conjectures, and proof obligations that a mature theory would require, while leaving domain mechanisms, empirical calibration, and several formal results as explicit open modules. A sustainability assessment begins with a prospectively frozen specification and an architecture registry. One typed constraint registry distinguishes physical feasibility, functional viability, normative admissibility, relational responsibility, and epistemic status without reducing them to one kind of fact. The formal spine contains two operators: robust viability within a fixed architecture, evaluated from the actual initial state, and hybrid transformation between architectures through reach–avoid–maintain paths constrained by identity continuity, cumulative harm, and irreversibility. Boundary adequacy is represented through explicit interface assumptions, disturbance envelopes, guarantees, and negligibility claims rather than an assertion of causal closure. A typed dependency hypergraph represents obligatory support, substitutable relations, harmful impacts, nested systems, and many-to-one commons burdens. Deterministic, robust, probabilistic, strategic, and scenario contracts allow unlike ecological, economic, and social mechanisms to share interfaces without being treated as identical. The framework derives conditional stock, capacity, buffer, delay, and growth lemmas; supplies diagnostic indicators and certification templates; and formulates conjectures concerning composition, capacity erosion, burden displacement, and transformation. Ecological, economic, public-service, and coupled community models are retained as instantiation sketches rather than presented as validated results. The manuscript concludes with an empirical programme, falsification tests, and an AI-assisted theory-development protocol. It does not claim a completed universal law. It proposes a stable architecture within which formal proofs, domain models, normative procedures, and comparative evidence can accumulate without requiring incompatible definitions of sustainability.

**Keywords:** sustainability; viability theory; transformation; social–ecological systems; ecological economics; robust control; commons; contract-based design; resilience; adaptive governance

---

# Part I. The Architectural Problem

## 1. Introduction

The ambition to formulate a general theory of sustainability confronts a persistent tension. A theory sufficiently abstract to apply to forests, firms, cities, public institutions, economies, and societies can become vacuous. A theory concrete enough to generate predictions usually becomes domain-specific. The task is therefore not to construct one immense model containing every ecological, economic, and social variable. It is to identify a stable architecture that every adequate sustainability model can instantiate while permitting each domain to supply its own mechanisms, evidence, variables, uncertainties, and normative commitments.

The familiar definition of sustainable development—meeting present needs without compromising the ability of future generations to meet their own needs—joins present provision to future capacity (World Commission on Environment and Development, 1987). It does not by itself determine the assessed system, protected identity, thresholds, affected population, disturbance class, policy set, distribution, institutional feasibility, or time horizon. Similar ambiguity appears when sustainability is equated with persistence, equilibrium, resilience, efficiency, circularity, growth, ecological integrity, or justice. These concepts are connected but not interchangeable.

A dictatorship may persist while violating the values an assessment is intended to protect. A profitable industry may continue by degrading an ecosystem on which it depends. An ecosystem may preserve aggregate productivity while losing species or functions judged essential. A national economy may improve territorial indicators by relocating extraction and pollution abroad. A technically possible policy may be institutionally unavailable or strategically unstable. A transition may promise a desirable endpoint while causing prohibited or irreversible harm along the way. A small emitter may not independently destabilize the climate while participating in a collectively destructive burden. These cases imply that sustainability is neither a purely physical property nor a synonym for desirable persistence.

The manuscript proposes the following architectural thesis:

> **Sustainability concerns the continued availability of physically feasible, functionally viable, normatively admissible, and relationally responsible trajectories within and across possible transformations of interdependent systems, under declared boundaries, disturbances, horizons, and implementable actions.**

This thesis is implemented by six commitments:

1. a sustainability claim is relative to a frozen and auditable specification;
2. constraints share one registry but retain typed meanings;
3. viability within an architecture and transformation between architectures are distinct operators;
4. external influences are handled through explicit boundary interfaces, not claims of complete closure;
5. dependencies and burdens are represented by typed hypergraphs, including commons nodes;
6. composition uses relation-specific contract modalities rather than one deterministic logic for all domains.

The commonality proposed across domains is formal, not mechanistic. Ecological, economic, and social systems need not obey the same substantive equations. They can nevertheless be described using states, processes, capacities, constraints, disturbances, dependencies, actions, information, distributions, and values. Whether this architecture eventually supports explanatory laws or predictive improvements is an empirical and formal research question.

### Box 1. Contribution type — architectural kernel

> This manuscript presents a **candidate architectural kernel and composition language** intended to support development of a general theory of sustainability. Definitions and interface principles establish the spine. Conditional lemmas, conjectures, templates, placeholder modules, and proof obligations identify future work. The manuscript does not claim a completed universal explanatory theory.

---

## 2. Intellectual foundations

### 2.1 Viability theory

Viability theory asks whether a dynamical system can remain within a constraint set under admissible controls. Its central object is the viability kernel: the set of initial states from which at least one admissible trajectory remains in the constraint set (Aubin, 2009; Aubin, Bayen, & Saint-Pierre, 2011). This supplies the mathematical basis for within-architecture sustainability. The present architecture extends the question by typing constraints, using an implementable rather than fictional action set, representing boundaries and commons explicitly, and adding transformation between model architectures.

### 2.2 Resilience, adaptation, and transformation

Holling (1973) distinguished ecological resilience from narrow equilibrium stability by emphasizing persistence of relationships under disturbance. Later work developed adaptability and transformability in social–ecological systems (Walker et al., 2004; Folke et al., 2010). This manuscript preserves value-neutral dynamical resilience as a distinct concept while introducing sustainability robustness for persistence of the complete typed sustainability judgment. It also separates adaptation inside an architecture from transformation between architectures.

### 2.3 Social–ecological systems and institutional analysis

Ostrom’s (2009) social–ecological systems framework organizes analysis around resource systems, resource units, users, governance systems, interactions, and outcomes. It supplies a rich diagnostic ontology and cautions against universal institutional prescriptions. The present proposal contributes a formal interface architecture: typed dependencies, implementable actions, aggregate commons burdens, and a distinction between local module behavior and system-level viability.

### 2.4 Ecological economics and strong sustainability

Ecological economics emphasizes material embeddedness, throughput, scale, distribution, and critical natural capital. Strong-sustainability approaches reject automatic substitution of produced capital for every ecological function (Ekins et al., 2003; Neumayer, 2013). Here, strong and weak sustainability become explicit constraint and substitution specifications rather than metaphysical assumptions hidden in aggregation.

### 2.5 Safe and just operating spaces

Planetary-boundary research identifies Earth-system constraints relevant to a safe operating space (Rockström et al., 2009; Steffen et al., 2015). Raworth (2012, 2017) combines ecological ceilings with social foundations. The sustainability corridor developed below generalizes the lower-bound/upper-bound idea and makes it dynamic, typed, capacity-dependent, disturbance-aware, and distribution-sensitive.

### 2.6 Systems, control, and contract-based design

Systems thinking contributes stocks, flows, feedback, delay, nonlinearity, and leverage points (Meadows, 2008). Control theory contributes observability, controllability, robust invariance, and reachability. Assume–guarantee reasoning contributes component contracts and compositional proof obligations. These tools do not determine the right identity, justice standard, or affected population. They become useful after those choices are declared and typed.

### 2.7 The architectural gap

Existing traditions contain most ingredients, but not one agreed spine that simultaneously:

- preserves distinct physical, functional, normative, and relational meanings;
- handles current viability and architecture change;
- prevents hidden burden displacement;
- represents many-to-one commons problems;
- distinguishes theoretical from implementable action;
- composes unlike domain mechanisms through typed interfaces;
- supports conjectures and placeholders without presenting them as completed theorems.

---

## 3. Epistemic discipline and box taxonomy

Every substantive statement should be classified as one of the following:

- **[D] Definition:** fixes terminology.
- **[L] Logical or mathematical consequence:** follows from stated premises.
- **[P] Physical constraint:** follows from accepted physical law under stated scope conditions.
- **[E] Empirical hypothesis:** requires observation, experiment, or comparative evidence.
- **[M] Modelling assumption:** simplifies a particular representation.
- **[N] Normative postulate:** identifies what ought to be protected, prohibited, or distributed.

Conservation of energy is [P]. A claim that institutional trust improves compliance in a specified population is [E]. A minimum-rights threshold is [N]. A finite non-substitutable stock with persistent positive net depletion eventually crosses a positive lower bound is [L] given the balance equation.

The manuscript also distinguishes the function of each displayed box.

| Box type | Function |
|---|---|
| Definition | Official meaning used by the architecture |
| Well-formedness rule | Requirement for a valid sustainability claim |
| Interface principle | Rule governing boundaries, controls, contracts, or dependencies |
| Conditional lemma | Consequence under an explicit model signature |
| Conjecture | Open formal or empirical claim |
| Template | Reusable specification, register, contract, or certificate |
| Placeholder module | Required component whose internal theory remains open |
| Proof obligation | Condition future work must discharge |
| Instantiation sketch | Domain example displaying interfaces and possible mechanisms |
| Limitation | Declared boundary on present claims |

This taxonomy allows ambitious anticipation without confusing scaffolding with established results.

---

# Part II. The Formal Spine

## 4. The sustainability specification

### 4.1 Definition

A sustainability assessment begins with

\[
\Omega=(S,z_0,I^H,I^L,\mathcal V,B,\mathscr C,W,T,\mathcal N,\mathcal R_A),
\]

where:

- \(S\) is the focal system;
- \(z_0\) is the actual initial state or an uncertainty set of initial states;
- \(I^H\) is the protected higher-order identity;
- \(I^L\) contains lower-level features permitted to change under declared rules;
- \(\mathcal V\) is the set of protected functions and values;
- \(B\) is the provisional system boundary;
- \(\mathscr C\) is the typed constraint registry;
- \(W\) is the disturbance and uncertainty class;
- \(T\) is the horizon;
- \(\mathcal N\) identifies normative authority and procedure;
- \(\mathcal R_A\) contains permitted architecture-change and specification-revision rules.

“System \(S\) is sustainable” is incomplete without these qualifiers.

### Box 2. Well-formedness rule — prospective specification

> Identity, values, horizon, affected population, normative authority, and principal constraints must be declared before the assessment outcome is known. Revisions produce a new specification \(\Omega'\) and cannot retroactively change the verdict under \(\Omega\).

This rule permits learning while preventing retrospective goalpost movement.

### 4.2 System and boundary

A system is an observer-specified collection of components, relations, processes, and boundaries treated as coherent for a stated purpose:

\[
S=(X,R,F,B).
\]

Boundaries may be spatial, organizational, legal, demographic, functional, informational, or temporal. No boundary is uniquely correct for all questions. The theory requires exportable justification and interface accounting, not a claim of absolute closure.

### 4.3 Identity hierarchy

System identity is the subset of structures, functions, relationships, or values whose continuity permits later states to count as continuations of the relevant system. The architecture distinguishes:

- \(I^H\): higher-order identity predicates protected across transformation;
- \(I^L\): lower-level realizations that may change.

A forest may replace organisms; an economy may replace firms; a public service may replace technologies. Whether a forest-to-plantation change preserves identity depends on the prospectively declared higher-order predicates—not on an after-the-fact claim that timber production was the only relevant function.

A transformation must satisfy an identity-continuity relation

\[
\mathcal C_I(q,z;q',z')=1.
\]

The theory does not derive the universally correct identity. It forces the identity and its authority into the assessment record.

### 4.4 Normative authority

The slot \(\mathcal N\) records:

- who selected normative constraints;
- which populations participated or were represented;
- which legal, constitutional, ethical, or rights framework applies;
- which constraints are non-revisable;
- how conflict and revision are handled.

The framework does not mechanically solve the dictatorship example. It distinguishes a dictator-relative specification from a constitutional or human-rights specification and prevents either from masquerading as value-free physics.

---

## 5. Architecture registry and control hierarchy

### 5.1 System architecture

For architecture index \(q\), define

\[
\mathcal A_q=(Z_q,F_q,U_q^{\mathrm{impl}},B_q,I_q,\mathscr C_q,\partial_q),
\]

where \(Z_q\) is the state space, \(F_q\) the dynamics or transition correspondence, \(U_q^{\mathrm{impl}}\) the actually implementable actions, \(B_q\) the architecture-specific boundary, \(I_q\) the identity realization, \(\mathscr C_q\) the applicable constraints, and \(\partial_q\) the boundary interfaces.

Let

\[
\mathbb A=\{\mathcal A_q:q\in Q\}
\]

be a registry of recognized or conjectured architectures. It is intentionally open. A first manuscript cannot enumerate all possible institutional, technological, ecological, or social architectures.

### 5.2 Control hierarchy

Define once:

\[
U_{\mathrm{impl}}
\subseteq U_{\mathrm{inst}}
\subseteq U_{\mathrm{tech}}
\subseteq U_{\mathrm{theor}}.
\]

- \(U_{\mathrm{theor}}\): actions permitted by an abstract equation;
- \(U_{\mathrm{tech}}\): technically feasible actions;
- \(U_{\mathrm{inst}}\): institutionally authorized and resourced actions;
- \(U_{\mathrm{impl}}\): actions actually implementable given incentives, power, legitimacy, and strategic response.

Within-architecture viability uses \(U_{\mathrm{impl}}\). Transformation can change this set. Strategic behavior is not an afterthought; it is one reason theoretical and implementable control differ.

### Box 3. Placeholder module — implementability

> A mature theory requires domain-specific institutional, political, and game-theoretic models that estimate \(U_{\mathrm{impl}}\). The architecture fixes where those models enter without claiming a universal equilibrium theory.

---

## 6. One typed constraint registry

### 6.1 Constraint object

The official source of constraints is

\[
\mathscr C=\{c_1,\ldots,c_m\}.
\]

Each entry is

\[
c_j=(p_j,\tau_j,s_j,\rho_j,\nu_j,\kappa_j,g_j,h_j),
\]

where:

- \(p_j\): predicate, interval, inequality, or behavioral condition;
- \(\tau_j\): physical, functional, normative, relational, or epistemic type;
- \(s_j\): subject—state, process, capacity, supporting system, distribution, liability, or interface;
- \(\rho_j\): provenance, evidence, and claim type;
- \(\nu_j\): substitutability rule;
- \(\kappa_j\): reversibility, criticality, and priority;
- \(g_j\): affected group or system;
- \(h_j\): horizon.

This registry resolves the manuscript’s earlier dual decomposition. Physical/functional/normative describes a constraint’s meaning. State/capacity/support/distribution/liability describes its subject. They are orthogonal tags on one record, not rival geometries.

### 6.2 Typed projections

Define

\[
K_P=\bigcap_{\tau_j=P}\{z:p_j(z)\},
\qquad
K_F=\bigcap_{\tau_j=F}\{z:p_j(z)\},
\]

\[
K_N=\bigcap_{\tau_j=N}\{z:p_j(z)\},
\qquad
K_R=\bigcap_{\tau_j=R}\{z:p_j(z)\}.
\]

The combined target may be written

\[
K^*=K_P\cap K_F\cap K_N\cap K_R,
\]

but leaving one projection retains a typed reason:

- leaving \(K_P\): physical infeasibility or model inconsistency;
- leaving \(K_F\): loss of declared function or identity;
- leaving \(K_N\): normative inadmissibility;
- leaving \(K_R\): externalization, burden-allocation failure, or damage to protected relations.

Conjunction does not make the sources equivalent.

### 6.3 Typed judgment vector

For trajectory \(\tau\), define

\[
\mathbf J_\Omega(\tau)
=
\left(P_\Omega(\tau),F_\Omega(\tau),N_\Omega(\tau),R_\Omega(\tau)\right).
\]

Qualified sustainability is

\[
\operatorname{QSust}_\Omega(\tau)
=
P_\Omega(\tau)
\land F_\Omega(\tau)
\land N_\Omega(\tau)
\land R_\Omega(\tau).
\]

The vector prevents injustice from being reported as physical impossibility and prevents local persistence from hiding relational failure.

### 6.4 Essential variables without definitional circularity

A protected loss criterion is first declared through \(I^H\), \(\mathcal V\), or \(\mathscr C\). A variable is **essential relative to that criterion** when a justified causal model shows that its departure from a range can force violation of the criterion under the stated disturbance and action sets. Viability is then preservation of the protected predicates. This breaks the circle in which essentiality and viability define each other.

### 6.5 Strong and weak sustainability

Weak sustainability permits compensation among designated capacities, for example

\[
\sum_i w_iC_i(t)\ge C_{\min}.
\]

Strong sustainability assigns independent non-compensable constraints:

\[
C_i(t)\ge C_i^{\min}
\quad\forall i\in\mathcal C_{\mathrm{critical}}.
\]

The architecture does not decide which capacities are critical. The registry makes that normative and empirical decision explicit.

### Box 4. Template — substitution test

A proposed substitution should record:

1. the essential function being replaced;
2. the substitute and causal mechanism;
3. whether all protected functions or only one output are preserved;
4. deployment scale and rate;
5. energy, material, institutional, and informational requirements;
6. new wastes, risks, and dependencies;
7. distribution of benefits and burdens;
8. reversibility;
9. performance under disturbance and uncertainty;
10. evidence and authority approving the substitution.

Monetary equivalence is not automatically functional equivalence.

---

## 7. Operator I: within-architecture viability

For architecture \(\mathcal A_q\), define the robust viability kernel over horizon \(T\):

\[
\operatorname{Viab}_{\mathcal A_q}
(K^*,W,T;U_q^{\mathrm{impl}})
=
\left\{
 z_0\in K^*:
 \exists\pi\in U_q^{\mathrm{impl}}
 \ \forall w\in W,
 \ z^{\pi,w}(t)\in K^*
 \ \forall t\in T
\right\}.
\]

The focal system is viable within the architecture when

\[
z_0\in
\operatorname{Viab}_{\mathcal A_q}(K^*,W,T;U_q^{\mathrm{impl}}).
\]

Kernel non-emptiness alone proves only that some initial state is viable.

For probabilistic uncertainty, one may instead require

\[
\Pr\left[z^{\pi,w}(t)\in K^*\ \forall t\in T\right]
\ge1-\epsilon.
\]

Risk tolerance \(\epsilon\), and who bears the risk, remain explicit normative and empirical inputs.

### 7.1 Four analytical views

The earlier distinction among state, process, capacity, and relational sustainability is retained as four analytical views—not four parallel primitives.

- **State view:** Are current variables inside their typed bounds?
- **Process view:** Do the dynamics and admissible successors preserve future viability?
- **Capacity view:** Are regenerative, maintenance, monitoring, and adaptive capacities preserved?
- **Relational view:** Does local viability respect protected dependencies, affected populations, and allocated commons burdens?

The process view is a property of \(F_q\) relative to \(K^*\), not a “process stock.” Capacity and relational variables appear through tagged registry entries.

### 7.2 Sustainability corridor

Many systems face a lower provision requirement and upper capacity bound:

\[
a(t)\ge a_{\min}(z),
\qquad
a(t)\le a_{\max}(z).
\]

A local corridor exists when

\[
a_{\min}(z)\le a_{\max}(z).
\]

If the inequality fails at the current state, the state is locally infeasible. Architectural transformation is required only if no admissible within-architecture trajectory can reach a state with a nonempty corridor before entering a forbidden set.

### 7.3 Constraint slack

For lower-bound constraint \(z_i\ge z_i^{\min}\), define, when the denominator is positive,

\[
\sigma_i^-(t)
=
\frac{z_i(t)-z_i^{\min}}
     {z_i^{\mathrm{ref}}-z_i^{\min}}.
\]

For upper-bound constraint \(z_i\le z_i^{\max}\), define

\[
\sigma_i^+(t)
=
\frac{z_i^{\max}-z_i(t)}
     {z_i^{\max}-z_i^{\mathrm{ref}}}.
\]

If the reference equals the bound, use an absolute or problem-specific normalization. The bottleneck diagnostic is

\[
M(t)=\min_i\sigma_i(t).
\]

This is not a welfare aggregate. It reports proximity to the nearest non-compensable boundary.

Let \(W_\gamma\) be an explicitly defined nested family of disturbance sets satisfying \(W_{\gamma_1}\subseteq W_{\gamma_2}\) for \(\gamma_1<\gamma_2\). A robustness margin is

\[
\Gamma(z_0)
=
\sup\left\{
\gamma:
 z_0\in
 \operatorname{Viab}_{\mathcal A_q}(K^*,W_\gamma,T;U^{\mathrm{impl}})
\right\}.
\]

### Box 5. Limitation — within-architecture scope

> Operator I does not represent a change in state space, dynamics, boundary, higher-level identity, or implementable action architecture. Those changes belong to Operator II.
