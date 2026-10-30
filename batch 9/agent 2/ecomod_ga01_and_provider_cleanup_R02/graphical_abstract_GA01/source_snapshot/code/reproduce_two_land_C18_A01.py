"""C18 two-land supplemental reproducer. Explicit Euler/method of steps.
C17 baseline convention: old current state, right-end delayed inputs, constant
q/no-wave B prehistory, projected delayed quality. mode=0 is a named CURRENT-
quality sensitivity, not the baseline. Outputs never overwrite recovered files.
"""
from pathlib import Path
import csv,json,math,importlib.util
import numpy as np
from numba import njit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]
@njit
def past(a,col,time,dt,history):
    if time<=0:return history
    x=time/dt;lo=int(math.floor(x+1e-10));w=x-lo
    if abs(w)<1e-9:w=0.
    return a[lo,col] if w==0 else a[lo,col]*(1-w)+a[lo+1,col]*w
@njit
def run(Ac0=1.,P0=2.,chi=.1,T=400.,dt=.1,mode=1,taug=20.,taup=25.,Efixed=-1.,gate=1,target=-1.,freeze=False,q0=.9):
    n=round(T/dt);a=np.zeros((n+1,8)) # Af,Ac,q,P,D,Ar,B,E
    a[0,0]=.6;a[0,1]=Ac0;a[0,2]=q0;a[0,3]=P0;a[0,5]=2.5-.6-Ac0
    B0=.85*.6+(.05+.064*q0*(1-q0))*Ac0
    a[0,6]=B0;a[0,7]=.55*P0 if Efixed<0 else Efixed
    for k in range(1,n+1):
        t=k*dt;Af,Ac,q,P,D,Ar,B,E=a[k-1]
        bf=.85*math.exp(-.03*D);B=bf*Af+(.05+.064*q*(1-q))*Ac
        S=max(E-B,0.);uc=0. if freeze else min(S/bf,max(Ac-.05,0.))
        z= B-E if gate==1 else E-B if gate==2 else 0.
        flow=chi*Ar*max(z,0.) if Efixed<0 else 0.
        # Policy-only target/donor restrictions are inactive in baseline grid runs.
        if gate==2 or target>=0 or freeze:
            flow=min(flow,max(Ar-.05,0.)/dt)
        if target>=0:flow=min(flow,max(target-Ac,0.)/dt)
        qp=past(a,2,t-taug,dt,q0) if mode else q
        dq=.08*qp*(1-qp)
        if q>=1:dq=min(dq,0.)
        Bp=past(a,6,t-taup,dt,B0)
        a[k,0]=max(0.,Af+dt*(uc+.06*Ar-.05*Af))
        a[k,1]=max(.05,Ac+dt*(-uc+flow))
        a[k,2]=min(1.,max(0.,q+dt*dq))
        a[k,3]=max(0.,P+dt*.02*P*(1-P/max(Bp/.55,.02)))
        a[k,4]=max(0.,D+dt*(S-.05*D));a[k,5]=2.5-a[k,0]-a[k,1]
        a[k,6]=.85*math.exp(-.03*a[k,4])*a[k,0]+(.05+.064*a[k,2]*(1-a[k,2]))*a[k,1]
        a[k,7]=.55*a[k,3] if Efixed<0 else Efixed
    return a

def savecsv(name,rows):
    with (R/'data'/(name+'_C18_A01.csv')).open('w',newline='')as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def threshold(Ac,tg=20.,chi=.1,dt=.05,T=1000.,tol=1e-6,mode=1):
    lo=1.;hi=4.
    for _ in range(35):
        mid=(lo+hi)/2
        if run(Ac,mid,chi,T,dt,taug=tg,mode=mode)[:,1].min()-.05<=tol:hi=mid
        else:lo=mid
    return (lo+hi)/2

