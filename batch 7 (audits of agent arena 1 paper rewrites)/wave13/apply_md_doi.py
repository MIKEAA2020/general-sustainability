#!/usr/bin/env python3
"""Wave-13 Part A: substitute the owner's nine Zenodo DOIs for the anonymous
companion-manuscript placeholder entries in the arena papers' reference lists.

Owner directive (2026-09-06): "substitute these dois for references" - "these"
being the nine Zenodo DOIs the owner registered in the ECOMOD v30 revision
(commit 7d10b03, agent 2 folder, read-only here):

  10.5281/zenodo.22545740  P1  The limits of compensatory aggregation ...
  10.5281/zenodo.22554177  P3  Typed flux ledgers and depletion arithmetic ...
  10.5281/zenodo.22552616  P2  An obstruction calculus ...
  10.5281/zenodo.22554217  P4  Delay-induced regime change in harvested stocks ...
  10.5281/zenodo.22554297  P5  Periodic review as sampled governance ...
  10.5281/zenodo.22552060  E2  Robust viability of the 2J3KL limit reference point ...
  10.5281/zenodo.22553609  E1  Does a surplus-production ladder improve forecasts of Northern cod? ...
  10.5281/zenodo.22553311  E4  Governance operators and viability kernels of the Edwards Aquifer ...
  10.5281/zenodo.22552680  E3  Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? ...

Method (mirrors the owner's own ECOMOD v30 treatment): each placeholder entry
"Author, X., et al., in review. <stand-in title>. Companion ... study." is
replaced by the real bibliographic record - Abaee, A. (2026), the registered
title, Zenodo, and the DOI - set in that paper's own house citation style,
keeping the paper's own companion descriptor tail verbatim. Titles use the
registered title text in each paper's reference-list casing (sentence case for
the E-series lists, matching how the same titles already appear in the papers'
placeholder entries). Two papers also carry entries for a tenth manuscript
("Interval-verified bounds in linear management templates") that has NO DOI
among the nine - those entries stay untouched (no DOI can be invented).

Version discipline: every revision is a NEW version file; the source versions
are never modified. P4 has no companion-citation placeholder entries (its
companion references are body prose only), so no P4 md version is created.

Fail-loud guarantees:
  1. Every placeholder string is found exactly once in its source file.
  2. The new file differs from the source ONLY on the substituted lines
     (asserted via a line-level diff).
  3. The source file is byte-identical before and after the run.
  4. The target filename must not already exist.
"""
from __future__ import annotations

import difflib
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"

# --- substitution table -------------------------------------------------------
# (source md, new md, [(old entry line, new entry line), ...])

