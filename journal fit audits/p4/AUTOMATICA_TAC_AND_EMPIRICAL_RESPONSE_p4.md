# Empirical grounding + Automatica/TAC evaluation — Paper 4 (delay dynamics)

**Task (owner directive, 2026-09-16):** (1) search the repo and the web for empirical case studies and calibration, implementing them **only if highly merited and appealing to editors and reviewers**; (2) evaluate whether *Automatica* and *IEEE Transactions on Automatic Control* ("strong general results on delayed sampled-data systems") merit the **same or a separate publication**. English only; new versions only, never overwrite.

**Paper at directive time:** `paper4_delay_dynamics_v31.md` (Task 86 deliverable; 699 lines, 40 pp tex/pdf).
**Deliverable of this round:** `paper4_delay_dynamics_v32.md` + `.tex/.pdf` (new version; v31 untouched), built by `batch 7 (audits of agent arena 1 paper rewrites)/wave15/`, plus this evaluation record.

---

## Part A — Empirical case studies and calibration: search, evaluation, decision

### A.1 Repository search record

| Source searched | What it contains | Relevance |
| --- | --- | --- |
| `revised_articles/A011_periodic_review_corrected.tex` | The corpus's own empirical record: a structured field-case search across **more than 30 resource systems** (fisheries, aquaculture, groundwater, surface water, rangeland, wildlife harvest, forestry, produced-capital) under four eligibility criteria (responsive institutional feedback; independently dateable lag; no dominant competing driver; unit-level data) — **zero eligible cases**; a multiplicity-controlled Lomb–Scargle screen of **42 RAM Legacy v4.66 stocks** selected for annual review (no robust peak, low power, no controller-sign fields in RAM); anchovy-class (3–4 yr), sprat-class (6–12 yr), cod-class (null) sampled-review trajectory regions. | This is the companion sampled-governance paper's subject matter (P5 v26 carries it). Importing it into P4 wholesale would duplicate P5's contribution — the redundancy boundary for any empirical addition to P4. |
| `revised_articles/A014_northern_cod_revised.md` | Verified Northern cod (NAFO 2J3KL) governance-timeline facts reproduced from DFO SAR 2016/026: SSB 734.51 kt (1991) → 381.95 (1992) → 101.05 (1993) → 30.55 kt (1994); moratorium announced **2 July 1992**; renewed commercial fishery announced **26 June 2024** (Canadian TAC 18,000 t); plus Rose & Walters 2019 and Liermann & Hilborn 2001 references. | The canonical documented instance of institutional response delay at management scale — the "real governance timelines" the Qwen audit asked for. |
| `revised_articles/A012_delay_dynamics_corrected.tex` | P4's own source article — confirms the paper was always positioned as "an applied, registered family … not a new general bifurcation theorem". | Confirms the deliberate-un calibrated stance is original design, not an omission. |
| `arena agent 1/other documents/rerun_campaigns/stage_scan_recovered/stage_decomp_results.md` | Source of the "documented governance lags (2–8 yr)" claim; P4 v31 Section 7.3 already carries the "documented 2–13 yr governance-lag distribution". | P4 already had one documented-scale hook; the new subsection now cites its instances properly. |
| P2 `Automatica_routes` line (`latex/paper2_obstruction_calculus_v29…v42_Automatica_routes.tex`, `build_paper2_v29_automatica.py`, routes supplementary line, `paper2_v32_addendum.md`) | A full **separate** Automatica-formatted derivative line for Paper 2, including genuinely new theorems (e.g. the Helly sparse-witness proposition). | The corpus's own precedent for how a control venue is served: a separate derivative paper, never the main paper itself. Load-bearing for Part B. |
| P5 `NatSustain` derivative lines (`paper5_sampled_governance_v38–v47_NatSustain.tex`) | Venue-targeted derivatives for P5. | Confirms the corpus practice: venue derivatives are separate version lines. |

