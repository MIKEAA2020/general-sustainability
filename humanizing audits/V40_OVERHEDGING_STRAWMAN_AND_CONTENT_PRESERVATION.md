# v40 — the over-hedging / phantom-strawman cleanup, the content-preservation audit, the alignment verification, and the DOI question answered directly

- **Round:** Task 99, 2026-09-19. Owner directives (verbatim intent): (1) *answer directly, which dois do u want? dois of what papers? mine? someone elses?* — with the policy clarification: *companion papers will eventually be published, so it makes sense to reference them; earlier, superseded manuscript versions will never be published... no reference to them should be made*; (2) *strip the change-log, internal dialogue, and surrounding meta-commentary... no editorial, self-praise or self-commentary statements, or informal terms from chat history... scan for and remove all naive over-hedging (metaphor apology / "map is not the territory" type statements) while keeping legitimate scope statements... it should not reference phantom or naive strawman points or unpublished work... scan for both navigation/diary/hedging patterns and methodological self-description... scan for scientific as well as pedagogical and expository content; any lost or condensed content, anything from earlier versions or original upload missing in final version?*; (3) *are abstract, keywords, and individual sections fully aligned with latest manuscript? is there a supplementary? if so, is it fully aligned?*; (4) *point to final files for manuscript and supplementary in repo*.
- **Baseline:** `arena agent 1/paper rewrites/paper4_delay_dynamics_v39.md` (md5 `5ca3850f3dd3b22f917cc4b0e5dcd583`), `paper4_supplementary_v8.md` (md5 `20156536b537265f1220ce17646dc799`), the v39 tex/pdf (md5 `629a97ae7a92c4146f2be1ff4fd3f1fe` / 45 pp).
- **Deliverables:** `paper4_delay_dynamics_v40.md` + `latex/paper4_delay_dynamics_v40.tex/.pdf` (tex md5 `0ce11af0262a80b15a2a24bf1695254f`; 45 pp; three byte-identical tectonic builds); the supplementary package refreshed in place (`submission_zips/paper4_supplementary_v8.zip`, new sha256 `ed8e99679494e32e106c9af64587ab0ebabdac379c6850ce36b643cf00a776bd`); `batch 7 (audits of agent arena 1 paper rewrites)/wave23/` (the fail-loud pipeline); this record. v39 and all prior versions untouched on disk and in history.

---

## Part I — the DOI question, answered directly (directive 1)

**Someone else's papers.** The DOIs in question are those of the *published third-party references already cited in the manuscript's reference list* — not your papers, not the corpus, not any unpublished material. Concretely, of the 38 reference entries, 7 already carry verified DOIs (Adamson & Hilker 2020; Beretka & Vas 2020; Hocherman, Trop & Ghermandi 2025; Hutchings & Myers 1994; Li, Bence & Brenden 2016; Peterson et al. 2022; Walters & Maguire 1996); **the DOIs I would want are the 16 missing journal-article DOIs** — 12 modern journal articles (publisher-registered DOIs exist; each pinnable by a Crossref lookup: volume/pages/title match) and 4 pre-digital articles (Ezekiel 1938; Hayes 1950; Hutchinson 1948; Ludwig, Jones & Holling 1978 — retro-registration varies, each needs a check). The 11 books are a style decision (book DOIs exist for some publishers); the 2 DFO grey-literature records have no DOIs to want. **Strictly none are required** — Theoretical Ecology's reference style permits DOI-less entries and the current list is house-consistent. If the DOI-complete form is wanted, each insertion is Crossref/publisher-verified before use — never guessed.

**Your papers, under the clarified policy:**
- *Companion papers* — agreed, they will eventually be published and can then be referenced with their verified DOIs. Today the manuscript needs no companion reference entries: its 21 prose companion mentions (the material-ledger, scaffold, two-stage, and sampled-governance companions, one carrying the standard "(under review)" status form) are exactly the endorsed class, and the reference list itself carries no companion citations. When a companion is published, its citation becomes a commissioned one-line round.
- *Superseded manuscript versions* — agreed, never referenced; machine-verified this round: zero references to earlier versions exist in the paper or the supplement ("superseded" survives only as the variant-registry status label in Supplementary S4.3 — a technical status, not a manuscript reference).
- *The Zenodo record you supplied* (`https://zenodo.org/records/22554217`) — fetched and read in Task 98: it is **this paper's own archival deposit** (DOI 10.5281/zenodo.22554217, published 2026-09-06, three files: the v30-era manuscript, the v4-era supplement, the graphical abstract), stale by 10 manuscript and 4 supplement versions, its registered metadata still carrying the retired title, and its DOI cited nowhere in the manuscript. It is not a source of reference DOIs; the clean move remains an owner-side Zenodo refresh with the final files before that DOI is cited anywhere.