SUBS: list[tuple[str, str, list[tuple[str, str]]]] = [
    (
        "paperE1_cod_forecast_ladder_v14",
        "paperE1_cod_forecast_ladder_v15",
        [
            (
                "Author, A., et al., in review. Does a one-pool water-balance "
                "model improve forecasts of Edwards Aquifer head? A scored test "
                "at J-17. Companion forecast-evaluation study (Edwards Aquifer, "
                "Texas).",
                "Abaee, A., 2026. Does a one-pool water-balance model improve "
                "forecasts of Edwards Aquifer head? A scored test at J-17. "
                "Zenodo. https://doi.org/10.5281/zenodo.22552680. Companion "
                "forecast-evaluation study (Edwards Aquifer, Texas).",
            ),
            (
                "Author, B., et al., in review. Periodic review as sampled "
                "governance: sample-and-hold dynamics of assessment-driven "
                "effort control. Companion governance study.",
                "Abaee, A., 2026. Periodic review as sampled governance: "
                "sample-and-hold dynamics of assessment-driven effort control, "
                "a selected 42-stock spectral screen, and the Northern Cod "
                "case. Zenodo. https://doi.org/10.5281/zenodo.22554297. "
                "Companion governance study.",
            ),
        ],
    ),
    (
        "paperE2_cod_intervention_v21",
        "paperE2_cod_intervention_v22",
        [
            (
                "Author, A., et al., in review. A forecast-evaluation scorecard "
                "for a collapsed stock: persistence and the negative "
                "certificate. Companion forecast-evaluation study.",
                "Abaee, A., 2026. Does a surplus-production ladder improve "
                "forecasts of Northern cod? A scored test on NAFO 2J3KL. "
                "Zenodo. https://doi.org/10.5281/zenodo.22553609. Companion "
                "forecast-evaluation study.",
            ),
            (
                "Author, B., et al., in review. Surplus-production intervention "
                "selection under a persistent recharge floor. Companion "
                "intervention study (groundwater object).",
                "Abaee, A., 2026. Governance operators and viability kernels "
                "of the Edwards Aquifer: an intervention-selection test at "
                "J-17. Zenodo. https://doi.org/10.5281/zenodo.22553311. "
                "Companion intervention study (groundwater object).",
            ),
        ],
    ),
    (
        "paperE3_edwards_forecast_ladder_v15",
        "paperE3_edwards_forecast_ladder_v16",
        [
            (
                "Author, A., et al. In review. A forecast-evaluation scorecard "
                "for a collapsed stock: persistence and the negative "
                "certificate. Companion forecast-evaluation study (Northern "
                "cod, NAFO 2J3KL).",
                "Abaee, A. 2026. Does a surplus-production ladder improve "
                "forecasts of Northern cod? A scored test on NAFO 2J3KL. "
                "Zenodo. https://doi.org/10.5281/zenodo.22553609. Companion "
                "forecast-evaluation study (Northern cod, NAFO 2J3KL).",
            ),
        ],
    ),
    (
        "paperE4_edwards_intervention_v13",
        "paperE4_edwards_intervention_v14",
        [
            (
                "Author, A., et al. In review. Does a one-pool water-balance "
                "model improve forecasts of Edwards Aquifer head? A scored test "
                "at J-17. Companion forecast-evaluation study.",
                "Abaee, A. 2026. Does a one-pool water-balance model improve "
                "forecasts of Edwards Aquifer head? A scored test at J-17. "
                "Zenodo. https://doi.org/10.5281/zenodo.22552680. Companion "
                "forecast-evaluation study.",
            ),
            (
                "Author, B., et al. In review. Surplus-production intervention "
                "selection under a persistent productivity floor. Companion "
                "intervention study (Northern cod, NAFO 2J3KL).",
                "Abaee, A. 2026. Robust viability of the 2J3KL limit reference "
                "point under a surplus-production map: policy scoring, "
                "expansion, and when catch cannot help. Zenodo. "
                "https://doi.org/10.5281/zenodo.22552060. Companion "
                "intervention study (Northern cod, NAFO 2J3KL).",
            ),
        ],
    ),
    (
        "paper1_assessment_separation_v22",
        "paper1_assessment_separation_v23",
        [
            (
                "Author, A., et al., in review. Typed flux ledgers and "
                "depletion arithmetic: conservation, componentwise "
                "diagnostics, and the semantics of depletion horizons. "
                "Companion material-ledger study.",
                "Abaee, A. (2026). Typed flux ledgers and depletion "
                "arithmetic: conservation, componentwise diagnostics, and the "
                "semantics of depletion horizons. Zenodo. "
                "https://doi.org/10.5281/zenodo.22554177. Companion "
                "material-ledger study.",
            ),
            (
                "Author, B., et al., in review. Does a surplus-production "
                "ladder improve forecasts of Northern cod? A scored test on "
                "NAFO 2J3KL. Companion scored forecast-evaluation study (the "
                "cod side).",
                "Abaee, A. (2026). Does a surplus-production ladder improve "
                "forecasts of Northern cod? A scored test on NAFO 2J3KL. "
                "Zenodo. https://doi.org/10.5281/zenodo.22553609. Companion "
                "scored forecast-evaluation study (the cod side).",
            ),
            (
                "Author, C., et al., in review. Does a one-pool water-balance "
                "model improve forecasts of Edwards Aquifer head? A scored "
                "test at J-17. Companion scored forecast-evaluation study (the "
                "Edwards Aquifer side).",
                "Abaee, A. (2026). Does a one-pool water-balance model improve "
                "forecasts of Edwards Aquifer head? A scored test at J-17. "
                "Zenodo. https://doi.org/10.5281/zenodo.22552680. Companion "
                "scored forecast-evaluation study (the Edwards Aquifer side).",
            ),
        ],
    ),
    (
        "paper2_obstruction_calculus_v12",
        "paper2_obstruction_calculus_v13",
        [
            (
                "Author, A., et al., in review. A formal separation of weak and "
                "strong sustainability assessment: the limits of compensatory "
                "aggregation. Companion assessment-separation analysis.",
                "Abaee, A.: The limits of compensatory aggregation: a formal "
                "separation of weak and strong sustainability assessment. "
                "Zenodo. https://doi.org/10.5281/zenodo.22545740 (2026). "
                "Companion assessment-separation analysis.",
            ),
        ],
    ),
    (
        "paper3_material_ledgers_v31",
        "paper3_material_ledgers_v32",
        [
            (
                "Author, D., et al., in review. Delay-induced regime change in "
                "harvested stocks: the mobilising and protective channels of "
                "institutional feedback, and the review interval as control. "
                "Companion delay-dynamics study.",
                "Abaee, A., 2026. Delay-induced regime change in harvested "
                "stocks: the mobilising and protective channels of "
                "institutional feedback, and the review interval as control. "
                "Zenodo. https://doi.org/10.5281/zenodo.22554217. Companion "
                "delay-dynamics study.",
            ),
            (
                "Author, E., et al., in review. Periodic review as sampled "
                "governance: sample-and-hold dynamics of assessment-driven "
                "effort control, a selected 42-stock spectral screen, and the "
                "Northern Cod case. Companion review-screen study.",
                "Abaee, A., 2026. Periodic review as sampled governance: "
                "sample-and-hold dynamics of assessment-driven effort control, "
                "a selected 42-stock spectral screen, and the Northern Cod "
                "case. Zenodo. https://doi.org/10.5281/zenodo.22554297. "
                "Companion review-screen study.",
            ),
            (
                "Author, F., et al., in review. The limits of compensatory "
                "aggregation: a formal separation of weak and strong "
                "sustainability assessment. Companion assessment-separation "
                "study.",
                "Abaee, A., 2026. The limits of compensatory aggregation: a "
                "formal separation of weak and strong sustainability "
                "assessment. Zenodo. https://doi.org/10.5281/zenodo.22545740. "
                "Companion assessment-separation study.",
            ),
        ],
    ),
    (
        "paper5_sampled_governance_v25",
        "paper5_sampled_governance_v26",
        [
            (
                "Author, D., et al., in review. Delay-induced regime change in "
                "harvested stocks: the mobilising and protective channels of "
                "institutional feedback. Companion delay-dynamics study.",
                "Abaee, A. 2026. Delay-induced regime change in harvested "
                "stocks: the mobilising and protective channels of "
                "institutional feedback, and the review interval as control. "
                "Zenodo. https://doi.org/10.5281/zenodo.22554217. Companion "
                "delay-dynamics study.",
            ),
        ],
    ),
]


