#!/usr/bin/env python3
"""Build paper5 supplementary v6 from v5: audit-verification fixes.

Asserted substitutions only. Author-blocked items NOT touched: I8 (S2.3
model scope), A2 (four-state period), A6 (undischarged registration
items: inventory, IDs, routines, seeds), F38 (delta role), S4 15-25x.
"""
import os

SRC = "/home/user/paper5_supplementary_v5.md"
DST = "/home/user/paper5_v28/paper5_supplementary_v6.md"

SUBS = [
("count-eight",
"It carries seven bodies of material",
"It carries eight bodies of material"),

("S1-precision",
"complex pair at $T_r = 47.54$ yr and real $-1$ at 79.1 yr, both command-step artefacts; exact held-assessment crossing at 6.50 yr; protective Euler crossing at 2.31 yr, artefact",
"complex pair at $T_r = 47.536$ yr and real $-1$ at 79.143 yr, both command-step artefacts; exact held-assessment crossing at 6.501 yr; protective Euler crossing at 2.306 yr, artefact"),

("S1-nominal-tier",
"its multiplier and trajectory records are reproducible numerical propositions, and its comparison",
"its multiplier and trajectory records are nominal results with reproduction materials declared in S8 \u2014 plan, code, five output tables \u2014 and its comparison"),

("S8-carveout",
"Nothing reported in this article reaches beyond the nominal tier, and the statuses above say so.",
"Nothing reported in this article reaches beyond the nominal tier except the logistic crossing record, which S1 reports as re-execution-verified on the companion hold map."),

("S8-deposit-tier",
"are committed with the article's deposited material, and its records are reproducible numerical propositions.",
"will be committed with the article's deposited material, and its records are nominal results with those reproduction materials declared."),

("S4-BH-family",
"all of them SOI cells; Granger one-sided",
"all of them SOI cells. The ninety index\u2013lag cells are the BH family; the Granger and split-half tests are confirmatory and outside it. Granger one-sided"),
]

def main():
    s = open(SRC, encoding="utf-8").read()
    n0 = len(s)
    for name, old, new in SUBS:
        c = s.count(old)
        assert c == 1, f"{name}: count={c}"
        s = s.replace(old, new, 1)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w", encoding="utf-8").write(s)
    print(f"OK - all supp v6 substitutions applied ({n0} -> {len(s)} bytes, {len(SUBS)} subs)")

if __name__ == "__main__":
    main()
