# ECOMOD “A rising biocapacity total” — C19 coverage and redistribution audit

**Date:** 31 October 2026  
**Verdict:** **No further main/SI redistribution or restorative manuscript edit is warranted.** The published C19 main/SI division is complete on the actual C18→C19 source evidence. No core finding is SI-only, no remaining specialist-only main block needs relocation on its merits, and no accidental content omission was found.

This was a new source-to-source audit, not a restatement of the C19 editorial summary. The complete 248-line main patch and 33-line SI patch were reviewed, structural inventories were compared, compressed passages were traced to their retained locations, numerical tokens were screened, and the anomalous endpoint display was checked against the row-level data.

## 1. Structural coverage

| Object | C18 | C19 | Result |
|---|---:|---:|---|
| Main labels | 52 | 52 | Same ordered labels |
| SI labels | 54 | 54 | Same ordered labels |
| Main section/subsection titles | 22 | 22 | Unchanged |
| SI section/subsection titles | 37 | 37 | Unchanged |
| Main bibliography records | 45 | 45 | Same keys; three authorized companion replacements |
| SI bibliography records | 12 | 12 | Same keys; two authorized companion replacements |
| Main equations | 17 | 17 | All retained |
| SI equations | 5 | 5 | All retained |
| Main tables / figures | 6 / 3 | 6 / 3 | Retained; yield sweep delegated without data loss |
| SI tables / figures | 18 / 5 | 18 / 5 | All retained and explicitly cited in main |

No combined main/SI citation key was lost. The SI still has eleven top-level sections and no separate Discussion section. C19 retains four main propositions and four concise proof sketches; full derivations remain in SI S2 and S9.

## 2. Placement review by content

| Content | Correct current placement | Audit finding |
|---|---|---|
| Complete two-land model, feedbacks, parameters, data definitions, and numerical scope | Main Methods; specialist notation and node-level diagnostics in SI S1/S3 | Main remains self-contained. No missing model equation or essential implementation qualification. |
| Four propositions | Main, with concise proof sketches | Full derivations and branch qualifications remain in SI S2/S9. No further move needed. |
| Baseline masking, floor approach, debt, recovery, identification, and budgets | Main Results and main Figs./Tables | Essential values and conclusions remain main. Full sweeps, grids, gate policies, witnesses, four-condition budgets, and refinement remain appropriately in SI. |
| NFA aggregate, per-person, and component evidence | Main Results, Figs. 2–3 and Table 5 | Complete empirical story remains main. Same-edition endpoint detail and proxy-anchor sensitivity remain in SI Tables S8–S9. |
| P1–P5 and test requirements | Main | Operational estimands, rejection rules, sampling, and uncertainty treatment remain in SI Table S18/S11. |
| One-stock comparator | SI S7, with explicit main qualification | Correctly auxiliary. Its full trajectory, masking example, delay pair, basin grid, equilibrium equation, and parameter qualifications remain in SI; moving them into main would blur the two-land result. |
| Technology-wave control | SI S8 | Main retains the essential matched peak-debt result and cites Table S13/Fig. S5. |
| Physical-stock measurement specification | SI Table S12 | It is explicitly unpopulated. The main retains the measurement limitation and does not imply an empirical inventory. |
| Discussion, limitations, conclusions | Main | No SI-only conclusion or extended SI discussion exists. |

All **18 SI tables and 5 SI figures** are named at relevant main-text points. Promoting auxiliary comparator/control floats merely to raise the main figure count would weaken rather than improve the division.

## 3. Compression and omission audit

- **Numerical implementation:** exact tested-array equality, interpolation errors (`7.1×10⁻⁵` and `8.9×10⁻⁶`), and full-state refinement values (`0.00221`, `0.00102`, `0.000831`, `0.000924`, and the other state errors) remain in SI S3. The main retains the algorithm, history, constraints, timestep, and validation boundary.
- **Yield sweep:** all four yield rows, both eigenvalues, balance-branch slopes, and demand ceilings remain in SI Table S3. The main retains the baseline result and sweep conclusion.
- **Proofs:** no proposition, assumption, equation, or result was removed. Special-detail derivations remain in SI S2 and S9.
- **One-stock comparator:** the equilibrium equation, monotonicity condition, delay/root qualifications, complete figures, and numerical diagnostics remain in SI S7.
- **Discussion compression:** repeated NFA and baseline values remain in Results and, where needed, Conclusions. This is non-duplication, not evidence deletion.
- **References:** only the authorized companion records and unverified inherited section/theorem locators changed. No unused SI `Abaee2026c` record was introduced.

## 4. Numerical-token screen and the `0.807659` exception

After removing hyperlink targets, only three unique numeric tokens from C18 main were absent from the combined live C19 main/SI:

1. **`1.1` and `10.1`:** superseded companion section locators. They were deliberately replaced with content-based DOI-linked descriptions; restoring them would reintroduce unverified pinpoints.
2. **`0.807659`:** do **not** restore this as the selected delayed-quality baseline endpoint. Row-level data show:
   - current-quality comparator: `Ac_end = 0.8076587446814144`, which rounds to `0.807659`;
   - selected delayed-quality run: `Ac_end = 0.8076571663098769`, which rounds to `0.807657` at six decimals and `0.808` at three decimals.

C18’s repeated Discussion display therefore matched the comparator’s six-decimal rounding, not the selected run’s. C19’s `0.808` is correct for the selected run, and the selected area decline remains `46.16%` after rounding. The full-precision selected value remains in `data/quality_law_comparison_C18_A01.csv`. This is a **deliberate non-restoration**, not lost numerical evidence and not a reason for a new manuscript version.

The token screen was used only as an exception finder; the conclusion also rests on manual patch review, structural checks, retained-content checks, the 60/60 C19 tests in both Python modes, and the passed live-reproduction evidence.

## 5. Final decision

There is nothing further that should be moved between main and SI. There is also no omitted passage or numerical display that requires restoration. C19 remains unchanged at **39 main pages and 31 SI pages**, with its complete model, evidence, conclusions, limitations, specialist derivations, robustness material, full tables, and reproduction package intact.

Machine-readable evidence: `metadata/ecomod_coverage_audit.json`  
Re-runnable check: `python code/verify_ecomod_coverage.py`
