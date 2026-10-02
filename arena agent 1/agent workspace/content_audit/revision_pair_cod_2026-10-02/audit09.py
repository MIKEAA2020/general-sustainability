#!/usr/bin/env python3
"""Independent exact-parameter analytical table audit, archived-ensemble analysis,
and direct interval robust feedback recursion. Writes only to this audit directory."""
from __future__ import annotations
import csv,sys,json,math
from pathlib import Path
import numpy as np
ROOT=Path('/home/user'); OUT=ROOT/'content_audit/revision_pair_cod_2026-10-02'
sys.path.insert(0,str(ROOT/'comp/wave_e_cod/src'))
import run_intervention_v3 as cod
# model fit is rebuilt from source CSVs, not read from a pre-rounded TeX cell
fit=cod.fit_surplus();r=float(fit['r']);K=float(fit['K']);L=cod.K_STAR;HI=cod.S_HI
minE,q05,q10=[float(fit[x]) for x in ('train_residual_min','train_residual_q05','train_residual_q10')]
assert len([z for y,z in fit['_res'].items() if y<=cod.TRAIN_END])==24
old=json.load(open(ROOT/'comp/wave_e_cod/results/intervention_results_v3.json'))['fit']
assert all(abs(fit[k]-old[k])<1e-9 for k in ('r','K','train_residual_min','train_residual_q05','train_residual_q10'))
# symmetric surplus exact algebra; parameter values double precision as fitted
G=lambda s,rr=r,kk=K:rr*s*(1-s/kk)
gmax=r*K/4
assert abs(gmax-296.08675347)<.001

def infroot(c,e,rr=r,kk=K):
    x=c-e; d=1-4*x/(rr*kk)
    if d<0:return None
    b=kk/2*(1-math.sqrt(d)); upper=kk/2*(1+math.sqrt(d))
    return max(L,b) if b<=HI and upper>=L else None

def t1(c,e,rr=r,kk=K,phi=0):
    rr=(1-phi)*rr;d=(1+rr)**2-4*(rr/kk)*(L+c-e)
    if d<0:return None
    b=((1+rr)-math.sqrt(d))/(2*rr/kk)
    return max(L,b) if b<=HI else None
rows=[]
for tag,e in [('worst',minE),('q05',q05),('q10',q10)]:
 for name,c in [('BAU',5),('flat_240',240),('flat_180',180),('flat_120',120),('flat_60',60),('flat_0',0)]:
  rows.append({'floor':tag,'policy':name,'T1':t1(c,e),'Tinf':infroot(c,e),'operator':'constant exact algebra'})
 for phi in (.25,.5,.6,.75):
  c=0;rr=(1-phi)*r;rows.append({'floor':tag,'policy':'A_phi'+str(phi),'T1':t1(c,e,phi=phi),'Tinf':infroot(0,e,rr=rr),'operator':'feedback surplus proportional exact algebra'})
# Piecewise-constant declared policies use the deposited exact-interval engine,
# with the fitted coefficients recomputed above. This completes all Table 1 rows.
def graded2(s):return 0. if s<L else (60. if s<1.25*L else 90.)
def graded3(s):return 0. if s<L else (30. if s<1.15*L else (60. if s<1.35*L else 90.))
for name,fn,ths in [('graded2',graded2,[L,1.25*L]),('graded3',graded3,[L,1.15*L,1.35*L])]:
 policy={'fn':fn,'thresholds':ths,'label':name}
 for tag,e in [('worst',minE),('q05',q05),('q10',q10)]:
  b1=cod.boundary(cod.kernel(policy,fit,e,L,1));bi=cod.boundary(cod.kernel_inf_stable(policy,fit,e,L))
  rows.append({'floor':tag,'policy':name,'T1':b1,'Tinf':bi,'operator':'piecewise exact interval recursion'})
for row in rows:
 if row['floor']=='q10' and row['policy']=='A_phi0.6':assert 1091.9<row['Tinf']<1092.1,row
# Method-specific source-year profile rerun at both frozen and freshly refit floors
Y,S,C=fit['_years'],fit['_ssb'],fit['_c_ann'];s0=np.asarray(S[Y<=cod.TRAIN_END][:-1]);delta=np.diff(S[Y<=cod.TRAIN_END]);catch=np.asarray(C[Y<=cod.TRAIN_END][:-1])
krows=[]
for kk in (1000.,1200.,1500.,1769.2,2000.,2500.,3000.,4000.,5000.,7000.):
 x=s0*(1-s0/kk);rr=float(np.dot(x,delta+catch)/np.dot(x,x));rr=max(.001,min(2.0,rr))
 residual=delta+catch-rr*x; floor=float(np.percentile(residual,10)); f05=float(np.percentile(residual,5))
 gk=G(L,rr,kk)
 krows.append({'K':kk,'r':rr,'floor_q10_frozen':q10,'floor_q10_refit':floor,'Cstar_frozen':gk+q10,'Cstar_refit':gk+floor,'T1_frozen':t1(5,q10,rr,kk),'T1_refit':t1(5,floor,rr,kk),'Tinf_frozen':infroot(5,q10,rr,kk),'Tinf_refit':infroot(5,floor,rr,kk),'q05_frozen_vac':rr*kk/4+q05<0,'q05_refit_vac':rr*kk/4+f05<0})
