"""Fig. 7 of paper11 v67: the two mechanisms behind the cross-system result.
(a) J-17 annual recharge is near-white: R_t against R_{t-1}, r = 0.17.
(b) The J-17 head increment tracks same-year recharge: dH_t against R_t, r = 0.74.
(c) Persistence/climatology RMSE ratio by horizon (rolling origin, same origin sets
    as the scored ladders): J-17 (crossover between h=1 and h=2) against the stationary
    prediction sqrt(2(1-rho_h)); Northern cod A and B never cross within five years.
Data: wave_e_edwards/data/annual_panel.csv (registered panel) and the cod rerun data.
"""
import csv, numpy as np, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
here = pathlib.Path(__file__).resolve().parent
rows=[r for r in csv.DictReader(open(here/'edw/data/annual_panel.csv')) if r['H_mean'] and 1934<=int(r['year'])<=2023]
yr=np.array([int(r['year']) for r in rows]); H=np.array([float(r['H_mean']) for r in rows]); R=np.array([float(r['R_total']) for r in rows])
dH=H[1:]-H[:-1]
def ack(x,k):
    x=np.asarray(x,float); x=x-x.mean(); return float((x[k:]*x[:-k]).sum()/(x*x).sum())
def ratio_curve(S, first_idx, hmax=5):
    out=[]
    for h in range(1,hmax+1):
        ep=[];em=[]
        for i in range(first_idx,len(S)-h):
            ep.append(S[i+h]-S[i]); em.append(S[i+h]-S[:i+1].mean())
        ep=np.array(ep); em=np.array(em)
        out.append(np.sqrt((ep**2).mean()/(em**2).mean()))
    return np.array(out)
cod=here/'cod/rerun/data'
A=list(csv.DictReader(open(cod/'ncam_2016_table_a2.csv'))); SA=np.array([float(r['ssb_kt']) for r in A]); yA=[int(r['year']) for r in A]
B=list(csv.DictReader(open(cod/'xtencam_table17_ssb.csv'))); SB=np.array([float(r['ssb_kt']) for r in B]); yB=[int(r['year']) for r in B]
hs=np.arange(1,6)
rJ=ratio_curve(H,14); rA=ratio_curve(SA,yA.index(1990)); rB=ratio_curve(SB,yB.index(1965))
predJ=np.array([np.sqrt(max(2*(1-ack(H,h)),0)) for h in hs])
fig,ax=plt.subplots(1,3,figsize=(12.5,3.9))
a=ax[0]; a.scatter(R[:-1],R[1:],s=14,color='k',alpha=.7); a.set_xlabel(r'$R_{t-1}$ ($10^3$ acre-ft)'); a.set_ylabel(r'$R_t$ ($10^3$ acre-ft)')
a.set_title('(a) J-17 recharge is near-white\n$r(R_t,R_{t-1})=%.2f$'%np.corrcoef(R[1:],R[:-1])[0,1],fontsize=10)
a=ax[1]; a.scatter(R[1:],dH,s=14,color='k',alpha=.7); a.set_xlabel(r'$R_t$ ($10^3$ acre-ft)'); a.set_ylabel(r'$\Delta H_t$ (ft)')
b=np.polyfit(R[1:],dH,1); xx=np.linspace(R.min(),R.max(),50); a.plot(xx,np.polyval(b,xx),color='0.4',lw=1)
a.set_title('(b) the head increment tracks same-year recharge\n$r(\\Delta H_t,R_t)=%.2f$'%np.corrcoef(dH,R[1:])[0,1],fontsize=10)
a=ax[2]
a.plot(hs,rJ,'o-',color='k',label='Edwards J-17 (observed)')
a.plot(hs,predJ,'s--',color='0.5',label=r'J-17, stationary prediction $\sqrt{2(1-\rho_h)}$')
a.plot(hs,rA,'^-',color='tab:blue',label='Northern cod, Spec. A')
a.plot(hs,rB,'v-',color='tab:red',label='Northern cod, Spec. B')
a.axhline(1,color='k',lw=.8,ls=':'); a.set_xlabel('horizon $h$ (years)'); a.set_ylabel('RMSE(persistence) / RMSE(training mean)')
a.set_xticks(hs); a.set_ylim(0,1.95); a.legend(fontsize=7.5,loc='upper left',frameon=False)
a.set_title('(c) when climatology overtakes persistence',fontsize=10)
fig.tight_layout(); fig.savefig(here.parent/'figs/fig7_mechanism.png',dpi=200); fig.savefig(here.parent/'figs/fig7_mechanism.pdf')
print('J ratios',rJ.round(3),'pred',predJ.round(3)); print('A',rA.round(3)); print('B',rB.round(3))
