"""Targeted independent C11 PDF checks; not the author's code.
Run: python verify_c11.py [path/to/ecomod_continued_11_revision_draft_20261028.pdf]
Requires numpy, scipy, pypdf. Creates text extraction and JSON beside this script.
The reconstruction follows the PDF's right-end delayed-input convention,
with old current states, projected Euler quality, and updated supply history.
It tests one interpretation of the description; original code is still needed.
"""
from pathlib import Path
import sys, json, hashlib, math
import numpy as np
from scipy.optimize import brentq
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
PDF=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT.parent/'uploads/ecomod_continued_11_revision_draft_20261028.pdf'

def run(dt=.05,T=100,tg=20.,Ac0=1.5,P0=1.5,Efixed=.825,chi=0.,project=True):
    n=round(T/dt)
    # Af, Ac, q, P, D, Ar, B, E. No technology in these checks.
    a=np.zeros((n+1,8));a[0,:5]=[.6,Ac0,.9,P0,0.]
    def supply(v):
        Af,Ac,q,P,D=v[:5]
        return .85*math.exp(-.03*D)*Af+(.05+.8*.08*q*(1-q))*Ac
    a[0,5]=2.5-.6-Ac0;a[0,6]=supply(a[0]);a[0,7]=Efixed if Efixed is not None else .55*P0
    B0=a[0,6]
    def past(column,time,k,history):
        if time<=0:return history
        u=time/dt;lo=math.floor(u+1e-10);w=u-lo
        if abs(w)<1e-9:w=0.
        # Delays here are > dt, so no future/current-step interpolation needed.
        assert lo<=k-1
        return a[lo,column] if w==0 else a[lo,column]*(1-w)+a[lo+1,column]*w
    for k in range(1,n+1):
        t=k*dt;Af,Ac,q,P,D,Ar,B,E=a[k-1]
        qpast=past(2,t-tg,k,.9);Bpast=past(6,t-25.,k,B0)
        S=max(E-B,0.);bf=.85*math.exp(-.03*D)
        uc=min(S/bf,max(Ac-.05,0.));R=chi*Ar*max(B-E,0.)
        dq=.08*qpast*(1-qpast)
        if project:
            if q>=1:dq=min(dq,0.)
            if q<=0:dq=max(dq,0.)
        a[k,:5]=[max(Af+dt*(uc+.06*Ar-.05*Af),0.),max(Ac+dt*(-uc+R),.05),
                   min(max(q+dt*dq,0.),1.),max(P+dt*.02*P*(1-P/max(Bpast/.55,.02)),0.),
                   max(D+dt*(S-.05*D),0.)]
        a[k,5]=2.5-a[k,0]-a[k,1];a[k,6]=supply(a[k]);a[k,7]=Efixed if Efixed is not None else .55*a[k,3]
    return a

def main():
    reader=PdfReader(PDF)
    pages=[p.extract_text() or '' for p in reader.pages]
    (ROOT/'c11_extracted_text.txt').write_text('\n\n'.join(f'=== PDF PAGE {i+1} ===\n'+p for i,p in enumerate(pages)))
    out={'input':{'filename':PDF.name,'bytes':PDF.stat().st_size,'sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),'pages':len(pages)},
         'scope':'Independent reconstruction and counterexamples, not author-code provenance verification.'}
    out['quality_exact']={'slope':.0072,'ceiling_time':125/9,'q20_raw':1.044,'q20_smooth_alternative':1-.1*math.exp(-.072*20)}
    out['projection_clip_comparison']=[]
    for tg in [5.,20.,40.]:
        x=run(tg=tg,project=True);y=run(tg=tg,project=False)
        out['projection_clip_comparison'].append({'tau_g':tg,'dt':.05,'T':100,'all_arrays_exactly_equal':bool(np.array_equal(x,y))})
        assert np.array_equal(x,y)
    x=run(tg=20);y=run(tg=40)
    out['tau20_tau40_all_arrays_equal']=bool(np.array_equal(x,y));assert np.array_equal(x,y)
    out['quality_piecewise_linear_max_error']=[]
    for dt in [.1,.05,.025,.0125]:
        a=run(dt=dt,T=20)
        # Both exact and interpolated paths are affine between grid times and ceiling time.
        t=125/9;k=int(t/dt);w=t/dt-k
        interp=a[k,2]*(1-w)+a[k+1,2]*w
        out['quality_piecewise_linear_max_error'].append({'dt':dt,'error_at_exact_contact':1-interp})
    reference=run(dt=.003125)
    out['frozen_trajectory_refinement']=[]
    for dt in [.1,.05,.025,.0125]:
        a=run(dt=dt);b=reference[::round(dt/.003125)]
        errors=np.max(np.abs(a-b),axis=0)
        out['frozen_trajectory_refinement'].append({'dt':dt,'T':100,'reference_dt':.003125,'max_errors':dict(zip(['Af','Ac','q','P','D','Ar','B','E'],map(float,errors)))})
    out['recovery_reconstruction']=[]
    for dt in [.1,.05,.025]:
        a=run(dt=dt,T=400,Ac0=1.,P0=2.,Efixed=None,chi=.1)
        amin=float(a[:,1].min());end=float(a[-1,1])
        out['recovery_reconstruction'].append({'dt':dt,'minimum_Ac':amin,'final_Ac':end,'recovery_fraction':(end-amin)/(1-amin)})
    k=.06/.11;ceiling=.85*k*2.45+.0025
    out['debt_equilibrium_inputs']=[]
    for E in [1.158,1.238,ceiling+.02,ceiling+.1]:
        d=brentq(lambda D:.05*D+.85*math.exp(-.03*D)*k*2.45+.0025-E,0,E/.05)
        out['debt_equilibrium_inputs'].append({'E':E,'D_equilibrium':d})
    out['maintenance_balance_not_invariant']={'at_balance_R0':True,'uc':.1,'derivative_of_muAr_minus_etafAf':-.05*.1}
    out['net_B_sign_only_if_counterexample']={
        'Af':1.2,'Ac':.8,'Ar':.5,'q':1,'E':1.2,'bf':.85,'D_frozen':0,
        'uc':(1.2-.85*1.2-.05*.8)/.85,'maintenance_balance':.06*.5-.05*1.2,
        'conversion_term':(.85-.05)*(1.2-.85*1.2-.05*.8)/.85,
        'maintenance_term':.85*(.06*.5-.05*1.2),
        'net_B_derivative':(.85-.05)*(1.2-.85*1.2-.05*.8)/.85+.85*(.06*.5-.05*1.2)}
    assert out['net_B_sign_only_if_counterexample']['net_B_derivative']>0
    out['reserve_floor_not_invariant_counterexample']={'Af':.1,'Ac':2.3,'Ar':.1,'E':1.,'q':1.,'D':0.,'B':.85*.1+.05*2.3,'R':0.,'Ar_derivative':-.06*.1+.05*.1}
    assert out['reserve_floor_not_invariant_counterexample']['Ar_derivative']<0
    out['capital_floor_comparison']='For y=Ac-Amin>=0, yprime>=-y/tau_conv if R>=0; hence y(t)>=y(0) exp(-t/tau_conv).'
    text='\n'.join(pages)
    out['PDF_text_checks']={'raw_Hutchinson_word_present':'Hutchinson' in text,'printed_0_828_present':'0.828' in text,
                           'full_debt_derivative_written_explicitly':False,
                           'full_debt_derivative_note':'Manual check: no explicit corrected full-system debt Jacobian in the main PDF; revised SI/code needed.'}
    (ROOT/'c11_verification_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
