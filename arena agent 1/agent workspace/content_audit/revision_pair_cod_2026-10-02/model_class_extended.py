#!/usr/bin/env python3
"""Explicitly conditional cod likelihood/posterior and 2-channel sensitivity. Never a physical guarantee."""
from pathlib import Path
import json, csv, math
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import f as fdist, norm
import sys
R=Path('/home/user');O=R/'content_audit/revision_pair_cod_2026-10-02'
sys.path.insert(0,str(R/'comp/wave_e_cod/src'))
import run_intervention_v3 as ri
fit=ri.fit_surplus();y=np.asarray(fit['_years']);s=np.asarray(fit['_ssb']);c=np.asarray(fit['_c_ann']);mask=y<=ri.TRAIN_END
S=s[mask];Y=np.diff(S)+c[mask][:-1];X=S[:-1];n=len(Y);L=ri.K_STAR;floor=-80.86977895283727
assert n==24 and abs(fit['r']-0.236869402778272)<1e-8
Klo=max(X)+10.;rlo=.001;rhi=2.;Khi=5000.; g=lambda r,K:r*L*(1-L/K)

def ss(K,r=None):
 x=X*(1-X/K);rhat=np.clip(np.dot(x,Y)/np.dot(x,x),rlo,rhi)
 rr=rhat if r is None else r
 return float(np.sum((Y-rr*x)**2)),float(rhat)
# Official pin is K<=5000; allow K>= Klo and refit growth at each K.
res=minimize_scalar(lambda k:ss(k)[0],bounds=(Klo,Khi),method='bounded',options={'xatol':1e-5})
K0=Khi if ss(Khi)[0]<=res.fun else float(res.x);sse0,r0=ss(K0);assert abs(r0-fit['r'])<1e-5
# Necessary and sufficient LRP fixed-point condition under same registered floor:
# r*LRP*(1-LRP/K)+floor-C >=0 (independent of higher-state kernel topology).
def rcrit(k,C=0.):return (C-floor)/(L*(1-L/k))
# Find best-fitting nonpositive-margin model in the physical and expansive domains.
def best_failure(low,C=0.):
 def atK(k):
  x=X*(1-X/k);rr=np.clip(np.dot(x,Y)/np.dot(x,x),rlo,min(rhi,rcrit(k,C)));return float(np.sum((Y-rr*x)**2)),float(rr)
 grid=np.linspace(low,Khi,2001);idx=int(np.argmin([atK(k)[0] for k in grid]));sslo=max(low,grid[max(0,idx-2)]);sshi=min(Khi,grid[min(len(grid)-1,idx+2)])
 loc=minimize_scalar(lambda k:atK(k)[0],bounds=(sslo,sshi),method='bounded') if sshi>sslo else None
 candidates=[low,Khi,grid[idx]]+([float(loc.x)] if loc is not None else [])
 k=min(candidates,key=lambda k:atK(k)[0]);loss,rr=atK(k)
 return {'K':float(k),'r':rr,'sse':loss,'SSE_ratio':loss/sse0,'Cstar':g(rr,k)+floor,'policy_margin_C':g(rr,k)+floor-C}
scenarios={key:best_failure(lower,C) for key,lower,C in [('nonpositive_LRP',max(L,Klo),0.),('nonpositive_LRP_expansive',max(2*L,Klo),0.),('BAU_5kt_failure_expansive',max(2*L,Klo),5.)]}
# 95% simultaneous 2-parameter nonlinear regression F-region, conditional Gaussian iid homoscedastic errors.
# This F approximation is not an exact finite-sample joint region for nonlinear K, and the optimizer is on a boundary.
cut_F=1+2*fdist.ppf(.95,2,n-2)/(n-2)
cut_LR=math.exp(float(__import__('scipy').stats.chi2.ppf(.95,2))/n) # n*log(SSE/SSE0)<=chi2_2
for z in scenarios.values():z['inside_F_cut_approx']=bool(z['SSE_ratio']<=cut_F);z['inside_LR_cut_approx']=bool(z['SSE_ratio']<=cut_LR)
# Conditional partial identification: single moment E[X*(deltaS+C-rX)]=0 gives only r=r(K).
# Fit-tolerance profile F(1,n-2) is a separate sampling-likelihood assumption.
profile=list(csv.DictReader(open(R/'comp/wave_e_cod/src/results_ident_v3/e2_profile_K.csv')))
pmin=min(float(x['sse']) for x in profile);pcut=pmin*(1+fdist.ppf(.95,1,n-2)/(n-2))
pin=[x for x in profile if float(x['sse'])<=pcut];Cfixed=[float(x['Cstar']) for x in pin]
# Alternate choice recomputes q10 at each K: not same as archived fixed-floor profile.
residual_floor=[]
for z in pin:
 k=float(z['K']);rr=ss(k)[1];e=Y-rr*X*(1-X/k);residual_floor.append(g(rr,k)+np.percentile(e,10))