**Round decision:** the owner's message clarifies the policy and supplies no DOI list, so the reference round stays unexecuted and the list stands as-is (valid for the venue). The execution path remains: commission the Crossref-pinned round (the Task-87 precedent), or paste a trusted list; both are one-line-per-entry insertions.

---

## Part II — the artifact-cleanup round (directive 2): one removal, everything else already clean

The wave-23 scan battery (`wave23/scan_v40_round.py`, reproducible): eight artifact classes over the v39 md and the v8 supplement, every hit adjudicated.

### The one actionable site (removed in v40)

> §1.1 (md line 30): "... so institutional and ecological delay are analysed within one frame **rather than opposed in caricature**."

The trailing clause evokes an unnamed naive opposition that no cited source holds — a phantom strawman point under the owner's rule. It adds no content: the positive statement ("analysed within one frame") carries everything. **Provenance:** the clause entered at v31 (the journal-fit round) — the ORIGINAL upload never carried it — so its removal restores the original register rather than removing original content. The removal is a 5-word, digit-free, math-free, line-count-preserving anchored edit; "opposed in caricature", "in caricature", and the bare word "caricature" are now permanent banned strings at md, tex, and rendered level (51 banned strings total in the scanners).

### The classes that scanned clean (0 hits), with the adjudicated keeps

| Class | Result | Adjudications (kept, with reasons) |
|---|---|---|
| Over-hedging / metaphor apology | 0 hits (48 patterns) | The hen/eggs/apple passage (§1.1) presents the liquidation-channel metaphor with **no disclaimer of any kind** — the owner's "legit metaphor is fine" standard was already met; the orchard-type apology does not exist in this manuscript. "This is a sufficient-condition statement, not an empirical calibration" (§5.4) kept: a legitimate scope statement in the certification-honesty register. |
| Navigation / diary | 0 hits (21 patterns) | "Nicholson's blowflies revisited" is the cited paper's own title. |
| Methodological self-description | 0 hits (10 patterns) | Kept by adjudication: the two certification-honesty scope statements ("Every entry below is a record already stated in this section... collected in one table", §7; "Each reading consolidates records registered in Sections 2.3, 9, and 8.3; none adds a computation...", §11.7) — they scope what the table/readings claim, the paper's anti-overreach discipline; "threshold relocation" (×3) — dynamical-systems terminology; "version-robust/version-specific" — model-variant statements; "The mathematics of this section says two things" / "For this paper the record does two things" — plain topic sentences. |
| Editorial / self-praise | 0 hits (17 patterns) | The paper is fully impersonal: zero "we" anywhere. |
| Informal chat artifacts | 0 hits (17 patterns) | "two things" (×2) and "actually tested" (×1) adjudicated plain formal English; the apparent "oops" hit is the substring of "governance loops". |
| Earlier-version references | 0 manuscript-version references | "superseded" ×1 = the S4.3 variant-registry status label; "committed" absent since Task 97; no "earlier/previous version/draft" constructs. |
| Phantom / naive strawman | 0 hits after this round's removal | The caricature clause (above) was the sole site. |
| Companion references | 21 prose sites | The owner-endorsed class (companions will be published); the "(under review)" status form is the standard academic convention for the unpublished companion. |

---

## Part III — the content-preservation audit (directive 2, second half): nothing lost

The question: *any lost or condensed content, anything from earlier versions or original upload missing in final version?* Four independent machine checks (`wave23/scan_v40_round.py`, Part II), over the ORIGINAL upload (`paper4_delay_dynamics.md`) → v40 + supplementary v8:

