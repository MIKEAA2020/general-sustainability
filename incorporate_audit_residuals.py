from pathlib import Path
p=Path('revised_sustainability_manuscript.md')
s=p.read_text(encoding='utf-8')

# R7: remove change-log phrasing.
s=s.replace('Ecological, economic, public-service, and coupled community models are retained as instantiation sketches rather than presented as validated results.', 'Ecological, economic, public-service, and coupled community models are presented as instantiation sketches rather than as validated results.')
s=s.replace('The earlier distinction among state, process, capacity, and relational sustainability is retained as four analytical views—not four parallel primitives.', 'State, process, capacity, and relational sustainability are treated as four analytical views—not four parallel primitives.')
s=s.replace('“Causal closure” is replaced by a property-relative interface principle.', 'Boundary adequacy is formulated as a property-relative interface principle.')
s=s.replace('The previous manuscript’s twelve principles are retained but reclassified as interface or operational principles rather than undifferentiated axioms.', 'The following twelve principles function as typed interface or operational principles rather than as undifferentiated axioms.')
s=s.replace('The earlier certification hierarchy is retained but renamed so that preliminary accounting is not confused with sustainability.', 'Assessment maturity is distinguished from sustainability certification so that preliminary accounting is not confused with a sustainability result.')
s=s.replace('The former unrestricted claim that every sustainability failure can be represented at an “adequate scale and resolution” is retired because it is too elastic to falsify.', 'No unrestricted claim that every sustainability failure can be represented at an “adequate scale and resolution” is adopted, because such a statement is too elastic to falsify.')

# R1: specification, architecture, actions, policy classes, disturbances.
s=s.replace(r'''\Omega=(S,z_0,I^H,I^L,\mathcal V,B,\mathscr C,W,T,\mathcal N,\mathcal R_A),''',r'''\Omega=(S,z_0,I^H,I^L,\mathcal V,B,\mathscr C,\mathcal I,W,\Delta,T,\mathcal N,\mathcal R_A),''')
s=s.replace('- \\(W\\) is the disturbance and uncertainty class;\n- \\(T\\) is the horizon;', '- \\(\\mathcal I\\) is the declared observation and information structure;\n- \\(W\\) is the disturbance and uncertainty signature;\n- \\(\\Delta\\) is the admissible disturbance-signal or nonanticipating-strategy class;\n- \\(T\\) is the horizon;')
s=s.replace(r'''\mathcal A_q=(Z_q,F_q,U_q^{\mathrm{impl}},B_q,I_q,\mathscr C_q,\partial_q),''',r'''\mathcal A_q=(Z_q,F_q,U_q^{\mathrm{impl}},\mathcal I_q,
\mathbb P_q^{\mathrm{impl}},\Delta_q,B_q,I_q,\mathscr C_q,\partial_q),''')
s=s.replace('where \\(Z_q\\) is the state space, \\(F_q\\) the dynamics or transition correspondence, \\(U_q^{\\mathrm{impl}}\\) the actually implementable actions, \\(B_q\\) the architecture-specific boundary, \\(I_q\\) the identity realization, \\(\\mathscr C_q\\) the applicable constraints, and \\(\\partial_q\\) the boundary interfaces.', 'where \\(Z_q\\) is the state space, \\(F_q\\) the dynamics or transition correspondence, \\(U_q^{\\mathrm{impl}}(z)\\) the implementable instantaneous-action correspondence, \\(\\mathcal I_q\\) the information pattern, \\(\\mathbb P_q^{\\mathrm{impl}}\\) the implementable causal policy class, \\(\\Delta_q\\) the disturbance signal or strategy class, \\(B_q\\) the architecture-specific boundary, \\(I_q\\) the identity realization, \\(\\mathscr C_q\\) the applicable constraints, and \\(\\partial_q\\) the boundary interfaces.')

