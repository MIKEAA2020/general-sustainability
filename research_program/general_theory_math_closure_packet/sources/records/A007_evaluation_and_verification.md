# Article 007 Evaluation and Verification

## Bibliographic identity

**Source file:** `uploads/Paper_I_Hybrid_Sustainability_Architecture_V4.txt`  
**Title:** *A Hybrid Sustainability-Systems Architecture: Material Accounting, Information, Institutions, and Governability*  
**Format:** LaTeX article source  
**Length:** approximately 1,734 words, 170 lines  
**Formal content:** four definitions, two lemmas, one remark, material flow/jump architecture, nested safety objects, module-admission standard  
**Evaluation status:** evaluated; integration not yet executed

## Executive assessment

The article is a concise and valuable architectural statement. Its strongest original features are:

- material, functional, information, authority, and implementation separation;
- boundary-relative hybrid accounting;
- the prescription/implementation distinction;
- nested safety objects;
- a detailed failure taxonomy;
- module-admission requirements;
- explicit refusal to infer local safety from aggregate stocks or outputs.

Two critical state-space inconsistencies prevent direct mathematical use.

First, the article defines

\[
X=(r,f,h)
\]

and then calls

\[
\phi_t=X_t\in C([ -\tau_{\max},0],\mathcal X)
\]

the physical history, even though \(h\) is an institutional mode that may be discrete and jump at events. A continuous-history phase space cannot contain a path with discrete jumps without an explicit hybrid/piecewise-history construction.

Second, the decision state is later defined as

\[
Z_t=(B_t,h_t),
\]

while \(B_t\) already contains histories of \(X=(r,f,h)\). The institutional state is therefore duplicated unless \(B_t\) is redefined to exclude known \(h_t\) or to include uncertainty about it without adding a separate copy.

These points are central, not cosmetic. They should be corrected by separating physical/functional history from institutional mode or by declaring a proper hybrid phase space and reset semantics.

The article overlaps the current master manuscript, Article 002’s richer canonical architecture, and Article 006’s institutional information state. It does not presently merit a separate paper. Its valid distinctive content should be integrated, especially the failure taxonomy and module-admission standard, while overlapping architecture is marked superseded-but-preserved.

---

## 1. State and phase-space architecture

### 1.1 Current inconsistency

The article defines

\[
X=(r,f,h)
\in
\mathbb R_+^{n_r}\times\mathcal F\times\mathcal H,
\]

where \(h\) may be discrete, and then assumes

\[
X_t\in C([ -\tau_{\max},0],\mathcal X).
\]

If \(h\) jumps, the full history is not continuous. At an event, changing only the current value of \(h\) while retaining the old tail also does not produce a continuous history.

### 1.2 Recommended repair

Use either:

#### Separated mode architecture

\[
x=(r,f),
\qquad
x_t\in C([ -\tau_{\max},0],\mathcal X_{pf}),
\qquad
h\in\mathcal H
\]

with hybrid state

\[
\zeta=(x_t,h).
\]

This is the cleanest choice when \(h\) is a current institutional mode.

#### Piecewise-history architecture

Use a declared càdlàg or piecewise-continuous history space with jump markers and a reset operator defined on the complete phase state. This requires new compactness, delayed-evaluation, and solution-map results.

Article 002 already treats the restricted review-synchronised phase-reset case and warns that a point reset with an unchanged delay tail generally leaves the continuous-history phase space.

### 1.3 Decision-state duplication

If \(B_t\subseteq\mathscr H\times\Theta\) contains histories including \(h\), then \(Z_t=(B_t,h_t)\) duplicates institutional state. Choose one of:

- \(B_t\) contains only compatible physical/functional histories and parameters, while current \(h_t\) is known and separate;
- the information state is one belief over both physical and institutional histories, with no separate \(h_t\);
- \(B_t\) contains uncertainty over physical state conditional on observed \(h_t\).

The first option matches Article 006’s intended \((B,h)\) structure after correcting its domain.

