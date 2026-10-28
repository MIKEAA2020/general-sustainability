# ECOMOD C10 results: code and provenance audit

**Audit date:** 2026-10-28  
**Scope:** read-only investigation of the advertised GitHub branches/tags, reachable file history (including deletions), releases and ZIP contents; targeted reproduction from the archived code. No repository files, C8/C9/C10 outputs, pins, checksums, DOI deposits, or `main` were changed.

## Executive finding

The best-supported result-producing snapshot is the **ECOMOD v45 working-package archive** at commit [`eab8e82eb5171d70711c1b319a83f99492e6fca8`](https://github.com/MIKEAA2020/general-sustainability/commit/eab8e82eb5171d70711c1b319a83f99492e6fca8), branch `ecomod-v45-workspace-archive-20261026`. It contains both the C10 output directory and the v45 model/data-generation code. The C10 output itself was also archived on `ecomod-v45-continuations-20261026` at [`a23bbca6dd183b2c39fcfe95637aff18db73fdc8`](https://github.com/MIKEAA2020/general-sustainability/commit/a23bbca6dd183b2c39fcfe95637aff18db73fdc8).

**The main generated C10 results are reproducible from that v45 snapshot.** I reran the producer scripts in isolated `/tmp` copies and got byte-identical PNGs for main Figures 1–3, the four one-stock SI figures, and the technology-wave SI figure; the wave metrics/time-series CSVs and NFA data outputs also matched exactly. The regenerated Figure 1 and wave PDFs match the archived PDFs byte-for-byte after normalizing only Matplotlib’s `/CreationDate` metadata. The generated drawdown/recovery table bodies (SI Tables S4/S5) match the C10 SI exactly.

C10 itself was **not a fresh simulation revision**. Its `LINEAGE.md` says the main TeX is unchanged from C9 and the SI changes are bibliography ordering and a page-break/layout correction. The checked C8/C9/C10 versions of main Figures 1–3, the technology-wave figure, and the four one-stock SI PNGs have identical SHA-256 hashes. Thus C10 carries forward results generated earlier in the v45 working sequence.

There are **two material gaps in exact historical provenance**: I found no preserved exact-run generator/configuration for (1) the full SI Table S2 current-quality/delayed-quality comparison and `tau_g = 5, 20, 40` threshold sweep, or (2) the final high-resolution bisection values in main Table 2(b). The verifier's basin output numerically matches one SI Table S2 value (delayed quality, `tau_g=20`, `A_c0=1.0`), but not the full table or its documented run path. The relevant solver variants and numerical checks are present, and the values are recorded in manuscript/history notes, but the exact full-table run path is not preserved. The current `verify_tab_conv_basin.py` also uses different horizon/step settings from Table 2(b) and gives different proximity thresholds. Consequently, the provenance is strong and reproducible for the main figures, NFA calculations, drawdown/recovery tables, wave outputs, and comparator figures, but **not complete for every static table entry**.

## 1. Branch, history, and release findings

### Relevant repository records

- The mirror contained **all 13 advertised heads and 3 tags**. Full reachable history was searched with `git log --all --full-history --follow` and deletion filters. `git fsck --full --no-reflogs --unreachable` reported no unreachable objects in the mirror.
- C10’s continuation branch head is `a23bbca6…` (`ecomod-v45-continuations-20261026`, 2026-10-26 16:06 +03:30). The full workspace archive is `eab8e82…` (2026-10-26 16:37 +03:30); its parent chain includes the C10 continuation snapshot. The v45 package is an archive-branch working snapshot, **not a C10 release tag**.
- The C10 output directory is `ecomod_v45/output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026/` in the workspace-archive branch. It contains assembled TeX/PDF/logs, figures, and `LINEAGE.md`, but no simulation scripts in the output directory itself. The generator code and inputs are in the sibling `ecomod_v45/` working-package tree.
- Current `main` is `d9f00aef6c8e80b229f875391b2783d394b49b4d`. It has the separate `batch 9/agent 2/ecomod_audit/` package, not the v45 generation package at its root.
- The audited v45 README describes the package as a working candidate derived from v44. That status note predates the later archive-branch snapshot; no separately tagged/published v45 release was found.

### Code lineage, including historical copies

The canonical C10 model solver is `ecomod_v45/work/twoland_fixed.py`, SHA-256 `7f2e47ab9a8047bfe335aaf02a90893b06aceba86c26b6f946999f94617e0c27` (Git blob `5ed5871c3b7dc80fbfbf112783097a1403f60936`). It uses the **delayed-quality** regeneration law `q(t - tau_g)` and is the solver imported by the v45 Figure 1 and drawdown scripts. The current-quality implementation is separately preserved in `work/twoland_fixed_current.py` for sensitivity; it is not the canonical reported solver.

Git copy history traces the model code through the original `model_sims/twoland_fixed.py` (v34, commit `84a39efbe870b921a125f36a4559a91530b536e6`, 2026-09-07), v42 (`f144fac93d77dd49c028a5f399ed699b4f31ca6a`, 2026-10-14), v43 (`461d59d3ab8e00a6409fd019f94361983618b488`, 2026-10-24), v44 (`36ef7a6bde047e3f555dae9ba8d2cf2aa4f10a2b`, 2026-10-24), and the v45 archive. At v45, the canonical file is a copy of v44’s `work/twoland_fixed_delayed.py`; comparison shows only the module docstring differs, not the executable code. The current-quality v44 `work/twoland_fixed.py` is not the solver used by the v45 generation scripts.

The reachable history search found no deletions of the v45 Python generator files or the relevant v42–v44 `twoland_fixed*`, `drawdown_depth.py`, or `make_fig_model.py` paths. Earlier candidate versions remain in the history/tree, but the current C10-equivalent code is the v45 delayed-quality package above.

### GitHub releases

All three release records and their assets were checked:

- **`saved_on_pc` (2026-10-25):** five PDF assets only; no source ZIP and no C10 source/generator package.
- **`edwards-framework-e1` (2026-09-12):** two workspace ZIPs. The ECOMOD-labelled ZIP contains older generic one-stock development scripts (`sim.py`–`sim6.py`, `makefig.py`, etc.), not the v45 two-land delayed-quality C10 pipeline. The second workspace ZIP has audit/PDF references but no C10 generation code.
- **`compendium-v1.0` (2026-09-04):** a workspace ZIP with no ECOMOD paths or C10 results.

So the useful code/result pairing is in the non-main v45 archive branch, not in a GitHub release asset.

## 2. C10 result-to-code map

| C10 result | Result-producing code and inputs | Reproduction finding |
|---|---|---|
| **Main Fig. 1(a,b)**: frozen-demand trajectory and equilibrium branch | `work/twoland_fixed.py` → `make_fig_model.py`. The script supplies the baseline parameters and `E=0.825` gha; `A_c0=1.5` ha, `A_f0=0.6` ha, `q0=0.9`; `T=400` yr, `dt=0.05` yr. The solver is explicit first-order Euler with delayed-history interpolation and stated state bounds. | Regenerated PNG is byte-identical to C10 (`c96e1579…`). PDF is identical after normalizing only `/CreationDate`; the remaining PDF bytes match exactly. The run reports a 149.0-year joint `B`-rise/`A_c`-decline window and the stated baseline endpoint checks. |
| **Main Fig. 1(c), SI Table S4 (`tab:si_drawdown`), and SI Table S5 (`tab:si_recovery`)** | `drawdown_depth.py` uses the same canonical solver, fixed parameters, `A_c0 = 0.40, 0.70, 1.00, 1.18` ha, `A_f0=0.6` ha, `q0=0.9`, `P0=1.0…4.0` cap at 0.1 increments, `T=400` yr, `dt=0.1` yr, and `chi_r=0.10`/`0`. It writes `si_drawdown_depth.csv`. `make_fig_model.py` reads that CSV for panel (c); `work/render_si_model_tables.py` writes the S4/S5 tables from the CSV. | The regenerated CSV is byte-identical (`073c6377…`); both generated table `tabular` blocks match the C10 SI exactly after whitespace normalization. This is a direct, verified code-to-table link. |
| **Main Figs. 2–3; NFA endpoint/component results** | `work/nfa_2026_recompute.py` reads `data/NEFBA_2026.xlsx`, validates the 1961–2023 complete-observation window and same-edition 1961–2022 sensitivity, then writes NFA CSV/JSON outputs and the two figures. | Both figure PNGs and all regenerated NFA CSV/JSON outputs are byte-identical to the archived v45 outputs. This is an accounting-data pipeline, not a simulation calibration/validation of the ECOMOD equation or parameters. |
| **SI proxy Divisia table/data** | `work/nfa_2026_proxy_divisia.py`; inputs are the same NFA workbook plus `data/empirical/cropland_area_owid.csv` and `cereal_yield_owid.csv`. | All three regenerated proxy CSVs match the archived v45 CSVs byte-for-byte. The script explicitly treats the residual as an accounting proxy, not physical capital or `Upsilon(q)A_c`. |
| **Four SI one-stock comparator figures** | `figure_scripts/make_si_onestock.py`; this is a separate one-stock comparator with parameters embedded in the script, not `twoland_fixed.py`. | All four C10 PNGs regenerate byte-for-byte. These figures are not outputs of the two-land model solver. |
| **SI technology-wave figure/table and time series** | `work/tb_wave_debt_scan.py` imports the delayed solver for reported runs and the current-quality solver only for sensitivity. It writes the SI figure, metrics, and time-series CSVs. Primary runs use matched wave/no-wave scenarios, `P0=1.0` cap, `T=250` yr, `dt=0.05` yr; selected runs use `P0=1.2` and a refined `dt=0.025` yr. | The PNG and all three reported metrics/time-series CSVs match archived outputs byte-for-byte. The PDF differs only in `/CreationDate`; all other bytes match. The delayed-quality primary ratio is 2.4865 at `P0=1.0`; the distinct `P0=1.2` all-time and post-wave ratios are 0.8337 and 2.3202. |
| **SI gate-sign/recovery table (`tab:si_gates`)** | `work/recovery_metric_and_tau_p_scan.py`; `s54()` computes and prints the gate table. It imports the delayed-quality solver. | Running `s54()` reproduces the displayed values. It is a calculation/validation helper, not a writer of the C10 TeX table. The optional `tau_p` diagnostic is separate from the table. |
| **Main Table 2(a), and one SI Table S2 threshold cell** | `work/verify_tab_conv_basin.py` computes/prints the composition contrasts, leading deficit-side eigenvalues, and basin thresholds. | The printed composition contrasts and $\lambda_1$ values match Table 2(a). An independent evaluation of the helper's Jacobian and ceiling formula gives $\lambda_2$ and $E_{\rm ceil}$ values that also match at the displayed rounding; the helper's stdout does not print those two columns. Its basin block uses $T=800$ yr and $\Delta t=0.1$ yr. At $A_{c0}=1.0$, the delayed-quality, $\tau_g=20$ result $P_0=2.954$ cap is numerically identical to the corresponding SI Table S2 cell; the table does not document enough settings to treat that match as proof of the historical run path. The helper does not reproduce the current-quality alternative, the $\tau_g=5$/$40$ rows, or the other S2 quantities. It does not generate either TeX table or Figure 1. Other static analytical/conceptual table text is not automatically built from one master script. |
| **Main Table 2(b) high-resolution bisection column and SI Table S2 (`tab:si_delay`)** | Related solvers and lower-resolution checks are present; no exact preserved table generator/run configuration was found. | **Historical provenance is incomplete.** See §4 below. |

### Direct comparison: verifier output vs main Table 2(a) and SI Table S2

- **Main Table 2(a):** the verifier prints `q*=0.5`, `b_c_eff=0.0660`, `Delta_b_conv=[+0.534, +0.784, +1.134, +1.934]`, and the leading eigenvalues `lambda_1=[-0.0522, -0.0537, -0.0547, -0.0556]`. These match the corresponding Table 2(a) entries. Its separate no-CSD block prints `lambda_1=-0.05366 yr^-1` at each tested demand fraction, consistent with the table's baseline `-0.0537`. The helper's stdout does **not** print `lambda_2` or `E_ceil`; evaluating the same Jacobian and ceiling expression gives `lambda_2=[-0.975, -0.998, -1.014, -1.029]` and `E_ceil=[0.804, 1.138, 1.606, 2.675]`, which also match Table 2(a) at its displayed precision.
- **SI Table S2:** the verifier's basin block prints `P_0=[2.387, 2.680, 2.954, 3.122]` cap for `A_c0=[0.40, 0.70, 1.00, 1.18]` ha, using `T=800` yr and `dt=0.1` yr. SI Table S2's `A_c0=1.0` row has `2.955` (current quality) and `2.954` (delayed quality) at `tau_g=20` yr. Thus only the delayed-quality `2.954` cell is a numerical match; the helper does not test the current-quality version or `tau_g=5`/`40`, and its other threshold outputs are not rows in S2. Because the full historical table-run settings are not recorded, this match does not establish the table's run provenance.

## 3. Inputs, parameters, and safe reproduction path

### Packaged inputs

The model figure/drawdown/wave simulations use hard-coded scenario parameters; they do not take an external ecological time series as a model input. Among the baseline values encoded in the scripts are `q_max=1` (imposed hard state bound, not estimated), `rho_c=0.08`, `tau_g=20` yr, `tau_p=25` yr, `A_tot=2.5` ha, `A_c^min=0.05` ha, and representative yields/flow parameters. Quality `q` is uncalibrated; `rho_c` and the delay values are scenario parameters, not estimates from recovery studies. These are model inputs, not fitted values. The proxy/data scripts use:

- `data/NEFBA_2026.xlsx` — SHA-256 `26e4f5c78d9fe20cb5cd51c073815157566711b53278a1f9118d7726ab60ad1b`.
- `data/empirical/cropland_area_owid.csv` — SHA-256 `1813b11ec66af1c747780e6b1b35832d6eac970b16abed14c068465d647df6fa`.
- `data/empirical/cereal_yield_owid.csv` — SHA-256 `52c445126fe3454891bf6199d94640629f3374f45bbf47f85d6f5e19209aedda`.

Producer-script SHA-256 hashes below are taken directly from the `ecomod-v45-workspace-archive-20261026` tree at commit `eab8e82…`:

| Script | SHA-256 |
|---|---|
| `work/twoland_fixed.py` (canonical delayed solver) | `7f2e47ab9a8047bfe335aaf02a90893b06aceba86c26b6f946999f94617e0c27` |
| `work/twoland_fixed_current.py` (current-quality sensitivity variant) | `5f38131c8c08692348decde24bb1b4da8f3fe03f986b5d7a90a446be1f76c529` |
| `drawdown_depth.py` | `c57eed8eda5b646f51ad3390ea8d29c6da9f65221932d5abd0edf803f7760c2b` |
| `make_fig_model.py` | `1a0f2fa6b58f553883c6bb6660179186e36635ffae575525505d98ced7a5a531` |
| `work/render_si_model_tables.py` | `9e2cd5b71d78b0bc01fffeafba73403e9b8ffe34f2521b3bdbfdb17da966af01` |
| `work/nfa_2026_recompute.py` | `861341efe5ebf4e7bbed0b6d343967cab61e2d746874e5ab6a6de2a932cbc70d` |
| `work/nfa_2026_proxy_divisia.py` | `f30f83db2fb71a8a7c25420556f8c81870b9ccdb054ab7cbe4922dcfbd9d5932` |
| `figure_scripts/make_si_onestock.py` | `610c2064c2d76610c608a6a0f73895313d76eb4c48bdca7e7188d29a367bfaf5` |
| `work/tb_wave_debt_scan.py` | `54b535e026728aba96c6f46e1988a4d64c865644b9f3b2cb391711bce66ca7fa` |
| `work/recovery_metric_and_tau_p_scan.py` (delayed-quality gate helper) | `9aac8c3c1ffa6c1df231725398945f2c711daf9477f07d974da4fef3177eaeba` |
| `work/recovery_metric_and_tau_p_scan_current_quality.py` (pre-audit gate/recovery helper; not the S2 sweep generator) | `4b7b784330ea19f830e573b672eab7a182e32d6d4fe89a544279f778807c1cf8` |
| `work/verify_tab_conv_basin.py` | `dc0b72cc7bd05e54a5f5fda98af799f3fcc2447a678a2a56cec251c0713337fb` |

The v45 package’s data notes identify the workbook as NFA Edition 2026 results/metadata v1.0 and describe the OWID series as FAOSTAT-derived. The cereal-yield series is a sentinel in the stated proxy, not an all-crops measure.

### Reproduce in a disposable clone/copy

These scripts write CSVs, figures, or table fragments into their package tree. To preserve the archived outputs, run only from a disposable clone or copy of the branch:

```bash
git clone --branch ecomod-v45-workspace-archive-20261026 \
  https://github.com/MIKEAA2020/general-sustainability.git /tmp/general-sustainability-v45
cd /tmp/general-sustainability-v45/ecomod_v45

python drawdown_depth.py
python make_fig_model.py
python work/render_si_model_tables.py
python work/nfa_2026_recompute.py
python work/nfa_2026_proxy_divisia.py
python figure_scripts/make_si_onestock.py
python work/tb_wave_debt_scan.py
python -c "import sys; sys.path.insert(0, 'work'); from recovery_metric_and_tau_p_scan import s54; s54()"  # gate table only; avoids optional long tau_p scan
python work/verify_tab_conv_basin.py  # check/print only; not a figure/table generator
```

The separate C10 TeX/PDF build is not the model-results run. C10 `LINEAGE.md` records Tectonic 0.17.0 on 2026-10-26. I did **not** use `ecomod_v45/parts/` as a substitute for the assembled C10 source; the C10 files and their own lineage are in the dedicated output directory. No Python lockfile/environment pin was found in the ECOMOD working package, so Python-library versions should be recorded in any future formal reproducibility deposit.

### Selected output hashes

- C10 Figure 1 PNG: `c96e1579e8bb32fb584e131514d6ada9f8c9f177384e415d23aa4f745870f796`.
- C10 Figure 2 PNG: `fc6375b57c7a22a88be0c400203c2d6c864283ceb0a5d954aeacd066c44c0f12`.
- C10 Figure 3 PNG: `7fa09d0e2dab341982edf6cc2b78e5e24cb38d3b1d73150309eb9ed78f7bab6d`.
- C10 technology-wave PNG: `4905bcf23d548e12645385091dac0accc28089ca9fdd9efecb3b4633a875b5c8`.
- Drawdown CSV: `073c63778c46042d029a842d5a12529c207e5b2797bd56f4ca8f221951942417`.
- Wave metrics CSV: `bea80389ba6db84c6d3ed2107e368603353cd14ff21670133eba3d89ca65e4e1`.

## 4. Explicitly unresolved provenance

### Main Table 2(b) final bisection values

The C10 table reports the final high-resolution proximity values `2.41, 2.70, 2.98, 3.14` cap, with `dt=0.05` yr and `T=1000` yr. The v44-to-v45 changelog records a run at those settings and the more precise values `2.4101, 2.7005, 2.9779, 3.1407`; `make_fig_model.py` then hard-codes the rounded values for plot markers. However, the preserved `work/verify_tab_conv_basin.py` bisection function is configured for `dt=0.1` yr and `T=800` yr and prints `2.387, 2.680, 2.954, 3.122` cap. The 0.05/1000 run script/configuration itself was not found in the branch tree or reachable code history. Therefore the exact final-column values are **documented and plausibly reproducible from the solver, but their original run provenance is not fully established**.

### SI Table S2 current-vs-delayed and `tau_g` sensitivity

The table values are present in earlier manuscript history and are retained in C10 as `tab:si_delay`. Both solver variants are preserved. A separate `work/recovery_metric_and_tau_p_scan_current_quality.py` is also present, but its own docstring describes a pre-audit gate/recovery helper, not the reported v45 results or the S2 delay sweep. No dedicated script/configuration for the full current-vs-delayed comparison and the `tau_g=5,20,40` threshold rows was found in the archived v45 package or reachable code history. `verify_tab_conv_basin.py` numerically matches one displayed cell: its delayed-quality run at `A_c0=1.0` ha and `tau_g=20` yr returns `P_0=2.954` cap, the SI Table S2 entry. Its settings are `T=800` yr and `dt=0.1` yr, and the table does not document enough settings to establish this as the historical run. It does not reproduce the current-quality alternative, the `tau_g=5`/`40` rows, or the other table quantities. The present solvers can be used to recompute that sweep, but that would establish a new reproduction, not prove which exact run produced the historical table. Provenance for the complete table is therefore **not established**.

### Static manuscript assembly and audit scripts

C10’s tables are statically embedded in its assembled TeX; there is no single end-to-end driver that regenerates every TeX table from simulation output. The independent `ecomod_audit/verify_ecomod.py` and `verify_ecomod_si.py` scripts on `main` were added at commits `0c8a1c862b366e5935ebf4efb5599fd0b34b46d8` and `195aa462d5796e708e4b8be75db24bc452cecc28`, respectively. They explicitly label themselves as independent audits and “not the author’s simulation code.” They write audit JSON/extracts and check equations/data; they do not produce the C10 figures or manuscript tables. They must not be cited as the generation pipeline.

## 5. Bottom line

Use `ecomod-v45-workspace-archive-20261026` / commit `eab8e82…` as the **best-supported, reproducible source snapshot** for C10’s carried-forward results. It identifies the canonical delayed-quality solver, inputs, figure/data-generation scripts, and working run settings, and its principal generated outputs reproduce. C10 itself is a manuscript/layout continuation over those existing outputs. Do not claim complete historical provenance for the Table 2(b) high-resolution bisection or the full SI Table S2 delay/current-quality sensitivity without recovering or rerunning and documenting their exact scripts/configurations.
