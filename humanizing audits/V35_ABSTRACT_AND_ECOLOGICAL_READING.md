# P4 v35 — Abstract Below 260 Words, Meta-Commentary Removed, and the Ecological-Reading Merit Evaluation

**Round:** Task 91 (owner-directed, fresh PAT, redacted). **Date:** 2026-09-17.
**Owner directive (verbatim):** *"1- abstract should stay below 260 words 2- 'it has a plain name' is meta-commentary without scientific, pedagogical or expository substance. maintain brevity without sacrificing substance. 3- does the work merit additional genuine, non-decorative, non-superficial ecological insights?"*

**Deliverables of this round:**
- `arena agent 1/paper rewrites/paper4_delay_dynamics_v35.md` — the new version (v34 untouched).
- `arena agent 1/paper rewrites/latex/paper4_delay_dynamics_v35.tex` + `.pdf` — 44 pages (same as v34), three consecutive byte-identical tectonic builds (tex md5 `f1bdcd666baf6a0195fa33a7e0913d80`).
- `batch 7 (audits of agent arena 1 paper rewrites)/wave18/` — `make_v35.py` (five surgical edits + the md-level fail-loud battery), `build_latex_v18.py`, `check_pdf_v35.py`, `review_v35.py`, `logs/` (tectonic log, five rendered pages, four VLM records).
- This document.

---

## Part I — Items 1 and 2: the compressed abstract (and the meta-commentary rule applied generally)

### I.1 The word cap

The v34 abstract ran **560 journal words**. The v35 abstract runs **258** (verified three ways: the markdown source, the LaTeX abstract environment, and the rendered PDF text layer, all by the journal method — whitespace tokens containing an alphanumeric, hyphenated compounds one word, list/formatting artefacts counted). The cap holds with margin under any reasonable counter.

### I.2 What was kept — the substance ledger

Every load-bearing element of the v34 abstract survives, in compressed form:

