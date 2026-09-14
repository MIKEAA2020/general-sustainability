# v42 — fix: duplicated References heading in the supplementary

## Change

The supplementary contained two consecutive `\subsection{References}` headings
with the same `\label{references}` (a visible "References / References" on the
final page and a multiply-defined label). Removed the duplicate. No other
change: the main text is carried forward from v41 unchanged (expanded scope
kept, as instructed).

## QA

- Supplementary: 13 pages, 3 images, 0 `??`, no overfull; "References" now
  renders exactly once; no duplicate labels remain in the source.
- Main: 16 pages, 4 images, 0 `??`, no overfull (unchanged from v41).
