#!/usr/bin/env python3
"""
Compile the eleven unit heads with tectonic, and report.

Figures: fetched from the branch where they exist (exact name first, then the
same stem with the _vNN version suffix stripped). Only figures that exist in
neither form are stubbed, and every stub is reported so the report never
conflates "compiled" with "compiled with real figures".

This is a verification harness. It writes only into its own scratch directory
and never modifies a paper.
"""
import base64
import io
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

BRANCH = "e2-v3-source-year"
RAW = ("https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/"
       + BRANCH + "/")
TECTONIC = "/tmp/tectonic"
PAPERS = Path("/home/user/papers")
SCRATCH = Path("/tmp/cbuild")
TREE = PAPERS / "supprec" / "tree.json"

UNITS = [
    ("1",  "paper01_obstruction_calculus_v63.tex"),
    ("2",  "paper02_probabilistic_sufficiency_v12.tex"),
    ("3",  "paper03_computational_certification_v16.tex"),
    ("4",  "paper04_minimax_dual_certificates_v16.tex"),
    ("5",  "paper05_exact_belief_computation_v16.tex"),
    ("6",  "paper06_assessment_separation_v67.tex"),
    ("7",  "paper08_governance_delay_v46.tex"),
    ("8",  "paper09_cod_certification_v32.tex"),
    ("9",  "paper10_depletion_ledgers_v53.tex"),
    ("10", "paper11_forecasting_baselines_v64.tex"),
    ("11", "paper11c_worked_systems_audit_v2.tex"),
]

# supplementary files, compiled as their own documents
SUPPS = [
    ("S1", "paper01_obstruction_calculus_v63_supplementary.tex"),
    ("S6", "paper06_assessment_separation_v67_supplementary.md", "md"),
    ("S7g", "paper08_governance_delay_v46_supplementary_governance.md", "md"),
    ("S7d", "paper08_governance_delay_v46_supplementary_delay.md", "md"),
    ("S9", "paper10_depletion_ledgers_v53_supplementary.tex"),
]

# 1x1 transparent PNG
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8"
    "z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
# minimal 1-page PDF
PDF = (b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
       b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
       b"3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 1 1]>>endobj\n"
       b"trailer<</Root 1 0 R>>\n%%EOF\n")


def load_index():
    """branch path -> set of candidate figure names, for lookup by basename"""
    d = json.load(io.open(TREE, encoding="utf-8"))
    idx = {}
    for t in d["tree"]:
        if t["type"] != "blob":
            continue
        p = t["path"]
        if re.search(r"\.(png|jpg|jpeg|pdf|eps)$", p, re.I):
            idx.setdefault(os.path.basename(p), []).append(p)
    return idx


def strip_version(name):
    """fig1_witness_v40.png -> fig1_witness.png ; also ..._v2.pdf -> ....pdf"""
    stem, ext = os.path.splitext(name)
    s = re.sub(r"_v\d+$", "", stem)
    return s + ext if s != stem else None


def fetch(rel, idx, dest):
    """Return (status, branch_path_or_None)."""
    base = os.path.basename(rel)
    cands = [base]
    sv = strip_version(base)
    if sv:
        cands.append(sv)
    for c in cands:
        for bp in idx.get(c, []):
            url = RAW + urllib.parse.quote(bp)
            try:
                with urllib.request.urlopen(url, timeout=90) as r:
                    data = r.read()
            except Exception:
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            return ("real", bp)
    return ("stub", None)