| Element | v35 form |
|---|---|
| Positioning (ecological vs governance delay) | "Delays destabilise renewable-resource systems; those studied so far are ecological. This paper analyses the delay that sits elsewhere — **governance delay**, the lag from observed decline to institutional response." |
| The model | "A three-state model — harvested stock, filtered deficit memory, bounded effort —" |
| The two rules (bold labels kept; gemini's inline-contrast form replaces the numbered list, which the word cap could not afford) | "the **mobilising rule**, effort grows as more effort is deployed; and the **protective rule**, a quota-tracking law restoring harvest toward a cap." |
| Mobilising headline + subcriticality + interval certification + both delays + the window | "intermediate delay stabilises the equilibrium: two subcritical Hopf crossings, interval-certified near 3.7 and 150 yr, bound the delay window in which the lag itself stabilises the loop." |
| Protective headline | "the loop gain stays below one at the calibrated point: the equilibrium is exponentially stable at every delay — a no-Hopf theorem." |
| Cadence contrast + artefact warning + restabilisation + crossing type | "Under periodic review the two rules respond oppositely: annual protective review remains stable — its apparent 2.3-yr threshold is a discretisation artefact — while annual mobilising review is unstable, restabilising only above 6.5 yr through a Neimark–Sacker-type crossing." |
| Global numerics with certification honesty | "The attractor topology is five-regime: two folds certified at the discrete collocation level (continuum stages open), and a basin-boundary transition toward an unverified large-amplitude attractor." |
| Breadth / stock-agnosticism / three design coordinates | "The class is stock-agnostic: its design coordinates — rule sign, deployment delay, review cadence — carry to any periodically reviewed renewable-resource regime." |
| Cod timelines + the not-a-calibration clause | "Documented timelines occupy the same scales — northern cod ran from annual assessment with incremental response to the 1992 moratorium, then the 2024 reopening — grounding scales, not coefficients." |
| The design message + the second overturned default | "Institutional form and timing, not ecological lag, decide whether governance stabilises or destabilises the stock; more frequent assessment is not always safer — the review interval is a local spectral design parameter." |

All six abstract digit tokens (3.7, 150, 2.3, 6.5, 1992, 2024) are preserved — the v31→v35 numeric chain stays closed.

### I.3 What was cut — and why each cut loses no substance

1. **"It has a plain name: governance delay, …"** — the owner-flagged meta-commentary. The concept name and its definition remain; only the announcement of the naming is gone.
2. **"The message of the paper is stated plainly."** — v33's own announcement sentence, cut under the same rule (pure meta; the message itself follows immediately and is kept verbatim-compressed).
3. **"The regime record is collected in one display:"** (§9.2) — an announcement sentence; the table's header (Regime | Delay range | Attractor record) is self-describing. The table itself is untouched.
4. **Glosses that the keywords and body already carry**: the Hopf-crossing definition ("oscillations are born"), the sample-and-hold parenthetical, "the sampled-review analogue of a Hopf transition", "a setting that shapes the eigenvalues which decide local stability". Each term remains defined at first body use (Sections 5.1, 2, 8).
5. **Duplicated scale colour**: "a few years to well over a century in the examples studied" — the certified values 3.7 and 150 yr state the same scale exactly.
6. **The numbered-list formatting** of the two rules (inline bold labels replace it) and "thirty-two years later" (the 1992→2024 dates state it).

### I.4 Machine-verified containment (owner item 2's "no substance sacrificed")

`wave18/review_v35.py` (ALL CHECKS PASS): every math span of v35 is byte-identical to a v34 span (empty whitelist) and every one of v34's 1,427 span occurrences survives; the numeric multiset is a superset of v34's with **zero losses** and the single declared new value 11.9 (the Discussion renumber); the heading skeleton is v34's plus exactly one insertion and two renumbers; title, keywords, references (36 entries, frozen since v32), data availability, competing interest, supplementary, and the figure block are byte-identical; the v31/v32/v33 content needles all survive (14 + 14 + the style battery minus the two abstract-only markers that the compression replaced with their surviving equivalents); all prior versions' md+tex checksums unchanged.

---

## Part II — Item 3: does the work merit additional genuine, non-decorative, non-superficial ecological insights?

### II.1 The verdict

**Yes — but only in one specific form: a consolidation of the paper's own already-registered ecological records into explicit insights. No new ecological computation, archetype, or empirical claim is merited.** The reasons, honestly stated:

**What the paper already certifies ecologically** (and therefore does not need added): the delayed-recruitment system with its life-history locus (§7.3), the cohort-cycle ground truth (§7.4), the M3-LC harvest-channel excursion records and fixed-demand experiment (§9.3), the Droop nutrient–quota variant's window invariance (§9.3), and the MPF intermittency records (§9.3, S11). This is substantial ecological content — but it is *registered as records*, distributed across three technical sections, and never consolidated as ecological insight. An ecologist or editor currently has to mine §7.3, §7.4 and §9.3 to see the ecological profile of the mechanism.

**Why consolidation is genuine and non-superficial**: each consolidated finding states a non-obvious relation *among* registered facts that constrains empirical prediction — which life histories are exposed (and why the selection is double), which delays generate which cycles, which extraction forms collapse faster, and which kinds of ecology can and cannot widen the instability window. None of this is illustration or decoration; each is a falsifiable-relevant claim assembled from the paper's own certified numbers.

**Why nothing beyond consolidation is merited**:
- *New ecological computations* (stochasticity, spatial structure, multispecies) would be new science requiring its own certification campaign — the paper's own limitations (§11.8) and open-problem register already bound this honestly.
- *Archetype mappings* (anchoveta, haddock, orange roughy, …) are exactly the failure mode the Task-89 audits exposed in gemini's outputs: invented, unverifiable, and decorative. Rejected — and still enforced by the zero-hit rejection scanner.
- *Importing the companion empirical record* (P5's 30+ system search, the stage-analysis archive beyond what §7 already registers) would duplicate the companion's own subject matter — the redundancy boundary recorded in the Task-87 round.
- *An r-range editorial* like gemini's "small pelagics r ∈ [0.2, 0.8]" invents a bound the paper never certified; the registered statement is the locus rg ≈ 1.5–1.6 with its four bands.

### II.2 The implementation: Discussion §11.7 "The ecological reading"

A new subsection (v35) with four findings, every number and math span reused verbatim from the registered records (the span check enforces byte-identity):

1. **The exposed life histories are doubly selected.** The two-crossing structure survives the maturation delay only on the product locus rg ≈ 1.5–1.6 (§7.3), moving to slower stocks with longer maturation (g = 10 near r ≈ 0.08); selection acts a second time through the institutional delay, since the band τ-windows grow with the maturation lag — (1.6, 3.5) yr at g = 1, (2.6, 7.8) yr at g = 2, (9.9, 20.3) yr at g = 5 — and only the g = 2 window lies inside the documented 2–13 yr governance-lag distribution. Fast-maturing small pelagics are therefore the *predicted* exposed class, not an illustrative example; at the slow end the question inverts (the 358.8-yr cohort cycle makes the institutional-delay question moot).
2. **Ecological delay and institutional delay sit in different compartments and produce different cycles.** Maturation delay in the stock equation and deficit signal; institutional delay only in the effort equation (§7.1); cohort cycles track the life history (~20 yr at r = 0.5, 358.8 yr at r = 0.02) while loop cycles track the deployed response (16.96 yr at r = 0.3); with both present, the institutional window survives on top of the ecological one (τ ≈ 10 carries the ~17-yr cycle; τ ≈ 21 is stable).
3. **The form of extraction is ecological even where the local mathematics is not.** The two M3-LC harvest channels leave the equilibrium, Jacobian, characteristic equation, and both Hopf points identical (§2.3), yet the transients separate (N ≈ 33 under pure culling vs N ≈ 10 under pure suppression at τ = 115 yr; first hit of N = 0 near time 158 vs asymptotic approach, N < 1 near time 430). Local spectra cannot see the extraction form; the excursion record can.
4. **Growth-coupled ecology cannot widen the window.** The Droop variant leaves the r-window unchanged (upper edge ≤ 0.023 yr⁻¹ at η = 0.914; no Hopf crossing at any r ≥ 0.2) because a growth-coupled pool self-relaxes at exactly r; the only r-independent slow pool in the registered family is the working core's ω_A-type exchange — decoupled storage, not growth-coupled ecology, is what can slow the loop.

The subsection closes with its own scope guard: each reading consolidates records registered in Sections 2.3, 7, and 9.3; none adds a computation, an archetype, or a calibration; the limitations of Section 11.8 apply unchanged. The §1.3 Organization sentence now lists the ecological reading; the Discussion renumbered Limitations → 11.8 and Open problems → 11.9 (verified: zero live cross-references to the old numbers existed).

### II.3 What this deliberately does not do

No restructuring of the paper's skeleton beyond the one subsection insertion; no new references; no archetype vocabulary (rejection-scanned); no empirical claim beyond the registered records; no change to any theorem, proof, number, interval, table, or certification-tier statement (all machine-verified as surviving byte-identically).

---

## Part III — Error-free-delivery evidence

| Gate | Result |
|---|---|
| Build determinism | three consecutive `build_latex_v18.py` runs byte-identical (tex md5 `f1bdcd666baf6a0195fa33a7e0913d80`); idempotent assembly asserted in-script |
| Compile | tectonic return 0; zero TeX errors; zero missing glyphs; pure-ASCII tex; 44 pages (v34: 44); 484 KB; overfull 10 — the same count as v33/v34 |
| md↔tex parity | numeric-token multiset exactly equal; no markdown word lost; no unexpected extra LaTeX words |
| Abstract cap | 258 journal words at md, tex, and rendered-text level (cap 259); all six digit tokens; both bold rule labels; governance-delay definition |
| PDF structural checks (PyMuPDF, ligature- and hyphen-normalised) | 10 page-1 needles + 13 pages-1–2 needles + 58 body needles; exactly the two URI annotations (orcid.org, mailto:); Figure 1 caption exactly once; rejection scan on the rendered text: **0 hits** (now including "plain name", "stated plainly", "is collected in one display") |
| Back matter | Declarations with the AI declaration as the final subsection, verbatim |
| VLM verification (glm-5v-turbo, 4 records in `wave18/logs/`) | page 1 — title, byline, blue ORCID/email links, date, bold "governance delay" with its definition, both rule labels, keywords on page 1, visibly compact abstract, no defects; pages 40–41 — the ecological reading ((i)–(iii) on p40, (iv) + the closing scope guard + the 11.8 Limitations heading on p41; Greek notation and values render correctly; no defects); page 44 — Declarations with the AI declaration last and verbatim, no defects |
| Version discipline | v31/v32/v33/v34 md+tex checksums unchanged (recorded in `review_v35.py` §E4); new files only |

## Part IV — Residuals, honestly stated

1. The pagination shift: the abstract now ends on page 1 (keywords on page 1), §1 begins on page 1, and downstream content moves up roughly one page relative to v34 (regime table p28, ecological reading pp40–41, declarations end p44; total pages unchanged at 44).
2. The two-rule contrast in the abstract is now inline-bold rather than a numbered list — the word cap forced the choice; the numbered/bulleted contrast devices survive in §11.1 and §11.3.
3. The v33-only style markers "The delay studied in this paper sits in a different place" and "oscillations are born" no longer appear (they were abstract-only phrasings); their body equivalents ("sits elsewhere" §1.1, "oscillatory dynamics are born" §5.1) are needle-verified.
4. "11.8" gains one occurrence (the new §11.7 closing cross-reference to Limitations) — a duplication, not a loss; the only new numeric value in the entire version chain is the renumber token 11.9.
5. The blocked metadata item (DOI substitution for the remaining references) remains blocked on the missing owner-supplied DOI list.

**Reproducibility:** `python3 wave18/make_v35.py && python3 build_latex_v18.py && python3 check_pdf_v35.py && python3 review_v35.py` — all four scripts deterministic and fail-loud.

**Status:** items 1 and 2 implemented and machine-verified; item 3 answered (verdict: consolidation-only, implemented) with the rejected alternatives recorded; v35 is the new latest version of paper 4; v34 and all prior versions untouched on disk and in history.
