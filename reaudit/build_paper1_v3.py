#!/usr/bin/env python3
"""
Build Paper 1's third edition (journal-facing edition) from manuscript_v2.md.

Transformation contract (no theorem, proof, number, or claim status is changed):
  - Front matter: repositioned abstract (formal vocabulary as this paper's framework,
    not as a description of field practice), keywords line, condensed edition note.
  - Section 1: repositioned motivation; provenance paragraph restated in
    manuscript-relative vocabulary; series declaration condensed (no roadmap).
  - Sections 2-9: body text preserved verbatim except (a) provenance bracket tags
    removed from headings, (b) 'verified present' proof-process markers reworded to
    source-relative forms, (c) 'flagship manuscript' -> 'programme manuscript',
    (d) inline 'row-verified' phrases resolved to Appendix-A pointers.
  - Section 10: restructured as a concrete reproducibility statement (the witness,
    the certification level, the concordance with motivated counts).
  - Section 11: new condensed future-directions section (the conjecture set).
  - Section 12: provenance and limits (reproducibility paragraph moved to section 10).
  - Appendix A: the statement-level inventory in two tables with concrete bases,
    a legend, and the stipulation/formal-validity disclaimer.
  - References: unchanged external entries; the programme-sources paragraph updated.

Run: python3 reaudit/build_paper1_v3.py   (from the repository root)
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "papers/paper1_general_theory/manuscript_v2.md"
DST = REPO / "papers/paper1_general_theory/manuscript_v3.md"

text = SRC.read_text(encoding="utf-8")

# ---------------------------------------------------------------- locate blocks
i_body_start = text.index("## 2 The typed canonical framework")
i_ten = text.index("## 10 The research architecture")
i_refs = text.index("## References")

body = text[i_body_start:i_ten]          # sections 2-9 (verbatim modulo edits)
refs = text[i_refs:]                     # references (modulo programme-sources edit)


def rep(block, old, new, count=1):
    n = block.count(old)
    if n != count:
        sys.exit(f"FATAL: expected {count} occurrence(s) of {old[:70]!r}, found {n}")
    return block.replace(old, new)


# ------------------------------------------------------- body surgical edits
# (a) heading provenance tags -> Appendix A (tag, expected count)
for tag, expected in [
    (" [CC-A002-001 · axiom/definition]", 1),
    (" [CC-A002-003 · axiom/definition]", 1),
    (" [CC-A002-004 · axiom/definition]", 1),
    (" [CC-A002-005 · axiom/definition]", 1),
    (" [CC-A002-006 · axiom/definition]", 1),
    (" [CC-A002-019 · axiom/definition]", 1),
    (" [CC-A002-035 · axiom/definition]", 1),
    (" [programme infrastructure, stated as typed instance of established constructions]", 1),
    (" [MS-Native-7 · definitional taxonomy for assessment practice]", 1),
    (" [manuscript-native · identity]", 1),
    (" [manuscript-native · theorem]", 3),   # sections 4.3, 4.5, 4.6
    (" [manuscript-native · axiom/definition]", 1),
    (" [artifact]", 1),
    (" [CC-A001-077 · axiom/definition, row-verified]", 1),
    (" [CC-A001-081 · theorem (verified present; summary)]", 1),
    (" [CC-A001-069 · theorem (verified present; summary)]", 1),
    (" [CC-A003-006 · definition, row-verified; CC-A006-010 · conditional theorem, row-verified]", 1),
    (" [CC-A001-082 · axiom/definition, row-verified]", 1),
    (" [CC-A001-083 · theorem (verified present; no separate proof — immediate)]", 1),
    (" [CC-A001-084 · theorem (verified present; summary)]", 1),
    (" [CC-A012-009 · theorem (verified present; summary)]", 1),
    (" [CC-A018-009 · theorem (verified present; summary)]", 1),
    (" [CC-A001-056 · example (verified present; status crosswalk recorded)]", 1),
    (" [CC-A002-049 · research programme, row-verified]", 1),
    (" [CC-A016-001, CC-A016-010 · registry entries, row-verified]", 1),
]:
    body = rep(body, tag, "", count=expected)

# (b) section 2 preamble sentence
body = rep(body,
    "The framework of this section is the A002 source's canonical layer [CC-A002-001, CC-A002-003, CC-A002-004, CC-A002-005, CC-A002-006, CC-A002-019, CC-A002-035 — all axiom/definition, row-verified]. Paper 2's atlas restates the same definitions in its preliminaries; the canonical forms are stated once here, and the atlas cross-references this paper as the architecture owner.",
    "The framework of this section is the canonical layer of the programme's source corpus (A002): seven stipulated definitions whose per-statement inventory, with provenance keys, is Appendix A (rows CC-A002-001, -003, -004, -005, -006, -019, -035). Paper 2's atlas restates the same definitions in its preliminaries; the canonical forms are stated once here, and the atlas cross-references this paper as the architecture owner.")

# (c) process markers -> source-relative forms
body = rep(body, "*Proof (verified present; summary):* each instrument is realized",
                  "*Proof (summary of the source's proof):* each instrument is realized")
body = rep(body, "*Mechanism (verified present; summary):* inside the strip",
                  "*Mechanism (summary of the source's proof):* inside the strip")
body = rep(body, "*Proof (verified present; summary):* a viable path would be",
                  "*Proof (summary of the source's proof):* a viable path would be")

# (d) implementability ladder tag
body = rep(body, "**The implementability ladder [MS-Native-5 · axiom/definition].**",
                  "**The implementability ladder.**")

# (e) flagship manuscript -> programme manuscript
assert body.count("flagship manuscript") == 2, body.count("flagship manuscript")
body = body.replace("flagship manuscript", "programme manuscript")

# (f) inline row-verified resolutions
body = rep(body,
    "use has limited or indirect effect on reproduction [CC-A003-006, row-verified]",
    "use has limited or indirect effect on reproduction (Appendix A, CC-A003-006)")
body = rep(body,
    "stated without proof in its source and carried at exactly that status [CC-A006-010, conditional theorem]",
    "stated without proof in its source and carried at exactly that conditional status")
body = rep(body,
    "as normative and unoperationalized research-programme items [both rows row-verified]",
    "as normative and unoperationalized research-programme items (Appendix A, CC-A016-001 and CC-A016-010)")

body = rep(body,
    "without claiming a universal equilibrium theory (programme manuscript §5.3; no concordance row)",
    "without claiming a universal equilibrium theory (programme manuscript §5.3)")

# (g) §4 preamble keeps its artifact pointer; §4.7 heading is plain after tag strip.

# ------------------------------------------------------------------- front
front = """# A Typed Architecture for Sustainability: Claim Statuses, Transformation Operators, and the Separation of Assessment Doctrines

