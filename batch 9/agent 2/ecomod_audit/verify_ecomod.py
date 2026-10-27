"""Independent equation/data audit of ecomod_continued_10.
Dependencies: numpy, scipy, openpyxl. Not the author's simulation code.
Euler paths implement the disclosed *clipped* quality law, not the raw DDE.
"""
from pathlib import Path
import csv, hashlib, json, math, re
import numpy as np
from scipy.optimize import brentq
from scipy.special import lambertw
import openpyxl

ROOT=Path(__file__).resolve().parent

def simulate(dt=.05,T=250,Af0=.6,Ac0=1.5,P0=1.5,fixed_E=.825,chi=0.,wave=False):
    n=round(T/dt);lg=round(20/dt);lp=round(25/dt)
    q=np.empty(n+1);Bh=np.empty(n+1)
    q[0]=.9;Af=Af0;Ac=Ac0;P=P0;D=0.
    B0=.85*Af+(.05+.8*.08*.9*.1)*Ac
    minAc=Ac;peakD=0.;peakDt=0.;postpeak=0.;minAr=2.5-Af-Ac
    snapshots={};lastmask=0.
    prevB=B0
    for i in range(n+1):
        t=i*dt;Tb=1/(1+math.exp(-.1*(t-40))) if wave else 0.
        bf=(.85+Tb)*math.exp(-.03*D)
        U=.05+.8*.08*q[i]*(1-q[i]);B=bf*Af+U*Ac;Bh[i]=B
        E=fixed_E if fixed_E is not None else .55*P
        Ar=2.5-Af-Ac;minAr=min(minAr,Ar)
        if i and B>prevB and Ac<prevAc:lastmask=t
        if D>peakD:peakD=D;peakDt=t
        if t>=40:postpeak=max(postpeak,D)
        for target in [4,25,50,149,250,400]:
            if abs(t-target)<dt/4:snapshots[str(target)]={'B':B,'Ac':Ac,'Af':Af,'P':P,'D':D,'q':q[i]}
        if i==n:break
        S=max(E-B,0.);uc=min(S/bf,max(Ac-.05,0.));R=chi*Ar*max(B-E,0.)
        qpast=q[i-lg] if i>=lg else .9
        Bpast=Bh[i-lp] if i>=lp else B0
        dq=.08*qpast*(1-qpast)
        dP=.02*P*(1-P/max(Bpast/.55,.02))
        prevB=B;prevAc=Ac
        Af=max(0.,Af+dt*(uc+.06*Ar-.05*Af))
        Ac=max(.05,Ac+dt*(-uc+R))
        D=max(0.,D+dt*(S-.05*D))
        P=max(0.,P+dt*dP) if fixed_E is None else P
        q[i+1]=min(1.,max(0.,q[i]+dt*dq))
        minAc=min(minAc,Ac)
    return {'dt':dt,'T':T,'final':{'Af':Af,'Ac':Ac,'Ar':2.5-Af-Ac,'B':B,'q':q[-1],'D':D,'P':P},'minAc':minAc,'minAr':minAr,'peakD':peakD,'peakDt':peakDt,'post40_peakD':postpeak,'last_strict_floating_mask_time':lastmask,'snapshots':snapshots}


