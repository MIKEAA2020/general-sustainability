# paper2_applications_note_v1 — addendum

**Lineage:** `paper2_applications_note_v1` — a satellite statement of the
paper-2 programme (not a new theory paper; no theorems created; every
claim a machine-checked pointer). Produced by the utility joint audit
(two owner-supplied use-case reviews, adjudicated jointly; dispositions
in `paper2_utility_joint_audit_v1.md`).

**Content.** "From Obstruction Certificates to Monitoring Standards: An
Applications and Limitations Statement for the Obstruction Calculus"
(3 pp.): four design rules restated at design precision with scope and
verified instances (R1 review-interval sizing — class-scoped per the
stochastic lineage's class declaration; R2 the fibre rule with the
two-cell coarsest-monitoring instance; R3 bias correction with the
21/100 drift bound; R4 structural-cause forensics with the audited
belief and the sixteen-pair deadlock boundary); the operational vs
architectural distinction; the stakeholder table; six precise
limitations (model availability with the bounding-is-the-regulatory-act
answer; the dimensionality wall with the exact worst-case laws and the
bridge's LP route; completeness scope with Open Problem 1; calibration;
software at verification grade; formalizing the intuitive); the
delivered-programme index against the utility prerequisites; and the
remaining open items.

**Verification.** `paper2_applications_note_v1_pointers.py` — nine
pointer families probing the shipped artifacts for every quoted object
(theorems, instances, lineage titles); 9/9 verified in the shipped
configuration; stated dependency pymupdf (PDF extraction); exit 0.
Note build: Tectonic 0.15.0, zero overfull boxes, 3 pages; post-build
probes pass.

**Defects found and repaired before ship.** (1) The first build's
stakeholder table overflowed the column twice (63.8pt, then 20.2pt after
the paragraph-column fix measured against the wrong width); converted to
a two-column-spanning float — final build zero overfull. (2) Two broken
`\ref`s to an unnumbered subsection (the same defect class the previous
audit caught in the stochastic lineage) were caught by this round's
post-build probes and repaired to literal "Section 7" before ship —
verify-before-fix working as designed on our own draft.

**Status.** Shipped to `latex/` (tex + pdf + pointers + this addendum)
via cp + cmp; source zip
`zips_archive/paper2_obstruction_calculus/paper2_applications_note_v1_source.zip`
(4 entries); pushed with the utility joint audit record and roadmap v12.
