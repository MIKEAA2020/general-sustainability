from pathlib import Path
p=Path('revised_sustainability_manuscript.md')
text=p.read_text()

add_a=r'''

### 6.6 Relation between constraint subject and constraint type

The registry has two independent axes. A capacity constraint may be physical, functional, normative, or relational. A distributional constraint is usually normative but can also enter functional dynamics. An ecological support constraint may be physical in one model and precautionary in another. The two-axis representation can be displayed as a matrix:

| Subject | Physical | Functional | Normative | Relational |
|---|---|---|---|---|
| Focal state | material feasibility | identity/function threshold | prohibited focal condition | local state linked to external obligation |
| Capacity | process-rate limit | minimum maintenance/adaptation capacity | required reserve or safety margin | capacity owed to dependent systems |
| Supporting system | biophysical boundary | required service level | protected ecological status | impact or dependency obligation |
| Distribution | accounting feasibility | distribution affecting system performance | rights, minima, maximum burdens | cross-group or cross-scale allocation |
| Liability | physically accumulated debt or damage | future functional impairment | prohibited deferred burden | burden transferred across time or place |

This matrix prevents an ontological subject from being mistaken for an epistemic or normative type.

### 6.7 Ordering and conflict among constraints

Typed separation does not eliminate conflict. A policy may satisfy a physical and functional condition while violating a right, or satisfy a social minimum only by crossing an ecological bound under the current architecture. The registry therefore records priority and revisability.

A possible decision structure is lexicographic:

1. exclude physically impossible trajectories;
2. exclude trajectories violating non-revisable rights or irreversible critical constraints;
3. evaluate remaining functional and relational trade-offs;
4. report unresolved conflicts rather than hiding them in a weighted sum.

This ordering is a template, not a universal moral theorem. Alternative legitimate procedures may use constitutional rules, deliberation, multi-criteria decision analysis, negotiated allocations, or precaution. The architectural requirement is that the procedure and its authority be explicit.

### 6.8 Comparison of competing specifications

The framework permits multiple specifications \(\Omega_1,\ldots,\Omega_n\) for the same physical system. Rather than forcing a false unique verdict, it can report:

- constraints shared across specifications;
- verdicts invariant across specifications;
- disagreements caused by identity, horizon, boundary, or normative authority;
- policies viable under all specifications;
- policies viable only under contested assumptions.

A **respecification-robust conclusion** is one that holds across a declared family \(\mathfrak O\):

\[
\forall\Omega\in\mathfrak O,
\quad
\mathbf J_\Omega(\tau)
\text{ satisfies the target condition}.
\]

This does not solve moral disagreement. It identifies which conclusions depend on it.
'''
text=text.replace('\n---\n\n## 7. Operator I',add_a+'\n\n---\n\n## 7. Operator I')

add_b=r'''

### 8.6 Architecture-change costs and option value

Transformation consumes resources and may close future options. Let \(C_{qq'}(z)\) denote financial, material, ecological, institutional, and social transition costs. Let \(O(q,z)\) represent the set of future architecture transitions still available. A meta-policy should account for both immediate viability and option preservation.

A transition can be rejected because it:

- crosses an irreversible state;
- violates cumulative-harm budgets;
- destroys higher-order identity;
- transfers prohibited burdens;
- makes the destination architecture nonviable under plausible disturbances;
- eliminates necessary future options.

The architecture does not assume that transformation is always desirable. Some transformations preserve one function by eliminating others. Typed judgments and identity continuity evaluate those changes.

### 8.7 Unknown architectures

The registry \(\mathbb A\) is incomplete. An assessment can distinguish:

- no viable path among known architectures;
- evidence that no path exists within a bounded architecture class;
- genuine global impossibility under stated physical or logical constraints;
- indeterminacy caused by unrepresented architectures.

This distinction prevents “no known transformation” from being reported as universal impossibility.

### Box 6A. Proof obligation — hybrid sustainability semantics

> Future formal work must define the admissible sequence of architecture changes, composition of disturbances across modes, translation of obligations and uncertainty through reset maps, and conditions under which a hybrid strategy preserves the complete typed judgment.
'''
text=text.replace('\n---\n\n# Part III. Composition and Embeddedness',add_b+'\n\n---\n\n# Part III. Composition and Embeddedness')

