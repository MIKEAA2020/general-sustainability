"""Reproduce the model M1/M2 additions. Python 3, numpy and matplotlib.

Run from any directory: python code/compute_c13.py
Outputs are relative to the package root. No network or fitted data are required.

The specified Euler/method-of-steps convention is retained for trajectories. Budget
quadrature independently evaluates the continuous RHS on saved nodes and uses
trapezoidal integration. No term is adjusted to force budget closure.
"""
from pathlib import Path
import csv
import json
import math
import hashlib
import platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
COLS = ['Af','Ac','q','P','D','Ar','B','E','bf','Tb']
TERMS = ['conversion','maintenance_retirement','restoration','quality','fast_yield']
DTS = [.05, .025, .0125, .00625, .003125, .0015625, .00078125]
CASES = [
    dict(id='F100', label='Frozen demand', T=100., Ac0=1.5, P0=1.5, Efixed=.825, chi=0., wave=False),
    dict(id='R400', label='Endogenous recovery', T=400., Ac0=1., P0=2., Efixed=None, chi=.1, wave=False),
    dict(id='N250', label='No-wave control', T=250., Ac0=.9, P0=1., Efixed=None, chi=.1, wave=False),
    dict(id='W250', label='Technology wave', T=250., Ac0=.9, P0=1., Efixed=None, chi=.1, wave=True),
]
PARAMETERS = dict(Atot=2.5, Af0=.6, q0=.9, D0=0., bf0=.85, bc=.05, bGc=.8,
                  rho=.08, alpha=.03, eta=.05, mu=.06, etaf=.05, Amin=.05,
                  tauconv=1., taug=20., taup=25., e=.55, r=.02, Kmin=.02,
                  delta_b=1., kappa=.1, twave=40.)


def writecsv(path, rows):
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def identification():
    bf, T, amin, umin, umax, B, C = .85, 2.5, .05, .05, .066, .825, .04
    af = (B-C)/bf
    aggregate = (amin, min(T, B/umin, (bf*T-B)/(bf-umax)))
    plus_af = (max(amin,C/umax), min(T-af,C/umin))
    q = .9
    known_q = C/(.05+.8*.08*q*(1-q))
    rows = []
    for label, bounds in [('B only',aggregate),('B and independently known Af',plus_af),('B, Af and independently known q', (known_q,known_q))]:
        rows.append(dict(observation_package=label, lower_Ac_ha=bounds[0], upper_Ac_ha=bounds[1], width_ha=bounds[1]-bounds[0]))
    witnesses=[]
    for name,ac,q in [('lower',plus_af[0],.5),('upper',plus_af[1],1.)]:
        u=.05+.8*.08*q*(1-q);ar=T-af-ac;recon=bf*af+u*ac
        assert ar>=0 and abs(recon-B)<1e-12
        witnesses.append(dict(endpoint=name,Ac_ha=ac,Af_ha=af,Ar_ha=ar,q=q,Ups_gha_per_ha=u,reconstructed_B_gha=recon))
    # Feasibility checks at all endpoints, plus grid verification of the formula.
    for ac in np.linspace(amin,aggregate[1],1001):
        low=umin*ac;high=bf*(T-ac)+umax*ac
        assert low<=B+1e-12 and high>=B-1e-12
    assert abs(aggregate[1]-(bf*T-B)/(bf-umax))<1e-12
    qroots=[(.5-math.sqrt(.25-(C/known_q-.05)/(.8*.08))),(.5+math.sqrt(.25-(C/known_q-.05)/(.8*.08)))]
    return rows,witnesses,dict(B=B,C=C,Af=af,bf=bf,T=T,amin=amin,Ups_bounds=[umin,umax],known_q=.9,Ac_given_q=known_q,compatible_q_roots_given_Ups=qroots)


