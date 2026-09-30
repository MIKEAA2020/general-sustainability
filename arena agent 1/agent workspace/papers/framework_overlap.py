#!/usr/bin/env python3
"""Measure how much of papers 2-5's framework setup is verbatim duplication of
paper 1.

Only VERBATIM reuse is counted, because only that is "clear duplication" in the
sense the author asked for: de-duplicate the least, retain when in doubt.
Paraphrase, re-derivation with different notation, and genuinely different
content are all left alone.

Method: shared word 12-grams between paper 1 and each of papers 2-5, reported as
contiguous runs so the actual duplicated passages can be inspected rather than
inferred from a percentage.
"""
import os
import re
import sys

from label_fetch import PAPERS

FILES = {
    1: "paper01_obstruction_calculus_v63.tex",
    2: "paper02_probabilistic_sufficiency_v12.tex",
    3: "paper03_computational_certification_v16.tex",
    4: "paper04_minimax_dual_certificates_v16.tex",
    5: "paper05_exact_belief_computation_v16.tex",
}

N = 12


def words(t):
    t = re.sub(r'(?<!\\)%.*', '', t)
    t = re.sub(r'\\[a-zA-Z]+', ' ', t)
    t = re.sub(r'[{}\\\$&_^~]', ' ', t)
    t = re.sub(r'[^a-zA-Z0-9 ]', ' ', t)
    return re.sub(r'\s+', ' ', t).lower().split()


def ngrams(w, n=N):
    return {" ".join(w[i:i + n]): i for i in range(len(w) - n + 1)}


def runs(matches, gap=6):
    """Collapse matched positions into contiguous runs."""
    if not matches:
        return []
    ms = sorted(matches)
    out = [[ms[0], ms[0]]]
    for m in ms[1:]:
        if m - out[-1][1] <= gap:
            out[-1][1] = m
        else:
            out.append([m, m])
    return out


def main():
    texts = {}
    for k, fn in FILES.items():
        p = os.path.join(PAPERS, fn)
        texts[k] = open(p, encoding="utf-8", errors="replace").read()

    w1 = words(texts[1])
    g1 = ngrams(w1)
    print("paper 1: %d words, %d %d-grams" % (len(w1), len(g1), N))
    print()

    only_short = "--all" not in sys.argv
    for k in (2, 3, 4, 5):
        wk = words(texts[k])
        gk = ngrams(wk)
        shared = set(g1) & set(gk)
        pct = 100.0 * len(shared) / max(1, len(gk))
        print("=" * 96)
        print("paper %d: %d words | shared %d-grams with paper 1: %d (%.2f%% of paper %d)"
              % (k, len(wk), N, len(shared), pct, k))
        pos = sorted(gk[s] for s in shared)
        rs = runs(pos)
        # a run's length in words = (end - start) + N
        big = [(a, b, (b - a) + N) for a, b in rs if (b - a) + N >= 40]
        big.sort(key=lambda x: -x[2])
        print("contiguous duplicated runs: %d total, %d of >=40 words"
              % (len(rs), len(big)))
        for a, b, L in big[:8]:
            snippet = " ".join(wk[a:a + 45])
            print("\n   [%4d words] at word %d" % (L, a))
            print("      ...%s..." % snippet[:210])


if __name__ == "__main__":
    main()
