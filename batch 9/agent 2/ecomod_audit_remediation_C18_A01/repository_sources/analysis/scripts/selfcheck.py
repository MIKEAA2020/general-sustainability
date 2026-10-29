import re
rev=open("IMPLEMENTED_revision_ECOMOD.md").read()
print("== MASKING consistency ==")
print("  'narrow' count:", rev.lower().count("narrow"))
pp=[l.strip() for l in rev.split('\n') if 'generic' in l.lower() and 'mask' in l.lower()]
print("  mask+generic lines:")
for l in pp: print("   -",l[:120])
print("\n== numbers that should co-occur ==")
checks=[("basin 0.506 & 0.042",["0.506","0.042"]),("basin 0.506 & 0.044",["0.506","0.044"]),
        ("mask 5.4 & 0.075",["5.4","0.075"]),("B/C M~1.19",["1.19"]),("tau_g 85.4",["85.4"]),
        ("tau_p 231",["231"]),("D_E 5.26",["5.26"]),("equil M*=0.74",["0.740","0.74"])]
for label,vals in checks:
    print(f"  {label}: {[v for v in vals if v in rev]}")
abstract=rev[:rev.index("## 2.")]; sec10=rev[rev.index("## 10."):rev.index("## 11.")]
print("\n== ABSTRACT vs §10 ==")
for phrase in ["small initial deficit","narrow","~5 yr","8 % overshoot"]:
    print(f"  '{phrase}': abstract={'Y' if phrase in abstract else 'N'}  sec10={'Y' if phrase in sec10 else 'N'}")
print("\n== ORIGINAL-MODEL provenance labelling ==")
for kw in ["original model","original-model","original manuscript","legacy","original S0","gross-depletion"]:
    print(f"  '{kw}': {rev.lower().count(kw.lower())}")
print("\n  lines containing '0.506':")
for l in rev.split('\n'):
    if '0.506' in l: print("   -",l.strip()[:140])
print("\n  lines containing '0.505' (should be none) or '0.506' context:")
for l in rev.split('\n'):
    if '0.505' in l or 'stable fraction' in l: print("   -",l.strip()[:120])
