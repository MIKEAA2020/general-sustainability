# v34 — Pass 2: connective/consistency polish after the v33 reorder

## What changed (all content-preserving; no math touched)

1. **Section 3.1 opening** (recursion) re-framed for its new lead position:
   the two opening sentences are swapped so the section now opens with the
   exact finite calculus and then frames the later subsections as sufficient
   certificates.
2. **Section 3.1 closing**: "the sufficient certificates of Sections 3.2--3.3
   and 3.5--3.6" -> "the sufficient certificates of the following subsections".
3. **Section 3.2** (common-action): one-sentence lead-in added — "The
   instantaneous obstruction is the static core of the calculus: it certifies
   nonviability at a single information state, without a timing or horizon
   argument."
4. **Section 3.6** (emptiness) opening: "The remaining obstructions apply"
   -> "The admissibility obstruction applies" (it is now the final subsection).
5. **Section 1.2 contributions**: the six enumerated items are reordered to the
   new spine (common-action, delayed-information, finite-time exit, epistemic
   emptiness, fibre criterion, certainty-equivalence trap); item bodies are
   byte-identical.
6. **Section 1.2 refinements**: the "Five refinements" sentence is reordered to
   the new spine (recursion, uniform-margin, threshold, Helly sparse witness,
   comparison-function form).
7. **Section 7**: duplicated phrase fixed — "This section makes that gap
   precise: it exhibits that gap precise: it exhibits two settings" -> "...it
   exhibits two settings".

## Supplementary

Unchanged from v33 (content identical; version-paired file produced for a
complete self-contained v34 set). The two Section 3 cross-references were
already remapped in v33.

## QA (identical harness)

- Main: 15 pages, 4 images, 1 table, 0 `??`, no overfull, abstract 262 words.
- Supplementary: 13 pages, 3 images, 0 `??`.
- Line-level multiset diff v33 -> v34 contains only the edits listed above.
