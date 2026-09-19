# The structure problem, its root cause, and what v34 changes

## Diagnosis (not a style complaint)

v32 carries three structural defects that *cause* the citation and numbering accidents the audits kept
finding. They are not cosmetic, and re-ordering headings would not touch them.

1. **The load-bearing obstruction sits after its uses.** No-weighted-certification (10.1) is invoked by
   the depletion classifications (6.5) and by the interface section (9), and the aggregation material is
   filed under "What the Ledger Does Not Support". A reader following 6.5 forward-references into 10.1,
   and an author adding a statement to 6.5 has to re-check 10.1. Root cause: sections are ordered by
   *narrative* (model → results → applications → caveats) while the *dependency* order is
   kernel → certification → aggregation → applications. Fix applied: the aggregation obstruction is now
   cited, not assumed --- and the composition calculus (3.7) is placed in the certification part, before
   the applications that need it, instead of in a deferred companion.
2. **Numbering was a convention maintained by prose.** v32 carries a "numbering note" of 40 words that
   asserts labels are unique, and the supplementary carries an "S6 statement-status naming offset" to
   reconcile the article's labels with the supplementary's --- two hand-maintained devices compensating
   for the absence of a machine-readable register. Every revision that adds statements (this one added
   19) risks silently falsifying both. Root cause: no derived artifact records which labels exist.
   Fix applied: `label_register.py` generates `labels_v34.json` from the LaTeX of record and checks,
   in both the `.tex` and the `.md`, that (kind, number) pairs are unique, that the label sets of the
   two formats agree, that every citation names an introduced label, and that the supplementary's
   inventory rows point at existing sections. It runs in seconds and fails loudly.
3. **Two formats, one content, no check.** The repository keeps `.md` and generated `.tex/.pdf` under
   the same version number, but nothing verifies that they say the same thing; paper1's `.md` line stops
   at v23 while its `.tex` runs to v43. Root cause: the pairing is by filename convention. Fix applied
   here: v33 and v34 are built from a single operation log per format, and both are checked to be
   insert-only over the previous version, so md and tex cannot drift apart silently (46 statement heads
   and an identical label set on both sides, per the register).

## The architecture v34 actually implements

* **Kernel (1--2)** what a ledger is, including composition (3.7 for the calculus, Definition 34).
* **Certification (3)** the predicates, the budgets, the interface price --- and now the composition
  theorem, so nothing in 4--10 depends on a property of assembled systems that is not proved.
* **Obstructions (6.6, 10)** what records cannot fix: identifiability sets of event times, and the
  aggregation impossibility, stated as theorems rather than as a caveats section.
* **Applications (6.5, 7, 8)** classification only; each row names the predicate it establishes.
* **Register (generated)** `labels_v34.json`, the shared spine of article, supplementary, and build.

Deferred no longer: rows 11 and 17 of the deployment register (the identifiability sets and the
"companion calculus") are now in-article statements 34--39 with proofs and machine-checked instances
(`kernel_exhibits.py`).
