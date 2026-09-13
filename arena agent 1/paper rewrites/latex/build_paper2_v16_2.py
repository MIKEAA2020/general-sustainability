#!/usr/bin/env python3
"""Build paper2 v16.2 from v16.1: remaining Layer-1 prose items.
1. Compress the Sec 1.1 'base vs yield' essay to one paragraph.
2. Reduce em-dashes: convert the worst paired-dash interruptions to
   parentheses/commas (genuine appositive asides kept).
3. Trim word tics: 'genuine', 'genuinely', 'precisely', two non-load-bearing
   'exactly' instances.
No theorem, proof, equation, or numbering changes.
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v16_1.tex"
src = open(SRC, encoding="utf-8").read()

def w(plain):
    rx = re.escape(plain)
    rx = re.sub(r'\\\s+', r'\\s+', rx)
    return rx

def sub(plain, new, expect=1):
    global src
    rx = w(plain)
    found = len(re.findall(rx, src))
    assert found == expect, f"SUB expect={expect} found={found}: {plain[:70]!r}"
    src = re.sub(rx, lambda m: new, src)

def sub_any(plain, new):
    global src
    rx = w(plain)
    found = len(re.findall(rx, src))
    src = re.sub(rx, lambda m: new, src)
    return found

def block(rx, new, expect=1):
    global src
    found = len(re.findall(rx, src, re.DOTALL))
    assert found == expect, f"BLOCK expect={expect} found={found}: {rx[:70]!r}"
    src = re.sub(rx, lambda m: new, src, flags=re.DOTALL)

# ---------- 1. Sec 1.1 essay compression ----------
block(r"Floors in sustainability assessment are typically constraints not on\nwhat a system yields but on the state of the system that yields it ---\non a productive base\. Such a base can be read as natural capital, as a\nstock, or as a slowly regenerating flow of services\. These are\noverlapping readings of the same asset rather than mutually exclusive\nones\. What makes a use of it sustainable is whether the use falls on the\nyield or on the base itself\. Across assets, whether the base behaves as\na flow or as a stock is a continuum, set by its regeneration timescale\nrelative to the rate of use\. This continuum runs from a season, through\na year, to geological time for a mineral deposit\. If a base regenerates\ntoo slowly for the rate at which it is taken, drawdown is still\nliquidation\.\n\nSuch a base can erode while measured output is maintained\. The\ndegradation is not yet reflected in the measured quantity, or it is\noffset by a higher per-unit service, because use may draw on the base\nrather than on its yield\. The signal that would reveal the erosion is\naccordingly often the one that is coarse, postponed, or absent\.\nIncompleteness of observation in sustainability governance is therefore\nnot merely a practical limitation\. It is a structural feature of the\ncertification problem, and it is in this sense that the sufficiency\nliterature and the obstruction calculus of this paper address the same underlying indeterminacy rather than competing ones\.",
      r"""Floors in sustainability assessment are typically constraints on the
productive base --- the state of the system that yields the measured
output --- rather than on the output itself. Because a base can be drawn
down while measured output is maintained, the signal that would reveal
erosion is often the one that is coarse, postponed, or absent.
Incompleteness of observation is therefore a structural feature of the
certification problem, not merely a practical limitation; the
sufficiency literature and the obstruction calculus of this paper
address the same underlying indeterminacy rather than competing ones.""")

# ---------- 2. em-dash reductions ----------
sub(r"its certificates remain valid --- and typically tighten --- when the institution's command set",
    r"its certificates remain valid, and typically tighten, when the institution's command set")
n = sub_any(r"the convexified --- relaxed --- inclusion", r"the convexified (relaxed) inclusion")
print("convexified/relaxed:", n)
sub(r"considers the same problem as Section 3 --- a tube in the state space, incomplete and inexact measurement --- and gives",
    r"considers the same problem as Section 3 (a tube in the state space under incomplete and inexact measurement) and gives")
n = sub_any(r"the robust --- all-disturbance --- reachable set", r"the robust (all-disturbance) reachable set")
print("robust all-disturbance:", n)
sub(r"converse results show that --- under convex-duality conditions on density functions --- the existence",
    r"converse results show that, under convex-duality conditions on density functions, the existence")
sub(r"merging states whose safe controls differ is what the theorem certifies --- and keeping every fibre within a single class is what removes that exposure",
    r"merging states whose safe controls differ is what the theorem certifies, and keeping every fibre within a single class is what removes that exposure")
sub(r"on opposite sides of a floor --- per-floor measurement is one sufficient design --- a formal complement",
    r"on opposite sides of a floor (per-floor measurement is one sufficient design), a formal complement")

# ---------- 3. word tics ----------
sub(r"and Example~\ref{ex:hidden-mode} gives the genuine hidden-mode instance.",
    r"and Example~\ref{ex:hidden-mode} gives the hidden-mode instance.")
sub(r"by information; the genuine", r"by information; the", expect=1)
sub(r"information genuinely lost.", r"information lost.")
sub(r"closed-loop realization is an additional requirement --- exactly the content of (H1.2)",
    r"closed-loop realization is an additional requirement --- the content of (H1.2)")
sub(r"the pair is exactly the Farkas lemma alternative.", r"the pair is the Farkas lemma alternative.")
sub(r"is precisely the certificate that no jointly admissible selection exists",
    r"is the certificate that no jointly admissible selection exists")

# ---------- header bump ----------
sub(r"% Amin Abaee. Revision v16.1 (symbol collisions from v16 fixed: Farkas lambda->mu, observer decay alpha->lambda, estimation error eta->zeta, patch coupling gamma->kappa). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v16.2 (Sec 1.1 compressed; em-dashes reduced; word tics trimmed). Compiles with tectonic, pdflatex, or xelatex.")

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v16_2.tex", "w", encoding="utf-8").write(src)
print("wrote v16.2,", len(src), "bytes")
print("em-dashes now:", src.count("---"))
