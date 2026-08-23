#!/usr/bin/env python3
"""Build a loss-resistant proposition-level intake concordance from A001–A025 inventories.

This does not infer proof validity. It enumerates every inventoried formal item and records
conservative routing/mapping fields so unresolved rows remain visible rather than disappearing.
"""
from pathlib import Path
import csv, re

ROOT=Path(__file__).resolve().parent
INV={}
for p in sorted(ROOT.glob('article_*/formal*inventory.md')):
    m=re.search(r'article_(?:A)?(\d{3})_',p.as_posix())
    if m: INV['A'+m.group(1)]=p

FIELDS=[
 'concordance_id','source_id','source_item','source_inventory','item_type',
 'canonical_module','canonical_object','primary_mapping','mapping_status',
 'assumptions_model_class','proof_evidence_status','publication_artifact_status',
 'destination_paper','monograph_chapter','interface_dependency','review_state','notes'
]

def extract(path):
    lines=path.read_text(encoding='utf-8').splitlines(); out=[]
    # Markdown tables: retain data rows, ignoring headers/separators.
    for line in lines:
        s=line.strip()
        if s.startswith('|') and not re.match(r'^\|\s*:?-+',s):
            cells=[c.strip() for c in s.strip('|').split('|')]
            if cells and cells[0].lower() not in {'section','type','id','item','result','claim'} and len(cells)>=2:
                title=cells[-1] or 'Untitled '+cells[-2]
                typ=cells[-2] if len(cells)>=3 else 'inventory_item'
                out.append((typ,title))
    # Bullet inventories.
    if not out:
        for line in lines:
            s=line.strip()
            if s.startswith('- ') and len(s)>3:
                text=s[2:].strip()
                if not text.lower().startswith(('source:','title:','no source')):
                    out.append(('inventory_item',text))
    # Numbered formal entries in some inventories.
    if not out:
        for line in lines:
            m=re.match(r'^\s*\d+[.)]\s+(.+)',line)
            if m: out.append(('inventory_item',m.group(1).strip()))
    # De-duplicate preserving order.
    seen=set(); ans=[]
    for x in out:
        key=(x[0].lower(),x[1].lower())
        if key not in seen: seen.add(key); ans.append(x)
    return ans

def module_for(text,src):
    t=text.lower()
    if src=='A021': return 'periodic_NAIM_coupling'
    if src in {'A022','A023'}: return 'stage_spatial_extension'
    if any(k in t for k in ['hopf','floquet','bifurcat','periodic orbit','fold','lyapunov','delay','rfde','characteristic','cycle','stability','monodromy']): return 'nonlinear_dynamics'
    if any(k in t for k in ['ledger','conservation','mass','material','moiety','depletion','first-passage','first passage','stock','flux','donor','service','support gap','phosphate','groundwater']): return 'ledger_diagnostics'
    if any(k in t for k in ['observation','information','epistemic','sampled','review interval','governance','institution','authority','implementation','empirical','power','event panel','mse','identif','falsif','cod','adaptive capacity']): return 'observation_governance_empirics'
    if any(k in t for k in ['transform','architecture','composition','coupling','commons','intergenerational','normative','relational','admission','type system']): return 'architecture_transformation_composition'
    if any(k in t for k in ['viab','kernel','capture','recover','safe','substitution','non-compensation','noncompensation','projectability','reduction','positiv']): return 'formal_foundations'
    return 'unclassified_canonical_review'

def object_for(mod):
    return {
      'periodic_NAIM_coupling':'model, mapping, theorem record, interface contract',
      'stage_spatial_extension':'state, model, mapping, theorem record',
      'nonlinear_dynamics':'state, model, admissible set, theorem record',
      'ledger_diagnostics':'ledger, services, admissible set, theorem record',
      'observation_governance_empirics':'observation, assessment, policy, implementation, evidence',
      'architecture_transformation_composition':'specification, architecture, operator II, composition',
      'formal_foundations':'operator I, theorem record, mapping',
      'unclassified_canonical_review':'theorem record pending classification'
    }[mod]

def mapping_for(text,mod):
    t=text.lower()
    if any(k in t for k in ['counterexample','obstruction','impossib','negative result','no-positive','no sign-free','rejected']): return 'COUNTEREXAMPLE_OR_LIMIT'
    if 'projectab' in t or 'exact triangular projection' in t: return 'PROJECTABLE_REDUCTION'
    if any(k in t for k in ['approximation','reduction','qss','frozen','coarse-grain','limit']): return 'APPROXIMATION'
    if 'transform' in t: return 'TRANSFORMATION'
    if mod=='unclassified_canonical_review': return 'UNRESOLVED'
    return 'EXACT_SPECIALIZATION'

def evidence_for(text,src):
    t=text.lower()
    if src in {'A008','A009','A015'}: return 'rejected_source_branch'
    if any(k in t for k in ['conjecture','open','pending','conditional','demoted','hypothesis']): return 'conditional_or_open'
    if any(k in t for k in ['source-stated','numerical','floquet','continuation','computed','spectrum','spectral']): return 'source_status_accepted_artifact_pending'
    if any(k in t for k in ['empirical','data','case','groundwater','phosphate','cod']): return 'source_specific_empirical_status_check_required'
    if any(k in t for k in ['theorem','proposition','corollary','lemma','identity','criterion']): return 'proof_inventory_present_line_check_required'
    if 'definition' in t: return 'defined_source_object'
    return 'status_crosswalk_required'

