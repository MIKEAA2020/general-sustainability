#!/usr/bin/env python3
"""Independent exact checks of EBC live five-cube claims / verifier coverage.
Run: python3 content_audit/scientific_validity/ebc/witnesses.py
"""
from fractions import Fraction as Q
from itertools import product, combinations
from collections import Counter
from pathlib import Path

V=list(product((0,1),repeat=5))
def hd(a,b): return sum(x!=y for x,y in zip(a,b))
# Every indefinitely surviving pair in the five-cube has distance <=2.
# Enumerate ALL maximal cliques of that necessary-condition graph.
import networkx as nx
G=nx.Graph();G.add_nodes_from(V)
G.add_edges_from((a,b) for a,b in combinations(V,2) if hd(a,b)<=2)
cliques=list(nx.find_cliques(G))
assert Counter(map(len,cliques))=={6:32,4:160}
balls={frozenset(v for v in V if hd(c,v)<=1) for c in V}
assert len(balls)==32 and all(frozenset(c) in balls for c in cliques if len(c)==6)
orbits=Counter(tuple(sorted(hd(a,b) for a,b in combinations(c,2))) for c in cliques if len(c)==4)
assert orbits=={(2,2,2,2,2,2):80,(1,1,1,1,2,2):80},orbits
small=[c for c in nx.enumerate_all_cliques(G) if len(c)<=3]
assert len(small)==912 and all(any(set(c)<=ball for ball in balls) for c in small)
print('five-cube graph: 32 six-vertex balls, 80+80 four-vertex orbits, 912 smaller cliques lie in balls')
# For a tetrahedron choose representative vertices 00000,11000,10100,
# 01100: all pairwise distances 2. The sum of their +/-1 sign vectors
# cancels in the first 3 coordinates, equals 4 in each of the last 2.
# Any sign-action yields aggregate drift in tenths <= -20+2*8=-4;
# hold gives -20. Thus no finite initial slack sustains all four.
tetra=((0,0,0,0,0),(1,1,0,0,0),(1,0,1,0,0),(0,1,1,0,0))
assert tuple(sorted(hd(a,b) for a,b in combinations(tetra,2)))==(2,)*6
for u in V:
    drift_sum=sum(5-4*hd(u,t) for t in tetra)
    assert drift_sum<=-4
print('tetra: aggregate slack declines by >=4 tenths per action; impossible at ANY finite starting level (no cap argument needed)')
# A square face has 4 vertices, 2 varying coordinates, 3 fixed.
# Some vertex is >=2 away from ANY sign action; minimum step drift <=-3.
# Hence starting slacks L=0,1,2 fail immediately. Alternating
# opposite square corners yields +2 net for every vertex per two steps;
# minimum transient is -3, so L>=3 suffices forever.
square=((0,0,0,0,0),(1,0,0,0,0),(0,1,0,0,0),(1,1,0,0,0))
assert tuple(sorted(hd(a,b) for a,b in combinations(square,2)))==(1,1,1,1,2,2)
for u in V:
    assert min(5-4*hd(u,t) for t in square)<=-3
for th in square:
    pairdrift=(5-4*hd(square[0],th),5-4*hd(square[3],th))
    assert sum(pairdrift)==2 and min(pairdrift[0],sum(pairdrift))>=-3
print('square: first-step necessity L>=3; opposite-corner two-cycle has min dip 3 and +2 net on all branches')
# Numerical comparison in the new five-cube prose. Raw 4-step
# sequences grow by 33^4/17^4; deduplicated vectors by 11145/545.
ratio4=Q(17**4,545);ratio5=Q(33**4,11145)
assert ratio5<ratio4
assert Q(11145,545)>Q(33**4,17**4)
print('comparative sentence false: 4-cube compression %s, 5-cube compression %s; relative deduplication is LESS, not more' % (ratio4,ratio5))
# Four-cube displayed glance-table per-step formula contradicts actual
# stated drift: for k=0 it yields -1/2 although matched drift is +3/10.
assert -Q(1,2) != Q(3,10)
print('four-cube glance table: printed -1/2-2k/5 is wrong; correct +3/10-2k/5')
# The v13 verifier's m=5 pair loop calls ham(a,b), which only compares
# coordinates 0..3: it never checks pairs differing ONLY at coordinate 4
# against the correct sharp bound, even though the PASS line says 496x33.
a=(1,)*5;b=(1,)*4+(-1,)
h4=lambda x,y:sum(x[i]!=y[i] for i in range(4))
assert h4(a,b)==0 and hd(a,b)==1
wrong_bound=2*(5-h4(a,b)); sharp_bound=2*(5-hd(a,b))
assert (wrong_bound,sharp_bound)==(10,8)
print('source v13 verifier false negative: fifth-coordinate-only pair h=0 in check (actual h=1); bound 10 substituted for sharp 8')
# Proof-completeness gate records missing needles but only checks count.
log=Path('/home/user/content_audit/scientific_validity/ebc/source_run.log').read_text()
assert "PASS proof completeness:" in log and "(missing: ['29-cell radius-two ball'])" in log
print('source verification log confirms a missing proof needle coexists with a green completeness check; see source_run.log')
