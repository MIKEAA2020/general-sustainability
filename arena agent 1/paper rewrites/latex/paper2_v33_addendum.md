# v33 — Pass 1: surgical physical spine reorder of Section 3

## What changed

Section 3 is physically reorganized into the requested spine order (A–D lead,
finite-time-exit and admissibility material repositioned as support), with the
sparse finite witness (Helly) promoted to its own subsection. All mathematical
content is preserved: the 22 numbered environments are byte-identical to v32
except for the two that carry a remapped `Section 3.5 -> Section 3.1`
cross-reference (`prop:selector`, `prop:degenerate`). Only three classes of text
were edited:

1. **Subsubsection titles** (renumbered to the new order);
2. **Hardcoded `Section 3.x` / `Sections 3.x--3.y` cross-references** (remapped
   to the new numbering); and
3. **Two now-false forward connectors** and the **Section 1.4 organization
   sentence** (rewritten to the new order).

## New subsection numbering (old -> new)

| New | Old | Content |
|-----|-----|---------|
| 3.1 | 3.5 | Finite-horizon completeness (finite systems) — recursion (A) |
| 3.2 | 3.3 | The instantaneous common-action obstruction (B) |
| 3.3 | 3.4 | The delayed-information obstruction, threshold σ* (C) |
| 3.4 | (new) | The sparse finite witness — Helly, extracted from 3.3 (D) |
| 3.5 | 3.1 | The finite-time exit certificate (support) |
| 3.6 | 3.2 | Epistemic emptiness by admissibility (support) |

## Cross-reference remap applied

- `Section 3.1` -> `Section 3.5`  (finite-time exit)
- `Section 3.2` -> `Section 3.6`  (emptiness)
- `Section 3.3` -> `Section 3.2`  (common-action)
- `Section 3.4` -> `Section 3.3`  (delayed)
- `Section 3.5` -> `Section 3.1`  (recursion)
- `Sections 3.1--3.4` -> `Sections 3.2--3.3 and 3.5--3.6`  (the sufficient certificates)
- `Sections 3.2--3.4` -> `Sections 3.2--3.3 and 3.6`  (the informational certificates)

## Connective corrections

- Emptiness section: "the common-action obstruction of the next section" ->
  "the common-action obstruction of Section 3.2".
- Emptiness section: "The next theorem states the general obstruction" ->
  "Theorem~\ref{thm:common-action} states the general obstruction".
- Section 1.4 organization sentence re-written with the new ranges:
  `Theorem~\ref{thm:finite-horizon}--\ref{thm:exit}` (renders "Theorem 1–4"),
  `Propositions~\ref{prop:uniform-margin}--\ref{prop:emptiness}` ("Propositions 2–5"),
  `Remarks~\ref{rem:sigma}--\ref{rem:comparison}` ("Remarks 1–2").

## Renumbering consequences (automatic, verified in the PDF)

- Theorem 1 = finite-horizon soundness and completeness; 2 = common-action;
  3 = delayed-information; 4 = finite-time exit.
- Proposition 2 = uniform margin; 3 = obstruction ladder; 4 = sparse
  common-action witness (Helly); 5 = epistemic emptiness.
- Remark 1 = threshold form (σ*); 2 = comparison-function form.

## Supplementary

Two cross-references remapped identically (`Sections 3.2--3.4` and
`Section 3.5`). No other content changed.

## QA (identical harness to v32)

- Main: 15 pages, 4 images, 1 table, 0 `??`, no overfull, abstract 262 words.
- Supplementary: 13 pages, 3 images, 0 `??`.
- All 22 numbered environments byte-identical to v32 (modulo the two intended
  reference remaps); line-level multiset diff contains only the intended edits.
