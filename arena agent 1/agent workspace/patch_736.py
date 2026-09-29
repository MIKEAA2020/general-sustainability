#!/usr/bin/env python3
"""v44: the EBC glance table's "736 stored antichain" is wrong.

The stored antichain is 496 = 16 + 15*32 (the verifier computes exactly
this and calls it "stored maximal sets"; the census proposition and the
abstract both say 496).

736 = 16 + 15*(16+32) counts ALL survivable sets above the edge --
including the non-maximal singletons, which are precisely what the
antichain discipline exists to discard. So 736 is a meaningful number
but is not the stored antichain, and the glance table's "Raw vs stored"
row mislabels it.

Worse, the verifier's own needle (line 224) hard-codes the 736 string,
so the check ENFORCES the error instead of catching it. Both the paper
and the needle must move together or the 30/30 run breaks.

Raw strings throughout -- no LaTeX backslash is ever eaten by Python.
"""
import io, os

BS = chr(92)

# ---------------------------------------------------------------- paper
P_SRC = "/home/user/paper2_exact_belief_computation_v11.tex"
P_DST = "/home/user/paper2_exact_belief_computation_v12.tex"

P_OLD = r"Raw vs stored & $2^{16} = 65{,}536$ raw subsets, $736$ stored antichain \\"
P_NEW = (r"Raw vs stored & $2^{16} = 65{,}536$ raw subsets per level, "
         r"$496$ stored maximal sets \\")

# ------------------------------------------------------------- verifier
V = "/home/user/ebc_verify/paper2_exact_belief_computation_v10_verification.py"

V_OLD_NEEDLE = (r'                "$2^{16} = 65{,}536$ raw subsets, $736$ stored antichain",')
V_NEW_NEEDLE = (r'                "$2^{16} = 65{,}536$ raw subsets per level, "'
                "\n"
                r'                "$496$ stored maximal sets",')

V_OLD_DOC = r"17^4 = 83,521 sequences); the antichain census (1,048,576 raw -> 736 stored);"
V_NEW_DOC = r"17^4 = 83,521 sequences); the antichain census (1,048,576 raw -> 496 stored);"

JOBS = [
    ("paper  glance table", P_SRC, P_DST, [(P_OLD, P_NEW)]),
    ("verifier needle",     V,     V,     [(V_OLD_NEEDLE, V_NEW_NEEDLE),
                                           (V_OLD_DOC, V_NEW_DOC)]),
]

def main():
    for label, src, dst, patches in JOBS:
        if not os.path.exists(src):
            print(f"[{label}] MISSING {src}")
            continue
        s = io.open(src, encoding="utf-8", newline="").read()
        for old, new in patches:
            if old in s:
                s = s.replace(old, new, 1)
                print(f"[{label}] ok   {old[:52]!r}")
            else:
                print(f"[{label}] MISS {old[:52]!r}")
        io.open(dst, "w", encoding="utf-8", newline="").write(s)
        import re
        if dst.endswith(".tex"):
            labels = set(re.findall(r"\\label\{([^}]*)\}", s))
            refs = set(re.findall(r"\\ref\{([^}]*)\}", s))
            print(f"           braces={s.count('{')-s.count('}')} "
                  f"bad-refs={sorted(refs-labels) or 'none'}")
    # cross-check: the needle must now appear in the paper
    paper = io.open(P_DST, encoding="utf-8", newline="").read()
    norm = " ".join(paper.split())
    needle = "$2^{16} = 65{,}536$ raw subsets per level, $496$ stored maximal sets"
    print("needle present in paper:", needle in norm)
    print("stale 736 still in paper:", "736" in norm)

if __name__ == "__main__":
    main()
