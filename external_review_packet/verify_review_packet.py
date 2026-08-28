#!/usr/bin/env python3
"""External review packet — integrity verification.

Pins the SHA-256 of every artifact the packet lists (the nine paper drafts,
the register of record, the pending-publications register, the Paper 2 venue
memo, and the monograph working preprint) and checks the existence of the
validated-computation artifact set. Idempotent; run from the repository root:

    python3 external_review_packet/verify_review_packet.py

Exit 0 = the packet is intact (every pinned artifact matches its reviewed
revision). A failure means a listed artifact drifted after the packet was
frozen — re-pin (and note the revision in the packet README) before the
packet is circulated.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- pins
PINS = [
    # The five core papers (final drafts)
    ("papers/paper1_general_theory/manuscript.md",
     "dc568ef4192d5aacd4a89028ce750d5078a957273af308ffe7e23cf859c20736"),
    ("papers/paper2_theorem_atlas/manuscript.md",
     "2404081fda7e17ea718ba5c92dcf19e6e0389a5f147131ed1a07de10d0ae841a"),
    ("papers/paper3_material_ledgers/manuscript.md",
     "d593c6f87ad340ebcea4c41fb77b82818348d7bbfb4149422f553cb26808d07b"),
    ("papers/paper4_delay_dynamics/manuscript.md",
     "f807993a1636029a0b7da689a19b2a25396f360ca4286525766d131171a5dfb9"),
    ("papers/paper5_sampled_governance/manuscript.md",
     "edb8eac3f4d1ef149a5d9e60c72464d2d8650bb36451ad3ae8330b786079308d"),
    # The four Wave E papers (final drafts; hashes identical to the
    # PROOF_MANIFEST Part VI pins)
    ("wave_e_cod/manuscript/wave_E_cod_forecast_ladder.md",
     "b5a5a43b47d43e93d3ed657a0e22c639611145866e665003d86f5ad1f38d3ce5"),
    ("wave_e_cod/manuscript/wave_E_cod_intervention.md",
     "46d55eadad8014a3a545219380a2f4f6d22a02016d15c850025afa230dc53353"),
    ("wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder.md",
     "f6ebe9422020177d8d791e9c7877857ebc381f83abb52eef1bf5bacfc9fb0c09"),
    ("wave_e_edwards/manuscript/wave_E_edwards_intervention.md",
     "09fd1b88c99fbf46cbd0b3f0f103d8a3f431799bb755a0b47a3a767e43bd7a34"),
    # The register of record and the programme registers
    ("PROOF_MANIFEST.md",
     "2d0cdcfed54f61cadb654edd9aaa9fc6f8c535027e54380f6139da50467bd5aa"),
    ("research_program/pending_separate_publications_register.md",
     "4fd5e0c48e6daa22890d9508da446c7d5a865213f626ed81cd7e11cc1f47484f"),
    ("research_program/paper2_venue_and_split_recommendation.md",
     "78e9bab239c90acddfb327ed412b6c17f6fcdc1953829c4d527c68603c927990"),
    # The monograph working preprint (context document, §1.3 / §5)
    ("revised_sustainability_manuscript.md",
     "092cbeb0aacc43133cc302f73148ef1ddce25eecb85cc20eb7dbad00faeb3343"),
]

# Validated-computation artifact set (existence check; the content hashes
# are pinned and verified by reaudit/verify_validated_computations.py and
# PROOF_MANIFEST.md Part II — this layer only asserts the packet's listing)
VC = "research_program/validated_computations"
ARTIFACTS = [
    f"{VC}/a025_fold/a025_interval_hopf.py",
    f"{VC}/a021_c4/c4_orbit_krawczyk.py",
    f"{VC}/a021_c4/c4_orbit_krawczyk_certificate.json",
    f"{VC}/a021_c4/c4_offgrid_interval_v2.py",
    f"{VC}/a021_c4/c4_offgrid_residual_interval.json",
    f"{VC}/a021_c4/c4_monodromy.py",
    f"{VC}/a021_c4/c4_monodromy_enclosure.json",
    f"{VC}/a021_c4/c4_monodromy_dt0p1_enclosure.json",
    f"{VC}/a021_c4/b4_t2_binding_product_certificate.py",
    f"{VC}/a021_c4/b4_t2_binding_product_certificate.json",
    f"{VC}/a021_c4/b4_t3_slack_semigroup_certificate.py",
    f"{VC}/a021_c4/b4_t3_slack_semigroup_certificate.json",
    f"{VC}/a021_c4/b4_t4_prefactor_certificate.py",
    f"{VC}/a021_c4/b4_t4_prefactor_certificate.json",
    f"{VC}/a021_c4/b4_t5_assembly_certificate.py",
    f"{VC}/a021_c4/b4_t5_assembly_certificate.json",
    f"{VC}/e5_admission.py",
    f"{VC}/E5_NUMBERS.json",
    f"{VC}/interval_lib.py",
    f"{VC}/ARTIFACT_MANIFESTS.json",
]

# --------------------------------------------------------------- checks
def sha(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()

fails = []

print("EXTERNAL REVIEW PACKET — integrity check")
print("=" * 72)
print("[1] Pinned artifacts (SHA-256)")
for rel, want in PINS:
    p = ROOT / rel
    if not p.exists():
        fails.append(f"missing: {rel}")
        print(f"  [FAIL] missing   :: {rel}")
        continue
    got = sha(p)
    if got == want:
        print(f"  [OK ] match      :: {rel}")
    else:
        fails.append(f"drift: {rel}")
        print(f"  [FAIL] DRIFT     :: {rel}")
        print(f"         pinned  {want}")
        print(f"         current {got}")

print("[2] Validated-computation artifact set (existence)")
for rel in ARTIFACTS:
    p = ROOT / rel
    if p.exists():
        print(f"  [OK ] present    :: {rel}")
    else:
        fails.append(f"missing artifact: {rel}")
        print(f"  [FAIL] absent    :: {rel}")

print("[3] Wave E Part VI pin cross-check (packet pin == manifest pin)")
manifest = (ROOT / "PROOF_MANIFEST.md").read_text()
wave_e = [r for r, _ in PINS if r.startswith("wave_e_")]
for rel in wave_e:
    got = sha(ROOT / rel)
    if got in manifest:
        print(f"  [OK ] manifest carries the same pin :: {rel}")
    else:
        fails.append(f"manifest pin mismatch: {rel}")
        print(f"  [FAIL] manifest does not carry pin  :: {rel}")

print("=" * 72)
if fails:
    print(f"REVIEW PACKET NOT INTACT — {len(fails)} problem(s):")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
print("REVIEW PACKET INTACT: all pinned artifacts match their reviewed "
      "revision; artifact set complete.")
sys.exit(0)
