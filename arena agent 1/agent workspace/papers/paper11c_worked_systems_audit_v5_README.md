# paper11c v5 — assembly, compilation and verification

**Lineage.** `paper11c_worked_systems_audit_v4.tex` (`e2-v3-source-year`, `arena agent 1/agent workspace/papers/` and `agent workspace/paper 2 family/11c_worked_systems/`; descended from `paper2_worked_systems_v17` in `arena agent 1/paper rewrites/latex/` on `main`) → **v5**. See `paper11c_worked_systems_audit_v5_CHANGELOG_v4_to_v5.md`.

## Deliverables
* `paper11c_worked_systems_audit_v5.tex` / `.pdf` — main article (article 11pt A4; 22 pp.; Sections 1–12 + Declarations; 6 theorems, 10 propositions, 3 corollaries, 2 lemmas, 8 definitions, 2 remarks; 5 figures, 2 tables; 31 references, all cited)
* `paper11c_worked_systems_audit_v5_supplementary.tex` / `.pdf` — Supplementary Material S1–S11 (13 pp.): S1 master table of the 36 pairs with the mechanism of every dead pair; S2 whole-universe census (viable beliefs by size and convention, maximal beliefs, the 104-belief join defect, fixed-thread conventions, idle instrument); S3 stationary policies; S4 decentralised law tables (sustainers, the 16 law pairs of 12|21, authority census); S5 monitoring-design census (kernel-size distribution, 16 coarsest designs); S6 four-state target; S7 the 93-cell timing grid; S8 scaling to caps 4 and 5; S9 benchmark and drift tables; S10 verification record (64-check list, Lean declarations); S11 symbols
* `paper11c_worked_systems_audit_v5_verification.py` — exact verification (64 named checks; integers, bitmasks and `fractions.Fraction` only). Run from the edition folder (it imports `work/ws_core.py` or `paper11c_worked_systems_audit_v5_src/work/ws_core.py`); the full run recomputes everything including the 4,140-partition census (≈70 s); `--quick` reuses the stored census from `work/results.json` (≈2 s) and does not overwrite the shipped output. When the compiled PDFs are beside it, checks X1–X3 compare the quoted numbers against the recomputed ones. Output of the full run: `paper11c_worked_systems_audit_v5_verification_output.txt` (64/64)
* `paper11c_worked_systems_audit_v5_CHANGELOG_v4_to_v5.md`, `paper11c_worked_systems_audit_v5_highlights.md`, `COVER_LETTER_paper11c_worked_systems_audit_DEDS_v5.md`

## Source folder `paper11c_worked_systems_audit_v5_src/`
* `parts/00_front.tex … 12_back.tex` — the main text in thirteen parts
* `si_parts/S0_front.tex, S0b_mainlabels.tex, S1_master.tex … S11_symbols.tex` — the SI in thirteen parts; `S0b_mainlabels.tex` is generated from the main `.aux` and supplies the main-text numbers quoted in the SI (`\mref`, `\meqref`); `tab_*.tex` are generated table bodies (18 files, including the two main-text tables `tab_kernels_main.tex` and `tab_design_main.tex`), inlined into both documents at assembly
* `work/assemble.py` — writes both `.tex` files from the parts (`python3 work/assemble.py` from the edition folder)
* `work/ws_core.py` — the exact core: the system family (any cap), the fibrewise belief game (observation maps, protocols free / ledger / branch (private register) / optimistic / first / last, bitmask greatest-fixed-point kernel with horizon history), alternation closed forms for the ledger and the private register, stationary-policy enumerations, unanimity laws and the statewise factoring, set partitions and the design census, the incompatibility graph, Helly numbers, the hidden-regime model, the max-plus timing recursion, and the continuous fibre (benchmark, duality, drift, floors) in exact rationals
* `work/run_all.py` — computes everything and writes `work/results.json` (69 s on one core; `python3 -u run_all.py` from `work/`)
* `work/make_si_tables.py` — all table bodies from `results.json` and the archived verification output; `work/make_figs.py` — the five figures (`figs/fig1_system … fig5_continuous.pdf`); `work/make_mainlabels.py` — the main-text number table for the SI
* `work/results.json` — the complete record of the full run
* `src/` — the inherited inputs: v4 `.tex` and `repo_scripts/` (the v17 verifier `paper2_worked_systems_v17_verification.py`, `paper2_worked_systems_figures.py`, `round2_joint_audit_v1.md`, `round3_joint_audit_v1.md`); `work/census_rows.json` is the per-partition record of the design census (4,140 rows)
* `lean/WS_WorkedSystems.lean`, `lean/WS_WorkedSystems_v2.lean` — the Lean 4 modules of the repository (`Formalizations/`, Lean 4.34.1) cited in Theorem 3.1 and Remark 3.4 (declarations `refineObs`, `Wk_mono_obs`, `master_action_axis`, `master_memory_axis`, `master_monotone`, `monotone_action_axis`; 0 `sorry`); copied for reference, not rebuilt in this edition

## Compilation
Both `.tex` files search `./`, `figs/` and `paper11c_worked_systems_audit_v5_src/figs/`, so they compile unchanged in the repository folder and in a flat working folder. Compiled with Tectonic 0.15.0 (XeTeX engine); no overfull boxes above 1 pt in either document; all cross-references and citations resolve; the SI quotes main-text numbers through `S0b_mainlabels.tex`.

Workflow: `python3 work/assemble.py` → compile main → `python3 work/make_mainlabels.py` → `python3 paper11c_worked_systems_audit_v5_verification.py` (writes the output file) → `cd work && python3 make_si_tables.py` (now including `tab_checks.tex`) → `python3 work/assemble.py` → compile SI → `python3 paper11c_worked_systems_audit_v5_verification.py --quick` (text checks against both PDFs).

## Environment used
Linux x86_64, Python 3.13 (standard library only for the core and the verifier; Matplotlib 3.10 for figures; PyMuPDF for the PDF text checks, skipped if absent). Full pipeline 69 s; verification 70 s (full) or 2 s (`--quick`).