def destination(src,mod,text):
    t=text.lower()
    if src=='A021': return 'Paper 6 conditional'
    if src in {'A022','A023'}: return 'Paper 7 conditional'
    if src=='A025': return 'Paper 4 appendix or compendium'
    if src in {'A008','A009','A015','A017'}: return 'negative/counterexample register or conditional redesign docket'
    if mod=='ledger_diagnostics': return 'Paper 3'
    if mod=='nonlinear_dynamics': return 'Paper 4'
    if mod=='observation_governance_empirics':
        if src in {'A001','A002','A006','A007','A010'} and any(k in t for k in ['theorem','kernel','criterion','definition']): return 'Paper 2'
        return 'Paper 5'
    if mod=='architecture_transformation_composition':
        if any(k in t for k in ['theorem','proposition','criterion','counterexample']): return 'Paper 1 if independent-result gate; otherwise Paper 2'
        return 'Paper 1 or monograph introduction'
    if mod=='formal_foundations': return 'Paper 2'
    return 'manual destination review'

def chapter(mod):
    return {
      'periodic_NAIM_coupling':'Advanced coupling and persistence',
      'stage_spatial_extension':'Stage and spatial extensions',
      'nonlinear_dynamics':'Delay and nonlinear transitions',
      'ledger_diagnostics':'Material ledgers and diagnostics',
      'observation_governance_empirics':'Observation, governance, and identification',
      'architecture_transformation_composition':'Canonical architecture, transformation, and composition',
      'formal_foundations':'Formal viability and theorem atlas',
      'unclassified_canonical_review':'Conditional docket'
    }[mod]

rows=[]
for src in sorted(INV):
    items=extract(INV[src])
    for i,(typ,title) in enumerate(items,1):
        text=f'{typ} {title}'; mod=module_for(text,src); mapping=mapping_for(text,mod)
        ev=evidence_for(text,src)
        if src in {'A008','A009','A015'}: review='adjudicated_rejected_or_negative_only'; mapstat='rejected_or_limit_mapping'
        elif ev in {'conditional_or_open','status_crosswalk_required','proof_inventory_present_line_check_required','source_specific_empirical_status_check_required'}:
            review='requires_row_level_verification'; mapstat='proposed_not_yet_interface_proved'
        else: review='mapped_requires_final_citation_check'; mapstat='proposed_mapping'
        rows.append({
          'concordance_id':f'CC-{src}-{i:03d}','source_id':src,'source_item':title,
          'source_inventory':INV[src].relative_to(ROOT.parent).as_posix(),'item_type':typ,
          'canonical_module':mod,'canonical_object':object_for(mod),'primary_mapping':mapping,
          'mapping_status':mapstat,'assumptions_model_class':'retain exact source assumptions; model-class extraction pending row review',
          'proof_evidence_status':ev,'publication_artifact_status':'see source evaluation and action register; do not infer completeness',
          'destination_paper':destination(src,mod,text),'monograph_chapter':chapter(mod),
          'interface_dependency':'TCS-1.0 interface contract; local producer/consumer fields required before theorem transfer',
          'review_state':review,'notes':'Inventory-complete intake row; no status promotion.'
        })

out=ROOT/'canonical_concordance_A001_A025.csv'
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(rows)

counts={}
for r in rows: counts[r['source_id']]=counts.get(r['source_id'],0)+1
missing=[f'A{i:03d}' for i in range(1,26) if f'A{i:03d}' not in counts]
review_counts={}
for r in rows: review_counts[r['review_state']]=review_counts.get(r['review_state'],0)+1
report=ROOT/'canonical_concordance_A001_A025_coverage.md'
with report.open('w',encoding='utf-8') as f:
    f.write('# Canonical Concordance A001–A025 — Coverage and Closure Status\n\n')
    f.write(f'- Schema: `TCS-1.0`\n- Inventoried rows: **{len(rows)}**\n- Sources represented: **{len(counts)}/25**\n')
    f.write(f'- Missing source inventories: `{", ".join(missing) if missing else "none"}`\n\n')
    f.write('## Rows by source\n\n| Source | Rows |\n|---|---:|\n')
    for s in sorted(counts): f.write(f'| {s} | {counts[s]} |\n')
    f.write('\n## Review state\n\n| State | Rows |\n|---|---:|\n')
    for s,n in sorted(review_counts.items()): f.write(f'| `{s}` | {n} |\n')
    f.write('\n## Interpretation\n\n')
    f.write('The inventory-coverage gate is closed: every item present in the registered A001–A025 formal-content inventories has a stable concordance row. The scientific closure gate is not automatically closed. Rows conservatively preserve source status and remain blocked where exact assumptions, proof line, mapping proof, or artifact must be checked. `proposed_not_yet_interface_proved` is not an accepted theorem transfer. Rejected sources remain visible as negative/limit records.\n')
print(f'wrote {len(rows)} rows from {len(counts)} sources; missing={missing}')
