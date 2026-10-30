#!/usr/bin/env python3
"""Offline QA for the publishable follow-up addendum."""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
E = ROOT / "evidence"


def rows(name):
    with (E / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    required = [
        "README.md", "provider_requests_update.md",
        "evidence/brazil_caatinga_c11_code_audit.json",
        "evidence/indonesia_toolkit_inventory.json",
        "evidence/indonesia_toolkit_inventory.csv",
        "evidence/finland_luke_appendix_A_examples_as_printed.csv",
        "evidence/finland_luke_report_assessment.json",
        "evidence/finland_transcription_verification.json",
        "evidence/canada_nfi_followup.json",
        "evidence/retrieval_ledger.csv", "evidence/source_files.csv",
        "evidence/local_source_documents.csv",
        "scripts/retrieve_followup_sources.py", "scripts/audit_brazil_caatinga.py",
        "scripts/extract_indonesia_toolkit_inventory.js",
        "scripts/build_finland_appendix_examples.py",
        "scripts/verify_finland_transcription.py",
    ]
    inventory = json.loads((E / "indonesia_toolkit_inventory.json").read_text())
    brazil = json.loads((E / "brazil_caatinga_c11_code_audit.json").read_text())
    finland = json.loads((E / "finland_luke_report_assessment.json").read_text())
    transcription = json.loads((E / "finland_transcription_verification.json").read_text())
    canada = json.loads((E / "canada_nfi_followup.json").read_text())
    fin_rows = rows("finland_luke_appendix_A_examples_as_printed.csv")
    table_counts = {table: sum(row["table"] == table for row in fin_rows) for table in ["A2", "A3", "A4", "A5"]}
    value_types = {row["value_type"] for row in fin_rows}
    docs = rows("local_source_documents.csv")
    registry = rows("source_files.csv")
    registry_by_path = {row["path"]: row for row in registry}

    checks = {
        "required_files_present": all((ROOT / path).is_file() for path in required),
        "no_provider_pdfs_in_payload": not any(path.suffix.lower() == ".pdf" for path in ROOT.rglob("*") if path.is_file()),
        "no_sandbox_links": not any("sandbox:" in (ROOT / name).read_text(encoding="utf-8") for name in ["README.md", "provider_requests_update.md"]),
        "no_private_credential_material": not any(re.search(r"ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|GITHUB_PAT=\S{10,}", path.read_text(encoding="utf-8", errors="ignore")) for path in ROOT.rglob("*") if path.is_file()),
        "retrieval_ledger_20_rows": len(rows("retrieval_ledger.csv")) == 20,
        "source_registry_44_rows": len(registry) == 44,
        "four_local_only_pdfs_registered": len(docs) == 4 and all(row["redistributed_to_github"] == "false" for row in docs),
        "local_document_hashes_match": all(sha256(pathlib.Path(row["local_path"])) == row["sha256"] for row in docs),
        "indonesia_exact_asset_counts": inventory["summary"]["product_assets"] == 16 and inventory["summary"]["lulc_assets"] == 10 and inventory["summary"]["fire_assets"] == 6 and inventory["summary"]["territory_assets"] == 24,
        "indonesia_csv_40_rows": len(rows("indonesia_toolkit_inventory.csv")) == 40,
        "indonesia_c41_coverage_only_1988_2024": any(row["collection"] == "collection-4.1" and row["asset_role"] == "integration" and row["period_count"] == 37 and row["periods"][0] == "1988" and row["periods"][-1] == "2024" for row in inventory["assets"]),
        "indonesia_no_reference_tvi_asset": inventory["summary"]["reference_or_tvi_assets"] == 0,
        "brazil_reference_export_but_no_weighted_metrics": brazil["reference_asset_in_both_exporters"] and brazil["metrics_drops_weights_and_coordinates"] and brazil["metrics_sample_weight_occurrences"] == 0 and brazil["metrics_noncomment_peso_amos_occurrences"] == 0,
        "brazil_no_c11_tabular_outputs_and_65_blobs": brazil["collection_11_blob_count"] == 65 and not brazil["collection_11_tabular_data_outputs_in_repository"],
        "brazil_2025_coverage_not_overclaimed": brazil["requested_reference_year_range"] == [1985, 2025] and brazil["actual_nonempty_2025_reference_coverage_verified"] is False,
        "finland_174_example_cells": len(fin_rows) == 174 and table_counts == {"A2": 66, "A3": 15, "A4": 15, "A5": 78},
        "finland_printed_value_types_preserved": value_types == {"U_percent_as_printed", "SD_as_printed", "correlation"},
        "finland_174_cells_match_both_source_editions": transcription["all_passed"] is True and transcription["csv_rows"] == 174 and all(item["numeric_cells_compared"] == 174 and item["all_match"] for item in transcription["editions"].values()),
        "finland_not_misrepresented_as_national_covariance": finland["target_estimand_assessment"]["numeric_national_NFI12_NFI13_AGB_endpoint_covariance_retrieved"] is False and finland["target_estimand_assessment"]["current_model_uncertainty_information_found"] is True,
        "finland_edition_not_double_counted": finland["edition_comparison"]["appendix_A_pdf_pages_62_68_text_identical"] is True and len(finland["edition_comparison"]["different_pdf_pages_after_running_header_normalization"]) == 3,
        "canada_urls_and_document_roles": canada["url_checks"][0]["http_status"] == 404 and canada["url_checks"][1]["http_status"] == 200 and "2004-09-03" in canada["process_11a"] and "2006-08-08" in canada["process_11b"],
        "canada_generator_values_match_frozen_audit": canada["current_generator_evidence_from_published_audit"]["national_and_ecozone_files"] == 58 and abs(canada["current_generator_evidence_from_published_audit"]["forest_change_point_sum_million_tonnes"] - 19.066) < 1e-9 and canada["current_generator_evidence_from_published_audit"]["forest_change_RSE_matches_within_0_02_percentage_points"] == "1/57",
        "python_scripts_parse": all(ast.parse(path.read_text(encoding="utf-8")) is not None for path in (ROOT / "scripts").glob("*.py")),
        "javascript_syntax_valid": subprocess.run(["node", "--check", str(ROOT / "scripts/extract_indonesia_toolkit_inventory.js")], capture_output=True).returncode == 0,
        "finland_builder_reproduces_csv": True,
        "source_registry_doc_hashes_agree": all(registry_by_path[row["local_path"]]["sha256"] == row["sha256"] for row in docs),
    }

    # Rebuild the Finnish transcription to a temporary path and compare bytes.
    temporary = ROOT / ".qa_finland_examples.csv"
    try:
        subprocess.run(["python3", str(ROOT / "scripts/build_finland_appendix_examples.py"), str(temporary)], check=True, capture_output=True)
        checks["finland_builder_reproduces_csv"] = temporary.read_bytes() == (E / "finland_luke_appendix_A_examples_as_printed.csv").read_bytes()
    finally:
        temporary.unlink(missing_ok=True)

    report = {"all_passed": all(checks.values()), "n_checks": len(checks), "n_passed": sum(checks.values()), "checks": checks}
    (E / "package_qa.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