old=r'''### 5.3 Control hierarchy

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
'''
new=r'''### 5.3 Action and policy hierarchy

Instantaneous action correspondences satisfy

\[
U_{\mathrm{impl}}(z)
\subseteq U_{\mathrm{inst}}(z)
\subseteq U_{\mathrm{tech}}(z)
\subseteq U_{\mathrm{theor}}(z).
\]

- \(U_{\mathrm{theor}}\): actions permitted by an abstract equation;
- \(U_{\mathrm{tech}}\): technically feasible actions;
- \(U_{\mathrm{inst}}\): institutionally authorized and resourced actions;
- \(U_{\mathrm{impl}}\): actions actually executable given incentives, power, legitimacy, compliance, and enforcement.

A causal policy is not an action. It is a rule mapping an available information history to an admissible action. Let

\[
\mathbb P_{\mathrm{impl}}
\subseteq
\mathbb P_{\mathrm{inst}}
\subseteq
\mathbb P_{\mathrm{tech}}
\subseteq
\mathbb P_{\mathrm{theor}}
\]

be the corresponding policy classes, with

\[
\pi(\mathcal I_{[0,t]})
\in U_{\mathrm{impl}}(z(t))
\]

for every state and history compatible with the declared information semantics. A decentralized or strategic implementation may use a policy profile rather than a single controller; its membership in \(\mathbb P_{\mathrm{impl}}\) depends on the applicable equilibrium, enforcement, and information conditions.

Within-architecture viability quantifies over \(\mathbb P_{\mathrm{impl}}\), not over \(U_{\mathrm{impl}}\). Transformation may change both the action correspondence and policy class.
'''
s=s.replace(old,new)
s=s.replace('> A mature theory requires domain-specific institutional, political, and game-theoretic models that estimate \\(U_{\\mathrm{impl}}\\). The architecture fixes where those models enter without claiming a universal equilibrium theory.', '> A mature theory requires domain-specific institutional, political, and game-theoretic models that estimate both \\(U_{\\mathrm{impl}}\\) and \\(\\mathbb P_{\\mathrm{impl}}\\). The architecture fixes where those models enter without claiming a universal equilibrium theory.')

# R6: typed registry removes epistemic as ordinary constraint; add epistemic status.
s=s.replace('- \\(\\tau_j\\): physical, functional, normative, relational, or epistemic type;', '- \\(\\tau_j\\): physical, functional, normative, or relational constraint type;')
s=s.replace('- \\(\\rho_j\\): provenance, evidence, and claim type;', '- \\(\\rho_j\\): provenance, evidence, uncertainty, and epistemic status;')
s=s.replace(r'''\mathbf J_\Omega(\tau)
=
\left(P_\Omega(\tau),F_\Omega(\tau),N_\Omega(\tau),R_\Omega(\tau)\right).''',r'''\mathbf J_\Omega(\tau)
=
\left(P_\Omega(\tau),F_\Omega(\tau),N_\Omega(\tau),R_\Omega(\tau),E_\Omega(\tau)\right).''')
s=s.replace(r'''\operatorname{QSust}_\Omega(\tau)
=
P_\Omega(\tau)
\land F_\Omega(\tau)
\land N_\Omega(\tau)
\land R_\Omega(\tau).''',r'''\operatorname{QSust}_\Omega(\tau)
=
P_\Omega(\tau)
\land F_\Omega(\tau)
\land N_\Omega(\tau)
\land R_\Omega(\tau)
\land E_\Omega(\tau).''')
s=s.replace('The vector prevents injustice from being reported as physical impossibility and prevents local persistence from hiding relational failure.', 'The first four components prevent injustice from being reported as physical impossibility and prevent local persistence from hiding relational failure. The epistemic component \\(E_\\Omega\\) records whether the claimed guarantee is knowable and implementable under the declared information and policy classes; it does not change whether the underlying physical trajectory is possible.')

marker='''### 6.4 Essential variables without definitional circularity
'''
add=r'''### 6.3A Epistemic provenance and epistemic viability

Epistemic status enters the architecture in three distinct places:

1. \(\rho_j\) records the evidence, uncertainty, and confidence supporting each constraint;
2. an information or belief state evolves under \(\mathcal I_q\);
3. the policy class \(\mathbb P_q^{\mathrm{impl}}\) restricts actions to rules implementable from available information.

Define \(E_\Omega(\tau)=1\) when the safety or sustainability claim for \(\tau\) can be certified and implemented under the declared information process and policy class. Physical or full-information viability may therefore exist while epistemic viability is empty. If

\[
\mathbb P_q^{\mathrm{epi}}
\subseteq
\mathbb P_q^{\mathrm{full}},
\]

then policy-class monotonicity gives

\[
\operatorname{Viab}
(\mathcal V_\Omega;\mathbb P_q^{\mathrm{epi}})
\subseteq
\operatorname{Viab}
(\mathcal V_\Omega;\mathbb P_q^{\mathrm{full}}).
\]

Epistemic viability is therefore primarily an Operator I restriction, not an ordinary fifth geometric constraint. The reporting component \(E_\Omega\) identifies inability to certify or implement a guarantee without relabeling that failure as physical impossibility.

'''
s=s.replace(marker,add+marker)

