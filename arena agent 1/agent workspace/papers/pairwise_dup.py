#!/usr/bin/env python3
"""Find duplicated passages across EVERY pair of the eleven units.

The framework check compared paper 1 against papers 2-5 only. That leaves
papers 6-11, and the merged concatenations (units 8, 10, 11), entirely untested
for cross-paper duplication -- which is where concatenation damage is most
likely, since those files were assembled from several sources.

Reports shared contiguous passages of >=MIN_WORDS words with the full text, so
each can be judged by reading rather than by a similarity score. Short shared
strings (formula fragments, boilerplate) are suppressed by requiring a run of
consecutive shared n-grams long enough to be a real passage.
"""
import os
import re
import sys
import unicodedata
from itertools import combinations

from label_fetch import PAPERS, strip_comments

UNITS = [
    ("u1  paper01", "paper01_obstruction_calculus_v63.tex"),
    ("u2  paper02", "paper02_probabilistic_sufficiency_v12.tex"),
    ("u3  paper03", "paper03_computational_certification_v16.tex"),
    ("u4  paper04", "paper04_minimax_dual_certificates_v16.tex"),
    ("u5  paper05", "paper05_exact_belief_computation_v16.tex"),
    ("u6  paper06", "paper06_assessment_separation_v67.tex"),
    ("u7  paper08", "paper08_governance_delay_v46.tex"),
    ("u8  paper09", "paper09_cod_certification_v32.tex"),
    ("u9  paper10", "paper10_depletion_ledgers_v53.tex"),
    ("u10 paper11", "paper11_forecasting_baselines_v64.tex"),
    ("u11 paper11c", "paper11c_worked_systems_audit_v2.tex"),
]

N = 10
MIN_WORDS = 45  # a shared passage, not a boilerplate phrase


def words(t):
    t = strip_comments(t)
    t = re.sub(r'\\[a-zA-Z]+', ' ', t)
    t = re.sub(r'[{}\\\$&_^~]', ' ', t)
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'[^a-zA-Z0-9 ]', ' ', t.lower())
    return re.sub(r'\s+', ' ', t).strip().split()


def runs(a_pos, b_pos, gap=8):
    """Shared n-gram positions -> contiguous shared passages."""
    pairs = sorted(zip(a_pos, b_pos))
    out = []
    for a, b in pairs:
        if out and a - out[-1][1] <= gap and b - out[-1][3] <= gap:
            out[-1][1] = a
            out[-1][3] = b
        else:
            out.append([a, a, b, b])
    return [(a0, a1 + N, b0, b1 + N) for a0, a1, b0, b1 in out]


def main():
    texts = {}
    for tag, fn in UNITS:
        p = os.path.join(PAPERS, fn)
        if os.path.exists(p):
            texts[tag] = words(open(p, encoding="utf-8",
                                    errors="replace").read())
    grams = {}
    for tag, w in texts.items():
        grams[tag] = {" ".join(w[i:i + N]): i
                      for i in range(len(w) - N + 1)}

    found = 0
    for (ta, fa), (tb, fb) in combinations(UNITS, 2):
        if ta not in texts or tb not in texts:
            continue
        shared = set(grams[ta]) & set(grams[tb])
        if not shared:
            continue
        ap = [grams[ta][s] for s in shared]
        bp = [grams[tb][s] for s in shared]
        wa, wb = texts[ta], texts[tb]
        big = [r for r in runs(ap, bp) if r[1] - r[0] >= MIN_WORDS]
        if not big:
            continue
        print("#" * 100)
        print("%s  <->  %s : %d shared passage(s) of >=%d words"
              % (ta, tb, len(big), MIN_WORDS))
        for a0, a1, b0, b1 in sorted(big, key=lambda r: -(r[1] - r[0]))[:4]:
            found += 1
            print("\n   %d words shared" % (a1 - a0))
            print("   [%s @ word %d] %s"
                  % (ta, a0, " ".join(wa[a0:a0 + 40])[:230]))
            print("   [%s @ word %d] %s"
                  % (tb, b0, " ".join(wb[b0:b0 + 40])[:230]))
    print("\n" + "=" * 100)
    print("shared passages found: %d" % found)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
