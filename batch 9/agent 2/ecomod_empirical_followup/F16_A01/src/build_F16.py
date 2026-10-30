#!/usr/bin/env python3
"""Compile SI first, generate exact cross-document numbers, then compile main."""
from __future__ import annotations
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT.parent / ".cache/F16_build"
LATEX = CACHE / "latex"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def expand(path: Path) -> str:
    text = path.read_text()
    return re.sub(r"\\input\{([^}]+)\}", lambda match: expand(ROOT / (match[1] if match[1].endswith(".tex") else match[1] + ".tex")), text)


def engine() -> list[str]:
    candidate = ROOT.parent / ".cache/F16_bin/tectonic"
    if candidate.exists():
        return [str(candidate), "-k", "--keep-logs"]
    if shutil.which("tectonic"):
        return [shutil.which("tectonic"), "-k", "--keep-logs"]
    if shutil.which("latexmk"):
        return [shutil.which("latexmk"), "-pdf", "-interaction=nonstopmode", "-halt-on-error"]
    raise FileNotFoundError("Install Tectonic 0.17+ or latexmk to compile the manuscript")


def compile_doc(kind: str) -> None:
    stem = "integrated_F16_A01_" + kind
    log_path = CACHE / (kind + "_build.log")
    command = engine()
    command += ["-o", str(LATEX), stem + ".tex"] if Path(command[0]).name == "tectonic" else ["-outdir=" + str(LATEX), stem + ".tex"]
    with log_path.open("w") as log:
        subprocess.run(command, cwd=ROOT, env=dict(os.environ, SOURCE_DATE_EPOCH="1793318400"), stdout=log, stderr=subprocess.STDOUT, check=True)
    shutil.copyfile(LATEX / (stem + ".pdf"), ROOT / (stem + ".pdf"))


def run() -> None:
    LATEX.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / "src/assemble_additive_F16.py")], check=True)
    compile_doc("SI")
    aux = (LATEX / "integrated_F16_A01_SI.aux").read_text()
    labels = dict(re.findall(r"\\newlabel\{((?:tab|fig):[^}]+)\}\{\{([^}]+)\}", aux))
    lines = ["\\newcommand{\\SIref}[1]{\\csname SIlabel:#1\\endcsname}"]
    for name, num in sorted(labels.items()):
        lines.append("\\expandafter\\def\\csname SIlabel:" + name + "\\endcsname{" + num + "}")
    (ROOT / "src/SI_reference_numbers_F16.tex").write_text("\n".join(lines) + "\n")
    main = (ROOT / "integrated_F16_A01_main.tex").read_text()
    cited = set(re.findall(r"\\SIref\{([^}]+)\}", main))
    missing = set(labels) - cited
    unknown = cited - set(labels)
    require(not missing, "Uncited SI items " + str(sorted(missing)))
    require(not unknown, "Unknown SI reference " + str(sorted(unknown)))
    (ROOT / "metadata/SI_linkage_F16.json").write_text(json.dumps({
        "labels": labels, "main_citations": sorted(cited),
        "uncited_SI_items": sorted(missing), "unknown_main_references": sorted(unknown),
        "every_SI_figure_and_table_cited_in_main": True,
    }, indent=2) + "\n")
    compile_doc("main")
    for kind in ("main", "SI"):
        log = (LATEX / ("integrated_F16_A01_" + kind + ".log")).read_text()
        bad = [line for line in log.splitlines() if "Overfull" in line or "undefined" in line.lower() or "LaTeX Error" in line]
        require(not bad, "Typesetting diagnostics " + kind + ": " + str(bad))
    print("Compiled both F16 PDFs; every SI figure/table is explicitly cited in main.")


if __name__ == "__main__":
    run()
