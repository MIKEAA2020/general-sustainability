# v35 — Pass 3: final review pass (three clarifying edits)

Third and final pass of the Section 3 spine reorder. Three references that
became forward references after the reorder are made explicit; no other change.

## Edits

1. Section 3.2 (Farkas discussion): "supplies one under the convexity
   hypotheses stated there." -> "stated in Section 3.4." (the Helly witness now
   lives two subsections ahead).
2. Section 3.3 (H4.2): "the class of Theorem~\ref{thm:exit}'s proof" -> "...'s
   proof, Section 3.5".
3. Section 3.1 (one-step instance): "This is Theorem~\ref{thm:common-action} in
   the finite-horizon language" -> "This is Theorem~\ref{thm:common-action}
   (Section 3.2) in the finite-horizon language".

## Full three-pass verification (v32 -> v35)

- All 22 numbered environments accounted for: 19 byte-identical to v32,
  2 differ only by remapped `Section 3.x` cross-references (prop:selector,
  prop:degenerate), 1 differs only by the added Section pointer above
  (thm:delayed). No mathematical content was added, removed, or altered.
- Line-level multiset diff v32 -> v35 contains only the intended renumbering,
  remapping, connective, and item-reorder edits across the three passes.
- Main: 15 pages, 4 images, 1 table, 0 `??`, no overfull, abstract 262 words.
- Supplementary: 13 pages, 3 images, 0 `??`.
- Rendered numbering verified: Theorem 1 = finite-horizon completeness,
  2 = common-action, 3 = delayed-information, 4 = finite-time exit;
  Proposition 2 = uniform margin, 3 = ladder, 4 = sparse witness (Helly),
  5 = emptiness; Remark 1 = threshold (sigma*), 2 = comparison-function form.

## Supplementary

Unchanged from v33/v34 (the two Section 3 cross-references were already
remapped in v33); version-paired file produced for a complete v35 set.
