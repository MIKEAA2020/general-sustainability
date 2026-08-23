
## 8. Operator II: transformation between architectures

### 8.1 Architecture graph

Let

\[
\mathcal G_A=(Q,E_A)
\]

be a graph of architectures and permitted transitions. A transition is

\[
(q,z)
\longrightarrow
\left(q',R_{qq'}(z)\right),
\]

where \(R_{qq'}\) is a reset or translation map between potentially different state spaces. It carries forward physical stocks, capacities, obligations, affected populations, liabilities, and protected identity predicates.

A hybrid trajectory is

\[
\tau=
(q_0,z_0)ightarrow(q_1,z_1)ightarrow\cdots .
\]

### 8.2 Reach–avoid–maintain transformation

Let \(F_{\mathrm{forbid}}\) be a forbidden set, \(K_{\mathrm{tr}}\) a transition region, and \(K^*_{q'}\) the typed target region in architecture \(q'\). A transformation policy must:

1. avoid \(F_{\mathrm{forbid}}\);
2. respect transition constraints;
3. reach a state in the destination viability kernel;
4. maintain viability thereafter;
5. satisfy identity continuity and normative procedure.

Formally, a candidate meta-policy \(\Pi\) seeks some \(q'\) and time \(T^*\) such that

\[
z(T^*)
\in
\operatorname{Viab}_{\mathcal A_{q'}}
(K^*_{q'},W_{q'},T';U_{q'}^{\mathrm{impl}})
\]

while all transition constraints hold before \(T^*\).

### 8.3 Cumulative harm and irreversibility

For harm \(h_g(t)\) to group or system \(g\), require

\[
\int_0^{T^*}h_g(t)\,dt
\le H_g^{\max}.
\]

Irreversible outcomes belong to \(F_{\mathrm{irr}}\subseteq F_{\mathrm{forbid}}\). Under uncertainty:

\[
\Pr\left[
(q(t),z(t))\in F_{\mathrm{irr}}
\text{ for some }t
\right]
\le\epsilon_{\mathrm{irr}}.
\]

The accepted probability is normatively specified and must identify who bears the risk.

### 8.4 Restoration, adaptation, transition, and transformation

- **Restoration:** moves a degraded state toward a viable region without changing the architecture.
- **Adaptation:** changes behavior or parameters within the architecture.
- **Transition:** follows a time-bounded pathway between regimes; it may or may not change architecture.
- **Transformation:** changes state space, dynamics, institutions, boundary, identity realization, or implementable actions.

Kernel emptiness in the current architecture means that Operator I cannot preserve all frozen constraints. It does not prove that Operator II succeeds.

### Box 6. Conjecture — transformability

> **Transformability Conjecture:** For identifiable classes of systems, persistent contraction or emptiness of the within-architecture viability kernel predicts the need for architecture change earlier than failure of current output indicators.

The terms “identifiable classes,” “contraction,” and “predicts” require formal and empirical development.

### 8.5 Transition credibility

A transition claim must specify:

- destination architecture or target class;
- deadline and milestones;
- transition constraints;
- resources and responsible actors;
- identity-continuity test;
- cumulative-harm budgets;
- monitoring and correction triggers;
- fallback or reversal conditions.

Without these elements, “transition” is an aspiration rather than a modeled path.

---

# Part III. Composition and Embeddedness

## 9. Boundary-interface adequacy

“Causal closure” is replaced by a property-relative interface principle.

### Box 7. Interface principle — boundary adequacy

> Every decision-relevant influence crossing boundary \(B\) must be internalized, represented by a typed interface assumption or guarantee, bounded by a disturbance or scenario envelope, or accompanied by an explicit negligibility claim and sensitivity bound.

For interface \(e\), define

\[
C_e=(A_e,G_e,W_e,\epsilon_e,E_e),
\]

where \(A_e\) is an environmental assumption, \(G_e\) an optional guarantee, \(W_e\) a disturbance envelope, \(\epsilon_e\) an accepted error or failure probability, and \(E_e\) supporting evidence.

Not every environment guarantees behavior. Some interfaces are adversarial bounds, scenarios, unknowns, or monitoring obligations. A boundary certificate must state which kind applies.

A model cut is adequate for proposition \(H\) when discharged interfaces and negligibility bounds support the claim that plausible excluded influences would not reverse \(H\) at the declared confidence. This is not metaphysical completeness. It is auditable truncation.

### 9.1 Boundary audit

For every interface, ask:

1. What crosses the boundary?
2. Is it an input, output, disturbance, obligation, or affected population?
3. Is its behavior endogenous, guaranteed, probabilistic, bounded, scenario-based, or unknown?
4. What evidence supports the envelope?
5. Could violation reverse the assessment?
6. What monitoring detects interface failure?
7. What revision is triggered?

### Box 8. Placeholder — omitted-edge discovery

> A complete algorithm for discovering every consequential omitted interface is not assumed. Future work may combine causal discovery, supply-chain analysis, stakeholder inquiry, sensitivity analysis, and adversarial model review.

---

## 10. Typed dependency hypergraph

Let

\[
\mathcal H=(V,E,\tau_E)
\]

be a directed hypergraph in which an edge may connect multiple source systems to one target or one source to multiple affected systems. Edge type \(\tau_E\) includes:

| Edge type | Meaning | Architectural effect |
|---|---|---|
| Obligatory support | Protected identity of \(A\) requires a function of \(B\) | Relevant function becomes a constraint or interface obligation |
| Optional/substitutable support | Function may be replaced under a substitution test | Replacement allowed only under registered conditions |
| Harmful impact | \(A\) affects protected system or population \(B\) | Relational or normative constraint enters registry |
| Mere nesting | \(B\subset A\) without declared protection | Sacrifice is representable but must be reported |
| Shared-source dependence | Multiple systems draw from one source | Aggregate withdrawal and allocation enter the model |
| Shared-sink contribution | Multiple systems burden one sink | Aggregate burden and responsibility enter the model |

Typed edges resolve the apparent tension between recursion and scale. A containing system is not obliged to preserve every nested subsystem merely because it contains it. Obligatory support, impact, or normative edges create protection. Mere nesting does not.

### 10.1 Recursive dependency

For obligatory support edge

\[
S_a\xleftarrow{q}S_b,
\]

loss of service \(q\) from \(S_b\) can force \(S_a\) outside its functional region. Recursive assessment follows obligatory and impact edges until they terminate in internalized modules, discharged boundary contracts, or justified negligibility claims.

### 10.2 Scale lattice

Systems may be partially ordered by containment or jurisdiction:

\[
S_{\mathrm{individual}}
\preceq
S_{\mathrm{organization}}
\preceq
S_{\mathrm{community}}
\preceq
S_{\mathrm{region}}
\preceq
S_{\mathrm{planet}}.
\]

In general,

\[
\operatorname{Sust}(S_i)
\not\Rightarrow
\operatorname{Sust}(S_j)
\]

and conversely. Typed edges and the frozen specification determine which cross-scale effects become obligations. A local firm may be viable while exceeding its allocated global commons budget; a region may be viable while violating a protected subgroup’s constraints.

---

## 11. Commons and aggregate burdens

For commons node \(C\), let contributors be \(N_C\). Aggregate burden is

\[
L_C
=
\mathcal L_C
\left(\{z_i,a_i\}_{i\in N_C}\right),
\]

where \(\mathcal L_C\) may be additive, nonlinear, path-dependent, or threshold-sensitive. The simple case is

\[
L_C=\sum_i l_i.
\]

The commons constraint is

\[
L_C\le C_C,
\]

where \(C_C\) may itself be state-dependent and uncertain.

### 11.1 Allocation

An institutional or normative procedure assigns budgets or obligations \(b_i\) satisfying, where appropriate,

\[
\sum_i b_i\le C_C.
\]

An actor may violate relational responsibility when

\[
l_i>b_i
\]

even if its individual contribution is not pivotal to threshold crossing.

Allocation may consider:

- equal shares;
- historical responsibility;
- capacity to mitigate;
- benefit received;
- basic needs;
- vulnerability;
- negotiated or legal rules.

These are [N] and [E] inputs, not deductions from sink capacity alone.

### 11.2 Collective action

Actors may choose

\[
a_i\in\arg\max_{a_i}U_i(a_i,a_{-i},z).
\]

A collectively viable burden profile may not be a strategic equilibrium. The architecture therefore distinguishes technical commons feasibility from implementable allocation and compliance.

### Box 9. Placeholder — commons governance

> Game-theoretic, institutional, polycentric, and enforcement models fill the commons-governance module. The architectural requirement is that aggregate capacity and actor-level responsibility both have explicit locations.

---

## 12. Typed contracts and composition

A module is

\[
M_i=(X_i,U_i,Y_i,A_i,G_i,F_i,\mu_i),
\]

where \(\mu_i\) is the contract modality. Contract type attaches to a relation, not an entire domain.

### 12.1 Contract modalities

**Deterministic**

\[
A\Rightarrow_{det}G.
\]

**Robust or set-valued**

\[
A\Rightarrow_{rob}G(W).
\]

**Probabilistic**

\[
A\Rightarrow_{prob}
\Pr(G\mid A,M)
\ge1-\epsilon.
\]

**Strategic**

\[
A\Rightarrow_{strat}
G\in\operatorname{Eq}(A,\Theta).
\]

**Scenario-only** records a condition without claiming a guarantee.

A mass-balance identity may be deterministic; ecological response may be bounded or stochastic; an economic accounting relation may be deterministic while investment behavior is probabilistic; social cooperation may require strategic and empirical semantics.

### 12.2 Type-aware compatibility

A deterministic downstream requirement cannot silently rely on a probabilistic upstream relation. Compatibility may require:

- a buffer;
- redundancy;
- fallback capacity;
- an accepted failure probability;
- a robust envelope;
- a strategy or institution that changes incentives.

All contracts participating in composition must also share compatible time, disturbance, unit, scale, and confidence signatures.

### 12.3 Expanded module templates

#### Ecological module

Inputs may include energy, material pools, climate, extraction, restoration, and pollutant load. Guarantees may include bounded resource flows, habitat conditions, regeneration, and assimilation. Failure modes include depletion, rate overload, threshold crossing, trophic cascade, and loss of regenerative capacity.

#### Economic module

Inputs may include materials, energy, labor, care, ecosystem services, infrastructure, information, institutions, and finance. Outputs may include goods, inventories, maintenance investment, livelihoods, and restoration resources. Failure modes include insolvency, shortage, depreciation, concentration of access, externalization, and maintenance suppression.

#### Social module

Inputs may include material provision, environmental quality, safety, care, information, and participatory channels. Outputs may include capabilities, knowledge, labor, cooperation, and social reproduction. These are empirically operationalized, not treated as conserved substances. Failure modes include deprivation, exclusion, conflict, rights violations, and overload of care or coordination.

#### Governance module

Inputs may include administrative resources, observability, legal authority, legitimacy, compliance, and workload. Outputs may include monitoring, implementation, conflict resolution, and learning. Failure modes include delayed detection, capture, enforcement incapacity, manipulation, and backlog cascades.

### Box 10. Compositional Sustainability Conjecture

> Under identifiable compatibility, timing, robustness, and boundary-interface conditions, locally verified typed contracts can establish a jointly viable system behavior without requiring complete monolithic verification.

The target compositional object may be an invariant set, viable tube, compatible behavior, or strategy profile. A stationary fixed point is only a special case.

### Box 11. Proof obligation — sound composition

A later theorem must specify:

- local state spaces and constraints;
- contract modalities;
- circular-assumption treatment;
- disturbance and delay composition;
- shared-resource competition;
- interface confidence propagation;
- conditions under which local guarantees imply a global typed judgment.

The present manuscript supplies the interface, not the theorem.

---

# Part IV. Domain-General Ontology and Conditional Diagnostics

## 13. States, stocks, capacities, loads, buffers, and feedback

### 13.1 State

A state is the information treated as sufficient to characterize the system for the model and decision. State choice is resolution-dependent. Ecological states may include biomass and nutrients; economic states may include productive capacity, inventories, and obligations; social-service states may include backlog, access, waiting time, and staff capacity.

### 13.2 Stock and flow

A stock is an accumulated quantity; a flow changes it. A generic balance is

\[
\dot s_i=I_i+G_i-O_i-D_i,
\]

where \(I_i\) is input, \(G_i\) generation or regeneration, \(O_i\) output or extraction, and \(D_i\) degradation or loss.

Not every social variable is a conserved stock. A state variable may obey an ODE without being conserved, but its dynamics require empirical justification and measurement semantics.

### 13.3 Capacity

Capacity is the maximum sustainable rate or magnitude of a process under specified conditions:

\[
C_i=C_i(z,t).
\]

Relevant capacities include source, regeneration, sink, processing, buffering, maintenance, coordination, information, governance, and adaptation. Present activity can reduce future capacity:

\[
\dot C_i=R_{C_i}(z)-D_{C_i}(L_i,z)+I_{C_i}.
\]

### 13.4 Load

Load is a demand, extraction, disturbance, waste stream, or coordination requirement. A diagnostic ratio is

\[
\rho_i(t)=\frac{L_i(t)}{C_i(t)}.
\]

Instantaneous \(\rho_i<1\) does not establish sustainability. Cumulative damage, uncertainty, correlated loads, thresholds, distribution, delay, and capacity erosion remain.

### 13.5 Buffer and slack

A buffer temporarily absorbs deviations. Slack is unused capacity. Examples include ecological refugia, food reserves, energy storage, liquidity, infrastructure redundancy, institutional trust reserves, and spare service capacity. A system optimized permanently to its estimated maximum can be efficient yet fragile.

### 13.6 Feedback and response

A policy may use delayed estimated state:

\[
u(t)=\pi(\hat z(t-\tau)).
\]

Response time is

\[
T_r=T_{det}+T_{dec}+T_{impl}+T_{effect}.
\]

Sustainability can therefore depend on observability, measurement accuracy, communication, authority, response speed, enforcement, and learning.
