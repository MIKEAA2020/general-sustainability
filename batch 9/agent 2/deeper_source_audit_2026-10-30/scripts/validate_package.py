#!/usr/bin/env python3
"""Validate the audit package without network access."""
from __future__ import annotations

import csv
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"


def csv_rows(name: str) -> list[dict]:
    with (EVIDENCE / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "run_canada_diagnostics.py")], check=True, cwd=ROOT, stdout=subprocess.DEVNULL)
    required = [
        "README.md",
        "provider_requests.md",
        "evidence/retrieval_ledger.csv",
        "evidence/canada_source_files.csv",
        "evidence/finland_nid_2026_table_6_4_13_as_printed.csv",
        "evidence/brazil_public_reference_audit.json",
        "scripts/retrieve_canada_wrt.py",
    ]
    checks = {
        "required_files_present": all((ROOT / path).is_file() for path in required),
        "retrieval_ledger_has_25_rows": len(csv_rows("retrieval_ledger.csv")) == 25,
        "canada_source_registry_has_39_rows": len(csv_rows("canada_source_files.csv")) == 39,
        "finland_table_has_10_rows": len(csv_rows("finland_nid_2026_table_6_4_13_as_printed.csv")) == 10,
        "canada_static_summary_has_6_rows": len(csv_rows("canada_static_rollup_summary.csv")) == 6,
        "canada_generator_diagnostics_have_116_rows": len(csv_rows("canada_generator_cell_diagnostics.csv")) == 116,
        "canada_ecozone_rollup_has_58_rows": len(csv_rows("canada_ecozone_to_national_variance_rollup.csv")) == 58,
        "canada_11_diagnostic_assertions_pass": json.loads((EVIDENCE / "canada_diagnostic_assertions.json").read_text())["all_passed"] is True,
        "no_sandbox_links": not any("sandbox:" in path.read_text(encoding="utf-8") for path in [ROOT / "README.md", ROOT / "provider_requests.md"]),
        "no_provider_pdfs_redistributed": not any(path.suffix.lower() == ".pdf" for path in ROOT.rglob("*") if path.is_file()),
    }
    report = {"all_passed": all(checks.values()), "n_checks": len(checks), "checks": checks}
    (EVIDENCE / "package_qa.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