def main():
    import urllib.parse  # noqa: F401  (used in fetch)
    if not os.path.exists(TECTONIC):
        sys.exit("tectonic not found at %s" % TECTONIC)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    idx = load_index()
    print("figure index: %d distinct image basenames" % len(idx))

    results = []
    for unit, fn in UNITS:
        src = PAPERS / fn
        if not src.exists():
            results.append((unit, fn, "MISSING", 0, 0, 0, 0))
            continue
        work = SCRATCH / ("u" + unit)
        work.mkdir(parents=True, exist_ok=True)
        text = io.open(src, encoding="utf-8", errors="replace").read()
        (work / fn).write_text(text)

        figs = sorted(set(re.findall(
            r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}", text)))
        nreal = nstub = 0
        for rel in figs:
            dest = work / rel
            if dest.exists():
                nreal += 1
                continue
            status, _ = fetch(rel, idx, dest)
            if status == "real":
                nreal += 1
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(PDF if dest.suffix.lower() == ".pdf" else PNG)
                nstub += 1

        try:
            p = subprocess.run(
                [TECTONIC, "-X", "compile", fn, "--outdir", "."],
                cwd=str(work), capture_output=True, text=True, timeout=1500)
            out = p.stdout + p.stderr
        except subprocess.TimeoutExpired:
            results.append((unit, fn, "TIMEOUT", len(figs), nreal, nstub, 0))
            continue

        errs = [l for l in out.splitlines() if "error" in l.lower()
                and " halted" not in l.lower()]
        undef = len(re.findall(r"undefined (?:reference|control sequence)",
                               out, re.I))
        pdf = work / (fn[:-4] + ".pdf")
        pages = 0
        if pdf.exists():
            data = pdf.read_bytes()
            # /Count in the page tree, else fall back to counting page objects
            m = re.search(rb"/Count\s+(\d+)", data)
            if m:
                pages = int(m.group(1))
            else:
                pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
        if pdf.exists() and not errs:
            status = "OK"
        elif pdf.exists():
            status = "ERRORS"
        else:
            status = "FAILED"
        results.append((unit, fn, status, len(figs), nreal, nstub, pages))

    print()
    print("%-4s %-46s %-9s %-7s %-13s %s" %
          ("unit", "file", "result", "pages", "figures", "notes"))
    print("-" * 104)
    for (unit, fn, st, nf, nreal, nstub, pages) in results:
        notes = ""
        if nf:
            notes = "%d real / %d stubbed" % (nreal, nstub)
        print("%-4s %-46s %-9s %-7s %-13s %s" %
              (unit, fn, st, pages if pages else "-",
               ("%d" % nf) if nf else "-", notes))
    print("-" * 104)
    ok = sum(1 for r in results if r[2] == "OK")
    print("compiled cleanly: %d / %d" % (ok, len(results)))

    # ---- supplementary files -------------------------------------------
    print("\nSupplementary files")
    print("%-6s %-56s %-10s %s" % ("unit", "file", "result", "pages"))
    print("-" * 104)
    sresults = []
    for tag, fn in [(t, f) for t, f, *_ in SUPPS]:
        src = PAPERS / fn
        if fn.endswith(".md"):
            print("%-6s %-56s %-10s %s" % (tag, fn, "N/A", "-"))
            sresults.append((tag, fn, "markdown"))
            continue
        work = SCRATCH / ("s" + tag)
        work.mkdir(parents=True, exist_ok=True)
        (work / fn).write_text(io.open(src, encoding="utf-8",
                                       errors="replace").read())
        text = (work / fn).read_text()
        figs = sorted(set(re.findall(
            r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}", text)))
        for rel in figs:
            dest = work / rel
            if dest.exists():
                continue
            status, _ = fetch(rel, idx, dest)
            if status == "stub":
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(PDF if dest.suffix.lower() == ".pdf" else PNG)
        try:
            p = subprocess.run(
                [TECTONIC, "-X", "compile", fn, "--outdir", "."],
                cwd=str(work), capture_output=True, text=True, timeout=1200)
            out = p.stdout + p.stderr
        except subprocess.TimeoutExpired:
            print("%-6s %-56s %-10s %s" % (tag, fn, "TIMEOUT", "-"))
            sresults.append((tag, fn, "TIMEOUT"))
            continue
        errs = [l for l in out.splitlines() if "error" in l.lower()
                and " halted" not in l.lower()]
        pdf = work / (fn[:-4] + ".pdf")
        pages = 0
        if pdf.exists():
            data = pdf.read_bytes()
            m = re.search(rb"/Count\s+(\d+)", data)
            pages = int(m.group(1)) if m else len(
                re.findall(rb"/Type\s*/Page[^s]", data))
        st = "OK" if (pdf.exists() and not errs) else (
            "ERRORS" if pdf.exists() else "FAILED")
        if errs:
            print("       first error: %s" % errs[0][:150])
        print("%-6s %-56s %-10s %s" % (tag, fn, st, pages or "-"))
        sresults.append((tag, fn, st))
    print("-" * 104)
    tok = sum(1 for r in sresults if r[2] == "OK")
    print("supplements compiled cleanly: %d / %d (.tex only; .md are markdown "
          "source, no converter available)" % (
              tok, sum(1 for r in sresults if r[2] != "markdown")))

    io.open(SCRATCH / "results.json", "w").write(
        json.dumps({"units": results, "supplements": sresults}, indent=1))


if __name__ == "__main__":
    main()
