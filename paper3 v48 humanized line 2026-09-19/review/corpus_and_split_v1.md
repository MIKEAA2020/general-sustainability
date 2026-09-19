# Corpus Assessment v1: Can Paper 3 Be Split, How Many Papers Is the Work, and What the Companions Cover

Prepared against `revision/v7/paper3_material_ledgers_v38.md` (the version the question was asked about) and
`…_v39.md` (the version this assessment produced). All structural numbers below are produced by
`review/split_graph_v1.py <article.md>`, so they can be re-derived rather than taken on trust.

---

## 1. Is v38 a candidate for splitting? No. Is it a candidate for demotion? Yes, three passages.

### 1.1 How the question was settled

"Too long" is not a structural property, and neither is "it covers several topics". A paper splits cleanly when
the *dependency graph of its numbered statements* is disconnected across some section boundary: no result on one
side may cite a result on the other, and each side must still carry its own results. So the graph was built and
measured rather than argued about.

Method, in one paragraph. Every `**Definition n**` / `**Proposition n**` / `**Theorem n**` /
`Corollary` / `Lemma` / `Remark` heading is a node, assigned to the section containing it. A section-level edge
A → B is drawn when B's text cites a label whose home is A. Sections are then contracted and their strongly
connected components computed. A proper subset of sections closed under citations in both directions is exactly
a union of strongly connected components — so if the result-bearing sections form one component, **there is no
cut that separates the results**, and any split would have to duplicate a definition or break a citation.

### 1.2 What the measurement gave (v38)

| sec | section | words | labels | cites |
|---|---|---:|---:|---|
| 1 | Introduction | 3,050 | 0 | 3 |
| 2 | The Typed Primitive Ledger | 4,596 | 4 | 3, 4, 6 |
| 3 | Certification Layers and the Accounting Theorems | 7,955 | 27 | 10, 2, 4, 6, 7 |
| 4 | Conservation and Positivity of the Closed Ledger | 3,186 | 8 | 3 |
| 5 | Service Readouts and the Componentwise Deficit | 1,090 | 4 | 3 |
| 6 | Depletion Arithmetic | 4,879 | 10 | 10, 3 |
| 7 | First-Passage Semantics on Declared Support | 1,779 | 4 | 3, 6 |
| 8 | Domain Templates at Registered Status | 425 | 0 | — |
| 9 | The Interface with Institutional Delay Dynamics | 1,664 | 0 | 2, 4, 5 |
| 10 | What the Ledger Does Not Support | 2,390 | 4 | 4, 5 |
| 11 | Conclusion | 529 | 0 | — |

- **One component.** Sections {2, 3, 4, 5, 6, 7, 10} form a single strongly connected component containing
  **all 61** numbered statements.
- **21 of 21** section pairs inside that component are mutually reachable. A clean split needs 0 of 21.
- **20** distinct cross-section edges, **60** cross-section citation instances, **31 of 61** statements cited
  from outside their home section.
- Sections 1, 9 and 11 hang off the component in one direction only, which is why they — not the middle — are
  the movable material: the introduction can be shortened, and the interface section can be tightened, but
  neither cut produces a second paper.
- Four sections carry words and zero labels: 1, 8, 9, 11. Two of those are *genre* sections (introduction,
  conclusion). Two are substantive prose without a single numbered result: §8 (425 words) and §9 (1,664 words).

The verdict on splitting is therefore not a stylistic preference: the cut set is empty. A referee who asked for
two papers out of this manuscript would be asking for the type structure to be defined twice.

### 1.3 What the same measurement did say, and what v39 did about it

Three passages are material that the article does not need to carry, and one passage is a result wearing prose
clothes. The asymmetry matters: the fix for a section that carries no results is demotion, and the fix for a
section that carries an unlabelled result is **promotion**, not deletion.

