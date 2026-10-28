# ECOMOD Continued 11 — rebase, implementation, and build check

**Date:** 2026-10-28  
**Scope:** canonical local C11 draft in `/home/user/ecomod_continued_11_revision_draft_20261028/`.  
**Status:** rebase/build checks passed; separate draft snapshot pushed to `agent/p06-ecomod-c11-local-draft-20261028`, not an issued release.

## 1. Source base and separation from the superseded attempt

The canonical C11 main and SI were rebuilt from the actual assembled C10 pair:

| Authoritative C10 source | SHA-256 |
|---|---|
| `../output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026/ecomod_continued_10.tex` | `9a5970ff26851f3b5495aff1341a484ecdfc7f33877c24493aff11bce596c971` |
| `../output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026/ecomod_continued_10_SI.tex` | `7e815ab3c5e384448c871d05cc71a735798c4ac265e66f8a068260cc10fb3aab` |

The editable C11 modules are under `parts/`; `assemble.py` concatenates them and inlines the maintained SI table fragments. The assembled outputs were checked against the modules by `check_c11_sources.py`; there are no residual `\\input{...}` commands. `C11_REBASE_DIFF_vs_ASSEMBLED_C10_20261028.patch` is a direct diff against the two authoritative files above.

The earlier draft based on the v45 working-tree TeX is preserved in `../ecomod_continued_11_misbased_v45_superseded_20261028/`. It is not a source for this canonical C11. The copied v45 model implementation is used only as a legacy comparator/test-harness or as documented producer-package reference where appropriate; it is not the manuscript/SI base. The separate C10 results-provenance report distinguishes producer-package reproduction from revised-model outputs and records the unresolved historical run links.

SHA-256 of the final assembled C11 sources:

- Main TeX: `05bfc2f8a6dde475aae81d34dfbac1bebfe7a3e5ddf60858d108e18534c964e4`
- SI TeX: `3862c5a8365a83fe01fd3d15c10c29334fc9411d528b89722cb96b337b1f5336`

## 2. Model choice and carried corrections

The selected quality law is

\[
K_q=[0,q_{\max}],\qquad
\dot q(t)=\Pi_{T_{K_q}(q(t))}G_c(q(t-\tau_g)),\qquad
G_c(x)=\rho_c x(1-x/q_{\max}),
\]

with admissible continuous history. C11 identifies `q` as an uncalibrated, model-defined quality index; `q_max=1` as an imposed bound, not an ecological threshold estimate; and `rho_c` and `tau_g` as scenario parameters. The current-quality version is a comparator only. No smooth alternative is presented as the selected model.

Other corrected scope statements include: the population delay is in carrying capacity rather than population's own crowding term; the baseline `tau_g=20/40 yr` equality is saturation-induced rather than general delay robustness; the equality point on `B_eq(A_c)=E` is distinct from the fixed-demand no-conversion surplus family; the debt derivative includes `alpha b_f A_f - eta`; the deficit-side spectrum is one-sided; and the delayed-quality recovery result is `0.677 ha`, `0.46` at `T=400 yr`. External frameworks/data are described as measurement and future-modeling precedents, not validation or calibration of the present equation/parameters.

## 3. Local projected-law test: actual scope and results

The test was rerun from `work/test_projected_quality_consistency.py`; its final console output is `output_revision_projected/projected_quality_consistency_final.log`.

### Same-grid discrete update comparison

A copied v45 legacy post-Euler clipping implementation was used only as a comparison implementation against the explicit tangent-cone projected Euler solver. For the Figure 1 parameterization, `T=100 yr`, `dt=0.05 yr`, and `tau_g=5, 20, 40 yr`, the tested arrays for `A_f`, `A_c`, `q`, `P`, `D`, `A_r`, `B`, `E`, and `T_b` were exactly equal. This is a local comparison of two discrete implementations; it is not the archived C10 producer source and does not prove historical C10 code-to-output provenance.

### Quality and full-scenario refinement

For the baseline constant history `q(s)=0.9`, `rho_c=0.08 yr^-1`, `q_max=1`, and `tau_g=20` or `40 yr`, the continuous projected path is `q(t)=min(1, 0.9+0.0072t)` and reaches the imposed ceiling at `125/9 ≈ 13.8889 yr`. The `tau_g=20` and `40` discrete paths were exactly equal on the tested `dt=0.05 yr` grid; `tau_g=5 yr` is distinct. Scalar-quality sup error for `tau_g=20/40` fell from `7.1e-5` at `dt=0.1 yr` to `8.8e-6` at `dt=0.0125 yr`. For `tau_g=5 yr`, sup error against a `dt=0.00025 yr` reference fell from `2.1763e-4` at `dt=0.1 yr` to `2.6778e-5` at `dt=0.0125 yr`.

In the full frozen-demand Figure 1 scenario, comparing each coarse run with a `dt=0.003125 yr` reference gave:

