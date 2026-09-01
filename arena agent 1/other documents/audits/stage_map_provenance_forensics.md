# Stage-Map Provenance Forensics — where the legacy bands came from, and where the code did not

Date: 2026-09-01. Scope: the question whether the P5 stage-map multiplier scan was ever built, and if so where its generating record went. Method: full-history clone of MIKEAA2020/general-sustainability (211 commits, main), pickaxe content searches, object inventory, and direct reading of the source-article chain. Every path cited below exists in HEAD unless noted.

## 1. Direct answers

**Was the stage-map scan built in this chat (the current agent sessions)?** No. The sessions from 2026-08-31 onward built the logistic hold-map crossing scans (wave 7), the four wave-E campaigns, and the turn-46 pre-registered two-stage reconstruction — a new labelled object that explicitly does not claim to be the original. The legacy bands (anchovy 3–4 yr, sprat 6–12 yr, cod convergence, slow-stock 30–50 yr) arrived in this chat already written in the unversioned P5 manuscript.

**Was it built in the earlier sessions that created the repo?** The repo's own record says the bands were produced before the repo existed, by a process whose generating artifacts were never committed. The bands entered the repository in its **first commit** (6ef8299, 2026-08-23, "Upload complete healthy research workspace from ecol extracted") as prose inside the source article `uploads/paper3_empirical.txt` (concordance id A011, "Periodic Review and Resource Governance: Sampled-Data Models, Spectral Screens, and Case Evidence") — the document P5 was later drafted from. No script, equation set, parameter table, trajectory file, or solver record for the stage variants appears in any of the 211 commits.

**Was it ever built at all?** Built-then-lost is the best-supported reading, with one residual alternative. See Section 4.

## 2. The evidence chain

### 2.1 The bands are prose in the source article, from the first commit

- `uploads/paper3_empirical.txt` (HEAD) contains the bands as "exploratory computational summaries". Its own words (line 185): *"The anchovy-, sprat-, cod-, and slow-stock calculations instead use delayed-recruitment variants, provisionally labelled SD-E-DR-AN, SD-E-DR-SP, SD-E-DR-CO, and SD-E-DR-SL… Because that complete stage registration is not present in the main-text model record, the values below are retained as exploratory computational summaries and are not attributed to SD-E-B3."*
- Line 292: *"To support reproduction, the computational supplement must register the complete delayed-recruitment equations, class-specific vectors, effort gating and signal map, initial histories, sampled-data solver, parameter grids, amplitude convention… Until the computational record is complete, the stage-output values have the exploratory status defined above rather than the status of reproducible numerical propositions."*
- The **only stage-specific parameters ever recorded anywhere** are line 189's continuous-delay anchors: maturation delay g and regeneration rate r, response regions near rg ≈ 1.5–1.6 — for g = 2 yr, r ∈ (0.77, 0.81) yr⁻¹ at η = 0.914 with a delay interval ≈ 2.6–7.8 yr; for g = 1 yr, r ∈ (1.565, 1.585) yr⁻¹ with a delay interval ≈ 1.6–3.5 yr; and for SD-E-DR-SL, r ∈ (0.01, 0.05) yr⁻¹ (line 199). No natural mortality, survival, steepness, state dimension, effort gate, initial history, or solver convention for the stage variants appears in the source.

### 2.2 The article says diagnostic outputs existed outside the repo

Line 195: *"The archived diagnostics indicate percent-scale biomass excursions and order-one effort excursions relative to equilibrium. The exact percentages are not used as effect-size estimates here because the available convention does not distinguish peak-to-peak range from half-range…"* — "archived diagnostics" is the article's own claim that computed outputs existed somewhere at writing time; nothing matching them is in the repository.

### 2.3 The earlier sessions verified and preserved exactly this status

