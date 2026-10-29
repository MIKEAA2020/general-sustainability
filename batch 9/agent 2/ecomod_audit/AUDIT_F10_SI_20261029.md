# Audit of `followup_F10_SI.txt`

**Audited item:** F10 Supplementary Information source, 340 lines / 5,585 words.
**Audit date:** 2026-10-29.
**Comparison target:** `batch 9/agent 2/ecomod_empirical_followup/F10` on `origin/main`. The attached SI is byte-identical to the package's `followup_F10_SI.tex`; the main source is also byte-identical to the attached main manuscript reviewed previously. The package contains the referenced results macro, figures, derived tables, code, source registries, and compiled PDFs.

## Overall assessment

**Technically careful and substantially improves the main paper's methods transparency.** The covariance identities, WGS84 ellipsoid-area integral, extent–density decomposition, cancellation definition, and conditional allocation-set algebra are internally correct. Important limitations are stated plainly: the local cover is mapped classification, zero is not recoded as absence, the allocation intervals are not confidence sets, and neither the account screen nor product access is presented as national physical-change evidence.

I spot-checked the SI's quantitative claims against the F10 package's derived files. The 16-row native-probe coverage CSV supports the reported 65,536 valid cells per endpoint and the stated zero counts; the native SD summary supports the SD-zero counts and quantiles; and the allocation endpoint/difference CSVs reproduce the reported intervals and signs after rounding. The account macro values and matched-source identity are present in the package. These are package-level checks, not a fresh raw-source acquisition or full pipeline rerun.

The principal actionable issue is traceability: the prose says that per-window zero counts are “supplied separately in the coverage table,” but the SI contains no such table and does not name the package CSV. A second, low-severity presentation issue is that intervals and their differences are rounded independently, creating apparent 0.0001–0.01 discrepancies when readers subtract printed endpoints. A short rounding note would make the numerical reporting unambiguous.

## Findings

### 1. Quantitative/methodological checks — No major internal error found

- **Account availability:** `results/availability_numbers.tex` defines 13,652 national rows, 236 identifiers, 183 account-pass identifiers and 53 account-fail identifiers. The package's derived availability data includes 236 identifiers and eight selected countries. The SI correctly distinguishes account availability from physical-boundary compatibility and analytical admission.
- **Native coverage and zero diagnostics:** `data/support/native_probe_coverage.csv` has the eight countries at both endpoints (16 rows), each with 65,536 valid joint AGB/SD cells. Its Brazilian zero-AGB counts are 44,546 (2015) and 44,767 (2023), matching the SI. `data/reference/native_sd_summary_R03.csv` matches the SD-zero totals (45,578 and 45,713), positive-AGB/zero-SD counts (1,032 and 946), zero-AGB/positive-SD counts, and the reported quartiles/medians. These are data-storage diagnostics, not ecological or calibrated-error results, as the SI says.
- **Allocation results:** package CSV values reproduce the endpoint sets and difference bounds. For formations, the unrounded difference set is approximately [−223,971.652, 282,002.018] Mg; for formations plus savanna it is [−178,109.797, 259,533.763] Mg. Both contain zero. Their scope is explicitly conditional on fixed point maps, exact cover/density correspondence, nonnegative but otherwise unrestricted allocation, and no temporal coupling.
- **Displayed arithmetic:** independently rounded endpoints do not always subtract to the displayed difference at the last printed digit. For example, the SI's formations lower endpoints print as 55.2216 and 279.1932 thousand Mg (difference −223.9716), while the difference set prints −223.9717. The underlying CSV values give −223.971652 Mg-thousand, which rounds to −223.9717. Likewise the formations-plus-savanna upper endpoints print as 489.2885 and 229.7548, while the unrounded difference is 259.533763 thousand Mg and prints as 259.5338. This is consistent with independent rounding, not a substantive arithmetic error.
- **Equations:** the temporal-difference variance expression correctly includes both cross-year covariance blocks; the total and average variance formulas distinguish area weights from normalized weights; the WGS84 rectangle integral and full-ellipsoid result are correct; the symmetric extent/density identity expands to \(A_1D_1-A_0D_0\); and the allocation difference interval uses cross-endpoint extremes rather than subtracting like endpoints.
- **LaTeX structure:** all explicit `\ref` targets resolve, there are no duplicate labels, and the source has no unmatched internal table references. The `\input` dependency resolves in the F10 package, not in the text attachment by itself. The package includes compiled PDFs and QA metadata; I did not independently rebuild them.

### 2. Per-window coverage table is referenced but not surfaced — Moderate

**Location:** S7, paragraph immediately after Table `domain` (attached SI line 188).

The sentence says zero counts “are supplied separately in the coverage table.” There is no all-country coverage table in the SI; the only native zero/SD table is the Brazil-specific table later in S7. The promised per-window values are present in the package at `data/support/native_probe_coverage.csv`, but the manuscript does not identify that filename or link to it at this point.

**Action:** identify the CSV path (ideally a stable supplemental-file link), or add a compact eight-country/two-endpoint table of valid and zero counts. Keep the note that probe windows are deterministic access/support screens, not national or forest coverage estimates.

### 3. Rounding convention should be stated — Low

**Locations:** S10, topological support/numerical safeguards and final allocation-results paragraph; corresponding main-text allocation table.

The exact values in the package resolve the apparent last-digit discrepancies. Because the SI prints endpoint and difference values at the same precision, readers may reasonably expect the printed endpoints to subtract exactly.

**Action:** add a note such as: “All difference bounds were calculated from unrounded endpoint bounds; displayed endpoints and differences are rounded independently.” This also resolves the main-text formations-plus-savanna 259.53/259.54 apparent discrepancy.

### 4. Reproduction status — Package present; full independent rerun not completed

The declared F10 URL on `main` resolves to a package containing this exact SI and the referenced macro, figures, derived CSVs, source metadata, code, compiled PDFs, and a manifest. It also records 134 passing tests under both normal and optimized Python execution and PDF QA results. This improves materially on assessing the standalone attachment: its missing `results/` input is supplied by the package.

I attempted `python -m unittest discover -s tests -v` against an extracted copy of the package; it stopped before executing the complete suite because this environment lacks `numpy`, `requests`, and `openpyxl` (additional declared dependencies are in `requirements_F10.txt`). I did not install dependencies or run the TeX build. Thus the repository's test/build records are available but not independently reproduced here. The package does not redistribute raw provider/MapBiomas/reference archives; it supplies source identity, acquisition metadata and derived outputs, so full source-level reproduction still depends on access to those named inputs.

## Scope note carried over from the main audit

The SI reinforces that the work reports availability, territorial/support screening, Brazilian mapped-cover endpoints, reference-input screening, and conditional allocation sets. It explicitly states that no national physical stock changes, conversion associations, change-resolution probabilities, or reporting-rule accuracy estimates are supplied. Accordingly, the framing recommendation in `AUDIT_F10_MAIN_20261029.md` remains: present this as a compatibility/feasibility and partial-identification assessment, or add the analyses needed to support the broader “test of composition masking” framing.

## Bottom line

The SI's formal methods and spot-checked numerical outputs are coherent under their stated assumptions; no substantive equation error was found. Link the native-coverage CSV where the SI currently promises a separate table, state that interval differences use unrounded endpoint values, and retain the strong distinction between conditional allocation bounds and measured ecological change. The F10 package exists on `origin/main` and matches the attachments; the previous main-source audit has been corrected accordingly. Full tests and a fresh TeX build remain unverified in this environment.
