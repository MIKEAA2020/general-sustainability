#!/usr/bin/env python3
"""Verify GA01 science, output geometry, reproducibility, cleanup, and frozen releases."""
from pathlib import Path
import argparse
import csv
import hashlib
import importlib.util
import json
import math
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
GA = ROOT / "graphical_abstract_GA01"
SNAPSHOT = GA / "source_snapshot"
STEM = GA / "ecomod_C19_GA01_graphical_abstract"
CLAIMS_PATH = GA / "graphical_abstract_claims_C19_GA01.json"
RESULT_PATH = ROOT / "metadata/verification_result.json"
FORMATS = ("png", "pdf", "svg", "tiff")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(actual, expected, tolerance=1e-11):
    require(math.isclose(float(actual), float(expected), rel_tol=tolerance, abs_tol=tolerance),
            f"Numerical mismatch: {actual} != {expected}")


def output_hashes():
    return {suffix: sha256(STEM.with_suffix("." + suffix)) for suffix in FORMATS}


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_manifest(root, manifest_name):
    manifest_path = root / manifest_name
    manifest = json.loads(manifest_path.read_text())
    for row in manifest["files"]:
        path = root / row["path"]
        require(path.is_file(), f"Frozen file missing: {path}")
        data = path.read_bytes()
        require(len(data) == row["bytes"], f"Frozen file size changed: {path}")
        require(hashlib.sha256(data).hexdigest() == row["sha256"], f"Frozen file hash changed: {path}")
    return {
        "path": str(root),
        "manifest": manifest_name,
        "manifest_sha256": sha256(manifest_path),
        "files_verified": len(manifest["files"]),
        "status": "PASS",
    }