# R3: transition relaxation tags in constraint record and explicit subsection.
s=s.replace(r'''c_j=(p_j,\tau_j,s_j,\rho_j,\nu_j,\kappa_j,g_j,h_j),''',r'''c_j=(p_j,\tau_j,s_j,\rho_j,\nu_j,\kappa_j,g_j,h_j,\zeta_j),''')
s=s.replace('- \\(h_j\\): horizon.', '- \\(h_j\\): horizon;\n- \\(\\zeta_j\\): transition status and authorized relaxation rule.')

marker='''---

## 7. Operator I: within-architecture viability
'''
add=r'''### 6.9 Transition status of constraints

Each constraint receives one transition status \(\zeta_j\):

- **non-relaxable:** must hold throughout every admissible path;
- **temporarily relaxable:** may be weakened only within a declared magnitude and duration;
- **emergency-only:** may be weakened only after a registered emergency trigger;
- **substitutable:** may be discharged through a successful registered substitution test;
- **destination-only:** applies upon entry into the target architecture;
- **compensable under rule:** may be offset only through a specified, authorized, non-silent compensation rule.

Write every constraint as a safety margin \(p_j(z)\ge0\). For an authorized temporary relaxation \(r_j(t)\ge0\), define

\[
K_{\mathrm{tr}}(t)
=
\bigcap_j
\{z:p_j(z)\ge-r_j(t)\},
\]

with \(r_j(t)=0\) for non-relaxable constraints. A relaxation record must specify authority, trigger, magnitude, duration, affected groups, monitoring, cumulative harm, and required repair. A transition-debt state may satisfy

\[
\dot\lambda_j^{\mathrm{tr}}
\ge a_j r_j(t)-\operatorname{repair}_j(t),
\qquad
0\le\lambda_j^{\mathrm{tr}}
\le\bar\lambda_j^{\mathrm{tr}}.
\]

Physical impossibilities cannot be relaxed. Normative constraints declared non-revisable by \(\mathcal N\) remain non-relaxable. The transition region is therefore generated by typed authorization, not selected after observing which constraints a proposed path violates.

---

## 7. Operator I: within-architecture viability
'''
s=s.replace(marker,add)

# R1: Operator I corrected.
s=s.replace(r'''\operatorname{Viab}_{\mathcal A_q}
(K^*,W,T;U_q^{\mathrm{impl}})
=
\left\{
 z_0\in K^*:
 \exists\pi\in U_q^{\mathrm{impl}}
 \ \forall w\in W,
 \ z^{\pi,w}(t)\in K^*
 \ \forall t\in T
\right\}.''',r'''\operatorname{RViab}_{\mathcal A_q}
(K^*,T)
=
\left\{
 z_0\in K^*:
 \exists\pi\in\mathbb P_q^{\mathrm{impl}}
 \ \forall\delta\in\Delta_q,
 \ z^{\pi,\delta}(t)\in K^*
 \ \forall t\in T
\right\}.''')
s=s.replace(r'''z_0\in
\operatorname{Viab}_{\mathcal A_q}(K^*,W,T;U_q^{\mathrm{impl}}).''',r'''z_0\in
\operatorname{RViab}_{\mathcal A_q}(K^*,T).''')
s=s.replace(r'''\operatorname{Viab}_{\mathcal A_q}(K^*,W_\gamma,T;U^{\mathrm{impl}})''',r'''\operatorname{RViab}_{\mathcal A_q}(K^*,T;\Delta_\gamma)''')
s=s.replace('A candidate meta-policy \\(\\Pi\\) seeks', 'A candidate meta-policy \\(\\Pi\\in\\mathbb P^{\\mathrm{meta}}\\) seeks')
s=s.replace(r'''\operatorname{Viab}_{\mathcal A_{q'}}
(K^*_{q'},W_{q'},T';U_{q'}^{\mathrm{impl}})''',r'''\operatorname{RViab}_{\mathcal A_{q'}}
(K^*_{q'},T')''')

