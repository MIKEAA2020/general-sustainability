#!/usr/bin/env python3
"""
Pass 3 (v35) — final review pass: three clarifying edits for references that
became forward references after the reorder, plus nothing else.

  F1  Section 3.2 Farkas discussion: "stated there" -> "stated in Section 3.4"
      (the Helly witness now lives two subsections ahead).
  F2  Section 3.3 H4.2: name the section of the exit theorem's proof class.
  F3  Section 3.1 one-step instance: name the section of the common-action
      theorem.
"""

import sys

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN_IN = f"{LATEX_DIR}/paper2_obstruction_calculus_v34_Automatica_routes.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v35_Automatica_routes.tex"

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def sub(text, old, new, name):
    n = text.count(old)
    assert n == 1, f"[{name}] {n} occurrences (expected 1)"
    return text.replace(old, new)

def main():
    text = read(MAIN_IN)

    text = sub(text,
        "convexity hypotheses stated there.",
        "convexity hypotheses stated in Section 3.4.",
        "F1")

    text = sub(text,
        "of class \\(C^1\\) (the\nclass of Theorem~\\ref{thm:exit}'s proof)",
        "of class \\(C^1\\) (the class of Theorem~\\ref{thm:exit}'s proof, Section 3.5)",
        "F2")

    text = sub(text,
        "This is\nTheorem~\\ref{thm:common-action} in the finite-horizon language",
        "This is\nTheorem~\\ref{thm:common-action} (Section 3.2) in the finite-horizon language",
        "F3")

    with open(MAIN_OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {MAIN_OUT}  ({len(text)} bytes)")

if __name__ == "__main__":
    main()