### A.2 Web search record (verification, 2026-09-16)

All four journal citations were verified against **Crossref** (bibliographic records fetched by DOI); the governance-timeline facts were verified against the corpus article A014 and public documents surfaced by search:

1. **Hutchings, J.A., Myers, R.A., 1994.** What can be learned from the collapse of a renewable resource? Atlantic cod, *Gadus morhua*, of Newfoundland and Labrador. Can. J. Fish. Aquat. Sci. **51(9), 2126–2146.** doi:10.1139/f94-214 — the canonical collapse attribution (overexploitation under sustained harvest pressure).
2. **Walters, C.J., Maguire, J.-J., 1996.** Lessons for stock assessment from the northern cod collapse. Rev. Fish Biol. Fish. **6, 125–137.** doi:10.1007/BF00182340 — the canonical assessment-and-response-failure chronology.
3. **Li, Y., Bence, J.R., Brenden, T.O., 2016.** The influence of stock assessment frequency on the achievement of fishery management objectives. N. Am. J. Fish. Manag. **36(4), 793–812.** doi:10.1080/02755947.2016.1167145 — "as assessments became less frequent, relative yields were reduced and the risk of stock depletion and interannual variation in yield increased."
4. **Peterson, C.D., Wilberg, M.J., Cortés, E., et al., 2022.** Effects of altered stock assessment frequency on the management of a large coastal shark. Mar. Coast. Fish. **14(5), e10221.** doi:10.1002/mcf2.10221 — agencies weighing multi-year assessment cycles; the caution against less frequent assessment.
5. **DFO, 2016** (SAR 2016/026) and **DFO, 2024** (26 June 2024 news release) — public documents; values as reproduced and verified in A014.

Also found and deliberately **not used**: the Library of Parliament background paper BP-313E (24 February 1992 "conservation ceiling", a 35% TAC reduction) — a real, documented incremental response event, but its bibliographic details could not be pinned to the same verification standard within this round, so the v32 subsection states the response-delay character at the level the four verified references support. It is recorded here as an available strengthening for a later version if the owner wants the February-1992 partial-response event cited explicitly.

### A.3 Merit evaluation and decision

