# v41 line: presentation restated for journal convention

Built 2026-09-18 (Asia/Tehran) from the frozen v40 line: article v40 + supplementary v11 + companions v2 →
**article v41, supplementary v12, companion A v3, companion B v3**. No file of an earlier version was edited.

## 1. The instruction this version answers

Four files that had accreted a working record — version parentheticals, change logs, what an earlier draft
printed, what a reviewer asked, whether a computation had been run, and self-commentary about the value of the
material — were restated so that the argument stands on its own. Rules applied:

1. A manuscript may cite work that exists or will exist. It may not cite its own drafts.
2. Where a pointer to a superseded arrangement helped a reader resolve a label, the resolution was kept and the
   history was dropped: the reader gets "the labels to read today", not "what the older file said".
3. No over-hedging: metaphor apologies and "this is not a claim about the territory" disclaimers were removed
   where the sentence already states the scope; legitimate scope statements were kept and are listed in §4.
4. Informal register was measured, not guessed at: a term counts as a defect only if it is not the name of
   something in the article.

## 2. What changed, by file

| File | Logged edits | Words | What kind of change |
|---|---|---|---|
| `paper3_material_ledgers_v41.{md,tex,pdf}` | 18 | 33,496 → 33,521 | numbering note rewritten as a convention statement; supplementary pointer de-filed and de-versioned; Remark 33's self-justifying tail cut; the aggregation-level sentence and Remark 37's record sentence recast impersonally; code availability rewritten (no "a fourth script is deliberately not claimed", no "two file names"); Remark 36 retitled "What the type structure yields, and what it does not"; the two companions cited in text and added to the reference list, whose Abaee entries are re-lettered 2026a–e |
| `paper3_supplementary_v12.{md,tex,pdf}` | 25 | 8,899 → 9,246 | the three part headings renamed from "additions at v9 / v10" to what the parts contain; the "Part I above is the file …_v8.md, carried unchanged" paragraph replaced by a contents paragraph; S17's "Added at v11, against main-text v40 … the computation the companion named as the one thing standing between it and a full paper" replaced by a scope sentence; six headings carrying "(main-text v39)", "(demoted from …)", "at v33" rewritten; S6's "Nothing above this section is edited" and its "1–20 counter" range corrected; the `[author]`-cells sentence recast; S15/S16 wording; **S9.4's extended inventory regenerated from the article** (27 rows, labels 21–47, with the section each now sits in) |
| `companionA_certification_procedure_v3.{md,tex,pdf}` | 16 | 5,064 → 4,954 | version parenthetical removed from the header; §8 retitled and its "What v2 changed, and why nothing was overwritten" block plus the v5→v2 relabelling table replaced by the archival principle itself ("Deposited material is not edited in place…"); §11 retitled from "Deposition, and what to hand to an editor" to "Availability of the deposited material, and its licence" with the Zenodo workflow advice dropped; run command paths de-versioned; "what the tool cannot buy" → "cannot certify"; a References list added (main text, companion B, Ricard et al. 2012) |
| `companionB_standards_horizon_v3.{md,tex,pdf}` | 15 | 4,569 → 4,345 | header de-versioned; §1's "A reviewer of the main text asked, in effect…" and "One question this file used to leave open has since been settled on data" rewritten as the question and the scope of §7; §7's "The question this section used to pose is now answered on data. The brief was:" replaced by the three questions it answers; §10 ("What changed at v2, and why v1 was not edited") deleted; "This is not a criticism of the standard" dropped with the classification argument kept; "It costs nothing but honesty", "worth more than it looks", "the check a reviewer can perform" recast; §5 title; References added (main text, companion A) |

Across the four files 2,459 words of narration and framing were removed and 2,497 added, the surplus being the
regenerated inventory, the availability paragraphs and the reference entries: the line is word-neutral overall.

## 3. Two structural fixes, not patches

**The extended statement inventory was stale, not merely version-flavoured.** S9.4 introduced itself as
"Main counter 1–33 … New in this version" and listed the labels added at an earlier revision, three of them
against section numbers the article no longer uses (Definition 21 shown under 1.3, now 2.1; Theorem 24 under
4.8, now 3.6; Proposition 32 under 6.5.1, now 6.5.4). The v40 line left the framing sentence as the explanation.
v12 generates the table from the article's own statement headings: all 27 labels numbered 21–47, each with the
section it currently sits in, and the builder asserts that the labels the old table listed are all still there.
The check in the gate recomputes the same mapping from the delivered files, so the inventory cannot silently
drift again.

