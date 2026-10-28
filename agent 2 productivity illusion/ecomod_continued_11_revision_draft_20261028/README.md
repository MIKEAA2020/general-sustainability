# ECOMOD Continued 11 — local revision draft

**Date:** 2026-10-28  
**Status:** separate draft pushed to branch `agent/p06-ecomod-c11-local-draft-20261028`; not an issued release, DOI deposit, or publication.  
**Lineage:** explicit successor to Continued 10 (C10); the archived C10 and all earlier releases remain unchanged.

## Canonical files

- `ecomod_continued_11_revision_draft_20261028.pdf` — current main draft (36 pages).
- `ecomod_continued_11_revision_draft_20261028_SI.pdf` — current Supplementary Information (23 pages).
- `ecomod_continued_11_revision_draft_20261028.tex` and `_SI.tex` — assembled TeX sources.
- `parts/` — editable modular TeX. `assemble.py` rebuilds the assembled files.
- `build_c11.sh` — assembles, runs source checks, and builds both PDFs in three ordered passes (`pdflatex` by default; Tectonic is supported as a portable fallback).
- `C11_REBASE_DIFF_vs_ASSEMBLED_C10_20261028.patch` — current source diff against the authoritative assembled C10 main/SI pair.
- `CHANGELOG_C11_REVISION_DRAFT_20261028.md` — revision history and scope.
- `validation/ECOMOD_C11_REBASE_BUILD_CHECK_20261028.md` — original rebase, model-test, and build record.
- `validation/ECOMOD_C11_REVIEW_FOLLOWUP_20261028.md` — version-matched follow-up to the targeted C11 review, including the revised findings, numerical verification, and rebuild.
- `validation/ECOMOD_C10_RESULTS_PROVENANCE_20261028.md` — separate, unchanged audit of historical C10 code/output links and unresolved items.
- `check_c11_sources.py` — deterministic source, title/contact-link, label/reference/citation, TeX-balance, and revision-regression checks.

## Correct source base and immutable boundary

The current C11 **manuscript and SI TeX** were split and revised from the actual assembled C10 pair—not from the old v45 working-tree TeX:

- Repository main: `../output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026/ecomod_continued_10.tex`  
  Matching workspace copy: `../ecomod_v45/output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026/ecomod_continued_10.tex`  
  SHA-256 `9a5970ff26851f3b5495aff1341a484ecdfc7f33877c24493aff11bce596c971`
- Repository SI: `../output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026/ecomod_continued_10_SI.tex`  
  Matching workspace copy: `../ecomod_v45/output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026/ecomod_continued_10_SI.tex`  
  SHA-256 `7e815ab3c5e384448c871d05cc71a735798c4ac265e66f8a068260cc10fb3aab`

The C11 diff and rebase/build record identify the ported edits. The earlier, misbased attempt is preserved in the pushed branch at `agent 2 productivity illusion/ecomod_continued_11_misbased_v45_superseded_20261028/`; its duplicate workspace directory (which contained same-named PDFs with an older title and no contact-link annotations) was removed after byte-for-byte verification against the pushed commit. The branch retains the complete v45/C10 archive directories. Redundant local copies of those archives inside this C11 workspace were removed after exact comparison with the separate v45 package; that package remains unchanged. Current C11 sources, data, figures, work scripts, PDFs, QA evidence, manifests, and validation records remain here. Final build logs are under `output_submission_cleanup_20261028/`. The repository C10 source files at the path above, C8/C9, `main`, pins, checksums, and DOI deposits were not modified.

## Selected model and corrections

C11 selects the **projected delayed-quality law**:

\[
K_q=[0,q_{\max}],\qquad
\dot q(t)=\Pi_{T_{K_q}(q(t))}G_c(q(t-\tau_g)),\qquad
G_c(x)=\rho_cx(1-x/q_{\max}),
\]

with admissible continuous history. The manuscript identifies `q` as an uncalibrated, model-defined index; `q_max=1` as an imposed admissibility bound, not an estimated ecological threshold; and `rho_c` and `tau_g` as scenario parameters. The current-quality law is a sensitivity comparator only; the smooth alternative is not selected.

