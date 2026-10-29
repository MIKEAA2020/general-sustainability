"""Offline NFA Edition 2026 + OWID pipeline, C18_A01. NFA derivatives: CC BY-SA 4.0.
Source attribution: ../repository_sources/ecomod_audit/DATA_LICENSE.md.
Run from any directory. Does not modify recovered originals.
"""
from pathlib import Path
import csv,json,math,hashlib
import numpy as np
import openpyxl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]
S=R/'repository_sources/ecomod_audit/reference'
D=R/'data'; F=R/'figures'
CATEGORIES=['crop','grazing','forest','fishing','built']
def savecsv(name,rows):
    with (D/(name+'_C18_A01.csv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def L(a,b):
    return a if a==b else (b-a)/(math.log(b)-math.log(a))
def main():
    D.mkdir(exist_ok=True);F.mkdir(exist_ok=True)
    w=openpyxl.load_workbook(S/'NEFBA_2026.xlsx',read_only=True,data_only=True)
    it=w['world_data'].iter_rows(values_only=True);h=next(it);raw=[dict(zip(h,r)) for r in it]
    # Keep the full source extraction, including flags; analysis explicitly joins 1961--2023.
    savecsv('nfa_world_source_extraction',raw)
    nfa={int(r['year']):r for r in raw};ys=list(range(1961,2024))
    if len(raw)!=len(nfa) or any(r['country_name']!='World'for r in raw):raise ValueError('Invalid or duplicate world-sheet records')
    ext=[]
    for name in ['cropland-area','cereal-yield']:
        with (S/(name+'.csv')).open() as f:
            reader=csv.DictReader(f);key=reader.fieldnames[3]
            rows=[r for r in reader if r['Entity']=='World' and r[key]]
        values={int(r['Year']):float(r[key]) for r in rows}
        if len(rows)!=len(values):raise ValueError('Duplicate world/year')
        ext.append(values)
    area,yield_=ext
    if not all(y in nfa and y in area and y in yield_ for y in ys):raise ValueError('Incomplete annual join')
    a=nfa[1961];B0=a['biocap_total_gha'];P0=1000*a['pop_1000_persons'];E0=a['efp_total_gha']
    phi=a['biocap_crop_gha']/B0;annual=[]
    for y in ys:
        z=nfa[y];B=z['biocap_total_gha'];P=z['pop_1000_persons']*1000;E=z['efp_total_gha']
        X=phi*B0*area[y]/area[1961]*yield_[y]/yield_[1961]
        annual.append(dict(year=y,source_flag=z['flag'],B_gha=B,Eprod_gha=E,P_persons=P,
            B_per_person=B/P,Eprod_per_person=E/P,Eprod_over_B=E/B,
            B_index=B/B0,BP_index=(B/P)/(B0/P0),EP_index=(E/P)/(E0/P0),
            logB=math.log(B/B0),logP=math.log(P/P0),logBP=math.log((B/P)/(B0/P0)),
            cropland_area_ha=area[y],cereal_yield_t_per_ha=yield_[y],X_proxy_gha=X,
            C_emp_gha=B-X,**{c+'_gha':z['biocap_'+c+'_gha'] for c in CATEGORIES},
            component_sum_residual_gha=sum(z['biocap_'+c+'_gha'] for c in CATEGORIES)-B))
    savecsv('empirical_annual_join',annual)
    components=[];endpoints=[];decompositions=[];calibration=[]
    for y in [2022,2023]:
        z=nfa[y];B=z['biocap_total_gha'];P=z['pop_1000_persons']*1000;E=z['efp_total_gha']
        endpoints.append(dict(year=y,B_gha=B,P_persons=P,B_change_pct=100*(B/B0-1),P_change_pct=100*(P/P0-1),
            BP_change_pct=100*((B/P)/(B0/P0)-1),EP_change_pct=100*((E/P)/(E0/P0)-1),
            logB=math.log(B/B0),logP=math.log(P/P0),logBP=math.log((B/P)/(B0/P0)),
            first_overshoot_year=min(r['year'] for r in annual if r['year']<=y and r['Eprod_over_B']>1)))
        for c in CATEGORIES:
            components.append(dict(year=y,component=c,ratio=z['biocap_'+c+'_gha']/a['biocap_'+c+'_gha'],
                contribution_pp=100*(z['biocap_'+c+'_gha']-a['biocap_'+c+'_gha'])/B0))
        for f in [.10,phi,.15,.19,.25,.30,.32,.34,.35]:
            X0=f*B0;X1=X0*area[y]/area[1961]*yield_[y]/yield_[1961];C0=B0-X0;C1=B-X1
            d=dict(year=y,phi0=f,X0=X0,XT=X1,C_emp0=C0,C_empT=C1,delta_X=X1-X0,delta_C_emp=C1-C0,delta_B=B-B0)
            if min(X0,X1,C0,C1)>0:
                wx=L(X0,X1)/L(B0,B);wc=L(C0,C1)/L(B0,B)
                dy=wx*math.log(yield_[y]/yield_[1961]);da=wx*math.log(area[y]/area[1961]);dc=wc*math.log(C1/C0)
                d.update(method='LMDI',wx=wx,wc=wc,yield_term=dy,area_term=da,residual_term=dc,sum_log=dy+da+dc,closure=dy+da+dc-math.log(B/B0))
            else:d.update(method='level_fallback',wx=None,wc=None,yield_term=None,area_term=None,residual_term=None,sum_log=None,closure=(X1-X0)+(C1-C0)-(B-B0))
            decompositions.append(d)
        crop=z['biocap_crop_gha']/a['biocap_crop_gha'];ar=z['area_crop_ha']/a['area_crop_ha']
        calibration.append(dict(year=y,nfa_crop_B_ratio=crop,nfa_crop_area_ratio=ar,nfa_crop_B_per_area_ratio=crop/ar,
            owid_area_ratio=area[y]/area[1961],owid_yield_ratio=yield_[y]/yield_[1961],
            phi_nonpositive_C_boundary=B/(B0*(area[y]/area[1961])*(yield_[y]/yield_[1961]))))
    for name,rows in [('empirical_endpoints',endpoints),('empirical_components',components),('empirical_LMDI_sensitivity',decompositions),('empirical_crop_calibration',calibration)]:savecsv(name,rows)
    plt.rcParams.update({'font.size':13,'axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(1,3,figsize=(10.5,4.3),layout='constrained')
    for key,label,color in [('B_index','B','#246588'),('BP_index','B / P','#b45438'),('EP_index','Eprod / P','#4f8058')]:
        ax[0].plot(ys,[r[key] for r in annual],label=label,color=color)
    ax[0].set(title='(a) Account indices',ylabel='1961 = 1',xlabel='Year');ax[0].legend(frameon=False)
    ax[1].plot(ys,[r['Eprod_over_B'] for r in annual],color='#635288');ax[1].axhline(1,color='gray',ls='--');ax[1].axvline(1973,color='gray',ls=':')
    ax[1].set(title='(b) Production footprint\nrelative to B',ylabel='Ratio',xlabel='Year')
    z=annual[-1];ax[2].bar(['Δ ln P','Δ ln(B/P)','Δ ln B'],[z['logP'],z['logBP'],z['logB']],color=['#246588','#b45438','#4f8058']);ax[2].axhline(0,color='gray',lw=.6);ax[2].set(title='(c) Exact log identity',ylabel='1961–2023 log change')
    for p in ax:p.grid(alpha=.15)
    for p in ax[:2]:p.set_xticks([1961,1990,2023])
    fig.savefig(F/'fig2_nfa_aggregation_face_C18_A01.pdf');fig.savefig(F/'fig2_nfa_aggregation_face_C18_A01.png',dpi=160);plt.close(fig)
    fig,ax=plt.subplots(1,2,figsize=(10,4.3),layout='constrained');rows=[r for r in components if r['year']==2023];labels=['Cropland','Grazing land','Forest biocapacity','Fishing grounds','Built-up land']
    for j,(key,title) in enumerate([('contribution_pp','(a) Contributions to Δ B'),('ratio','(b) Endpoint ratios')]):
        vals=[r[key] for r in rows];ax[j].barh(labels,vals,color=['#ad7b28','#92945a','#367052','#467c9e','#78728f']);ax[j].invert_yaxis();ax[j].axvline(0 if j==0 else 1,color='gray',ls='--');ax[j].set_title(title);ax[j].set_xlabel('Percentage points of B1961' if j==0 else '2023 / 1961');ax[j].grid(axis='x',alpha=.15)
    fig.savefig(F/'fig3_composition_attribution_C18_A01.pdf');fig.savefig(F/'fig3_composition_attribution_C18_A01.png',dpi=160);plt.close(fig)
    summary=dict(edition='NFA 2026 v1.0',years=ys,excluded_estimate_years=[2024,2025],phi0=phi,
        max_component_sum_residual_gha=max(abs(r['component_sum_residual_gha']) for r in annual),
        max_component_sum_relative=max(abs(r['component_sum_residual_gha'])/r['B_gha'] for r in annual),
        max_log_identity_error=max(abs(r['logB']-r['logP']-r['logBP']) for r in annual),
        max_LMDI_closure=max(abs(r['closure']) for r in decompositions if r['method']=='LMDI'),
        endpoints=endpoints,calibration=calibration,
        source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [S/'NEFBA_2026.xlsx',S/'cropland-area.csv',S/'cereal-yield.csv']},
        license='NFA inputs and NFA-derived numerical outputs: CC BY-SA 4.0, Lo et al. (2026); OWID/FAOSTAT attribution and provider terms retained.')
    (D/'empirical_summary_C18_A01.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
