# Controlled ECOMOD Continued 11 local revision draft — change log

**Date:** 2026-10-28  
**Lineage:** separate local successor draft to archived Continued 10 (C10).  
**Base:** separate copy of `ecomod-v45-workspace-archive-20261026`, commit `eab8e82eb5171d70711c1b319a83f99492e6fca8`.

This log concerns only `../ecomod_continued_11_revision_draft_20261028/`. It does not modify the base package, archived C10, c8/c9, `main`, pins, checksums, or DOI records; Continued 11 has not been issued as a release.

## Model specification and numerical work

- Added `work/twoland_fixed_projected.py` as a separate revision solver; retained the copied `work/twoland_fixed.py` unchanged for comparison.
- Made the current continuous-time quality specification explicit in the modular main text and SI:
  `K_q=[0,q_max]`,
  `q_dot=Pi_{T_{K_q}(q(t))} G_c(q(t-tau_g))`,
  `G_c(x)=rho_c x(1-x/q_max)`, with an admissible continuous history.
- Clarified throughout that `q` is an uncalibrated, model-defined quality index, `q_max=1` is an imposed admissibility bound, and `rho_c` and `tau_g` are scenario values rather than estimates.
- Added a local same-grid and timestep-refinement test. The results and exact scope are recorded in the implementation-check report; they do not establish historical provenance.
- Corrected the revised SI delay-table producer to emit valid TeX row terminators (`\\`) after the first SI compile exposed a single-backslash row-ending error; regenerated the table and reassembled the SI.
- Regenerated Figure 1, the drawdown CSV, drawdown/recovery table bodies, and a new SI delay table from the projected solver. The Figure 1 PNG and drawdown/recovery table bodies match archived C10 outputs at their displayed/source representations; the new SI delay generator also matches historical displayed precision, but it is a fresh run and not proof of the old run path.

## Disposition of the six verified findings

1. **Quality ceiling:** replaced the raw unbounded delayed-quality equation with the tangent-cone projected law; recorded the numerical comparison and convergence checks.
2. **20/40-year comparison:** identified it as saturation-induced degeneracy under the baseline constant history, because the quality path reaches the imposed ceiling at `125/9 ≈ 13.8889 yr` before either delay elapses. Removed general delay-robustness language.
3. **Population stability:** removed the Hutchinson `r tau_p < pi/2` classification for the written `P_dot=rP(1-P/K(t-tau_p))` equation. SI now gives `delta P_dot=-r delta P+r delta K(t-tau_p)` and limits any coupled stability claim to a proper active-set analysis.
4. **Debt Jacobian:** corrected the `D`-row derivative to include `alpha b_f A_f - eta`; retained the independent finite-difference check. No full coupled spectrum is claimed.
5. **Recovery endpoint:** changed the main Results from the current-quality sensitivity's `0.828 ha / 0.71` to the projected delayed-quality run's `0.677 ha / 0.46` at `T=400 yr`, matching the SI delayed-quality table. The old numbers remain only in the excluded current-quality comparison snapshot.
6. **Equilibrium family:** separated the unique equality-balance locus from the fixed-demand surplus/no-conversion set and from the full endogenous-population equality family. The deficit-side Jacobian is described as one-sided, not two-sided stability of an isolated switched equilibrium.

## Assembly and release state

- Modular main/SI are the editable sources under `parts/`; `assemble.py` inlines SI table bodies into `ecomod_continued_11_revision_draft_20261028.tex` and `ecomod_continued_11_revision_draft_20261028_SI.tex`.
- Compiled the assembled main and SI with pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev/Debian), three passes each: `ecomod_continued_11_revision_draft_20261028.pdf` (36 pages) and `_SI.pdf` (22 pages). Final logs, hashes, and nonfatal warnings are recorded in `output_revision_projected/continued_11_tex_build_20261028.log`.
- The main and SI PDFs in nested v45/C10 output snapshots remain older archived builds; they are not substitutes for the new root-level PDFs.
- Historical C10 provenance remains a separate workstream; a matching number or plot is not treated as proof that the revised solver generated an archived output.