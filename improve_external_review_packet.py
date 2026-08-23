from pathlib import Path
p=Path('research_program/external_review_packet.md')
s=p.read_text()

purpose_marker='''Please treat this packet as self-contained. Do not assume that an internal classification is correct merely because it is stated here.
'''
insert=purpose_marker+r'''

### Scope of self-containedness

This packet is self-contained for the listed correction, architecture, priority, and publication questions: it defines the official objects, reproduces the disputed mathematical forms, states the diagnosed defect, and supplies the source status needed for advice. It is **not** a substitute for a line-by-line audit of every source proof. If a requested verdict requires omitted hypotheses or proof text, mark the issue `INSUFFICIENT INFORMATION`, name the exact missing item, and give only a conditional recommendation. Do not invent missing source content.

### Independent-review rule

Treat every internal diagnosis, “verified” label, source hierarchy, and publication recommendation as contestable. In particular:

- independently check whether the diagnosed error is real;
- distinguish a false theorem from an incomplete proof, notation defect, model-admissibility failure, empirical gap, or merely conservative assumption;
- do not infer truth from reviewer agreement;
- do not downgrade a result solely because code or data are absent when the packet states that verification has been attested; instead distinguish truth status from reproducibility status;
- preserve source-stated distinctions among theorem, numerical result, inferred numerical classification, and conjecture.

### Evidence discipline

For each mathematical correction:

1. state the exact quantifier order;
2. define all sets and maps and their domains/codomains;
3. state regularity, compactness, convexity, measurability, information, and horizon assumptions;
4. indicate whether the conclusion is weak viability, strong invariance, robust/discriminating viability, or stochastic/chance safety;
5. provide a proof sketch sufficient to expose the decisive step;
6. provide a minimal counterexample when an assumption is removed;
7. identify whether the correction changes downstream results.

For literature, give precise references—preferably DOI, theorem number, or book chapter. If uncertain, say so rather than fabricating a citation.
'''
s=s.replace(purpose_marker,insert)

# Add publication criterion after standing constraints section before architecture.
marker='''### Typed failure semantics

Physical impossibility, functional nonviability, normative inadmissibility, relational externalization, and epistemic non-implementability are not the same failure.
'''
insert=marker+r'''

### Publication-merit criterion

Recommend a separate paper only if the material has at least one of:

- an independent research question and conclusion;
- a substantial independent theorem/proof architecture;
- a distinct specialist audience or incompatible evidentiary method;
- a complete independent empirical/computational study;
- length or technical detail that cannot be responsibly handled by the flagship plus appendices/supplement.

Otherwise recommend integration or a supplement. State explicitly which legitimate content goes where.
'''
s=s.replace(marker,insert)

# Add formal conventions after composition paragraph.
marker='''Subsystems use typed deterministic, robust, probabilistic, strategic, or scenario contracts. The general compositional theorem remains open, though restricted sufficient theorems and counterexamples exist.
'''
insert=marker+r'''

### Formal conventions used in this packet

- State spaces are metric spaces unless a stronger structure is stated.
- Constraint/safe sets are closed when viability or tangency results require closedness.
- \(T_K(x)\) denotes the contingent/Bouligand tangent cone.
- An instantaneous action correspondence is \(U(x)\); a causal policy belongs to \(\mathbb P\) and maps available histories to actions.
- Disturbance signals or nonanticipating strategies belong to \(\Delta\).
- “Robust invariance” means one causal policy keeps every admissible disturbance realization in the set; it is stronger than existence of one viable trajectory of a set-valued inclusion unless strong-invariance hypotheses are supplied.
- Information states may be sets/beliefs in a hyperspace. Literal inclusion between kernels under different information structures requires a common physical projection or a declared order/map.
- A capture basin is indexed by target, envelope, horizon, policy class, and disturbance class.
- Numerical verification and publication reproducibility are tracked separately.
'''
s=s.replace(marker,insert)

