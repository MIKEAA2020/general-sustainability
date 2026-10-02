#!/usr/bin/env python3
"""Versioned, source-scoped changes to the cod and forecast manuscripts."""
from pathlib import Path
from difflib import unified_diff
import shutil,hashlib
R=Path('/home/user');D=R/'content_audit/editorial_revisions'
def once(s,a,b):
 assert s.count(a)==1,(s.count(a),a[:100]);return s.replace(a,b,1)
def save(p,q,s):
 assert p.is_file() and not q.exists(),q;old=p.read_text();assert s!=old;q.write_text(s)
 (D/('editorial_'+q.parent.name.replace(' ','_')+'_'+q.name+'.diff')).write_text(''.join(unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(p.relative_to(R)),tofile=str(q.relative_to(R)))))
 print(str(q.relative_to(R)),len(s.splitlines()))
P=R/'papers';S=R/'paper 2 family'
# The source-year-stabilized staged v32, not the contradicted live v32, supplies the numeric revision.
orig=(P/'paper09_cod_certification_v32.tex').read_text();st=(S/'09_cod_with_arv/paper09_cod_certification_v32.tex').read_text()
st=once(st,'{\\small Independent Researcher, Tehran, Iran}','{\\small Independent Researcher}') # retain the live head's author line
st=once(st,'Author, C., et al., in preparation. Interval-verified bounds in linear\nmanagement templates. Companion methodological study.\n\n','')
# Manuscript-wide comment reflects the new two-system structure, not a still-embedded exact-rational part.
st=st.replace('%%         is NOT yet done. See PAPERS_MANIFEST.md.','%%         was reviewed for this editorial version; see the editorial change log.')
if not (P/'paper09_cod_certification_v33.tex').exists():save(P/'paper09_cod_certification_v32.tex',P/'paper09_cod_certification_v33.tex',st)
if not (S/'09_cod_with_arv/paper09_cod_certification_v33.tex').exists():save(S/'09_cod_with_arv/paper09_cod_certification_v32.tex',S/'09_cod_with_arv/paper09_cod_certification_v33.tex',st)
# Separate companion 09b: live citation is corrected; staged already had it.
for d in (P,S/'09_cod_with_arv'):
 p=d/'paper09b_arv_certification_v2.tex';v=p.read_text()
 if d==P:v=once(v,'An obstruction calculus for viability under\nincomplete observation. Submitted manuscript.','An Obstruction Calculus for Viability under Incomplete Observation. Figshare preprint, version 2. \\url{https://doi.org/10.6084/m9.figshare.33716593.v2}.')
 if d==P:v=once(v,'the companion paper (Part~I).','the separate two-system paper09 main (System I).')
 else:v=once(v,'the paper09 main (System I).','the separate two-system paper09 main (System I).')
 if (d/'paper09b_arv_certification_v3.tex').exists():
  q=d/'paper09b_arv_certification_v3.tex';q.write_text(v)
 else:save(p,d/'paper09b_arv_certification_v3.tex',v)
