import re
txt = open('data/revisions/IMPLEMENTED_revision_ECOMOD_v21.md').read()
m = re.search(r'## Abstract\n(.*?)\n\n\*\*Keywords', txt, re.S)
ab = m.group(1)
clean = re.sub(r'[`*_#]', '', ab)
toks = [t for t in clean.split() if re.search(r'[A-Za-z0-9]', t)]
print("ABSTRACT WORD COUNT:", len(toks))
kw = re.search(r'\*\*Keywords:\*\*\s*(.*?)\n', txt)
if kw:
    kws=[k.strip() for k in kw.group(1).split(';') if k.strip()]
    print("KEYWORD COUNT:", len(kws), kws)