def main():
    plt.rcParams.update({"font.size":13})
    # Cross-check the compiled loop against the separately implemented C17 solver.
    spec=importlib.util.spec_from_file_location('baseline',R/'inherited_C17/code/simulate_budgets.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    checks=[]
    for idx in [0,1]:
        c=m.CASES[idx];dt=.05;_,a,_,_=m.simulate(c,dt)
        b=run(c['Ac0'],c['P0'],c['chi'],c['T'],dt,Efixed=c['Efixed'] if c['Efixed']is not None else -1.)
        err=float(np.max(np.abs(a[:,:8]-b)))
        if err>2e-11:raise ValueError(('C17 cross-check',idx,err))
        checks.append(dict(case=c['id'],dt=dt,max_abs_state_difference=err))
    grid=[];legacy=[]
    for Ac in [.4,.7,1.,1.18]:
        for P in np.round(np.arange(1.,4.001,.1),1):
            for chi in [.1,0.]:
                a=run(Ac,P,chi);j=int(np.argmin(a[:,1]))
                grid.append(dict(Ac0_ha=Ac,P0_cap=P,chi=chi,minimum_Ac_ha=a[j,1],minimum_gap_ha=a[j,1]-.05,
                    time_min_yr=j*.1,final_Ac_ha=a[-1,1],peak_D_gha_yr=a[:,4].max(),final_Ar_ha=a[-1,5],minimum_Ar_ha=a[:,5].min()))
            # The current-quality experiment is retained separately for provenance comparison.
            b=run(Ac,P,.1,mode=0)
            legacy.append(dict(Ac0_ha=Ac,P0_cap=P,minimum_Ac_ha=b[:,1].min(),final_Ac_ha=b[-1,1]))
    savecsv('si_drawdown_depth',grid);savecsv('current_quality_comparator',legacy)
    old=list(csv.DictReader((R/'repository_sources/manuscript_ECOMOD_v44_src/si_drawdown_depth.csv').open()))
    olderr=max(abs(r['minimum_Ac_ha']-float(z['minAc_ha_chi0.10'])) for r,z in zip(legacy,old))
    oldfinal=max(abs(r['final_Ac_ha']-float(z['finalAc_ha_chi0.10'])) for r,z in zip(legacy,old))
    thresholds=[]
    for Ac in [.4,.7,1.,1.18]:
        g=[r for r in grid if r['Ac0_ha']==Ac and r['chi']==.1]
        z=dict(Ac0_ha=Ac,proximity_1e_2_grid=min(r['P0_cap'] for r in g if r['minimum_gap_ha']<=1e-2),
               proximity_1e_3_grid=min(r['P0_cap'] for r in g if r['minimum_gap_ha']<=1e-3),
               proximity_1e_4_grid=min(r['P0_cap'] for r in g if r['minimum_gap_ha']<=1e-4),
               proximity_1e_6_bisection=threshold(Ac),proximity_1e_6_coarse=threshold(Ac,dt=.1,T=400.))
        thresholds.append(z)
    savecsv('proximity_thresholds',thresholds)
    delays=[]
    for tg in [5.,20.,40.]:
        for chi in [.1,0.]:delays.append(dict(taug_yr=tg,chi=chi,P0_proximity_1e_6=threshold(1.,tg,chi)))
    savecsv('proximity_delay_sensitivity',delays)
    lawchecks=[]
    for mode in [0,1]:
        a=run(1.5,1.5,0.,250.,.05,mode=mode,Efixed=.825)
        idx=np.flatnonzero((np.diff(a[:,6])>0)&(np.diff(a[:,1])<0))
        j=int(idx[-1]+1)
        lawchecks.append(dict(mode='delayed' if mode else 'current',mask_end_yr=j*.05,
            B_end=a[j,6],Ac_end=a[j,1],Af_end=a[j,0],Yc_end=(.05+.064*a[j,2]*(1-a[j,2]))*a[j,1],
            Yf_end=.85*math.exp(-.03*a[j,4])*a[j,0],threshold_coarse=threshold(1.,dt=.1,T=400.,mode=mode)))
    savecsv('quality_law_comparison',lawchecks)

    recovery=[]
    for P in [1.5,2.,2.5,3.,3.5,4.]:
        a=run(1.,P,.1);b=run(1.,P,0.);j=np.argmin(a[:,1]);amin=a[j,1]
        recovery.append(dict(P0=P,E0=.55*P,minimum_Ac=amin,time_min=j*.1,final_Ac_no_restoration=b[-1,1],final_Ac_restoration=a[-1,1],Rc=(a[-1,1]-amin)/(1-amin)))
    savecsv('si_recovery',recovery)
    # Common physically specified reference-generating runs; no hand-entered equilibria.
    ref=run(.9,1.2,0.,3000.,.1);deg=run(.9,2.5,0.,3000.,.1)
    ar=float(ref[-1,1]);pr=float(ref[-1,3]);ad=float(deg[-1,1])
    refs=dict(healthy_Ac=ar,healthy_P=pr,degraded_Ac=ad)
    policies=[('none',0.,0,-1.,False),('surplus_002',.02,1,-1.,False),('surplus_005',.05,1,-1.,False),('surplus_010',.1,1,-1.,False),('target',.1,1,ar,False),('surplus_frozen',.1,1,-1.,True),('deficit_005',.05,2,-1.,False),('deficit_010',.1,2,-1.,False),('deficit_frozen',.1,2,-1.,True)]
    gates=[]
    for dt in [.1,.05,.025]:
        for name,chi,gate,target,frozen in policies:
            a=run(.058,1.2,chi,2000.,dt,gate=gate,target=target,freeze=frozen)
            gates.append(dict(policy=name,dt_yr=dt,Rc100=(a[round(100/dt),1]-ad)/(ar-ad),Rc900=(a[round(900/dt),1]-ad)/(ar-ad),
                final_Ac=a[-1,1],final_Af=a[-1,0],final_Ar=a[-1,5],final_B=a[-1,6],final_E=a[-1,7],P_ratio=a[-1,3]/pr,minimum_Ar=a[:,5].min(),maximum_Ac=a[:,1].max(),peak_D=a[:,4].max(),area_balance_error=np.abs(a[:,0]+a[:,1]+a[:,5]-2.5).max()))
    savecsv('si_gate_sign',gates)
    # Figure 1 retains the original three scientific panels, now with the selected delayed law.
    fig,ax=plt.subplots(1,3,figsize=(10.5,4.3),layout='constrained')
    a=run(1.5,1.5,0.,250.,.05,Efixed=.825);t=np.arange(len(a))*.05
    for col,label,c in [(6,'B (gha)','#246588'),(1,'Ac (ha)','#b45438'),(0,'Af (ha)','#4f8058')]:ax[0].plot(t,a[:,col],label=label,color=c)
    mask=(np.diff(a[:,6])>0)&(np.diff(a[:,1])<0)
    ax[0].fill_between(t[:-1],0,1.6,where=mask,color='#dad5b8',alpha=.4);ax[0].axhline(.825,color='gray',ls='--');ax[0].set(xlim=(0,60),title='(a) Fixed demand' ,xlabel='Time (yr)',ylabel='Account and area (units differ)');ax[0].legend(fontsize=12,frameon=False)
    k=.06/.11;ac=np.linspace(.05,1.6,300);be=.85*k*(2.5-ac)+.05*ac
    ax[1].plot(ac,be,color='#246588');ax[1].axvline(.05,color='gray',ls=':')
    for E in [.7,.9,1.,1.1,1.13]:
        x=(.85*k*2.5-E)/(.85*k-.05);ax[1].plot(x,E,'o',ms=4)
        tx,ty={.7:(1.25,.66),.9:(1.0,.86),1.:(.75,.97),1.1:(.55,1.07),1.13:(.30,1.17)}[E]
        ax[1].annotate(f'{E:.2f}',(x,E),xytext=(tx,ty),fontsize=12,arrowprops=dict(arrowstyle='-',lw=.6,color='gray'))
    ax[1].set(title='(b) Reduced equality relation',xlabel='Ac (ha)',ylabel='Beq (gha)',ylim=(.45,1.23),xlim=(0,1.7))
    for Ac in [.4,.7,1.,1.18]:
        g=[r for r in grid if r['Ac0_ha']==Ac and r['chi']==.1]
        line,=ax[2].plot([r['P0_cap'] for r in g],[r['minimum_Ac_ha'] for r in g],label=f'Ac0={Ac:g} ha')
        th=next(z for z in thresholds if z['Ac0_ha']==Ac);ax[2].plot(th['proximity_1e_6_bisection'],.05,'v',ms=5,color=line.get_color())
    ax[2].axhline(.05,color='gray',ls='--');ax[2].set(title='(c) Endogenous-demand\ndrawdown',xlabel='Initial P (cap)',ylabel='Minimum Ac (ha)');ax[2].legend(fontsize=12,frameon=False)
    for p in ax:p.grid(alpha=.15)
    fig.savefig(R/'figures/fig1_model_dynamics_C18_A01.pdf');fig.savefig(R/'figures/fig1_model_dynamics_C18_A01.png',dpi=160);plt.close(fig)
    summary=dict(baseline_cross_checks=checks,legacy_v44_current_minimum_max_error=olderr,legacy_v44_current_final_max_error=oldfinal,
        conclusion='Historical v44 drawdown uses current quality, not selected delayed quality; C18 baseline grid regenerated.',references=refs,
        thresholds=thresholds,delay_sensitivity=delays,recovery=recovery,gate_rows=gates,
        fig1_fixed_final=dict(Ac=a[-1,1],B=a[-1,6],Af=a[-1,0]),grid_rows=len(grid),source='C17 selected equations; named legacy/current sensitivity only for version audit')
    (R/'data/two_land_summary_C18_A01.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
