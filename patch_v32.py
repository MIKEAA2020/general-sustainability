#!/usr/bin/env python3
"""Create build_paper2_v32.py from build_paper2_v31.py:
   - v32 paths (main + supplementary),
   - apply revisions_v32 on top of revisions_v31,
   - NEW_SECTIONS edits (case-study scope caveat, chance constraint, horizon convention).
"""
src = open("/home/user/build_paper2_v31.py", encoding="utf-8").read()

def rep(s, old, new, n=1):
    assert s.count(old) >= n, "NOT FOUND: %r" % old[:70]
    return s.replace(old, new, n)

# paths
src = rep(src, "paper2_obstruction_calculus_v31_Automatica_routes.tex",
               "paper2_obstruction_calculus_v32_Automatica_routes.tex")
src = rep(src, "paper2_obstruction_calculus_v31_Automatica_routes_supplementary.tex",
               "paper2_obstruction_calculus_v32_Automatica_routes_supplementary.tex")

# second revision pass
anchor = "t = apply_revisions(t)"
assert anchor in src
src = rep(src, anchor, anchor + "\n"
          "from revisions_v32 import apply_revisions_v32\n"
          "t = apply_revisions_v32(t)")

# NEW_SECTIONS edits (inside the raw string)
i_open = src.index("NEW_SECTIONS = r") + len('NEW_SECTIONS = r"""')
i_close = src.index('"""', i_open)
body = src[i_open:i_close]

# Tier B: horizon convention + chance constraint
body = rep(body,
    "\\(V_{0}(b) = b(\\mathcal{V})\\), and for \\(k \\ge 0\\)",
    "\\(V_{0}(b) = b(\\mathcal{V})\\) (the horizon counts the current state), and for \\(k \\ge 0\\)")
body = rep(body,
    "the chance constraint \\(\\mathbb{P}_{\\pi}(x_{t} \\in \\mathcal{V} \\text{ for } t \\le k) \\ge 1 - \\varepsilon\\) is infeasible",
    "the chance constraint \\(\\mathbb{P}_{b,\\pi}(x_{0}, \\dots, x_{k} \\in \\mathcal{V}) \\ge 1 - \\varepsilon\\) is infeasible")

# Tier A8: case-study scope caveat before section 9
anchor9 = "\n\\subsection{9. A Probabilistic Development: Belief-State Safety Values}\\label{probabilistic-development}"
caveat = ("\nThe audit is symbolic and one-dimensional; a multidimensional belief-space\n"
          "numerical campaign is deferred to future work, and the case study makes\n"
          "no claim of a general-purpose computational calculus.\n")
body = rep(body, anchor9, caveat + anchor9)

src = src[:i_open] + body + src[i_close:]

open("/home/user/build_paper2_v32.py", "w", encoding="utf-8").write(src)
print("wrote /home/user/build_paper2_v32.py", len(src), "bytes")
