# The v42 line: what changed, and what was measured

Four documents — article v42, supplementary v13, Companion A v4, Companion B v4 — plus a re-bundled
code release (`code_v3/`) and a single archive (`paper3_supplementary_package_v1.zip`). The v41 line
and the frozen v2 code directory are untouched on disk, and every edit is reversible from
`revisions_v42_formal_log.json`: reversing the twelve logged replacements against the shipped
markdown returns the v41 bytes exactly.

## Why the line was rebuilt rather than re-worded

Two measurements came back from the files themselves, not from the prose.

**Lines ran past the text block.** With a 159.2 mm text block on an A4 page, the widest word on the
widest line sat beyond the right margin by:

| document (prior line) | right overhang | words outside the frame | Overfull \hbox |
| --- | --- | --- | --- |
| article v41 | 74.2 pt | 44 | 3 |
| supplementary v12 | 77.8 pt | 154 | 13 |
| Companion A v3 | 77.9 pt | 159 | 2 |
| Companion B v3 | 48.2 pt | 26 | 2 |

That is more than a quarter of the text block: the long monospaced labels in the exhibit tables and
the input-name tables were unbreakable, so TeX set them and let them run.

**The supplementary printed its own converter.** Its PDF contained 34 literal `\S` sequences and 83
unpaired `$` characters, and 15 headings printed `$\cdot$` or `\textperiodcentered{}` — because the
section-sign spans had been wrapped as `$\S$` in the markdown, where the converter escapes the
backslash, and because the heading line is itself escaped by the converter, so TeX markup placed in a
heading is printed rather than executed. The article's own PDF printed `\S{}` twice for the same
reason.

## What the rebuild did

* The three tables that could not fit were given a width-solving stage (`tablekit_v2.py`): for each
  table a font and inter-column gap are chosen from six steps, and a penalty structure is built in the
  two width units the material actually needs — 1.85 mm per character inside `\texttt{}`, 1.60 mm for
  ordinary text, 1.95 mm inside `$…$` — with monospaced runs broken at underscores and slashes and
  long hex digests at 16 characters. Each column carries its own size and padding inside `>{}`, and
  the gaps are `@{\hspace{…pt}}` glue, so nothing sits between `\toprule` and `\begin{longtable}`,
  which is where a stray declaration becomes a misplaced `\noalign`.
* Long URLs get breakpoints at `/` and `_` and are set with `\urlbreaks`; the arithmetic identity
  cells of `tau_by_year_2017edition` (up to 142 characters on one line) are re-wrapped as two
  aligned display equations, which is the only change made to the supplementary's data.
* Unicode in escaped registers — headings and code spans — is spelled the way the rest of the file
  spells it: `§` becomes `Sec. `, `·` becomes `-`, `ℓ` becomes `ell`, `∂` becomes `partial`, `Ḃ`,
  `Ṙ` and `ḃ` become `B_dot`, `R_dot`, `b_dot`, `Ø` becomes `\varnothing`. A `Ø` set as `\O` in
  running text still reported a missing character in `cmmi10`, so the math form is used there.
* Every `.tex` header states what the file is in three comment lines — manuscript and line, the
  sources it was typeset from and the compile sequence, and the typography stage that made the tables
  fit. Headers used to carry the deposit's own history, which is why the four of them were rewritten
  in place; the body of each file was never touched by that change.
* Each file's `**References**` line was corrected to the objects that actually exist: the NFA
  deposit's directory now has one manifest, beside the two tables it points at; `code_v3/MANIFEST.md`
  records the run command, the file hashes, the exhibit inputs and the environment; the two edition
  tables are not redistributed, which is stated in the three places a reader meets them.
* Every mention of "submitted with this article" was checked: the phrase remains only where the
  journal's own wording is still to be settled, and the open list at the end of `README.md` in the
  archive says so.

## What the rebuild reports

| document | pages | Overfull \hbox | right / left overhang | words outside the frame | underfull \vbox |
| --- | --- | --- | --- | --- | --- |
| article v42 | 57 | 0 | 0.0 / 0.0 pt | 0 | 0 |
| supplementary v13 | 19 | 0 | 0.0 / 0.0 pt | 0 | 0 |
| Companion A v4 | 10 | 0 | 0.0 / 0.0 pt | 0 | 0 |
| Companion B v4 | 8 | 0 | 0.0 / 0.0 pt | 0 | 0 |

The supplementary's `§` material now renders as 33 section signs in prose and one as `Sec.` in a
heading; no `$`, `\S`, `\text` or unresolved `??` survives in any of the four PDFs, and the longtable
columns sum to 159.2 mm or less on every page (the supplementary's wide table sits at 0.00 mm of
slack, the others between 0.13 and 0.43 mm). Article, Companion A and Companion B grow by 0 pages;
the supplementary grows by one because S16's tables were set one size down.

## The framing work

The article's opening and closing sentences were cut where they claimed more than the analysis
earns: a passage of the form "when one of these quantities moves, does the others' response follow,
and does the gap between them widen or close?" is a description of what the paper does, not a claim
about institutions, so it now says that similar units conceal distinct constructs; the closing
sentence states that each claim carries the predicate it establishes and no more, with an interface
contract as the place where the shared object is fixed. The abstract and the conclusion were
rewritten to match, at the same word count.

The unit passage in §1.1 states the distinction the register work needs: the four quantities share a
denominator and differ in their numerators, so their period is the same dimension as the quantity they
divide — years of *that* subtraction — and a half-life, a residence time and a time constant are
different estimators of a decay, not three names for one number; the work that raises a tower over a
year and the torque that holds it are both newton-metres, which is why the promotion from balance to
stress is inferential and not arithmetical.

