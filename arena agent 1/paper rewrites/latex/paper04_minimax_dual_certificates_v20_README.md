# paper04 v20 — assembly, compilation and verification

**Lineage.** `paper04_minimax_dual_certificates_v19.tex` (`e2-v3-source-year`, `arena agent 1/agent workspace/papers/`; the `main` lineage `minimax_dual_certificates_v*` is an ancestor) → v20. See `paper04_minimax_dual_certificates_v20_CHANGELOG_v19_to_v20.md`.

## Deliverables
* `paper04_minimax_dual_certificates_v20.tex` / `.pdf` — main article (article 11pt A4; 19 pp.; Sections 1–8; 4 theorems, 6 propositions, 1 corollary, 3 examples, 4 remarks, 4 open problems; 4 figures, 1 table; 30 references, all cited)
* `paper04_minimax_dual_certificates_v20_supplementary.tex` / `.pdf` — Supplementary Material S1–S8 (13 pp.): S1 proof details for the static theory (Sion hypotheses, Helly for infinite families and the rank reduction, the tight family's dual, the convex-hull programme, polyhedral duality with the Y = 6 Farkas numbers); S2 static instance records (one-dimensional instances, tight family k = 1…4, benchmark atoms, margin table, demand-floor law); S3 the two-patch codex; S4 the random Helly-size study; S5 review-envelope records (all cells of the two-window instance, tree count, coupling vertices, sweep with worst couplings, inherited instances, matching and posterior-only instances); S6 the integrated certificate and its sign convention; S7 verification record (scripts, 66-check list, Lean scope list, figure provenance); S8 symbol table and sign conventions
* `paper04_minimax_dual_certificates_v20_verification.py` — exact-arithmetic verification (66 checks; `fractions`-based; SciPy's HiGHS is used only as a float *proposer* inside two routines, every proposal is confirmed exactly, and both routines degrade gracefully without SciPy). Run from a directory containing `work/` or `paper04_minimax_dual_certificates_v20_src/work/` (it imports `p04_core.py` from there); `--quick` skips the k = 4 random study (≈30 s instead of ≈100 s). When the compiled `.aux` and the supplementary `.tex` are beside it, the text-binding checks (TXT, TXT.1, TXT.2) run as well. Output archived as `paper04_minimax_dual_certificates_v20_verification_output.txt`
* `paper04_minimax_dual_certificates_v20_CHANGELOG_v19_to_v20.md`, `paper04_minimax_dual_certificates_v20_highlights.md`, `COVER_LETTER_paper04_minimax_dual_certificates_JOTA_v20.md`

## Source folder `paper04_minimax_dual_certificates_v20_src/`
* `parts/00_front.tex … 08_related.tex, 12_back.tex` — the main text in ten parts
* `si_parts/S0_front.tex, S0b_mainlabels.tex, S1_proofs.tex … S8_symbols.tex` — the SI in ten parts; `S0b_mainlabels.tex` is generated from the main `.aux` and supplies the main-text numbers quoted in the SI (`\mref`, `\meqref`); `tab_*.tex` are generated table bodies (Helly study, sweep, coupling vertices, two-window tree, instances, matching, check list, benchmark margins, demand-floor law, two-patch codex), inlined at assembly
* `work/assemble.py` — writes both `.tex` files from the parts (`python3 work/assemble.py` from the edition folder)
* `work/p04_core.py` — the exact module: rational polytopes and support functions, lower values by vertex enumeration of the lifted polytope, exact simplex programmes for dual values and margins, minimal infeasible subfamilies (optionally float-screened, always exactly confirmed), the tight family and its plant, the convex-hull programme, the benchmark (caps from the model equations, margin law, demand-floor law), the two-patch codex, the generic review-tree class (node recursion, tree enumeration, tower and martingale identities, defeat masses), the two-window instance and the inherited instances, the coupling polytope and the certified robust values, the integrated certificate
* `work/make_figs.py` — the four figures, recomputed from the module and `work/results.json` (`figs/fig1_dual_geometry, fig2_benchmark, fig3_review, fig4_helly_gamma`)
* `work/make_si_tables.py` — the SI table bodies, generated from `results.json`, the module and the archived verification output
* `work/make_mainlabels.py` — the main-text number table for the SI
* `work/results.json` — written by the verification script (consumed by the figure and table scripts)
* `work/repo_scripts/` — the inherited v19 scripts and records (`minimax_dual_certificates_v12_verify.py`, `verify_new_math.py`, `minimax_residue_grid_lp_v1.py` with its record, `minimax_caps_v1.json`, logs), unchanged
* `Minimax_Dual.lean` — copy of the Lean 4 module (source of record: the repository's Lean workspace, Lean 4.34.1, 60/60 jobs, 0 `sorry`)

## Compilation
Both `.tex` files search `./`, `figs/` and `paper04_minimax_dual_certificates_v20_src/figs/`, so they compile unchanged in the repository folder and in a flat working folder. Compiled with Tectonic 0.15.0 (XeTeX engine); no overfull boxes in either document; all cross-references resolve; the SI's main-text numbers are checked against the compiled `.aux` (check TXT.2).

## Environment used
Linux x86_64, Python 3.13, SciPy 1.17 (float proposals only), Matplotlib 3.10 (figures only). The verification runs in about 100 s (full) or 30 s (`--quick`).