---

## 2. Flow and event architecture

The continuous equations

\[
\dot r
=
\mathsf S\nu(\phi_t,u,\omega,\vartheta)+b(\phi_t,u,\omega,t),
\]

\[
\dot f
=G(\phi_t,u,\omega,\vartheta)
\]

are valid templates when the phase space and regularity assumptions are supplied.

The requirement that every module declare schedule, dwell-time/event rule, reset convention, priority, and hold/interpolation rule is strong and should be preserved.

### Required additions

- Define whether event times are exogenous, guard-triggered, or controlled.
- State local finiteness or non-Zeno conditions.
- Define a full phase-state reset for delayed modes.
- Distinguish physical jumps, functional resets, and institutional mode changes.
- State post-reset admissibility and solution continuation.

---

## 3. Material balance

The hybrid identity

\[
\mathsf L^\top r(t)-\mathsf L^\top r(0)
=
\int_0^t\mathsf L^\top b\,ds
+
\sum_{t_k\le t}
\mathsf L^\top[r(t_k^+)-r(t_k^-)]
\]

is correct under absolute continuity between locally finite events and \(\mathsf L^\top\mathsf S=0\).

### Classification correction

The article says a nonzero jump summand may be a “measurement/reclassification event.” A measurement should not physically change \(r\). A coordinate reclassification can alter components while preserving the moiety total. Therefore:

- an internal physical reclassification should have zero moiety summand;
- a boundary impulse may have a nonzero summand;
- a bookkeeping correction or model discrepancy must be labeled epistemic and not interpreted as physical material creation or loss.

Donor-limited flow and reset positivity conditions are appropriate. The limiter’s units, range, and constitutive meaning should be specified in each module.

---

## 4. Safety, services, allocation, and normative constraints

The state-safe set, state–action service relation, and noncompensatory margin vector are conceptually sound.

The two static lemmas are correct:

1. for positive weights and unrestricted margins, positive weighted aggregate does not imply componentwise nonnegativity;
2. if safe and unsafe states share one instantaneous observation, no deterministic memoryless classifier can classify both correctly.

The second lemma is properly limited to static instantaneous aliasing and does not establish dynamic unobservability.

### Distributional placement

Distributional and procedural requirements should not be placed only in the institutional authority set. Some constrain:

- admissible prescriptions and procedures;
- implemented allocations;
- trajectory outcomes and burdens.

The typed registry should record each at the appropriate layer.

---

## 5. Observation, belief, authority, and implementation

The distinction

\[
a_t\in\Gamma(B_t,h_t),
\qquad
u_t\in\mathcal E(B_t,h_t,a_t)
\]

is strong and aligns with the corrected action/policy architecture.

The lower-game quantifier order is correct. The same causal prescription rule must succeed across every compatible implementation, disturbance, parameter, and observation branch unless information arrives before action.

### Required specification

- observation and error spaces;
- compatible-set update;
- policy class and measurability/selection requirements;
- whether \(h_t\) is observed;
- implementation correspondence dependence on latent state;
- event order and inter-sample safety.

---

## 6. Nested safety objects and failure taxonomy

The nested-object design is useful:

- material feasibility;
- full-information robust viability;
- epistemic-institutional viability;
- safety under one specified institution.

The caveat that inclusions require aligned information, authority, implementation, and uncertainty classes is essential.

The failure taxonomy is especially valuable and should be integrated substantially as written:

1. material inconsistency;
2. physical infeasibility;
3. epistemic/common-action infeasibility;
4. authority infeasibility;
5. implementation infeasibility;
6. temporal infeasibility;
7. recovery failure;
8. model-credibility failure;
9. normative incompatibility.

### Additional type

Architecture-transition infeasibility should be added: no admissible within-architecture recovery or cross-architecture meta-policy is available under the frozen specification and registered architecture class.

The taxonomy should map directly to the master system-level assessment map and typed verdict vector.

---