**Paper 1 of the programme's publication architecture (general-sustainability, A001–A025).**

*Third edition (journal-facing edition, 2026-08-29): the external style review's accepted findings are implemented — the abstract and introduction reposition the formal vocabulary as this paper's analytical framework rather than as a description of field practice; the statement-level inventory moves from the body to Appendix A in two-table form with concrete bases and a stipulation/validity legend; the research-architecture section is restructured as a concrete reproducibility statement and a condensed future-directions section; publication roadmaps and internal process vocabulary are removed from the body. No theorem, proof, number, or claim status is changed; the second edition remains the programme-internal record.*

---

## Abstract

Sustainability claims are difficult to compare across domains. Statements about a fish stock, an aquifer, a liability regime, and an intergenerational floor rest on different mathematical structures, require different forms of evidence, and fail in different characteristic ways, yet policy discourse frequently treats them as commensurable. This paper introduces a typed, domain-agnostic architecture that formalizes these differences as explicit state spaces, proof obligations, and failure modes, and makes them auditable: a canonical system schema with declared types; four uncertainty levels with a fixed quantifier discipline; three policy questions; four model maps that license every cross-model claim; diagnostic claim types with a no-transfer rule; a transformation operator for changes of system architecture; constructors for governance instruments; intergenerational viability structures; restricted composition interfaces; and admission standards governing the retention of additional structure. The architecture's central discipline is that every claim carries an explicit status — axiom, identity, theorem, conditional theorem, conjecture, or counterexample — and that negative results are first-class content. The paper's principal mathematical contribution is a separation theorem for assessment doctrines: endpoint-only accounting, scalarized aggregate assessment (the weak-sustainability doctrine: one index, prices on capital forms, compensation across floors), and noncompensatory typed assessment (the strong-sustainability doctrine: each floor separately binding) form a strictly nested hierarchy, and the gap between the aggregate family and the noncompensatory assessment is exactly the failure of "a plan exists for each price vector" to commute to "one plan exists for all price vectors". On an explicit two-architecture datum the gap is a region with interior in which every price vector certifies its own transition and no single transition respects the floors; the typed recursion splits this false-positive set into a fundable rescue set and a certified impossibility region. The separation is machine-witnessed in exact integer arithmetic and propagates through the backward induction. The architecture is operationalized in a source-to-canonical-to-publication concordance of 409 mappings, provided with the verification artifacts to support independent re-execution.

