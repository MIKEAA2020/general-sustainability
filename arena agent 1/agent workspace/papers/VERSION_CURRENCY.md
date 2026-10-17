# Version currency of the eleven papers — audited 2026-09-29

## Why this file exists

Paper 2 was assembled from `paper2_probabilistic_sufficiency_v9.tex` while v14 existed.
The user caught it. The check was then generalised to all eleven. **Three of the five
P2-group papers were built from stale sources.** This file records what was wrong, what
was corrected, and what remains open. No file was overwritten: each correction is a new
version.

## The correction

| my paper | source used | latest source | drift | words recovered | new labels |
|---|---|---|---|---|---|
| paper02 `psuff` | `_v9` | **`_v14`** | 5 versions | +641 | `rem:feedback-strict` |
| paper03 `comp`  | `_v9` | **`_v20`** | **11 versions** | **+1,967** | `prop:beliefcells`, `prop:redesign`, `fig:hierarchy`, `fig:trajectories` |
| paper05 `ebc`   | `_v9` | **`_v13`** | 4 versions | +540 | — |

Re-assembled as `paper02_..._v11.tex`, `paper03_..._v11.tex`, `paper05_..._v11.tex`.
**No label was dropped in any lineage**, so each new version is a content superset of the
old. The v10 files are retained.

## Verified NOT drifted

- **paper01 `obstr`** — source `fam/obstr_v57.tex`. The rewrites lineage
  (`paper2_obstruction_calculus_*`) stops at v56, so v57 is ahead of it. Current.
- **paper04 `minimax`** — `fam/minimax_v11.tex` and
  `paper rewrites/latex/minimax_dual_certificates_v12.tex` are **identical** (6,107 words,
  same labels, no Lean). Current.
- **paper07** — source `diffs/p5_v47.tex`. (`v47_blinded_NatSustain` is a blinded variant
  that deliberately drops `fig:cod`, `fig:rho-scan`, `fig:screen`.)
- **paper09 `arv`**, **paper10**, **paper11 `e1`** — sources match the latest available.

## What the stale versions were missing, substantively

Not cosmetic. The v9 -> v14 `psuff` gap included:

1. **A mathematical correction.** v14 distinguishes the feedback viable-set recursion
   `\mathcal{W}^{fb}_k` from the blind recursion `\mathcal{W}_k`, with
   `rem:feedback-strict` noting the inclusion is strict in general. My v10 conflated them.
