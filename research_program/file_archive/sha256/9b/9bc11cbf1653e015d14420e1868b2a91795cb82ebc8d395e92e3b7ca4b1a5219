#!/usr/bin/env python3
from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'A001_A002_theorem_interface_map.csv'
FIELDS=['map_id','source_id','source_section','source_label','opening_or_title','theorem_family','canonical_interface','adjudicated_status','verification_dependencies','destination','paper2_role','publication_ready','notes']

def tables(path):
    out=[]
    for line in path.read_text(encoding='utf-8').splitlines():
        s=line.strip()
        if not s.startswith('|') or re.match(r'^\|\s*:?-+',s): continue
        c=[x.strip() for x in s.strip('|').split('|')]
        if len(c)<3 or c[0].lower()=='section': continue
        out.append(c[:3])
    return out

def family(src,section,label,title):
    t=' '.join([section,label,title]).lower()
    if src=='A001':
        m=re.match(r'\s*(\d+)',section)
        n=int(m.group(1)) if m else -1
        if 'conjecture' in label.lower() or 'open problem' in label.lower() or n==18: return 'F14 conditional research docket'
        if n==2: return 'F13 core viability and obstruction calculus'
        if n==3: return 'F04 recovery and irreversibility'
        if n==4: return 'F07 diagnostics and delay certificates' if 'delay margin' in label.lower() else 'F03 observation and epistemic viability'
        if n==5: return 'F13 core viability and obstruction calculus'
        if n==6: return 'F08 scalar resource and sink kernels'
        if n==7: return 'F09 resource-capital, distribution, and exhaustibility'
        if n==8: return 'F02 noncompensation and substitution feasibility'
        if n==9: return 'F09 resource-capital, distribution, and exhaustibility'
        if n in {10,11,16}: return 'F10 coupling, networks, and restricted composition'
        if n in {12,13}: return 'F11 commons and institutional implementation'
        if n in {14,17}: return 'F12 intergenerational and stochastic results'
        if n==15: return 'F07 diagnostics and delay certificates'
        return 'F15 manual family review'
    if 'canonical sustainability system' in t: return 'F00 canonical definitions and types'
    if 'typed conservation' in t: return 'F01 typed conservation, positivity, boundedness'
    if 'substitution as pathway' in t: return 'F02 noncompensation and substitution feasibility'
    if 'observation limits' in t: return 'F03 observation and epistemic viability'
    if 'sustainability as robust viability' in t:
        if 'capture basin' in title.lower(): return 'F04 recovery and irreversibility'
        return 'F05 sampled, hybrid, and information kernels'
    if 'sampled-to-continuous' in t: return 'F05 sampled, hybrid, and information kernels'
    if 'reduction' in section.lower() or 'coarse-graining' in section.lower() or 'projectability' in section.lower(): return 'F06 projectability and reduction'
    if 'diagnostic' in section.lower() or 'stability' in section.lower(): return 'F07 diagnostics and delay certificates'
    if any(k in section.lower() for k in ['conjecture','empirical hypotheses','research programmes']): return 'F14 conditional research docket'
    return 'F15 manual family review'

def deps(src,section,label,title,fam):
    t=' '.join([section,label,title]).lower(); d=[]
    if src=='A001':
        pairs=[
          (['robust invariance','tangency'],'V-A001-02'),(['order-minimal','minimum control'],'V-A001-03'),
          (['pollution'],'V-A001-04'),(['consumption'],'V-A001-05'),(['non-polyhedral'],'V-A001-06'),
          (['rosen','unique nash'],'V-A001-07'),(['safe capacity','uniform negative drift'],'V-A001-08'),
          (['quota rescue','quota aggregate'],'V-A001-09'),(['best response','dominance'],'V-A001-10'),
          (['ostrom'],'V-A001-11'),(['lattice structure','implementation lattice'],'V-A001-12')]
        for keys,aid in pairs:
            if any(k in t for k in keys): d.append(aid)
        d+=['V-A001-13','V-A001-14']
    else:
        d+=['V-A002-01','V-A002-03','V-A002-18']
        byfam={
          'F01':['V-A002-02','V-A002-04'], 'F02':['V-A002-05'],
          'F03':['V-A002-06','V-A002-07','V-A002-08','V-A002-11','V-A002-12'],
          'F05':['V-A002-09','V-A002-10','V-A002-11','V-A002-12','V-A002-13'],
          'F06':['V-A002-14','V-A002-15','V-A002-16'], 'F07':['V-A002-17']}
        key=fam.split()[0]
        d+=byfam.get(key,[])
    return ';'.join(dict.fromkeys(d))

