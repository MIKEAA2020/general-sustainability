"""End-to-end certificate protocol demonstration.

Produces the three certificate families, round-trips them through the
package's serializer, hands them to the *independent* checker (a separate
stdlib-only script sharing no code with the package), and demonstrates that
tampered certificates are rejected. Run from the repository root:

    PYTHONPATH=src python3 examples/certificates_demo.py
"""
import json
import os
import subprocess
import sys
import tempfile

from safetransition import (FarkasCertificate, benchmark_certificate,
                            certify_polyhedron, weight_partition)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHECKER = os.path.join(ROOT, "check_safe_transition_cert.py")

print("== 1. produce certificates ==")
farkas = certify_polyhedron([[1], [-1]], ["2/5", "-3/5"]).certificate.to_dict()
partition = weight_partition()
bench = benchmark_certificate()
print(f"  farkas margin: {-sum(FarkasCertificate.from_dict(farkas).lam[i] * FarkasCertificate.from_dict(farkas).b[i] for i in range(2))}")

print("== 2. independent checker (shares no package code) ==")
with tempfile.TemporaryDirectory() as tmp:
    paths = []
    for name, cert in (("farkas.json", farkas),
                       ("partition.json", partition),
                       ("benchmark.json", bench)):
        p = os.path.join(tmp, name)
        json.dump(cert, open(p, "w"))
        paths.append(p)
    res = subprocess.run([sys.executable, CHECKER, *paths],
                         capture_output=True, text=True)
    print(res.stdout.rstrip())
    assert res.returncode == 0, res.stdout + res.stderr

    print("== 3. tamper rejection ==")
    bad = json.loads(json.dumps(farkas)); bad["b"][0] = "3/5"
    p = os.path.join(tmp, "bad.json"); json.dump(bad, open(p, "w"))
    res = subprocess.run([sys.executable, CHECKER, p],
                         capture_output=True, text=True)
    print("  " + res.stdout.strip().splitlines()[0])
    assert res.returncode != 0

print("protocol demonstration complete.")
