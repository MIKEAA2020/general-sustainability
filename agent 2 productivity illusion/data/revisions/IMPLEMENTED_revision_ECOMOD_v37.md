# IMPLEMENTED REVISION — ECOMOD v37 (editorial alignment round)

**Task 123 / owner directive (2026-09-26).** Executes the Task-117 audit
(`ECOMOD_ALIGNMENT_AUDIT.md`) flags and cross-strengthening anchors as one
batched editorial round on `manuscript_ECOMOD_v36.tex` →
`manuscript_ECOMOD_v37.tex`. No mathematical content is touched; the
bibliography is unchanged (2026a/b/c already present and DOI-resolved).
Builder: `make_v37_ecomod.py` (11 anchored exact-match operations, each
asserted to occur exactly once; math environments and theorem-env counts
verified unchanged; +17/−11 lines).

## The operations

1. **Author block (flag 4):** `Amin Abaee^1 / ^1 Independent Researcher,
   Tehran, Iran` — matching P4 v41 and the live JIE v3 precedent; header
   comment and date updated; a v37 provenance note added.
2. **Doctrine borrowing (the ~25-word echo):** the strong-sustainability
   definition is now an exact, quotation-marked quotation of the ledger
   study's sentence — with the dropped word "either" restored, so the
   quotation is verbatim — introduced by "in the ledger study's words"
   and attributed (Abaee, 2026c).
3. **Sub-threshold phrasings:** "are returned to use in time and are
   therefore not waste" and "waste is a relational status, not an
   intrinsic property of any material" paraphrased ("come back into
   service soon enough not to count as waste"; "waste is relational ---
   a status of the use it enters, not an intrinsic property of the
   material"), breaking both near-verbatim echoes.
4. **Elevator image (flag, shared image):** attributed at first use —
   "in the ledger study's own image (Abaee, 2026c)".
5. **Productivity-illusion gloss (flag 1):** line 71's parenthetical now
   states the ledger study's actual definition (the appearance of
   adequate delivery while the base that sustains it is being reduced),
   with technological outperformance named as one channel — not the
   definition.
6. **Mobilising/protective taxonomy (flag 2):** inline citation
   (Abaee, 2026a) at the stabilising-signature bullet.
7. **Exact-tube semantics (flag 3):** attributed to the assessment
   companion's vocabulary (Abaee, 2026b) at consequence (b).
8. **Lemma A anchor (cross-strengthening 1):** "the linear,
   perfectly-substitutable member of the assessment companion's
   aggregator family, its attained weak extreme (Lemma A of Abaee,
   2026b)" — making "B is the weak-sustainability index" literal.
9. **Theorem S2(ii) anchor (cross-strengthening 2):** the structural
   mask claim now carries its family-level theorem — "no
   positive-elasticity aggregator is uniformly safe, and the only
   uniformly safe aggregator is the typed, non-compensating one
   (Theorem S2(ii) of Abaee, 2026b)".

## Verification

- **Engine note:** the sandbox lacks LuaLaTeX; the build battery used
  tectonic (XeTeX engine) with the Latin Modern Math OpenType font
  fetched into the user font directory. v36 compiles identically under
  this battery (31 pp, the same four pre-existing box warnings), so v37
  is checked against a like-for-like baseline. The shipped
  `manuscript_ECOMOD_v37.pdf` is the tectonic build; a canonical
  LuaLaTeX rebuild by the owner's pipeline will paginate identically
  (31 pp) up to engine-level line breaking.
- **Compile:** v37 exit 0, 31 pages (unchanged from v36), box profile
  identical (the same four warnings: overfull 23.31815pt at the title
  block, underfull 6284 and 1215, overfull 26.67603pt; line numbers
  shifted by the insertions only). Zero new boxes.
- **Text layer:** all nine new markers render (Tehran affiliation; both
  anchors with their theorem names; the taxonomy and exact-tube
  citations; the elevator attribution; the precise gloss; the restored
  "either" inside the quotation; the paraphrased waste phrasings).
- **Duplication scan (10/15-gram, comments stripped, LaTeX normalized)
  vs the ledger paper (P3 v32):** all shared 15-gram windows now sit
  inside the quotation-marked, attributed exact quotation; the two
  unmarked sub-threshold echoes are gone. Clean against P1/P2/P4/P5 as
  before.
- **Anchors verified at source:** Lemma A ("the handshake") and
  Theorem S2 ("the two-sided Leontief statement") confirmed present
  with stable statements in the assessment companion's current edition
  (v62) before the citations were written.

## Standing items (unchanged, owner-side)

The Zenodo deposit-title network refresh (2026a's current title vs the
old deposit title; 2026c's deposit title vs the live JIE v3 retitle;
ECOMOD's own deposit 22554480 joining the citable network) remains an
owner action; the optional P2/P5 soft pointers (controller
observability; robust-viability caveat) were not in the approved scope
and remain recorded in the audit's §4.