**Keywords:** sustainability assessment; viability theory; weak and strong sustainability; typed systems; claim status; reproducibility

---

## 1 Introduction

### 1.1 The question this paper answers

**What is the typed, domain-agnostic architecture of sustainability, viability, observation, governance, transformation, and composition — and what does that architecture prove about the assessment doctrines used to judge sustainability transitions?**

Two failure modes motivate the question. The first is *commensurability drift*: sustainability assessments aggregate stocks, services, liabilities, and floors into single indices whose compensation principles are rarely stated as explicit mathematics. The second is *status drift*: conceptual frameworks state aspirations as theorems, conditional results circulate as unconditional ones, and negative findings disappear from the literature. The programme whose architecture this paper states was built against both failures, and this paper makes the motivating differences precise rather than assumed: it assigns every object a type, every claim a status, and every cross-model statement a declared map — formalizing as distinct state spaces, proof obligations, and failure modes what assessment practice tends to treat as one currency.

### 1.2 What enters this paper

Paper 1 is the architecture paper of the series. Its retained set consists of the twenty-one concordance rows routed to it by the programme's destination pass (definitions and structures of the canonical framework; the governance constructors; the intergenerational structures; the restricted-composition interfaces; the research-architecture material), plus this paper's own independent result — the assessment-separation theorem with its complete instantiation. The full proof corpus (viability calculus, conservation, noncompensation algebra, sampled kernels, projectability) belongs to Paper 2, the theorem atlas; the ledger, delay-dynamics, and empirical-identification applications belong to Papers 3–5. Where this paper needs an atlas result, it states the canonical form once, cross-references the owning paper, and never transfers a status. Per-statement provenance keys link every concordance-sourced statement to the 409-row inventory; the complete inventory is Appendix A.

### 1.3 Claim-status discipline

Every statement below carries a status label from the programme's hierarchy (the A002 source's own table, adopted programme-wide):

| Status | Admission rule |
|---|---|
| Axiom/definition | Declares an object, domain, type, or convention; asserts no empirical truth |
| Identity | Follows by construction or direct algebra |
| Theorem | Complete proof under explicit mathematical assumptions |
| Conditional theorem | Complete implication whose hypotheses are not established for every intended application |
| Conjecture | Precise unproved statement with a declared proof gap and disproof route |
| Counterexample/limit | An explicit construction establishing that an implication fails |

Two rules govern this article. **No promotion:** a conditional theorem is never stated as a theorem; conditionality is part of the mathematical content. **No silent transfer:** a status proven for one model class does not transfer to extensions, reductions, or applications without a declared map (§2.7) and, where the map crosses modules, the interface contract recorded per row.

### 1.4 Provenance and auditability

Twenty-one of this paper's statements are drawn from the programme's source corpus through the concordance of §10; each was verified against its source in a dated closure campaign (full-source reads with per-statement confirmation of existence, kind, proof presence, module, and mapping type; sources A001, A002, A003, A006, A012, A016, A018 closed 2026-08-27/28), and each is stated below at exactly its source-declared status, with no promotion. Content-level verification of provenance is not a theorem-status promotion, and the cross-module interface contract remains an open obligation recorded per row. The complete statement-level inventory, with the per-statement provenance keys, is Appendix A. This paper's own theorems (§4) are complete here, and their machine witness is a committed deterministic artifact.

### 1.5 Relationship to the companion papers

This paper is the first of a series of companion papers: a theorem collection (the atlas) carrying the proof corpus; three application papers (material ledgers, delay dynamics, and sampled governance with empirical identification); and four scored empirical studies on two resource systems, each reporting its own negative certificates. A monograph reintegrates the material at full length after the papers receive external scrutiny. No paper depends on another for a locally load-bearing definition: each carries a Minimal Working Realization of the canonical objects it needs, and §2 is this paper's. Where a result's full development or named instantiations belong elsewhere, the ownership is declared on the line.