Four passages that had drifted into the language of adequacy or of a proposal were re-cast as
characterisation with a proof predicate: the exhibit comparison (S16) states which convention each
table reports and why the two must not be pooled, not which one the reader should prefer; the
reconciliation rule (S8.1) is the rule this pair of ledgers satisfies; the certification paragraph in
§3.1 states what `Recompute` accepts and what it rejects, and the same holds for the
recomputation-equals-recomputation claim, which is now a proposition about one object rather than a
programme; the ledger-to-standard mapping (§6.1) and the `check()` lemma (§6.2) are exhibited as
properties of the arithmetic, not argued for.

The 2022 exhibit stays a numerical illustration of the criterion, which the section now says in
those words; the data-vintage rule in S5 records that the 2018 table is the headline cohort under that
rule and that the 2017 control is what a reader following the published command obtains today;
§6.2 says "a row with two statuses" rather than "the same row twice"; the paragraph that explained
why the two NFA tables sit where they sit was cut, and the record's own manifest is cited instead.
A tone scan of the four sources with the established instrument
(`review/tone_scan_v1.py`, output in `review/tone_scan_v42.txt`) returns zero hits.

## The code release

`code_v3/` is the v2 bundle with the parts that had drifted put back in line: the two exhibit scripts
carry a header and a usage line naming their inputs — the `NCS_2018` shape file that
`curvature_and_crossover.py` reads is now named in its docstring and in the manifest's exhibit-inputs
table — `outputs.txt` is regenerated from the three scripts, all 47 numeric lines of it are identical
to the deposited record's, and `MANIFEST.md` gives the run command, the file sizes and checksums, the
environment (CPython 3.11 with pandas 2.2.3, numpy 1.26.4, pulp 2.8.0), and the limits of scope: no
script takes an argument, reads a file, opens a network connection or writes anything, so no
deposition date or version identifier can be embedded in them. The frozen `code/` directory keeps the
outputs of the deposit as they were, and the two `outputs.txt` are compared line for line by the
gate.

## The archive

`paper3_supplementary_package_v1.zip` (1.10 MB, 36 files, `MANIFEST.sha256` verifying for 35 of them
and excluding only itself) holds `README.md`, `manuscript/` with the four documents in markdown, TeX and PDF, `code/`
from `code_v3/`, `analysis/nfa_tau/` — the reader-revised record, with the two edition tables left in
`source/` and their retrieval commands in `source/MANIFEST.md` — and `builders/` with the two
builders, the two shared kits, the verification gate, and the two logs that make the line reproducible
and reversible.

The README says what the supplementary is, in the archive's own words: its "role is checking, not argument",
it "reports what was verified and by which operation, which deviations from the standard are documented and on
what grounds, which statements the record supports and at what predicate, and what remains unresolved", and proofs
are "given to the depth at which a reader can re-do a step with a calculator and the tables in this archive", with
the text saying so wherever a step is stated rather than demonstrated. It separates the exhibit bundle from the
analysis record by what repetition requires of a reader: the bundle "runs on synthesised inputs and nothing else"
and asserts that the article's computed figures reproduce, the record "runs on the two edition tables of the
accounts" and asserts that the overshoot date recomputes under the weighting its README states; "neither needs the
other, and neither needs the network". The four papers in `manuscript/` are separated from both, and the companions
are named as "papers in their own right, not appendices". Three ways of checking are stated in
"Verifying it": `sha256sum -c`, reading a table beside the text that quotes it, and running
`python3 analysis/nfa_tau/recompute_tau.py` from the top of the unpacked archive.

and it distinguishes the exhibit bundle from the analysis record: the bundle is what a reader runs to
see the exhibits reproduce, the record is what a reader runs to recompute τ itself, and they differ in
their inputs (synthesised versus the Footprint Network tables), in what they assert, and in what a
reader needs in order to repeat them. The four papers in `manuscript/` are separated from both, and
the three ways of checking — `sha256sum -c`, reading the table beside the text that quotes it, and
`python3 analysis/nfa_tau/recompute_tau.py` — are stated in "Verifying it".

## Verification

`verify_v42_build.py` runs eleven groups: the log reverses to the v41 bytes; no quantity disappears
and no number in a removed span is unexplained; each framing correction is present in the markdown,
the TeX and the PDF while the superseded sentence is absent from all three; the register scan covers
the sources the previous gate had not read, including the four TeX headers and the three MANIFEST
files; no path to a working directory survives; a fresh compile from the shipped TeX returns
`rc = 0` with the counts above; the PDFs print no raw TeX; the S9.4 inventory still bijects with the
article's 27 numbered objects in 21–47 with their loci; `recompute_tau.py` reproduces the four output
files byte for byte from the two tables in `source/`; the archive unpacks, verifies against its
manifest, runs its script from its own top, and its output record matches the deposited numerics line
for line; and the four older gates still pass. The whole run prints `ALL CHECKS PASS`.

## For the author

1. The journal's own wording for A and B — "submitted with this article", "accompanying", or a
   deposit DOI once Zenodo records exist for them.
2. Whether a 2022-vintage component table can be obtained by email from
   `data@footprintnetwork.org`; `analysis/nfa_tau/source/MANIFEST.md` now records the request and the
   answer as "no", which is the fact as at this build.
3. Whether the two NFA edition tables should be mirrored in a separate data deposit, which is the
   only way they can be redistributed by us.
