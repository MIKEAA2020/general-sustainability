#!/usr/bin/env python3
"""Audit the pinned Collection 11 Caatinga accuracy scripts without executing GEE."""
from __future__ import annotations

import hashlib
import json
import pathlib
import sys

C11_PREFIX = "lulc_30m_landsat/collection_11/"
ACCURACY_PREFIX = C11_PREFIX + "src/validation/acuracia/"
REFERENCE_ASSET = "projects/mapbiomas-workspace/VALIDACAO/mapbiomas_85k_col5_points_w_edge_and_edited_v3"


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(snapshot_dir: pathlib.Path, tree_json: pathlib.Path, destination: pathlib.Path) -> None:
    files = {
        "getCSVsPointstoAccGlobarlBacia_2col.py": snapshot_dir / "getCSVsPointstoAccGlobarlBacia_2col.py",
        "runAll_accuracy.py": snapshot_dir / "runAll_accuracy.py",
        "newsMetrics_AccuracySamples.py": snapshot_dir / "newsMetrics_AccuracySamples.py",
        "README.md": snapshot_dir / "README.md",
    }
    text = {name: path.read_text(encoding="utf-8") for name, path in files.items()}
    tree = json.loads(tree_json.read_text(encoding="utf-8"))
    paths = [entry["path"] for entry in tree["tree"] if entry.get("type") == "blob"]
    c11_paths = [path for path in paths if path.startswith(C11_PREFIX)]
    tabular_extensions = (".csv", ".xlsx", ".rds", ".rda", ".parquet")
    c11_tabular = [path for path in c11_paths if path.lower().endswith(tabular_extensions)]
    metrics = text["newsMetrics_AccuracySamples.py"]
    noncomment_metrics = "\n".join(line for line in metrics.splitlines() if not line.lstrip().startswith("#"))

    result = {
        "repository": "mapbiomas/brazil-caatinga",
        "commit": tree["sha"],
        "repository_tree_entries": len(tree["tree"]),
        "collection_11_blob_count": len(c11_paths),
        "source_files": [
            {"path": ACCURACY_PREFIX + name if name != "README.md" else C11_PREFIX + name,
             "bytes": path.stat().st_size, "sha256": sha256(path)}
            for name, path in files.items()
        ],
        "reference_asset_in_both_exporters": all(REFERENCE_ASSET in text[name] for name in ["getCSVsPointstoAccGlobarlBacia_2col.py", "runAll_accuracy.py"]),
        "reference_asset": REFERENCE_ASSET,
        "requested_reference_year_range": [1985, 2025],
        "comment_claims_reference_points_through_2025": "ano final dos pontos de referência disponíveis" in text["getCSVsPointstoAccGlobarlBacia_2col.py"],
        "actual_nonempty_2025_reference_coverage_verified": False,
        "coverage_verification_limit": "The GEE feature collection was not retrieved; a requested CLASS_2025 field and a code comment do not establish non-null 2025 labels.",
        "export_properties": ["BIOMA_250K", "CARTA_2", "DECLIVIDAD", "PESO_AMOS", "LON", "LAT"],
        "annual_reference_fields_requested": "CLASS_1985 through CLASS_2025",
        "map_sampling_scale_metres": 30,
        "drive_export_folder": "ptosAccCol11",
        "caatinga_basins_documented": 49,
        "metrics_drops_weights_and_coordinates": "df_CSV = df_CSV[lstColRef + lstColPred + ['bacia']]" in metrics,
        "metrics_sample_weight_occurrences": noncomment_metrics.count("sample_weight"),
        "metrics_noncomment_peso_amos_occurrences": noncomment_metrics.count("PESO_AMOS"),
        "metrics_legacy_col10_labels_present": "ptosAccCol10" in metrics and "Collection10" in metrics,
        "collection_11_tabular_data_outputs_in_repository": c11_tabular,
        "design_covariance_or_variance_paths_in_collection_11": [path for path in c11_paths if any(term in path.lower() for term in ["covari", "variance", "design"])],
        "assessment": {
            "implementation_route_found": True,
            "reference_microdata_retrieved": False,
            "design_weighted_caatinga_metrics_demonstrated": False,
            "official_national_c11_estimator_identified_from_this_biome_script": False,
            "interpretation": "The scripts generate mapped/reference samples and unweighted accuracy/Pontius summaries. PESO_AMOS is exported but not used by this Caatinga metrics script. This is not a delivered C11 design-covariance workflow and must not be conflated with the separate national brazil-accuracy C110 workflow."
        }
    }
    assert result["reference_asset_in_both_exporters"]
    assert result["metrics_drops_weights_and_coordinates"]
    assert result["metrics_sample_weight_occurrences"] == 0
    assert result["metrics_noncomment_peso_amos_occurrences"] == 0
    assert result["collection_11_blob_count"] == 65
    assert not c11_tabular
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("Usage: audit_brazil_caatinga.py SNAPSHOT_DIR TREE_JSON DESTINATION_JSON")
    main(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]))
