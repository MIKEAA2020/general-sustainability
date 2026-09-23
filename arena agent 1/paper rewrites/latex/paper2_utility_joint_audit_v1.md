# Utility Joint Audit Record and Dispositions (v1)

**Audited object.** The applications posture of the obstruction-calculus
programme, with paper 2 (v48, 19 pp.) as the primary artifact — two
owner-supplied use-case reviews (`uploads/stochastic selector use.txt`):
a stakeholder-reach assessment (grok) and an
operational-versus-architectural assessment with a stakeholder table
(gemini). Adjudicated jointly against the artifacts under the
verify-before-fix discipline.

**Artifact verification at audit opening.** Every object-level citation
of both reviews was probed against the shipped v48 PDF and found
accurate: Theorem 3 (timing), Proposition 7 and Corollary 1 (fibre
criterion), Remark 4 (certainty-equivalence trap), the §6.4 governance
translations, Open Problem 1, and the v48 sentence applying Proposition 7
verbatim to composite indices. The reviews read the programme's papers
correctly; their object-level claims contain no misquotes.

---

## Part I — Evaluation of the two audits

**Convergent and accepted.** (1) The work is foundational, not
operational: no reviewer claims a field-ready tool, and the manuscripts
themselves defer calibration, campaigns, and tooling. (2) The genuine
use identified is architectural and forensic: standard-setting against
composite-index aggregation (fibre criterion), sizing of review
intervals against worst-case exit times (timing certificate),
structural-cause forensics (common-action obstruction), and
sensor-sufficiency certification in safety-critical automation
(gemini's extension). (3) The honest-limitations list (expertise
threshold, dimensionality wall, toy-scale exact instances, no real-data
calibration, no user-facing software) matches the manuscripts' own
delimitations — the papers said all of this first.

**Outdated elements (corrected, not defects).** Both reviews treat the
follow-up tracks as future ("Tracks B–D would have to produce checkable
continuous-to-finite certificates, belief-state software, and applied
calibration before the utility becomes operational"). Two of the three
named prerequisites are now drafted, verified, and pushed: the
continuous-to-finite certificates (companion lineage, exact primal/dual
LP witnesses, solver-certified campaign) and the belief-state value
theory (stochastic selector, fifteen exact check families), alongside
the monitoring-design, policy-lattice, exit-time, uncertainty, regime,
margin, and institutional lineages. The third prerequisite — applied
calibration and user-facing tooling — remains genuinely open and is
recorded as such (Part III, L4/L5).

**Scope corrections applied to the audits' framings.** (i) gemini's
"engineering formula" for inspection intervals is adopted only with its
class scope: the timing certificate is a statement about the declared
hold-until-review class; the stochastic lineage's class declaration
(coincidence at the one-step horizon; difference exactly on the timing
cells) is part of the rule, not a footnote. (ii) grok's "rhetorical
scaffolding" charge is answered rather than accepted: the
sustainability framing is the regulatory use case — the formal value of
the calculus in standard-setting is precisely that its conclusions bind
where intuition does not (adopted as limitation L6 of the new
statement). (iii) gemini's "Zero" entry for field managers is adopted
with the nuance the reviews themselves supply: the rules reach field
practice only after institutional adoption (the stakeholder table says
"none direct; institutional uptake"). (iv) The "epistemic paradox"
(high-fidelity models would not need crude indicators) is adopted as
limitation L1 with the answer the calculus itself supplies: declaring
bounds and margins is the regulatory act, and the margin is priced into
the certificates by the buffered-viability lineage.

---

## Part II — Dispositions

**U1 (both). Utility statement missing as a reader-facing artifact. —
ACCEPTED AND COMPLETED.** New satellite statement
`paper2_applications_note_v1` ("From Obstruction Certificates to
Monitoring Standards: An Applications and Limitations Statement"):
four design rules (R1 review-interval sizing, class-scoped; R2 the
fibre rule with its cost instance; R3 bias correction; R4 forensic
separation), each a restatement of a source theorem at design precision
with scope and verified instance attached; the
operational/architectural split; the stakeholder table; six precise
limitations (L1 model availability, L2 dimensionality, L3 completeness
scope, L4 calibration, L5 software status, L6 formalizing the
intuitive); and an index of the delivered lineages against the utility
prerequisites. No new theorems; every claim a pointer.

**U2 (gemini). Four genuine-use domains. — ADOPTED** as the organizing
structure of the statement's Sections 3–4 (standard-setting, interval
sizing, forensics, sensor-sufficiency with the programme's
policy-lattice and hybrid lineages as instruments).

**U3 (grok). Stakeholder-reach table. — ADOPTED** (statement, Table 1),
with the institutional-uptake nuance.

**U4 (both). "No software, no calibration." — ACCEPTED AS OPEN ITEMS**
(recorded as L4/L5 of the statement; roadmap v12 carries them as
owner-side items). The verification-grade status of the programme's
scripts is stated precisely rather than overstated.

**U5 (both). "Tracks B–D would have to..." — CORRECTED AS OUTDATED;**
the delivered-programme index (statement, Section 6) resolves the
prerequisites against the fifteen shipped lineages, with the remaining
items named.

**U6 (gemini). Timing formula without class scope. — CORRECTED IN THE
ADOPTION;** see Part I (i). The class declaration of the stochastic
lineage is cited inside R1 itself.

**U7 (grok). "Completeness only for finite-state one-step and
static-observation classes." — PARTIALLY CORRECTED;** the finite-horizon
completeness lineage now proves soundness, completeness, and empty
certificate gap for finite systems on finite horizons; the continuous
and dynamic-observation characterizations remain open (L3, Open
Problem 1). The statement records both.

**Pointer integrity.** Every pointer in the statement is
machine-checked: `paper2_applications_note_v1_pointers.py` probes the
shipped artifacts (9 pointer families — the calculus objects, the
selector split and class-scope remark, the design instances, and the
lineage titles); record 9/9, exit 0, shipped alongside the statement.
The statement's own build: Tectonic 0.15.0, zero overfull boxes, three
pages, post-build probes passing (the first build's overflowing
stakeholder table was converted to a spanning float; two broken
`\ref`s to an unnumbered section — the same defect class the previous
audit caught in the stochastic lineage — were caught by the post-build
probes of this round and repaired to literal references before ship).

---

## Part III — Completing actions and remaining items

Completed in this round: the applications-and-limitations statement
(tex + pdf + pointer script + addendum, shipped and mirrored); this
record; roadmap v12. Remaining, owner-side or open (statement L2–L5):
the deferred medium-dimensional numerical campaign; the continuous-class
timing check (Open Problem 1) and the residual dynamic gap; applied
calibration against real schedules and data; user-facing tooling beyond
verification-grade scripts.

**Declarations.** Funding: none. Competing interests: none. The two
utility reviews were supplied by the owner; their adjudication, the
satellite statement, the pointer record, and this document were prepared
with AI assistance under the programme's verification discipline.