# Proper *conditional* Bayesian posterior: uniform r in [.001,2], K in [Klo,5000],
# IID N(0,sigma^2) innovations in the increments; p(sigma^2) ∝ 1/sigma^2 integrated out.
# The independent normal error likelihood and priors are analyst choices, not established data properties.
ks=np.linspace(Klo,Khi,700);rs=np.linspace(rlo,rhi,2100);logw=[];rchunks=[];cchunks=[]
for kk in ks:
 xx=X*(1-X/kk);SSE=np.sum((Y[:,None]-xx[:,None]*rs[None,:])**2,axis=0)
 logw.append(-n/2*np.log(SSE));cchunks.append(g(rs,kk)+floor)
logw=np.array(logw);m=logw.max();w=np.exp(logw-m);w/=w.sum();cstars=np.array(cchunks)
# Equal-volume grid cells: HPD threshold on posterior density (not equal-tailed rectangle).
order=np.argsort(w.ravel())[::-1];cum=np.cumsum(w.ravel()[order]);lim=w.ravel()[order[np.searchsorted(cum,.95)]];hpd=w>=lim
hpd_refit=[]
for i,kk in enumerate(ks):
 if not hpd[i].any():continue
 rsel=rs[hpd[i]];xx=X*(1-X/kk)
 q10=np.percentile(Y[:,None]-xx[:,None]*rsel[None,:],10,axis=0)
 hpd_refit.extend((g(rsel,kk)+q10).tolist())
# Prior-sensitivity: Jeffreys/log-uniform alternatives for positive r,K in
# the same declared box, with the same conditional Gaussian likelihood.
wlog=np.exp(logw-m)/(ks[:,None]*rs[None,:]);wlog/=wlog.sum()
idxlog=np.argsort(wlog.ravel())[::-1];cumlog=np.cumsum(wlog.ravel()[idxlog]);cutlog=wlog.ravel()[idxlog[np.searchsorted(cumlog,.95)]];hpdlog=wlog>=cutlog
logprior={'prior':'log-uniform r,K on same box; same Gaussian likelihood and Jeffreys sigma prior','posterior_mass_Cstar_le_0':float(wlog[cstars<=0].sum()),'HPD_95_min_Cstar':float(cstars[hpdlog].min()),'HPD_95_includes_nonpositive_budget':bool(np.any(hpdlog&(cstars<=0)))}
# Paired floor convention changes the uncertainty set: refitting the residual
# quantile at each candidate parameter is different from a registered fixed floor.
F_refit_min=(float('inf'),None)
for kk in np.linspace(Klo,Khi,600):
 xx=X*(1-X/kk);rrs=np.linspace(.001,.6,900)
 errs=Y[:,None]-xx[:,None]*rrs[None,:];SSE=np.sum(errs**2,axis=0)
 eligible=SSE<=sse0*cut_F
 if not eligible.any():continue
 q=np.percentile(errs[:,eligible],10,axis=0);margin=g(rrs[eligible],kk)+q
 idx=int(np.argmin(margin))
 if margin[idx]<F_refit_min[0]:F_refit_min=(float(margin[idx]),[float(rrs[eligible][idx]),float(kk),float(SSE[eligible][idx]/sse0)])
