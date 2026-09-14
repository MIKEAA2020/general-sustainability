# v37 — final alignment: hypothesis labels + supplementary proof order

Third re-verification round found two residual restructuring defects (now fixed).

## 1. Hypothesis labels tracked the old subsection numbers

The labels (H1.x), (H3.x), (H4.x) encode the subsection in which each theorem
sat (H1 = Section 3.1 exit, H3 = Section 3.3 common-action, H4 = Section 3.4
delayed). After the reorder they were misaligned. Renumbered to the new
subsections (main + supplementary):

| old | new | theorem |
|-----|-----|---------|
| H1.1, H1.2 | H5.1, H5.2 | finite-time exit (now 3.5) |
| H3.1–H3.3 | H2.1–H2.3 | common-action (now 3.2) |
| H4.1–H4.3 | H3.1–H3.3 | delayed-information (now 3.3) |

Every cross-reference (e.g. "Theorem~\ref{thm:delayed}'s (H3.1)", "the
closed-loop existence hypothesis (H5.2)") remapped in both files.

## 2. Supplementary S1 (complete proofs) followed the old main order

S1 presented exit → emptiness → common-action → delayed → recursion → fibre.
Reordered to the new main spine: recursion → common-action → uniform-margin →
ladder → delayed → exit → emptiness → fibre → certainly-safe → monotone, and
its equation tags/references renumbered to match (same mapping as the main:
(1)→(4), (2)→(1), (3)→(2), (4)→(3), (5) unchanged). The supplementary's theorem
numbering now coincides with the main's (Theorem 1 = recursion, 2 =
common-action, 3 = delayed, 4 = exit).

## Verification (v32 -> v37)

- Supplementary: 17 numbered environments accounted for; the 5 that differ
  differ only by the remapped `Section 3.x` references, hypothesis labels, or
  equation tags — bodies byte-identical otherwise. Block reorder is a pure
  move (no connective prose between blocks was touched).
- Main: unchanged from v36 except the hypothesis-label renumbering.
- QA: main 15 pp / 4 images / 1 table / 0 `??` / no overfull / abstract 262
  words; supplementary 12 pp / 3 images / 0 `??`.
- Equation tags now (1)–(5) in reading order in both documents; hypothesis
  labels read H2 → H3 → H5 in both documents.
