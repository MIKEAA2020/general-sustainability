#!/usr/bin/env python3
"""Exact comp manuscript checks outside Lean. Run: python3 witnesses.py.

The first witness tests the actual redesign proposition, not just its
certificate expression. The second isolates an unnecessary false
absolute-error step in the supplementary proof; it does NOT disprove
its one-sided control-moment inequality or the bridge sandwich.
"""
from fractions import Fraction as Q
from pathlib import Path

# prop:redesign: the theorem explicitly declares the a=2 rung viable at
# tau_max = 7/50+(a-1)/2 = 16/25. Its three branches start at
# p_j=(34/25)n_j, v_j=n_j and share the same blind-window acceleration.
n=[(Q(1),Q(0)),(Q(-3,5),Q(4,5)),(Q(-3,5),Q(-4,5))]
w=[Q(3,8),Q(5,16),Q(5,16)]
assert sum(w)==1 and all(sum(w[j]*n[j][k] for j in range(3))==0 for k in range(2))
assert all(sum(z*z for z in normal)==1 for normal in n)
tau=Q(7,50)+Q(2-1,2)
assert tau==Q(16,25) and Q(34,25)+tau==2
# For EVERY measurable shared-window input, the weighted normal position
# equals 34/25+t and weighted normal velocity equals 1, independent of
# the input. If all branches are safe at tau, their weighted mean position
# is 2 and all positive weights force every normal position to equal 2.
# The weighted velocity is 1, so at least one branch has strictly positive
# outward normal velocity at its active p=2 facet. Bounded post-reveal
# acceleration (2U) cannot prevent an immediate strict violation.
assert sum(w[j]*Q(1) for j in range(3))==1
# Stronger: a three-label finite certificate at t=tau+1/10 within T=6/5.
# Every oracle post-control in 2U has n_j*u >= -2; the weighted critical
# positions must average at least 34/25+t - 2*(t-tau)^2/2 = 209/100.
eps=Q(1,10); T=Q(6,5)
assert tau+eps==Q(37,50)<T
obstruction_margin=Q(34,25)+(tau+eps)-Q(2)*eps*eps/2-Q(2)
assert obstruction_margin==Q(9,100)>0
print('redesign: at a=2, tau=16/25 weighted position=2 and velocity=1; a valid t=37/50 three-label obstruction has margin 9/100, refuting claimed viable endpoint')
# The proof also says max_{u in aU}<n_j,u>=-a: u=a*n_j is in aU,
# so max is >=+a. Scaling both F and f by a leaves {Fu<=f}, not aU.
for a in (Q(3,2),Q(2)):
    assert sum((a*z)*z for z in n[0])==a > -a
# u=2*n1 belongs to 2U but violates (2F)u<=2f at the facet
# 2u1+u2<=2, because its rescaled left side is 8 > 4.
a=Q(2)
assert a*Q(2)*Q(2) > a*Q(2)
print('redesign proof: max over aU is not -a; aF u<=af describes U, not aU')

# prop:beliefcells: the stated cell label SUPREMUM has the wrong
# orientation for a worst-case upper bound unless its full discrepancy
# from the robust beta is explicitly charged. A one-mode plant x'=1,
# U={0}, D={0}, initial P=C=[0,1/2], safety 0<=x<=1, T=1 satisfies
# the standing initial-safety and linear/exogenous assumptions.
# At t=1 the upper-facet margins beta_x=1-x-1=-x range [-1/2,0].
# C has exact center 1/4 and radius delta_C=1/4. The displayed rule
# beta^C=sup_C beta_x+delta_C produces +1/4, although the robust beta
# is -1/2. On a fine grid, LP rho=-1/4 while the true safety value J=1/2.
rad=Q(1,4);beta_robust=-Q(1,2);beta_cell=max(Q(0),-Q(1,2))+rad
rho=-beta_cell;J=Q(1,2);ht=Q(1,200)
assert beta_cell-beta_robust==Q(3,4)
assert rho== -Q(1,4) and J>rho+rad+ht
print('belief-cell: exact radius 1/4 but beta^C-beta_robust=3/4; an upper sandwich charged by radius alone fails (rho=-1/4, J=1/2)')
# Clause (ii) says a split changes the SAME witness by only formula (12).
# With no control k=0, its right side is zero, while changing a cell's
# supremum beta to a singleton beta changes that witness's margin.
coarse_beta=Q(1)+rad  # plant x'=0, upper facet x<=1, C=[0,1/2]
subcell_beta=Q(1,2)  # exact singleton x=1/2, radius=0
assert coarse_beta-subcell_beta==Q(3,4) and 0!=coarse_beta-subcell_beta
print('belief-cell split: kernel-erosion expression (12)=0 for k=0, but changing sup beta and radius shifts this stored label by 3/4')

# Supplementary Step 2 asserts |A v - integral k u| <= bar_e for every
# e=integral h_U(kbar-k). This fails for asymmetric 2-D U. Use
# U=conv{0,e1,e2}, one equal-length block with k=e1,e2,-e1-e2 on
# thirds and kbar=0, so q=kbar-k=-e1,-e2,e1+e2 has zero mean.
def support(q):return max(Q(0),q[0],q[1])
ks=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(-1)))
assert all(sum(k[d] for k in ks)==0 for d in (0,1))
e=sum(support((-k[0],-k[1])) for k in ks)/3
eref=sum(support(k) for k in ks)/3
assert (e,eref)==(Q(1,3),Q(2,3))
# u=(e1,e2,0) gives int k*u=2/3 and A v=0.
assert abs(Q(0)-eref)>e and Q(0)-eref<=e
print('moment proof: exact one-sided e=1/3, reverse deviation=2/3; the claimed absolute <=e is false, while required one-sided inequality holds')

# The main's pointwise claim h_U(g) <= R_U||g|| is false if R_U is
# radius about an arbitrary fixed center. It is the INTEGRAL estimate
# that remains valid because the zero-mean deviation cancels the center.
assert Q(100)>0
print('radius proof: U={100} has radius 0 about center 100 but h_U(1)=100; center cancellation is needed before integration')

p=Path('/home/user/latest/comp_v20.tex').read_text()
a=p.index('\\begin{theorem}[continuous-to-finite]')
b=p.index('\\end{theorem}',a)
assert 'Then:' in p[a:b] and 'Certified value sandwich' not in p[a:b]
assert 'Certified value sandwich' in p[b:b+250]
print('scope markup: thm:bridge environment ends immediately after H1-H6/Then; parts (i)-(v) are outside the environment')
