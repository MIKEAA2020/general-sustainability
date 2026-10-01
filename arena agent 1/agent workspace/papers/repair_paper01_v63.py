#!/usr/bin/env python3
"""Collapse paper01 v63's duplicate Declarations to one, drop the paper02 block.

Dry-run by default; --apply writes the file.

WHAT IS WRONG
    paper01_obstruction_calculus_v63.tex carries TWO declarations blocks:

      L2117  \\section*{Declarations}    -- paper01's own (one-line, \\quad-joined)
      L2120  \\subsection*{Declarations} -- paper02's (\\subsection*-itemised)

    They come from the merge emitting one block per source. The second is
    cross-unit: its Code availability names four paper02 scripts
    (paper2_probabilistic_sufficiency_v14_verification.py,
    paper2_belief_state_v2_verification.py,
    paper2_stochastic_selector_v2_verify.py, paper2_belief_state_figures.py)
    and claims they "reproduce all values, bounds, thresholds, figures, and
    tabulated entries verbatim".

WHY BLOCK 2 IS NOT paper01's
    paper01 v63's label namespace is entirely `calc-` (39 labels: calc-prop,
    calc-thm, calc-rem, calc-tab, calc-fig, calc-ex, calc-def, calc-op,
    calc-cor). It contains no `suff-` labels and no paper02 body. The scripts
    named in block 2 cannot regenerate anything in it.

WHY BLOCK 1'S `paper2_coverage_audit.py` IS NOT THE SAME KIND OF ERROR
    That name looks like contamination but is not: it also appears in the BODY
    at L1775 ("The audit is reproduced by the script
    \\texttt{paper2\\_coverage\\_audit.py} ... which regenerates
    Table~\\ref{calc-tab:coverage} and Figure~\\ref{calc-fig:coverage}
    verbatim"), and those ARE paper01's own labels. paper02 v12 does not
    mention the script at all. It is a STALE FILENAME from the unit rename,
    not cross-unit content -- the same class as the paper08 v42/43/44 pointer.
    Kept as-is; renaming it is a separate, source-level decision.

WHAT THIS REPAIR DOES
    Keeps block 1 intact, and folds in the one thing block 2 has that block 1
    lacks: the fuller AI declaration ("The author reviewed and edited outputs
    and takes responsibility for the final work."). Block 2 is otherwise
    dropped. Nothing is invented.
"""
from __future__ import annotations

import io
import re
import sys

PATH = "/home/user/papers/paper01_obstruction_calculus_v63.tex"

FULLER_AI = ("The author reviewed and edited outputs and takes\n"
             "responsibility for the final work.")


def main() -> int:
    apply = "--apply" in sys.argv
    src = io.open(PATH, encoding="utf-8").read()

    m_sec = re.search(r'\\section\*\{Declarations\}', src)
    m_sub = re.search(r'\\subsection\*\{Declarations\}', src)
    if not m_sec or not m_sub:
        print("expected two declarations blocks; found section=%s subsection=%s"
              % (bool(m_sec), bool(m_sub)))
        return 2

    block1 = src[m_sec.start():m_sub.start()]
    block2 = src[m_sub.start():]

    # block 1 must be paper01's own: it points at calc- labels
    if "calc-tab:coverage" not in block1:
        print("block 1 does not reference paper01's own calc- labels; aborting")
        return 2
    # block 2 must be the paper02 block we intend to drop
    if "paper2_probabilistic_sufficiency" not in block2:
        print("block 2 is not the paper02 block; aborting")
        return 2

    new1 = block1
    if FULLER_AI not in new1:
        new1 = new1.replace(
            "assisted with drafting and iterative review.",
            "assisted with drafting and iterative review. " + FULLER_AI, 1)
    new1 = new1.rstrip() + '\n'

    out = src[:m_sec.start()].rstrip() + '\n\n' + new1 + '\n\\end{document}\n'

    print("block 1 kept : %d chars (calc-tab:coverage present)" % len(block1))
    print("block 2 drop : %d chars (paper02 scripts)" % len(block2))
    print("net change   : %+d chars" % (len(out) - len(src)))
    print()
    print("--- resulting Declarations block ---")
    print(out[out.index("\\section*{Declarations}"):].strip())

    if not apply:
        print("\nDRY RUN - nothing written. Re-run with --apply.")
        return 0

    io.open(PATH, "w", encoding="utf-8").write(out)
    print("\napplied: %s" % PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