- `research_program/article_011_periodic_review/evaluation_and_verification.md` (HEAD): "None of the reported simulation bands, spectral results, power estimates, or case calculations can be independently verified from the submitted file. The required delayed-recruitment equations, parameter vectors, code, histories, eligibility table… were not attached. The article itself acknowledges most of these gaps and appropriately labels the outputs exploratory." Section 14: "Valid but unverified from supplied files — sampled-review response regions; continuous-delay comparison regions; assessment-error robustness…"
- `worklog.md` (HEAD, Task 45, third complete source closure — A011): "The artifact-obligation rows (017–024) closed as REGISTERED OBLIGATIONS, not discharged artifacts (the source declares the computational record incomplete)". The closure's evidence witness was "the source's own exploratory-status discipline".
- The glm-writer journal edition (`glm writer/paper5_sampled_governance/manuscript_journal.md`, line 188) and `papers/paper5_sampled_governance/manuscript.md` repeat the same discipline; a grep for stage-equation fragments (M = 0., s_A, J_t) in the journal edition returns zero matches.
- `uploads/MODEL_REGISTRY.md` registers V-STAGE and V-STAGE-DELAY as incomplete objects: "Mean-field stage result or separate local extension… Local delayed Hopf open"; "Separate operator; not the one-box Erlang model".
- `revised_articles/A011_periodic_review_corrected.tex` — the corrected revision's changes touch other defects (hold/interpolation wording etc.); it adds no stage material.

### 2.4 The sibling stage article carries the same pattern with an explicit attestation

A022 ("Stage-Structured Harvest as the Core: Adult Take versus Juvenile Take", `uploads/paper_V_stage_harvest.txt`) is the continuous-delay stage companion. Its evaluation (`research_program/article_A022_stage_harvest/evaluation_and_verification.md`) records: *"By explicit user attestation, the numerical spectra and searched-set computations were verified in another workspace and are accepted at their exact source-stated status. Publication artifacts remain to be archived."* The A022 numerical table (adult-take Hopf at τ* ≈ 52.07 yr, period 269.4 yr, etc.) entered the repo the same way — computed elsewhere, attested, artifacts never archived.

### 2.5 Negative results of the forensic sweep

- Pickaxe (`git log -S`) for anchovy / sprat / slow-stock: first appearance is commit 6ef8299 (the first commit); every later hit is a prose document (manuscripts, audits, our own turn-46 CSV/scripts). "stage-map" as a term enters the record only in this chat's 2026-08-31 sync (our registry/audit language).
- All pathnames ever in history: the only stage-related code files are this chat's `campaign_p5_stage_reconstruction.py` (+ its five CSVs) and `campaign_e4_stage_occupancies.py` (the Edwards elevation campaign — unrelated). 151 code files exist across all history; none is a stage-map scan.
- `full-session-work.patch` and `wave-e-handoff.patch` exist as blobs in history: both contain zero stage terms (anchovy/sprat/slow-stock/DR-AN all absent).
- The content-addressed `file_archive/` holds an earlier TeX state of A011 (author "Anonymous", identical abstract prose) and a threshold registry for the continuous-delay Hopf pairs — neither contains stage-map material. (The local trimmed clone dropped file_archive in the turn-42 budget cleanup; GitHub retains it — nothing was lost by that deletion.)
- 211 commit messages: none claims a stage-map computation; the drafting commit (68f4eee, Task 52) describes Paper 5 as carrying the stage-structured windows as drafted content.

## 3. How the bands exist without the code — the mechanism

The bands were never committed to the repository in any form other than prose because the repository's first commit carried the **article**, not the **workspace** that produced it. The authoring process (an earlier session) summarized computed outputs — bands, peaks, excursion ranges — into manuscript prose, and the manuscript itself flagged that the generating registration was absent. The earlier sessions' evaluation and concordance layers then verified this self-declared incomplete status and preserved it ("exploratory computational summaries", "REGISTERED OBLIGATIONS, not discharged artifacts"). So the repository's record has always been: bands as prose, generating record absent, status exploratory — from commit 1 through every subsequent manuscript layer.

## 4. Verdict: built-then-lost vs never-built