The revisions also:

- replace the population-delay classification based on `r tau_p < pi/2` with the actual delayed-capacity interpretation;
- qualify the `tau_g=20/40` comparison as saturation-induced degeneracy for the baseline history, not general delay robustness;
- separate the unique equality point on `B_eq(A_c)=E` from fixed-demand surplus no-conversion allocations and the full endogenous-population equality family;
- include the deficit-side debt derivative `partial D_dot/partial D = alpha b_f A_f - eta` and limit the spectrum to its stated one-sided active branch;
- reconcile the delayed-quality recovery endpoint to `A_c(T)=0.677 ha`, recovery fraction `0.46`;
- report the local projected-implementation and timestep checks at their tested scope, without claiming historical C10 producer-to-output provenance;
- frame outside ecological records/frameworks as measurement and future-modeling precedents only, not validation or calibration of the present equation/parameters.
- clarify that the conversion term determines the sign of net biocapacity change only when the other terms vanish; maintenance balance is not invariant during active conversion;
- replace the broad B-only impossibility statement with the exact floor inequality, distinguish information limits from universal control impossibility, and scope any service-constrained claim to a stated controller class;
- recompute both debt roots and numerical integrations from the same unrounded demand inputs, distinguish multiplicative `alpha` from the additive comparator coefficient, and retain `D(0)` in transient debt bounds;
- relabel the reserve minimum as a monitored threshold rather than an enforced hard floor, report the actual tested reserve minima, and make SI gate-table endpoint/extrema windows explicit;
- qualify finite-grid monotonicity as tested-run evidence and remove un-reproduced cross-study recovery-fit medians; scope supply-only observations to the `b_G,c rho_c` product; dynamic identification would require informative quality-trajectory data.

## Output provenance: keep revised runs and C10 history distinct

`figures/fig1_model_dynamics.png`, `si_drawdown_depth.csv`, and the SI drawdown/recovery table fragments were freshly generated or updated in this local draft using the projected solver. Figure 1's substantive values remain unchanged. The CSV now includes post-hoc minimum-reserve and maximum-fast-land diagnostics for both restoration settings, so it is not byte-identical to the earlier producer-package CSV; the existing drawdown/recovery table bodies retain their displayed model values. The fresh SI delay-sensitivity table was generated separately and reproduces the archived displayed precision, but it does not prove which historical run generated C10 Table S2. Other unchanged empirical figures and retained SI outputs remain C10 account/reproduction artifacts, not newly validated model outputs. See the two separate records under `validation/` for the tested implementation and the remaining historical run-to-output gaps.

## Rebuild and checks

From this directory, run:

```sh
./build_c11.sh
```

The script runs `assemble.py`, `check_c11_sources.py`, and three ordered passes for the main paper followed by three for the SI. `pdflatex` remains the default; set `TEX_ENGINE=tectonic` (or an executable path to Tectonic) if pdfLaTeX is unavailable. Build logs and contact-link verification are retained under `output_submission_cleanup_20261028/`. The source checker verifies title restoration, clickable email and ORCID in both assembled documents, modular/assembled synchronization, labels/references/citations, balance, and revision-specific claims. The latest build used Tectonic 0.17.0 because `pdflatex` is not installed in this workspace; the follow-up record gives the 36-page main and 23-page SI hashes and diagnostics. No unresolved labels or citations remain. There is one 2.608 pt front-page overfull box under Tectonic, several underfull boxes in dense tables/bibliography, and nonfatal `hyperref` title/author-note warnings; the parameter-table float now fits. `pypdf` inspection confirms the mailto and ORCID annotations in both PDFs. Exact current file hashes are listed in `SHA256SUMS_C11_LOCAL_20261028.txt`; that is a local-draft manifest, not a refresh of any archived v45/C10 checksum list.

**Repository snapshot:** pushed on branch `agent/p06-ecomod-c11-local-draft-20261028`. This is not a DOI deposit, publication, or issued release.