def main() -> int:
    src_digests_before: dict[str, str] = {}
    results = []
    total_subs = 0
    for src_name, new_name, pairs in SUBS:
        src = PR / f"{src_name}.md"
        dst = PR / f"{new_name}.md"
        assert src.exists(), f"missing source {src}"
        assert not dst.exists(), f"target already exists: {dst}"
        text = src.read_text(encoding="utf-8")
        src_digests_before[src_name] = hashlib.md5(src.read_bytes()).hexdigest()

        new_text = text
        for old, new in pairs:
            n = new_text.count(old)
            assert n == 1, f"{src_name}: placeholder found {n} times (expected 1): {old[:60]!r}"
            new_text = new_text.replace(old, new, 1)
            total_subs += 1

        # line-level diff: only the substituted lines may change (blank lines
        # may appear as hunk-internal separators between adjacent changes and
        # are ignored; any other unexpected line still fails the comparison)
        diff = list(difflib.unified_diff(
            text.splitlines(), new_text.splitlines(), lineterm="", n=0,
        ))
        removed = [
            l[1:] for l in diff
            if l.startswith("-") and not l.startswith("---") and l[1:].strip()
        ]
        added = [
            l[1:] for l in diff
            if l.startswith("+") and not l.startswith("+++") and l[1:].strip()
        ]
        assert removed == [old for old, _ in pairs], f"{src_name}: unexpected removed lines"
        assert added == [new for _, new in pairs], f"{src_name}: unexpected added lines"

        dst.write_text(new_text, encoding="utf-8")

        # source untouched
        assert hashlib.md5(src.read_bytes()).hexdigest() == src_digests_before[src_name], \
            f"{src_name}: source file was modified!"

        md5 = hashlib.md5(dst.read_bytes()).hexdigest()
        results.append((src_name, new_name, md5, len(pairs)))
        print(f"  {src_name} -> {new_name}: {len(pairs)} DOI substitution(s), "
              f"md5={md5[:10]}")

    assert total_subs == 15, f"total substitutions {total_subs} != 15"
    print(f"\n{len(results)}/8 new md versions written; {total_subs} reference entries "
          f"now carry the owner's Zenodo DOIs. P4: no substitution (no companion "
          f"reference entries). Interval-verified-template entries left untouched "
          f"(no DOI among the nine).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
