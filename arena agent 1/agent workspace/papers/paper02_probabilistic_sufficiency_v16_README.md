# paper02 v16 — assembly, compilation and verification

**Lineage.** `paper02_probabilistic_sufficiency_v15.tex` (`e2-v3-source-year`, `arena agent 1/agent workspace/papers/`) → v16. See `paper02_probabilistic_sufficiency_v16_CHANGELOG_v15_to_v16.md`.

## Deliverables
* `paper02_probabilistic_sufficiency_v16.tex` / `.pdf` — main article (article 11pt A4; 23 pp.; Sections 1–11; 4 figures; 37 references, all cited)
* `paper02_probabilistic_sufficiency_v16_supplementary.tex` / `.pdf` — Supplementary Material S1–S8 (8 pp.): S1 the complete certified value table and census; S2 the two-floor instance and the asymmetric audit; S3 jump loci and agreement of the segment enumeration; S4 learning-deadline tables and the two-patch instance; S5 exact wrong-majority probabilities; S6 contamination operator (conventions, computations); S7 verification record (scripts, check list, Lean layer, figure provenance, changes affecting claims); S8 symbol table with the companion readings
* `paper02_probabilistic_sufficiency_v16_verification.py` — exact-arithmetic verification (62 checks; Python standard library only). Run from a directory containing `work/` or `paper02_probabilistic_sufficiency_v16_src/work/` (it imports `p02_core.py` from there); when the compiled `.aux` and the supplementary `.tex` are beside it, the five text-binding checks run as well. Output archived as `paper02_probabilistic_sufficiency_v16_verification_output.txt`
* `paper02_probabilistic_sufficiency_v16_CHANGELOG_v15_to_v16.md`, `paper02_probabilistic_sufficiency_v16_highlights.md`, `COVER_LETTER_paper02_probabilistic_sufficiency_MOR_v16.md`

## Source folder `paper02_probabilistic_sufficiency_v16_src/`
* `parts/00_front.tex … 12_back.tex` — the main text in thirteen parts
* `si_parts/S0_front.tex, S0b_mainlabels.tex, S1_grid.tex … S8_symbols.tex` — the SI in ten parts; `S0b_mainlabels.tex` is generated from the main `.aux` and supplies the main-text numbers quoted in the SI (`\mref`, `\meqref`); `tab_grid.tex, tab_asym.tex, tab_deadline.tex, tab_majority.tex` are generated table bodies, inlined at assembly
* `work/assemble.py` — writes both `.tex` files from the parts (`python3 work/assemble.py` from the edition folder)
* `work/p02_core.py` — the exact module (generic finite safety POMDP with masked α-vector backup, dominance pruning, Bayes update, open-loop enumeration, contaminated operator; the delayed, declining, two-floor, sensor, contamination, `F_n` and two-patch instances; closed forms, census, class difference, deadlines, schedule law, noisy probes, majority reading, probe-count tail)
* `work/make_figs.py` — the four figures, recomputed from the module (writes `figs/fig1_deficits, fig2_closedforms, fig3_deadlines, fig4_probes` as `.pdf` + `.png`)
* `work/make_si_tables.py` — the SI tables with built-in assertions against the closed forms
* `work/repo_scripts/` — the inherited v15 scripts (`paper2_belief_state_v2_verification.py`, `paper2_stochastic_selector_v2_verify.py`, `hidden_parameter_learning_v1_verify.py`, `paper2_belief_state_figures.py`), unchanged

## Compilation
Both `.tex` files search `./`, `figs/` and `paper02_probabilistic_sufficiency_v16_src/figs/`, so they compile unchanged in the repository folder and in a flat working folder. Compiled with Tectonic 0.15.0 (XeTeX engine); no overfull boxes in either document; all cross-references resolve; the SI's main-text numbers are checked against the compiled `.aux` (check TXT.5).

## Environment used
Linux x86_64, Python 3.13.16, Matplotlib 3.10.9 (figures only). The verification needs only the standard library (`fractions`, `itertools`, `random` with a fixed seed) and runs in about four seconds.