| # | item | measured basis | action in v39 |
|---|---|---|---|
| D1 | §6.5.2's basin-row provenance paragraph (149 w) | §6's only unlabelled provenance block; its own text says the numbers "must not be reused numerically" | moved to the supplementary as **S5.4**, next to the vintage record (S5) it belongs to; the article keeps the classification sentence, the dagger note, and a pointer. The classification itself stays in the article because Section 6.5.3 depends on it |
| D2 | §8.1 and §8.2 (198 w) | §8 = 425 w, 0 labels; the ladders these paragraphs name are already stated as obligations in the supplementary's **S2**, and nothing in §6–§10 cites §8 | condensed in the article to the registered status plus the one admitted object and one gap, with the full detail moved to **S14** beside S2 |
| D3 | the §3.7 remark's self-pointer | the sentence "the statistical standards recalled in Section 1.5" pointed at a section that does not exist: the standards paragraph sits in §1.2 | re-aimed to §1.2. This was a genuine dangling reference in v38 — the same class of defect v38 existed to repair — and it is now caught by a gate check that resolves every internal `Section n.m` pointer |
| P1 | §9's exact-projection claim | §9 = 1,664 w with 0 labels, yet its central sentence — the block's six vector-field components exclude the macroeconomic states, prices and demand, "with no singular limit required" — *is* a theorem-shaped claim, stated and defended by inspection | promoted to **Proposition 43** with a two-line proof (invariance is the projection; the converse fails by construction, so the projection is one-way). The semiconjugacy to the companion's core is *not* claimed: the article states it is made under the paper-4 citation and not re-proved here, and v39 preserves that boundary explicitly |
| S1–S16 | the supplementary's missing fields | the review cycle deferred a per-parameter identifiability table and a material-and-energy-value (MEV) checkability table, and the `Typed` proof-obligation row cited an undefined use of "typing" | supplementary **v10** = v9 verbatim + Part III: S10 (identifiability), S11 (MEV), S5.4 and S14 (the demoted text, reproduced without change), S15 (`Typed` row citing Definition 47 and Proposition 42), S16 (S7's discharge column restated against v39, found while assembling S15) |

Two of these need a word of defence.

*Why the §6.5 basin row was demoted rather than deleted.* The Indo-Gangetic magnitude is quarantined: a
June-2005 SWE anomaly propagates into groundwater and the fitted trend is an order of magnitude beyond published
basin-mean behaviour. A referee asked why a quarantined number is printed at all. The answer the article gives —
and the answer S5.4 now carries in full — is that the row is the worked instance of the index construction, and
the classification status assigned to it does not depend on the magnitudes. That argument is a *provenance*
argument about a data product, so it belongs where the vintage record lives. The table, the dagger, the
classification and the pointer stay in the article; nothing a reader needs is behind a link.