# R2: official system assessment map before Part III.
marker='''---

# Part III. Composition and Embeddedness
'''
add=r'''### 8.8 Official system-level assessment map

Let

\[
\mathcal K_q
=
\operatorname{RViab}_{\mathcal A_q}(K_q^*,T)
\]

be the current architecture's robust kernel. Let \(\mathcal E_q\supseteq K_q^*\) be an authorized emergency envelope and

\[
\mathcal C_q
=
\operatorname{Capt}^{H}_{\mathbb P_q^{\mathrm{impl}},\Delta_q}
(\mathcal K_q;\mathcal E_q)
\]

its robust capture basin over recovery horizon \(H\). Let \(\operatorname{Trans}_\Omega(q_0,z_0)\) mean that an admissible meta-policy satisfies the Operator II reach–avoid–maintain, identity, transition-relaxation, and cumulative-harm conditions and reaches a destination kernel.

The official assessment map is ordered as

\[
\mathfrak A_\Omega(q_0,z_0)
=
\begin{cases}
\text{currently viable},&z_0\in\mathcal K_{q_0},\\
\text{recoverable within architecture},&z_0\notin\mathcal K_{q_0},\ z_0\in\mathcal C_{q_0},\\
\text{transformationally viable},&z_0\notin\mathcal C_{q_0},\ \operatorname{Trans}_\Omega(q_0,z_0),\\
\text{infeasible within known architectures},&\text{all registered paths fail under discharged interfaces},\\
\text{indeterminate},&\text{otherwise}.
\end{cases}
\]

Every status is accompanied by \(\mathbf J_\Omega=(P,F,N,R,E)\), its horizon, confidence, boundary adequacy, and unresolved proof obligations. “Infeasible within known architectures” is not universal impossibility unless the architecture class and physical obstruction justify that stronger conclusion.

---

# Part III. Composition and Embeddedness
'''
s=s.replace(marker,add)

# R4: add epistemic status hierarchy after box taxonomy.
marker='''This taxonomy allows ambitious anticipation without confusing scaffolding with established results.
'''
add=marker+r'''

A second, independent axis records epistemic status.

| Epistemic status | Admission rule |
|---|---|
| Definition/architectural postulate | Declares an object, type, convention, or adopted normative requirement |
| Identity | Follows by construction or direct algebra |
| Theorem | Complete proof under explicit mathematical assumptions |
| Conditional theorem/lemma | Complete implication whose hypotheses are not established for every intended application |
| Conjecture | Precise unproved statement with a proof gap and disproof route |
| Numerical proposition | Reproducible statement tied to a model version, algorithm, tolerances, and archived output |
| Empirical hypothesis | Population, observables, estimator, uncertainty, and falsification rule are declared |
| Normative postulate | Protected value, right, entitlement, or authority is explicitly adopted rather than inferred from dynamics |
| Research programme | Proposed extension or connection without a claim of completion |

Box function and epistemic status are orthogonal. A “conjecture box” can contain a formal or empirical conjecture; an “instantiation sketch” can contain identities, assumptions, and hypotheses. Appendix G contains the populated claim-status ledger for the named claims in this manuscript.
'''
s=s.replace(marker,add)

