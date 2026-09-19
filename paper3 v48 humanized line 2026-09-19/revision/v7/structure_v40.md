# v40 — the recomputation, folded back into the article

Prepared 17 September 2026. Previous version of record: **v39** (unchanged on disk). This record says what v40
changed, what measurement forced each change, and what v40 deliberately does *not* claim.

## Why a new version exists at all

Companion B's Section 7 said that one computation stood between it being a commentary and being a paper: recompute
$\tau_{\mathrm{agg}}$ with carbon demand excluded, on the accounts rather than in discussion, and report (i) whether
the restricted premium's trend sign survives the exclusion, (ii) how far the restricted and unrestricted dates
separate over the last decade, and (iii) whether the four-day vintage gap widens or closes. It has been run. Three
of its answers change the main text, and running it exposed two further defects in the main text that are fixed here
rather than left for the next reviewer.

## The twelve logged edits

| id | what it does | the measurement behind it |
|---|---|---|
| E1 | Remark 33 names the edition its 2022 row comes from, and keeps Lin et al. (2018) for the construction | the 2018 edition's `World` rows run 1961–2014, read from the table's own year column, so that release cannot contain a 2022 figure |
| E2 | Section 10.2's "vintage and nowcasting" clause becomes "vintage, nowcasting and aggregation level" | on the 2018 edition, the publisher's `World` row and a sum of the national rows differ by up to 9.2 d in the date, against at most 1.9 d for a whole edition step on a closed year |
| E3 | new **Remark 37 (Two component ratios are identities at a world aggregate)** | $r_{\mathrm{crop}} = r_{\mathrm{built}} = 1$ exactly in 54 of 54 years and $\tau_{\min}^{\mathrm{NOC}} = 365$ d in 54 of 54; $\tau^{\mathrm{NOC}}/\tau^{\mathrm{ALL}} = 1/(1-s_{\mathrm{carbon}})$ to $4.4\times10^{-16}$ |
| E4 | Data availability records both editions, their hashes and the registration gate | the current edition ships only through a form; `data.footprintnetwork.org` answers 403, the query service 404, data.world mirrors just the 2018 edition |
| E5 | Code availability says where the recomputation lives and why it is not in the exhibit bundle | the bundle's own manifest rules that no script obtains data |
| E6 | numbering note, Remarks 33–36 → 33–37 | Remark 37 is the 63rd labelled statement on the article's counter |
| E7 | Theorem 13's `no *interior* rest point` loses its inner emphasis pair | the pair was nested inside an italic span running to the paragraph's end, which no markdown reader resolves |
| E8 | four paragraphs re-converted so their emphasis typesets | Definition 40, Proposition 42, Theorem 13 and Proposition 43 printed literal `*` in the PDF; v39 had 8 such glyphs, v40 has 0 |
| E9 | two duplicated markdown heading markers removed from the tex | the PDF of record printed `## Code availability` and `## Declaration of competing interest` as text since before v38 |
| E10 | `Definition 19's programme` → `Proposition 37's joint programme` | no vintage of this article has ever labelled a Definition 19 (the number belongs to Corollary 19); the joint programme whose value gives the exact threshold is stated in Proposition 37, in the same subsection |
| E11 | the body names `paper3_supplementary_v11.md` | it named v9 while v10 was already accompanying the article |
| E12 | the supplementary-material paragraph enumerates S5.4, S10, S11, S14–S16 and S17 | so that the demotions of v39 and the addition of v40 are visible where the reader looks for them |

E7–E9 are typography and conversion repairs found *while verifying* v40's own content, not reviewer requests; they
are logged and reversible like the rest, which is why the gate's reversal test covers them.

## What was added to the corpus

`analysis/nfa_tau/` — `recompute_tau.py` (standard library only, no network, no interpolation), the per-year CSVs
for both editions, `edition_delta.csv`, `results.txt` (complete stdout), `checksums.txt`, a `README.md` with the
licence, the retrieval route and the aggregation trap, and `source/` holding the two tables as fetched with their
own `MANIFEST.md`. Companion B at **v2** reports the run, fixes the same Lin et al. mis-credit in its own
Section 4, and adds a provenance section; its items now run B1–B21, because the brief that used to be B18 became
prose and the four results became B18–B21. Companion A at **v2** records the analysis directory in its bundle
section. The exhibit bundle under `code/` is untouched, as its manifest requires.

## What v40 does not claim

- It is **not** a recomputation on the current release. The 2018 and 2017 editions are what can be fetched without
  an account; the script re-runs on a newer edition by changing two file names, and the article says so.
- The restricted minimum being 365 d at the world aggregate is **not** an empirical finding about convergence;
  Remark 37 states it as an identity of the accounting convention, which is why the article's earlier reading of
  the display needed qualifying rather than reinforcing.
- The four-day difference between an announced Overshoot Day and a recomputed date is **not** shown to be an error
  or to be explained away. It is shown to be smaller than one choice the reader makes (the aggregation level) and
  larger than one edition step on a closed year, which is a different and more useful statement.
- The world figures are world totals, not any territory's, exactly as before.

## Gates run

`verify_v40_build.py` — ALL CHECKS PASS. The logged pairs turn v40's markdown and tex back into v39's byte for
byte; the label inventory is 64 in v40 against 63 in v39 with exactly one addition, `('Remark', '37')`, and no
label lost or renumbered; every figure interpolated into the prose is recomputed by the gate from the CSVs; every
`Section` and supplementary pointer resolves; every statement-number citation names a label that exists, with zero
unresolved after E10; the PDF (tectonic, as the rest of the corpus) is 56 pages with no unconverted prose asterisk,
no literal heading marker, and exactly three underscores — the contact line and the named supplementary file.

`verify_companions_v2.py` — ALL CHECKS PASS: v1 files intact and recoverable by reversing the logged pairs, B1–B21
and Protocols 1–8 gap-free, the table rows matched against the CSVs, the hashes matched against `checksums.txt`,
and the analysis record re-run from a clean output directory reproducing its three outputs byte for byte.
`verify_companions_v1.py` still passes, which is the check that v1 was not edited.

`verify_v39_build.py` was not re-run: v39 is superseded, not modified.
