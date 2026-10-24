import re, sys
def summarize(path, maxabs=2500):
    s = open(path, encoding='utf-8', errors='replace').read()
    title = re.search(r'\\title\s*(\[[^\]]*\])?\s*\{(.+?)\}\s*\n', s, re.S)
    print("FILE:", path)
    if title: print("TITLE:", re.sub(r'\s+', ' ', title.group(2))[:400])
    m = re.search(r'\\begin\{abstract\}(.+?)\\end\{abstract\}', s, re.S)
    if m:
        a = re.sub(r'\s+', ' ', m.group(1)).strip()
        print("ABSTRACT (%d chars):" % len(a)); print(a[:maxabs])
    kw = re.search(r'\\(?:begin\{keyword\}|keywords\{)(.+?)(?:\\end\{keyword\}|\})', s, re.S)
    if kw: print("KEYWORDS:", re.sub(r'\s+', ' ', kw.group(1))[:300])
    print("SECTIONS:")
    for mm in re.finditer(r'\\(section|subsection)\*?\{(.+?)\}', s):
        lvl = '  ' if mm.group(1)=='subsection' else ''
        print(lvl + '-', re.sub(r'\s+', ' ', mm.group(2))[:120])
    envs = {}
    for e in ['theorem','proposition','lemma','corollary','definition','remark','example','assumption','hypothesis','openproblem','conjecture']:
        n = len(re.findall(r'\\begin\{%s\}' % e, s))
        if n: envs[e]=n
    print("ENVS:", envs)
    print("FIGURES:", len(re.findall(r'\\begin\{figure', s)), "TABLES:", len(re.findall(r'\\begin\{table', s)), "CITES(bibitems):", len(re.findall(r'\\bibitem', s)), "WORDS~:", len(re.sub(r'\\[a-zA-Z]+|[{}$\\]', ' ', s).split()))
    print("="*100)
for p in sys.argv[1:]:
    try: summarize(p)
    except Exception as ex: print("ERR", p, ex)