# R5: contribution and novelty matrix before epistemic discipline.
marker='''---

## 3. Epistemic discipline and box taxonomy
'''
add=r'''### 2.8 Provisional contribution matrix

The architecture integrates established traditions but does not claim ownership of their component results. The table states the proposed incremental contribution that must be tested against the full literature.

| Established tradition | Established contribution | Proposed architectural increment | Present status |
|---|---|---|---|
| Classical viability theory | Viability kernels, capture basins, tangency and regulation | Typed sustainability specification plus current-state, recovery, and transformation status map | Synthesis; formal subclasses supplied by Articles 001–002 |
| Robust/discriminating kernels | Adversarial disturbances and robust invariance | Explicit disturbance signatures joined to normative, relational, and interface typing | Architectural synthesis |
| Partial-observation and information-state safety | Belief states, observers, knowledge games | Epistemic sustainability reporting linked to implementable policy classes and typed judgments | Synthesis with restricted theorem programme |
| Sampled, hybrid, and RFDE safety | Review-time, tube, hybrid, and history-state invariance | Common decision-clock and interface registry across sustainability modules | Restricted results and open generalization |
| Contract-based and compositional invariance | Local assume–guarantee proof rules | Relation-level deterministic, robust, probabilistic, strategic, and scenario modalities with commons dependencies | Conjectural general layer; restricted theorems available |
| Social–ecological systems and commons governance | Resource–user–institution interactions and design mechanisms | Mapping institutions, information, enforcement, allocation, and shared sinks into viability operators | Cross-domain synthesis and formal cases |
| Ecological economics and strong sustainability | Throughput, critical natural capital, substitution limits, distribution | Typed non-compensation and pathway-specific substitution certificates inside dynamic viability | Synthesis with formal CES/Farkas modules |
| Safe-and-just-space frameworks | Ecological ceilings and social foundations | Horizon-, policy-, information-, and transformation-sensitive safe-and-just trajectories | Architectural extension |
| Systems and resilience science | Stocks, flows, feedback, delay, regime persistence | Distinction among dynamical resilience, sustainability robustness, recoverability, and transformability | Conceptual and formal synthesis |
| Model reduction and coarse-graining | Exact projection, approximation, aggregation error | Mandatory model-map and scale-transfer proof obligations for sustainability claims | Formal integration programme |

This matrix is provisional until a systematic review verifies priority, terminology, and overlap. Novelty may reside in a theorem, counterexample, interface, synthesis, or research programme; those categories must not be conflated.

---

## 3. Epistemic discipline and box taxonomy
'''
s=s.replace(marker,add)

# R4: replace Appendix G template with populated high-level ledger.
start=s.index('# Appendix G. Claim-ledger template')
# Preserve everything before G; it is final appendix after AI appendix removal.
ledger=r'''# Appendix G. Populated claim-status ledger

| ID | Named claim or object | Manuscript function | Epistemic status | Principal assumptions or authority |
|---|---|---|---|---|
| D1 | Sustainability specification \(\Omega\) | Definition | Architectural definition | Purpose-relative declared assessment |
| D2 | Architecture \(\mathcal A_q\) and registry \(\mathbb A\) | Definition | Architectural definition | Declared state, dynamics, policies, interfaces |
| D3 | Typed constraint registry \(\mathscr C\) | Definition/template | Architectural definition | Provenance and authority recorded per entry |
| D4 | Typed judgment vector \((P,F,N,R,E)\) | Definition | Architectural definition | Typed predicates and information process |
| D5 | Operator I robust viability | Definition | Established viability construction specialized here | Causal policy and disturbance classes |
| D6 | Operator II transformation | Definition/research architecture | Architectural postulate and research programme | Architecture graph, reset maps, transition rules |
| D7 | System-level assessment map \(\mathfrak A_\Omega\) | Definition | Architectural definition | Ordered current/recovery/transformation tests |
| WF1 | Prospective specification locking | Well-formedness rule | Methodological/normative postulate | Declared authority and preregistration |
| IP1 | Boundary-interface adequacy | Interface principle | Methodological postulate | Discharged interfaces and sensitivity bounds |
| IP2 | Typed dependency and commons accounting | Interface principle | Architectural definition plus normative allocation | Registered edge types and allocation authority |
| IP3 | Transition relaxation rule | Interface principle | Architectural/normative postulate | Constraint-specific authorization and debt limits |
| IP4 | Contract modality compatibility | Interface principle | Architectural postulate | Common units, horizons, confidence, and timing |
| L1 | Finite essential-stock condition | Conditional lemma | Mathematical consequence | Non-substitution, positive floor, persistent net depletion |
| L2 | Rate–buffer condition | Conditional lemma | Mathematical consequence | Declared capacity, buffer, and duration |
| L3 | Zero-margin fragility | Conditional lemma | Mathematical consequence | Disturbance direction and absent response/buffer |
| L4 | Delay condition | Conditional lemma | Conditional mathematical implication | Valid \(T_r,T_c\) estimates |
| L5 | Obligatory-support condition | Conditional lemma | Logical consequence of typed dependency | Registered support and no substitute |
| L6 | Non-compensation | Conditional lemma/interface rule | Logical consequence plus normative tag | Constraint designated non-compensable |
| L7 | Conditional growth bound | Conditional lemma | Mathematical consequence | Persistent intensity and bounded capacity |
| L8 | Local corridor failure | Conditional lemma | Mathematical consequence | Declared lower and upper activity bounds |
| C1 | Compositional sustainability | Conjecture box | Formal conjecture | Compatibility, timing, robustness, interfaces |
| C2 | Transformability | Conjecture box | Formal/empirical conjecture | Identified system class and kernel metric |
| C3 | Capacity-leading failure | Conjecture box | Empirical hypothesis | Preregistered indicators and comparison model |
| C3A | Bottleneck–robustness relation | Conjecture box | Empirical hypothesis | Comparable disturbance geometry and controls |
| C4 | Boundary-expansion reversal | Conjecture box | Empirical hypothesis | Preregistered boundary alternatives |
| C5 | Distributional dynamics | Conjecture box | Empirical hypothesis | Causal distribution-to-dynamics mechanism |
| C6 | Correlated disturbance | Conjecture box | Empirical hypothesis | Joint shock model and benchmark |
| C7 | Maintenance suppression | Conjecture box | Empirical hypothesis | Maintenance/output separation and lag |
| C8 | Efficiency–scale interaction | Conjecture box | Empirical hypothesis | Rebound and total-burden measurements |
| M1 | Stock–capacity–support model | Instantiation sketch | Modeling assumption/template | Uncalibrated generic dynamics |
| M2 | Grassland model | Instantiation sketch | Modeling assumption | Domain calibration required |
| M3 | Economic model | Instantiation sketch | Modeling assumption | Behavioral contracts required |
| M4 | Public-health model | Instantiation sketch | Modeling assumption | Measurement and strategic semantics required |
| M5 | Coupled community model | Instantiation sketch | Modeling assumption/hypothesis generator | No validated kernel claimed |
| RP1 | Restricted composition theorem programme | Proof obligation | Research programme | Contract synthesis and confidence propagation |
| RP2 | Hybrid transformation semantics | Proof obligation | Research programme | Cross-architecture policies and obligation translation |
| RP3 | Empirical comparative programme | Research programme | Empirical programme | Preregistered cases and model ladder |

The research-program claim ledger contains source-level theorems, proofs, bridges, and verification status. This appendix records the named claims of the architectural manuscript and is updated whenever a claim changes status.
'''
s=s[:start]+ledger+'\n'