# Add source table before source hierarchy bullets.
marker='''## 4. Current source hierarchy
'''
insert=r'''## 4. Current source hierarchy

### Source scale and current role

| Source | Approx. words | Current role |
|---|---:|---|
| Master manuscript | 14,000 | Candidate architectural flagship spine |
| Article 001 | 23,174 | Broad mathematical viability/economic/coupling/institutional corpus |
| Article 002 | 23,977 | Typed architecture and restricted constructive theorem corpus |
| Article 003 | 1,286 | Institutional-feedback framing/conjecture note |
| Article 004 | 1,150 | Phosphorus domain-module template |
| Article 005 | 1,205 | Groundwater domain-module template |
| Article 006 | 2,290 | Institutional information-state formulation; flawed fixed point |
| Article 007 | 1,734 | Early hybrid architecture; taxonomy/admission standard |
| Article 008 | 3,227 | Rejected institutional scalar index; redesign only |
| Article 009 | 963 | Rejected distributive formulation; redesign only |
| Article 010 | 6,701 | Perspective and ten-state negative model audit |
| Article 011 V2 | 5,294 | Sampled governance, retrospective evidence, prospective identification/MSE |
| Article 012 | 7,482 | Registered analytical/numerical delay-dynamics paper |
| Article 013 | 4,909 | Verified componentwise accounting and applications |
'''
s=s.replace(marker,insert)

# Add priority decision criteria before error docket.
marker='''# 6. Live mathematical error docket
'''
insert=r'''# 6. Live mathematical error docket

### Required issue-status vocabulary

Use exactly one primary verdict for each item:

- `FALSE_AS_STATED`
- `PROOF_INCOMPLETE`
- `TYPE_OR_DOMAIN_ERROR`
- `MODEL_INCOMPLETE`
- `NOT_AN_ERROR_BUT_NEEDS_CLARIFICATION`
- `DIAGNOSIS_MISTAKEN`
- `INSUFFICIENT_INFORMATION`

Then state whether the source should be corrected, restricted, demoted, superseded, or left unchanged.
'''
s=s.replace(marker,insert)

# Add appendices before requested response format.
marker='''# 8. Requested response format
'''
appendix=r'''# 8. Canonical decision questions that must be answered explicitly

## 8.1 Viability hierarchy

Recommend one notation for the following distinct objects:

1. controlled existential viability;
2. robust/discriminating viability under \(\exists\pi\forall\delta\);
3. epistemic viability on belief/information states;
4. institutional viability under authority and implementation correspondences;
5. finite-horizon chance viability;
6. capture/recoverability;
7. institution-specific safety under a fixed policy.

State which inclusions are literal and which require projection or aligned classes.

## 8.2 Fixed-point construction

For an information predecessor \(Pre\), compare rigorously:

\[
\Phi_1(Q)=S_{safe}\cap Pre(Q)
\]

and

\[
\Phi_2(Q)=Q\cap Pre(Q).
\]

State:

- which operator computes the greatest robust invariant information family;
- the correct initial iterate;
- whether the target is a fixed point or greatest post-fixed point;
- conditions for countable descent;
- when transfinite iteration is needed;
- how policy selection is preserved in the limit.

## 8.3 Transformation theorem target

Propose the smallest nontrivial class for which a theorem can be proved. An acceptable answer should define architecture-indexed spaces, transitions, safe sets, reset maps, policies, disturbances, and identity/obligation translation. Avoid merely restating reach–avoid definitions.

## 8.4 Composition theorem target

Propose one restricted theorem with checkable conditions and a conclusion not already assumed. Candidate classes include monotone systems, linear systems with invariant polytopes, barrier-certified modules with bounded interface gains, or sampled finite-state contracts.

## 8.5 Empirical anchor

Choose groundwater or phosphorus as the first complete domain test. Give a reason based on falsifiability, available measurements, model-identification feasibility, and ability to exercise multiple architectural layers.

---

# 9. Requested response format
'''
s=s.replace(marker,appendix)

# Adjust final section numbering internal references not critical.
p.write_text(s)
print('chars',len(s),'words',len(s.split()))
