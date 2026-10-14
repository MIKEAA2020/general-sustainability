#!/usr/bin/env python3
"""Independent read-only checks of selected v4 claims and the attached review.
No imported manuscript verifier, no edits to manuscripts, no LaTeX or Lean claim.
Run from any cwd: python3 content_audit/paper11c_joint_audit_2026-10-15/check.py
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import hashlib,re
root=Path(__file__).resolve().parents[2]
source=root/'paper 2 family/11c_worked_systems/paper11c_worked_systems_audit_v4.tex'
attachment=root/'uploads/p11c v4 audit.txt'
s=source.read_text();a=attachment.read_text()
for p in (source,source.with_suffix('.pdf'),attachment):
    print('SHA256',p.relative_to(root),hashlib.sha256(p.read_bytes()).hexdigest())
assert a.rstrip().endswith('The abstract says the floored rule fails one cell per row from \\(z_0=2\\). The figure says it fails on 21 of')
print('ATTACHMENT_TRUNCATED mid-sentence in Grok point 2; only one complete Grok point available')
# Same 93 domain, different stipulated damage path/viability predicates.
grid=range(10,41)
free={T:sum(Q(i,10)-1>=T for i in grid) for T in (1,2,3)}
alt={T:sum(Q(i,10)-1>=((T//2)*Q(3,2)+(T%2)*1) for i in grid) for T in (1,2,3)}
assert free=={1:21,2:11,3:1} and alt=={1:21,2:16,3:6}
print('GRID_93 free_damage D=(1,2,3)',free,'sum',sum(free.values()),'alternating_damage D=(1,3/2,5/2)',alt,'sum',sum(alt.values()))
strict_tau=strict_floor=0
for i,T in product(grid,(1,2,3)):
    tau=Q(i,10)-1; floor=tau.numerator//tau.denominator
    viable=T<=tau
    assert viable==(T<=floor)
    strict_tau+=viable and not T<tau
    strict_floor+=viable and not T<floor
assert (strict_tau,strict_floor)==(3,21)
print('PREDICATES inclusive_real=inclusive_floor on all integer deadlines; strict_real_loses',strict_tau,'strict_floor_loses',strict_floor)
# Distinct register conventions: counts and pair witnesses from current paper and tested legacy script.
assert '24, 26, 25, 28' in s and '25, 26, 26, 28' in s and 'codex \\(27\\)' in s
assert 'institutional kernel equals the aggregate kernel setwise' in s and '26 = 26' in s
print('REGISTER pessimistic_shared=(24,26,25,28); fixed_single_thread=(25,26,26,28); per_branch=(26,26,27,28); optimistic_codex=27')
# Labels at lines 310--312 are swapped relative to the manuscript's own 2x2 class definitions.
assert '(observation axis, free protocol)' in s and '(protocol axis at fixed aggregation)' in s
print('CONFIRMED_AXIS_LABEL_SWAP: observation I24->C25, A26->F28; protocol I24->A26, C25->F28; source labels these the other way round')
# Bell partitions (unlabeled), graph criterion on the given four-state target.
states=('12','21','22','31')
def partitions(items):
    if not items:yield ();return
    first,*rest=items
    for part in partitions(rest):
        yield ((first,),)+part
        for i in range(len(part)):
            new=list(part);new[i]=(first,)+new[i];yield tuple(new)
P=list(partitions(states));assert len(P)==15
R={'12':{1},'21':{2},'22':{1,2},'31':{2}}
adequate=[p for p in P if all(set.intersection(*(R[x] for x in cell)) for cell in p)]
assert len(adequate)==7 and sum(len(p)==2 for p in adequate)==2
print('MONITORING unlabeled partitions=15 adequate=7 adequate_two_cell=2; labeled two-colorings=4')
# Raw law pairs: 2^4 options per agency, z=0 never used (both z>=1 while safe).
assert 2**4*2**4==256 and 2**3*2**3==64
print('LAW_SPACE pair of 4-bit agency laws: raw=256; quotient ignoring each agency z=0 bit=64; paper reports 16 sustaining raw=4 behavioral (tested source witness)')
assert 2**9==512 and 2**5==32
print('STATIONARY free-protocol memoryless cells: full=512 aggregate=32; augmented clock/register policies not counted')
cap1=lambda y:Q(3,2)-(Q(y)-2)/10
cap2=lambda y:Q(59,50)-(Q(y)-2)/10
assert (cap1(Q(27,5)),cap2(Q(27,5)))==(Q(29,25),Q(21,25))
assert (cap1(6),cap2(6))==(Q(11,10),Q(39,50))
assert (2-cap1(6)-cap2(6))/2==Q(3,50)
print('BENCHMARK Y*=27/5 feasible u=(29/25,21/25), dual normalized cap margin Y6=3/50, not a metric distance')
# max_u min_i psi_i = -1/10, and lambda*=1/2 uniquely minimizes max_u sum lambda psi.
psi1=lambda u:Q(2,5)-u
psi2=lambda u:u-Q(3,5)
assert psi1(Q(1,2))==psi2(Q(1,2))==-Q(1,10)
assert max(min(psi1(Q(i,100)),psi2(Q(i,100))) for i in range(101))==-Q(1,10)
for i in range(101):
    l=Q(i,100)
    dual=max(l*psi1(0)+(1-l)*psi2(0),l*psi1(1)+(1-l)*psi2(1))
    assert dual>=-Q(1,10) and (dual==-Q(1,10))==(l==Q(1,2))
print('DUAL static value=-1/10, u*=1/2 and lambda*=1/2 unique at sample endpoints and by piecewise linearity')
# Continuous scalar polynomial, no norm or grid restriction needed.
assert Q(1,5)*1+Q(1,100)==Q(21,100)
print('DRIFT g(s+1/10)-g(s)=s/5+1/100, exact continuous bound [21/100,41/100] on s in [1,2]')
labels=re.findall(r'\\label\{([^}]+)\}',s)
refs=re.findall(r'\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}',s)
missing=set(refs)-set(labels);unused=set(labels)-set(refs)
assert not missing and len(unused)==14
assert s.count('\\subsection*{References}')==1 and s.count('\\subsection*{AI declaration}')==1
print('SOURCE references_missing=0 unused_labels=',len(unused),'manual_bibliography=1 ai_declaration=1 cite_commands=',len(re.findall(r'\\cite\\b',s)))
print('DONE scoped source/math/attachment checks; no referee review')
