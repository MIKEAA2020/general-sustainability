# Independent rerun — Edwards intervention-selection leg (2026-08-26)

**Scope.** The intervention artifacts committed in the Task-33 session (`wave_e_edwards/src/run_intervention.py`, `results/intervention_results.json`, `results/intervention_boundaries.csv`) were **first-run** with independent-rerun status NONE. This record documents their rerun by a second agent session: a fresh execution of the committed runner on a clean process, verifying that the committed code deterministically reproduces the committed artifacts.

**Environment.** Python 3.12.13 / numpy 2.1.3 / pandas 2.2.3, x86_64 Linux (`environment.txt`) — the SAME machine, interpreter, and library versions as the original Task-33 run. **Honest scope note:** this is a second-session rerun in the same environment, not a cross-toolchain rerun (the Task-29 standard for the Part II certificates used Python 3.13.14 / numpy 2.3.5 on a different toolchain). What it verifies: committed-code reproducibility, determinism, and freedom from uncommitted state. What it does not verify: numerical stability across library versions. Given the byte-identity result and the deterministic (no-randomness) runner, the artifact claim is reproduced; the cross-toolchain standard remains available to a future rerun if the owner wants it.

**Procedure.**

1. Committed artifacts snapshotted and hashed before execution (`committed/`, hashes below).
2. `cd wave_e_edwards && python3 src/run_intervention.py` executed fresh (`rerun_console.log`, exit 0, ~1.2 s, deterministic — no randomness anywhere in the runner).
3. The regenerated artifacts compared byte-for-byte against the committed snapshot.

**Result: BYTE-IDENTICAL (hash-identical) on both artifacts** (same-environment second-session rerun; see the scope note above).

| Artifact | SHA-256 (committed = rerun) |
|---|---|
| `results/intervention_results.json` | `41712fdc653fa05a39b41634137adfe2744b7eadcc1af76c57098316cff7a6b1` |
| `results/intervention_boundaries.csv` | `57ddb684d83b93b5ecd20c968c8fea9f5b078cbda54376a0c7a79999414061be` |

**Headline verdicts re-observed on the rerun** (console log): fit a=0.7461, β=0.0198, γ=−0.02844; ε train max 15.41 / OOS max 21.81 ft; S1 and cpm RETAINED (nominal and certified, drought-floor/physical readings); certified kernels defect-bound to T ≤ 3 yr (physical) / T ≤ 1 yr (institutional); flat_0 certified to T=5 under q05/q10 physical; every policy's stress replay stays above 618 ft; the worst-case steady states reproduce exactly (e.g. flat_60 UC_min 628.36, cpm UC_min 628.36).

**What this does and does not close.**

- CLOSED: the "first run / independent rerun NONE" limitation on the intervention artifacts. The runner, results, and boundary table are now `INDEPENDENT_RERUN 2026-08-26 (byte-identical)`.
- NOT CLOSED: Wave E itself (Part III paper-support rows remain NOT CONFIRMED); the nominal-level status of the positive content (the certified kernels remain defect-bound — a rerun cannot change the model defect); the cod-side Cor2 analogue (G1a); the two-pool exact specialization.

Files: `committed/` (pre-run snapshot), `rerun_console.log`, `rerun_hashes.txt`, `environment.txt`.
