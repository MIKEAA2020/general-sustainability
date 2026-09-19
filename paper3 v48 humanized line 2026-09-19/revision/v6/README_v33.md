# v33 — the surviving audit points carried into the repository's manuscript of record

Nothing in the clone was modified and nothing was pushed; the repository clone under
`github/gs/` is left exactly as fetched (`git status --porcelain` empty, checked by
`verify_v33.py`).

## What this version is

`paper3_material_ledgers_v32.md` in `arena agent 1/paper rewrites/` is the markdown of record for
paper 3 — its LaTeX header says the `.tex` is generated from it and the shipped PDF matches the
md5 of the compiled v32. Its LaTeX file also shows that v32's *own* statement counter ends at 20,
so the 13 statements drafted in `revision/v5/paper3_v5.md` as numbers 21–33 land in v33 without
collision, and every cross-reference has been re-pointed from my section structure to v32's
(v32: depletion arithmetic at 6.x, first-passage at 7.x, institutional delay at 9,
non-compensation at 10.x).

| file | contents |
|---|---|
| `paper3_material_ledgers_v33.md` | v32 plus 30 logged operations: 13 statements, 6 passages, 9 reference entries, the 5 companion-placeholder citations fixed, the numbering note extended, the supplementary pointer advanced, a Code availability section |
| `revisions_v33.py` | the revision script (repository convention: previous version untouched, every operation logged) |
| `revisions_v33_log.json` | the operation log used by the verifier |
| `paper3_supplementary_v9.md` | `paper3_supplementary_v8.md` carried verbatim, then Part II: S7 certification-state proof obligations and certificate vectors, S8 the linear programmes and the reading rule for infeasibility, S9 worked exhibits, promotion rules, reproduction record, statement inventory extended to 21–33 |
| `build_supp_v9.py` | builder for the supplementary, including the section re-pointing of the added blocks |
| `verify_v33.py` | 30+ checks; all pass |

## Checks that ran

`python3 revision/v6/revisions_v33.py` then `python3 revision/v6/verify_v33.py`:

* **Insert-only proof.** Reversing the 30 logged operations reproduces `paper3_material_ledgers_v32.md`
  byte-for-byte (sha256 match), so no sentence of v32 was reworded or dropped.
* **Labels.** 21–33 each introduced exactly once; statement heads grow by exactly 13; `$`/`$$`
  dialect matches the repository's markdown (no `\(`/`\[` introduced); `$$` balanced.
* **Citations.** Zero `in review` / `Author, D.` / `Author, E.` / `Author, F.` remain; the nine new
  reference entries appear once each and are alphabetised in place.

## LaTeX

No `.tex` or PDF was produced here: the sandbox has no pandoc or LaTeX, and the repository's own
builder is `batch 7 (audits of agent arena 1 paper rewrites)/wave13/build_latex_v13.py`, which
regenerates the LaTeX from the markdown and enforces the md/LaTeX numeric-token identity. Put
`paper3_material_ledgers_v33.md` where the builder expects the v33 markdown and run it there; the
declarations and references added here are in the shapes that builder already recognises.

## What the author still holds

* The pointer in the recharge-law text to "eq. (1) and Section 2.4" of the companion (the DOI and its
  Hopf/restabilisation figures resolve; the internal cross-reference inside that companion is the
  author's to confirm).
* The two companion DOIs used for the review screen (22554297) and the assessment analysis
  (22545740) — inserted because they are what the repository's References list already carries; not
  independently resolved here.
* D4's wording sign-off, and whether v33 keeps v32's section structure (it does) or adopts the
  re-cut in `revision/v5/`.