def simulate(case, dt):
    p=PARAMETERS;n=round(case['T']/dt);a=np.zeros((n+1,10),dtype=float)
    def vals(t,Af,Ac,q,P,D):
        tb=(1./(1.+math.exp(-p['kappa']*(t-p['twave'])))) if case['wave'] else 0.
        bf=(p['bf0']+tb)*math.exp(-p['alpha']*D)
        B=bf*Af+(p['bc']+p['bGc']*p['rho']*q*(1-q))*Ac
        E=case['Efixed'] if case['Efixed'] is not None else p['e']*P
        return B,E,bf,tb
    a[0,:5]=[p['Af0'],case['Ac0'],p['q0'],case['P0'],p['D0']]
    a[0,5]=p['Atot']-a[0,0]-a[0,1];a[0,6:]=vals(0.,*a[0,:5])
    # No-wave prehistory is shared in both technology cases, per specified SI S8.
    Bhist=p['bf0']*p['Af0']+(p['bc']+p['bGc']*p['rho']*p['q0']*(1-p['q0']))*case['Ac0']
    clips={k:0 for k in ['Af','Ac','P','D','q_upper']}; max_q_overshoot=0.
    def past(col,time,k,history):
        if time<=0:return history
        u=time/dt;lo=math.floor(u+1e-10);w=u-lo
        if abs(w)<1e-9:w=0.
        if lo>k-1:raise ValueError('Unavailable delayed state')
        return a[lo,col] if w==0 else a[lo,col]*(1-w)+a[lo+1,col]*w
    for k in range(1,n+1):
        t=k*dt;Af,Ac,q,P,D,Ar,B,E,bf0,tb0=a[k-1]
        # specified convention: old current states, right-end time-dependent input/delays.
        bf=(p['bf0']+(1/(1+math.exp(-p['kappa']*(t-p['twave']))) if case['wave'] else 0))*math.exp(-p['alpha']*D)
        qp=past(2,t-p['taug'],k,p['q0']);Bp=past(6,t-p['taup'],k,Bhist)
        # Recompute the current account on the old state with the right-end wave.
        # The saved B column is retained separately for delayed-history lookup.
        Bcurrent=bf*Af+(p['bc']+p['bGc']*p['rho']*q*(1-q))*Ac
        S=max(E-Bcurrent,0.);uc=min(S/bf,max(Ac-p['Amin'],0.))/p['tauconv']
        R=case['chi']*Ar*max(Bcurrent-E,0.);dq=p['rho']*qp*(1-qp)
        if q>=1:dq=min(dq,0.)
        if q<=0:dq=max(dq,0.)
        raw=[Af+dt*(uc+p['mu']*Ar-p['etaf']*Af),Ac+dt*(-uc+R),q+dt*dq,
             P+dt*p['r']*P*(1-P/max(Bp/p['e'],p['Kmin'])),D+dt*(S-p['eta']*D)]
        for j,key,floor in [(0,'Af',0.),(1,'Ac',p['Amin']),(3,'P',0.),(4,'D',0.)]:
            if raw[j]<floor-1e-14:clips[key]+=1
            raw[j]=max(raw[j],floor)
        if raw[2]>1:clips['q_upper']+=1
        max_q_overshoot=max(max_q_overshoot,raw[2]-1.)
        raw[2]=min(max(raw[2],0.),1.)
        a[k,:5]=raw;a[k,5]=p['Atot']-a[k,0]-a[k,1];a[k,6:]=vals(t,*raw)
    t=np.arange(n+1)*dt
    assert a[:,5].min()>-1e-12, 'Negative reserve: this run is inadmissible'
    assert max(clips[k] for k in ['Af','Ac','P','D'])==0,clips
    # Independent continuous-RHS node evaluation: no discrete telescoping allocation.
    Af,Ac,q,P,D,Ar,B,E,bf,Tb=a.T
    qp=np.interp(t-p['taug'],t,q,left=p['q0'])
    dq=p['rho']*qp*(1-qp);dq=np.where(q>=1,np.minimum(dq,0),dq)
    S=np.maximum(E-B,0);uc=np.minimum(S/bf,np.maximum(Ac-p['Amin'],0))/p['tauconv']
    R=case['chi']*Ar*np.maximum(B-E,0)
    dD=S-p['eta']*D
    tbprime=p['kappa']*Tb*(1-Tb) if case['wave'] else np.zeros_like(t)
    dbf=np.exp(-p['alpha']*D)*tbprime-p['alpha']*bf*dD
    integrands=np.column_stack(((bf-(p['bc']+p['bGc']*p['rho']*q*(1-q)))*uc,
         bf*(p['mu']*Ar-p['etaf']*Af),
         (p['bc']+p['bGc']*p['rho']*q*(1-q))*R,
         p['bGc']*p['rho']*(1-2*q)*Ac*dq,Af*dbf))
    cumulative=np.vstack([np.zeros((1,5)),np.cumsum((integrands[:-1]+integrands[1:])*(dt/2),axis=0)])
    integrals=cumulative[-1];delta=B[-1]-B[0];resid=delta-float(integrals.sum())
    technology=Af*np.exp(-p['alpha']*D)*tbprime
    debt=-p['alpha']*Af*bf*dD
    ti=float(np.sum((technology[:-1]+technology[1:])*(dt/2)))
    di=float(np.sum((debt[:-1]+debt[1:])*(dt/2)))
    assert abs(ti+di-integrals[-1])<1e-10
    result=dict(case=case['id'],T_yr=case['T'],dt_yr=dt,B0_gha=B[0],BT_gha=B[-1],delta_B_gha=delta,
                **{term+'_gha':float(v)for term,v in zip(TERMS,integrals)},technology_subterm_gha=ti,debt_subterm_gha=di,integral_sum_gha=float(integrals.sum()),closure_residual_gha=resid,
                relative_closure_abs=abs(resid)/max(abs(delta),1e-15),minimum_Ac_ha=float(Ac.min()),final_Ac_ha=float(Ac[-1]),minimum_Ar_ha=float(Ar.min()),peak_D_gha_yr=float(D.max()),peak_D_time_yr=float(t[np.argmax(D)]),quality_ceiling_clips=clips['q_upper'],maximum_quality_overshoot_before_clipping=max_q_overshoot,quality_cap_first_node_yr=float(t[np.flatnonzero(q>=1)[0]]),conversion_availability_limiter_nodes=int(np.sum(S/bf>np.maximum(Ac-p['Amin'],0)+1e-12)),max_area_balance_error_ha=float(np.max(np.abs(Af+Ac+Ar-p['Atot']))),other_state_clips=sum(clips[k]for k in ['Af','Ac','P','D']))
    return t,a,cumulative,result


