"""One-shot paper08 v46 correction using its two unblinded source studies.

Paper07 inherited review masks from v47; those exact masks are the only
citation/hash/reference substitutions here. Combined author block is from
paper08's continuous-channel v45, corroborated by sampled v46. No CRediT roles
inferred: replace the unfilled template with owner's exact contribution text.
"""
from pathlib import Path
p = Path('/home/user/papers/paper08_governance_delay_v46.tex')
s = p.read_text()
a = Path('/home/user/papers/paper08_governance_delay_v45.tex').read_text()
b = Path('/home/user/content_audit/seeds/07_previous_unblinded_paper5_sampled_governance_v46_NatSustain.tex').read_text()
author = a[a.index('\\author{'):a.index('\\date{',a.index('\\author{'))].strip()
bib = b[b.index('Abaee, A. 2026. Delay-induced'):b.index('\n\n', b.index('Abaee, A. 2026. Delay-induced'))]
assert s.count('\\maketitle') == 3 and not s.count('\\author{')
assert s.count('(citation blinded for review') == 7 and s.count('[blinded]') == 9
assert s.count('Author. 2026. [Blinded for review.]') == 1
s=s.replace('\\begin{document}\n\\title{', '\\begin{document}\n'+author+'\n\\title{',1)
s=s.replace('citation blinded for review','Abaee, 2026')
s=s.replace('uncalibrated: (Abaee, 2026);','uncalibrated: Abaee, 2026);')
s=s.replace('[blinded]','24c980cd')
s=s.replace('Author. 2026. [Blinded for review.]',bib)
# Keep the umbrella title page. Part titles and their own abstracts remain,
# but repeated source maketitles do not make a three-title-page article.
first=s.index('\\maketitle')
s=s[:first+len('\\maketitle')]+s[first+len('\\maketitle'):].replace('\\maketitle','')
start=s.index('\\subsection*{CRediT authorship contribution statement}')
end=s.index('\\subsection*{AI declaration}',start)
assert '[AUTHOR NAME --- full name as it should appear]' in s[start:end]
s=s[:start]+('\\subsection*{Author contributions}\n'
 'A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.\n\n')+s[end:]
# Sampled-source declaration included a responsibility statement absent from the
# merged declaration. Attribute it to that study, without replacing Part I's AI.
ai='GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.'
assert s.count(ai)==1
s=s.replace(ai,ai+' For the sampled-governance source: The author reviewed and edited the work and takes responsibility for the content of the manuscript.',1)
assert not any(t in s for t in ['citation blinded for review','[blinded]','Anonymized for review.','Author. 2026. [Blinded for review.]','[AUTHOR NAME ---'])
assert s.count('\\maketitle') == 1 and s.count('\\author{') == 1
assert s.count('10.5281/zenodo.22554217') == 1 and s.count('24c980cd')==9
assert s.count('\\subsection*{References}')==1 and s.count('\\section*{Declarations}')==1
p.write_text(s)
print('paper08: source v46 citation/hash/reference restored, v45 author, approved contribution; 1 title page')
