"""Immutable versioning for the manuscript (and the master plan).

The revision (and the master) evolve. To honour "always create a new version, never
overwrite an earlier one", every edit produces a *new* versioned file under a
`versioned/` directory; the live working path stays as a pointer to the latest.

Layout
------
`data/revisions/IMPLEMENTED_revision_ECOMOD_v<N>.md`   (immutable snapshots)
`data/revisions/MASTER_joint_assessment_..._v<N>.md`   (immutable snapshots)
`data/revisions/CHANGELOG.md`                           (version history / provenance)
`VERSION`                                               (current version number)
"""
import json
import re
from pathlib import Path
from datetime import datetime


def _next_version(root: Path, stem: str) -> int:
    """Largest existing `_v<N>_` number for `stem` plus one."""
    rev_dir = root / "data" / "revisions"
    if not rev_dir.exists():
        return 1
    pat = re.compile(re.escape(stem) + r"_v(\d+)")
    mx = 0
    for p in rev_dir.glob(stem + "_v*.md"):
        m = pat.search(p.name)
        if m:
            mx = max(mx, int(m.group(1)))
    return mx + 1


def snapshot(root: Path, which="revision", note="") -> dict:
    """Copy the live `which` file into an immutable versioned snapshot. Returns metadata."""
    if which == "revision":
        live = root / "data" / "IMPLEMENTED_revision_ECOMOD.md"
        stem = "IMPLEMENTED_revision_ECOMOD"
    elif which == "master":
        live = root / "data" / "MASTER_joint_assessment_and_implementation_plan.md"
        stem = "MASTER_joint_assessment_and_implementation_plan"
    else:
        raise ValueError(f"unknown `which`={which!r}")
    if not live.exists():
        return {"ok": False, "error": f"{live} not found"}
    rev_dir = root / "data" / "revisions"
    rev_dir.mkdir(parents=True, exist_ok=True)
    ver = _next_version(root, stem)
    dst = rev_dir / f"{stem}_v{ver}.md"
    dst.write_text(live.read_text(encoding="utf-8"), encoding="utf-8")
    stamp = datetime.utcnow().isoformat() + "Z"
    changelog = rev_dir / "CHANGELOG.md"
    if not changelog.exists():
        changelog.write_text("# Revision / Master changelog\n\n", encoding="utf-8")
    with open(changelog, "a", encoding="utf-8") as f:
        f.write(f"- **{which} v{ver}** ({stamp}): {note or 'snapshot'}\n")
    return {"ok": True, "which": which, "version": ver, "path": str(dst), "timestamp": stamp}


def log_release(root: Path, sig: dict) -> None:
    """Record a human-readable release note in the changelog."""
    rev_dir = root / "data" / "revisions"
    rev_dir.mkdir(parents=True, exist_ok=True)
    changelog = rev_dir / "CHANGELOG.md"
    if not changelog.exists():
        changelog.write_text("# Revision / Master changelog\n\n", encoding="utf-8")
    if sig.get("release"):
        with open(changelog, "a", encoding="utf-8") as f:
            f.write(f"\n## Release note — {datetime.utcnow().isoformat()+'Z'}\n")
            for k, v in sig["release"].items():
                f.write(f"- **{k}:** {v}\n")
            f.write("\n")
