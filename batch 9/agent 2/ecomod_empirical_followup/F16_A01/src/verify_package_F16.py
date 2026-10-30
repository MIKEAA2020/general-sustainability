#!/usr/bin/env python3
"""Freeze/verify only additive F16; never rebuild or run earlier publishers."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "artifact_manifest_F16_A01.json"
POST = {"PUBLICATION_RECEIPT_F16_A01.json"}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def gitsha(payload: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(payload)).encode() + b"\0" + payload).hexdigest()


def load(name: str):
    return json.loads((ROOT / name).read_text())


def files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*") if path.is_file() and not any(part in {".git", ".cache", "__pycache__"} for part in path.relative_to(ROOT).parts) and path.name not in POST | {MANIFEST})


def prior(folder: str) -> Path:
    path = ROOT.parent / folder
    if not path.exists():
        path = ROOT.parent / re.search(r"F\d+_A01", folder)[0]
    require(path.is_dir(), "Prior package missing " + folder)
    return path


def guards() -> int:
    reproduction = load("metadata/reproducibility_F16.json")
    require(reproduction["artifact_count"] == 12 and reproduction["byte_identical_across_consecutive_builds"], "Reproduction scope/count")
    require(reproduction["new_calibrated_national_AGB_comparisons"] == 0, "Unexpected calibrated AGB claim")
    for name, digest in reproduction["files"].items():
        require(sha((ROOT / name).read_bytes()) == digest, "Changed reproduced artifact " + name)
    for name, digest in reproduction["source_scripts"].items():
        require(sha((ROOT / "src" / name).read_bytes()) == digest, "Reproduction source changed " + name)
    for mode in ("normal", "optimized"):
        text = (ROOT / f"evidence/tests_{mode}_F16.log").read_text()
        require(re.search(r"Ran 48 tests in .*\n\nOK\s*$", text) is not None and "FAILED" not in text and "skipped" not in text, "Incomplete tests " + mode)
    quality = load("metadata/deliverable_QA_F16.json")
    require(quality["visual_review_completed"], "Visual review incomplete")
    require((quality["main_figures"], quality["main_tables"], quality["main_result_sections"], quality["SI_figures"], quality["SI_tables"]) == (7, 2, 5, 2, 28), "Editorial allocation drift")
    for kind in ("main", "SI"):
        report = quality[kind]
        require(sha((ROOT / report["file"]).read_bytes()) == report["sha256"], "PDF changed after QA")
        require(not report["text_outside_page_bounds"] and report["all_fonts_embedded"] and report["ORCID_hyperlink"], "PDF QA failed")
        require(quality["visual_review_pages"][kind] == list(range(1, report["pages"] + 1)), "Not every page reviewed")
    require(quality["main"]["AI_declaration"] and quality["keywords"] == 7 and quality["abstract_whitespace_words"] <= 250, "Declaration/keywords/abstract")
    workbook = quality["workbook"]
    require((workbook["sheets"], workbook["inherited_sheets_unchanged"], workbook["new_sheets"], workbook["inherited_cells_checked"]) == (41, 31, 10, 60336), "Workbook inheritance QA")
    require(sha((ROOT / workbook["file"]).read_bytes()) == workbook["sha256"], "Workbook changed after QA")
    linkage = load("metadata/SI_linkage_F16.json")
    require(len(linkage["labels"]) == 30 and set(linkage["labels"]) == set(linkage["main_citations"]) and not linkage["uncited_SI_items"] and not linkage["unknown_main_references"], "Unlinked SI")
    protected = 0
    f15 = load("metadata/protected_F15_identity.json")
    parent = prior(f15["folder"])
    for record in f15["files"]:
        require(sha((parent / record["path"]).read_bytes()) == record["sha256"], "Protected F15 file changed " + record["path"])
        protected += 1
    for package in load("metadata/protected_prior_identity_F15.json"):
        parent = prior(package["folder"])
        for record in package["files"]:
            require(sha((parent / record["path"]).read_bytes()) == record["sha256"], "Protected earlier file changed " + record["path"])
            protected += 1
    require(protected == 667, "Protected count drift")
    provenance = load("metadata/source_provenance_F16.json")
    require(len(provenance["sources"]) == 7 and provenance["CRT_selective_range_listing"]["range_payload_bytes"] == 6160, "Source/CRT provenance")
    summary = load("data/national_physical_module_summary_F16.json")
    require(summary["Cameroon"]["reported_total_forest_area"]["change_2015_to_2020_ha"] == -148732, "Cameroon result changed")
    require(summary["Australia"]["NIR2023_forest_land"]["change_2014_15_to_2021_22_kha"] == 2054, "Australia result changed")
    main = (ROOT / "integrated_F16_A01_main.tex").read_text()
    require("None of the eight calibrated national 2015--2023 forest-AGB analyses is complete" in main and "not forest-AGB stock changes or 2023 endpoints" in main, "Primary scope/flux typing changed")
    for name in ["README_F16_A01.md", "REVISION_AND_MIGRATION_ACCOUNT_F16_A01.md", "CONTENT_COVERAGE_AUDIT_F16_A01.md", "ACCESS_AND_EVIDENCE_WORKAROUNDS_F16_A01.md", "requirements_F16_A01.txt"]:
        require((ROOT / name).is_file(), "Disclosure missing " + name)
    for path in files():
        require(path.suffix not in {".zip", ".dbf", ".shp", ".tif", ".nc", ".nc4"}, "Raw provider payload included " + str(path))
    return protected


def run(write: bool = False) -> dict:
    protected = guards()
    quality = load("metadata/deliverable_QA_F16.json")
    records = []
    for path in files():
        payload = path.read_bytes()
        records.append({"path": str(path.relative_to(ROOT)), "bytes": len(payload), "sha256": sha(payload), "git_blob_sha1": gitsha(payload)})
    if write:
        (ROOT / MANIFEST).write_text(json.dumps({
            "version": "F16_A01",
            "kind": "Additive reported national physical modules; no calibrated national AGB completion",
            "files": records, "file_count": len(records), "manifest_self_excluded": True,
            "post_publication_receipts_excluded": sorted(POST),
            "protected_F15_and_earlier_files_unchanged": protected,
            "original_primary_AGB_analyses_incomplete": 8,
            "new_reported_physical_modules": 2,
        }, indent=2) + "\n")
    else:
        require(records == load(MANIFEST)["files"], "Manifest mismatch/unlisted durable file")
    return {
        "verified_files": len(records), "bytes": sum(row["bytes"] for row in records),
        "protected_F15_and_earlier_files": protected, "tests_per_execution_mode": 48,
        "reproduced_artifacts_byte_identical": 12,
        "new_reported_physical_modules": 2, "new_calibrated_national_AGB_comparisons": 0,
        "original_primary_AGB_analyses_incomplete": 8,
        "main_pages": quality["main"]["pages"], "SI_pages": quality["SI"]["pages"],
        "main_figures": 7, "main_tables": 2, "SI_figures": 2, "SI_tables": 28,
        "all_SI_items_cited": True, "workbook_sheets": 41,
        "one_integrated_publication": True, "manifest_written": write,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    print(json.dumps(run(parser.parse_args().write_manifest), indent=2))
