#!/usr/bin/env python3
"""Small independent arithmetic/counterexample checks; not manuscript proof or replay."""
from fractions import Fraction as F
from itertools import product
from math import sqrt, log
import json, pathlib, hashlib
R=pathlib.Path('/home/user');OUT=R/'content_audit/external_six_audits_2026-10-02';v={}
def put(label,value):v[label]=value;print(label,value)
# Paper 02, one-probe and three-probe errors; two probes with randomized ties.
e=F(1,10);p3=3*e*e*(1-e)+e**3;p2=e*e+e*(1-e)
put('02_three_probe_error',str(p3));put('02_two_probe_error_with_fair_ties',str(p2))
put('02_pinned_thresholds', [str(F(21+t,10)) for t in range(5)])
put('02_both_benchmarks_below_pinned_T4', F(25,10)>F(21,10)>F(14,10))
# Paper 03: non-symmetric U=[0,1]. One-sided outer error in (3) is h_U(bar-k-k).
# A sign reversal would fail for bar-k-k=+1; the actual (2) sign is correct.
put('03_nonsymmetric_support_sign_test',{'h_U(+1)':1,'h_U(-1)':0,'required_upper_for_Av_minus_integral':1})
# Paper 04 exact exhaustive value: s and d independent, u1 first, u2 after z1.
acts=(-2,0,2);states=list(product((-1,1),repeat=3)) # s,d1,d2
best={};trees={}
for u1 in acts:
 cells=sorted({2+s*u1+d1 for s,d1,d2 in states});n=0;top=None
 for choice in product(acts, repeat=len(cells)):
  policy=dict(zip(cells,choice));val=sum((F(2-abs(2+s*(u1+policy[2+s*u1+d1])+d1+d2),8) for s,d1,d2 in states),F(0))
  n+=1
  if top is None or val>top:top=val
 best[u1]=str(top);trees[u1]=n
put('04_reachable_trees_by_first_action',trees);put('04_value_by_first_action',best)
put('04_total_reachable_policy_trees',sum(trees.values()))
# Paper 05: cardinality vs real downset baseline.
put('05_fourcube_powerset_per_stored', {'total':str(F(16*2**16,16+15*32)),'one_level':str(F(2**16,32)),'downset_per_stored':str(F(1+16+32,32))})
put('05_fivecube_powerset_per_stored',str(F(16*2**32,3*32+13*112)))
# Paper 06: true harmonic-circle diagonal crossing phi; two printed points checked.
phi=(1+sqrt(5))/2
put('06_harmonic_circle_LHS',{'claimed_diagonal_sqrt2':2*(2*sqrt(2)-1)**2,'true_diagonal_phi':2*(2*phi-1)**2,'claimed_audit_sqrt2_2':(2*sqrt(2)-1)**2+9,'target':10})
root=sqrt(6*sqrt(3)-9)
put('06_two_thirds_diagonal_root',root)
put('06_witness_weight_cutoffs',{'rho1':str((F(2)-F(6,5))/F(6,5)),'rho2':str(F(6,5)/(F(2)-F(6,5)))})
# Paper 09. Use printed registered fit: r=0.2369, K=5000, LRP=884.6.
r=.2369;K=5000.;LRP=884.6;g=lambda s:r*s*(1-s/K)
def lowroot(catch,efloor):
 disc=1-4*(catch+efloor)/(r*K)
 return float('nan') if disc<0 else K*(1-sqrt(disc))/2
put('09_phi60_q10_root_80p87',lowroot(0,80.87/.4))
put('09_flat120_q10_root_80p87',lowroot(120,80.87))
put('09_expansion_boundary_K',2*LRP)
put('09_Fprime_K1000_K5000',[1+r*(1-2*LRP/k) for k in [1000,1500,5000]])
# Current source-year q10 t=1 BAU lower boundary solves F(s)=LRP (monotone near LRP).
def bound1(c,ef,threshold):
 lo,hi=LRP,10000.
 for _ in range(100):
  m=(lo+hi)/2
  if m+g(m)-c-ef<threshold:lo=m
  else:hi=m
 return (lo+hi)/2
