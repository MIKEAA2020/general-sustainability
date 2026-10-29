# Follow-up F04 — Ecological assets behind improving accounts

**A boundary-matched test of composition masking — developing empirical study**

- [Main manuscript — F04](followup_F04_main.pdf), [LaTeX](followup_F04_main.tex)
- [Supplementary Information — F04](followup_F04_SI.pdf), [LaTeX](followup_F04_SI.tex)
- [Physical sample/support report](PHYSICAL_SAMPLE_F04.md)
- [Current admission/hold table](data/support/physical_admission_F04.csv)

F04 advances the physical-sample step with eight pinned candidate boundary objects, a geographic-domain intersection database, a territorial crosswalk, a forest-observation endpoint check, and sixteen bounded native-resolution biomass coverage probes. It does **not** finalize the analytical forest sample or estimate national asset changes. All eight candidate account records remain available; all eight physical admissions remain on hold, with no permanent exclusions. The paper remains the intended empirical study, not a replacement design-only publication.

Primary manuscript and SI filenames now carry `F04` explicitly. F03, earlier follow-up versions and the ECOMOD revisions are unchanged.

## New evidence and its limits

- The selected Canadian polygon extends above the native product's 80 N boundary: approximately 1.2363% of polygon area is outside that latitude domain. This is not a missing-forest percentage or an estimate of omitted biomass.
- The French geometry is metropolitan-European, while several overseas territories are separately tabulated in the account workbook. Australian outlying components and other territorial conventions require explicit matching; ISO-code agreement is insufficient.
- The examined CDS land-cover catalogue and retrieval form end in 2022, leaving a 2023 endpoint gap **for that product**. Other national or global observations are not ruled out. Neither study interval has been silently changed.
- All sixteen 256-by-256 native endpoint windows contain finite, in-range AGB and AGB-SD values. Observed zeros are retained separately. This deterministic access/coverage result is not national coverage, independent forest extent, biomass-change validation or analytical eligibility.

## Reproduce

```sh
python -m pip install -r requirements.txt
# Inherited account availability and coarse metadata audit (three frozen inputs):
python src/data_suitability.py --cache /your/external/original-input-cache --download
# Geography from bundled, hash-verified full published TopoJSON objects:
python src/physical_support.py
python src/territorial_crosswalk.py --workbook /your/external/original-input-cache/NEFBA_2026.xlsx
# Bounded native endpoint queries; at most 25 MB per response, never a global raster:
python src/native_coverage_probes.py --cache /your/external/native-probe-cache
python -m unittest discover -s tests -v
bash src/build.sh
```

The representative point is selected from the largest supported polygon by longitude–latitude planar area; it is a geometry-only navigation choice, not an area-weighted national or forest sampling design. The plan was frozen before native payload requests and must not be reselected after observing coverage. The original protocol snapshot and the pre-payload freeze record are retained. Later reruns must respect the recorded query hashes; provider drift requires a separately documented source update, not silent replacement.

Geographic polygon areas and 1-degree planning fractions can contain waters and boundary uncertainty. The planning grid must **not** be used as a forest mask or a shortcut for national stock estimation. Appropriate country/land/forest support, complete native coverage and covariance-aware change validation are still required.

## Source scopes, licences and operational records

- `metadata/source_registry.json`, `results/data_suitability.json` and `metadata/biomass_metadata.json` retain the narrower inherited account/coarse-metadata audit scope. Their statements that coarse biomass values were not read do not describe the new native probes.
- `metadata/physical_source_registry.json`, `metadata/native_probe_provenance.json` and the support tables describe F04's additional inputs and computations.
- `protocol/PHYSICAL_SUPPORT_F04.md` records the bounded-probe specification; `protocol/STUDY_PROTOCOL.md` is the current working design. These are not externally registered preregistrations.
- `REMAINING_EMPIRICAL_WORK.md` separates completed screening from the unfinished physical sample and later empirical work.
- `metadata/SOURCE_USE.md` and `metadata/BOUNDARY_LICENCES.md` provide attribution and per-source licence information. Account adaptations are CC BY-SA 4.0; OSM-derived boundary support databases are ODbL 1.0. Original boundary contents retain their upstream terms. Raw biomass responses, the biomass guide and provider implementation are not redistributed.

The original estimand kernels remain unchanged. Tests and compilation establish scoped computational consistency, not scientific validation of stock change. Production history and revision records remain outside the journal articles. Compilation requires latexmk, xurl, recommended fonts, CM-Super and the declared LaTeX packages. `artifact_manifest.json` excludes itself and lists distributed file hashes; PDF byte hashes may differ after recompilation.
