# V39 round record — the retitle (Theoretical Ecology) and the DOI question

**Task 98, 2026-09-18.** Owner directive: "1- choose accurate, honest title,
appropriate to Theoretical ecology journal  2- which dois do u want? are they
on repo? https://zenodo.org/records/22554217". A PAT was supplied for the
push (in-memory only; redacted from every file, log and command echo; unset
immediately; rotation advised).

Directive 1 is a commission (the title choice, delegated to this agent under
the named venue); directive 2 is a question (answered below in Part II; it
changes no file).

---

## Part I — the retitle (directive 1)

### The chosen title

> **Governance delay and the stability of harvested stocks: mobilising and
> protective feedback rules, and the review interval as a design parameter**

21 words (the old title: 23). Implemented as `paper4_delay_dynamics_v39.md`
(exactly 2 lines differ from v38: the title line; the supplementary pointer,
because the accompanying file carries the title in three places and is
republished as `paper4_supplementary_v8.md`).

### The accuracy audit (every element is the paper's own phrase)

| Title element | Source in the manuscript | Verdict |
|---|---|---|
| "Governance delay" | the defined object of §1.1 ("**governance delay**, the lag between the institution's observation of a decline and the response that finally acts on it"); the abstract's second sentence | accurate, the paper's own term |
| "the stability of harvested stocks" | compresses the paper's actual subject — the local stability and attractor topology of the stock–memory–effort system (§1.1: "what this delay *does* to the stability of a harvested-stock system") | accurate compression |
| "mobilising and protective feedback rules" | the two effort laws' own adjectives (abstract: "the **mobilising rule** … the **protective rule**"; §1.2 "The sign separation"); "feedback" from the institutional-feedback loop that the paper analyses | accurate |
| "the review interval as a design parameter" | the abstract's own closing claim — "the review interval is a local spectral design parameter"; §12: "The review interval is a control variable" | accurate; the title form drops only the qualifier "local spectral", a conventional title compression, not an escalation (the qualifier and its certification scope remain in the abstract and body) |

### Why each dropped old-title element was dropped

