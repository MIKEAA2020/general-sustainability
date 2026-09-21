"""Build paper5 v46 main from v45 (broadened abstract + 7 keywords).

R1 abstract block -> broadened wrapper (general lead, fisheries as
    demonstration, cross-sector close); results spine unchanged
R2 keywords 9 -> 7 (drop periodic review, sampled-data control,
    Neimark--Sacker bifurcation; add environmental governance)
R3 version comment line v45 -> v46
"""
import re

SRC = '/home/user/paper5_v45/paper5_sampled_governance_v45_NatSustain.tex'
DST = '/home/user/paper5_v46/paper5_sampled_governance_v46_NatSustain.tex'

s = open(SRC, encoding='utf-8').read()

NEW_ABSTRACT = (
"Environmental governance runs on clocks: institutions observe resource systems "
"at discrete times and hold the resulting controls until the next review. Formal "
"models routinely substitute this sampled architecture with a continuous delay or "
"a single annual step. We show the substitution matters. Modelling periodic review "
"as sample-and-hold governance --- a loop that observes and updates only at review "
"times --- we establish two exact properties, forward invariance of the sampled "
"state space and rapid-review consistency over finite horizons only, and compute "
"stability review-interval by review-interval, demonstrated on fisheries. Stability "
"boundaries move or vanish when the operator is changed: at an illustrative baseline "
"the exact map crosses once near a 6.5-year interval while one-step approximations "
"report artefact crossings, and the protective channel is stable at every tested "
"interval. A multiplicity-controlled screen of 42 fish stocks finds no robust "
"institutional cycles and a 32-system cross-sector case search no unconfounded "
"oscillator, showing periodicity alone cannot diagnose governance feedback; the "
"northern cod record splits into a formulation-dependent crash and an unresolved "
"post-collapse identification problem. What decides whether management stabilises or "
"destabilises a renewable resource is therefore not biology alone but the decision "
"clock --- the timing and form of policy revision --- a design variable with "
"stability consequences for any periodically reviewed regime, from fisheries "
"assessment to climate stocktakes.")

NEW_KEYWORDS = ("sample-and-hold governance; review interval; decision clock; "
"institutional delay; management strategy evaluation; fisheries management; "
"environmental governance")

EDITS = [
 ('R1-abstract',
  r'\\begin\{abstract\}.*?\\end\{abstract\}',
  '\\\\begin{abstract}\n' + NEW_ABSTRACT + '\n\\\\end{abstract}', 1),
 ('R2-keywords',
  r'\\textbf\{Keywords:\} periodic review;.*?management strategy evaluation',
  '\\\\textbf{Keywords:} ' + NEW_KEYWORDS, 1),
 ('R3-version-line',
  r'^% The decision clock \(paper 5, revision v45\):.*$',
  ('% The decision clock (paper 5, revision v46): broadened abstract and 7 keywords, '
   'with line numbers for review.'), 1),
]

for name, pat, rep, expect in EDITS:
    s, n = re.subn(pat, rep, s, flags=re.S if name in ('R1-abstract', 'R2-keywords') else re.M)
    print(f'{name}: {n} (expect {expect})')
    assert n == expect, name

open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST, len(s), 'chars')
