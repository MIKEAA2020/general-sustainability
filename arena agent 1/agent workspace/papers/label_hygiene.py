#!/usr/bin/env python3
"""Static label/float hygiene audit for the eleven unit heads.

Checks that need no LaTeX run:

  1. Duplicate \\label names. Two definitions of the same label silently make the
     first unreachable; every \\ref to it points at the second definition. LaTeX
     warns, but the warning is easy to miss in a long log and does not fail the
     build.
  2. Orphaned floats: \\label inside figure/table that no \\ref or \\eqref points
     at. Not necessarily a defect (some figures are never cited), but a large
     count is worth knowing about.
  3. \\ref targets that have no \\label anywhere in the same file. These are the
     genuinely broken ones -- they render as ?? and DO produce a warning.

Comments are stripped before scanning, so %% notes are not counted.
"""
import os
import re
from collections import Counter, defaultdict

PAPERS = "/home/user/papers"

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

FLOAT_ENVS = ("figure", "figure*", "table", "table*", "algorithm")


def strip_comments(t):
    return "\n".join(re.sub(r'(?<!\\)%.*', '', l) for l in t.splitlines())


def float_at(lines, i):
    """If line i sits inside a float environment, return its kind, else None."""
    depth = defaultdict(int)
    for j in range(i):
        for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', lines[j]):
            kind = m.group(2)
            if kind in FLOAT_ENVS:
                depth[kind] += 1 if m.group(1) == "begin" else -1
    for k, v in depth.items():
        if v > 0:
            return k
    return None


def audit(fn):
    txt = open(os.path.join(PAPERS, fn), encoding="utf-8",
               errors="replace").read()
    live = strip_comments(txt)
    lines = live.splitlines()

    labels = []
    for i, l in enumerate(lines):
        for m in re.finditer(r'\\label\{([^}]+)\}', l):
            labels.append((m.group(1), i + 1, float_at(lines, i)))

    names = [n for n, _, _ in labels]
    dupes = {n: c for n, c in Counter(names).items() if c > 1}

    refs = set(re.findall(r'\\(?:ref|eqref|nameref|autoref)\{([^}]+)\}', live))
    defined = set(names)

    missing = sorted(refs - defined)          # renders ?? and warns
    orphans = sorted(n for n, _, k in labels
                     if k in FLOAT_ENVS and n not in refs)

    return labels, dupes, missing, orphans


def main():
    print("%-44s %6s %7s %8s %8s" %
          ("file", "labels", "dupes", "missing", "orphan"))
    print("-" * 82)
    tot_d = tot_m = tot_o = 0
    for group, files in (("units", UNITS), ("supps", SUPPS)):
        if group == "supps":
            print("-" * 82)
        for fn in files:
            p = os.path.join(PAPERS, fn)
            if not os.path.exists(p):
                print("%-44s  MISSING" % fn[:44])
                continue
            labels, dupes, missing, orphans = audit(fn)
            tot_d += len(dupes)
            tot_m += len(missing)
            tot_o += len(orphans)
            flag = ""
            if dupes:
                flag += "  DUP: " + ", ".join(sorted(dupes)[:4])
            if missing:
                flag += "  MISS: " + ", ".join(missing[:4])
            print("%-44s %6d %7d %8d %8d%s" %
                  (fn[:44], len(labels), len(dupes), len(missing),
                   len(orphans), flag))
        if group == "units":
            pass
    print("-" * 82)
    print("duplicate labels: %d   missing (renders ??): %d   orphaned floats: %d"
          % (tot_d, tot_m, tot_o))

    # detail
    print("\n=== detail ===")
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        labels, dupes, missing, orphans = audit(fn)
        if not (dupes or missing):
            continue
        print("\n%s" % fn)
        if dupes:
            for n in sorted(dupes):
                where = [(i, k) for nm, i, k in labels if nm == n]
                print("   DUPLICATE %-46s x%d  at %s"
                      % (n, dupes[n],
                         ", ".join("L%d%s" % (i, "(%s)" % k if k else "")
                                   for i, k in where)))
        if missing:
            for n in missing:
                print("   MISSING   %-46s no \\label in file" % n)


if __name__ == "__main__":
    main()