def verify(workspace_root, rebuild=False, skip_workspace_checks=False):
    sys.dont_write_bytecode = True
    rebuild_result = None
    if rebuild:
        command = [sys.executable, "-W", "error", str(GA / "build_graphical_abstract_C19_GA01.py")]
        environment = dict(__import__("os").environ, PYTHONDONTWRITEBYTECODE="1")
        subprocess.run(command, check=True, capture_output=True, text=True, env=environment)
        first = {**output_hashes(), "claims": sha256(CLAIMS_PATH)}
        subprocess.run(command, check=True, capture_output=True, text=True, env=environment)
        second = {**output_hashes(), "claims": sha256(CLAIMS_PATH)}
        require(first == second, "GA01 rebuild is not byte-identical")
        rebuild_result = {"performed": True, "byte_identical": True, "hashes": second}

    claims = json.loads(CLAIMS_PATH.read_text())
    require(claims["version"] == "C19_GA01", "Wrong claims version")
    require(claims["canvas"] == {"width_px": 1328, "height_px": 531, "dpi": 200}, "Canvas metadata changed")

    source_paths = {
        "selected_model_code": SNAPSHOT / "code/reproduce_two_land_C18_A01.py",
        "empirical_endpoints": SNAPSHOT / "data/empirical_endpoints_C18_A01.csv",
        "empirical_components": SNAPSHOT / "data/empirical_components_C18_A01.csv",
        "quality_law_comparison": SNAPSHOT / "data/quality_law_comparison_C18_A01.csv",
    }
    for key, path in source_paths.items():
        require(sha256(path) == claims["source_hashes"][key], f"Source snapshot differs: {key}")

    # Independently recompute the selected delayed-quality fixed-demand trajectory.
    twoland = load_module(source_paths["selected_model_code"], "ga01_verification_twoland")
    a = twoland.run(1.5, 1.5, 0.0, 250.0, 0.05, Efixed=0.825)
    mask = (np.diff(a[:, 6]) > 0) & (np.diff(a[:, 1]) < 0)
    j = int(np.flatnonzero(mask)[-1] + 1)
    yc = (0.05 + 0.064 * a[:, 2] * (1 - a[:, 2])) * a[:, 1]
    baseline = claims["baseline"]
    close(baseline["mask_end_yr"], j * 0.05)
    close(baseline["B_end_gha"], a[j, 6])
    close(baseline["B_change_pct"], 100 * (a[j, 6] / a[0, 6] - 1))
    close(baseline["Ac_end_ha"], a[j, 1])
    close(baseline["Ac_change_pct"], 100 * (a[j, 1] / a[0, 1] - 1))
    close(baseline["capital_contribution_end_gha"], yc[j])
    close(baseline["capital_contribution_change_pct"], 100 * (yc[j] / yc[0] - 1))
    require(baseline["fixed_demand_gha"] == 0.825 and baseline["restoration"] == "off", "Run scope changed")
    require(round(baseline["B_change_pct"]) == 39, "Rounded account-total claim changed")
    require(round(baseline["Ac_change_pct"], 2) == -46.16, "Rounded capital-area claim changed")
    require(round(baseline["capital_contribution_change_pct"], 2) == -51.72, "Rounded capital-contribution claim changed")

    # Independently read the primary 1961–2023 NFA endpoint/component fields.
    with source_paths["empirical_endpoints"].open(newline="") as handle:
        endpoints = {int(row["year"]): row for row in csv.DictReader(handle)}
    with source_paths["empirical_components"].open(newline="") as handle:
        components = {(int(row["year"]), row["component"]): row for row in csv.DictReader(handle)}
    nfa = claims["NFA_primary_1961_2023"]
    require(nfa["window"] == "1961–2023" and nfa["excluded_estimate_years"] == [2024, 2025], "NFA window changed")
    close(nfa["B_change_pct"], endpoints[2023]["B_change_pct"])
    close(nfa["B_per_person_change_pct"], endpoints[2023]["BP_change_pct"])
    close(nfa["cropland_ratio"], components[(2023, "crop")]["ratio"])
    close(nfa["forest_ratio"], components[(2023, "forest")]["ratio"])
    close(nfa["built_up_ratio"], components[(2023, "built")]["ratio"])

    # Check raster geometry/mode/resolution and vector page geometry.
    raster_checks = {}
    for suffix in ("png", "tiff"):
        with Image.open(STEM.with_suffix("." + suffix)) as image:
            require(image.size == (1328, 531), f"{suffix} dimensions differ")
            require(image.mode == "RGB", f"{suffix} is not opaque RGB")
            dpi = image.info.get("dpi")
            require(dpi and all(abs(float(value) - 200) < 0.01 for value in dpi), f"{suffix} DPI differs")
            if suffix == "tiff":
                require(image.info.get("compression") == "tiff_lzw", "TIFF is not LZW compressed")
            raster_checks[suffix] = {"size": list(image.size), "mode": image.mode,
                                     "dpi": [float(value) for value in dpi],
                                     "compression": image.info.get("compression")}
    pdf = STEM.with_suffix(".pdf").read_bytes()
    require(pdf.startswith(b"%PDF-"), "PDF signature missing")
    match = re.search(rb"/MediaBox\s*\[\s*0\s+0\s+([0-9.]+)\s+([0-9.]+)\s*\]", pdf)
    require(match is not None, "PDF MediaBox missing")
    close(float(match.group(1)), 1328 / 200 * 72, 1e-8)
    close(float(match.group(2)), 531 / 200 * 72, 1e-8)
    require(b"/CreationDate (D:20261031000000Z)" in pdf, "PDF date is not pinned")
    svg_text = STEM.with_suffix(".svg").read_text()
    svg_root = ET.fromstring(svg_text)
    require(svg_root.attrib["width"] == "478.08pt" and svg_root.attrib["height"] == "191.16pt", "SVG geometry differs")
    require(svg_root.attrib["viewBox"] == "0 0 478.08 191.16", "SVG viewBox differs")
    require("<dc:date>2026-10-31</dc:date>" in svg_text, "SVG date is not pinned")
    for required in ("1961–2023 COMPLETE OBSERVATIONS", "No universal collapse or delay threshold",
                     "Model and NFA evidence remain separate"):
        require(required in svg_text, f"Required graphical-abstract scope text missing: {required}")
    for obsolete in ("small standing value", "big standing value", "1961–2022", "collapse trigger is demand"):
        require(obsolete not in svg_text, f"Obsolete wording remains: {obsolete}")

    cleanup = json.loads((ROOT / "metadata/provider_pdf_cleanup_result.json").read_text())
    require(cleanup["status"] == "PASS" and cleanup["deleted_local_provider_pdfs"] == 4, "Cleanup status changed")
    require(cleanup["no_other_files_deleted"] is True, "Cleanup scope changed")
    require(cleanup["bytes_freed"] == sum(row["bytes"] for row in cleanup["files"]) == 11078811,
            "Cleanup byte total differs")
    require(cleanup["workspace_logical_bytes_immediately_before_deletion"] - cleanup["bytes_freed"]
            == cleanup["workspace_logical_bytes_after"], "Cleanup workspace arithmetic differs")
    for row in cleanup["files"]:
        require(row["fresh_provider_copy_byte_identical"] is True, "A provider copy was not exact")
        require(row["url"].startswith("https://") and len(row["sha256"]) == 64, "Provider recovery metadata incomplete")

    frozen = []
    if not skip_workspace_checks:
        for row in cleanup["files"]:
            require(not (workspace_root / row["path"]).exists(), f"Deleted provider PDF returned: {row['path']}")
        for relative in cleanup["text_extracts_retained"]:
            require((workspace_root / relative).is_file(), f"Retained text extract missing: {relative}")
        require((workspace_root / cleanup["retrieval_script"]).is_file(), "Original retrieval workflow missing")
        c19_root = workspace_root / "ecomod_editorial_division_C19_A01"
        for key, path in source_paths.items():
            original = c19_root / str(path.relative_to(SNAPSHOT))
            require(original.is_file() and original.read_bytes() == path.read_bytes(),
                    f"Source snapshot is not byte-identical to frozen C19: {key}")
        frozen = [
            check_manifest(workspace_root / "ecomod_audit_remediation_C18_A01", "artifact_manifest_C18_A01.json"),
            check_manifest(workspace_root / "ecomod_editorial_division_C19_A01", "artifact_manifest_C19_A01.json"),
            check_manifest(workspace_root / "ecomod_C19_coverage_and_workspace_R01", "artifact_manifest.json"),
        ]
        require(not (workspace_root / "ecomod_editorial_division_C19_A01/graphical_abstract_GA01").exists(),
                "The frozen C19 root contains the new GA01 directory")

    manifest_path = ROOT / "artifact_manifest.json"
    packaged_manifest = None
    if manifest_path.exists():
        packaged_manifest = check_manifest(ROOT, "artifact_manifest.json")

    return {
        "date": "2026-10-31",
        "version": "ECOMOD_GA01_provider_cleanup_R02",
        "status": "PASS",
        "rebuild": rebuild_result,
        "selected_model_recomputed": True,
        "NFA_1961_2023_fields_recomputed": True,
        "source_snapshot_hashes_verified": True,
        "source_snapshot_matches_frozen_C19": None if skip_workspace_checks else True,
        "output_hashes": output_hashes(),
        "raster_checks": raster_checks,
        "vector_checks": "PASS",
        "obsolete_wording_absent": True,
        "provider_pdf_cleanup_verified": True,
        "deleted_provider_pdfs_absent": None if skip_workspace_checks else True,
        "frozen_release_manifests": frozen,
        "package_manifest": packaged_manifest,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=ROOT.parent)
    parser.add_argument("--rebuild", action="store_true", help="Build twice and require byte-identical outputs")
    parser.add_argument("--skip-workspace-checks", action="store_true", help="Use for a standalone downloaded package")
    parser.add_argument("--write-result", action="store_true")
    args = parser.parse_args()
    result = verify(args.workspace_root, args.rebuild, args.skip_workspace_checks)
    if args.write_result:
        RESULT_PATH.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
