"""Traceable within-stock institutional-event evidence, not a delay distribution.
Calendar intervals propagate source date precision; they are not confidence
intervals or fitted DDE delays. Related clocks from one episode are dependent.
No graph-digitized stock/catch quantities are used.
"""
from pathlib import Path
from datetime import date
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
S='https://www.vliz.be/imisdocs/publications/222472.pdf'
C='https://www.cefas.co.uk/data-and-publications/publications/list/publication-abstract/?id=12671'
EVENTS=[
 ['effort_advice_1965','early','1965-01-01','1965-12-31','advice','Overall effort reduction advised as improving future catches',S,'Table 1, journal p.688','year'],
 ['specific_TAC_advice_1970','early','1970-01-01','1970-12-31','advice','TAC implementation recommended; constitutional constraints delay it',S,'Table 1, journal p.688','year'],
 ['restrictive_TAC_1976','early','1976-01-01','1976-12-31','implementation','First restrictive TAC in force; prior nominal allocations not equivalent',S,'Table 1 continued, journal p.689','year'],
 ['directed_closure_1977','early','1977-01-01','1977-12-31','implementation','Directed fishery closed with limited bycatch allowances',S,'Table 1 continued, journal p.689','year'],
 ['broad_reopening_1983','early','1983-01-01','1983-12-31','reopening','General closure continues until 1983; not equated with partial earlier reopening',S,'Table 1 continued, journal p.689','year'],
 ['TAC_advice_1995_oct','late','1995-10-01','1995-10-31','advice','ACFM recommends severe TAC reduction for 1996',C,'Recent developments','month'],
 ['urgent_advice_1996_may','late','1996-05-01','1996-05-31','advice','New assessment prompts urgent additional reduction advice',C,'Recent developments','month'],
 ['emergency_implementation_1996','late','1996-05-01','1996-12-31','implementation','Emergency measures implemented during 1996 after May advice; exact effective day not supplied',C,'Recent developments','year with causal lower bound'],
]
PAIRS=[('effort_advice_1965','restrictive_TAC_1976','broad effort advice to first restrictive TAC'),('specific_TAC_advice_1970','restrictive_TAC_1976','specific TAC advice to first restrictive TAC'),('specific_TAC_advice_1970','directed_closure_1977','specific TAC advice to directed closure'),('TAC_advice_1995_oct','emergency_implementation_1996','initial TAC reduction advice to emergency implementation'),('urgent_advice_1996_may','emergency_implementation_1996','urgent additional advice to emergency implementation')]

def run():
    rows=[dict(zip(['event_id','episode','date_lo','date_hi','event_type','description','source_url','source_location','precision'],x))for x in EVENTS]
    by={r['event_id']:r for r in rows};pairs=[]
    for start,end,meaning in PAIRS:
        a,b=by[start],by[end];low=max(0,(date.fromisoformat(b['date_lo'])-date.fromisoformat(a['date_hi'])).days);high=(date.fromisoformat(b['date_hi'])-date.fromisoformat(a['date_lo'])).days
        lo,hi=low/365.25,high/365.25
        overlap=max(0,min(hi,7.8)-max(lo,2.6))
        pairs.append({'start_event':start,'end_event':end,'definition':meaning,'lag_lo_days':low,'lag_hi_days':high,'lag_lo_years':lo,'lag_hi_years':hi,'g2_model_window_overlap':overlap>0,'inference':'event-clock compatibility only; not identification of a constant DDE delay'})
    for name,rr in [('institutional_events_v42.csv',rows),('institutional_lag_intervals_v42.csv',pairs)]:
        with open(ROOT/'data'/name,'w',newline='')as f:w=csv.DictWriter(f,rr[0].keys());w.writeheader();w.writerows(rr)
    out={'stock':'North Sea autumn-spawning herring','selection':'Targeted within-stock comparison motivated by the small-pelagic hypothesis; not a random sample','events':len(rows),'derived_clocks':len(pairs),'distinct_episodes':2,'days_per_year':365.25,'date_bounds':'source precision plus explicit causal ordering; not confidence intervals','not_equated':['closure-to-reopening with deployment lag','nominal TAC agreement with restrictive implementation','spawning-stock biomass with the model total renewable stock','event lag with a fitted constant feedback delay'],'data_exclusion':'No values inferred from PDF figures or automatically reconstructed figure tables','dynamic_validation':'Not achieved: effective effort, latent memory and the stock observation operator remain unidentified','sources':[{'url':S,'doi':'10.1093/icesjms/fsm045','type':'peer-reviewed historical reconstruction drawing on listed ICES reports','checked_locations':'Table 1, pp.688-689'},{'url':C,'type':'Cefas agency account by J.H. Nichols, 1999','checked_locations':'Recent developments; 1995-1996 advice and implementation chronology'}],'pairs':pairs}
    (ROOT/'data/empirical_event_evidence_v42.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return out
if __name__=='__main__':run()