---

"""

# ------------------------------------------------------------------- back
back = """## 10 Reproducibility and data availability

All computational results in this paper are verified by a committed deterministic artifact (`research_program/paper1_instantiation/`): exact integer arithmetic at scale 40 — no floating-point operations, tolerances, or randomness — over a 29,791-state grid with dense critical weight sets including the exact boundary weights and the adversarial midpoint; all 25 checks pass, and re-execution reproduces the outputs exactly. The runner, the JSON results, and the human-readable report are committed alongside the raw novelty-search records. The certification level of this verification is *exact* — the strongest tier available to a finite discrete verification. More generally, computational claims in the programme carry a declared certification level — nominal, re-execution-verified (outputs identical on fresh execution), independently re-executed (a second agent and toolchain), or certified (interval or rigorous arithmetic) — stated per claim and never implied; the present paper makes no computational claim beyond the exact witness above.

The architecture is operationalized in a source-to-canonical-to-publication concordance of 409 mappings, each linking a source proposition to canonical notation, assumptions, evidence status, mapping type, and destination. Of these, 354 have completed statement-level scientific verification across nineteen sources; the remainder are either adjudicated negative-register entries (28) or open rows attached to conditional results (27, exactly the three gated conditional-paper sources). The concordance, its machine layer, and the verification records are provided in the repository. Every valid source proposition in the corpus maps to a paper section, an appendix, a conditional docket, or an explicit negative record — the non-loss rule the concordance checks row by row. One finding of the verification campaign is part of the architecture's claim: machine verification of the concordance (quotes, coverage, vocabulary) is not content verification — the campaign's found-and-repaired defect classes (intake row corruption, keyword false positives, register misalignment) are the evidence.

## 11 Future directions

The architecture generates a set of falsifiable conjectures for future empirical work. None is executed here, and none carries an empirical finding; the full set, with the falsification test designs and candidate leading indicators and their architectural rationales, is provided in the supplementary material. The nine conjectures are: **compositional sustainability** — local typed contracts can establish jointly viable behaviour without monolithic verification, under identifiable compatibility, timing, robustness, and interface conditions; **transformability** — sustained contraction or emptiness of the viability kernel predicts the need for architecture change earlier than output failure; **capacity-leading failure** — declining regenerative, maintenance, or governance capacity predicts typed failure earlier than current output measures; **bottleneck–robustness** — smaller typed bottleneck margin predicts smaller estimated robustness margin after controls, within a preregistered system class and comparable disturbance geometry; **boundary-expansion reversal** — some favourable assessments reverse when imported resources, exported burdens, affected populations, and deferred liabilities enter through adequate boundary interfaces; **distributional dynamics** — unequal provision and burden can alter health, compliance, conflict, and governance enough to change the functional viability kernel; **correlated-disturbance amplification** — independence-assuming models underestimate joint failure where shocks share causes or reinforcing feedback; **maintenance suppression** — diverting maintenance toward present output raises visible performance while reducing future viability and transformability; and **efficiency–scale interaction** — efficiency gains do not reliably reduce total burden where scale and rebound exceed intensity reduction. Each candidate leading indicator's predictive advantage over simpler outcome indicators is an empirical requirement, not a guarantee of definition.

The conjectures are governed by preregistration restrictions: no conjecture is rescued by arbitrary post-hoc state augmentation; each study preregisters system class, specification, candidate indicators, excluded variables, predicted direction, acceptable model revisions, and the observations that count against the conjecture; and the unrestricted claim that every sustainability failure is representable at an "adequate scale and resolution" is excluded as too elastic to falsify. The mechanism-level hypotheses (observation aggregation, governance phase ordering, substitution certificates) and their declared tests belong to the empirical-identification companion paper and are complementary to, not duplications of, the conjectures above.

## 12 Provenance and limits