| Candidate strengthening | Merit verdict | Reason |
| --- | --- | --- |
| Full case-study **calibration** of P4 to a named fishery | **Not merited** | The corpus's own structured search found **zero unconfounded eligible cases** (A011); the theorems are parameterisation-specific (registered Candidates A/B, calibrated-point statements); inventing coefficients would fabricate empirical grounding and contradict the paper's declared Limitation (i). Task 86's "blocked on owner-supplied material" status is confirmed as correct. |
| Wholesale import of A011/P5's case-search and spectral-screen record | **Not merited** | That record is the companion sampled-governance paper's contribution; duplicating it in P4 would create cross-paper redundancy and weaken both. |
| **Documented governance timelines** grounding (the Qwen audit's own fallback: "perhaps case-study calibration or **at least a detailed discussion of real governance timelines**"; ICES JMS: "discussion of actual management review cycles"; the sustainability strategy: "real-world governance examples") | **Highly merited — implemented in v32** | Real, citable, verified; grounds the paper's two timing coordinates (deployment delay, review cadence) at documented management scale; serves the sustainability, fisheries and broad venues jointly without touching any theorem; adds no calibration claim. |

### A.4 What v32 implements (14 surgical edit regions; +21/−0 lines; v31 byte-identical on disk)

1. **Abstract:** one documented-timelines sentence — the northern cod record (annual assessment, incremental response, the 1992 moratorium, the 2024 reopening) grounds the two timing coordinates "without calibrating any coefficient."
2. **Introduction 1.1:** the management-record grounding sentence at the behavioural-basis paragraph (Moxnes/Ostrom context) with the four new citations.
3. **Organization sentence:** the new Discussion theme named.
4. **Discussion 11.3 closing:** forward pointer to the new subsection.
5. **NEW Discussion 11.4 "Documented institutional timelines":** (i) the delay coordinate — northern cod SSB ≈735 kt (1991 assessment) → ≈31 kt (1994 assessment) under annual assessment cycles (DFO, 2016); moratorium 2 July 1992; reopening 26 June 2024, thirty-two years later (DFO, 2016, 2024); collapse attributed to overexploitation (Hutchings and Myers, 1994) with the assessment-and-response chronology as a management failure (Walters and Maguire, 1996); the record documents response delays of years and management-cycle decisions spanning decades at the scale of the paper's windows (3.7–150 yr; the Section 7.3 $g=2$ $\tau$-window inside the documented 2–13 yr governance-lag distribution); and it supplies the canonical instance of the inter-review depletion that Section 8's local spectral statements explicitly do not certify. (ii) the review-cadence coordinate — the assessment-frequency literature (Li, Bence, and Brenden, 2016; Peterson et al., 2022) treats the review interval as a managed design variable with measured yield/depletion-risk consequences: the empirical counterpart of $T_r$ as a local spectral design parameter, with a matching direction of caution. (iii) the scope guard — the timelines ground **scales, not coefficients**; no calibration; the institutional coefficients remain to be identified; the companion sampled-governance paper's zero-eligible-case search marks the empirical programme as prospective; nothing converts a theorem into a claim about a named institution.
6. Old 11.4–11.7 renumbered **11.5–11.8**; the one internal cross-reference re-pointed ("Section 11.5's first stated open task"); no live external reference to the old numbers (checked; supplementary S11.3 is an unrelated supplement section).
7. **Limitations (i):** the not-a-calibration clause.
8. **References:** six new entries (DFO 2016; DFO 2024; Hutchings & Myers 1994; Li, Bence & Brenden 2016; Peterson et al. 2022 — "et al." per the paper's 4+-author convention; Walters & Maguire 1996), alphabetically placed.

Deliberately **not** implemented: any numeric threshold, theorem statement, or model change; venue retitling (submission-time menu, per Task 86); the February-1992 35% event (A.2 above).

### A.5 Verification record (all fail-loud, all passing)

- **md level** (`wave15/make_v32.py`): every edit block matched verbatim exactly once; edit regions pairwise disjoint; **numeric discipline: v32 loses/reduces no frozen token of v31** (section renumber 11.4–11.8 exempted and separately verified: Discussion 11.1–11.8 in the expected order; the open-task cross-reference re-pointed), and **every new numeric token belongs to the declared empirical-record whitelist (25 tokens**: the documented dates 1991/1992/1994/1996/2016, the SSB values 735/31, and the volume/page/DOI tokens of the six new references, each mapped to its source in the script); v31 byte-identical on disk after the run; 15 diff hunks = the 14 declared regions.
- **tex level** (`wave15/build_latex_v15.py`): the wave-14 pipeline with every inherited check (numeric-token multiset exactly equal md↔tex; no markdown word lost; pure ASCII; figure count; emphasis-symptom scan; declaration relocation with the AI declaration as the final subsection; clickable ORCID/email; pinned date) **plus** 20 v32 content needles and a tex-level numeric-superset check against the v31 body (every frozen scientific token survives verbatim).
- **Build reproducibility:** three consecutive tectonic builds byte-identical (tex md5 `02d479c048…`), **42 pages** (v31: 40; +2 from the new content), 1 figure, 475 KB; overfull-hbox profile identical to v31 (the same ten pre-existing boxes, shifted by the inserted lines; none introduced by the new content); logs archived in `wave15/logs/`.
- **PDF structure (PyMuPDF):** byline/ORCID/email/date on page 1; exactly the two URI annotations (orcid.org, mailto:); the new subsection on p. 36 spanning to p. 37; organization sentence p. 4; new reference entries pp. 40–41; Declarations (Data availability → Declaration of competing interest → AI declaration, AI last) ending p. 42. (Extraction notes handled: line-wrap hyphenation, ff-ligature, and page-footer tokens.)
- **VLM verification:** page 1 (title; blue linked ORCID/email + date; the new abstract sentence transcribed **verbatim**; keywords verbatim; no defects); pages 2/4 (the intro management-record sentence and the organization sentence transcribed verbatim; math intact); pages 36–37 (subsection heading; the SSB sentence, the moratorium/reopening sentence, the Li/Peterson sentence, and the companion-paper fragment all transcribed **verbatim**; all six citation forms present; no defects); pages 40–41 (all six new reference entries transcribed verbatim with correct DOIs; alphabetical placement confirmed: Costantino→DFO→Diekmann, Hayes→Hutchings→Hutchinson, Kuznetsov→Li→Ludwig, Ostrom→Peterson→Scheffer, Scheffer→Walters→Zhang). The VLM once flagged a "truncated DOI" on p. 40 — **disproven objectively**: the glyph box of `doi:10.1139/f94-214` ends at x=275.3 pt, far inside the 523.3 pt text edge, and no word on the page violates the margin.

---

## Part B — Automatica and IEEE TAC: same or separate publication?

### B.1 Verdict

**Same publication: not merited.** P4 (any version, including v32) should not be submitted to Automatica or IEEE TAC.

**Separate publication: merited, conditionally — as a distinct follow-on research paper** that proves genuinely general theorems on delayed sampled-data feedback loops. This is a research-investment decision for the owner, not an editorial strengthening of P4; the corpus precedent (P2's `Automatica_routes` line) shows exactly what such a derivative looks like and what it costs (a separate version line with its own new theorems).

**Between Automatica and IEEE TAC: one venue only.** They are direct competitors for the same class of general results; the same derivative material cannot ethically target both (sequential resubmission after rejection aside, a same-time or split carving would be a dual-/salami-submission violation).

### B.2 Why the same publication is not merited

1. **Centre of mass.** P4 is an application-architecture paper: a specific gated stock–memory–effort loop with theorems at a registered parameterisation (loop gain 0.08011 < 1; crossings ≈3.7/150 yr; restabilising crossing 6.50–6.73 yr across schemes; the Candidate-A/B anchors). Automatica's author guide solicits "original high-quality contributions in all areas of systems and control interpreted in a broad sense" — the operative bar is a *control-theoretic* contribution; the Qwen audit's own assessment is decisive here: "it will care less about fisheries per se … if the contribution is mainly a specific fisheries governance model, it may be considered too applied for Automatica," and TAC is "even more control-theory oriented. You would need strong general results on delayed sampled-data systems."
2. **What is already general in P4 is thin against that bar.** The consistency limit $(M(T_r)-I)/T_r \to J_{\mathrm{cont}}$ (Theorem 8.1(iii)) is standard sampled-data knowledge (Åström and Wittenmark, 1997, already cited). The rank-one/DC-gain restabilisation argument ($T_r \to \infty$; the filter identity $L(0)=0$) is architecture-specific — it is a property of *this* loop's leaky-memory controller, not of a class. The no-Hopf theorem holds at the calibrated point of a specific quota law. The closed-form monodromies (Euler, exact held-measurement, native ZOH) are for this three-state hold structure. None is a theorem about a class of delayed sampled-data systems.
3. **The literature bar is mature.** Delayed sampled-data control is a settled, active field: Fridman's refined input-delay approach (Automatica 2010; ~1,400 citations by the search record), the discontinuous-Lyapunov-functional line, networked time-delay systems in TAC, H∞ sampled-data with multiple delays, and current (2024–2025) work on sampled-data control of time-delay nonlinear systems. A new paper there must advance that machinery or analyse a genuinely new class; Section 8 of P4 is a careful, honestly-tiered case analysis, not an advance in that machinery.
4. **Format.** IEEE CSS lists the TAC standard full paper at ~12 pages; P4 v32 is 42 pages. Automatica regular papers are expected to be concise. Fitting P4 to either means the wholesale machinery-to-SI transfer that Task 86 already evaluated and rejected (it weakens the mathematics venues and violates the joint criterion).
5. **Register mismatch.** P4's proved / interval-certified / numerical certification tiers — an asset at SIADS, JNLS, Nonlinearity, and the honest applied venues — read at TAC/Automatica as an incomplete general theory with numerical gaps ("the continuum off-grid residual stage and the continuous-delay lift remain open").

### B.3 Why a separate derivative is conditionally merited, and what it would have to contain

P4's Section 8 and its open-problem register contain a real seed of general results — the one statement in the paper that is already proved *qualitatively* and *scheme-independently*:

> as $T_r \to 0$ every consistent review scheme inherits the undelayed linearisation; as $T_r \to \infty$ the exact hold tends to a rank-one operator whose eigenvalue is the DC gain (which vanishes by the filter identity); hence **every consistent periodic-review scheme restabilises at some $T_r$; only the location is scheme-dependent** (quantified here: 6.50–6.73 yr across three schemes).

A separate Automatica/TAC paper would promote exactly this shape to a theorem about a **class**: e.g. strictly-proper stable scalar plant + leaky-memory (filtered deficit) controller + delayed effort loop with vanishing DC gain — (i) the rapid-review consistency limit; (ii) the long-review rank-one collapse and restabilisation-at-finite-$T_r$ theorem; (iii) scheme-dependence bounds on the crossing location; (iv) a general artefact theorem for explicit command-step discretisations (the 2.3-yr and 47.5-yr instances of P4 as calibrated examples of thresholds manufactured by the update, not the loop); optionally (v) the first Lyapunov coefficient of the exact-hold Neimark–Sacker crossing — which is already P4's own declared matching open computation. The paper's open-problem register carries the adjacent directions (an RFDE/hybrid transition-persistence analogue; a restricted delay-separation principle for modularly identified governance loops; an exergy-limited controller class).

**What it would cost:** genuinely new theorems with proofs for the declared class — new research, exactly as Task 86 recorded ("requires genuinely new theorems (general delayed sampled-data results), not editorial strengthening"). The corpus precedent is instructive: P2's `Automatica_routes` line (v29–v42) is a separate two-column Automatica-formatted derivative with its own supplementary line and *new results of its own* (e.g. the Helly sparse-witness proposition) — the main P2 was never itself offered to Automatica. That is what "separate publication" means in practice here, and P2 could do it because its obstruction calculus was already general theory; P4's Section 8 is not (B.2 item 2), so its derivative must first earn its generality.

### B.4 Recommendation

1. Submit P4 v32 to the venues of the Task 86 menu — the sustainability/broad legs (Nature Communications / PNAS / Proc B) are now materially stronger for the documented-timelines grounding; the fisheries legs (Fish and Fisheries / ICES JMS) get the assessment-frequency bridge; the mathematics legs are untouched.
2. If the owner wants an Automatica or IEEE TAC presence for this programme, commission it as a **separate** derivative-paper workstream with the B.3 theorem programme, in the P2-`Automatica_routes` pattern (new version line, new theorems, one venue chosen up front). Nothing in P4 v32 needs to wait on it.
3. Do not split P4 itself for the control venues: carving Section 8 out of P4 would orphan it from the model class that gives the sampled-data results their meaning, and would be salami slicing of a coherent paper.

---

## Files

- New: `arena agent 1/paper rewrites/paper4_delay_dynamics_v32.md`; `arena agent 1/paper rewrites/latex/paper4_delay_dynamics_v32.{tex,pdf}`; `batch 7 (audits of agent arena 1 paper rewrites)/wave15/{make_v32.py, build_latex_v15.py, logs/}`; this response.
- Untouched: v31 md/tex/pdf and all earlier versions; the Qwen audit file; A011/A014/A012 and all other repo sources (read-only for this task).
