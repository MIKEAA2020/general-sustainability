"""Additional independent SI checks; not the author's code.
Uses the reference/data files from the adjacent ECOMOD audit package.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import csv,hashlib,json,math,re
import numpy as np
from scipy.optimize import brentq
import openpyxl

ROOT=Path(__file__).resolve().parent

def main():
    upload=Path('/home/user/uploads/ecomod_continued_10_SI.txt')
    ref=ROOT/'reference/ecomod_continued_10_SI.tex'
    source=upload if upload.exists() else ref
    text=source.read_text()
    out={'source':{'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'matches_previous_reference':source.read_bytes()==ref.read_bytes()}}
    # Exact immediate boundary and constraint checks.
    q0=F(9,10);rho=F(2,25);slope=rho*q0*(1-q0)
    out['quality']={'raw_slope':str(slope),'q_at_20':str(q0+20*slope),'first_ceiling_time':str((1-q0)/slope),'projected_tau20_tau40_paths_identical_under_constant_history':True}
    assert q0+20*slope>1
    out['reserve_initial_conditions']=[{'Ac0':float(a),'Af0':.6,'Ar0':float(F(5,2)-F(3,5)-a),'Ar0_below_claimed_0_80':F(5,2)-F(3,5)-a<F(4,5)} for a in [F(2,5),F(7,10),F(1),F(59,50)]]
    out['gate_summary_counterexample']={'announced_Ac0':.058,'reported_no_restoration_max_Ac':.057,'full_trajectory_max_must_be_at_least_initial':True,'first_step_if_dt_0_1_and_floor_limited':.058-.1*(.058-.05)}
    out['debt_bound_counterexample']={'D0':10,'shortfall_all_times':0,'time':1,'eta':.05,'actual_D':10*math.exp(-.05),'actual_debt_log_channel':-.03*10*math.exp(-.05),'SI_claimed_lower_bound':0}
    assert out['debt_bound_counterexample']['actual_debt_log_channel']<0
    # At the capital floor, fast-land equilibrium is an additional restriction.
    E,Af_boundary,Ac_boundary=1.158,.6,.05
    Af_equilibrium=.06/(.06+.05)*(2.5-Ac_boundary)
    out['boundary_debt_reduction']={
        'Af_actual':Af_boundary,'Af_equilibrium':Af_equilibrium,
        'Af_derivative_at_actual':.06*(2.5-Ac_boundary-Af_boundary)-.05*Af_boundary,
        'D_derivative_actual_at_D0':E-.85*Af_boundary-.05*Ac_boundary,
        'D_derivative_reduced_at_D0':E-.85*Af_equilibrium-.05*Ac_boundary}
    assert abs(out['boundary_debt_reduction']['D_derivative_actual_at_D0']-out['boundary_debt_reduction']['D_derivative_reduced_at_D0'])>.6
    # Independently check the debt-row derivative against finite differences.
    Af,Ac,q,P,D=.9,.8,.9,3.,.2
    bf=lambda d:.85*math.exp(-.03*d)
    U=.05+.8*.08*q*(1-q)
    debt=lambda d:.55*P-bf(d)*Af-U*Ac-.05*d
    eps=1e-5
    fd=(debt(D+eps)-debt(D-eps))/(2*eps)
    correct=.03*bf(D)*Af-.05
    out['debt_Jacobian']={'finite_difference':fd,'correct_analytic':correct,'printed_entry':-.05}
    assert abs(fd-correct)<1e-9
    # Reproduce the one-stock comparator's claimed characteristic roots.
    b,bG,rho,A,Amax,r=.5,.8,.05,.8,1.2,.02
    Gp=rho*(1-2*A/Amax);Bp=b+bG*Gp
    roots=[]
    for tg,tp in [(0.,0.),(30.,25.)]:
        def det(l):return (l-b/bG-Gp*math.exp(-l*tg))*(l+r)+r*Bp/bG*math.exp(-l*tp)
        root=brentq(det,.1,1.)
        roots.append({'tau_g':tg,'tau_p':tp,'characteristic_residual_at_zero':det(0),'positive_root':root})
        assert abs(det(0))<1e-14
    out['one_stock_characteristic_roots']=roots
    # Audit the complete anchor-sensitivity table and the 2022 proxy split.
    wb=openpyxl.load_workbook(ROOT/'reference/NEFBA_2026.xlsx',read_only=True,data_only=True)
    it=wb['world_data'].iter_rows(values_only=True);head=next(it);rows={v[1]:dict(zip(head,v)) for v in it}
    ss=[]
    for name in ['cropland-area','cereal-yield']:
        with (ROOT/'reference'/f'{name}.csv').open() as f:
            rd=csv.DictReader(f);key=rd.fieldnames[3]
            ss.append({int(v['Year']):float(v[key]) for v in rd if v['Entity']=='World' and v[key]})
    area,yield_=ss
    B0=rows[1961]['biocap_total_gha'];phi=rows[1961]['biocap_crop_gha']/B0
    L=lambda a,b:(b-a)/(math.log(b)-math.log(a)) if a!=b else a
    results=[]
    for year in [2022,2023]:
        B=rows[year]['biocap_total_gha'];gA=area[year]/area[1961];gY=yield_[year]/yield_[1961]
        for anchor in ([phi] if year==2022 else [.1,phi,.15,.19,.25,.30,.32,.34]):
            X0=anchor*B0;X=X0*gA*gY;C0=B0-X0;C=B-X
            wx=L(X0,X)/L(B0,B);wc=L(C0,C)/L(B0,B)
            terms=[wx*math.log(gY),wx*math.log(gA),wc*math.log(C/C0)]
            assert abs(sum(terms)-math.log(B/B0))<1e-12
            results.append({'year':year,'anchor':anchor,'wx':wx,'wc':wc,'yield':terms[0],'area':terms[1],'residual':terms[2],'sum':sum(terms)})
    out['proxy_sensitivity']=results
    out['residual_zero_anchor']={str(y):(rows[y]['biocap_total_gha']/B0)/((area[y]/area[1961])*(yield_[y]/yield_[1961])) for y in [2022,2023]}
    labels=re.findall(r'\\label\{([^}]+)\}',text);refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',text)
    bib=re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',text)
    cites=[k.strip() for x in re.findall(r'\\cite\w*(?:\[[^\]]*\]){0,2}\{([^}]+)\}',text) for k in x.split(',')]
    out['source_checks']={'missing_labels':sorted(set(refs)-set(labels)),'duplicate_labels':[k for k,v in Counter(labels).items() if v>1],'missing_cite_keys':sorted(set(cites)-set(bib)),'mentioned_drawdown_csv_present_in_package':(ROOT/'si_drawdown_depth.csv').exists()}
    (ROOT/'si_verification_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