add_c=r'''

### 12.4 Contract slack and confidence

For a quantitative assumption requiring input \(x\ge x_{min}\), contract slack is

\[
s=x-x_{min}.
\]

For an upper-bound assumption \(l\le l_{max}\),

\[
s=l_{max}-l.
\]

A probabilistic contract additionally carries confidence and calibration error. System-level confidence cannot generally be obtained by naïvely multiplying local confidence values because failures may be correlated. The composition proof obligation must specify dependence assumptions or conservative bounds.

### 12.5 Circular contracts

Ecological, economic, social, and governance modules frequently depend on one another. For example, governance assumes provision and legitimacy, provision assumes productive and ecological capacity, ecological capacity assumes bounded extraction, and bounded extraction assumes governance. Circularity is not itself an error; an unsupported circular guarantee is.

A valid circular contract requires a jointly consistent behavior over a common time signature. Candidate mathematical objects include:

- a robust invariant set in the product state space;
- a viability tube;
- a greatest fixed point of a contract-refinement operator, where “fixed point” refers to the contract computation rather than a stationary system state;
- a strategy profile satisfying dynamic compatibility;
- a conservative outer or inner approximation.

The manuscript does not select one universal solution.

### 12.6 Competition among modules

Local assumptions may be individually satisfiable but jointly impossible because modules compete for one stock, sink, budget, workforce, or attention resource. Compatibility therefore requires a shared-resource allocation constraint rather than pairwise matching alone.

For shared input \(r\):

\[
\sum_i r_i\le r_{available}.
\]

For a probabilistic or state-dependent resource, this becomes a robust or chance constraint. Commons nodes are a special case of this general composition problem.

### 12.7 Contract refinement

A contract may be refined by strengthening its guarantee or weakening its assumption without invalidating downstream composition. Refinement provides a way for future research to improve modules without rewriting the whole architecture. Every refinement must preserve modality, units, scale, and horizon or explicitly update dependent contracts.
'''
text=text.replace('\n---\n\n# Part IV. Domain-General Ontology',add_c+'\n\n---\n\n# Part IV. Domain-General Ontology')

add_d=r'''

### 18.7 Information as an enabling capacity

Information is not merely another resource stock. Decision-relevant information has accuracy, timeliness, resolution, accessibility, and legitimacy. Monitoring capacity can fail even when measurements exist if information cannot reach authorized actors or trigger action.

A minimal information interface includes:

\[
\text{observation}
\rightarrow
\text{interpretation}
\rightarrow
\text{communication}
\rightarrow
\text{decision}
\rightarrow
\text{implementation}
\rightarrow
\text{effect}.
\]

Failure at any link increases effective response time or reduces the implementable policy set.

### 18.8 Goodhart and strategic measurement

When an indicator becomes a target, actors may optimize the indicator rather than the protected construct. The indicator registry should therefore include manipulation risk, independent validation, and multiple measures where feasible. A certificate based on a strategically corrupted indicator fails the epistemic projection even if the reported value satisfies its nominal threshold.

### 18.9 Endogenous preferences and institutions

Preferences, norms, technologies, and institutions can evolve. Within-architecture models may treat some as states. Changes that alter the action set, authority, or identity realization may instead trigger architecture transition. The distinction is made by the registered architecture, not by whether a variable is conventionally called “social.”
'''
text=text.replace('\n---\n\n# Part V. Instantiation Sketches',add_d+'\n\n---\n\n# Part V. Instantiation Sketches')