2. **A repaired proof.** v10's converse for the value-one characterisation read "with
   deterministic observations the realized observation path is fixed by the declared
   sequence" — a hand-wave. v14 replaces it with a proper induction on `k`.
   (`psuff` v14 says the Lean support identity is machine-checked "on the repaired reading
   of Theorem `thm:support` recorded in Remark `rem:feedback-strict`.")
3. **The completed mechanized layer.**

## The mechanized layer — the largest thing the stale sources omitted

Three of the current sources carry a Lean 4 claim; **ten of my eleven papers carried no
Lean mention at all**, and none mentioned machine-checking.

- `comp_v20`: the Farkas core underlying the exact primal-dual witnesses is **proved** in
  Lean 4 (54 modules, 60 build jobs, no axioms, no admitted gaps); the soundness direction
  — the one the certificates use — from the ordered-field interface alone. The converse is
  not proved there and is not used.
- `ebc_v13`: Sections `hamming`-`deadline` formalized in Lean 4, no axioms, no admitted
  gaps, no computer-algebra oracle; derived from the ordered-field interface alone.
- `psuff_v14`: support identity, freeze count and its frozen value, and rationality of the
  α-vectors, machine-checked. **One bound remains cited rather than formalized**: the
  Sperner bound of `prop:antichain` (iii).

Papers 2, 3 and 5 now carry these claims.

## Open, and the biggest single finding

**Paper 1's central results are already machine-checked and the paper does not say so.**

`lean/Formalizations/P1_Obstruction.lean` — 29,054 characters, **58 theorem/lemma/def,
0 axioms, 0 `sorry`**, importing only `Formalizations.Prelude`. It declares
`post`, `possible`, `commonAdm`, `beliefSafe`, `preOp`, `Wk`, `preOp_mono`,
`Wk_antitone`, `Wk_descending`, `SafeUnderPi`, `finite_horizon_sound`, `tree_sound`,
`finite_horizon_complete`, `Blocked`, `blocked_iff`, `commonSafe`.

The mapping onto paper 1's labelled results is direct:

| Lean declaration | paper 1 result |
|---|---|
| `finite_horizon_sound` / `finite_horizon_complete` | `thm:finite-horizon` |
| `commonSafe`, `Blocked`, `blocked_iff` | `thm:common-action` |
| `Wk_antitone`, `Wk_descending` | `def:kernel` (the kernel iteration) |
| `preOp_mono` | `prop:monotone` |

Likewise `Minimax_Dual.lean` (13,427 chars, 26 declarations, 0 axioms, 0 `sorry`) sits
under paper 4, which also does not mention it.

For the top-journal bar — *substantial methodological development* — a machine-checked
soundness and completeness theorem for the paper's central recursion is about as strong an
asset as these papers have, and it is currently invisible in the two papers it belongs to.

**Not yet done, deliberately.** I have not added these claims to papers 1 and 4. Doing so
requires first confirming the modules actually build and that each named declaration means
what the mapping above assumes. Writing the claim before the check is exactly the failure
that produced the retracted "tension" argument.

## Caveat — RETRACTED

~~`P1_AssessmentSeparation_v5.lean` (paper 6) has 1 `sorry`, an admitted gap.~~

**This was a false positive and is retracted.** The single grep hit for `sorry` is line
108 of the file, which is a *comment* reading "Every theorem is fully proved; there are
no `sorry`s and no extra axioms." A grep hit is not evidence. The claim was made from an
unexamined grep, the same failure family as the retracted "tension" argument.

Corrected by the verification pass below: paper 6's module is clean.


---

## Verification pass on the Lean layer — 2026-09-29

Every mechanized claim above was **checked before being written into any paper**.

### Method

Lean 4.14.0 was installed (elan), the `lean/` project fetched from the remote
(`lakefile.toml` plus 67 modules) and built.

### Result 1: the project builds

`lake build` → **60/60 jobs, exit 0**. This matches the "54 modules, 60 build jobs"
figure the sources claim.

### Result 2: no admitted gaps, established three independent ways

1. **`#print axioms` on the named declarations** (the only reliable test — in Lean an
   unfinished proof surfaces as the axiom `sorryAx` in the footprint of every declaration
   depending on it):

   | declaration | axioms |
   |---|---|
   | `finite_horizon_sound` | none |
   | `finite_horizon_complete` | `Classical.choice` |
   | `tree_sound` | none |
   | `blocked_iff` | `propext`, `Classical.choice`, `Quot.sound` |
   | `Wk_antitone`, `Wk_descending`, `preOp_mono`, `commonSafe` | none |

   `sorryAx` appears nowhere. The three named axioms are Lean's standard classical
   axioms, not gaps.

2. **Comment-stripped source scan** over all of `Formalizations/`: **zero** `sorry`,
   `admit`, or `axiom` declarations. The only modifier found is `noncomputable` (20
   occurrences), which marks a definition as using classical choice and is not a gap.

3. **At scale**: 170 declarations of `P1_AssessmentSeparation_v5` checked —
   `sorryAx` count **0**; only `propext`, `Quot.sound`, `Classical.choice` appear.

### Result 3: scale of the layer

**1,237** theorem/lemma declarations across 61 modules, including 199 in
`P1_AssessmentSeparation_v5`, 33 in `P1_Obstruction` (plus the `HiddenMode` section),
and 21 in `Minimax_Dual`.

### Result 4: fidelity — the formalization does apply to paper 1 as it stands

The formalization's declared source of record is `paper2_obstruction_calculus_v53`;
paper 1 descends from `obstr_v57`. Comparing them: v53 has 73 labels, paper01 has 74,
**and the only difference is `worked-case`, added by me this session**. Nothing dropped,
and `thm:finite-horizon`, `def:kernel`, `thm:common-action`, `prop:monotone`,
`thm:static-complete`, `prop:selector` are present in both.

### Scope limits, recorded in the papers, not omitted

1. **The continuous-time results are NOT formalized.** The header of
   `P1_Obstruction.lean` says the Dini-derivative arguments, exit certificates and timing
   bounds "live in an analysis setting outside a dependency-free Lean layer." What is
   formalized is the discrete core: Section 3.1 (finite systems, backward recursion over
   beliefs), the Section 7 one-step characterization, the Section 3.2 common-action
   obstruction in discrete/infinite-horizon form, the Section 4.1 certification theory,
   the Farkas robustness margin, the hidden-mode conflict example, and kernel monotonicity.
2. **Completeness is with respect to policy trees, not stationary policies.**
   `finite_horizon_complete` returns a `PolicyTree`, a history-dependent object. Where a
   paper asserts a stationary policy suffices, that rests on the hand proof.

### Written

- `paper01_obstruction_calculus_v60.tex` — new subsection **3.8 Mechanized verification
  of the discrete core**, with the declaration-to-result table, the axiom evidence, and
  both scope limits.
- `paper04_minimax_dual_certificates_v13.tex` — new section **Mechanized verification**
  (inserted before References; that paper has no Conclusion section).

Neither claim was written before the checks above had run.

---

## Current Paper07/Paper08 lineage status — 2026-10-16 all-ref audit

This section supersedes the historical Paper07 line above for current version numbering; it does not rewrite the earlier audit conclusions for the other papers.

- The repository is `MIKEAA2020/general-sustainability`. All six remote branches, both tags, and both GitHub prereleases were checked. Immediately before this update, the latest existing standalone Paper07 edition was v52 on `e2-v3-source-year` (pre-release tip `fe1eabdc9ffb`, 2026-10-15); no branch, tag, or release contained Paper07 v53 or a higher Paper07 edition.
- The other branches contained older Paper5 sampled-governance material (up to v47 blinded on `main`/`lean-audit-v4`, and v46 on the E1 branches); `archive/paper3-v48-workspace` had no Paper07 candidate. The older `paper5_sampled_governance` name is a historical lineage path, not a newer Paper07 edition.
- The v53 standalone continuation is stored at `paper07_sampled_governance_v53/` under this directory, based on `paper07_sampled_governance_v52.tex`. Its complete source, supplementary information, analysis records, build artifacts, and audit are in that versioned package.
- Paper08 v48 remains the parallel combined manuscript at `paper08_governance_delay_v48.tex` with its existing PDF and supplementary files. It is preserved unchanged. `PAPER_MERGE_08_07.md` records the historical v46 merge; it is not an instruction to replace v48 or to merge v53.
- The repository has no Paper07-specific tag or release. This v53 update continues the existing `e2-v3-source-year` branch lineage; it does not move or renumber prior editions.

The detailed pre-publication branch/tag/release and split/merge audit, including hashes of the preserved v52/v48 artifacts, is retained in `paper07_sampled_governance_v53/VERSION_AUDIT_2026-10-16.md`.


---

## Paper07 v54 and the v52-to-v53 coverage crosswalk — 2026-10-16

A fresh check of all six remote branches, both tags, both GitHub prereleases, tree metadata, and this version-currency file was completed before assigning v54. The latest Paper07 before the decision was v53 at `556240fda8498d11efa8921b7aa5d469da2e9140` on `e2-v3-source-year`; no v54 or higher existed in any checked ref. The parallel Paper08 v48 remains unchanged.

Paper07 v54 is now a new standalone continuation at `paper07_sampled_governance_v54/` on `e2-v3-source-year`. It does not overwrite v52 or v53, alter Paper08 v48, or create a tag/release. The new version corrects stale Supplementary pointers, distinguishes the archived crossing-only sensitivity table from its full CSV record, restores a general AI-use disclosure, and adds bounded modelling implications rather than the unsupported policy prescriptions removed from v52.

`PAPER07_V52_TO_V53_COVERAGE_CROSSWALK.md` and the v54 package's `CROSSWALK_V52_TO_V53.md` record the content map. The v52 main PDF is 36 pages, but its final pages and source refer to a separately deposited Supplementary file; the source's closing inventory says S1–S10 while body citations extend through S13.3. No such SI file or the promised dimensionless identifiability chart was found in the audited repository refs. Therefore the crosswalk is complete for recovered material, not a claim of full equivalence to the missing historical SI.

The detailed fresh audit, including all branch tips, tag/release status, and the preservation decision, is in `paper07_sampled_governance_v54/VERSION_AUDIT_2026-10-16.md`.


---

## Paper09b v5 — conditional accounting revision (2026-10-16)

A fresh all-branch/tag scan found Paper09b v4 as the latest existing edition on `e2-v3-source-year`; no higher Paper09b edition was present on the checked refs, and the previously checked release inventory contained no paper-specific Paper09b asset. The v4 source and PDF are preserved. The new v5 is a separate path on the same branch. It distinguishes assessed SSB from DFO 2025 Table 1 reported total landings, carries unknown nonnegative `kappa`, shows both adjacent-year assignments, and limits contraction statements to the strict row-specific threshold condition. The v5 checker and five source extracts are in `paper09b_arv_certification_v5_src/`. Static source checks pass; compilation was not possible because no TeX engine is installed.


---

## Paper10 v54 — MCS 2026 and typed depletion indicators (2026-10-16)

All-branch/tag scan found v53 as the latest Paper10 before numbering; no v54 existed on checked refs. The v53 main source's internal header incorrectly read v52 (2026-09-30); v53 and its SI remain preserved, and v54 corrects metadata in a new edition. V54 distinguishes static reserve/production quotients, anomaly-trend extrapolations, frozen-rate local ratios, and model-conditioned barrier-hitting times; corrects G3P's scope as reference-period anomalies rather than absolute aquifer volume or index-well measurement; and refreshes phosphate values to USGS MCS 2026 (world snapshot 73,000,000/250,000 = 292 yr, not a forecast). Its source package includes the snapshot CSV and arithmetic checker. Static checks pass; no TeX engine was available, so no PDF is claimed.


---

## Paper08 v49 — scoped two-operator synthesis (2026-10-16)

The all-branch/tag scan found v48 as the latest Paper08; v48 is preserved. V49 keeps the merged continuous-delay and sampled-review study but corrects the abstract and cross-regime synthesis to distinguish a declared baseline parameterization from empirical calibration, to treat `tau` and `T_r` as distinct operators, and to state that the stock-agnostic model class does not establish cross-system transportability. Existing sensitivity results are made explicit in the abstract and the 42-stock and 32-system nulls are separated. The v49 supplementary companions carry forward v48 calculations without revision and include provenance notes. Static checks pass; no TeX engine was installed, so no compiled PDF is claimed.


---

## Paper10b v2 — J-17 scope and companion-citation update (2026-10-16)

All-ref scan found Paper10b v1 as the latest split edition. The same study appears as `paperE4_edwards_intervention_v16.tex` in the LaTeX lineage; v1 is the later split copy and adds the related-work section and bibliography, so v2 is based on v1. V2 updates the published forecast-companion status (Zenodo 22552680), classifies the realized-flux 7.55-ft score as a conditional diagnostic rather than a forecast, and scopes the 660-ft result to the annual-mean map and persistent drought floor rather than the live 10-day CPM implementation. Analysis code and data are stored under `comp/wave_e_edwards/`, not in a Paper10b-specific `push_src`. The frozen protocol is `wave_e_edwards/protocol_intervention.md` (also included in `arena agent 1/agent workspace/papers/paper09_cod_certification_v44_src/src/wave_e_edwards/protocol_intervention.md`). **Path correction (2026-10-18):** the v2 audit's `comp/wave_e_edwards/protocol_intervention.md` pointer is invalid; that path is absent from the checked refs. The historical v2 audit remains unchanged. Static checks pass; no TeX engine was available and no PDF is claimed.


---

## Paper10b v3 — post-freeze 660-ft coefficient sensitivity (2026-10-16)

The branch/tag scan found v2 as the latest Paper10b edition on `e2-v3-source-year` (base head `248e8b9f7969`); no Paper10b v3 existed on any of the six branch tips or two tag tips inspected. V3 is based on v2 and preserves v1/v2 unchanged. It adds a post-freeze extension of the existing 5,000-draw iid residual bootstrap at the 660-ft threshold, reports both 618-ft and 660-ft refit shares, and separates CPM from flat-60% in Table 7 because their bootstrap distributions differ. The coefficient theorem remains conditional on its fitted-map hypotheses; under UC-min, the zero-pump attractor is at or above 660 ft in 344/5,000 refits (6.88%), so the point-fit positive-margin premise is not coefficient-robust. The extension does not re-score frozen retention, recalculate viability kernels, evaluate the live 10-day CPM, or estimate real-world safety probabilities. Source/data/output package: `paper10b_edwards_aquifer_v3_src/`; full audit: `PAPER10B_V3_AUDIT_2026-10-16.md`. Static structure/cross-reference checks and deterministic reruns pass; no TeX engine was available, so no PDF is claimed. Release ZIP payloads were not unpacked.

---

## Paper11b/E3 v25 — same-study lineage and source audit (2026-10-16)

The pre-versioning all-ref scan found Paper11b v2 on `e2-v3-source-year` and same-study E3 v24/SI v2 on `edwards-framework-e1-audit-implementation`; Paper11b v2 is the recovered Edwards half of the older combined v61/v66 lineage. The current standalone line is E3 v25/SI v3, pushed to the E3 branch at `3b3b87b6858d`; its updated claim crosswalk and computational-source audit are at `e3/PAPER11B_E3_V24_V67_CLAIM_CROSSWALK_2026-10-16.md` (refresh commit `9f3a3842795d`). Paper11b v2 and Paper11 v67/SI S15–S22 remain preserved historical/complementary editions; no duplicate Paper11b v3 was made.

The lineage disposition separates the H1/H2 point-score gate from M2m's broader class clause; class demotion is not a point-gate failure. The realized-future-flux score is a conditional diagnostic, not a nowcast/forecast. The five-year result is specific to the tested J-17 rolling origins, not policy advice. Source audit: `paper11_forecasting_baselines_v67_src/work/edw` carries derived panels/results, while the full scripts and raw inputs are under root `wave_e_edwards/src/` and `wave_e_edwards/data/`; the broader protocol is `wave_e_edwards/protocol_pass2.md`, and `SPECIFICATION.md`/`SPECIFICATION_v2.md` record the separate M2m class disposition.

## Paper11b/E3 v26/SI v4 — current standalone Edwards line (2026-10-17)

The all-ref audit found E3 v25/SI v3 as the latest standalone Edwards version before this edition. E3 v26 and SI v4 are now published on `edwards-framework-e1-audit-implementation` (commit `2bdf39ff1c13357a44c48b5ed7385c9945aff0b5`) at the established paths:

- `e3/paperE3_edwards_forecast_ladder_v26.tex` / `.pdf` (remote source blob `b5dc7d44991713c0afe7d0e53ada3e4c0dbf2b91`; PDF blob `050306783274c8053a36172e31b283df5b27ce51`).
- `e3/paperE3_supplement_v4.tex` / `.pdf` (remote source blob `540aa14e1f10209aae870433f34b532960678b7e`; PDF blob `79fab734973e05ecdec66240b0b099a02ca4bb38`).

E3 v25 and published SI v3 are unchanged and byte-verified against their remote blobs (`3b9380c6c35ec077c5943e47303fdf4ea2950bc2` and `5d9e3362a5fbecf5a2f5b37ff3b60c9f220ec52c`). SI v4 fixes v3's `No counter 'none' defined` longtable compile failure without overwriting v3. The v26/v4 PDFs build to 10 and 8 pages; logs have no LaTeX errors, unresolved references/citations, or overfull boxes.

The dated E3 v24/SI v2 versus Paper11 v67/SI S15--S22 crosswalk remains preserved at `e3/PAPER11B_E3_V24_V67_CLAIM_CROSSWALK_2026-10-16.md`. The new v25/v68 alignment/build audit is `e3/PAPER11B_E3_V25_V68_ALIGNMENT_BUILD_AUDIT_2026-10-17.md`; the version scan is `e3/VERSION_AUDIT_2026-10-17_v26.md`. Paper11 v68 remains the current combined two-system edition on `main`; no Paper11 version was created for bookkeeping.


## 2026-10-17 source-only build refresh and Paper11 page-count check

The previous entries dated 2026-10-16 accurately recorded that no TeX engine was then available; this refresh supersedes their build-status statements without changing any versioned source. On `e2-v3-source-year` at audited head `1488e61f5c0e92452805ac9deaba6240d78d466f`, the source-only candidates were byte-checked against the branch, their remote figure dependencies located and staged, and builds run with the verified Tectonic 0.15.0 binary. The results and page-count evidence are in `papers/SOURCE_ONLY_EDITION_BUILD_AND_PAGECOUNT_AUDIT_2026-10-17.md`.

- **Paper10 v54 main/SI:** compiled and visually checked; 56/19 pages. The MCS 2026 arithmetic checker passes; the main has no layout warnings and the SI has only underfull boxes. PDFs and dated logs were published at the established v54 paths in commit `1616013fb8a94a390c59f17cbf188b39551f30c9`.
- **Paper08 v49, Paper09b v5, Paper10b v3:** all compile and their source/data checks pass where applicable, but no canonical PDF was published because visual checks found materially overlapping/clipped content. Their sources remain unchanged; no new version numbers were assigned.
- **Paper11 page count:** the current `papers/` v66 PDF is 60 pages; v67 is 49 pages and its SI is 35 pages; v68 remains 49 pages (36-page SI). The v66-to-v67 changelog maps substantial technical detail to SI S1--S24, consolidates duplicate sections, and withdraws an unsupported cross-system claim. The evidence does not support restoring content merely to recover 60 main-text pages.

Paper07 v54 already had its main/SI PDFs and logs and was not rebuilt. Paper11b v2 remains preserved as historical material and was not part of the active build batch. No existing source or edition was overwritten or deleted.

---

## Paper08 v50, Paper09b v6, and Paper10b v4 — layout successors (2026-10-17)

A fresh all-ref scan checked all six branches, both tags, and the two GitHub releases at `e2-v3-source-year` head `e8367e820cb75f3f609ac7b43c47b5b7d689ea87`. It found Paper08 v49, Paper09b v5, and Paper10b v3 as the latest editions; no v50/v6/v4 paths existed on the checked refs. The three base sources were byte-identical to their recorded remote blobs. The earlier editions remain preserved.

- **Paper08 v50** is a layout-only successor to v49. It replaces the overlapping interval table with readable point-value and certified-interval tables, reflows long equations/parameter tuples, and clarifies that both v49 supplementary companions are carried forward unchanged. The v50 PDF builds to 87 pages, with zero overfull boxes.
- **Paper09b v6** is a layout-only successor to v5. It reflows the conditional-accounting lemma and gives summary Table 3 a full-width, non-overlapping layout. The existing verifier passes; the PDF builds to 9 pages, with zero overfull boxes. The source continues to distinguish SSB from reported landings/catch, convert tonnes to kt, keep nonnegative `kappa` unknown, show both adjacent-year assignments, and state only the strict conditional `kappa < kappa*` certificate.
- **Paper10b v4** is a layout-only successor to v3. It makes both long EAA URLs breakable and renders the code filename/relative v3 package paths without clipping. The 5,000-draw verifier reproduces the unchanged v3 CSV outputs byte-for-byte; the PDF builds to 18 pages, with zero overfull boxes.

All three sources pass normalized exact-content comparisons after reverting only version/date, layout, and path-rendering edits. Tectonic 0.15.0 logs, per-paper changelogs/audits, PDFs, and a combined build audit accompany these editions. See `LAYOUT_SUCCESSOR_BUILD_AUDIT_2026-10-17.md` and `LAYOUT_SUCCESSOR_PUBLICATION_RECEIPT_2026-10-17.md` for the full build and remote-byte verification record.

The 17-file package was published on `e2-v3-source-year` in commit `5226a9bf5214fed4246409fe08ed65a1ed018f9d` (parent `e8367e820cb75f3f609ac7b43c47b5b7d689ea87`). Each remote Git blob was fetched and byte-verified against the local file; the previous v49/v5/v3 source blobs remain unchanged. The follow-up verification commit adds the publication receipt and this currency refresh.

---

## Paper08 v51 — first-page title/abstract correction (2026-10-17)

A fresh all-ref scan on 2026-10-17 checked all six branches, both tags, and both GitHub releases/assets before assigning v51. The highest Paper08 edition was v50 on `e2-v3-source-year` at `ae4abeb0f0dd2d9e30d1c013d0c2179b7a688a64`; no higher Paper08 version was found. Paper07 v54 is a separate lineage and does not supersede Paper08 v50. The user authorized this narrow correction and publication; v50 and all earlier editions remain unchanged.

Paper08 v51 is a layout-only correction at the existing Paper08 publication path, `arena agent 1/agent workspace/papers/`, on `e2-v3-source-year`. It moves the date and `\maketitle` before the abstract, so the title/author block is printed first. The abstract is byte-identical, and a normalized source check found no other manuscript-content change. The Tectonic 0.15.0 build is 86 pages (v50: 87); the table of contents updates and the main text begins on page 4. Visual QA confirms the title precedes the abstract on page 1 without clipping or overlap. There are zero overfull boxes; inherited underfull boxes and package warnings are recorded in `PAPER08_V51_LAYOUT_AUDIT_2026-10-17.md` and `paper08_governance_delay_v51_BUILD_LOG_2026-10-17.txt`.

The source, PDF, build log, changelog, and layout audit are published as `paper08_governance_delay_v51.tex`, `paper08_governance_delay_v51.pdf`, `paper08_governance_delay_v51_BUILD_LOG_2026-10-17.txt`, `PAPER08_V51_CHANGELOG_2026-10-17.md`, and `PAPER08_V51_LAYOUT_AUDIT_2026-10-17.md`. No tag or GitHub release was created.

---

## Paper10 v55 — conclusion punctuation correction (2026-10-18)

After the verification-only v54 pass found a missing sentence-ending period and a doubled terminal period in §11, the user authorized a narrow successor. A fresh all-ref scan of all six branches, both tags, and both releases/assets found v54 as the latest Paper10 Part I edition; v55 did not exist before numbering. Paper10b/E4 remains the separate Part II Edwards-aquifer line. See `paper10_depletion_ledgers_v55_src/VERSION_AUDIT_2026-10-18.md` for the refs, lineage disposition, build checks, and hashes.

Paper10 v55 changes only that §11 punctuation plus version/date metadata. The normalized source comparison reverts exactly to v54; v54 main/SI source and PDFs are preserved unchanged. At the initial main-text publication, the v54 supplementary material remained the unchanged companion; the later v55 SI metadata follow-up is recorded below. The MCS 2026 CSV and verifier are carried forward byte-for-byte in `paper10_depletion_ledgers_v55_src/`. Tectonic 0.15.0 builds the v55 main PDF to 56 pages with no overfull/underfull boxes, LaTeX errors, or unresolved references/citations. The source, PDF, log, changelog, audit, and reproduction package were published on `e2-v3-source-year` in commit `b897dde8d5c0dac7b7eb9bccc7dc4b3a60221ca1` (parent `7b4e426f9c139cddb38732d28732598f6429114f`). The publication receipt records the remote byte verification. No tag or release was created.

---

## Paper10 v55 SI follow-up — supplementary metadata correction (2026-10-18)

Before this follow-up, a fresh scan of six branches, two tags, and two release records/assets found v54 as the latest SI; no v55 SI existed. The v54 source header's statement that no compiled v54 PDF was claimed was stale: the v54 SI PDF had been built and published. The new v55 supplementary source updates only the edition/date/companion metadata and removes that stale comment. After reverting those changes, its substantive source content matches v54 byte-for-byte. V54 SI remains preserved; the v55 main text/PDF are unchanged.

The supplementary PDF builds to 19 pages with zero overfull boxes, six inherited underfull boxes, no LaTeX errors, and no unresolved references/citations. The source, PDF, log, changelog, and audit were published on `e2-v3-source-year` in commit `9dae8142c8a5d08e80ccab69f1a4be15b3e36ab7` (parent `864dc85672e2e6be2e33530f86e6a0cc5b767de4`); the follow-up receipt records the remote byte verification. The v55 source-package README was then refreshed to point to the current SI; no manuscript source/PDF changed. No tag or release was created.