**Built-then-lost is the best-supported reading.** Three independent repo-side indicators point to real prior computation: (i) the A011 article's own "archived diagnostics" phrasing — a claim that computed outputs existed at writing time; (ii) the A022 sibling's explicit user attestation that its numerical spectra "were verified in another workspace", with publication artifacts pending; (iii) the specificity and internal consistency of the bands (anchovy 3–4 with weak 2-yr response, sprat 6–12, cod [1,20] convergence, slow-stock 30–50 transitions, the 4/12 and 8/60 yr peaks, the 80–240% vs 1–2% excursion ordering) — the kind of output a trajectory-classification run produces, matching the article's stated method (long-horizon trajectories, tail amplitudes, multiple histories, step refinement).

**The residual alternative cannot be excluded from the repository alone:** the numbers may have been written by the authoring session without a committed computation (a manuscript-generation session producing computed-sounding numbers). The repository cannot adjudicate this, because the generating record was never in it. The one authority that can resolve it is the original author: the A011 article's line 292 specifies exactly what must be supplied (equations, class-specific vectors, gating, histories, solver, grids, amplitude convention, trajectories), and the A022 evaluation shows the author has previously attested such records for a sibling article.

**What is certain either way:** no cleanup, reset, or commit in the repository ever lost this record. It was never committed. The turn-42 budget deletion removed only a local trimmed clone's copy of `file_archive/`, which GitHub retains in full.

## 5. Consequences for the current work

1. The turn-46 reconstruction's standing is unchanged and correct: the original registration is unrecoverable from the repository; a new labelled, pre-registered reconstruction is the only legitimate route. Nothing in this forensic record contradicts P5 v5's presentation.
2. **New anchor available for a future pre-registered reconstruction:** A011 line 189's g/r windows (rg ≈ 1.5–1.6; g = 2 → r ∈ (0.77, 0.81); g = 1 → r ∈ (1.565, 1.585); slow-stock r ∈ (0.01, 0.05); η = 0.914) are the only original stage parameters on record. A new pre-registered deviation could parameterize the stage plant by maturation delay and regeneration rate rather than M/τ, with those windows as declared consistency targets — a closer reconstruction family than the turn-46 M/τ parameterization, still fully labelled and pre-registered.
3. The legacy bands' provenance is now documented to the finest level the repository permits. Any future claim about the stage windows can cite: first commit 6ef8299 → `uploads/paper3_empirical.txt` → lines 185/189/193–199/292 → A011 evaluation §6/§14 → worklog Task 45 closure → P5 lineage.

## 6. Extracted artifacts (workspace copies)

`audits/_scan_work/`: A011_original.txt, A011_revised.tex, A011_eval.md, A022_original.txt, A022_revised.tex, A022_eval.md, A022_inventory.md, model_registry_excerpt.md, worklog_excerpt.md.

## 7. UPDATE 2026-09-01 — the generating code has been recovered (user-provided batch)

The user recovered a batch of 13 unique files (15 attachments, two duplicate pairs) from the earlier authoring chats, including the stage-analysis scripts and results. See `audits/stage_code_recovery_report.md`. In short: (i) the continuous-delay stage scan WAS built — `stage_r_window.py`, `stage_tau0_decomposition.py`, `stage_robust_check.py`, `stage_decomp2.py`, results `stage_decomp_results.md` (2026-08-08) and `stage_hopf.json` — and a verified re-run of the verbatim scripts reproduces the recorded results at every anchor (g=0 base-window validation exact; slow-r cohort cycle P=358.7 yr vs 358.8; r=0.5/g=5 cohort cycle P=20 yr; institutional bands (0.28,0.33) exact; A022 Hopf table byte-identical). This closes the provenance of A011 line 189's continuous-delay g/r windows (rg ≈ 1.5–1.6) — the layer that was "built-then-lost" is now on file. (ii) The SAMPLED stage-map record (SD-E-DR-* T_r bands) remains without a generating script: the batch contains no sampled_governance.py, and the recovered readme's chat-2 transcript states it was never written/uploaded. The turn-46 pre-registered reconstruction stands as the only labelled record for the sampled stage operator. The stage analysis was continuous-time characteristic-root scans + RK4 verification — the DDE analogue of a multiplier scan — never a discrete review-map multiplier computation; the readme's own chat transcripts say so explicitly.
