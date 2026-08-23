#!/usr/bin/env python3
"""List and update research-program actions.

Examples:
  python research_program/manage_actions.py list --source A001 --status open
  python research_program/manage_actions.py list --type verification --priority critical
  python research_program/manage_actions.py show V-A001-07
  python research_program/manage_actions.py set V-A001-07 active --evidence "Review started"
  python research_program/manage_actions.py set V-A001-07 completed --evidence "Corrected theorem in <file>"
"""
from pathlib import Path
import argparse, csv, sys

REGISTRY = Path(__file__).with_name('action_register.csv')
FIELDS = ['action_id','source','action_type','title','target','priority','status','dependencies','completion_evidence','notes']

def load():
    with REGISTRY.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def save(rows):
    with REGISTRY.open('w', encoding='utf-8', newline='') as f:
        w=csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)

def matches(r,args):
    return all([
        not args.source or r['source']==args.source,
        not args.type or r['action_type']==args.type,
        not args.status or r['status']==args.status,
        not args.priority or r['priority']==args.priority,
    ])

def print_row(r, verbose=False):
    print(f"{r['action_id']:12} {r['status']:10} {r['priority']:8} {r['action_type']:20} {r['title']}")
    if verbose:
        print(f"  target: {r['target']}")
        if r['dependencies']: print(f"  dependencies: {r['dependencies']}")
        if r['completion_evidence']: print(f"  evidence: {r['completion_evidence']}")
        if r['notes']: print(f"  notes: {r['notes']}")

def main():
    ap=argparse.ArgumentParser()
    sub=ap.add_subparsers(dest='cmd',required=True)
    lp=sub.add_parser('list')
    for name in ['source','type','status','priority']: lp.add_argument('--'+name)
    lp.add_argument('-v','--verbose',action='store_true')
    sp=sub.add_parser('show'); sp.add_argument('action_id')
    up=sub.add_parser('set'); up.add_argument('action_id'); up.add_argument('status',choices=['open','blocked','active','completed','superseded']); up.add_argument('--evidence',default='')
    args=ap.parse_args(); rows=load()
    if args.cmd=='list':
        selected=[r for r in rows if matches(r,args)]
        for r in selected: print_row(r,args.verbose)
        print(f"\n{len(selected)} action(s)")
    elif args.cmd=='show':
        hit=[r for r in rows if r['action_id']==args.action_id]
        if not hit: sys.exit(f"Unknown action: {args.action_id}")
        print_row(hit[0],True)
    else:
        hit=False
        for r in rows:
            if r['action_id']==args.action_id:
                r['status']=args.status
                if args.evidence:r['completion_evidence']=args.evidence
                hit=True
        if not hit: sys.exit(f"Unknown action: {args.action_id}")
        save(rows); print(f"Updated {args.action_id} -> {args.status}")
if __name__=='__main__': main()
