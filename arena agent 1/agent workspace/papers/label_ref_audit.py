#!/usr/bin/env python3
"""Audit: find LIVE \\ref/\\eqref whose target label exists but resolves to EMPTY
text, so the reference renders as a blank instead of a number.

This defect class is invisible to an "undefined reference" check: the label DOES
exist, so LaTeX is satisfied, but because the enclosing heading is unnumbered
(usually \\section*), \\@currentlabel was never set and the reference prints
nothing. Typically renders as "Section ." or "Section  with a gap".

Comments are stripped before scanning for refs, so mentions inside %% notes are
not counted as live references.
"""
import base64
import json
import os
import re
import shutil
import subprocess
import urllib.parse
import urllib.request

TD = "/tmp/tectonic"
BR = "e2-v3-source-year"
BASE = "https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/%s/" % BR
PAPERS = "/home/user/papers"
SCRATCH = "/tmp/lab2"

# 1x1 transparent PNG, base64 (hand-typed hex literals are not trustworthy)
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAh"
    "KmMIQAAAABJRU5ErkJggg==")

UNITS = [
    "paper01_obstruction_calculus_v63.tex",
    "paper02_probabilistic_sufficiency_v12.tex",
    "paper03_computational_certification_v16.tex",
    "paper04_minimax_dual_certificates_v16.tex",
    "paper05_exact_belief_computation_v16.tex",
    "paper06_assessment_separation_v67.tex",
    "paper08_governance_delay_v46.tex",
    "paper09_cod_certification_v32.tex",
    "paper10_depletion_ledgers_v53.tex",
    "paper11_forecasting_baselines_v64.tex",
    "paper11c_worked_systems_audit_v2.tex",
]


def strip_comments(t):
    return "\n".join(re.sub(r'(?<!\\)%.*', '', l) for l in t.splitlines())


def build_index():
    try:
        idx = json.load(open(os.path.join(PAPERS, "supprec", "tree.json")))
    except Exception:
        return {}
    by = {}
    for e in idx.get("tree", []):
        by.setdefault(os.path.basename(e["path"]), []).append(e["path"])
    return by


def fetch(by, rel, dest):
    b = os.path.basename(rel)
    for cand in (b, re.sub(r'_v\d+', '', b)):
        for p in by.get(cand, []):
            try:
                d = urllib.request.urlopen(BASE + urllib.parse.quote(p),
                                           timeout=60).read()
            except Exception:
                continue
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, 'wb').write(d)
            return True
    return False


def main():
    by = build_index()
    print("figure index: %d distinct image basenames" % len(by))
    print("%-44s %8s %7s  %s" % ("file", "liveRef", "empty",
                                 "LIVE refs resolving empty"))
    print("-" * 104)
    total = 0
    for fn in UNITS:
        src = os.path.join(PAPERS, fn)
        if not os.path.exists(src):
            print("%-44s  MISSING" % fn[:44])
            continue
        w = os.path.join(SCRATCH, fn[:-4])
        os.makedirs(w, exist_ok=True)
        txt = open(src, encoding="utf-8", errors="replace").read()
        open(os.path.join(w, fn), "w", encoding="utf-8").write(txt)
        live = strip_comments(txt)

        pat = r'\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}'
        for rel in sorted(set(re.findall(pat, live))):
            d = os.path.join(w, rel)
            if not os.path.exists(d) and not fetch(by, rel, d):
                os.makedirs(os.path.dirname(d), exist_ok=True)
                open(d, 'wb').write(PNG)

        subprocess.run([TD, "-X", "compile", fn, "--outdir", ".",
                        "--keep-intermediates"],
                       cwd=w, capture_output=True, timeout=900)
        auxf = os.path.join(w, fn[:-4] + ".aux")
        if not os.path.exists(auxf):
            print("%-44s  NO AUX (compile failed)" % fn[:44])
            continue
        aux = open(auxf, encoding="latin-1").read()
        labs = re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}', aux)
        empty = {n for n, t in labs if t.strip() == ""}
        refd = set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', live))
        bad = sorted(empty & refd)
        total += len(bad)
        print("%-44s %8d %7d  %s" % (fn[:44], len(refd), len(empty),
                                     ", ".join(bad) if bad else "—"))
    print("-" * 104)
    print("LIVE cross-references resolving to EMPTY label text: %d" % total)


if __name__ == "__main__":
    main()