def tables(bounds,witnesses,results):
    tex=ROOT/'tables'
    labels=[r'$B$',r'$B,A_f$',r'$B,A_f,q$']
    (tex/'model_bounds_rows.tex').write_text('\n'.join(f'{lab} & {r["lower_Ac_ha"]:.6f} & {r["upper_Ac_ha"]:.6f} & {r["width_ha"]:.6f} \\\\'for lab,r in zip(labels,bounds))+'\n')
    (tex/'model_witness_rows.tex').write_text('\n'.join(f'{r["endpoint"]} & {r["Af_ha"]:.6f} & {r["Ac_ha"]:.6f} & {r["Ar_ha"]:.6f} & {r["q"]:.1f} & {r["Ups_gha_per_ha"]:.3f} & {r["reconstructed_B_gha"]:.3f} \\\\'for r in witnesses)+'\n')
    fine={r['case']:r for r in results if r['dt_yr']==DTS[-1]}
    fields=[('conversion_gha','Conversion'),('maintenance_retirement_gha','Maintenance/retirement'),('restoration_gha','Restoration'),('quality_gha','Quality readout'),('fast_yield_gha','Fast-yield change'),('integral_sum_gha','Sum of integrals'),('delta_B_gha',r'$B(T)-B(0)$'),('closure_residual_gha','Closure residual')]
    def make(cases):
        return '\n'.join(name+' & '+' & '.join(f'{fine[c][key]:+.6f}'for c in cases)+r' \\' for key,name in fields)+'\n'
    (tex/'model_budget_main_rows.tex').write_text(make(['F100','R400']))
    (tex/'model_budget_all_rows.tex').write_text(make(['F100','R400','N250','W250']))
    (tex/'model_fast_yield_split_rows.tex').write_text('\n'.join(c+' & '+f'{fine[c]["technology_subterm_gha"]:+.8f} & {fine[c]["debt_subterm_gha"]:+.8f} & {fine[c]["fast_yield_gha"]:+.8f}'+r' \\'for c in ['F100','R400','N250','W250'])+'\n')
    (tex/'model_refinement_rows.tex').write_text('\n'.join(f'{r["case"]} & {r["dt_yr"]:.8f} & {r["delta_B_gha"]:+.8f} & {r["integral_sum_gha"]:+.8f} & {r["closure_residual_gha"]:+.3e} \\\\'for r in results)+'\n')
    descriptions={'F100':'Fixed demand','R400':'Restoration','N250':'Control','W250':'Technology'}
    for fragment in tex.glob('model_*_rows.tex'):
        text=fragment.read_text()
        for key,value in descriptions.items():text=text.replace(key,value)
        fragment.write_text(text)
        fragment.write_text(fragment.read_text()+r'\bottomrule'+'\n')
    return fine


