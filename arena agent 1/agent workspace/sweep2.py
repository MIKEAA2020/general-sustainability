#!/usr/bin/env python3
"""Coverage sweep: perturb numbers that appear in ABSTRACTS and TABLE CELLS.

Numbers in figure widths, section references and code blocks are formatting,
not claims, and are excluded. A battery that passes a perturbed claim-number
does not pin that claim.
"""
import os, re, shutil, subprocess, sys, tempfile, json, time
sys.path.insert(0, "/home/user")
import texcheck

JOBS = [
  ("obstr v56", "fam/ob", "paper2_obstruction_calculus_v56_Automatica_routes.tex", "paper2_obstruction_calculus_v56_verification.py", 300),
  ("E3 v17",    "fam/ed", "paperE3_edwards_forecast_ladder_v17.tex", "paperE3_edwards_forecast_ladder_v17_verification.py", 300),
  ("E4 v16",    "fam/ed", "paperE4_edwards_intervention_v16.tex",   "paperE4_edwards_intervention_v16_verification.py", 300),
  ("minimax v12","fam/mm","minimax_dual_certificates_v12.tex",      "minimax_dual_certificates_v12_verify.py", 300),
  ("ARV v9",    "fam/arv","applied_regime_viability_v9.tex",        "applied_regime_viability_v9_verification.py", 300),
  ("E1 v59",    "fam/e1", "paperE1_cod_forecast_ladder_v59.tex",    "paperE1_cod_forecast_ladder_v59_verification.py", 300),
  ("ws v17",    "fam/ws", "paper2_worked_systems_v17.tex",          "paper2_worked_systems_v17_verification.py", 400),
  ("comp v20",  "vc",     "paper2_computational_certification_v20.tex","paper2_computational_certification_v20_verification.py", 800),
  ("psuff v14", "vp13",   "paper2_probabilistic_sufficiency_v14.tex","paper2_probabilistic_sufficiency_v14_verification.py", 800),
  ("ebc v13",   "ebc_verify","paper2_exact_belief_computation_v13.tex","paper2_exact_belief_computation_v13_verification.py", 800),
]

def claim_numbers(tex):
    """Decimal numbers occurring in the abstract or in a table cell."""
    zones = []
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    if m:
        zones.append(m.group(1))
    for lab in re.findall(r"\\label\{(tab:[^}]*)\}", tex):
        try:
            for row in texcheck.table_rows(tex, lab):
                zones.append(" ".join(row))
        except Exception:
            pass
    for mk in re.findall(r"\\textbf\{Table \d+\.\}", tex):
        try:
            for row in texcheck.longtable_rows(tex, mk):
                zones.append(" ".join(row))
        except Exception:
            pass
    blob = " ".join(zones)
    # drop cross-reference numbers: "Section 6.4", "Theorem 3.1", "Figure 2.5"...
    blob = re.sub(r"(Section|Theorem|Proposition|Remark|Corollary|Lemma|Figure|Table|"
                  r"Appendix|Equation|Eq\.)\s*~?\\ref\{[^}]*\}", " ", blob)
    blob = re.sub(r"(Section|Theorem|Proposition|Remark|Corollary|Lemma|Figure|Table|"
                  r"Appendix)\s+\d+\.\d+", " ", blob)
    out, seen = [], set()
    for m in re.finditer(r"(?<![\w.{}\\])(-?\d{1,4}\.\d{1,3})(?![\w.])", blob):
        s = m.group(1)
        if s in seen:
            continue
        seen.add(s)
        out.append(s)
    return out

def mutate(s):
    last = s[-1]
    nl = "7" if last != "7" else "3"
    return s[:-1] + nl

def run(name, d, texname, verifier, timeout, limit=8):
    texp = os.path.join(d, texname)
    if not (os.path.exists(texp) and os.path.exists(os.path.join(d, verifier))):
        return name, None, "missing files", []
    src = open(texp, encoding="utf-8").read()
    cands = [c for c in claim_numbers(src) if mutate(c) != c][:limit]
    if not cands:
        return name, None, "no claim-numbers found", []
    base = tempfile.mkdtemp(prefix="sw2_")
    caught, missed = 0, []
    for i, old in enumerate(cands):
        new = mutate(old)
        wd = os.path.join(base, f"m{i}")
        os.makedirs(wd, exist_ok=True)
        for f in os.listdir(d):
            if f == texname:
                continue
            s, t = os.path.join(d, f), os.path.join(wd, f)
            if os.path.isfile(s):
                shutil.copy2(s, t)
            elif os.path.isdir(s):
                shutil.copytree(s, t, dirs_exist_ok=True)
        shutil.copy2(os.path.join(d, verifier), os.path.join(wd, verifier))
        open(os.path.join(wd, texname), "w", encoding="utf-8").write(src.replace(old, new, 1))
        try:
            r = subprocess.run([sys.executable, verifier], cwd=wd,
                               capture_output=True, text=True, timeout=timeout)
            ok = r.returncode != 0
        except subprocess.TimeoutExpired:
            ok = None
        if ok:
            caught += 1
        else:
            missed.append(f"{old}->{new}" + ("(timeout)" if ok is None else ""))
    shutil.rmtree(base, ignore_errors=True)
    return name, (caught, len(cands)), "", missed

only = sys.argv[1:] if len(sys.argv) > 1 else None
print(f"{'paper':12} {'pinned':>8}   reading")
print("-" * 78)
res = []
for name, d, texname, verifier, to in JOBS:
    if only and name.split()[0] not in only:
        continue
    t0 = time.time()
    n, r, err, missed = run(name, d, texname, verifier, to)
    if r is None:
        print(f"{n:12} {'--':>8}   {err}")
        res.append((n, None, missed)); continue
    c, t = r
    v = "all pinned" if c == t else ("partial" if c else "NONE PINNED")
    print(f"{n:12} {c:>4}/{t:<3}   {v:12} unpinned: {', '.join(missed[:4])}  ({time.time()-t0:.0f}s)")
    res.append((n, f"{c}/{t}", missed))
json.dump(res, open("/home/user/sweep2_results.json", "w"), indent=1)