**Provenance.** Bracketed pointers of the form [A001 §13.6] reference the programme's source corpus — the manuscripts from which the concordance-sourced statements of this paper were verified — committed, together with the concordance itself, to the project repository (<https://github.com/MIKEAA2020/general-sustainability>). The manuscript-native theorems (§4) are complete in this paper; their full development, proofs, and machine witness are the committed files `research_program/paper1_typed_false_positive_theorem.md` and `research_program/paper1_instantiation/` (runner, JSON results, report, raw novelty-search records). Appendix A carries the statement-level inventory. The further manuscript-native entries (§3.4, §6.1, §11) restate programme-manuscript content at its declared statuses — the implementability ladder (programme manuscript §5.3), the typed failure taxonomy (programme manuscript §24.1; module-family origin A007 §6), and the architecture-level empirical conjectures, falsification tests, and leading indicators with their preregistration restrictions (programme manuscript §§27–29) — each restating its source at exactly the declared status.

**Limits.** (i) The assessment-separation theorem is an existence result with interior, not a claim that the gap is always large; on dominated-action data the assessments coincide. (ii) Its novelty verdicts at no-match-found are bounded-search absences, conditioned per §5.2; if external review overturns a verdict, the fallback destination is the monograph's series introduction — the programme's standing fallback rule, not a demotion. (iii) All concordance rows behind this paper (Appendix A) are content-verified against their sources; no statement depends on a pending verification. (iv) The architecture covers no infinite horizons, no partial observation, no stochastic chance constraints, and no endogenous event times at the transformation-operator level; each exclusion is recorded in the theorem files and inherited here. (v) The empirical layers of the programme (Papers 3–5) own every data-bearing claim; this paper asserts nothing empirical — the conjecture set, falsification tests, and leading indicators of §11 are declared at non-executed conjecture and design status and carry no empirical finding.

---

## Appendix A. Statement inventory and verification summary

This appendix inventories the formal statements of the paper in two tables. The **identifier** column carries the programme's concordance row codes (`CC-A0dd-ddd`) or manuscript-native keys (`MS-Native-n`, `Infra-1`); the codes key each statement to the source-to-canonical inventory committed in the repository and are provenance keys, not citations. Every concordance-sourced entry was verified against its source manuscript in the closure campaign of 2026-08-27/28 (full-source reads with per-statement confirmation of existence, kind, proof presence, module, and mapping type); this is content-level verification of provenance, not a promotion of any entry's mathematical status.

