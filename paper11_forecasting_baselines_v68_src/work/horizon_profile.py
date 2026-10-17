"""paper11 v67, SI S23: horizon profile of the two baselines (h = 1..5) on the three
scored series, on the origin sets of the scored ladders, with the lag-h autocorrelation
of the predictand and the stationary prediction sqrt(2(1-rho_h)) of Remark 2; and the
autocorrelations used by Proposition 2 (Section 5.1). Registered data only.
Writes si_parts/gen/tabS23_horizon.tex and si_parts/gen/tabS23_autocorr.tex and prints
a JSON summary (work/horizon_profile.json). Standard library + numpy.
"""
import csv, json, pathlib, numpy as np
here = pathlib.Path(__file__).resolve().parent
root = here.parent
def ack(x,k):
    x=np.asarray(x,float); x=x-x.mean(); return float((x[k:]*x[:-k]).sum()/(x*x).sum())
def profile(S, first_idx, hmax=5):
    out=[]
    for h in range(1,hmax+1):
        ep=[];em=[]
        for i in range(first_idx,len(S)-h):
            ep.append(S[i+h]-S[i]); em.append(S[i+h]-S[:i+1].mean())
        ep=np.array(ep); em=np.array(em)
        rp=float(np.sqrt((ep**2).mean())); rm=float(np.sqrt((em**2).mean()))
        out.append(dict(h=h,n=len(ep),persist=rp,mean=rm,ratio=rp/rm,rho_h=ack(S,h),pred=float(np.sqrt(max(2*(1-ack(S,h)),0.0)))))
    return out
# --- data ---
edw=[r for r in csv.DictReader(open(here/'edw/data/annual_panel.csv')) if r['H_mean'] and 1934<=int(r['year'])<=2023]
H=np.array([float(r['H_mean']) for r in edw]); R=np.array([float(r['R_total']) for r in edw]); P=np.array([float(r['P_wells']) for r in edw])
cod=here/'cod/rerun/data'
A=list(csv.DictReader(open(cod/'ncam_2016_table_a2.csv'))); SA=np.array([float(r['ssb_kt']) for r in A]); yA=[int(r['year']) for r in A]
B=list(csv.DictReader(open(cod/'xtencam_table17_ssb.csv'))); SB=np.array([float(r['ssb_kt']) for r in B]); yB=[int(r['year']) for r in B]
landB={int(r['year']):float(r['catch_kt']) for r in csv.DictReader(open(cod/'dfo_2025_table1_landings.csv'))}
landA={int(r['year']):float(r['catch_kt']) for r in csv.DictReader(open(cod/'catch_schijns_2021.csv'))}
series={'J-17 head (ft)':(H,14),'Cod A, SSB (kt)':(SA,yA.index(1990)),'Cod B, SSB (kt)':(SB,yB.index(1965))}
res={k:profile(*v) for k,v in series.items()}
# --- table S23a ---
L=[r'\begin{tabular}{@{}lrrrrrrr@{}}',r'\toprule',r'Series & $h$ & $n$ & persist & mean & ratio & $\rho_h$ & $\sqrt{2(1-\rho_h)}$ \\',r'\midrule']
for k,rows in res.items():
    for i,r in enumerate(rows):
        name=k if i==0 else ''
        L.append(f"{name} & {r['h']} & {r['n']} & {r['persist']:.2f} & {r['mean']:.2f} & {r['ratio']:.3f} & {r['rho_h']:.3f} & {r['pred']:.3f} \\\\")
    L.append(r'\midrule')
L[-1]=r'\bottomrule'; L.append(r'\end{tabular}')
(root/'si_parts/gen/tabS23_horizon.tex').write_text('\n'.join(L)+'\n')
# --- autocorrelations for Proposition 2 ---
dH=H[1:]-H[:-1]
X=np.c_[np.ones(len(dH)),R[1:],P[1:],H[:-1]]; coef,*_=np.linalg.lstsq(X,dH,rcond=None)
m=coef[1]*R+coef[2]*P
def corr(a,b): return float(np.corrcoef(a,b)[0,1])
def coarse(y): return 240.0 if y<=1991 else (120.0 if y==1992 else 5.0)
CA=np.array([coarse(y) for y in yA]); PA=SA[1:]-SA[:-1]+CA[:-1]
CA2=np.array([landA[y] for y in yA]); PA2=SA[1:]-SA[:-1]+CA2[:-1]
CB=np.array([landB.get(y,landB[2023]) for y in yB]); PB=SB[1:]-SB[:-1]+CB[:-1]
auto=[('J-17: annual recharge $R_t$', ack(R,1), float(R.mean()), float(R.std())),
      ('J-17: annual pumpage $P_t$', ack(P,1), float(P.mean()), float(P.std())),
      ('J-17: flux mechanism $\\hat\\beta R_t+\\hat\\gamma P_t$', ack(m,1), float(m.mean()), float(m.std())),
      ('J-17: head increment $\\Delta H_t$', ack(dH,1), float(dH.mean()), float(dH.std())),
      ('J-17: head $H_t$', ack(H,1), float(H.mean()), float(H.std())),
      ('Cod A: apparent net production, coarse regime', ack(PA,1), float(PA.mean()), float(PA.std())),
      ('Cod A: apparent net production, annual landings', ack(PA2,1), float(PA2.mean()), float(PA2.std())),
      ('Cod B: apparent net production, landings', ack(PB,1), float(PB.mean()), float(PB.std())),
      ('Cod A: SSB $S_t$', ack(SA,1), float(SA.mean()), float(SA.std())),
      ('Cod B: SSB $S_t$', ack(SB,1), float(SB.mean()), float(SB.std()))]
L=[r'\begin{tabular}{@{}lrrr@{}}',r'\toprule',r'Series & $\rho_1$ & mean & s.d. \\',r'\midrule']
for n,a,mu,sd in auto: L.append(f"{n} & {a:.3f} & {mu:.2f} & {sd:.2f} \\\\")
L+= [r'\bottomrule',r'\end{tabular}']
(root/'si_parts/gen/tabS23_autocorr.tex').write_text('\n'.join(L)+'\n')
summary=dict(profiles=res, autocorr={n:dict(rho1=a,mean=mu,sd=sd) for n,a,mu,sd in auto},
   corr=dict(dH_R=corr(dH,R[1:]), dH_Rlag=corr(dH,R[:-1]), R_Rlag=corr(R[1:],R[:-1]), H_pairs=corr(H[1:],H[:-1])),
   fullsample_fit=dict(alpha=coef[0],beta=coef[1],gamma=coef[2],delta=coef[3]),
   prop2=dict(sigma2_1m2rho=float(m.var()*(1-2*ack(m,1))), persist_mse=13.230085772397212**2,
              pred_M2_rmse=float(np.sqrt(13.230085772397212**2+m.var()*(1-2*ack(m,1)))),
              observed_M2m_vs_M2_mse_gap=14.697759248814572**2-12.28321959100849**2))
json.dump(summary,open(here/'horizon_profile.json','w'),indent=1,default=float)
print(json.dumps(summary['prop2'],indent=1)); print(summary['corr'])
for k,rows in res.items(): print(k,[round(r['ratio'],3) for r in rows],[round(r['pred'],3) for r in rows])
