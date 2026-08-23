from pathlib import Path

p = Path('general_theory_of_sustainability_v0.2_comprehensive.md')
text = p.read_text(encoding='utf-8')
marker_d = '# Appendix D. Traceability matrix for the theory-building dialogue'
marker_e = '# Appendix E. Expanded classification of conclusions'
pre, tail = text.split(marker_d, 1)
trace_body, appendix_e = tail.split(marker_e, 1)

# Clean academic manuscript: remove process note and change-log language.
pre = pre.replace('**Comprehensive working manuscript, Version 0.2**  \n', '**Working manuscript**  \n')
pre = pre.replace('**Scope note:** This version incorporates all valid substantive material developed during the preceding theory-building dialogue. Rejected or qualified claims are retained and explicitly evaluated rather than silently omitted.  \n', '')
pre = pre.replace('The current proposal complements this tradition', 'The proposed framework complements this tradition')
pre = pre.replace('First, the current proposal may be a formal framework', 'First, the proposed account may be a formal framework')

# Appendix E becomes D after traceability is removed.
clean = pre.rstrip() + '\n\n# Appendix D. Expanded classification of conclusions\n' + appendix_e.lstrip()
Path('general_theory_of_sustainability_manuscript.md').write_text(clean, encoding='utf-8')

trace = '''# Traceability Report: General Theory of Sustainability Manuscript\n\n**Companion document**  \n**Manuscript:** *Toward a General Theory of Sustainability: Robust Viability in Dependency-Closed Ecological, Economic, and Social Systems*  \n**Date:** 14 August 2026\n\n## Purpose\n\nThis report maps the substantive concepts developed during theory construction to their locations in the manuscript. It is maintained separately so that the manuscript reads as a self-contained scholarly argument rather than a development log.\n\n## Traceability matrix\n\n''' + trace_body.strip() + '\n'
# Remove duplicate explanatory sentence/header remnants from extracted body.
trace = trace.replace('This appendix records where each valid substantive element developed during the dialogue appears in Version 0.2. It is intended to make omission visible.\n\n', '')
trace = trace.replace('| Dialogue element | Manuscript location | Treatment |', '| Source concept | Manuscript location | Treatment |')
Path('general_theory_of_sustainability_traceability.md').write_text(trace, encoding='utf-8')

print('manuscript chars', len(clean))
print('trace chars', len(trace))
