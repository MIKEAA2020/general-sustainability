import io, re, os, json

D = '/home/user/papers/'
files = sorted(f for f in os.listdir(D) if f.startswith('paper') and f.endswith('.tex'))
W = lambda t: len(re.findall(r"[A-Za-z']+", t))

def count_res(t):
    n = 0
    for env in ('theorem', 'proposition', 'lemma', 'corollary', 'definition'):
        n += len(re.findall(r'\\begin\{' + env + r'\}', t))
    n += len(re.findall(r'\\paragraph\{(Theorem|Proposition|Lemma|Corollary)', t))
    return n

# markers of explicit novelty positioning
RELATED = r'(?i)(related work|prior art|literature review|previous work|comparison with)'
CONTRIB = r'(?i)(contribution|we (?:show|establish|prove|provide)|our result|main result|novel)'
# markers of empirical / applied content
EMPIR = r'(?i)\b(kt\b|stocks?\b|NAFO|cod\b|Edwards|case study|data set|dataset|empirical|observed|catch\b|survey data|reserve)'
PRIOR_RISK = r'(?i)(to our knowledge|has not been|not been stated|leave[s]? open|open problem)'

rows = []
for f in files:
    t = io.open(D + f, encoding='utf-8').read()
    body = t
    secs = re.findall(r'\\(?:sub)?section\{([^}]*)\}', body)
    rows.append(dict(
        file=f,
        words=W(body),
        sections=len(secs),
        results=count_res(body),
        related=len(re.findall(RELATED, body)),
        contrib=len(re.findall(CONTRIB, body)),
        empir=len(re.findall(EMPIR, body)),
        prior_risk=len(re.findall(PRIOR_RISK, body)),
        has_related_sec=1 if any(re.search(RELATED, s) for s in secs) else 0,
        bib=len(re.findall(r'\\bibitem|\\subsection\{References\}|thebibliography', body)),
    ))

hdr = "%-42s %7s %5s %5s %6s %6s %6s %6s %4s" % (
    "file", "words", "sect", "res", "relat", "contr", "empir", "risk", "refS")
print(hdr); print("-" * len(hdr))
for r in rows:
    print("%-42s %7d %5d %5d %6d %6d %6d %6d %4d" % (
        r['file'], r['words'], r['sections'], r['results'], r['related'],
        r['contrib'], r['empir'], r['prior_risk'], r['has_related_sec']))
json.dump(rows, open('/home/user/papers/_bar.json', 'w'), indent=1)