# Add references needed for novelty matrix before existing references end; simple insertion after Aubin/Bayen.
ref_marker='''Aubin, J.-P., Bayen, A. M., & Saint-Pierre, P. (2011). *Viability theory: New directions*. Springer. https://doi.org/10.1007/978-3-642-16684-6
'''
refs=ref_marker+'''\nBlanchini, F. (1999). Set invariance in control. *Automatica, 35*(11), 1747–1767.\n\nGoebel, R., Sanfelice, R. G., & Teel, A. R. (2012). *Hybrid dynamical systems: Modeling, stability, and robustness*. Princeton University Press.\n\nHale, J. K., & Verduyn Lunel, S. M. (1993). *Introduction to functional differential equations*. Springer.\n\nMunda, G., & Nardo, M. (2009). Noncompensatory/nonlinear composite indicators for ranking countries: A defensible setting. *Applied Economics, 41*, 1513–1523. https://doi.org/10.1080/00036840601019364\n\nO’Neill, D. W., Fanning, A. L., Lamb, W. F., & Steinberger, J. K. (2018). A good life for all within planetary boundaries. *Nature Sustainability, 1*, 88–95. https://doi.org/10.1038/s41893-018-0021-4\n\nSaint-Pierre, P. (1994). Approximation of the viability kernel. *Applied Mathematics and Optimization, 29*, 187–209. https://doi.org/10.1007/BF01204182\n'''
s=s.replace(ref_marker,refs)

# Conclusion updates for policy and epistemic layers.
s=s.replace('4. a typed physical, functional, normative, and relational judgment vector;', '4. a typed physical, functional, normative, relational, and epistemic judgment vector;')
s=s.replace('5. within-architecture viability evaluated from the actual initial state;', '5. within-architecture viability evaluated from the actual initial state under a causal implementable policy class;')

p.write_text(s,encoding='utf-8')
print('updated chars',len(s))