**Legend and disclaimer.** Entries categorized as *Definition*, *Axiom*, *Scope*, *Registry*, *Programme*, or *Registration* are stipulated or declared — they carry no empirical truth-value and need no proof. Entries categorized as *Theorem*, *Lemma*, *Identity*, or *Example* are established under the assumptions stated where they appear (proved in this paper, or summarized from the identified source's proof). Entries categorized as *Conditional theorem* retain their hypotheses as mathematical content. The formal validity of any entry within the declared framework does not by itself imply applicability to an empirical system (§12, Limits). No status is promoted anywhere in this inventory; the manuscript-native results MS-Native-1–4 are this paper's own, with artifact provenance, and MS-Native-5–8 restate programme-manuscript content that carries no concordance row, each at exactly its declared status.

**Table A1. Stipulated definitions, axioms, scope restrictions, and declared programme entries.**

| Identifier | Statement | Category | Basis |
|---|---|---|---|
| CC-A002-001 | Type system and physical state (§2.1) | Definition | Stipulated; restated from source A002 |
| CC-A002-003 | Canonical system, thirteen-slot tuple (§2.2) | Definition | Stipulated; source A002 |
| CC-A002-004 | Four uncertainty levels with fixed quantifier discipline (§2.3) | Definition | Stipulated; source A002 |
| CC-A002-005 | Diagnostic types and the no-transfer rule (§2.4) | Definition | Stipulated; source A002 |
| CC-A002-006 | Threshold and intergenerational types (§2.5) | Definition | Stipulated; source A002 |
| CC-A002-019 | Three policy questions (§2.6) | Definition | Stipulated; source A002 |
| CC-A002-035 | Four model maps (§2.7) | Definition | Stipulated; source A002 |
| CC-A001-077 | Governance constructors (§6.1) | Definition | Stipulated; source A001 §13.6 |
| CC-A001-082 | Generation structure (§7.1) | Definition | Stipulated; source A001 |
| CC-A003-006 | Weak viability coupling scope restriction (§6.4) | Definition (scope) | Stipulated; source A003 |
| CC-A016-001 | Typed registry with tagged normative premises (§9.3) | Registry entry | Source A016 |
| CC-A002-049 | Exergy and quality-grades transformation programme (§8.4) | Declared programme | Source A002 |
| CC-A016-010 | Proposed floors, normative and unoperationalized (§9.3) | Declared programme | Source A016 |
| MS-Native-5 | Implementability ladder, `U_impl ⊆ U_inst ⊆ U_tech ⊆ U_theor`, with the parallel policy-class ladder; within-architecture viability quantifies over the implementable class (§6.1) | Definition | Programme manuscript §5.3 (repository) |
| MS-Native-7 | Typed failure taxonomy, ten classes, with the earliest-discharged-obstruction rule (§3.4) | Definitional taxonomy | Programme manuscript §24.1; module-family origin A007 §6 |
| MS-Native-8 | Conditional stage-structured and spatial extensions paper, registered with conditional prerequisites | Registration (conditional) | Programme conditional-allocation design; A022/A023 conditional docket |
| MS-Native-6 | Nine empirical conjectures, eight falsification test designs, ten candidate leading indicators, with preregistration restrictions (§11) | Declared conjectures and test designs — not executed | Programme manuscript §§27–29 |

**Table A2. Theorems, lemmas, identities, and examples.**

| Identifier | Statement | Category | Basis |
|---|---|---|---|
| MS-Native-1 | Lemma 4.2, closed-cone pointwise equivalence (§4.2) | Identity | Proved here (two lines) |
| MS-Native-2 | Theorem A, assessment hierarchy and quantifier noncommutativity (§4.3) | Theorem | Proved here; machine-witnessed |
| MS-Native-3 | Theorem B, false positives, blindness levels, disagreement, rescue, impossibility (§4.5) | Theorem | Proved here; machine-witnessed |
| MS-Native-4 | Theorem C, propagation through backward induction (§4.6) | Theorem | Proved here; machine-witnessed |
| Infra-1 | Finite-architecture robust transformation recursion (§3.3) | Theorem — typed instance of established constructions | Proved in the programme's theorem file (repository) |
| CC-A001-069 | Finite-time commons obstruction, uniform strip-margin form (§6.3) | Theorem | Proof in source A001 §12.3; summarized in §6.3 |
| CC-A001-081 | Management vocabularies are constructor rewrites (§6.2) | Theorem | Proof in source A001; summarized in §6.2 |
| CC-A001-083 | Stationary-generation equivalence (§7.2) | Theorem (immediate) | Immediate equivalence; §7.2 |
| CC-A001-084 | Nested-impossibility theorem (§7.3) | Theorem | Proof in source A001; summarized in §7.3 |
| CC-A006-010 | Conditional compositional safety across coupled subsystems (§6.4) | Conditional theorem | Stated without proof in source A006; carried at that status |
| CC-A012-009 | Effort-scale invariance (§8.1) | Theorem | Proof in source A012; §8.1 |
| CC-A018-009 | Yield-gap soft-minimum and quantified decoupling (§8.2) | Theorem | Proof in source A018; §8.2 |
| CC-A001-056 | Coupling creates viability, two-factor example (§8.3) | Example | Constructed in source A001; §8.3 |

---

"""

# ------------------------------------------------- references programme note
refs = rep(refs,
    "Programme sources. The programme-internal provenance documents named in §12 — the full development and proofs of the manuscript-native theorems of §4 (`research_program/paper1_typed_false_positive_theorem.md`) and their machine witness (`research_program/paper1_instantiation/`: runner, JSON results, report, and raw novelty-search records) — are committed to the project repository at <https://github.com/MIKEAA2020/general-sustainability>.",
    "Programme sources. The programme-internal documents named in this paper — the source corpus (A001–A025) and the 409-row concordance (§10); the full development and proofs of the manuscript-native theorems of §4 (`research_program/paper1_typed_false_positive_theorem.md`); and their machine witness (`research_program/paper1_instantiation/`: runner, JSON results, report, and raw novelty-search records) — are committed to the project repository at <https://github.com/MIKEAA2020/general-sustainability>.")

out = front + body + back + refs
DST.write_text(out, encoding="utf-8")
print(f"wrote {DST} ({len(out)} chars; source {len(text)} chars)")