put('09_current_q10_t1_bau_certified',bound1(5,80.87,LRP+328.9725))
put('09_current_q10_t1_max_observed_is_below',940.75<bound1(5,80.87,LRP+328.9725))
# Reconstruct SOURCE-year residuals directly from public tables and the printed fit.
import csv, numpy as np
D=R/'comp/wave_e_cod/data'
def rows(name):
 with (D/name).open() as f:return list(csv.DictReader(f))
s={int(x['year']):float(x['ssb_kt']) for x in rows('ncam_2016_table_a2.csv')}
c={int(x['year']):float(x['catch_kt']) for x in rows('catch_schijns_2021.csv')}
res=np.array([s[y+1]-s[y]-g(s[y])+c[y] for y in range(1983,2007)])
put('09_sourceyear_quantiles_reconstructed_rounded_r',{'linear_q05':float(np.percentile(res,5)),'linear_q10':float(np.percentile(res,10)),'hazen_q05':float(np.percentile(res,5,method='hazen')),'weibull_q05':float(np.percentile(res,5,method='weibull')),'inverted_cdf_q05':float(np.percentile(res,5,method='inverted_cdf')),'three_smallest':sorted(res)[:3]})
# The actual deposited bootstrap column is already max(0, raw): inspect sign mass.
B=np.array([float(x['constructive']) for x in rows('e2_elevation_bootstrap.csv')]) if False else np.array([float(x['constructive']) for x in rows('../src/results_srcyear_v3/e2_elevation_bootstrap.csv')])
put('09_bootstrap_constructive_clipped_summary',{'n':len(B),'zero_share':float(np.mean(B==0)),'q05':float(np.percentile(B,5)),'median':float(np.median(B))})
# Horizon: nominal worst-floor map from ceiling vs published certificate erosion.
def horizon(c,ef,eps):
 x=10000.; y=10000.;a=1+r*(1-2*LRP/K);ours=[]
 for t in range(1,36):
  y=y+g(y)-c-ef
  x=x+g(x)-c-ef-eps
  radius=eps*(a**t-1)/(a-1)
  ours.append({'T':t,'nominal':round(y,2),'radius':round(radius,2),'original_accept':y>=LRP+radius,'direct_worst_plus_eps':round(x,2),'direct_accept':x>=LRP})
 return {'published_method_Tmax':max((z['T'] for z in ours if z['original_accept']),default=0),'direct_worst_plus_eps_Tmax':max((z['T'] for z in ours if z['direct_accept']),default=0),'first_eight':ours[:8]}
put('09_q10_horizons_using_rounded_coefficients',horizon(5,80.87,328.9725))
put('09_worst_horizons_using_rounded_coefficients',horizon(5,328.9725,328.9725))
put('09_phi75_nonempty_margin_q10',(1-.75)*r*K/4-80.87)
put('09_phi75_LRP_margin_q10',(1-.75)*g(LRP)-80.87)
# Remaining-review checks for the addendum.
put('04_reviewer_Y5_candidate_meets_demand',F(4,5)+F(4,5)>=2)
put('05_radii_3_to_8_count',len(range(3,9)))
tstar=2.82256976483
put('06_interior_total_margin_window',{'anchor':707/250,'gap':707/250-tstar,'fraction_of_anchor':(707/250-tstar)/(707/250)})
a=1-15.41/60.70
put('09_flat50_institutional_Tempty_rounded',{'UC_min':log((710-631.52)/(660-631.52))/log(1/a),'UC_q10':log((710-642.09)/(660-642.09))/log(1/a)})
put('09_class_specific_vacuity_catches_using_printed_gmax_296p09',{'worst':296.09-328.9725,'q05':296.09-287.36,'q10':296.09-80.87})
# manifest links reviewer files with immutable hashes; never modify uploads.
inputs={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'uploads').glob('*audit.txt')}
manifest={'inputs_sha256':inputs,'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'papers').glob('paper0*_v*.tex') if any(p.name.startswith('paper0'+i+'_') for i in ['2','3','4','5','6','9'])},'results':v}
(OUT/'VERIFICATION.json').write_text(json.dumps(manifest,indent=2))
assert p3==F(7,250) and p2==F(1,10) and trees=={-2:81,0:9,2:81} and best[-2]=='1/2' and abs(2*(2*phi-1)**2-10)<1e-10