def main():
    for d in ['data','tables','figures']:(ROOT/d).mkdir(exist_ok=True)
    bounds,witnesses,info=identification();writecsv(ROOT/'data/model_identification_bounds.csv',bounds);writecsv(ROOT/'data/model_identification_witnesses.csv',witnesses)
    results=[];finest={};grid_comparison=[]
    for case in CASES:
        print('Computing',case['id'],flush=True)
        previous=None
        for dt in DTS:
            t,a,cum,res=simulate(case,dt);results.append(res)
            if previous is not None:
                pt,pa,pc=previous
                # Each refinement has a nested time grid.
                diff=np.max(np.abs(a[::2]-pa),axis=0)
                grid_comparison.append(dict(case=case['id'],coarse_dt_yr=dt*2,fine_dt_yr=dt,max_Ac_difference_ha=float(diff[1]),max_B_difference_gha=float(diff[6]),max_D_difference_gha_yr=float(diff[4])))
            previous=(t,a,cum)
        finest[case['id']]=(t,a,cum)
    writecsv(ROOT/'data/model_budget_refinement.csv',results);writecsv(ROOT/'data/model_nested_grid_comparison.csv',grid_comparison)
    fine=tables(bounds,witnesses,results)
    for case in CASES:
        rows=[r for r in results if r['case']==case['id']]
        # Tested tolerances, not a general error theorem.
        assert abs(rows[-1]['closure_residual_gha'])<abs(rows[0]['closure_residual_gha'])
        assert rows[-1]['relative_closure_abs']<.001
    path=ROOT/'data/model_trajectories_reporting_grid.csv'
    with path.open('w',newline='')as f:
        names=['case','t_yr']+COLS+['cum_'+x+'_gha'for x in TERMS]
        w=csv.writer(f);w.writerow(names)
        for case in CASES:
            t,a,cum=finest[case['id']];stride=round(.05/DTS[-1])
            for k in range(0,len(t),stride):w.writerow([case['id'],f'{t[k]:.6f}']+[f'{x:.12g}'for x in a[k]]+[f'{x:.12g}'for x in cum[k]])
    # Fresh rendering of the existing specified technology-wave illustration at its stated .05 yr step.
    wcase=next(c for c in CASES if c['id']=='W250');ncase=next(c for c in CASES if c['id']=='N250')
    tw,aw,_,rw=simulate(wcase,.05);tn,an,_,rn=simulate(ncase,.05)
    fig,ax=plt.subplots(2,2,figsize=(10,6.3),constrained_layout=True)
    ax[0,0].plot(tw,aw[:,9],color='#4477aa');ax[0,0].set(title='(a) Technology increment',ylabel=r'$T_b$ (gha ha$^{-1}$)')
    for ar,t,a,col in [(ax[0,1],tn,an,'#4477aa'),(ax[0,1],tw,aw,'#cc6677')]:
        lab='wave' if col=='#cc6677' else 'no wave';ar.plot(t,a[:,6],color=col,label='$B$, '+lab);ar.plot(t,a[:,7],color=col,ls='--',label='$E$, '+lab)
    ax[0,1].set(title='(b) Annual account values',ylabel='gha');ax[0,1].legend(fontsize=7,ncol=2)
    for t,a,lab,col in [(tn,an,'no wave','#4477aa'),(tw,aw,'wave','#cc6677')]:
        ax[1,0].plot(t,a[:,3],label=lab,color=col);ax[1,1].plot(t,a[:,4],label=lab,color=col)
        k=np.argmax(a[:,4]);ax[1,1].scatter(t[k],a[k,4],color=col,s=22,zorder=4)
    ax[1,0].set(title='(c) Population',ylabel='cap');ax[1,1].set(title='(d) Leaky model debt',ylabel='gha yr');ax[1,1].legend(fontsize=8)
    for x in ax.flat:x.axvline(40,color='0.5',ls=':',lw=1);x.set_xlabel('Time (yr)');x.grid(alpha=.2)
    fig.savefig(ROOT/'figures/fig_tb_wave_debt.pdf');plt.close(fig)
    validation={
        'scope':'Static identification and integrated contribution budgets for four model conditions',
        'parameters':PARAMETERS,'cases':CASES,'dt_levels':DTS,
        'identification':info,'budget_finest_results':fine,
        'quadrature':'Independent continuous-RHS node evaluation and trapezoidal integration; no balancing adjustment. Closure residual is Delta B minus sum of integrals.',
        'trajectory_convention':'specified method-of-steps Euler: old current state, right-end technology/delayed inputs, projected quality plus finite-step clipping; constant q and no-wave B prehistory.',
        'all_finest_relative_closure_below_0_001':all(r['relative_closure_abs']<.001 for r in fine.values()),
        'all_nonquality_state_clips_zero':all(r['other_state_clips']==0 for r in results),
        'existing_wave_peak_check_at_dt_0_05':dict(no_wave_peak=rn['peak_D_gha_yr'],no_wave_time=rn['peak_D_time_yr'],wave_peak=rw['peak_D_gha_yr'],wave_time=rw['peak_D_time_yr']),
        'versions':dict(python=platform.python_version(),numpy=np.__version__,matplotlib=matplotlib.__version__)
    }
    # Reproduction of the specified printed wave maxima to their 6-decimal rounding.
    assert abs(rn['peak_D_gha_yr']-.008126)<.0000006
    assert abs(rw['peak_D_gha_yr']-.020205)<.0000006
    (ROOT/'data/model_validation_results.json').write_text(json.dumps(validation,indent=2)+'\n')
    print(json.dumps(fine,indent=2))

if __name__=='__main__':main()
