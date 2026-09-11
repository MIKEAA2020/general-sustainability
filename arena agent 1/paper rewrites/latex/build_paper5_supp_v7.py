#!/usr/bin/env python3
"""Build paper5 supplementary v7 from v6: root-cause resolution items.

Asserted substitutions only. Still author-blocked (NOT touched): A6
(undischarged registration items), A3 disclosure policy, A5 archive role.
Applied: I8 (S2.3 provenance), A2/F4 (S4 period mirror), I7 (S8
re-execution set), companion-status currency (delay study published).
"""
import os
import sys

SRC = "/home/user/paper5_v28/paper5_supplementary_v6.md"
DST = "/home/user/paper5_v29/paper5_supplementary_v7.md"

SUBS = [
("S2.3-provenance",
"**S2.3 The dimensionless identifiability chart (theorem, proof in full).** In the three-state gated core, let",
"**S2.3 The dimensionless identifiability chart (theorem, proof in full).** This chart is the companion delay study\u2019s identifiability record (Abaee, 2026, \u00a79.5), whose objects are that study\u2019s three-state gated core; it is proved here because the companion defers the sampled-governance identification statements to this supplement. In the three-state gated core, let"),

("S4-F4-mirror",
"cohort resonance supplies an alternative mechanism, its period 15\u201325 times shorter than the four-state prediction.",
"cohort resonance supplies an alternative mechanism, its period 15\u201325 times shorter than the four-state prediction (slow-stock cohort cycle $P \\approx 250$\u2013360 yr in the archived record)."),

("S8-reexec-set",
"Nothing reported in this article reaches beyond the nominal tier except the logistic crossing record, which S1 reports as re-execution-verified on the companion hold map.",
"Nothing reported in this article reaches beyond the nominal tier except the logistic crossing record, which S1 reports as re-execution-verified on the companion hold map (independent crossing-scan and exact-hold monodromy implementations, each with validation gates)."),

("S8-companion-status",
"proceeds under the same discipline and is reported separately (companion studies under separate review); no result of this article depends",
"proceeds under the same discipline and is reported separately (the delay study published as Abaee, 2026; the other companions proceeding separately); no result of this article depends"),
]

def main():
    s = open(SRC, encoding="utf-8").read()
    for name, old, new in SUBS:
        n = s.count(old)
        if n != 1:
            print(f"FAIL {name}: count={n}")
            sys.exit(1)
        s = s.replace(old, new)
        print(f"ok {name}")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w", encoding="utf-8").write(s)
    print("wrote", DST, len(s), "bytes")

if __name__ == "__main__":
    main()
