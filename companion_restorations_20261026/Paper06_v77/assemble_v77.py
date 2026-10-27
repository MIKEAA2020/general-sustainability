#!/usr/bin/env python3
"""Assemble the modular Paper06 v77 TeX sources without editing v76 files.

Run from any directory: python /path/to/Paper06_v77/assemble_v77.py
Use --check to verify the checked-in assembled files match the modular parts.
"""
from __future__ import annotations

import argparse
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
PARTS = PACKAGE / "paper06_assessment_separation_v77_src" / "parts"
OUTPUTS = {
    "paper06_assessment_separation_v77.tex": [
        "00_front.tex",
        "01_setting.tex",
        "02_general.tex",
        "03_witness.tex",
        "04_benchmark.tex",
        "04b_related.tex",
        "05_discussion.tex",
        "06_appendix.tex",
        "07_refs.tex",
    ],
    "paper06_assessment_separation_v77_supplementary.tex": [
        "si_00_front_proofs.tex",
        "si_01_extensions.tex",
        "si_02_benchmark_practice.tex",
        "si_03_verification_positioning.tex",
    ],
}


def assemble(names: list[str]) -> str:
    chunks = []
    for name in names:
        path = PARTS / name
        text = path.read_text(encoding="utf-8")
        chunks.append(text.rstrip() + "\n")
    result = "\n".join(chunks)
    if result.count("\\documentclass") != 1:
        raise SystemExit("assembly check failed: expected exactly one \\documentclass")
    if result.count("\\begin{document}") != 1:
        raise SystemExit("assembly check failed: expected exactly one \\begin{document}")
    if result.count("\\end{document}") != 1:
        raise SystemExit("assembly check failed: expected exactly one \\end{document}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare assembled output with existing files; do not write",
    )
    args = parser.parse_args()

    mismatches = []
    for output_name, part_names in OUTPUTS.items():
        target = PACKAGE / output_name
        content = assemble(part_names)
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != content:
                mismatches.append(output_name)
            else:
                print(f"OK: {output_name} matches {len(part_names)} modular parts")
        else:
            target.write_text(content, encoding="utf-8", newline="\n")
            print(f"Wrote {target} from {len(part_names)} modular parts")

    if mismatches:
        print("Mismatch: " + ", ".join(mismatches))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
