"""Live-test all three numerical pipelines in a disposable C19 copy.

The final package is never used as the output directory. Numerical data and PNG
figures must be byte-identical to the frozen artifacts. PDF figures may differ
in container metadata, so their page geometry and extracted content are checked.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

from pypdf import PdfReader

R = Path(__file__).resolve().parents[1]
COMMANDS = [
    "reproduce_empirical_C18_A01.py",
    "reproduce_two_land_C18_A01.py",
    "reproduce_comparator_C18_A01.py",
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pdf_signature(path):
    reader = PdfReader(str(path))
    return [
        {
            "width": float(page.mediabox.width),
            "height": float(page.mediabox.height),
            "text": page.extract_text() or "",
        }
        for page in reader.pages
    ]


def main():
    cache = R / ".cache"
    cache.mkdir(exist_ok=True)
    logs = {}
    with tempfile.TemporaryDirectory(prefix="c19_reproduction_", dir=cache) as tmp:
        work = Path(tmp) / "package"
        shutil.copytree(R, work, ignore=shutil.ignore_patterns(".cache"))
        for script in COMMANDS:
            run = subprocess.run(
                [sys.executable, "code/" + script],
                cwd=work,
                capture_output=True,
                text=True,
                timeout=900,
            )
            logs[script] = run.stdout + run.stderr
            if run.returncode:
                (R / "evidence" / f"reproduction_{script}.log").write_text(logs[script])
                raise RuntimeError(f"Reproduction failed: {script}\n{logs[script][-3000:]}")

        data_original = sorted((R / "data").glob("*"))
        data_equal = []
        for original in data_original:
            generated = work / "data" / original.name
            if not generated.exists() or sha(original) != sha(generated):
                raise RuntimeError(f"Numerical output differs or is missing: {original.name}")
            data_equal.append(original.name)

        png_equal = []
        pdf_checked = []
        pdf_byte_equal = []
        for original in sorted((R / "figures").glob("*")):
            generated = work / "figures" / original.name
            if not generated.exists():
                raise RuntimeError(f"Figure output missing: {original.name}")
            if original.suffix == ".png":
                if sha(original) != sha(generated):
                    raise RuntimeError(f"PNG figure differs: {original.name}")
                png_equal.append(original.name)
            elif original.suffix == ".pdf":
                if pdf_signature(original) != pdf_signature(generated):
                    raise RuntimeError(f"PDF figure content/geometry differs: {original.name}")
                pdf_checked.append(original.name)
                if sha(original) == sha(generated):
                    pdf_byte_equal.append(original.name)

        provenance = json.loads((R / "metadata/inherited_artifact_provenance_C19_A01.json").read_text())
        for row in provenance["files"]:
            path = row["path"]
            if path.startswith("repository_sources/") or path.startswith("inherited_C17/"):
                if sha(work / path) != row["sha256"]:
                    raise RuntimeError(f"Reproduction modified an inherited input: {path}")

    for script, log in logs.items():
        (R / "evidence" / f"reproduction_{script}.log").write_text(log)
    result = {
        "date": "2026-10-31",
        "status": "PASS",
        "disposable_copy": True,
        "commands": ["python code/" + x for x in COMMANDS],
        "data_files_byte_identical": len(data_equal),
        "png_figures_byte_identical": len(png_equal),
        "pdf_figures_content_and_geometry_checked": len(pdf_checked),
        "pdf_figures_also_byte_identical": len(pdf_byte_equal),
        "pdf_note": "PDF container hashes may vary with generation metadata; page geometry and extracted content were required to match.",
        "inherited_inputs_unchanged": True,
        "final_package_outputs_unchanged": True,
    }
    (R / "evidence/reproduction_C19_A01.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
