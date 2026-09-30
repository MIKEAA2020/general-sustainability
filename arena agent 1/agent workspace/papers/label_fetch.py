#!/usr/bin/env python3
"""Shared helper: copy a unit into scratch and fetch the figures it requests.

Extracted so several audits can share one figure-fetching routine instead of
each re-implementing it (and each getting the PNG stub wrong).
"""
import base64
import json
import os
import re
import urllib.parse
import urllib.request

PAPERS = "/home/user/papers"
SCRATCH = "/tmp/lab2"
TD = "/tmp/tectonic"
BR = "e2-v3-source-year"
BASE = "https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/%s/" % BR

# 1x1 transparent PNG, base64. Hand-typed hex literals have failed before.
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

SUPPS = [
    "paper01_obstruction_calculus_v63_supplementary.tex",
    "paper10_depletion_ledgers_v53_supplementary.tex",
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


_BY = None


def index():
    global _BY
    if _BY is None:
        _BY = build_index()
    return _BY


def fetch(rel, dest):
    b = os.path.basename(rel)
    for cand in (b, re.sub(r'_v\d+', '', b)):
        for p in index().get(cand, []):
            try:
                d = urllib.request.urlopen(BASE + urllib.parse.quote(p),
                                           timeout=60).read()
            except Exception:
                continue
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, 'wb').write(d)
            return True
    return False


def ensure_figures(fn):
    """Copy fn into scratch, fetch every figure it requests; return scratch dir."""
    src = os.path.join(PAPERS, fn)
    w = os.path.join(SCRATCH, fn[:-4])
    os.makedirs(w, exist_ok=True)
    txt = open(src, encoding="utf-8", errors="replace").read()
    open(os.path.join(w, fn), "w", encoding="utf-8").write(txt)
    live = strip_comments(txt)
    pat = r'\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}'
    for rel in sorted(set(re.findall(pat, live))):
        d = os.path.join(w, rel)
        if not os.path.exists(d) and not fetch(rel, d):
            os.makedirs(os.path.dirname(d), exist_ok=True)
            open(d, 'wb').write(PNG)
    return w
