#!/usr/bin/env python3
"""lean_README_v16.md -> lean_README_v17.md

v41: verified the merge state of repair A (it is merged, not merely
drafted); corrected the P3 paper version pointer v11 -> v12; relabelled
P3_Binomial from "INCOMPLETE" to complete machinery; fixed the stale
prop:ladder heading. Targeted substitutions; each prints ok/MISS.
"""
import io, os

SRC = "/home/user/lean_README_v16.md"
DST = "/home/user/lean_README_v17.md"

OLD_DRAFT = """**Repair A** is adopted: `𝒲_k` in `thm:support`
becomes the feedback recursion `𝒲^{fb}_k`, and the repaired statement is
what the layer proves. A remark covers the blind window, where the two
recursions agree (`Wmem_eq_Wblind_of_blind`). The paper edit — including
the notation fix for `𝒲^{bel}_k` — is drafted in
`paper2_repairA_thm_support_v1.tex`."""

NEW_DRAFT = """**Repair A** is adopted: `𝒲_k` in `thm:support`
becomes the feedback recursion `𝒲^{fb}_k`, and the repaired statement is
what the layer proves. A remark covers the blind window, where the two
recursions agree (`Wmem_eq_Wblind_of_blind`).

**The repair is merged into the paper, not merely drafted.** Verified
against `paper2_probabilistic_sufficiency_v12.tex` (v41):

* the notation paragraph defines all three symbols — `𝒲^{fb}_k`
  (feedback), `𝒲_k` (blind, "one action for the whole set, chosen before
  the observation arrives"), `𝒲^{bel}_k`;
* `thm:support` states `V_k(b) = 1` iff `supp(b) ∈ 𝒲^{fb}_k` for the
  unrestricted sequential class — repair A verbatim;
* the line-256 cross-reference reads `𝒲^{bel}_k` as the belief-space
  analogue of **`𝒲_k`** (blind), not of `𝒲^{fb}_k` — the correction
  repair A costs;
* `rem:feedback-strict` records `𝒲_k ⊆ 𝒲^{fb}_k` with strict inclusion
  under `thm:support`'s own hypotheses, the `{p,q}` witness, agreement
  on a blind window, and the consequence that `thm:support` is a feedback
  theorem while `prop:degen` is blind.

Earlier text here said the edit "is drafted in
`paper2_repairA_thm_support_v1.tex`", which understated the state: that
file is the standalone draft, and its content is in v12."""

OLD_BINOM = "### `P3_Binomial` — machinery for Sperner (v31, INCOMPLETE)"
NEW_BINOM = "### `P3_Binomial` — machinery for Sperner (v31, complete machinery)"

OLD_BINOM_TAIL = """**What remains, and why it is not done.** Three steps: (1) unimodality,
`C(n,k) ≤ C(n, n/2)`; (2) LYM, by maximal-chain counting; (3) the
cardinality bound. Step 1 was attempted and **failed**, informatively:
the two-step recursion needs the case `2(k+2) = n+1`, which is binomial
*symmetry* — so symmetry must precede unimodality, and symmetry is itself
a separate induction. Step 2 needs factorials, a permutation enumerator,
and `C(n,k)·k!·(n-k)! = n!`, none of which exists here."""
NEW_BINOM_TAIL = OLD_BINOM_TAIL + """

**Scoped in v41: the machinery is complete, and nothing here is
half-built.** `choose` and every law this module claims are proved; the
module does exactly the job it was built for, which is to make
`prop:antichain` (iii) *statable* — the layer had no binomials at all, so
the bound could not previously be written down. It is **machinery only**:
the Sperner bound itself is **cited, not formalized, by decision**, and
that decision is unchanged. The three steps listed above were never
claimed; step 1's failure is a recorded finding about a route not taken,
not an unfinished proof."""

PATCHES = [
    ("paper2_probabilistic_sufficiency_v11.tex",
     "paper2_probabilistic_sufficiency_v12.tex",
     "P3 paper pointer v11 -> v12"),
    (OLD_DRAFT, NEW_DRAFT, "repair A merge state"),
    (OLD_BINOM, NEW_BINOM, "P3_Binomial heading"),
    (OLD_BINOM_TAIL, NEW_BINOM_TAIL, "P3_Binomial scoped note"),
    ("### EBC — `prop:ladder` (analysed, not started)",
     "### EBC — `prop:ladder` (closed in v38; see the status section below)",
     "stale prop:ladder heading"),
]

def main():
    s = io.open(SRC, encoding="utf-8").read()
    for old, new, label in PATCHES:
        if old in s:
            s = s.replace(old, new, 1)
            print(f"ok   {label}")
        else:
            print(f"MISS {label}")
    io.open(DST, "w", encoding="utf-8").write(s)
    print(f"wrote {DST}: {len(s.splitlines())} lines, {os.path.getsize(DST)} bytes")

if __name__ == "__main__":
    main()
