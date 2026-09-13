#!/usr/bin/env python3
"""Phase B implementation (2026-09-13) — framework v14 -> v15.

Owner decisions (recorded in PHASE_B_ROOT_CAUSE_DECISION_MEMO.md and the interactive prompt):
  AD6 = adopt fully  -> title / abstract / section 1 / section 7 / section 8 reframed in ONE pass:
                        the deliverable is a minimum reporting standard for non-retention claims;
                        the retention rule is its worked example. Verdicts/tables/numbers untouched.
  AD2 = option (a)    -> keep frozen pre-registered labels, rename the concept to
                        "mechanism misattribution" in prose, add a "Row measures" column to Table 2b.
  AD4 = option (b)    -> reword the prospective-band sentence: future applications only,
                        never re-opens the verdicts reported here.
Version discipline: v14 is untouched; this pass writes v15.
"""
SRC = 'framework/paperF1_retention_framework_v14.md'
DST = 'framework/paperF1_retention_framework_v15.md'

s = open(SRC, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, f'expected {n} match(es), got {c} for: {old[:80]!r}'
    s = s.replace(old, new)

# ---------------- AD6 — the reframe (adopted fully) ----------------

rep('# When does added model structure earn its place? A retention rule, an information-set audit, and two out-of-domain applications',
    '# When a model is not retained, what must be reported? A retention rule, an information-set audit, and operating characteristics — a minimum reporting standard worked on three scored objects in two domains')

rep('or the decision instrument may lack the power to detect it.',
    'or the decision instrument may lack the power to detect it. The field lacks a minimum standard for making such claims interpretable; this article proposes one and demonstrates it.')

rep('**Approach.** This article states a retention rule as an explicit algorithm, pairs it with an information-set audit that separates quantities available at the forecast origin from quantities supplied after it, and evaluates the rule itself by simulation under known ground truth.',
    '**Approach.** This article proposes a minimum reporting standard for non-retention claims, with three components: a retention rule stated as an explicit algorithm; an information-set audit that separates quantities available at the forecast origin from quantities supplied after it; and a mandatory operating-characteristic study that evaluates the rule itself by simulation under known ground truth.')

rep('The rule is applied unchanged to three scored objects in two unrelated domains:',
    'The standard is worked unchanged on three scored objects in two unrelated domains:')

rep('**Implications.** Non-retention is strong evidence against a module where the rule has power (D1) and weak where it does not (D3/D4). Reporting a verdict without operating characteristics leaves the reader unable to distinguish. Information criterion outperforms the adopted rule on both axes — instrument choice for new work. Minimum accompanying evidence: rule\'s power under in-class processes own models could generate and specificity under null, with block-bootstrap intervals.',
    '**Implications.** Non-retention is strong evidence against a module where the rule has power (D1) and weak where it does not (D3/D4). Reporting a verdict without operating characteristics leaves the reader unable to distinguish the two, which is why the standard makes them mandatory. The information criterion outperforms the adopted rule on both axes — a finding about instrument choice within the standard, not against it. Minimum accompanying evidence: the rule\u2019s power under in-class processes the study\u2019s own models could generate, and its specificity under the null, with block-bootstrap intervals.')

rep('**Keywords:** model selection; out-of-sample forecasting; retention rule; operating characteristics;',
    '**Keywords:** model selection; out-of-sample forecasting; retention rule; reporting standard; operating characteristics;')

rep('Contribution is not finding persistence hard to beat, which companions report. It is that same rule, with operating characteristics measured, produces same verdict in two unrelated physical systems by two different routes, and conditions under which verdict informative can be stated.',
    'The contribution is not finding persistence hard to beat, which the companions report. It is a minimum reporting standard for non-retention claims — a retention rule stated as an algorithm, an information-set audit, and mandatory operating characteristics — demonstrated by the same rule, with those characteristics measured, producing the same verdict in two unrelated physical systems by two different routes, with the conditions under which a verdict is informative stated. The rule is the worked example; the standard is the deliverable.')

rep('Sections 5 and 6 apply rule to three scored objects and compare. Section 7 states what pair jointly licenses and not.',
    'Sections 5 and 6 apply the rule to three scored objects and compare. Section 7 states what the standard extracts from the pair, and what it does not license.')

rep('## 7. What the two applications license',
    '## 7. What the standard extracts from the two applications')

rep('**Licensed.** Rule applicable to scored objects in unrelated domains: original pre-registered rule had no tie band, unified rule adds 5% band post-hoc to groundwater as disclosed in Section 5.2; verdicts unchanged under both versions, returns interpretable verdicts in both.',
    '**Licensed.** The standard is applicable to scored objects in unrelated domains: the original pre-registered rule had no tie band, the unified rule adds the 5% band post-hoc to groundwater as disclosed in Section 5.2; verdicts are unchanged under both versions, and the rule returns interpretable verdicts in both.')

rep('**Implication for practice.** Retention verdict reported without operating characteristics leaves reader unable to distinguish module uninformative from rule cannot see it. The two opposite conclusions — module uninformative versus rule cannot see it — and score alone does not separate them. Where study reports non-retention, minimum accompanying evidence is rule\'s power under process study\'s own models could have generated, and its specificity under null, with block-bootstrap intervals per Künsch 1989. Information criterion dominating on both axes bears on instrument choice. Formal information-set table — what is available at origin t and to which module — is most useful addition, proposed as reporting template.',
    '**Implication for practice.** Any non-retention report should carry the standard\u2019s three components: a verdict without a pre-stated rule, without an information-set audit, or without operating characteristics leaves the reader unable to distinguish a module that is uninformative from a rule that cannot see it. The two opposite conclusions — module uninformative versus rule cannot see it — the score alone does not separate them. Where a study reports non-retention, the minimum accompanying evidence is the rule\u2019s power under processes the study\u2019s own models could have generated, and its specificity under the null, with block-bootstrap intervals per Künsch (1989). That the information criterion dominates on both axes bears on instrument choice within the standard, not on the standard. The formal information-set table — what is available at origin t and to which module — is the most useful single addition, proposed as a reporting template.')

rep('Retention rule stated as algorithm, paired with information-set audit, evaluated by pre-registered simulation.',
    'The minimum reporting standard for non-retention claims is stated and demonstrated: a retention rule as an explicit algorithm, an information-set audit, and a pre-registered operating-characteristic simulation, worked unchanged on three scored objects in two domains.')

rep('Non-retention therefore strong evidence against module where rule shown to have power and weak evidence where not. Reporting verdict without operating characteristics does not distinguish two. Pre-check diagnostic identifying in advance where rule has power remains open (dispersion Spearman 0.52 weak, margin 0.88 strong but circular and misclassifies stock-flow cells).',
    'Non-retention is therefore strong evidence against a module where the rule is shown to have power and weak evidence where it is not; reporting a verdict without the standard\u2019s three components cannot distinguish the two. The negative findings are themselves evidence for the standard: a pre-registered, calibrated rule retains nothing where the data are uninformative, and only the operating-characteristic study reveals the difference. A pre-check diagnostic identifying in advance where the rule has power remains open (dispersion Spearman 0.52 weak, margin 0.88 strong but circular and misclassifies stock-flow cells).')

# ---------------- AD2 — mechanism misattribution (option a) ----------------

rep('| Process | Truth | σ low 11.8 | σ high 33.8 | Note |\n|---|---|---|---|---|',
    '| Process | Truth | σ low 11.8 | σ high 33.8 | Row measures | Note |\n|---|---|---|---|---|---|')

rep('| D1 autonomous collapse | M1 | 0.965 | 0.985 | power high, exceeds 80% adequacy bar |',
    '| D1 autonomous collapse | M1 | 0.965 | 0.985 | decision reliability | power high, exceeds 80% adequacy bar |')
rep('| D2 autonomous recovery | M1 | 0.710 | 0.130 | power falls with noise, low σ near bar, high σ below |',
    '| D2 autonomous recovery | M1 | 0.710 | 0.130 | decision reliability | power falls with noise, low σ near bar, high σ below |')
rep('| D3 stock-flow | M2 | 0.090 | 0.110 | 18–22× the null false-retention rate (0.005 per module), below bar |',
    '| D3 stock-flow | M2 | 0.090 | 0.110 | decision reliability | 18–22× the null false-retention rate (0.005 per module), below bar |')
rep('| D4 depensation identifiable | M1b | 0.005 | 0.015 | below bar |',
    '| D4 depensation identifiable | M1b | 0.005 | 0.015 | decision reliability | below bar |')
rep('| D5 persistence-true (specificity) | none | 0.985 | 0.970 | 1 - any retained |',
    '| D5 persistence-true (specificity) | none | 0.985 | 0.970 | decision reliability (specificity) | 1 - any retained |')
rep('| **D6 time-varying productivity** | out-of-class | **0.680** | **0.760** | false retention |',
    '| **D6 time-varying productivity** | out-of-class | **0.680** | **0.760** | mechanism attribution | false retention |')
rep('| **D7 obs error only** | out-of-class | **0.975** | **0.925** | false retention |',
    '| **D7 obs error only** | out-of-class | **0.975** | **0.925** | mechanism attribution | false retention |')

rep('false retention 0.680/0.760; D7 observation-error-only (state evolves noise-free r=0.9, K=1032.7, C=180, scored series = state + Gaussian noise) → 0.975/0.925 versus pre-declared 0.10 threshold — specificity conditional.',
    'mechanism misattribution 0.680/0.760; D7 observation-error-only (state evolves noise-free r=0.9, K=1032.7, C=180, scored series = state + Gaussian noise) → mechanism misattribution 0.975/0.925 versus pre-declared 0.10 threshold — specificity conditional.')

rep('| Decision rule | mean power | specificity | false retention misspecification D6-D7 |',
    '| Decision rule | mean power | specificity | mechanism misattribution, misspecified (D6-D7) |')

rep('Retention licenses a prediction claim, never a mechanism claim; the D6/D7 rows measure the gap between the two, and the realised predictive gain of the retained module in those replicates is registered for reporting.',
    'Retention licenses a prediction claim, never a mechanism claim; the D6/D7 rows measure mechanism misattribution — retention on a real predictive gain that the module\u2019s mechanism did not cause — and the \u201cRow measures\u201d column separates decision reliability (D1–D5) from mechanism attribution (D6/D7). The realised predictive gain of the retained module in those replicates is registered for reporting.')

# ---------------- AD4 — prospective band, future-only (option b) ----------------

rep('A simulation-calibrated band targeting power ≥0.80 / specificity ≥0.90 at the object’s own T and SNR is registered as the prospective replacement.',
    'A simulation-calibrated band targeting power ≥0.80 / specificity ≥0.90 at the object\u2019s own T and SNR is registered as the prospective replacement for future applications of the standard; it never re-opens the verdicts reported here, which remain decided by the frozen 5% band.')

open(DST, 'w', encoding='utf-8').write(s)
print(f'wrote {DST} ({len(s):,} chars, {s.count(chr(10))} lines)')
