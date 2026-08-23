from pathlib import Path
p=Path('revised_sustainability_manuscript.md')
text=p.read_text(encoding='utf-8')

# 1. Augmented-state template + general dynamics
needle='''Let

\\[
\\mathbb A=\\{\\mathcal A_q:q\\in Q\\}
\\]

be a registry of recognized or conjectured architectures. It is intentionally open. A first manuscript cannot enumerate all possible institutional, technological, ecological, or social architectures.
'''
insert=needle+r'''

### 5.2 Augmented-state template

A useful architecture may organize its state as

\[
z_q(t)=
\begin{bmatrix}
 x_q(t)\\
 c_q(t)\\
 e_q(t)\\
 d_q(t)\\
 \lambda_q(t)
\end{bmatrix},
\qquad
\dot z_q\in F_q(z_q,u_q,w_q),
\]

where:

- \(x_q\) contains focal-system states;
- \(c_q\) contains enabling, regenerative, maintenance, informational, or governance capacities;
- \(e_q\) contains internally represented supporting-system states;
- \(d_q\) contains distributions of benefits, burdens, rights, and risks;
- \(\lambda_q\) contains deferred liabilities.

This is a template, not a mandatory universal decomposition. Each block may be vector-valued, replaced, or omitted when it is irrelevant. For discrete, stochastic, set-valued, agent-based, or hybrid systems, \(F_q\) is interpreted as the appropriate transition rule or correspondence rather than an ordinary differential equation.
'''
text=text.replace(needle,insert)
text=text.replace('### 5.2 Control hierarchy','### 5.3 Control hierarchy')

# 2. Disturbance-class signature
needle='''### Box 3. Placeholder module — implementability

> A mature theory requires domain-specific institutional, political, and game-theoretic models that estimate \\(U_{\\mathrm{impl}}\\). The architecture fixes where those models enter without claiming a universal equilibrium theory.
'''
insert=needle+r'''

### 5.4 Disturbance-class signature

A robustness claim must characterize more than a generic disturbance symbol. A disturbance specification should record, as relevant:

- admissible support or scenario set;
- magnitude or intensity;
- duration;
- frequency or recurrence structure;
- temporal and cross-domain correlation;
- spatial extent;
- predictability and observation delay;
- probability law, adversarial status, or deep-uncertainty status.

A generic template is

\[
W=(\mathcal W,\mu,\Delta,\phi,\chi,\ell,\mathcal P),
\]

where the entries respectively record admissible disturbances, magnitude, duration, recurrence, correlation, spatial extent, and probability or model status. The exact representation remains domain-specific. Two systems are not meaningfully compared as “equally robust” unless their disturbance signatures are comparable.
'''
text=text.replace(needle,insert)

# Optional 10: explanatory examples for four views
needle='''- **Relational view:** Does local viability respect protected dependencies, affected populations, and allocated commons burdens?

The process view is a property of \\(F_q\\) relative to \\(K^*\\), not a “process stock.” Capacity and relational variables appear through tagged registry entries.
'''
insert='''- **Relational view:** Does local viability respect protected dependencies, affected populations, and allocated commons burdens?

The views can diverge. A lake may currently satisfy a water-quality threshold while continuing pollutant accumulation commits it to later failure. A firm may be solvent while obligations accumulate faster than repayment capacity. A service may preserve current output by exhausting staff and maintenance capacity. A local economy may remain viable by exporting pollution or deprivation beyond its reporting boundary.

The process view is a property of \\(F_q\\) relative to \\(K^*\\), not a “process stock.” Capacity and relational variables appear through tagged registry entries.
'''
text=text.replace(needle,insert)

# 5. Explicit hybrid reach-avoid-maintain equations
needle='''Formally, a candidate meta-policy \\(\\Pi\\) seeks some \\(q'\\) and time \\(T^*\\) such that

\\[
z(T^*)
\\in
\\operatorname{Viab}_{\\mathcal A_{q'}}
(K^*_{q'},W_{q'},T';U_{q'}^{\\mathrm{impl}})
\\]

while all transition constraints hold before \\(T^*\\).
'''
insert=r'''Formally, a candidate meta-policy \(\Pi\) seeks some \(q'\) and time \(T^*\) satisfying the hybrid reach–avoid–maintain conditions

\[
(q(t),z(t))\notin F_{\mathrm{forbid}}
\qquad\forall t,
\]

\[
(q(t),z(t))\in K_{\mathrm{tr}}(t)
\qquad 0\le t<T^*,
\]

\[
(q(T^*),z(T^*))
\in
\{q'\}\times
\operatorname{Viab}_{\mathcal A_{q'}}
(K^*_{q'},W_{q'},T';U_{q'}^{\mathrm{impl}}),
\]

followed by

\[
z(t)\in K^*_{q'}
\qquad\forall t\in[T^*,T^*+T']
\]

under the destination architecture and declared disturbance class. The target is therefore not merely a point in a new state space; it is a state from which destination-architecture viability can be maintained.
'''
text=text.replace(needle,insert)

# 6. Transition delay + just transition
needle='''Without these elements, “transition” is an aspiration rather than a modeled path.
'''
insert=needle+r'''

### Box 6B. Interface principle — transition delay and justice

> Transition language is not evidence of a transition path and must not legitimize indefinite postponement. Interim constraints must cover group-specific provision, burdens, rights, displacement, participation, cumulative harm, funding, responsible actors, milestones, and correction triggers. An ecologically viable destination reached through prohibited deprivation or irreversible damage is normatively inadmissible under the original specification.
'''
text=text.replace(needle,insert)