## 7. Modularity, information, recovery, and substitution

The compositional warning is correct: separate local certificates do not imply global safety without interface routing, shared-control compatibility, and nonblocking event composition.

The information-refinement statement is appropriately left conditional until belief dynamics and strategy spaces are specified. Articles 001–002 provide theorem versions.

The recovery template correctly requires return of the joint information/institution state, not only the physical state.

The substitution statement is strong and should be retained: substitutes require material, energy, delay, waste/displacement, authority, and implementation pathways. This maps directly to Article 002’s Farkas pathway theorem and Article 001’s CES thresholds.

The spatial-scope warning is also correct. Aggregate stability does not imply local safety when gradients, habitat configuration, trade, catchment routing, exposure, or independent-unit fragility matter.

---

## 8. Admission standard

The module-admission list is one of the article’s most reusable contributions. A domain module must supply:

- boundary and units;
- material and jump ledger;
- functional/service maps;
- state and state–action constraints;
- observation/proxy/error model;
- authority and implementation correspondences;
- uncertainty and discrepancy semantics;
- event model;
- identifiability plan;
- numerical verification;
- out-of-sample or prospective validation.

This should become a master domain-module admission template and should govern Articles 003–005.

---

## 9. Relationship to other programme sources

### Article 001

Provides fuller robust/epistemic viability, recovery, common-action, observer, institutional, composition, and resource results.

### Article 002

Provides a richer canonical tuple, type system, hybrid conservation/positivity, sampled/hybrid/RFDE information kernels, projectability, diagnostics, and status hierarchy.

### Article 006

Uses the joint information/institution state \((B,h)\) and develops the conditional predecessor theorem. Article 007 supplies the surrounding architecture but contains the phase-space duplication that must be corrected.

### Articles 003–005

These domain and mechanism modules can be tested against Article 007’s admission standard after correction.

### Master manuscript

Already contains a broader frozen specification, typed verdict, architecture transformation, boundary interfaces, commons nodes, and assessment map. Article 007 should not replace that spine; it should contribute its institutional formulation, failure taxonomy, and admission standard.

---

## 10. Publication assessment

Article 007 does not currently merit a separate paper because:

- its architecture overlaps the master and Article 002;
- its mathematical companion Article 006 overlaps stronger Articles 001–002;
- the physical/institutional phase-state definition is inconsistent;
- its unique content can be integrated without loss.

Recommended treatment:

- integrate the failure taxonomy and module-admission standard into the flagship;
- integrate the corrected \((x_t,h)\) and \((B,h)\) architecture where useful;
- mark duplicate architecture definitions superseded-but-preserved;
- use Articles 001–002 as canonical theorem sources;
- do not maintain a separate Paper I/Paper II pair unless later evidence reveals an independent contribution not already covered.

---

## 11. Verification verdict

### Verified or conceptually sound

- boundary-relative material accounting;
- material/functional/institutional distinction;
- donor and reset positivity requirements;
- noncompensatory safety vector;
- prescription/implementation distinction;
- lower-game quantifier convention;
- nested safety concepts with alignment caveat;
- static compensation and aliasing lemmas;
- failure taxonomy;
- substitution and spatial-scope requirements;
- module-admission standard.

### Critical correction required

- continuous history containing a discrete jumping institutional mode;
- duplication of \(h\) in both physical-history belief and decision state.

### Additional correction required

- delayed phase-state reset and non-Zeno semantics;
- classification of measurement/reclassification jumps;
- distributional constraints at procedure, action, and outcome layers;
- information-state update and policy classes;
- architecture-transition failure category;
- literature/provenance and canonical source selection.

### Not established by this source

- a general output-feedback safety theorem;
- a nonempty kernel for any domain system;
- a calibrated observation or implementation model;
- a composition theorem;
- a transformation theorem;
- any empirical domain result.

Article 007 should remain on integration hold until the phase-space architecture is corrected and its unique material is separated from duplicated content.
