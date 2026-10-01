#!/usr/bin/env python3
"""Source-specific, non-destructive ARV aligned draft."""
from pathlib import Path
from difflib import unified_diff
import re
root=Path('/home/user');base=root/'content_audit/claim_alignment'
src=root/'papers/paper09b_arv_certification_v2.tex';old=src.read_text();s=old
abs_=re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',old,re.S);assert len(abs_)==1
(base/'original_abstracts').mkdir(parents=True,exist_ok=True)
(base/'original_abstracts'/(src.stem+'.txt')).write_text(abs_[0])
def change(a,b):
 global s
 assert s.count(a)==1,(s.count(a),a[:95]);s=s.replace(a,b,1)
# Historical terminator spelling was inside a comment, but fooled raw token counts.
change('%% WHY THIS FILE EXISTS: in v30 this half sat AFTER the first \\end{document}',
       '%% WHY THIS FILE EXISTS: in v30 this half sat AFTER the first document terminator')
change('This paper certifies that specific steps in the published Northern cod record were\ncontractions regardless of removals.',
       'This paper infers subunitary non-fishing factors for specific Northern cod\nassessment steps under either of the two stated removals-accounting forms.')
change('was the step a contraction even had removals been zero? That is a statement about the\n\\emph{arithmetic of the record}, not about the cause of the collapse.',
       'does either declared accounting equation imply a subunitary non-fishing\nfactor at the observed reading and catch? That is a conditional statement about the\n\\emph{arithmetic of the record}, not a biological zero-harvest counterfactual or a claim about the cause of the collapse.')
change('and the individual annual steps can still be contractions at zero harvest. Both hold here.',
       'and the observed annual steps can still have inferred non-fishing factors below one under both declared accounting forms. Only the latter is established here.')
change('The contraction is accordingly robust to the choice of series, and is if anything\nstronger in the raw survey than in the assessment record on which the main certificates are\ncomputed. That result is the answer to the divergence concern, and it is stated here so that\nthe reader can see the concern was met rather than assumed away.',
       'The recorded net decline is visible in both series and is steeper in the raw survey\nover the stated common window. The harvest-free multiplier bracket, however, is computed\nonly from assessment SSB and assigned removals, not from the survey-index units; the\nsurvey result does not independently certify a harvest-free contraction.')
change('but no placement of\nthe \\emph{realized} removals within the interval\'s accounting --- early\nor late --- can leave the non-fishing account non-contracting when the\nbracket\'s upper bound is sub-unitary.',
       'and under either of the two \\emph{declared} placements of realized\nremovals --- before or after a single interval-wide factor --- the\ninferred non-fishing factor is subunitary when the bracket\'s upper bound is.\nArbitrary within-interval biological time variation is not covered.')
change('Fifteen of the twenty-one\nsubwindows are all-growth at the annual level.',
       'Fifteen of the twenty-one\nsubwindows grow in net from start to end; only five grow at\nevery constituent annual step.')
change('A threshold fixed at a window\'s own mean places roughly half\nthat window\'s readings below it by construction and retains no\nheadroom above it (the window\'s maximum is \\(6.4\\%\\) above; its\nminimum \\(5.5\\%\\) below, outward-rounded).',
       'For this particular window three of seven readings fall below its\nmean (the maximum is \\(6.4\\%\\) above and the minimum \\(5.5\\%\\)\nbelow, outward-rounded). In general, the mean of nonconstant readings\nfalls between the minimum and maximum but guarantees neither a near-half\ncount below nor a uniform headroom bound.')
change('\\(12{,}881\\) t in 2017) --- between \\(2.3\\%\\) and \\(3.0\\%\\) of the\nsame vintage\'s stock reading per year.',
       '\\(12{,}881\\) t in 2017). For the six outcome years 2016--2021,\nthose official removals are between \\(2.3\\%\\) and \\(3.0\\%\\) of\nthe database vintage\'s stock reading; the 2015 share is\n\\(4436/277000\\approx1.60\\%\\) and is not in that range.')
change('harvest-free contractions under every timing convention the rows admit\n(upper bounds \\(0.754\\) and \\(0.372\\)): no placement of the realized\nremovals --- which the year of the floor breach puts at \\(4.06\\%\\) of\nthe stock\'s loss --- explains the decline,',
       'associated with inferred non-fishing factors below one under\nboth stated accounting forms and both adjacent-row alignments (upper\nbounds \\(0.754\\) and \\(0.372\\)). The observed removals for the\nfloor-breach year equal \\(4.06\\%\\) of the stock loss; no biological\nzero-removals counterfactual is identified here,')
change('and separates nothing: a design property of mean-rule thresholds,\ncertified here on the readings themselves.',
       'and separates nothing in this window: an observed property of\nthese seven readings, not a universal near-half rule for means.')
change('and under the moratorium\'s\nown removals rows the non-fishing account drove a further certified\nfactor-of-\\(10.4\\) contraction to the series minimum.',
       'and under the moratorium\'s\nown removals rows subunitary inferred non-fishing factors accompany\na further factor-of-\\(10.4\\) decline to the series minimum.')
change('typology (two harvest-free collapse steps inside a\nfishing-era decline)',
       'typology (two steps with subunitary accounted non-fishing factors\ninside a fishing-era decline)')
change('zero-removals counterfactual is identified here, and under the moratorium\'s',
       'zero-removals counterfactual is identified here. Under the moratorium\'s')
assert re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',s,re.S)==abs_
out=base/'drafts'/src.name;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(s)
(base/'diffs'/(src.stem+'.diff')).write_text(''.join(unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(src),tofile=str(out))))
print(out)
