"""Restore only the literal v46->v47 redactions retained in paper07 v50.

The unblinded ancestor is in content_audit/seeds/07_previous_unblinded_...
The owner approved Amin Abaee and exactly one contribution sentence; other
personal roles are not inferred. One-shot, fails if the blinded form changes.
"""
from pathlib import Path
p = Path('/home/user/papers/paper07_sampled_governance_v50.tex')
s = p.read_text()
v46 = Path('/home/user/content_audit/seeds/07_previous_unblinded_paper5_sampled_governance_v46_NatSustain.tex').read_text()
author = v46[v46.index('\\author{'):v46.index('\\date{', v46.index('\\author{'))].strip()
assert s.count('\\author{Anonymous}') == 1
s = s.replace('\\author{Anonymous}', author)
assert s.count('(citation blinded for review') == 7
s = s.replace('citation blinded for review', 'Abaee, 2026')
# The v47 masking added a spurious open parenthesis inside the Candidate-A
# parenthetical; v46 has only one opening parenthesis here.
assert s.count('uncalibrated: (Abaee, 2026);') == 1
s = s.replace('uncalibrated: (Abaee, 2026);', 'uncalibrated: Abaee, 2026);')
assert s.count('[blinded]') == 9
s = s.replace('[blinded]', '24c980cd')
assert s.count('Author. 2026. [Blinded for review.]') == 1
bib = v46[v46.index('Abaee, A. 2026. Delay-induced'):v46.index('\n\n', v46.index('Abaee, A. 2026. Delay-induced'))]
s = s.replace('Author. 2026. [Blinded for review.]', bib)
# Scope: sampled-governance article, not a declaration borrowed from the delay study.
sub = v46[v46.index('\\subsection*{Funding}'):v46.index('\\end{document}', v46.index('\\subsection*{Funding}'))].strip()
# Contribution is the owner's exact sentence, not the older manuscript's wording.
assert '\\subsection*{Conflicts of interest}' in sub and '\\subsection*{AI declaration}' in sub
assert s.count('\\subsection*{Author contributions} Anonymized for review.') == 1
s = s.replace('\\subsection*{Author contributions} Anonymized for review.',
              '\\subsection*{Author contributions} A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.')
for name in ('Funding', 'Conflicts of interest', 'AI declaration'):
    start = sub.index('\\subsection*{' + name + '}')
    following = sub.find('\\subsection*{', start+2)
    original = sub[start:following if following >= 0 else len(sub)].strip()
    marker = '\\subsection*{' + name + '} Anonymized for review.'
    assert s.count(marker) == 1, name
    s = s.replace(marker, original)
# Eliminate only the obsolete review-mask header comments, retaining provenance.
assert 'revision v47, blinded for review' in s
s = s.replace('% The decision clock (paper 5, revision v47, blinded for review): author details, self-citations and declarations anonymized. Unblinded counterpart: v46.\n% Author details blinded for review.',
              '% Source history: v47 was a blinded-review derivative of unblinded v46; source attribution and declarations restored for the non-blind article.')
assert 'Anonymized for review.' not in s and '[blinded]' not in s and 'citation blinded for review' not in s
assert s.count('24c980cd') == 9
assert s.count('10.5281/zenodo.22554217') == 1
p.write_text(s)
print('paper07: v46 source author/citations/hash/reference/declarations restored; exact owner-approved contribution')