def main():
    out={}
    k=.06/.11
    out['reduced']={'k':k,'Eceil':.85*k*2.45+.05*.05,'balance_Ac_at_E_0_825':(.85*k*2.5-.825)/(.85*k-.05)}
    out['yield_sweep']=[]
    for b in [.6,.85,1.2,2.]:
        J=np.array([[-1.11,-.06-.05/b],[1.,.05/b]])
        out['yield_sweep'].append({'bf':b,'J':J.tolist(),'eigenvalues':np.linalg.eigvals(J).tolist(),'Eceil':b*k*2.45+.0025})
    out['quality']={'raw_first_interval_slope':.08*.9*.1,'raw_q_at_t20':.9+20*.08*.9*.1,'first_ceiling_crossing':.1/(.08*.9*.1),'critical_delay':math.pi/(2*.08),'baseline_rho_tau':1.6,'dominant_raw_linear_root_tau20':[float(lambertw(-1.6).real/20),float(lambertw(-1.6).imag/20)]}
    # Two distinct fixed-demand no-conversion equilibria at the same demand.
    out['surplus_equilibrium_counterexample']={'E':.825,'Ac':.5,'Af':k*2.,'Ar':(1-k)*2.,'B':.85*k*2.+.05*.5,'land_eigenvalues_surplus':[-.11,0.]}
    out['debt_roots']=[]
    for E in [1.158,1.238,out['reduced']['Eceil']+.02,out['reduced']['Eceil']+.10]:
        D=brentq(lambda D:.05*D+.85*math.exp(-.03*D)*k*2.45+.0025-E,0,E/.05)
        out['debt_roots'].append({'E':E,'D':D})
    out['frozen_runs']=[simulate(dt=d,T=250) for d in [.1,.05,.025]]
    out['recovery_runs']=[dict(chi=c,**simulate(dt=.05,T=400,Ac0=1.,P0=2.,fixed_E=None,chi=c)) for c in [0.,.10]]
    out['wave_runs']=[dict(P0=p,wave=w,**simulate(dt=.05,T=250,Ac0=.9,P0=p,fixed_E=None,chi=.1,wave=w)) for p in [1.,1.2] for w in [False,True]]
    wb=openpyxl.load_workbook(ROOT/'reference/NEFBA_2026.xlsx',read_only=True,data_only=True)
    it=wb['world_data'].iter_rows(values_only=True);header=next(it);rows=[dict(zip(header,r)) for r in it]
    byyear={r['year']:r for r in rows};a=byyear[1961];B0=a['biocap_total_gha'];p0=a['pop_1000_persons']*1000
    out['nfa']={}
    for year in [2022,2023]:
        b=byyear[year];B=b['biocap_total_gha'];p=b['pop_1000_persons']*1000
        components={}
        for c in ['crop','grazing','forest','fishing','built']:
            key='biocap_'+c+'_gha';components[c]={'ratio':b[key]/a[key],'pp':100*(b[key]-a[key])/B0}
        out['nfa'][str(year)]={'B':B,'P':p,'B_per_person':B/p,'Efp_per_person':b['efp_total_gha']/p,'B_change_pct':100*(B/B0-1),'BP_change_pct':100*((B/p)/(B0/p0)-1),'EfpP_change_pct':100*((b['efp_total_gha']/p)/(a['efp_total_gha']/p0)-1),'delta_log_B':math.log(B/B0),'delta_log_P':math.log(p/p0),'delta_log_BP':math.log((B/p)/(B0/p0)),'components':components,'component_sum_error':sum(b['biocap_'+c+'_gha'] for c in ['crop','grazing','forest','fishing','built'])-B}
    out['nfa']['first_overshoot']=min(r['year'] for r in rows if r['year']<=2023 and r['efp_total_gha']>r['biocap_total_gha'])
    out['nfa']['flags_last_three']={str(y):byyear[y]['flag'] for y in [2023,2024,2025]}
    with (ROOT/'world_data_extracted.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=header);wr.writeheader();wr.writerows(rows)
    out['sources']={'workbook_url':'https://footprint.info.yorku.ca/files/2026/04/NEFBA_Data_global_national_ecological_footprint_biocapacity.xlsx','workbook_sha256':hashlib.sha256((ROOT/'reference/NEFBA_2026.xlsx').read_bytes()).hexdigest(),'workbook_license':'CC BY-SA 4.0; extracted CSV retains attribution/license per README.'}
    # Recompute the proxy LMDI split using the downloaded OWID CSVs.
    series=[]
    for name in ['cropland-area','cereal-yield']:
        with (ROOT/'reference'/f'{name}.csv').open() as f:
            reader=csv.DictReader(f); key=reader.fieldnames[3]
            series.append({int(x['Year']):float(x[key]) for x in reader if x['Entity']=='World' and x[key]})
    area,yield_=series
    X0=a['biocap_crop_gha']; B1=byyear[2023]['biocap_total_gha']
    X1=X0*(area[2023]/area[1961])*(yield_[2023]/yield_[1961]); C0=B0-X0; C1=B1-X1
    def L(a,b): return (b-a)/(math.log(b)-math.log(a)) if a!=b else a
    wx=L(X0,X1)/L(B0,B1); wc=L(C0,C1)/L(B0,B1)
    out['proxy_LMDI']={'yield':wx*math.log(yield_[2023]/yield_[1961]),'area':wx*math.log(area[2023]/area[1961]),'residual':wc*math.log(C1/C0),'X0':X0,'X1':X1,'C0':C0,'C1':C1}
    uploaded=Path('/home/user/uploads/ecomod_continued_10.txt')
    source=uploaded if uploaded.exists() else ROOT/'reference/ecomod_continued_10.tex'
    main=source.read_text()
    labs=re.findall(r'\\label\{([^}]+)\}',main);refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',main)
    bibs=re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',main)
    cites=[k.strip() for x in re.findall(r'\\cite\w*(?:\[[^\]]*\]){0,2}\{([^}]+)\}',main) for k in x.split(',')]
    out['source_checks']={'missing_labels':sorted(set(refs)-set(labs)),'missing_cite_keys':sorted(set(cites)-set(bibs)),'main_identical_to_pinned_reference':source.read_bytes()==(ROOT/'reference/ecomod_continued_10.tex').read_bytes(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
    (ROOT/'verification_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
