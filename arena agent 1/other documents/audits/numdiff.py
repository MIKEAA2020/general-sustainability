#!/usr/bin/env python3
"""Numeric-fidelity diff v2: significant-value multiset comparison.
Signals: numbers missing from the rewrite (potential drops) and numbers present
only in the rewrite (potential introduced values). Reference lists are excluded
(bibliographic page numbers are formatting, not content)."""
import re, sys, collections

def clean(text, strip_years=True):
    t = text
    t = t.replace('\\,', '').replace('\\.', '.').replace('{', '').replace('}', '')
    # cut references
    m = re.search(r'\n#+ *References', t)
    if m: t = t[:m.start()]
    t = re.sub(r'\[?CC-[A-Z0-9]+\s*[-–]\s*\d+\]?', ' ', t)          # CC tags
    t = re.sub(r'\d{4}-\d{2}-\d{2}', ' ', t)                          # ISO dates
    t = re.sub(r'https?://\S+', ' ', t)                               # URLs
    t = re.sub(r'\b(Theorem|Thm|Corollary|Cor|Proposition|Prop|Definition|Def|Lemma|Remark|Section|Sec|Fig|Figure|Table|Layer|Rule)\s*\.?\s*\d+(?:\.\d+)*(?:\([a-z0-9]+\))?', ' ', t)
    t = re.sub(r'§\s*\d+(?:\.\d+)*', ' ', t)
    # article/programme IDs: A001, R04, H8, E5, M2, G3, B5 ...
    t = re.sub(r'\b(?:[A-Z]+\d{2,3}|[A-Z]\d)\b', ' ', t)
    # subscripts/superscripts (digits only)
    t = re.sub(r'[_^]\{?[a-zA-Z]+\}?', ' ', t)
    if strip_years:
        t = re.sub(r'\b(?:19|20)\d{2}\b', ' ', t)
    return t

NUM = re.compile(r'\d[\d,]*(?:\.\d+)?(?:[eE×][-−]?\d+)?')
def significant(s):
    return '.' in s or len(re.sub(r'[^0-9]', '', s)) >= 4

def nums(text, strip_years=True):
    t = clean(text, strip_years)
    out = collections.Counter()
    for m in NUM.finditer(t):
        s = m.group(0).replace(',', '').replace('−','-').replace('×','e')
        if s in ('', '.'): continue
        try:
            'e' in s and float(s)
            _ = float(s) if 'e' not in s else float(s)
        except ValueError:
            continue
        if significant(s):
            out[s] += 1
    return out

def compare(name, src_path, dst_paths, strip_years=True):
    sn = nums(open(src_path).read(), strip_years)
    dn = collections.Counter()
    for p in dst_paths:
        dn += nums(open(p).read(), strip_years)
    missing = sn - dn
    extra   = dn - sn
    print(f"═══ {name}")
    print(f"    source sig-numbers: {sum(sn.values())}  rewrite sig-numbers: {sum(dn.values())}")
    if missing:
        print(f"    IN SOURCE NOT IN REWRITE ({sum(missing.values())}):")
        for k, v in sorted(missing.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"      {k} ×{v}")
    if extra:
        print(f"    IN REWRITE NOT IN SOURCE ({sum(extra.values())}):")
        for k, v in sorted(extra.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"      {k} ×{v}")
    if not missing and not extra:
        print("    significant-number multiset identical")
    print()

if __name__ == '__main__':
    pairs = [
        ("P1", "papers/paper1_general_theory/manuscript_v3.md", ["paper1_assessment_separation.md","paper1_supplementary.md"], True),
        ("P2", "papers/paper2_theorem_atlas/manuscript_v2.md", ["paper2_obstruction_calculus.md"], True),
        ("P3-main", "papers/paper3_material_ledgers/manuscript_v2.md", ["paper3_material_ledgers.md","paper3_supplementary.md"], True),
        ("P3-recon", "papers/paper3_material_ledgers/manuscript_v2.md", ["paper3_material_ledgers_reconstructed.md","paper3_supplementary.md"], True),
        ("P3-reconV2", "papers/paper3_material_ledgers/manuscript_v2.md", ["paper3_material_ledgers_reconstructed_v2.md","paper3_supplementary.md"], True),
        ("P3-V2", "papers/paper3_material_ledgers/manuscript_v2.md", ["paper3_material_ledgers_v2.md","paper3_supplementary.md"], True),
        ("P4", "papers/paper4_delay_dynamics/manuscript_v2.md", ["paper4_delay_dynamics.md","paper4_supplementary.md"], True),
        ("P5", "papers/paper5_sampled_governance/manuscript_v2.md", ["paper5_sampled_governance.md","paper5_supplementary.md"], True),
        ("E1", "wave_e_cod/manuscript/wave_E_cod_forecast_ladder_v2.md", ["paperE1_cod_forecast_ladder.md"], True),
        ("E2", "wave_e_cod/manuscript/wave_E_cod_intervention_v2.md", ["paperE2_cod_intervention.md"], True),
        ("E3", "wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder_v2.md", ["paperE3_edwards_forecast_ladder.md"], True),
        ("E4", "wave_e_edwards/manuscript/wave_E_edwards_intervention_v2.md", ["paperE4_edwards_intervention.md"], True),
    ]
    for name, s, ds, y in pairs:
        compare(name, "/home/user/repo/" + s, ["/home/user/arena agen1/"+d for d in ds], y)