| `dt` (yr) | max `A_c` error (ha) | max `B` error (gha) | max `P` error (cap) | max `D` error (gha yr) |
|---:|---:|---:|---:|---:|
| 0.100 | 0.004673 | 0.003799 | 0.000520 | 0.004222 |
| 0.050 | 0.002214 | 0.001799 | 0.000252 | 0.002001 |
| 0.025 | 0.001023 | 0.000831 | 0.000118 | 0.000924 |
| 0.0125 | 0.000436 | 0.000354 | 0.0000505 | 0.000394 |

These are tested local refinements, not a global error bound or convergence proof for all settings.

## 4. Fresh projected-solver outputs versus archived C10 values

The following C11 outputs were regenerated after the TeX rebase using the projected solver:

- `make_fig_model.py` regenerated Figure 1; PNG SHA-256 is `c96e1579e8bb32fb584e131514d6ada9f8c9f177384e415d23aa4f745870f796`, byte-identical to the archived C10 Figure 1 PNG.
- `drawdown_depth.py` regenerated `si_drawdown_depth.csv`; SHA-256 is `073c63778c46042d029a842d5a12529c207e5b2797bd56f4ca8f221951942417`, byte-identical to the retained producer-package CSV. `work/render_si_model_tables.py` regenerated the SI drawdown and recovery table fragments; they match the C10 table bodies byte-for-byte. The recovery table gives `A_c(T)=0.677 ha` and `R_c(T)=0.46` for `P_0=2.0 cap`.
- `work/generate_revised_si_delay_table.py` freshly regenerated SI Table S2's current-quality comparator versus selected projected delayed-quality model. It uses `dt=0.1 yr`, `T_threshold=800 yr`, and `tau_g=5,20,40 yr`. The resulting delayed thresholds are `2.95458, 2.95443, 2.95443 cap`, displayed as `2.955, 2.954, 2.954`; current-quality thresholds are `2.95475 cap`, displayed as `2.955`. The comparison reproduces archived displayed precision but does not identify the exact historical C10 table run.

The main C10 producer-to-output history is not inferred from these equalities. `validation/ECOMOD_C10_RESULTS_PROVENANCE_20261028.md` remains the controlling account of archived reproductions and unresolved historical links, including the original full SI Table S2 sweep and the high-resolution main Table 2(b) bisection. Unchanged NFA account calculations/figures and retained C10 SI outputs are not recast as newly validated model outputs.

## 5. Source, compilation, and PDF inspection

- `python check_c11_sources.py` passes: assembled main/SI match their modular sources and table fragments; labels/references and citations resolve; braces/environments balance; revision-specific checks pass.
- pdfLaTeX was run three times for each assembled document with `-interaction=nonstopmode -halt-on-error -file-line-error`.
- Main PDF: 35 pages, SHA-256 `1433afaf75dc43f318545a695277d7b05a31aeb950a1283de962829199ce43db`.
- SI PDF: 21 pages, SHA-256 `3cc70931f8756d5c1b848c55c9da9aeb16af57aa619d504d31b8e02d478ae5f9`.
- Final pass logs are `output_submission_cleanup_20261028/main_pass3.log` and `output_submission_cleanup_20261028/si_pass3.log`. No unresolved references/citations or overfull boxes were found. Nonfatal warnings: main title-author-note tokens omitted from PDF bookmarks by `hyperref`, plus underfull boxes in tight tables/bibliographic lines; SI underfull boxes in dense table material.
- Visual review used rendered PDF pages for the title/abstract, model equations, Figure 1, NFA figures/table, balance proposition/Table 4, discussion/conclusion, SI symbols/spectrum/debt derivative, SI Table S2, recovery Table S5, and the SI post-table layout. No clipping/overlap or blank page from the revised SI layout was found.

Current C11 artifact hashes are also listed in `SHA256SUMS_C11_LOCAL_20261028.txt`. No archived C10, C8/C9, `main`, pins, checksum lists, or DOI deposits were changed; the branch push stores this draft only; no DOI deposit or publication was made.

## 6. Final title and contact-link verification (2026-10-28)

The final assembled C11 main and SI use the exact C10 title, `A rising biocapacity total can mask ecological-capital land drawdown: a two-land model`; the superseded alternate title is absent. The strengthened `check_c11_sources.py` requires clickable email and ORCID markup separately in both documents and rejects the stale title and identified internal provenance/change-log phrases. It passes after assembly.

The PDFs were rebuilt after this cleanup. `mutool show` confirms the following PDF link annotations in **both** main and SI: `mailto:amin_abaee@ut.ac.ir` and `https://orcid.org/0000-0002-0019-1842`. The main and SI are 35 and 21 pages, respectively. Final engine, pass logs, annotation records, and source-check output are under `output_submission_cleanup_20261028/`. No unresolved citations/references or overfull boxes appear in the final logs; main has only the nonfatal `hyperref` title/author-footnote PDF-string warnings.
