#!/usr/bin/env python3
"""Validate internal methodology records before claim integration."""
from pathlib import Path
import csv, sys

ROOT=Path(__file__).parent
ALLOWED_EDGES={'deduced_from','defined_by','estimated_from','analogous_to','consistent_with','conjectured_from','normatively_selected_by','restricted_by','specializes','approximates','supersedes'}
REQUIRED=['claim_id','source','claim','epistemic_type','quantifiers_domain','systems_scales_horizons','verification_method','verification_status','integration_destination','revocation_trigger']
STRONG_TYPES={'theorem','conditional_theorem','numerical_proposition','statistical_claim','causal_claim','empirical_regularity'}

def read(name):
 with (ROOT/name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))

def main():
 errors=[]; warnings=[]
 claims=read('claim_ledger.csv'); ids=set()
 for n,r in enumerate(claims,2):
  cid=r.get('claim_id','')
  if not cid:errors.append(f'claim_ledger.csv:{n}: missing claim_id');continue
  if cid in ids:errors.append(f'claim_ledger.csv:{n}: duplicate {cid}')
  ids.add(cid)
  for field in REQUIRED:
   if not r.get(field,'').strip():errors.append(f'{cid}: missing required {field}')
  typ=r.get('epistemic_type','')
  if typ in STRONG_TYPES:
   for field in ['dependencies','derivation_evidence','countermodel_or_limit','falsifier_or_disproof_route','uncertainty_scope']:
    if not r.get(field,'').strip():warnings.append(f'{cid}: strong claim lacks {field}')
  if r.get('verification_status') in {'verified','completed'} and not r.get('derivation_evidence','').strip():
   errors.append(f'{cid}: marked verified without evidence')
 edges=read('inference_edges.csv');eids=set()
 for n,r in enumerate(edges,2):
  eid=r.get('edge_id','')
  if not eid:errors.append(f'inference_edges.csv:{n}: missing edge_id');continue
  if eid in eids:errors.append(f'inference_edges.csv:{n}: duplicate {eid}')
  eids.add(eid)
  if r.get('edge_type') not in ALLOWED_EDGES:errors.append(f'{eid}: invalid edge type {r.get("edge_type")}')
  for f in ['parent_claim','child_claim']:
   if r.get(f) not in ids:errors.append(f'{eid}: unknown {f} {r.get(f)}')
 # Status-upgrade guard on analogy/consistency is intentionally manual, but flag it.
 types={r['claim_id']:r.get('epistemic_type','') for r in claims if r.get('claim_id')}
 for r in edges:
  if r.get('edge_type') in {'analogous_to','consistent_with'} and types.get(r.get('child_claim')) in STRONG_TYPES:
   warnings.append(f"{r.get('edge_id')}: {r.get('edge_type')} points to strong-status child; verify independent evidence")
 print(f'claims={len(claims)} edges={len(edges)} errors={len(errors)} warnings={len(warnings)}')
 for x in errors:print('ERROR:',x)
 for x in warnings:print('WARNING:',x)
 return 1 if errors else 0

if __name__=='__main__':sys.exit(main())