add_e=r'''

### 23.5 Necessary steady-state relations in the sketch

If the coupled model admits a steady state, necessary relations include:

**Resource:**

\[
H^*
\le
r(E^*)R^*
\left(1-\frac{R^*}{K_R(E^*)}\right)
-\phi(P^*)R^*.
\]

**Pollution:**

\[
\epsilon_YY^*
\le
A^*+\lambda_E(E^*)P_{max}.
\]

**Ecological capacity:**

\[
J_E^*
\ge
\delta_EE^*
+\psi_H(H^*,R^*)
+\psi_P(P^*).
\]

**Productive capital:**

\[
J_K^*
\ge
\delta_KK^*
+\chi(P^*,R^*)K^*.
\]

**Governance capacity:**

\[
J_G^*
\ge
\delta_GG^*
+\Phi_G(Q^*/G^*).
\]

**Provision:**

\[
C_g^*\ge C_g^{min}
\qquad\forall g.
\]

These conditions are not sufficient. Stability, disturbance, delay, transition, contract confidence, strategic behavior, and commons allocation remain.

### 23.6 Expanded failure-loop catalogue

**Extraction–capacity spiral**

\[
H\uparrow
\Rightarrow
R,E\downarrow
\Rightarrow
\text{regeneration}\downarrow
\Rightarrow
\text{future extraction effort}\uparrow.
\]

**Pollution–production spiral**

\[
Y\uparrow
\Rightarrow
P\uparrow
\Rightarrow
E,K\downarrow
\Rightarrow
\text{maintenance burden}\uparrow
\Rightarrow
\text{abatement capacity}\downarrow.
\]

**Underinvestment spiral**

\[
\text{present pressure}\uparrow
\Rightarrow
J_E,J_K,J_G\downarrow
\Rightarrow
\text{future capacities}\downarrow
\Rightarrow
\text{future pressure}\uparrow.
\]

**Governance-overload spiral**

\[
Q\uparrow
\Rightarrow
\Phi_G\uparrow
\Rightarrow
G\downarrow
\Rightarrow
\mu\downarrow
\Rightarrow
Q\uparrow.
\]

**False-success trajectory**

Average output and provision rise while ecological capacity, governance margin, or provision to a protected subgroup declines. Typed judgments prevent an aggregate output indicator from certifying this trajectory.

### 23.7 Transformation sketch

Suppose no implementable extraction and investment policy can satisfy resource, provision, and governance constraints in the current architecture. Candidate destination architectures might alter technology, property rules, distribution, monitoring, or production structure. Each destination receives its own state space and contracts. Operator II asks whether the transition preserves higher-order identity, avoids irreversible ecological loss, respects cumulative social harm, and reaches the destination viability kernel.

The sketch intentionally leaves destination dynamics open. Its role is to show where transformation theory attaches.
'''
text=text.replace('\n# Part VI. Assessment Outputs',add_e+'\n\n# Part VI. Assessment Outputs')

add_f=r'''

## 30A. Comparative theory development

The empirical programme should distinguish three possible outcomes for the architectural project.

1. **Specification-language success:** the framework improves transparency and comparability but yields no new explanatory law.
2. **Diagnostic-theory success:** typed capacities, interfaces, and transformation variables improve diagnosis or early warning across cases.
3. **General-theory success:** restricted domain-general propositions survive respecification and receive repeated empirical support.

The first outcome is useful but does not justify the strongest title claim by itself. The second and third would progressively support a general theory.

### 30A.1 Novelty test

Future literature review must compare the proposal with existing viable-sustainability, robust-control, social–ecological, safe-and-just-space, ecological-economics, commons, and contract-based traditions. Novelty may lie in the integrated architecture rather than any single component. It should be claimed only where the combination produces a new formal object, proof obligation, diagnosis, or empirical result.

### 30A.2 Respecification test

For family \(\mathfrak O\) of plausible specifications, compare whether a conclusion is:

- invariant;
- sensitive to one declared normative choice;
- sensitive to boundary or horizon;
- dependent on an uncertain empirical contract;
- reversed by a plausible alternative architecture.

This converts specification relativity from a hidden weakness into an explicit robustness analysis.
'''
text=text.replace('\n## 31. AI-assisted theory development',add_f+'\n\n## 31. AI-assisted theory development')

p.write_text(text)
print(len(text))