1. **Object-level mapping — 16/16 survive.** Every named object of the original (Theorems 1–6, Propositions 1–7, Corollaries 1–3) exists in v40 under renumbering: Theorem 1→2.1, Corollary 1→2.1, Proposition 1 (Frozen-active-pool)→Lemma 2.1 (restated in the scaled-norm form, v2 era), Theorem 2→4.1, Corollary 2→4.1, Proposition 2→Remark 5.1 (conditional status), Proposition 3→5.1, Proposition 4→5.2, Corollary 3→5.1, Theorem 3→6.1, Proposition 5→6.1, Proposition 6→6.2, Theorem 4→Corollary 6.1 (honest reclassification), Theorem 5→7.1, Theorem 6→10.1, Proposition 7→Lemma 10.1. v40 adds Remark 7.1 and Proposition 7.1 (18 total).
2. **Rare-token coverage — 824 tokens, 36 absent, all adjudicated.** 29 morphological variants (content present in other form: destabilised/destabilises, attracting/attractor, nonnegative/nonnegativity, ...); "committed" (the Task-97 repository-speak removal); khiyar/lineage/preprint (the original's two placeholder references — "Gao, S., Zhang, Z., 2022 ... (Delay-harvesting lineage; representative of ...)" and "Khiyar, O., et al., 2026 ..." carried no bibliographic records — removed under never-guess-references, the citation site re-grounded on verified entries: Aiello & Freedman 1990, Kuang 1993, Zhang, Shen & Chen 2013, Li et al. 2016, Peterson et al. 2022); "gestation" (dropped with the placeholder citations at the re-grounded site; the literature statement survives).
3. **Numeric fates — every value survives, is superseded by a certified recomputation, or is a condensed duplicate.** The original's cruder values were replaced by the deposited, reproducible campaign records: the lower-fold brackets 5.574–5.587 → the Krawczyk enclosure [5.587236198689, 5.587236198691]; the upper-boundary brackets 148.125–148.438 → the capture onset [148.6, 149.5]; cycle records 25/21.7/322.9/314.3 → 24.91/19.94/322.60/308.16; the equilibrium 89.55/2.090 → 89.5256/2.0896; the gate floor 68.7 → 68.6. The Hopf ℓ₁ values (+5.75×10⁻⁵, +3.55×10⁻⁴), the Euler ρ = 1.00055, and the loop-gain peak 0.08011 survive verbatim. **Honestly recorded condensations:** the undelayed-cubic RH-violation arithmetic (λ³ + 0.2774λ² + 0.00056λ + 0.000213) is now stated qualitatively ("the product of the first two coefficients falls below the constant term") — the claim survives, the inline digits were a prose arithmetic check; the ℓ₁ and 1.00055 prose-summary echoes were deduplicated (each survives at least once). The original's *two-fold lower-boundary reading* ("a pair of nearby folds of distinct families") was **corrected** by the certified five-regime campaign (a single fold of one S-shaped branch) — a scientific correction with deposited records, not a loss.
4. **v30-baseline containment.** v30's math spans reach v40 with 5 occurrence-losses (the Lemma 2.1 restatement family, object-mapped above); v30's numeric occurrence-losses (35) all sit at the adjudicated recomputation sites. The v31→v40 chain itself is machine-frozen (references v32==...==v37 at 36 entries; v38==v39==v40 at 38; every prior checksum unchanged — `wave23/review_v40.py` check C).

**Verdict: no scientific, pedagogical, or expository content is missing from the original upload through v40.** Every difference is a survival, a certified supersession, a recorded correction, a deduplication, or a never-guess-references removal of placeholders.

---

## Part IV — the alignment verification (directive 3)

**Abstract — aligned.** Byte-identical from v36 through v40 (machine-frozen: `make_v40.py` gate 2h; `review_v40.py` A6): 258 journal words, rendered 258 (cap 259). Every load-bearing abstract claim was needle-verified against the body through the inherited battery (the frozen v32 claims + the v34/v35 device needles, re-run in `build_latex_v23.py` and `check_pdf_v40.py`): the 3.7/150-yr window, the no-Hopf theorem, the 2.3-yr artefact, the 6.5-yr restabilisation, the five-regime topology with the two discrete-collocation folds and the unverified large-amplitude attractor, the cod 1992/2024 scales, "more frequent assessment is not always safer", the design-parameter closing.

**Keywords — aligned.** Byte-identical since v36 (all nine terms defined or load-bearing in the body; "maturation delay; recruitment dynamics" grounded in §9).

**Individual sections — aligned.** The heading skeleton is byte-identical v39→v40 (gate 2d); the §1.3 Organization paragraph matches the v36 structure (verified in Task 95; untouched since); the cross-reference resolver reports **0 unresolved Section constructs**; all 132 section references resolve; the label counts hold (Theorem 7.1 ×11, Proposition 7.1 ×9, Remark 7.1 ×2). The v38/v39/v40 deltas (two reference insertions + citations; the retitle + pointer; the one-clause removal) touch no abstract-claimed or section-structural content.

**Supplementary — yes, and fully aligned.** `paper4_supplementary_v8.md` (S1–S12): carries the current title in all three places (H1, the *Accompanies* line, the opening subject phrase — Task 98, re-verified); all **eight** supplement→main-paper section references resolve against v40's headings (`review_v40.py` B4: 2.3, 5, 6, 5.1, 8.2, 8.3, 9, 10.4); the S12 statement-label mapping's targets all exist in v40 (B5); the mirror statements agree (B8); the supplement is byte-identical this round (B1–B3). The submission package `paper4_supplementary_v8.zip` is refreshed to name the v40 manuscript (Part VI).

---

## Part V — the final files (directive 4)

| Artifact | Repository path |
|---|---|
| **Manuscript (source of record)** | `arena agent 1/paper rewrites/paper4_delay_dynamics_v40.md` |
| **Manuscript (built LaTeX/PDF)** | `arena agent 1/paper rewrites/latex/paper4_delay_dynamics_v40.tex` / `.pdf` (45 pp; tex md5 `0ce11af0262a80b15a2a24bf1695254f`) |
| **Supplementary (document)** | `arena agent 1/paper rewrites/paper4_supplementary_v8.md` |
| **Supplementary (submission package)** | `arena agent 1/paper rewrites/submission_zips/paper4_supplementary_v8.zip` (91 entries; sha256 `ed8e99679494e32e106c9af64587ab0ebabdac379c6850ce36b643cf00a776bd`) |
| **Graphical abstract** | `arena agent 1/paper rewrites/graphical_abstracts/graphical_abstract_p4.{pdf,png,tiff}` (the Task-98 retitled headline) |

---

## Part VI — the implementation record (wave 23)

- **`make_v40.py`** — v39 + exactly 1 anchored edit (L30); ALL CHECKS PASS: 1,473 math spans multiset-equal; numerics unchanged (digit-free edit); word delta exactly {rather, than, opposed, in, caricature each −1}; frozen blocks (abstract/keywords/declarations/Data availability/References [38 entries]/figure/Supplementary paragraph) byte-identical; body byte-identical outside L30; the 51-string rejection list 0-hit; resolver 0 unresolved; supp v8 untouched with its eight refs resolving; idempotent; v39 unmodified.
- **`build_latex_v23.py`** — the wave-19/20/21/22 battery inherited + the wave-23 gates (the edited sentence's new form as a needle; "caricature" banned at md and tex level); three consecutive byte-identical tectonic builds (tex md5 `0ce11af0262a80b15a2a24bf1695254f`); 45 pages (v39: 45); overfull 10 inherited; pdf 486 KB (md5 `3d7f3c04680286581fba97c7d4bf1d28`).
- **`check_pdf_v40.py`** — 10 page-1 + 90 body needles; spine 5<6<7<8<9; 2 URI annotations; 0 rejection hits over 50 rendered banned strings (incl. the 3 phantom-strawman gates); the v8 pointer rendered, stale v7 absent; the wave-23 edit gate green (the new sentence form rendered on pdf page 2; "caricature" absent from the whole text layer); AI declaration last.
- **`review_v40.py`** — the A/B/C/D/E ledger ALL CHECKS PASS (A: reconstruction — v40 == v39 + the 1 declared edit; B: supplement v8 re-verified, unchanged; C: references frozen v32==...==v37 [36] with v38==v39==v40 [38], all prior checksums unchanged incl. v39 md/tex and supp v8; D: 51-string rejection 0-hit md+tex, 'if and only if' ×5, tex md5 == the three builds; E: the removed clause absent from md/tex/rendered, the new form present in all three, the Task-98 title gates re-verified).
- **`scan_v40_round.py`** — the round's own battery (Part I: the 8-class artifact scan with the adjudicated keeps; Part II: the 4-part content-preservation audit) — ALL CHECKS PASS, reproducible.
- **`refresh_package_v40.py`** — the supplementary package refreshed in place (the built-asset precedent): the README's Manuscript line advanced to the v40 checksums; the refresh note `verification/packaging_refresh_2026-09-19_v40.md` added; MANIFEST regenerated (90 entries); 88 payload files verified byte-identical; old zip sha256 `6af7de...` preserved in git history, new `ed8e99679494e32e106c9af64587ab0ebabdac379c6850ce36b643cf00a776bd`.
- **VLM verification** — page 1: 5/5 (the title verbatim, byline with clickable ORCID/email, pinned date, abstract opening, no defects); the edit-site page (pdf page 2): 5/5 (the sentence ends "...analysed within one frame." flowing into "Fisheries supply the motivating instance", the removed word absent, natural flow, the Adamson & Hilker citation in place, no defects); the final declarations page: 4/4 (Declarations structure, the AI declaration last and verbatim, the v8 pointer in typewriter font, no defects).

### Honest residuals

1. **The reference-DOI round is not executed** — directive 1 is a question, now answered directly (Part I); the execution awaits the owner's commission or trusted list.
2. **The Zenodo deposit staleness** — owner-side action (refresh the record with the final files before citing 10.5281/zenodo.22554217).
3. **The standing abstract-phrase decision** (Task 97's flag: "those studied so far are ecological" vs "ecological or informational" — the 2-word cost vs the below-260 bound) — still with the owner.
4. **The package README** now names v40; the graphical abstract's headline is unchanged (correct — the title did not change this round).
