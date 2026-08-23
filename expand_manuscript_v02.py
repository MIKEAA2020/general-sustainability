from pathlib import Path

src = Path('general_theory_of_sustainability_v0.1.md').read_text(encoding='utf-8')
text = src.replace('**Working manuscript, Version 0.1**', '**Comprehensive working manuscript, Version 0.2**')
text = text.replace('**Date:** 14 August 2026', '**Date:** 14 August 2026  \n**Scope note:** This version incorporates all valid substantive material developed during the preceding theory-building dialogue. Rejected or qualified claims are retained and explicitly evaluated rather than silently omitted.')

insert1 = r'''

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
'''
text = text.replace('\n---\n\n## 5. Formal core', insert1 + '\n\n---\n\n## 5. Formal core')

insert2 = r'''

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
'''
text = text.replace('\n---\n\n## 9. Modular composition', insert2 + '\n\n---\n\n## 9. Modular composition')

insert3 = r'''

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
'''
text = text.replace('\n---\n\n## 10. Transition sustainability', insert3 + '\n\n---\n\n## 10. Transition sustainability')

insert4 = r'''

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
'''
text = text.replace('\n---\n\n## 11. Canonical coupled model', insert4 + '\n\n---\n\n## 11. Canonical coupled model')

insert5 = r'''

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
'''
text = text.replace('\n---\n\n## 12. Observability, power, and strategic action', insert5 + '\n\n---\n\n## 12. Observability, power, and strategic action')

insert6 = r'''

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
'''
text = text.replace('\n---\n\n## 13. Sustainability and impossibility certificates', insert6 + '\n\n---\n\n## 13. Sustainability and impossibility certificates')

insert7 = r'''

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
'''
text = text.replace('\n---\n\n## 14. Leading indicators and testable hypotheses', insert7 + '\n\n---\n\n## 14. Leading indicators and testable hypotheses')

insert8 = r'''

### 14.1 Why the leading indicators should work

A declining minimum slack indicates approach to the first binding essential constraint. A falling capacity-to-load ratio indicates that a system is losing room to respond even if output remains stable. Increasing recovery time suggests weakening restorative dynamics. Rising control effort means more intervention is needed to hold the same state and may expose hidden deterioration. Greater reserve dependence indicates that recurrent loads are being financed by finite buffers. A rising response-time/time-to-threshold ratio indicates that governance is becoming dynamically too slow. Increasing burden transfer indicates apparent local improvement achieved through relational degradation.

None of these is universally predictive in isolation. Their value is as theory-derived candidates to be compared with simpler outcome indicators.
'''
text = text.replace('\nEight hypotheses follow:', insert8 + '\n\nEight hypotheses follow:')

insert9 = r'''

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
'''
text = text.replace('\n---\n\n## 16. Central conjectures', insert9 + '\n\n---\n\n## 16. Central conjectures')

insert10 = r'''

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
'''
text = text.replace('\n---\n\n## 19. Conclusion', insert10 + '\n\n---\n\n## 19. Conclusion')

appendix = r'''

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
'''
text = text + appendix

Path('general_theory_of_sustainability_v0.2_comprehensive.md').write_text(text, encoding='utf-8')
print('written', len(text), 'characters')