*Why §9 was promoted and not demoted.* A 1,664-word section with no numbered statement invites the verdict
"cut it". Measuring the citation graph says the opposite thing about this particular section: §9 is cited by
nothing and cites three sections, but the claim it rests on is load-bearing for §4's and §5's macroeconomic
readouts. Deleting it would have removed the only place where the closure of the institutional-failure subsystem
is asserted; labelling it makes that assertion checkable, costs 71 words, and adds a label the article's own
numbering note can accommodate without disturbing monotonicity (Proposition 43 is the last label in the last
numbered position, and the note's added-label list changes from "39–42" to "39–43").

### 1.4 What v39 is, by measurement

Same script, same article line:

- 32,900 words (was 32,860) and 62 labels (was 61): **the restructuring does not shorten the paper**. It moves
  347 words of unlabelled prose out and puts 387 words of labelled content in. Anyone reading this as a length
  reduction has mis-read the verdict; the win is that the article now contains no *unlabelled* load-bearing
  result, and no prose whose only function is provenance.
- §6 4,879 → 4,827; §8 425 → 446; §9 1,664 → 1,735 (labels 0 → 1).
- The component structure is unchanged ({2,3,4,5,6,7,10}, 21/21 mutually reachable pairs), as it must be: no
  dependency was cut, and one was added to §9, which is why the demotion candidates are now only §1 and §11.
- Maxima: Definition 47, Proposition 43, Theorem 24, Remark 36, Lemma 4, Corollary 19; 55 typeset pages.
- `verify_v39_build.py`: all checks pass, including the reversal test — reverting the five logged edits returns
  v38 byte-for-byte in both markdown and LaTeX, so nothing else in the paper moved.

### 1.5 Where the length actually is, and what would have to change

If the author's real objective is a shorter paper rather than a better-structured one, the numbers say which
doors are closed. Section 3 carries 7,955 words and 27 labels and is cited by six other sections; Section 2
carries 4,596 words and 4 labels and is cited by Sections 3, 4, 6. Together they are 38% of the words and half
the labels, and they are the definitional apparatus the results are stated in — cutting them is cutting the
paper. The tables in §6.5 (three classified indicators) are the only other bulk, and they are the applied
content a referee asked to see. In this corpus, a shorter paper is not available; a differently-partitioned one
is not either. The correct response to "it is long" is what was done: move what has no results in it, and label
what does.

---

## 2. How many papers is this work? Six, of which two are new.

Counted as defensible units of contribution — a claim, its evidence, and its boundaries, in one register — and
not as files:

| # | work | register | status | what makes it a paper |
|---|---|---|---|---|
| 1 | Compensatory aggregation and the aggregation-fallacy account (paper 1) | theory + application | deposited | own object: the compensation predicate and its failure taxonomy |
| 2 | Typed flux ledgers and depletion arithmetic (paper 3, v39, Zenodo 22554177) | theory, with classification exhibits | deposited; v39 is a reallocation, not a rewrite | 47 definitions, 43 propositions, 24 theorems, the depletion-horizon semantics |
| 3 | Delay dynamics and the institutional-failure core (paper 4, Zenodo 22554217) | dynamics | deposited, under review | owns the gated three-state core, the memory–effort pair, and the semiconjugacy v39 declines to prove |
| 4 | Sampled governance (paper 5) | governance dynamics | deposited | owns the sampling and review-cycle objects |
| 5 | **Companion A** — certifying a typed ledger: predicates, programmes, vintages, reproduction bundle | methods / software | new, written this turn (`revision/v7/companionA_certification_procedure_v1.*`, 4.8k words, 10 pp.) | the eight obligations as decision procedures with input schemas, cost and exit conditions; the three LPs as solver-ready recipes; the three-test vintage protocol; the code bundle at v2 with its run record. None of this is a theorem, and none of it fits an article that is already 55 pages |
| 6 | **Companion B** — what the accounts settle and what they leave open | commentary / correspondence | new, written this turn (`…companionB_standards_horizon_v1.*`, 3.0k words, 6 pp.) | the 2025 SNA's recording change read against the horizon arithmetic: three steps from a rate to a horizon that no standard takes; the τ_agg = 213 d exhibit and the carbon zero-row convention; the citation-hygiene rule against paragraph numbers, with a concrete instance of draft-stage drift |

**Six, not eight.** The following were considered and refused, each for a stated reason rather than for
inertia:

| candidate | why it is not a paper yet |
|---|---|
| invariance of the results under umbrella reparameterisation (mechanism-design framing) | its primitives are undefined — the "umbrella" and the reparameterisation class are not objects in any deposited file; a paper needs the definitions first, and they are not ours to invent in someone else's register. If the author wants this, it starts as a two-page primitive note, not a paper |
| the MDV / identifiability material as a standalone metric paper | its content is now two tables in the supplementary (S10, S11) plus Propositions 38–39 in the article; standing alone it is a metric note without a comparison against an existing index family |
| the Lean 4 formalisation | nothing in the corpus states a formalisation target, the file set does not exist here, and a formalisation paper must report what failed to formalise; there is no such record |
| pilots, dashboards, decision-support interfaces | no evaluation design, no users, no protocol; would be a systems description with no evidence |
| re-deriving the G3P basin rows from the product masks | a data task, and a *prerequisite* for removing the quarantine note — valuable, publishable only if it produces a corrected basin series, which is the product's job, not ours |
| affinity / exergy as a fifth admissibility predicate | the predicate is defined in the article (Definition 42) but its check needs a species table and a declared `Ω` that no public instance supplies; Companion A §10 states exactly what would make it a paper |

**Overlap guard**, so the six do not become one with repetition: paper 1 owns the weak/strong predicate
language; papers 4 and 5 own delay and governance dynamics; paper 3 owns ledger semantics, the certification
layers and the horizon arithmetic; Companion A owns decidability-as-procedure, input schemas, solver recipes and
the vintage protocol; Companion B owns the standards interface and citation hygiene for it. A referee reading A
and §3.1 together should find that the *same* eight obligations appear in both, once as results and once as
procedures — that is the intended relation, stated in A's opening paragraph and in its "what this companion is
for".

**B's half-or-one hinge, kept out of the paper and recorded here.** B currently has one exhibit and no
un-run promises, which is what a commentary is. It becomes a full paper if, and only if, the carbon-demand
exclusion is recomputed on the current accounts release: the three numbers that decide it are listed in B's
Section 7 (sign of the premium's trend under exclusion, the restricted/unrestricted separation over the last
decade, and whether the four-day vintage gap to the announced overshoot date widens or closes). Writing that
computation into B as a third section without running it would turn a commentary into a proposal, and the last
thing this corpus needs is a claim resting on an unexecuted calculation.

---

## 3. What to change if the split question comes back

A split becomes arguable only if the dependency graph changes, which means one of:

1. §2.3's typed structure and §3's certification layers are re-axiomatised so that §4–§7 no longer cite §3
   (then the ledger-semantics/typology axis — Sections 1, 2, 6, 8, 10 — could stand alone at roughly 14k
   words, and the proof apparatus — 3, 4, 5, 7 — at 16k); or
2. the supplementary absorbs the whole classification apparatus (§6.5, S5.4, S10, S11), leaving a short theory
   paper — which would be a *different* submission with a different referee problem, not a shorter version of
   this one.

Neither is recommended. The first requires new mathematics (a decomposition of §3 that does not cite §2's
typing); the second removes the article's only applied content.

---

## Addendum, 17 September 2026 — the Companion B hinge is closed, and the pointer scan gained a check

This file recorded that Companion B was "half a paper, not one" until the carbon-exclusion recomputation was run.
It has been run, on the two editions of the National Footprint and Biocapacity Accounts obtainable without an
account (the 2018 edition, 1961–2014, with the 2017 edition as revision control), and the three answers are in
`revision/v7/analysis/nfa_tau/` and in Companion B **v2** Section 7, items B18–B21:

- the restricted premium's downward trend **survives** carbon's exclusion (524 → 323 → 230 → 179 d on the 2018
  edition; 45 of 53 year-on-year moves are declines; the article's later-release series 547 → 346 → 251 → 173 d
  has the same sign and shape and sits 4–8% above it);
- the two conventions part by **340.8 d on average** over 2005–2014, a ratio of 2.41–2.60 that equals
  $1/(1-s_{\mathrm{carbon}})$ to 4.4e-16, so the separation is a property of the convention and not a finding;
- the four-day vintage gap **neither widens into an error nor closes**: at most 1.9 d comes from an edition step on
  a closed year, while up to 9.2 d comes from the level at which the accounts are aggregated, and the restricted
  date is 5.8 times more revision-sensitive than the aggregate date.

So B is a commentary with an exhibit, and its v2 is a complete companion paper in the sense its own Section 7
defined. v1 is left in place, citable as the claim made before the numbers existed.

**Two things this measurement turned up that the structural scan had no vocabulary for.**

1. *A dangling internal citation the label inventory could not see.* `review/split_graph_v1.py` classified
   citations by kind and number to build the section graph, and the v39 gate checked that section and label
   *pointers* resolve, but nobody had checked that every `Kind n` citation in the prose names a label that exists.
   Doing so at v40 found one failure, `Definition 19's programme`, in Remark 34 — a number the article has never
   labelled (Corollary 19 holds it), present since v35 and copied forward through four gates. It is repaired at
   v40 by re-aiming it at Proposition 37, whose joint programme is what the sentence means. Split-graph note: this
   does not change the SCC result — a mis-numbered citation inside Section 3.7's own paragraph still points within
   the same component — but it is the kind of defect the graph was not built to detect, and the citation check is
   now part of the build gate.
2. *A conversion defect that outlived every content gate.* Four statements printed literal asterisks in the PDF of
   record because the manuscript's md→tex rule cannot close an emphasis span that crosses inline math or opens
   immediately after a bold run, and two heading markers had leaked into the tex as text. Both were found by
   looking at the typeset artefact rather than the source, which is why `verify_v40_build.py` asserts on the
   extracted PDF text (0 unconverted prose asterisks, 0 literal `##`, and the exact multiset of
   underscore-bearing strings) and not only on the markdown.

**Unmeasured, deliberately:** the section graph was *not* recomputed for v40. v40 adds one labelled statement
(Remark 37) into Section 10.2 and no new cross-section citation, so the one-SCC result of v38's graph is expected
to hold; if a split is ever argued on v40's structure, re-run `review/split_graph_v1.py` against
`revision/v7/paper3_material_ledgers_v40.md` rather than assuming it.

---

## Addendum, 2026-09-18 (second entry): the v41 line and what the register audit measured

The corpus was restated for journal convention: article **v41**, supplementary **v12**, companions **A v3** and
**B v3** (no earlier file edited). The editorial rule now binding on this line is that a manuscript may cite work
that exists or will exist but not its own drafts, so 74 logged edits removed every version parenthetical, change
log, "what the earlier draft printed" passage and self-commentary, while adding the two companion citations the
article was missing and, in the supplementary, the inventory and label records the article points to. The record
is `revision/v7/structure_v41.md`; the gate is `revision/v7/verify_v41_formal.py` (11 groups, ALL CHECKS PASS),
whose first assertion reverses all 74 edits to byte-identical v40 / v11 / v2 sources and whose second proves no
removed span carries a measurement. Two substantive corrections came out of the same pass, both found by measuring
rather than by reading for style:

1. *Supplementary S9.4's extended statement inventory was stale, not merely version-flavoured.* It listed the
   labels added at an earlier revision and, for three of them, section numbers the article no longer uses
   (Definition 21 under 1.3 where it sits in 2.1; Theorem 24 under 4.8, now 3.6; Proposition 32 under 6.5.1, now
   6.5.4). v12 generates the table from the article's own headings — 27 labels, 21 to 47, current loci — and the
   gate recomputes the same mapping from the delivered files, so it cannot drift silently. `Main counter 1–33`
   became the true range, and S6's "1–20 counter" was corrected with it.
2. *The supplementary is now typeset.* It had been markdown-only because the corpus's pdflatex-safe converter
   refuses non-ASCII; `revision/v7/build_supp_tex_v1.py` transliterates the 35 characters involved (ASCII operator
   spellings inside fenced listings, math commands in prose) and `verify_v41_formal.py` checks the result by
   requiring every prose word of six or more letters of the source to appear in the 18-page PDF, plus the
   numerals and headings.

**Register audit, and its false positives.** `review/tone_scan_v1.py` (four families: meta, self-praise,
apology/hedge, diary) reported 28 / 15 / 18 / 9 hits on the v40-era files and 74 sites of real defect were
derived from them; after the v41 edits it reports 0 on all four new sources
(`review/tone_scan_v41.txt`). The scanner now carries an explicit allowlist for the terms that are *objects of
this article* rather than narration — the non-displacement gate of Remark 35, the maintainability kernel and the
empty-kernel obstructions, `satisfying` a hypothesis, `promoted` as a status word, `load-bearing`, the
deliberately incomplete comparison process behind the ADH proxy — because a scanner that fires on all of them
makes a clean report meaningless. Over-hedging was separated from scope by the same test: "not a claim about any
territory" survives where the sentence is doing scope work, and "This is not a criticism of the standard", "It
costs nothing but honesty" and "what stands between it and a full paper" do not.

**Unmeasured, deliberately:** the section graph is still v38's. v41 adds no labelled statement and no new
cross-section citation, but it does add five reference entries and re-letter the Abaee ones (2026a–e), so the
graph should be re-run with `review/split_graph_v1.py` against
`revision/v7/paper3_material_ledgers_v41.md` before any split argument is made on this line.

---

## Addendum, 2026-09-19: the v42 line, measured from the PDFs rather than the prose

The author's reply to v41 named four things that still read like a technical report, and all four turned
out to be verifiable in the artefacts rather than arguable in the text. Two of them were.

**Typography.** A 159.2 mm text block on A4 had been assumed to hold the tables; the PDFs said otherwise.
Measuring word boxes against the margins (`texkit.overhang`, which reads `page.get_text("words")` and
compares against the media box after the kit's own 16 mm inset) returned right overhangs of 74.2 pt for the
article, 77.8 for the supplementary v12, 77.9 for Companion A v3 and 48.2 for Companion B v3 - between a
third and a half of the text block - with 44 / 154 / 159 / 26 words outside the frame and 3 / 13 / 5 / 2
Overfull \hbboxes. The cause was never a missing \raggedright: it was unbreakable monospaced material (long
identifiers, hex digests, URLs, and the 142-character arithmetic identity cells of `tau_by_year_2017edition`)
inside fixed-width tables. The fix is a solving stage (`revision/v7/tablekit_v2.py`) that picks a font and gap
per table from six steps and builds penalty structure in the two units that matter - 1.85 mm per character
inside \texttt{}, 1.95 mm inside math, 1.60 mm for ordinary text - with size and padding carried inside each
column's `>{}` and gaps as `@{\hspace{..pt}}` glue; a bare `\small` or a `\tabcolsep` line between
`\begin{longtable}` and `\toprule` is a misplaced `\noalign`. URLs break at `/` and `_`; the identity cells
became two aligned displays. All four now report 0 overhang, 0 overfull, 0 words outside the media box, with
longtable widths inside 159.2 mm on every page (the tightest at 0.00 mm of slack) and no underfull \vbox
anywhere. Pages: 57 / 19 / 10 / 8.

**The converter was showing.** The v12 supplementary PDF printed 34 literal `\S` sequences, 83 unpaired `$`
characters and `\textperiodcentered{}` or `$\cdot$` inside 15 headings; the article printed `\S{}` twice; the
Companions' `.tex` headers printed "v12 of the supplementary" and sentences about the deposit; `Ø` in prose
raised a missing-character warning because `\O` is not in `cmmi10`. The pattern is one rule: text that the
converter escapes - code spans, whole heading lines, TeX headers - must be ASCII prose, never TeX. Spelling
Unicode into those registers with commands fixes the source file and breaks the print. So headings and code
spans are now spelled (`Sec.`, `-`, `ell`, `partial`, `B_dot`), math forms are used only in prose, and the four
headers state what the file is and how it was typeset. `verify_v42_build.py` reads each PDF and asserts both
halves: no raw-TeX token survives, and the section signs still count 33 + 1.

**Framing.** Eight article passages and four elsewhere were re-anchored so that no sentence claims an
institutional or prescriptive predicate the arithmetic does not earn: the abstract's opener and closer, a new
§1.1 passage separating period from half-life from residence time from time constant and newton-metres of work
from newton-metres of torque ("the promotion is inferential, not arithmetical"), the exhibit comparison
(conventions and poolability, not adequacy), the reconciliation rule (what this pair satisfies, not what a
record should be), the certification paragraph and the recomputation-equals-recomputation claim (one object, two
predicates), the ledger-to-standard mapping and the `check()` lemma (exhibited, not argued), the 2022 exhibit
(a numerical illustration of the criterion), and the row-status wording. Three passages of construction chatter
were cut, including the paragraph explaining why the two NFA tables sit where they sit, and every "submitted
with this article" was checked against what actually exists. Net word change +271 across the four files; no
quantity and no numeral disappeared, which the gate proves by scanning every removed span for unexplained
decimals.

**Deposit.** `code_v3/` regenerates the two exhibit scripts' headers and run lines, rewrites
`outputs.txt` (47 numeric lines, identical to the deposited record's), and adds a `MANIFEST.md` giving run
command, sizes, sha256, environment (CPython 3.11, pandas 2.2.3, numpy 1.26.4, pulp 2.8.0) and the limit that
no script can embed a DOI because none reads a file or writes anything. `analysis/nfa_tau/` gains a
reader-revised README (`README_v2.md`, shipped as `README.md` in the archive; the earlier file stays as
history) and a `source/MANIFEST.md` that is the single provenance document for the two edition tables:
retrieval commands, sizes, sha256 of the bytes as read, the licence check performed on the day (the dataset
records carry no licence field, so the tables are not redistributed by us), the recorded request for a
2022-vintage component table and the answer, and the arithmetic identity a reader can re-do. The whole thing
ships as `paper3_supplementary_package_v1.zip` (1.10 MB, 34 files, `MANIFEST.sha256` verifying for all of
them), whose README says what the supplementary is - the checking half of the pair, sections S1 to S17, not a
second argument - and separates the exhibit bundle from the analysis record and from the four papers.

**The split, re-measured on this line.** `review/split_graph_v1.py` against the v41 and v42 articles
(`review/split_graph_v42.txt`) returns the same graph for both: 63 statements, 21 distinct cross-section
section-pair edges, 61 citation instances, one strongly connected component of seven sections holding 59 of 63
labels, 21 of 21 mutually reachable pairs, 32 statements cited away from home. A clean split needs 0 of 21. The
conclusion first reached on v38's graph stands unchanged on this line, and the three zero-statement sections (1,
8, 11) remain the only demotion candidates. So the corpus stays as it is: one article, one supplementary, two
companions in their own frames.

Register: `review/tone_scan_v1.py` on the four v42 sources plus the two shipped MANIFEST-style files returns
0 in every manuscript file, 3 in the analysis record, all three being the noun "the run" in a file whose
subject is a run and all three present identically in the frozen v1 of that file
(`review/tone_scan_v42.txt`). Verification is `revision/v7/verify_v42_build.py`, eleven groups, ending
`ALL CHECKS PASS`, and it re-runs the four older gates as its last group. The v41 line and the frozen `code/`
directory are untouched; `revisions_v42_formal_log.json` reverses to v41's bytes exactly.