# The SI is recovered at a precise historical revision; do not edit/reconstruct its substantive content.
si=D/'E1_SUPPLEMENTARY_source.md';h=hashlib.sha256(si.read_bytes()).hexdigest();assert h=='fb3f8bd2e1eb5590c20371a6107fe7a40670eb67c8f92ae73682e26c31a4f122'
for d in (P,S/'11_forecasting_baselines'):
 out=d/'paper11_forecasting_baselines_v65_SI.md'
 if not out.exists():shutil.copy2(si,out)
 assert out.read_bytes()==si.read_bytes()
 (d/'paper11_forecasting_baselines_v65_SI_PROVENANCE.md').write_text('# Cod supporting information provenance\n\nThe attached `paper11_forecasting_baselines_v65_SI.md` is an unchanged copy of `E1_SUPPLEMENTARY.md` from `MIKEAA2020/general-sustainability` revision `1d27e763c4b55d9d2c355ccc31b31689e435b772`, at `arena agent 1/paper rewrites/latex/E1_SUPPLEMENTARY.md`. SHA-256: `'+h+'`. Its headings SI-1 through SI-5 are the cod study’s own supporting material; it does not purport to supply the aquifer study’s records. Original: https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/1d27e763c4b55d9d2c355ccc31b31689e435b772/arena%20agent%201/paper%20rewrites/latex/E1_SUPPLEMENTARY.md\n')
 p=d/'paper11_forecasting_baselines_v64.tex';v=(S/'11_forecasting_baselines/paper11_forecasting_baselines_v64.tex').read_text()
 v=once(v,'{\\small Independent Researcher, Tehran, Iran}','{\\small Independent Researcher}') # live head's existing author metadata
 v=once(v,'Forecasting under a locked retention rule: process models, naive benchmarks, and two systems','Forecasting against naive benchmarks: two systems, distinct retention protocols')
 v=once(v,'on \\emph{two} systems under one frozen\nretention rule:', 'on \\emph{two} systems under a shared RMSE scoring core and distinct disclosed retention clauses:')
 v=once(v,'The mechanism by which added structure fails differs between them', 'The mechanism by which added structure fails differs between them') if False else v
 v=once(v,'with later tie-band and comparator completions disclosed;', 'with the cod tie-band and comparator completions and the aquifer protocol deviations disclosed;')
 v=once(v,'method they share (the locked retention rule and the evaluation design) is restated in each part\nwith the system-specific detail it carries there.', 'common RMSE scoring comparison is restated in each part with its own horizon, comparator and retention clauses. The cod protocol is a fixed computational protocol, not prospectively registered: the 5\\% band and non-nested comparator declarations were completed after scores. The aquifer uses a one-horizon point rule with no 5\\% band and reports its own later completions.')
 v=once(v,'freeze the scoring core in advance. Both also report power', 'share a scoring core comparing added structure with naive benchmarks, but do not share one fully predeclared retention rule: cod formalised its 5\\% tie band and non-nested comparators after scoring, while Edwards used its own one-horizon point rule and disclosed later completions. Both also report power')
 v=once(v,'must clear naive persistence and the training mean under a protocol fixed in advance, and that the','must be scored against naive persistence and relevant simpler comparators under each system\\textquotesingle{}s disclosed protocol, and that the')
 v=once(v,'The two studies above were designed to answer one question with two systems, and the answer is the\nsame on both.', 'The two studies above address a shared forecasting question on two systems without pooling scores or imposing identical decision predicates. Their source-specific protocols and dates remain in their respective sections.')
 v=once(v,'\\newpage\n\n\\part*{Part I --- Northern cod', '\\noindent\\textbf{Cod supporting information.} SI-1--SI-5 cited in the cod study are attached as \\texttt{paper11\\_forecasting\\_baselines\\_v65\\_SI.md}; its source hash and revision are in the accompanying provenance note. These cod SI references do not denote the Edwards study\\textquotesingle{}s separate records.\n\n\\newpage\n\n\\part*{Part I --- Northern cod')
 save(p,d/'paper11_forecasting_baselines_v65.tex',v)
# Source history corroborates only the earlier internal worked-systems text, not independent cod ancestry.
for d in (P,S/'11c_worked_systems'):
 p=d/'paper11c_worked_systems_audit_v2.tex';v=p.read_text()
 a='The systems are drawn from the applied model of Abaee (2026, Robust viability of the 2J3KL limit reference point), in which\na two-coordinate resource stock is managed by acting one of two\ninstruments under incomplete observation.'
 b='The two-coordinate shared audit system is a constructed worked example in this paper, not the fitted one-stock Northern-cod model of Abaee (2026, Robust viability of the 2J3KL limit reference point). Earlier worked-systems source text uses the same two-coordinate construction but repeats the cod-origin attribution; that lineage alone does not establish an independent derivation from cod. The cod study motivates the applied question of robust resource viability, not these particular states, instruments or counts.'
 v=once(v,a,b)
 save(p,d/'paper11c_worked_systems_audit_v3.tex',v)