# 3 and 4: regeneration/maintenance/adaptive capacity + concept comparison
needle='''## 14. Interface principles and operational principles
'''
insert=r'''## 13A. Regeneration, maintenance, and adaptive capacity

**Regeneration** is a process that moves a depleted renewable stock or capacity toward its registered viable range.

**Maintenance** is action that prevents or slows deterioration of an enabling capacity. Current provision can therefore appear successful while consuming the capacity that makes future provision possible.

**Adaptive capacity** is the set of implementable within-architecture changes that can preserve or enlarge the viability kernel under altered conditions. Schematically,

\[
\mathcal U_{\mathrm{adapt}}(q,z)
=
\left\{
\Delta u\in U_q^{\mathrm{impl}}:
\operatorname{Viab}_{\mathcal A_q}^{\,\Delta u}
\text{ is preserved or enlarged under the declared comparison}
\right\}.
\]

This expression is a template: “enlarged” requires a declared state domain, disturbance signature, horizon, and ordering.

**Transformative capacity** is the set of admissible meta-actions, resources, institutions, and translation maps that make one or more architecture transitions available. Kernel emptiness establishes a need for architecture change under the frozen specification; it does not establish transformative capacity.

## 13B. Persistence, stability, resilience, and sustainability

| Concept | Core question |
|---|---|
| Persistence | Does a recognizable system or regime continue? |
| Stability | Does it remain near or return toward a reference behavior under specified dynamics? |
| Dynamical resilience | Which disturbances can it absorb while preserving a declared regime or functional identity? |
| Sustainability | Are physically feasible, functionally viable, normatively admissible, and relationally responsible paths available within or across architectures? |

Sustainable systems need not be static. They may fluctuate, reorganize, learn, and transform. Conversely, harmful institutions can be persistent, stable over a range, and dynamically resilient without satisfying the complete sustainability judgment.

## 14. Interface principles and operational principles
'''
text=text.replace(needle,insert)

# 9 physical ecological interface example
needle='''Thermodynamics constrains social systems through physical embodiment but does not derive rights, justice, legitimacy, or meaning.
'''
insert=needle+r'''

### Box 12A. Ecological interface example

A physical ecological module may receive energy flux, temperature, finite material pools, climatic conditions, extraction, restoration, and disturbance as inputs. It may offer resource flows, regenerated biomass, ecosystem services, habitat conditions, assimilative capacity, waste streams, degraded heat, and uncertainty envelopes as outputs. These interfaces allow economic and social modules to respect physical conditions without claiming that social value, legitimacy, or justice reduces to energy and material variables.
'''
text=text.replace(needle,insert)

# 8 joint state and constraints
needle='''The policy vector is

\\[
u=(H,A,J_E,J_K,J_G,\\theta_1,\\ldots,\\theta_n).
\\]

Candidate failure loops include:
'''
insert=r'''The policy vector is

\[
u=(H,A,J_E,J_K,J_G,\theta_1,\ldots,\theta_n).
\]

An illustrative augmented state is

\[
z=
(R,P,E,K,I,Q,G,C_1,\ldots,C_n,V_1,\ldots,V_n).
\]

Its typed constraint registry may generate the joint conditions

\[
R\ge R_{\min},\quad
P\le P_{\max},\quad
E\ge E_{\min},\quad
K\ge K_{\min},\quad
I\ge I_{\min},
\]

\[
Q\le Q_{\max},\quad
G\ge G_{\min},\quad
C_g\ge C_g^{\min},\quad
V_g\le V_g^{\max}
\qquad\forall g.
\]

These bounds do not all have the same status. Resource and pollution conditions may combine physical and functional evidence; provision and violation bounds may be normative; governance thresholds may be empirical-functional; and commons allocations are relational. The registry retains those types while Operator I evaluates their joint attainability.

Candidate failure loops include:
'''
text=text.replace(needle,insert)

# Optional 11 policy witness emphasis
needle='''A qualified certificate should include:

1. frozen \\(\\Omega\\) and architecture index;
'''
insert='''A qualified certificate requires an **implementable policy witness** for Operator I or an implementable meta-policy witness for Operator II. The existence of desirable states without a path or strategy does not establish sustainability.

A qualified certificate should include:

1. frozen \\(\\Omega\\) and architecture index;
'''
text=text.replace(needle,insert)

# 7 bottleneck robustness conjecture; renumber subsequent conjectures not essential, use 3A
needle='''### Conjecture 3. Capacity-leading failure

Declining regenerative, maintenance, or governance capacity predicts typed sustainability failure earlier than current output measures.
'''
insert=needle+r'''

### Conjecture 3A. Bottleneck–robustness relation

Within a preregistered system class and comparable disturbance geometry, smaller typed bottleneck margin predicts a smaller empirically estimated robustness margin after controlling for dynamics, response, and buffer structure. The controls distinguish an empirical cross-system claim from the definitional fact that a state closer to a boundary has less geometric distance in one direction.
'''
text=text.replace(needle,insert)

# Optional 12 AI operationalization
needle='''A claim should not jump from intuition to theorem.
'''
insert=needle+r'''

Natural-language concepts should not become formal variables until their operational meaning, scale, measurement interface, and—where applicable—units are specified. Formal syntax, dimensional checks, unit tests, simulation, model checking, and proof assistants should replace prose confidence wherever the claim type permits.
'''
text=text.replace(needle,insert)

p.write_text(text,encoding='utf-8')
print('updated',len(text))