posterior={'prior':'r ~ Uniform[.001,2], K ~ Uniform[max(training SSB)+10,5000]; Jeffreys p(sigma^2) proportional 1/sigma^2','likelihood':'independent Gaussian zero-mean additive one-step innovations in delta S+source-year catch, not externally validated','grid':[int(len(ks)),int(len(rs))],'posterior_mass_Cstar_le_0':float(w[cstars<=0].sum()),'posterior_mass_Cstar_lt_5':float(w[cstars<5].sum()),'HPD_95_mass_actual':float(w[hpd].sum()),'HPD_95_min_Cstar':float(cstars[hpd].min()),'HPD_95_includes_nonpositive_budget':bool(np.any(hpd&(cstars<=0))),'HPD_95_min_Cstar_if_q10_refit_each_model':float(min(hpd_refit)),'HPD_95_refit_floor_assumption':'q10 recomputed from the same residual data for each candidate r,K; not an independent future process channel','HPD_95_min_K':float(np.repeat(ks[:,None],len(rs),axis=1)[hpd].min()),'HPD_95_max_K':float(np.repeat(ks[:,None],len(rs),axis=1)[hpd].max())}
# Two-channel dependence thought experiment: do not infer variances from one residual.
mu=-10.9;sd=114.9;sig1=sig2=sd/np.sqrt(2);z=norm.ppf(.9);want=g(fit['r'],fit['K']);rho_star=(((want+mu)/z)**2-sig1**2-sig2**2)/(2*sig1*sig2)
correlation={'status':'ILLUSTRATIVE only: sigma1=sigma2=114.9/sqrt(2) and mu=-10.9 are arbitrary allocations of ONE measured residual pool; not estimates of independent channels','assumed_mu':mu,'assumed_sigma1':sig1,'assumed_sigma2':sig2,'normal_q10_model':'q10(rho)=mu-1.2815515655*sqrt(sigma1^2+sigma2^2+2*rho*sigma1*sigma2)','LRP_g':want,'zero_catch_flip_rho':float(rho_star),'BAU_5kt_flip_rho':float(((((want-5+mu)/z)**2-sig1**2-sig2**2)/(2*sig1*sig2))),'rho_cases':{str(v):{'normal_q10':float(mu-z*math.sqrt(sig1**2+sig2**2+2*v*sig1*sig2)),'LRP_Cstar':float(want+mu-z*math.sqrt(sig1**2+sig2**2+2*v*sig1*sig2))} for v in [0,.25,.5,.75,1.]},'note':'Normal q10 at rho=0 need not equal empirical q10=-80.87. Sensitivity is conditional on the Gaussian and scale assumptions; correlation alone supplies no quantile or deterministic bound.'}
result={'observed':{'n':n,'rfit':r0,'Kfit':K0,'SSE':sse0,'K_min_from_campaign':Klo,'q10_floor_fixed':floor,'Cstar_fit':g(r0,K0)+floor},'fail_boundary':'for K>LRP, Cstar<=C iff r<=(C-floor)/(LRP*(1-LRP/K)); only local LRP budget, not full policy kernel','closest_failing_models':scenarios,'conditional_joint_region':{'F_cut_SSE_ratio':float(cut_F),'Wilks_LR_cut_SSE_ratio':float(cut_LR),'approx_grid_min_Cstar_refit_q10':F_refit_min[0],'approx_grid_min_Cstar_refit_q10_at_r_K_SSEratio':F_refit_min[1],'refit_scope':'approximate gridded minimum under same F cut; recalibrating q10 on the same residuals is NOT an independent future error bound','assumptions':'iid Gaussian zero-mean additive errors, conditional on observations/catches and model form; nonlinear/boundary K makes nominal 95% approximate'},'partial_identification':{'single_moment_identifies':'r as function of K only; absent assumptions on K or noise distributions, neither parameter nor a 95% confidence set is identified by that moment','archived_grid_K_bounds':[min(float(z['K']) for z in pin),max(float(z['K']) for z in pin)],'profile_F95_Cstar_fixed_floor_range':[min(Cfixed),max(Cfixed)],'profile_F95_Cstar_refit_floor_range':[float(min(residual_floor)),float(max(residual_floor))],'status':'profile is conditional likelihood/tolerance, not assumption-free identified set'},'posterior':posterior,'posterior_log_prior_sensitivity':logprior,'channel_correlation_illustration':correlation}
(O/'MODEL_CLASS_EXTENDED.json').write_text(json.dumps(result,indent=2))
# Visual diagnostic; contours are assumption-dependent, not physical coverage sets.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
kr=np.linspace(Klo,Khi,450);rr=np.linspace(.001,.65,560)
SSEgrid=np.array([np.sum((Y[:,None]-(X*(1-X/k))[:,None]*rr[None,:])**2,axis=0)/sse0 for k in kr])
fig,ax=plt.subplots(figsize=(8.4,5.3))
ax.fill_between(kr,0,np.minimum(.65,[rcrit(k) for k in kr]),color='#f7d7d4',alpha=.7,label='C* < 0 at registered fixed q10')
ax.contour(kr,rr,SSEgrid.T,levels=[cut_F],colors=['#355b97'],linewidths=[2]);
ax.contour(ks,rs,hpd.T.astype(float),levels=[.5],colors=['#12694c'],linewidths=[1.7]);
ax.scatter([K0],[r0],marker='*',s=180,c='#111111',zorder=5,label='registered fit')
ax.scatter([scenarios['nonpositive_LRP']['K']],[scenarios['nonpositive_LRP']['r']],marker='x',s=90,c='#9b1616',zorder=5,label='best fitting failure')
from matplotlib.lines import Line2D
extra=[Line2D([0],[0],color='#355b97',lw=2,label='approx. joint F 95% boundary'),Line2D([0],[0],color='#12694c',lw=2,label='Gaussian-prior posterior HPD 95%')]
h,l=ax.get_legend_handles_labels();ax.legend(h+extra,l+[x.get_label() for x in extra],loc='upper right',fontsize=8)
ax.set(xlim=(Klo,5000),ylim=(0,.65),xlabel='Carrying capacity K (kt)',ylabel='Growth r',title='Conditional cod parameter-space diagnostic (fixed registered q10 floor)');ax.grid(alpha=.2);fig.tight_layout();fig.savefig(O/'COD_FAILING_SET.png',dpi=170);plt.close(fig)
print(json.dumps(result,indent=2))
