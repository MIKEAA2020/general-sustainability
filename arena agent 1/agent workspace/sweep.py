#!/usr/bin/env python3
"""Mutation-sweep every battery in the family: can each one actually fail?"""
import os, re, shutil, subprocess, sys, tempfile, json, time

JOBS = [
  ("obstr v56", "fam/ob", "paper2_obstruction_calculus_v56_Automatica_routes.tex", "paper2_obstruction_calculus_v56_verification.py", 300),
  ("E3 v17",    "fam/ed", "paperE3_edwards_forecast_ladder_v17.tex", "paperE3_edwards_forecast_ladder_v17_verification.py", 300),
  ("E4 v16",    "fam/ed", "paperE4_edwards_intervention_v16.tex",   "paperE4_edwards_intervention_v16_verification.py", 300),
  ("minimax v12","fam/mm","minimax_dual_certificates_v12.tex",      "minimax_dual_certificates_v12_verify.py", 300),
  ("ws v17",    "fam/ws", "paper2_worked_systems_v17.tex",          "paper2_worked_systems_v17_verification.py", 400),
  ("ARV v9",    "fam/arv","applied_regime_viability_v9.tex",        "applied_regime_viability_v9_verification.py", 300),
  ("E1 v59",    "fam/e1", "paperE1_cod_forecast_ladder_v59.tex",    "paperE1_cod_forecast_ladder_v59_verification.py", 300),
  ("comp v20",  "vc",     "paper2_computational_certification_v20.tex","paper2_computational_certification_v20_verification.py", 900),
  ("psuff v14", "vp13",   "paper2_probabilistic_sufficiency_v14.tex","paper2_probabilistic_sufficiency_v14_verification.py", 900),
  ("ebc v13",   "ebc_verify","paper2_exact_belief_computation_v13.tex","paper2_exact_belief_computation_v13_verification.py", 900),
]

def mutations_for(tex):
    """Pull distinctive printed numbers out of the manuscript and perturb them."""
    cands = []
    seen = set()
    for m in re.finditer(r"(?<![\w.])(\d{1,3}\.\d{2})(?![\w.])", tex):
        s = m.group(1)
        if s in seen or len(cands) >= 6:
            continue
        seen.add(s)
        # flip the last digit
        last = s[-1]
        new_last = "7" if last != "7" else "3"
        cands.append((s, s[:-1] + new_last))
    return cands

def run(name, d, texname, verifier, timeout):
    texp = os.path.join(d, texname)
    if not (os.path.exists(texp) and os.path.exists(os.path.join(d, verifier))):
        return name, None, "missing files"
    src = open(texp, encoding="utf-8").read()
    cands = mutations_for(src)
    if not cands:
        return name, None, "no numeric candidates"
    base = tempfile.mkdtemp(prefix="sweep_")
    caught = 0
    missed = []
    for i, (old, new) in enumerate(cands):
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
    return name, (caught, len(cands)), missed

print(f"{'paper':12} {'caught':>8}   verdict")
print("-" * 62)
results = []
for name, d, texname, verifier, to in JOBS:
    if len(sys.argv) > 1 and name.split()[0] not in sys.argv:
        continue
    t0 = time.time()
    n, res, missed = run(name, d, texname, verifier, to)
    if res is None:
        print(f"{n:12} {'--':>8}   {missed}")
        results.append((n, None, missed)); continue
    c, t = res
    verdict = "FALSIFIABLE" if c == t else ("PARTIAL" if c else "CANNOT FAIL")
    print(f"{n:12} {c:>4}/{t:<3}   {verdict:12} missed: {', '.join(missed[:3])}"
          f"  ({time.time()-t0:.0f}s)")
    results.append((n, f"{c}/{t}", missed))
json.dump(results, open("/home/user/sweep_results.json", "w"), indent=1)