def status(src,label,title):
    t=(label+' '+title).lower()
    if 'conjecture' in t or 'open problem' in t or 'research programme' in t or 'empirical hypothesis' in t: return 'retain_conditional_or_prospective'
    if 'counterexample' in t or 'obstruction' in t or 'does not' in t: return 'retain_limit_or_counterexample_pending_line_check'
    if 'definition' in t: return 'definition_retained_subject_to_notation_and_scope_audit'
    if src=='A001': return 'corrected_source_family_pending_numbering_citation_and_line_check'
    return 'restricted_source_result_pending_targeted_verification'

def destination(fam,src,label,title):
    f=fam.split()[0]; t=(label+' '+title).lower()
    if f=='F01' and any(k in t for k in ['conservation','non-negative','nonnegative','moiety','donor']): return 'Paper 2 canonical theorem; Paper 3 may restate ledger-specific instance'
    if f in {'F00','F03','F04','F05','F06','F07','F08','F09','F10','F11','F12','F13'}: return 'Paper 2 unless application-specific row is delegated'
    if f=='F02': return 'Paper 2 canonical alternative; Paper 3 owns accounting/application instance'
    if f=='F14': return 'conditional docket or monograph; not Paper 2 main theorem corpus'
    return 'manual destination review'
rows=[]
for src,path in [('A001',ROOT/'article_001_topdown/formal_result_inventory.md'),('A002',ROOT/'article_002_general_theory/formal_result_inventory.md')]:
    for i,(section,label,title) in enumerate(tables(path),1):
        fam=family(src,section,label,title); stat=status(src,label,title)
        rows.append({'map_id':f'TM-{src}-{i:03d}','source_id':src,'source_section':section,'source_label':label,'opening_or_title':title,
          'theorem_family':fam,'canonical_interface':'TCS-1.0 theorem record + Operator I/II/composition interface as applicable',
          'adjudicated_status':stat,'verification_dependencies':deps(src,section,label,title,fam),
          'destination':destination(fam,src,label,title),'paper2_role':'main' if fam.split()[0] not in {'F14','F15'} else 'conditional_or_excluded',
          'publication_ready':'no','notes':'No status promotion; exact source statement/proof and listed corrections control.'})
with OUT.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
counts={}
for r in rows: counts[r['theorem_family']]=counts.get(r['theorem_family'],0)+1
with (ROOT/'A001_A002_theorem_interface_map_summary.md').open('w',encoding='utf-8') as f:
    f.write('# A001/A002 Theorem-Interface Map — Batch 2A\n\n')
    f.write(f'- Rows adjudicated: **{len(rows)}**\n- A001: **{sum(r["source_id"]=="A001" for r in rows)}**\n- A002: **{sum(r["source_id"]=="A002" for r in rows)}**\n- Publication-ready rows: **0** (numbering/citation/targeted line gates intentionally retained)\n\n')
    f.write('## Family counts\n\n| Family | Rows |\n|---|---:|\n')
    for k,v in sorted(counts.items()): f.write(f'| {k} | {v} |\n')
    f.write('\n## Decision\n\nEvery A001/A002 inventoried formal item now has a theorem family, canonical interface, correction/verification dependency, and publication destination. This closes row classification, not proof publication readiness. Conditional programmes are excluded from the main Paper 2 theorem corpus; application-specific instances may be delegated after line review.\n')
print(len(rows),counts)
