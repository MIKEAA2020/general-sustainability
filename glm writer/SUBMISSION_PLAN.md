# Submission Plan — All Nine Papers, Compressed Calendar (2026-08-30)

**Purpose.** The two external audits proposed a four-wave submission sequence spread over roughly six months (empirical papers first, the theory paper at month 3, methods papers at months 4–5, heavy mathematics at month 6+). The owner's instruction overrides the calendar: **submit all papers soon.** This plan compresses the sequence into a single three-week campaign while preserving everything the phased plan was protecting — citation independence, honest companion declarations, and the registered pre-submission obligations. The venue routing itself is unchanged (the adjudicated primaries and alternates of `research_program/paper_types_and_venues_decision.md` §4, re-examined and maintained in `PUBLICATION_STRATEGY_JOINT_EVALUATION.md` §4).

## 1. Why simultaneous preparation is sound

The two-layer edition architecture makes the nine submissions mutually independent by construction:

1. **The empirical papers are citation-closed.** E1–E4 were designed to be submittable independently of the core papers' editorial stage (the standing release protocol). Their journal-facing editions genericize every internal identifier, state the retention rule as each study's own preregistered design, and describe companions only as "companion studies under separate review" — never as citable literature.
2. **The core papers are standalone.** Each carries its own Minimal Working Realization of the canonical objects it needs (the series' designed anti-dependency discipline), so no referee needs any sibling paper to evaluate any submission.
3. **The identifier-resolution fork is resolved the right way.** The standing rule: identifiers resolve to published sibling anchors *if* the siblings are published, and genericize *if not*. Submitting everything now selects the genericize route — which these editions implement throughout. (When a sibling is later accepted, nothing needs rewriting: the genericized phrasings remain true.)
4. **Different papers to different journals.** There is no duplicate-submission issue: these are nine distinct articles going to nine distinct venues, with companion relationships declared honestly in each introduction.

The one real sequencing constraint the audits identified — building a citation network so later papers can cite earlier ones — is preserved at no calendar cost: the citations become possible *after* the first acceptances, and the monograph (the apparatus carrier) follows external scrutiny of the principal papers exactly as the standing architecture requires.

## 2. The three-week campaign

**Week 1 — pre-flight (owner actions, mostly mechanical).**
- Insert author names, affiliations, and corresponding-author details into the nine title pages (the editions ship anonymized for double-anonymous review; Fisheries Research and ICES JMS are single-blind, so unblinding there is a formatting choice at submission).
- Prepare the anonymized artifact mirrors for double-anonymous venues: an anonymized copy of the public repository containing each paper's protocols, frozen specification sheets, deterministic runners, and pinned outputs (the data-availability statements in the editions already reference them).
- Assemble Paper 2's electronic supplementary material: the complete proof expansion (≈27k words) from the internal edition, packaged as ESM for *Set-Valued and Variational Analysis* (the standing packaging decision; the journal-facing edition's proof summaries point to it).
- Run the registered independent line-by-line re-verification pass over the four Wave E papers (the standing pre-submission obligation; the deterministic rerun records — byte-identical outputs, pinned hashes — are committed and referenced in each paper's availability statement).
- Optional but recommended: the cross-toolchain rerun of the post-v1.0 fold/monodromy computations and both intervention legs (the manifest's environment-sensitivity note; immaterial to verdicts, but it closes the last reproducibility caveat).

**Week 1–2 — submit the four empirical papers** (they are the most immediately publishable and establish the empirical credibility the audits emphasized):
- E1 (cod forecast ladder) → *Fisheries Research* — research article.
- E2 (cod intervention) → *Fisheries Research* — short communication (submitted alongside E1; the venue explicitly welcomes companion short communications; the papers cross-declare each other neutrally).
- E3 (Edwards forecast ladder) → *Groundwater* — research article (the peer-reviewed groundwater-forecasting literature is now engaged: Daliakopoulos et al. 2005; Adamowski & Chan 2011; Makridakis et al. 2020; Ropelewski & Halpert 1986; Scanlon et al. 2003).
- E4 (Edwards intervention) → *Journal of Water Resources Planning and Management* — applied management analysis (drought-trigger literature engaged: Steinemann 2003; Scanlon et al. 2003; Watkins & McKinney 1997).

**Week 2–3 — submit the five core papers** (the theory dyad first, then the applications, per the standing release protocol's ordering within the same campaign):
- Paper 1 (typed architecture + separation theorem) → *Environmental Modelling & Software* — theory/methods article. Alternate if desk-rejected: *Ecological Modelling*, then *Ecological Economics* (with the doctrine-led positioning already in the v3 abstract).
- Paper 2 (theorem atlas) → *Set-Valued and Variational Analysis* — mathematics article with ESM proofs. Alternate: *Journal of Mathematical Analysis and Applications*.
- Paper 3 (material ledgers) → *Ecological Modelling* — methods/formal-framework article. Alternate: *Journal of Industrial Ecology*.
- Paper 4 (delay dynamics) → *Communications in Nonlinear Science and Numerical Simulation* — applied nonlinear-dynamics article. Alternates: *Nonlinear Dynamics*; *Journal of Economic Dynamics and Control*.
- Paper 5 (sampled governance) → *ICES Journal of Marine Science* — methodology + case study. Alternates: *Canadian Journal of Fisheries and Aquatic Sciences*; *Fisheries Research* (note: if E1/E2 are still in review there, P5's submission is still independent — different article — but the alternates avoid stacking three papers at one journal simultaneously).

**If any desk rejection occurs:** rotate to the listed alternate in the same week; the editions are venue-agnostic in structure (no venue-specific formatting is embedded beyond the "Prepared for submission to" line on the title page, which is a one-line change).

## 3. Per-paper readiness notes

| Paper | Status of this edition | Remaining owner actions before submit |
|---|---|---|
| Paper 1 (EMS) | Submission-ready; built from the journal-facing v3 with the final venue-pass items (roadmap §1.6, contribution statement, apparatus in Appendix A) | Author details; anonymized artifact mirror (EMS is single-blind — optional); confirm the public repository URL |
| Paper 2 (SVVA) | Submission-ready main text (~16k words, all 11 families, statement inventory in Appendix A) | **Assemble the ESM proof package** from the internal edition; author details |
| Paper 3 (Ecological Modelling) | Submission-ready (~14.9k words; conservation theorems, diagnostics, three application records, non-reduction boundary) | Author details; artifact mirror |
| Paper 4 (CNSNS) | Submission-ready (~18.5k words; interval-certified Hopf pair, certification hierarchy, nominal folds honestly labeled, conjecture register) | Author details; decide whether to run the optional cross-toolchain rerun (the edition states the current certification levels exactly) |
| Paper 5 (ICES JMS) | Submission-ready (~14.7k words; sample-and-hold model, 42-stock screen, cod case, falsification designs; nominal computational tier stated honestly) | Author details; optionally commit the screen code/outputs (or the edition's honest restatement stands, as it does now) |
| E1 (Fisheries Research) | Submission-ready (~4.8k words, 4 figures, 8 tables; negative certificates at first-class status; cod literature engaged: Hutchings & Myers 1994; Walters & Maguire 1996; Shelton & Healey 1999 — all verified) | Author details; independent re-verification pass (registered standing obligation) |
| E2 (Fisheries Research) | Submission-ready short communication (~2.3k words; the two-layer robust/certified discipline explicit) | Same as E1 |
| E3 (Groundwater) | Submission-ready (~4.4k words, 5 figures, 6 tables; groundwater-forecasting literature engaged with five verified references) | Author details; re-verification pass |
| E4 (JWRPM) | Submission-ready (~3.2k words; 3.3–16.2% and 50.6% supply results; robust vs certified layers never conflated) | Same as E3 |

## 4. The pre-flight checklist (run once per manuscript, before each submission)

1. **Jargon purge (Ctrl+F).** Verified 0 hits in all nine editions for: "Wave E", "R04", "R03", "A014", "general theory", "concordance", "row-verified", "batch-5", "second edition", "flagship", "E5", CC identifiers in body text (machine-checked by the edition pipeline; re-run `grep -ic` on the .md if edited).
2. **The standalone test.** Each introduction was written for a referee who has never heard of the programme; all notation is defined at first use; every acronym expanded. Re-read the abstract + introduction once before submitting.
3. **The proof check.** Every theorem in these editions carries its source-declared status (theorem / conditional theorem / conjecture / counterexample); Paper 4's folds remain nominal-tier by design; no claim was promoted. Verify no accidental "theorem" appears where the source said "conjecture" (spot-check the conjecture registers).
4. **The code link.** Each edition's data-availability statement names its data sources and artifact record concretely; for double-anonymous venues confirm the anonymized mirror is live; for single-blind venues the public repository link suffices.
5. **The one-sentence contribution statement** is on each title page; the roadmap paragraph closes each introduction.
6. **Cover letter.** Use the matching letter from `COVER_LETTERS.md` (adjust the editor name if the journal names one; add the competing-interests and funding statements required by the venue).

## 5. What this plan deliberately does not do

- It does not stagger the submissions by months; the audits' four-wave phasing was a risk-management suggestion, not a requirement, and the venue-pass obligations it protected (literature engagement, identifier resolution, independence) are discharged in these editions.
- It does not split Paper 2 or merge papers; the audits' split proposal rested on premises verified false against the committed artifacts (the atlas is ≈15.9k words across 11 families, not a 100-page 12-family monolith), and the SVVA no-split route is the programme's endorsed, re-examined decision.
- It does not touch any internal edition, ledger, register, or verification artifact; the two-layer architecture keeps the auditable record intact for the monograph and the review process.
- It does not promise acceptance: the honest negative certificates, conditional theorems, and nominal-tier labels are features of the corpus and are stated as such — the strategy is to let each paper find the referees who value exactly that discipline.
