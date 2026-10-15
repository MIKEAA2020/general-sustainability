# paper03 v23 — assembly, compilation and verification

**Lineage.** `paper03_computational_certification_v22.tex` (`e2-v3-source-year`, `arena agent 1/agent workspace/papers/`) → v23. See `paper03_computational_certification_v23_CHANGELOG_v22_to_v23.md`.

## Deliverables
* `paper03_computational_certification_v23.tex` / `.pdf` — main article (article 11pt A4; 26 pp.; Sections 1–10, Appendices A–B; 4 figures, 2 tables; 30 references, all cited)
* `paper03_computational_certification_v23_supplementary.tex` / `.pdf` — Supplementary Material S1–S8 (10 pp.): S1 proofs for Sections 2–4; S2 hypothesis moduli from primitives and the Th/4 sharpening; S3 exact pair/ladder arithmetic; S4 the two-stage observer schedule and the archived sweep; S5 extensions (erosion, oracle, belief cells); S6 dilation scoping; S7 verification record (scripts, Lean layer, figure provenance); S8 sparsification on the instance
* `paper03_computational_certification_v23_verification.py` — exact-arithmetic verification (63 checks; optional SciPy/HiGHS cross-check). Run from a directory containing `work/` or `paper03_computational_certification_v23_src/work/` (it imports `p03_core.py` and reads `observer_sweep.tsv` from there). Output archived as `paper03_computational_certification_v23_verification_output.txt`
* `paper03_computational_certification_v23_CHANGELOG_v22_to_v23.md`, `paper03_computational_certification_v23_highlights.md`, `COVER_LETTER_paper03_computational_certification_SICON_v23.md`

## Source folder `paper03_computational_certification_v23_src/`
* `parts/00_front.tex … 12_back.tex` — the main text in thirteen parts; `cat parts/0*.tex parts/1*.tex > paper03_computational_certification_v23.tex`
* `si_parts/S0_front.tex … S9_end.tex` — the SI in ten parts; `cat si_parts/S*.tex > paper03_computational_certification_v23_supplementary.tex`
* `figs/fig1_trajectories, fig2_meshlaw, fig3_ladder, fig4_observer` (`.pdf` + `.png`)
* `work/p03_core.py` — the exact module (instance data, `h_U`/`phi_U`, exact leg-wise trajectories, LP builder for any aligned mesh and refining information structure, closed-form primal/dual witnesses, mesh law, HiGHS interface, erosion, authorities, pair duals, rational root brackets, exact rank)
* `work/make_figs.py` — recompute-then-assert figure script (≈ 40 s; 21 HiGHS solves for the Fig. 4 sweep); writes `figs/*` and `work/observer_sweep.tsv`
* `work/observer_sweep.tsv` — the archived sweep read by the verifier and tabulated in SM S4
* `work/repo_scripts/` — inherited scripts (`paper2c_lp_campaign.py` 9/9, `paper2_nonstandard_verification.py` 51/51, v20 verification, `certificate_exchange_v1.py`, figures v1) and `work/viacert/` (`python3 -m viacert selftest` → 12/12)

## Compilation
Both `.tex` files search `./`, `figs/` and `paper03_computational_certification_v23_src/figs/`, so they compile unchanged in the repository folder and in a flat working folder. Compiled with Tectonic 0.15.0 (XeTeX engine); no overfull boxes in either document; all cross-references resolve.

## Environment used
Linux x86_64, Intel Xeon @ 2.60 GHz, Python 3.13.16, NumPy 2.3.5, SciPy 1.17.1 (HiGHS dual simplex), Matplotlib 3.10.9. The exact checks need only the standard library.
