# ECOMOD Continued 11 — controlled local revision draft

**Snapshot date:** 2026-10-28  
**Lineage:** Archived ECOMOD **Continued 10 (C10)** is the predecessor; this workspace is the separate local draft for **Continued 11**. It is based on the best-supported v45 working-package archive snapshot (commit `eab8e82eb5171d70711c1b319a83f99492e6fca8`). “v45” identifies that source-package snapshot, not the manuscript continuation number. This is not yet an issued release. The original v45 package, archived C10 outputs, c8/c9, `main`, pins, checksums, and DOI deposits remain untouched.

## Scope and status

This directory is the controlled workspace for revising ECOMOD after the C10 model/evidence audit. It keeps two distinct tasks separate:

1. **Revised-model runs:** outputs generated here with an explicit projected quality law and documented local code/settings.
2. **Historical C10 reproduction/provenance:** identifying the exact producer version, dependencies, parameters, histories, time step, interpolation, update order, and run-to-output mapping for each archived C10 item.

A revised run is not an archived-run reproduction merely because displayed values match. The complete historical run path for the old SI delay sweep and the high-resolution Table 2(b) column remains unestablished; see the separate reports referenced below.

## Governing model specification

- The quality index is uncalibrated and model-defined. The bound `q_max=1` is imposed for admissibility, not estimated as an ecological threshold.
- `rho_c` and `tau_g` are scenario parameters, not estimates from recovery studies.
- The current continuous-time law is
  `K_q=[0,q_max]`,
  `q_dot = Pi_{T_{K_q}(q(t))} G_c(q(t-tau_g))`,
  `G_c(x)=rho_c x (1-x/q_max)`,
  with an admissible continuous history.
- The draft's `work/twoland_fixed.py` is the unchanged archived v45 candidate solver. `work/twoland_fixed_projected.py` is the separate revision solver. Do not treat the former as proven historical provenance for every C10 artifact.
- A local same-grid/refinement test succeeded for the cases documented in `/home/user/ECOMOD_C11_PROJECTED_IMPLEMENTATION_CHECK_20261028.md`. It establishes tested local discrete-update consistency, not the historical code-to-C10-output link.

## Principal files

- `parts/00_front.tex`–`parts/04_refs.tex` — modular main article.
- `parts/si_00.tex`–`parts/si_refs.tex` — modular Supplementary Information.
- `ecomod_continued_11_revision_draft_20261028.tex`, `ecomod_continued_11_revision_draft_20261028_SI.tex` — assembled main paper and Supplementary Information; regenerate with `python assemble.py` after source edits.
- `ecomod_continued_11_revision_draft_20261028.pdf`, `ecomod_continued_11_revision_draft_20261028_SI.pdf` — compiled main and SI PDFs from those assembled sources.
- `work/twoland_fixed.py` — preserved v45 candidate solver, unchanged.
- `work/twoland_fixed_projected.py` — separate projected-quality solver used by the revision's relevant producers.
- `work/test_projected_quality_consistency.py` — same-grid and time-refinement checks.
- `work/generate_revised_si_delay_table.py` — fresh SI delay/current-quality sensitivity run and table writer.
- `drawdown_depth.py`, `make_fig_model.py`, `work/render_si_model_tables.py` — projected-model drawdown data, Figure 1, and SI drawdown/recovery table producers.
- `si_drawdown_depth.csv`, `parts/si_tab_drawdown.tex`, `parts/si_tab_recovery.tex`, `parts/si_tab_delay.tex` — generated drawdown and sensitivity data/table bodies.
- `output_revision_projected/si_delay_sensitivity.csv` — full-precision threshold results from the new SI delay-table run.
- `figures/fig1_model_dynamics.png` and `.pdf` — Figure 1 freshly regenerated in the draft.
- `CHANGELOG_C11_REVISION_DRAFT_20261028.md` — controlled change log for this draft.

## Rebuild and checks

Run from this directory:

```sh
python work/test_projected_quality_consistency.py
python drawdown_depth.py
python make_fig_model.py
python work/render_si_model_tables.py
python work/generate_revised_si_delay_table.py
python assemble.py
```

The current main and SI PDFs were compiled from these assembled sources with pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev/Debian), three passes per document. The main is 36 pages and the SI is 22 pages. Final-pass logs are beside the PDFs; the detailed record, hashes, and remaining nonfatal warnings are in `output_revision_projected/continued_11_tex_build_20261028.log`. For a future rebuild, use a TeX Live installation with `elsarticle` and the listed packages, running `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error` three times on each assembled `.tex`. The v45 archive's separate C10 build record lists Tectonic 0.17.0; that is not evidence that the archived simulations ran under the same Python environment.

## Audit and provenance reports

- `/home/user/ECOMOD_C10_RESULTS_PROVENANCE_20261028.md` — historical code/output investigation and producer map; identifies unresolved historical provenance.
- `/home/user/ECOMOD_C10_FINDINGS_VERIFICATION_20261027.md` — six verified manuscript findings.
- `/home/user/ECOMOD_C10_HARDBOUND_EVIDENCE_VERIFICATION_20261028.md` — quality-bound/evidence note.
- `/home/user/ECOMOD_C11_REVISION_BRIEF_20261028.md` — controlled-revision decisions and separated workstreams.
- `/home/user/ECOMOD_C11_PROJECTED_IMPLEMENTATION_CHECK_20261028.md` — numerical consistency test and revised-run metadata.

## Release boundary

This folder is the local working draft for Continued 11, not an issued release. No DOI deposit, checksum manifest, release tag, or archived C10 file is updated by the draft workflow. Any later release or remote-repository action requires its own explicit decision and a version-matched manifest.