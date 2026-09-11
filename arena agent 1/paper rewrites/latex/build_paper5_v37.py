"""Build paper5 v37 main tex from v36. All six open-items discharges. Guarded edits."""
import re

SRC = '/home/user/paper5_v36/paper5_sampled_governance_v36.tex'
DST = '/home/user/paper5_v37/paper5_sampled_governance_v37.tex'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:200]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

def repw(old_joined, new, tag):
    """Whitespace-flexible: old given space-joined, matched across line wraps."""
    global s
    pat = re.compile(re.escape(old_joined).replace(r'\ ', r'\s+'))
    ms = pat.findall(s)
    assert len(ms) == 1, f'{tag}: count={len(ms)}\n---\n{old_joined[:200]}'
    s = pat.sub(lambda _: new, s, count=1)
    print(f'{tag}: OK (flex)')

print('--- zero inventory ---')
for m in re.finditer(r'.{80}(?:no qualifying example|No system in the|zero count).{60}', s):
    print(' *', m.group(0).replace('\n', ' ')[:160])

rep('% Periodic Review as Sampled Governance (paper 5, revision v36): supplementary-readability revision (sentence splits, glossary lists; no content change) with line numbers for review.',
    '% Periodic Review as Sampled Governance (paper 5, revision v37): six open-items discharges (U5 case table/log, eta basis, Icelandic-cod audit, Lemma 2.2 seal application, Prop 2.1 demotion, I5 data/code split, 4.4(iii) illustration, T_r-ranked test) with line numbers for review.',
    'M0-version')

rep(r'\textbf{Proposition 2.1} (Phase-line obstruction). Let',
    r'\textbf{Remark 2.1} (Phase-line obstruction). Let', 'M2-remark')

rep(r'\emph{Statement.} (i) Constant loss.',
    r'\emph{Statement.} Assume \(0 < \mathfrak s < K\). (i) Constant loss.', 'M3-hypothesis')

repw('and the same threshold-shift reading applies to the modified positive roots.',
    r'and the smaller modified positive root lies strictly above \(\mathfrak s\) (in \((\mathfrak s, S_h)\), where \(S_h\) is the vertex of the per-capita curve \(h(S) = f(S)/S\)).',
    'M4-tighten')

rep('mortality-allocation comparison --- states.\n',
    'mortality-allocation comparison --- states. Read through Lemma 2.2(ii), the seal-predation attribution carries a directional consequence: to the extent predation acts as additional mortality on the stock, the effective threshold facing recovery lies above \\(\\mathfrak s\\), so predation raises the threshold for re-establishment rather than merely slowing convergence. No predation-mortality rate is estimated here; the lemma is used for the direction of the effect, not its magnitude.\n',
    'M5-seal-apply')

repw('has a post-implementation coefficient of variation of 0.143, lower despite higher recruitment variability.',
    'has a post-2013 (own-HCR) SSB coefficient of variation of 0.24, lower despite higher recruitment variability.',
    'M6-haddock')

repw('has a post-rule coefficient of variation of 0.387 (calculated here) with a 10--15 yr fluctuation.',
    'has a post-rule coefficient of variation of 0.387 (calculated here; 0.394 on the current ICES vintage, Supplementary S4) with a 10--15 yr fluctuation.',
    'M7-cod-audit')

repw('If realistic record lengths have low power for the predicted signal, field spectral nulls cannot adjudicate the mechanism; prospective or experimental evidence is required.',
    'If realistic record lengths have low power for the predicted signal, field spectral nulls cannot adjudicate the mechanism; prospective or experimental evidence is required. The Icelandic cod case illustrates the bind: its 10--15 yr fluctuation sits inside the continuous-delay band (9.9--20.3 yr) yet carries no institutional signature, because a competing environmental driver is empirically supported for the same outcome (criterion (iii); Supplementary S4).',
    'M8-44iii')

repw('Five designs are specified as preregistration targets; none has been executed,',
    'Retrospective evidence can still discipline the mechanism where a prespecified contrast exists: the \\(T_r\\)-ranked cross-sectional test across the 42-stock cohort is executed in Supplementary S10 and returns a controlled null --- no window-approach gradient, with \\(T_r \\approx 1\\) dormancy holding at 0/42 and 1/42 flags in the two bands. Five designs are specified as preregistration targets; none has been executed,',
    'M9-tr-pointer')

rep('yr\\(^{-1}\\) at \\(\\eta=0.914\\) with a delay interval',
    'yr\\(^{-1}\\) at \\(\\eta=0.914\\) (the uncalibrated Candidate-A baseline; Appendix A) with a delay interval',
    'M10-eta-firstuse')

repw('effort-response coefficient \\(\\eta\\) & 0.914 & This table; constants block \\texttt{droop\\_test.py} L49--58 @ 24c980cd \\\\',
    'effort-response coefficient \\(\\eta\\) & 0.914 & This table; constants block \\texttt{droop\\_test.py} L49--58 @ 24c980cd; inherited illustrative baseline (Candidate-A value from the companion delay study, whose institutional coefficients are explicitly uncalibrated: Abaee, 2026); the delay-Hopf window opens between \\(\\eta = 0.5\\) and \\(0.7\\) and the \\(r = 0.02\\) inclusion threshold sits at \\(\\eta^* \\approx 0.85\\), so 0.914 is neither threshold (basis runs deposited; Supplementary S9.2) \\\\',
    'M11-eta-basis')

rep('identified from periodicity alone.',
    'identified from periodicity alone. No system in the searched set meets all four criteria; the case-screening table (32 systems) and query log are recorded in Supplementary S4.',
    'M12-u5-pointer')

repw('the nonlinear exact-update comparison of Section 3.4, and the case-screening table and query log are registration requirements;',
    'the nonlinear exact-update comparison of Section 3.4 are registration requirements; the case-screening table and query log are deposited with the article;',
    'M13a-dataavail-flip')

repw('The spectral-screen materials (RAM stock identifiers and eligibility table, processed spectral series and routines), the power-simulation code and seeds, and the sensitivity-battery code and logs are deposited with the article.',
    'The analysis datasets (RAM stock identifiers and eligibility table; processed spectral series; case-screening table and query log; \\(T_r\\)-ranked test table; ICES cod and haddock series; \\(\\eta\\)-basis window runs) and the analysis code (spectral-screen routines; power-simulation code and seeds; sensitivity-battery code and logs; case-screen, \\(T_r\\)-ranked test, Icelandic-cod audit, and \\(\\eta\\)-basis scripts with their logs) are deposited with the article.',
    'M13b-i5-split')

print('--- supp-guide context ---')
i = s.find('case-screening records at full detail (S4)')
print(s[i:i+700].replace('\n', ' '))
m = re.search(r'(stage-scan decomposition\s+records \(S9\)[^.]*)\.', s[i:i+700])
assert m, 'M14: S9 list anchor missing'
full = m.group(1)
rep(full + '.', full + ', and the \\(T_r\\)-ranked test record (S10).', 'M14-s10-list')

print('--- post-checks ---')
print('Proposition 2.1 remaining:', s.count('Proposition 2.1'))
print('Remark 2.1:', s.count('Remark 2.1'))
print('0.143 remaining:', s.count('0.143'))
print('len delta:', len(s) - n0)
assert s.count('Proposition 2.1') == 0
assert s.count('0.143') == 0

open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)
