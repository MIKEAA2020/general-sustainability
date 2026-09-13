#!/usr/bin/env python3
# Build v27 from v26: three targeted restorations from the pre-restructuring v15.
#   (a) restore the productive-base passage of Section 1.1 (condensed at v16.2);
#   (b) re-add the site-local symbol-meanings note to Section 2.4, updated to v26 symbols;
#   (c) re-insert the "one minimal construction" categorization into the abstract,
#       with a compensating 2-word trim so the abstract stays under 265 words.
# No other change is made; v27 must reverse-reconstruct v26 modulo these edits.

import sys

SRC = "/home/user/arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v26.tex"
DST = "/home/user/arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v27.tex"

with open(SRC, encoding="utf-8") as f:
    t = f.read()

edits = []

# ---- (a) productive-base passage, Section 1.1 -------------------------------
old_a = (
    "Floors in sustainability assessment are typically constraints on the\n"
    "productive base --- the state of the system that yields the measured\n"
    "output --- rather than on the output itself. Because a base can be drawn\n"
    "down while measured output is maintained, the signal that would reveal\n"
    "erosion is often the one that is coarse, postponed, or absent.\n"
    "Incomplete observation is therefore structural to the certification problem, not merely a practical limitation; the sufficiency literature and the obstruction calculus of this paper address the same underlying indeterminacy rather than competing ones."
)
new_a = (
    "Floors in sustainability assessment are typically constraints on the\n"
    "productive base --- the state of the system that yields the measured\n"
    "output --- rather than on the output itself. Such a base can be read as\n"
    "natural capital, as a stock, or as a slowly regenerating flow of\n"
    "services; these are overlapping readings of the same asset rather than\n"
    "mutually exclusive ones, and what makes a use of it sustainable is\n"
    "whether the use falls on the yield or on the base itself. Across\n"
    "assets, whether the base behaves as a flow or as a stock is a\n"
    "continuum, set by its regeneration timescale relative to the rate of\n"
    "use --- a continuum that runs from a season, through a year, to\n"
    "geological time for a mineral deposit. If a base regenerates too\n"
    "slowly for the rate at which it is taken, drawdown is still\n"
    "liquidation.\n"
    "\n"
    "A base can also erode while measured output is maintained: the\n"
    "degradation is not yet reflected in the measured quantity, or it is\n"
    "offset by a higher per-unit service, because use may draw on the base\n"
    "rather than on its yield. The signal that would reveal the erosion is\n"
    "accordingly often the one that is coarse, postponed, or absent.\n"
    "Incomplete observation is therefore structural to the certification\n"
    "problem, not merely a practical limitation; the sufficiency literature\n"
    "and the obstruction calculus of this paper address the same underlying\n"
    "indeterminacy rather than competing ones."
)
edits.append(("a: productive-base passage", old_a, new_a))

# ---- (b) site-local note, Section 2.4 --------------------------------------
old_b = (
    "\\(\\mathcal{Y}_{\\mathrm{safe}}\\).\n"
    "\n"
    "The four correspondences of this section are one skeleton."
)
new_b = (
    "\\(\\mathcal{Y}_{\\mathrm{safe}}\\).\n"
    "\n"
    "Some letters carry site-local meanings. The strip width \\(a\\) of\n"
    "Theorem~\\ref{thm:exit}'s \\(\\mathcal{S}_a\\) is not the held action\n"
    "\\(a = \\pi(B)\\) of Theorem~\\ref{thm:common-action}'s proof, nor the\n"
    "pathway vector \\(a \\ge 0\\) of Section 5(d); \\(\\lambda\\) is the Farkas\n"
    "multiplier of Theorem~\\ref{thm:common-action}'s checkability\n"
    "certificate and the observer decay rate of Section 5(c); and\n"
    "\\(\\alpha\\) is the comparison function of Remark~\\ref{rem:comparison}\n"
    "and a multiplier of Section 5(d)'s substitution alternative. The\n"
    "letter \\(K\\) denotes the safe set of Section 4's certification\n"
    "problems, while in Section 2.2 and Section 5(c) it denotes the kernel\n"
    "itself, with the buffered set \\(K_\\zeta\\) and eroded kernels\n"
    "\\(K^{-c\\zeta}\\) of Section 5(c). The observation-error map of\n"
    "Section 2.3 is \\(H(\\xi, v)\\), whereas the harvest vector of\n"
    "Appendix A is the lowercase \\(h\\); and the finite-horizon recursion\n"
    "set \\(\\mathcal{W}_N\\) of Section 3.5 is calligraphic, distinct from\n"
    "the Lyapunov function \\(W = S_1 + S_2\\) of Appendix A.2.\n"
    "\n"
    "The four correspondences of this section are one skeleton."
)
edits.append(("b: site-local note", old_b, new_b))

# ---- (c) abstract taxonomy + compensating trim -----------------------------
old_c = (
    "Five mechanisms are established, with a sixth exhibited under a\n"
    "policy-class restriction."
)
new_c = (
    "Five mechanisms are established --- two finitely checkable, two\n"
    "closed-form conditional, one minimal construction --- with a sixth\n"
    "exhibited under a policy-class restriction."
)
edits.append(("c: abstract taxonomy", old_c, new_c))

old_c2 = "the observation-based counterpart of the kernel"
new_c2 = "the kernel's observation-based counterpart"
edits.append(("c2: abstract trim", old_c2, new_c2))

# ---- apply, with uniqueness checks -----------------------------------------
out = t
for name, old, new in edits:
    n = out.count(old)
    if n != 1:
        print(f"ABORT: anchor for '{name}' found {n} times (expected 1)")
        sys.exit(1)
    out = out.replace(old, new)
    print(f"applied {name}")

with open(DST, "w", encoding="utf-8") as f:
    f.write(out)
print(f"wrote {DST} ({len(out)} bytes)")

# ---- reverse reconstruction check: applying inverse edits to v27 -> v26 ----
back = out
for name, old, new in reversed(edits):
    back = back.replace(new, old)
print("v27 reverse-reconstructs v26 (modulo the 4 edits):", back == t)
