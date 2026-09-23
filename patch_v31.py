#!/usr/bin/env python3
"""Patch build_paper2_v31.py with the v31 verified revisions.

Changes:
  1. SUPP path -> v31 supplementary (new file, never overwrite v29).
  2. Inject `from revisions_v31 import apply_revisions; t = apply_revisions(t)`
     right after the source is read (fixes flow to main AND supplementary).
  3. new_11: "finite in the polyhedral and finite-fibre cases"
        -> "finite in the finite-state and polyhedral cases".
  4. thm:delayed proof sketch: inadmissibility branch.
  5. NEW_SECTIONS: replace Theorem 6 block, section 7 intro, section 8
     reproducible model + CE hit time, and section 9 (POMDP) blocks.
"""
import sys

P = "/home/user/build_paper2_v31.py"
s = open(P, encoding="utf-8").read()

def rep(s, old, new, n=1):
    assert s.count(old) >= n, "NOT FOUND (%d< %d): %r" % (s.count(old), n, old[:60])
    return s.replace(old, new, n)

# 1. supplementary path
s = rep(s, "paper2_obstruction_calculus_v29_supplementary.tex",
           "paper2_obstruction_calculus_v31_Automatica_routes_supplementary.tex")

# 2. inject revisions application
anchor = 't = open(SRC, encoding="utf-8").read()'
assert anchor in s
s = rep(s, anchor, anchor + "\n"
        "from revisions_v31 import apply_revisions\n"
        "t = apply_revisions(t)")

# 3. new_11 finite-fibre scoping
s = rep(s, "finite in the polyhedral and finite-fibre cases",
           "finite in the finite-state and polyhedral cases")

# 4. delayed proof sketch: inadmissibility branch
s = rep(s, "open-loop control. (H4.2), applied to it, supplies",
           "open-loop control; if it is ever inadmissible at a compatible state the policy fails "
           "outright, otherwise (H4.2), applied to this implementable control, supplies")

# 5. NEW_SECTIONS edits (targeted, inside the raw string)
i_start = s.index("NEW_SECTIONS = r")
i_open = i_start + len('NEW_SECTIONS = r"""')
i_close = s.index('"""', i_open)
body = s[i_open:i_close]

def load(fn):
    return open(f"/home/user/v31/{fn}", encoding="utf-8").read()

# 5a. section 7 intro sentence
old = ("two settings in which the certificates are complete --- the one-step "
       "(finite discrete) setting and the static-observation setting --- and states "
       "the residual dynamic gap as an open problem.")
body = rep(body, old, load("new_n1.txt").rstrip("\n"))

# 5b. Theorem 6 block (up to, but not including, the open problem)
i = body.index("\\begin{theorem}[static-observation completeness]")
j = body.index("\\begin{openproblem}", i)
body = body[:i] + load("new_n2.txt") + body[j:]

# 5c. reproducible delayed hidden-regime model before the coverage audit
anchor3 = "\\textbf{A coverage audit.}"
i3 = body.index(anchor3)
body = body[:i3] + load("new_n3.txt") + "\n" + body[i3:]

# 5d. CE hitting time rounding
body = rep(body, "\\approx 3.34\\)", "\\approx 3.3\\)")

# 5e. section 9 POMDP development (from the setup sentence to the final remark)
i = body.index("Let \\(X, A, D, Y\\) be finite, with a stochastic transition")
j = body.rindex("\\end{remark}") + len("\\end{remark}")
body = body[:i] + load("new_n9.txt").rstrip("\n") + "\n" + body[j:]

s = s[:i_open] + body + s[i_close:]

open(P, "w", encoding="utf-8").write(s)
print("patched", P, "->", len(s), "bytes")
