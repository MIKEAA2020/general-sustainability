#!/usr/bin/env python3
"""Rebuild F16 twice if needed and require byte-identical generated artifacts.

No provider extraction, publisher, earlier verifier or visual-review assertion is run.
"""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = [
    "figures/national_physical_modules_F16.pdf",
    "evidence/national_physical_modules_F16.png",
    "national_results_F16_A01.xlsx",
    "metadata/plot_values_F16.json",
    "metadata/workbook_QA_F16.json",
    "integrated_F16_A01_main.tex",
    "integrated_F16_A01_SI.tex",
    "src/national_protocols_inherited_F16.tex",
    "src/SI_reference_numbers_F16.tex",
    "integrated_F16_A01_main.pdf",
    "integrated_F16_A01_SI.pdf",
    "metadata/SI_linkage_F16.json",
]
SCRIPTS = ["build_assets_F16.py", "assemble_additive_F16.py", "build_F16.py"]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> None:
    subprocess.run([sys.executable, str(ROOT / "src/build_assets_F16.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "src/build_F16.py")], check=True)


def run() -> None:
    if not all((ROOT / name).is_file() for name in ARTIFACTS):
        build()
    before = {name: sha(ROOT / name) for name in ARTIFACTS}
    build()
    after = {name: sha(ROOT / name) for name in ARTIFACTS}
    changed = [name for name in ARTIFACTS if before[name] != after[name]]
    if changed:
        raise ValueError("Non-reproduced generated artifacts: " + str(changed))
    report = {
        "version": "F16_A01",
        "files": after,
        "artifact_count": len(after),
        "byte_identical_across_consecutive_builds": True,
        "source_scripts": {name: sha(ROOT / "src" / name) for name in SCRIPTS},
        "provider_extraction_rerun": False,
        "publisher_or_prior_verifier_rerun": False,
        "visual_review_assertion_changed": False,
        "new_reported_physical_modules": ["Cameroon", "Australia"],
        "new_calibrated_national_AGB_comparisons": 0,
    }
    (ROOT / "metadata/reproducibility_F16.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"byte_identical_artifacts": len(after), "new_calibrated_national_AGB_comparisons": 0}, indent=2))


if __name__ == "__main__":
    run()
