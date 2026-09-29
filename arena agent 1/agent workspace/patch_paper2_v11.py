#!/usr/bin/env python3
"""paper2_exact_belief_computation_v10.tex -> paper2_exact_belief_computation_v11.tex

v42: the paper's verification section describes an apparatus that
predates the mechanized layer. Three targeted edits:

  (a) prop:deadline  — results are proved, not only simulated
  (b) sectionmethods — describe the apparatus as it now is, and say
                       which warrant each result actually carries
  (c) section scope   — make the blind-class restriction precise, with
                       the structural caveat stated rather than glossed

New version number; the v10 source is never overwritten.
"""
import io, os

SRC = "/home/user/paper2.tex"                                   # v10
DST = "/home/user/paper2_exact_belief_computation_v11.tex"

# ---------------------------------------------------------------- (a)
OLD_A = ("verified by direct simulation on the grid. The excursion vanishes")
NEW_A = ("verified by direct simulation on the grid and, independently, by a\n"
         "mechanized proof (Section~\\ref{methods}). The excursion vanishes")

OLD_A2 = ("the simulation certifies\nthe identity cell by cell on the grid.")
NEW_A2 = ("the simulation certifies\nthe identity cell by cell on the grid. The mechanized layer proves\nthe same threshold as an \\emph{equivalence} --- viability holds iff\n"
          "\\(z_{0} \\ge 1 + T/2\\) --- over an arbitrary ordered field and with\n"
          "\\(T\\) symbolic, so neither the grid nor the restriction\n"
          "\\(T \\le 4\\) is load-bearing for the argument.")

# ---------------------------------------------------------------- (b)
OLD_B = "and every headline number asserted present in this\ntext."
NEW_B = OLD_B + """

\\textbf{A second, independent apparatus.} The script above enumerates;
it does not prove. Alongside it, the results of
Sections~\\ref{bands}--\\ref{deadline} are formalized in a mechanized
layer (Lean~4, 54 modules, 60 build jobs) with no axioms, no admitted
gaps, and no reliance on a computer-algebra oracle: every statement is
derived from the ordered-field interface alone, so it holds in any
model of that interface. The two apparatus were built separately and
agree where they overlap --- the ladder's first two entries
(\\(1/16\\) at the edge, \\(1/8\\) above it), the
adjacency-triangle fact behind the \\(560\\)-triple check, and the
\\(16\\)-singleton / \\(32\\)-pair census. Agreement of an enumeration
with a proof is evidence about both; it is not a substitute for either.

What each result now rests on, stated plainly:

\\begin{itemize}
\\item \\textbf{Proved.} The band structure at the floor and above the
edge (Section~\\ref{bands}); the ladder's value form
(Section~\\ref{ladder}); the deadline threshold
(Section~\\ref{deadline}). These hold as stated over an arbitrary
ordered field, with the support size and the horizon symbolic.

\\item \\textbf{Enumerated, not proved.} The census, the \\(84\\)
point-based pairings, the \\(83{,}521 \\to 545\\) deduplication, and the
dimension-scope battery at \\(m \\ne 4\\). These are finite checks over
the cube; their content is the count, and a count is what the script
supplies.

\\item \\textbf{Simulated.} The \\(60\\)-step ball certificates at
\\(m = 5\\) and \\(m = 7\\), and the grid certification of the deadline
thresholds. For the deadline the simulation is now redundant --- the
threshold is proved --- and is retained as an independent cross-check.
\\end{itemize}

\noindent Where this text previously attributed a result to simulation
or enumeration alone, the attribution above governs."""

# ---------------------------------------------------------------- (c)
OLD_C = "as in the class discipline of the companion theory (Abaee, 2026, An obstruction calculus)."
NEW_C = ("as in the class discipline of the companion theory\n"
         "(Abaee, 2026, An obstruction calculus), where the blind and\n"
         "observation-dependent recursions are shown to differ --- the\n"
         "feedback family contains the blind one, strictly, under\n"
         "hypotheses of the same shape as this instance's. That result is\n"
         "proved \\emph{in the companion's model}; the correspondence with\n"
         "the cube here is one of form, not of type, so it motivates\n"
         "restricting to the blind class rather than proving that\n"
         "restriction necessary. It does, however, fix the meaning of the\n"
         "open question recorded above: since the two disciplines differ\n"
         "strictly somewhere, whether a non-blind discipline beats the\n"
         "pairs \\emph{on the cube} cannot be settled by transferring the\n"
         "companion's strictness, and is left open.")

PATCHES = [
    (OLD_A,  NEW_A,  "(a) prop:deadline statement"),
    (OLD_A2, NEW_A2, "(a) prop:deadline proof"),
    (OLD_B,  NEW_B,  "(b) verification methods"),
    (OLD_C,  NEW_C,  "(c) blind-class precision"),
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