- **"Delay-Induced Regime Change"** — the honest-title problem. The
  large-amplitude attractor is *unverified* (the paper's own word); the two
  folds are certified at the *discrete collocation* level with the continuum
  stages open; the capture onset is "a basin boundary, not a fold". "Regime
  change" as the headline claim would also borrow the empirical
  regime-shifts register (Carpenter 2011; Scheffer 2003/2009 — cited in the
  paper as literature, not as membership). The paper's own headline result is
  the stabilising window and the sign separation, not regime change.
- **"The Mobilising and Protective Channels of Institutional Feedback"** —
  compressed to "mobilising and protective feedback rules"; the "channels"
  terminology stays in the body where it is defined.
- **"and the Review Interval as Control"** — replaced by "as a design
  parameter", the abstract's own phrase. "As Control" is the control-theory
  register (and paper 2 occupies the Automatica routes in this portfolio);
  the management-ecology register fits the named venue. Note: the phrase
  "The Review Interval as Control" survives **legitimately** as §7's heading
  and is deliberately NOT banned.
- **"Harvested Stocks"** — kept (the paper's own recurring phrase; ecological
  vocabulary; no named fishery, matching the "grounds scales, not
  coefficients" cod discipline).

### Venue fit (Theoretical Ecology)

The venue's own house style includes full descriptive titles (the paper's
closest relative — Adamson & Hilker 2020, *Theoretical Ecology* 13, 425–434,
the delayed-knowledge modelling counterpart cited since v38 — carries a
20-word declarative title). The chosen form is topic-plus-design-clauses:
mechanism ("governance delay"), subject ("the stability of harvested
stocks"), the two analysed rule classes, and the design message. No
control-theory jargon in the title ("sample-and-hold", "monodromy",
"spectral" all absent); the certification-tier discipline stays in the body
(no "certified"/"proved" in the title).

### Candidates considered and rejected

1. *"Institutional delay, not ecological delay, determines stability in
   periodically reviewed harvested stocks"* — rejected: "determines"
   overclaims (shown on one declared model class, not in field institutions);
   also foregrounds the §9 ecological-delay contrast, which the paper
   deliberately analyses *within one frame* rather than opposing "in
   caricature" (its own words).
2. *"Intermediate governance delay can stabilise harvested stocks: …"* —
   rejected: foregrounds only the mobilising channel's window; the protective
   channel's no-Hopf theorem is the other half of the paper's headline, and
   the topic-style main clause is the only form that carries both honestly.
3. *"Governance delay and harvested-stock stability: response-law sign,
   deployment delay, and review cadence as design coordinates"* — rejected:
   "design coordinates" is §12's internal vocabulary; less readable than
   "design parameter" for the venue's audience.

---

## Part II — the DOI question (directive 2): "which dois do u want? are they
on repo?"

### The state of the reference list (v39 = v38's list, untouched this round)

36 reference entries; **7 carry verified DOIs** (Adamson & Hilker 2020;
Beretka & Vas 2020; Hocherman, Trop & Ghermandi 2025; Hutchings & Myers
1994; Li, Bence & Brenden 2016; Peterson et al. 2022; Walters & Maguire
1996 — the first three pinned by web search in Tasks 96/97, the last four
pinned against Crossref records in Task 87). **29 entries carry no DOI**,
in four verification classes:

| Class | Entries | DOI status |
|---|---|---|
| (a) modern journal articles (12) | Aiello & Freedman 1990; Carpenter et al. 2011; Church & Lessard 2022; Church & Queirolo 2024; Costantino et al. 1995; Engelborghs et al. 2002; Faria & Magalhães 1995; Gurney, Blythe & Nisbet 1980; Moxnes 1998; Scheffer & Carpenter 2003; Scheffer et al. 2009; Zhang, Shen & Chen 2013 | publisher-registered DOIs exist; each can be pinned by a Crossref lookup (volume/pages/title match) — the Task-87 precedent, one round |
| (b) pre-digital journal articles (4) | Ezekiel 1938 (Q. J. Econ.); Hayes 1950 (J. Lond. Math. Soc.); Hutchinson 1948 (Ann. N.Y. Acad. Sci.); Ludwig, Jones & Holling 1978 (J. Anim. Ecol.) | DOI existence uncertain (retro-registration varies by publisher); each needs a Crossref/JSTOR/publisher check; some may have no DOI at all |
| (c) books (11) | Åström & Wittenmark 1997; Cloud, Moore & Kearfott 2009; Diekmann et al. 1995; Guckenheimer & Holmes 1983; Halanay 1966; Hale & Verduyn Lunel 1993; Hassard et al. 1981; Kuang 1993; Kuznetsov 2004; Moore 1979; Ostrom 1990 | book-level DOIs exist for some publishers (Springer/SIAM/CUP); pre-1995 Academic Press / Prentice Hall books typically have none; each needs a publisher-page check; whether book DOIs are wanted at all is a style decision |
| (d) grey literature (2) | DFO 2016 (Sci. Advis. Rep. 2016/026); DFO 2024 (news release, 26 June 2024) | no DOI exists; cited by report number / date as now |

**Which DOIs I want** (the direct answer): strictly *none are required* —
Springer's Theoretical Ecology reference style permits DOI-less entries and
the current list is house-consistent. If the DOI-complete form is wanted,
the ones I would ask for are the **16 journal-article DOIs** (classes (a)+(b)),
each to be pinned by Crossref/publisher verification before insertion —
never guessed; optionally the book DOIs of class (c) that verifiably exist.
Class (d) has no DOIs to want.

### "Are they on repo?" — no, verified this round

- No reference-DOI registry for P4's bibliography exists anywhere in the
  repository. The only DOI registry ever present is the **nine companion-
  paper Zenodo DOIs** registered in the agent-2 ECOMOD revision at wave 13
  (22545740 P1, 22554177 P3, 22552616 P2, **22554217 P4**, 22554297 P5,
  22552060 E2, 22553609 E1, 22553311 E4, 22552680 E3) — those are the
  corpus's *own* deposits, used to replace anonymous "in review" companion
  placeholders in the other eight papers; P4 has no companion-citation
  entries, so none of them is a P4 bibliography reference.
- **The Zenodo record https://zenodo.org/records/22554217 is the paper's own
  archival deposit** (fetched and read this round): DOI
  `10.5281/zenodo.22554217`, published 2026-09-06, creator "Abaee, Amin",
  exactly three files (`graphical_abstract_p4.pdf`,
  `paper4_delay_dynamics_v30.pdf`, `paper4_supplementary_v4.md`), an empty
  related-identifiers field, and **no reference list or DOI list inside**.
- The paper's own deposit DOI is currently cited **nowhere** in the
  manuscript (0 hits for `10.5281` in the v39 md and the v8 supplement).

### The deposit-staleness flag (owner-side action recommended)

The Zenodo deposit is **stale relative to the shipped manuscript**: it holds
the v30 manuscript and the v4 supplement (the current round ships v39 and
supplement v8), and its registered metadata title is the now-retired old
title. The clean move, whenever the owner wants the deposit DOI cited (e.g.
in Data availability or the Supplementary material paragraph — a one-line
round on commission): first refresh the Zenodo record with the final files
(a new version carrying the new title; the owner controls the account), then
cite that DOI. Citing today's DOI would point readers at a superseded
version under a retired title — an accuracy problem, so it was not done
unilaterally.

### The three paths forward for the owner

1. **Paste the trusted DOI list** (any subset of the 29) — applied verbatim
   as v40, the wave-13 protocol (each entry substituted exactly once,
   anchored, never overwritten).
2. **Commission the Crossref-verified DOI round** — I pin each DOI against
   its Crossref/publisher record (volume/pages/title must match) and insert
   only the verified ones, as v40; the Task-87 precedent did exactly this
   for four references.
3. **Leave the references as they are** — valid for the venue.

---

## Part III — the implementation record (wave 22)

- **`paper4_delay_dynamics_v39.md`** — v38 + exactly 2 anchored edits (the
  title line; the supplementary pointer v7 → v8). Machine-verified: 1,473
  math spans multiset-equal; the abstract (258 journal words), keywords,
  declarations, Data availability, References block (36 entries,
  byte-identical — no reference touched), figure and heading skeleton
  byte-identical; content numerics change only by the pointer's version
  digit (+8, −7; both titles digit-free); 0 unresolved cross-references;
  the old title's fragments absent in every case form (4 new permanent
  regression gates at md/tex/rendered levels).
- **`paper4_supplementary_v8.md`** — v7 + exactly 3 anchored edits (the H1;
  the *Accompanies* line with the full new title; the opening subject
  phrase). S1–S12 structure, object labels, numerics, and all eight
  supplement→paper section references unchanged and resolving.
- **`latex/paper4_delay_dynamics_v39.tex` / `.pdf`** — built by
  `wave22/build_latex_v22.py` (the wave-19/20/21 battery inherited: the
  needle battery with the new title and v8-pointer gates; the 48-string
  rejection scanner; the tex-level resolver and section-order gate; the
  numeric discipline vs the v38 tex = the pointer digit only).
  **Three consecutive byte-identical tectonic builds** (tex md5
  `629a97ae7a92c4146f2be1ff4fd3f1fe`); 45 pages (v38: 45); overfull 10
  (inherited); PDF md5 `65971aae315f74065b02104d00d28cf8`; 486 KB.
  `check_pdf_v39.py`: 10 page-1
  needles (the new title rendered verbatim) + 90 body needles; spine order
  5<6<7<8<9; 2 URI annotations; 0 rejection hits over 47 rendered banned
  strings; the v8 pointer rendered with the stale v7 absent; AI declaration
  last; page-1 and declarations renders produced.
- **VLM verification (glm-5v):** page 1 — 5/5 (the new title exactly, byline
  with clickable ORCID/email, the pinned date, the abstract's opening, no
  rendering defects); the final declarations page — 4/4 (the v8 pointer in
  typewriter font with no v7 anywhere, the AI declaration last and verbatim,
  no defects).
- **The graphical abstract regenerated** (`wave22/make_ga_p4_v39.py` — the
  wave-10 generator with the two headline lines retitled; every panel,
  value and layout coordinate unchanged): byte-reproducible across two runs
  (pdf md5 `29ce7164cb6337e4f359398ce3642a49`; png
  `a0d361e97f5d349420e8d829e54e1fac`; tiff
  `a36f2ee5eaccd044193c00fe7bcb81ce`); VLM 3/3 (the new headline exactly,
  no cut-offs or overlaps, panels clean). In-place regeneration per the
  wave-11/12 asset precedent (git history preserves the old bytes).
- **`submission_zips/paper4_supplementary_v8.zip`** (sha256
  `6af7de2051f98271f3b6f2d7708ce470c0f3ed65ce1b298e3b02f838d1339846`;
  89 files): the v8 document + the code-and-records payload verified
  byte-identical file-by-file against the v7 package (79 payload files,
  sha256) + the updated README (the new title; the v39 manuscript
  checksums) + the regenerated MANIFEST.sha256 (verified against the
  extracted tree, all 89 files) + the v8 packaging refresh note; the
  2026-09-18 re-execution record stands for the unchanged payload bytes.
- **`wave22/review_v39.py`** — the A/B/C/D/E ledger, ALL CHECKS PASS:
  reconstruction gates (v39 = v38 + 2 edits; supp v8 = v7 + 3 edits);
  references frozen v32==…==v37 (36 lines) with v38 == v39 byte-identical
  (38 lines); prior checksums unchanged (v31–v38 md+tex, supp v5/v6/v7);
  the title gates (the new title is the md H1 and the tex \title argument;
  the old title absent from the md, the tex, and the rendered PDF text
  layer).

## Honest residuals

1. **The Zenodo deposit staleness** (Part II) — owner-side action; not
   repairable from this repository.
2. **The DOI round itself is not executed** — directive 2 was a question and
   is answered, not implemented; the three paths are on the table.
3. **The standing abstract-phrase decision** (Task 97's flag:
   "those studied so far are ecological" vs "ecological or informational",
   the 2-word cost 258→260 against the below-260 bound) — still with the
   owner; the abstract is byte-identical in v39.
4. The title in the **cover-letter / submission-strategy documents** for the
   venue (if any are later authored for P4) should quote the new title; no
   such document exists for P4 yet, so nothing else needed the retitle.