**The supplementary is now typeset.** Every version of this line distributed the supplementary as markdown,
because the corpus's converter is pdflatex-safe and refuses non-ASCII output; the file carries programme
listings and prose with operators and diacritics (`≤`, `λ`, `X̄`, `□`, `Ø`). `build_supp_tex_v1.py` transliterates
each such character to the construct that denotes it — ASCII spellings inside a fenced listing, math commands in
prose — and nothing else, and the gate then requires that **every prose word of six or more letters in the
source appears in the compiled PDF** (0 missing of 178 lines / 232 sentences checked) plus the numerals and
headings by needle. 18 pp. The transliterated intermediate, `paper3_supplementary_v12.ascii.md`, is kept so the
`.tex` is reproducible.

## 4. What was deliberately kept

* Legitimate scope statements: "the figures are world totals, not any territory's"; "simulation, not a claim
  about any basin"; "not a member of the $J^{\mathrm{gross}}$–$H^{\mathrm{loc}}$–$T_A$ hierarchy"; the quarantine
  daggers; "the reported value is not promoted to a forecast".
* Terms of art the register audit flagged and adjudicated as technical: the non-displacement *gate* (Remark 35),
  the maintainability *kernel* and empty-*kernel* obstructions, *satisfying* a hypothesis, *promoted* as a status
  word, *load-bearing*, the *deliberately incomplete* comparison process of the ADH construction.
* The label-reconciliation table in S16, without its history: three of S7's pointers name sections that no
  longer carry the cited statements, and the reader needs the mapping.
* The archival principle in A §8, stated version-free, and A's licence paragraph (CC-BY-4.0 covers the quoted
  spot values, not the archived extract).

## 5. Verification

* `verify_v41_formal.py` — **ALL CHECKS PASS**, 11 groups: (1) positional reversal of all 74 logged edits
  reproduces v40 md, v40 tex, v11 md, A v2 md and B v2 md byte for byte (md5 matches on all five); (2) no
  unit-bearing or in-math decimal was removed (0), all 435 removed digits are label, cross-reference, path or
  DOI shaped, and no numeric table row was deleted; (3) the strict publication-register pattern set returns 0
  hits on all four sources; (4) every surviving `v…` token is a cited product vintage; (5) the companion
  citations and reference letters resolve in all four files, and every S-number cited anywhere resolves to a
  section that exists; (6) S9.4 against the article as built; (7) the numbering note's maxima equal the
  article's real ones (Definition 47, Lemma 4, Proposition 43, Theorem 24, Remark 37, Corollary 19);
  (8) content parity; (9) the three typeset PDFs (56 / 10 / 8 pp) against their sources, on extracted text
  folded for ligatures; (10) `recompute_tau.py` re-run in a scratch copy from `source/` alone reproduces the
  three CSVs and `results.txt` byte for byte; (11) the supplementary PDF against its markdown.
* `verify_v40_build.py`, `verify_companions_v2.py`, `verify_companions_v1.py` re-run over the frozen prior line:
  **ALL CHECKS PASS** on each; those files are unmodified (mtimes unchanged).
* `review/tone_scan_v1.py` — four pattern families with an adjudicated technical allowlist — over the four new
  sources: **total 0**; the record is `review/tone_scan_v41.txt`.
* Content audit against the deposited vintage, answered by measurement rather than assertion: the v5 line's
  quantity tokens still short after v41 (4) are the same 4 that were short after v40, and each was traced —
  two are comma-grouped thousands whose figures the §6.5.2 implied-production table carries (`$239{,}482$`,
  `$2{,}778$`), two are the same values inside `$…$ kt` in the article's text. Nothing the deposit stated is
  absent from the line as delivered; the v5 sentence on per-country implied production survives as the table
  column it describes.

## 6. Still the author's to confirm

1. The two new reference entries say "submitted with this article". Change to the journal's wording ("this
   issue", with DOIs) if the companions are accepted, and mirror the same wording in the two companion files.
2. If A and B are deposited, their reference entries should gain the Zenodo records, as the other three
   companions already have.
3. Whether the supplementary should ship as PDF at all: the deposit currently carries it as markdown; v12 now
   also has `.tex` and `.pdf`, produced by the transliteration above, and the two must be deposited together with
   `paper3_supplementary_v12.ascii.md` if the PDF is used.