# Independent reproduction of the deposited fixed-floor K-grid diagnostics.
arch_k={float(z['K']):z for z in csv.DictReader(open(ROOT/'comp/wave_e_cod/src/results_srcyear_v3/e2_elevation_k_grid.csv'))}
for z in krows:
 arow=arch_k[z['K']]
 assert abs(z['r']-float(arow['r']))<.000051
 assert abs(z['Cstar_frozen']-float(arow['constructive_q10_raw']))<.011
 if arow['BAU_q10_T1_lo']:
  assert abs(z['T1_frozen']-float(arow['BAU_q10_T1_lo']))<.061,(z['K'],z['T1_frozen'],arow['BAU_q10_T1_lo'])
 assert (z['Tinf_frozen'] is None)==(arow['BAU_q10_Tinf_lo']==''),(z['K'],z['Tinf_frozen'],arow['BAU_q10_Tinf_lo'])
# residual percentile conventions and non-vacuity sensitivity
pool=np.array([fit['_res'][y] for y in sorted(fit['_res']) if y<=cod.TRAIN_END]);qtypes={k:float(np.percentile(pool,5,method=k)) for k in ('linear','inverted_cdf','hazen','weibull')}
# archived bootstrap ensembles are already 2,000 independently seeded replicates; convert
# clipped statistic back to its raw signed counterpart using stored g(K*) and fixed floor.
boot=list(csv.DictReader(open(ROOT/'comp/wave_e_cod/src/results_srcyear_v3/e2_elevation_bootstrap.csv')))
raw=np.array([float(x['g_Kstar'])+q10 for x in boot]);clipped=np.maximum(0,raw)
arch=np.array([float(x['constructive']) for x in boot]);assert np.max(abs(clipped-arch))<1e-7
bootj=list(csv.DictReader(open(ROOT/'comp/wave_e_cod/src/results_ident_v3/e2_bootstrap_joint.csv')))
jraw=np.array([float(x['Cstar']) for x in bootj]);jK=np.array([float(x['K']) for x in bootj])
# Co-equal catch-alignment sensitivity: each convention gets its own fixed-K fit
# and residual pool; no hybrid of one fit and the other convention's floors.
x=s0*(1-s0/K);r_dst=float(np.dot(x,delta+np.asarray(C[Y<=cod.TRAIN_END][1:]))/np.dot(x,x))
res_dst=delta+np.asarray(C[Y<=cod.TRAIN_END][1:])-r_dst*x
floors_dst={'min':float(min(res_dst)),'q05':float(np.percentile(res_dst,5)),'q10':float(np.percentile(res_dst,10))}
align={'source_r':r,'destination_r':r_dst,'destination_floors':floors_dst,'source_Cstar_q10':G(L)+q10,'destination_Cstar_q10':G(L,r_dst,K)+floors_dst['q10'],'destination_BAU_q05_inf':infroot(5,floors_dst['q05'],r_dst,K),'destination_BAU_q10_inf':infroot(5,floors_dst['q10'],r_dst,K)}
(OUT/'COD_ALIGNMENT.json').write_text(json.dumps(align,indent=2))
unc={'n_fixedK':len(raw),'fixedK_raw_q05_q50_q95':np.percentile(raw,[5,50,95]).tolist(),'fixedK_clipped_q05_q50_q95':np.percentile(clipped,[5,50,95]).tolist(),'fixedK_nonpositive_count':int((raw<=0).sum()),'fixedK_nonpositive_fraction':float((raw<=0).mean()),'joint_n':len(jraw),'joint_raw_q05_q50_q95':np.percentile(jraw,[5,50,95]).tolist(),'joint_K_below_LRP_fraction':float((jK<L).mean()),'q05_methods':qtypes,'gmax':gmax,'q05_informative_by_method':{k:(gmax+v>0) for k,v in qtypes.items()}}
# Edwards fit independently from observed local panel; mathematically valid robust
# set recursion for bounded additive defect under the declared fitted affine map.
sys.path.insert(0,str(ROOT/'comp/wave_e_edwards/src'))
import run_intervention as ed
panel=ed.load_panel();ef=ed.fit_affine(panel);epol=ed.make_policies(float(panel[panel['year']<=ed.TRAIN_END]['P_wells'].mean()))
rtr=panel[panel['year']<=ed.TRAIN_END]['R_total'].to_numpy(float)
fl={'UC_min':float(rtr.min()),'UC_q05':float(np.percentile(rtr,5)),'UC_q10':float(np.percentile(rtr,10))}
assert abs(ef['a']-.7460940904262889)<1e-9
EPS_TRAIN=ef['train_residual_max'];EPS_OOS=ef['oos_residual_max'];

