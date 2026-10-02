#!/usr/bin/env python3
"""Pre-submission staging checks for eight units; not a scientific proof.
Checks exact source/package identity, compile evidence, original paper09
abstracts, live-head preservation, ARV extraction and asset manifest.
"""
from pathlib import Path
from difflib import unified_diff
from collections import Counter
import csv,hashlib,re
R=Path('/home/user');A=R/'content_audit/claim_alignment';P=R/'paper 2 family'
expected={'01_obstruction','02_probabilistic_sufficiency','03_computational_certification','04_minimax_dual_certificates','05_exact_belief_computation','09_cod_with_arv','11_forecasting_baselines','11c_worked_systems'}
actual={p.name for p in P.iterdir() if p.is_dir() and p.name[0].isdigit()};assert actual==expected,(actual,expected)
rows=list(csv.DictReader((P/'SHA256SUMS.tsv').open(),delimiter='\t'))
assert len(rows)==83 and len({r['path'] for r in rows})==83
for row in rows:
 f=P/row['path'];assert f.is_file() and hashlib.sha256(f.read_bytes()).hexdigest()==row['sha256'],f
for f in P.rglob('*.tex'):
 assert f.read_bytes()==(A/'drafts'/f.name).read_bytes(),f
 assert (f.with_suffix('.pdf')).is_file(),f
for name in ('figs_e1','figs_e3','figs_e2_v3','figs_e4'):
 assert (P/name).is_dir(),name
b=A/'compile';compiled=list(csv.DictReader((b/'results.tsv').open(),delimiter='\t'))
assert len(compiled)==12 and all(row['pass']=='1' and row['exit']=='0' and row['undefined_references']=='0' and row['missing_assets']=='0' for row in compiled)
for row in csv.DictReader((b/'paper09_results.tsv').open(),delimiter='\t'):
 assert row['pass']=='1' and row['exit']=='0' and row['undefined_references']=='0' and row['missing_assets']=='0'
live=(R/'papers/paper09_cod_certification_v32.tex').read_text();main=(A/'drafts/paper09_cod_certification_v32.tex').read_text();arv=(A/'drafts/paper09b_arv_certification_v2.tex').read_text()
start=live.index('\\part*{Part II --- Regime viability on the Northern cod stock}');end=live.index('\\part*{Part III --- Governance operators',start)
assert (A/'original_sections/paper09_v32_embedded_ARV.tex').read_text()==live[start:end]
original=re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',live,re.S)
assert len(original)==4
for i,text in enumerate(original,1):assert (A/'original_abstracts'/f'paper09_cod_certification_v32_live_abstract_{i}.txt').read_text()==text
assert len(re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',main,re.S))==3
pre=(A/'original_sections/paper09b_arv_v2_prehost.tex').read_text()
assert re.search(r'\\begin\{abstract\}.*?\\end\{abstract\}',pre,re.S).group() in arv
assert 'Part II --- Regime Viability' in arv and 'Part II --- Regime viability' not in main
assert 'xteNCAM (this row) & 0.5023 & 4813.1 & 1.4447 & 7.49 & 276.0 & 276.0' in main
assert 'xteNCAM (this row) & 0.5023 & 4812.9 & 1.4447 & \\ensuremath{-}48.0' not in main
assert (P/'POSTING_METADATA_2026-10-02.md').is_file()
assert 'nine intended Preprints.org postings' in (P/'README.md').read_text()
assert not re.search(r'\\(?:ref|eqref|pageref)\{regime-[^}]+\}',main)
assert 'figs_arv/fig_record.pdf' not in main
for fn,source,new,diffname in [('paper09_cod_certification_v32.tex',live,main,'paper09_cod_certification_v32_host_2026-10-02.diff'),('paper09b_arv_certification_v2.tex',pre,arv,'paper09b_arv_certification_v2_host_2026-10-02.diff')]:
 diff=(A/'diffs'/diffname).read_text()
 assert diff.splitlines()[2:]==''.join(unified_diff(source.splitlines(True),new.splitlines(True))).splitlines()[2:],diffname
# Check executable TeX starts/ends, not commented provenance tokens.
for f in P.rglob('*.tex'):
 t='\n'.join(re.sub(r'(?<!\\)%.*$','',line) for line in f.read_text().splitlines())
 assert len(re.findall(r'\\begin\{document\}',t))==1 and len(re.findall(r'\\end\{document\}',t))==1,f
 assert Counter(re.findall(r'\\begin\{([^}]+)\}',t))==Counter(re.findall(r'\\end\{([^}]+)\}',t)),f
print('FINAL_STAGING_PASS',len(expected),'intellectual units / 9 intended postings',len(rows),'SHA-verified package files',len(compiled)+2,'passing isolated TeX runs; source-year xte review candidate, not publication proof')