def normalize(intervals):
 iv=sorted((lo,hi) for lo,hi in intervals if hi-lo>1e-9);out=[]
 for lo,hi in iv:
  if out and lo<=out[-1][1]+1e-9:out[-1]=(out[-1][0],max(out[-1][1],hi))
  else:out.append((lo,hi))
 return out

def one_step(cur,policy,floor,K,eps):
 if not cur:return []
 A=ef['a'];new=[]
 for plo,phi in ed._pieces(policy['thresholds']):
  # the code uses the lower regime immediately below each threshold
  c=ef['alpha']+ef['beta']*floor+ef['gamma']*policy['fn']((plo+phi)/2)
  for ulo,uhi in cur:
   if uhi-ulo<2*eps-1e-9:continue
   pl=(ulo+eps-c)/A;ph=(uhi-eps-c)/A
   lo=max(pl,plo,K);hi=min(ph,phi,ed.H_HI)
   if hi>lo+1e-9:new.append((lo,hi))
 return normalize(new)

def robust(policy,floor,K,eps,n):
 cur=[(K,ed.H_HI)]
 for _ in range(n):cur=one_step(cur,policy,floor,K,eps)
 return cur

def bnd(iv):return None if not iv else iv[0][0]
# definition-level check against deposited nominal exact interval recursion
for key in ('BAU','flat_90','flat_80','S1','cpm'):
 for k in (618.,660.):
  a=robust(epol[key],fl['UC_min'],k,0,3);b=ed.kernel(epol[key],ef,fl['UC_min'],k,3)
  assert (a==[] and b is None) or (a and b and abs(a[0][0]-b[0][0])<1e-7),(key,k,a,b)
erows=[]
for k in (618.,660.):
 for name in ('BAU','flat_90','flat_80','flat_60','flat_50','flat_0','S1','cpm'):
  for class_name,rr in fl.items():
   for eps_name,eps in [('nominal',0.),('train_defect',EPS_TRAIN),('oos_defect',EPS_OOS)]:
    hist={str(n):bnd(robust(epol[name],rr,k,eps,n)) for n in (1,2,3,4,5,6,8,10,13)}
    erows.append({'threshold':k,'policy':name,'class':class_name,'error':eps_name,'boundary':hist})
# exact oscillation-bound version for discontinuous feedback. Oscillation at any
# small radius crossing a stage boundary is the stage jump, so original r_T fails.
osc={}
for key in ('BAU','flat_90','S1','cpm'):
 P=epol[key];ths=[ed.H_LO]+sorted(P['thresholds'])+[ed.H_HI]
 pvals=[float(P['fn'](.5*(lo+hi))) for lo,hi in zip(ths[:-1],ths[1:])]
 def omega(radius):
  if radius<=0:return 0.
  return max((abs(x-y) for i,x in enumerate(pvals) for j,y in enumerate(pvals) if max(0.0,max(ths[i],ths[j])-min(ths[i+1],ths[j+1])) <= radius+1e-12),default=0.)
 R=0.;rad=[]
 for _ in range(6):R=abs(ef['a'])*R+abs(ef['gamma'])*omega(R)+EPS_TRAIN;rad.append(R)
 osc[key]={'pumping_levels':pvals,'radius_train':rad}
# Output all in separate new paths, never overwrite deposited campaigns.
writecsv=lambda fn,rows:None
for path,rr in [('COD_EXACT_TABLE.csv',rows),('COD_K_SENSITIVITY.csv',krows)]:
 with (OUT/path).open('w',newline='') as f:
  w=csv.DictWriter(f,rr[0].keys());w.writeheader();w.writerows(rr)
(OUT/'EDW_ROBUST_INTERVALS.json').write_text(json.dumps({'fit':ef,'recharge_floors':fl,'train_eps':EPS_TRAIN,'oos_eps':EPS_OOS,'rows':erows,'oscillation':osc},indent=2))
(OUT/'COD_UNCERTAINTY.json').write_text(json.dumps(unc,indent=2))
print('COD FIT r',r,'K',K,'E',minE,q05,q10,'phi60 root',next(x for x in rows if x['floor']=='q10' and x['policy']=='A_phi0.6')['Tinf'])
print('COD K TABLE frozen vs refit representative',[(round(z['K']),round(z['Cstar_frozen'],2),round(z['Cstar_refit'],2)) for z in krows])
print('COD UNCERTAINTY',json.dumps(unc))
print('EDW FIT',ef,'Pbar',float(panel[panel['year']<=ed.TRAIN_END]['P_wells'].mean()),'floors',fl)
for x in erows:
 if x['class']=='UC_min' and x['threshold']==618 and x['policy'] in ('BAU','flat_90','flat_80','S1','cpm') and x['error'] in ('train_defect','oos_defect'):print('EDW',x)
print('EDW radii',osc)
print('RESULT PASS exact-parameter source fits, archived uncertainty raw reconstruction, nominal interval parity, and feedback robust preimages')
