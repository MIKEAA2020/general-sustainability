"""Immutable versioning for the manuscript (and the master plan).

The revision (and the master) evolve. To honour "always create a new version, never
overwrite an earlier one", every edit produces a *new* immutable file under
`data/revisions/`; the live working path (`data/IMPLEMENTED_revision_ECOMOD.md`) is a
**symlink pointer** to the latest version, so manuscript content is never rewritten in
the live path — only the pointer moves to a new `_v<N>.md`.

Workflow
--------
1. `start_revision(root, which, note)`   — copy the latest version into a brand-new
   `_v<next>.md` and point the live link at it. This is the ONLY thing that advances
   the version number (so a new version is created BEFORE you edit).
2. Edit `data/revisions/<stem>_v<next>.md` directly (the immutable file being built).
3. `snapshot`/`bump` is thus deprecated; the history advances only via `start_revision`.

Layout
------
`data/revisions/IMPLEMENTED_revision_ECOMOD_v<N>.md`   (immutable snapshots)
`data/revisions/MASTER_joint_assessment_..._v<N>.md`   (immutable snapshots)
`data/revisions/CHANGELOG.md`                           (version history / provenance)
`VERSION`                                               (current version number)
`data/<live>.md`                                        (SYMLINK -> revisions/<stem>_v<N>.md)
"""
import re
from pathlib import Path
from datetime import datetime


def _live(root: Path, which: str):
    if which == "revision":
        return root / "data" / "IMPLEMENTED_revision_ECOMOD.md", "IMPLEMENTED_revision_ECOMOD"
    if which == "master":
        return root / "data" / "MASTER_joint_assessment_and_implementation_plan.md", \
            "MASTER_joint_assessment_and_implementation_plan"
    raise ValueError(f"unknown `which`={which!r}")


def _rev_dir(root: Path) -> Path:
    return root / "data" / "revisions"


def _next_version(root: Path, stem: str) -> int:
    rev_dir = _rev_dir(root)
    if not rev_dir.exists():
        return 1
    pat = re.compile(re.escape(stem) + r"_v(\d+)")
    mx = 0
    for p in rev_dir.glob(stem + "_v*.md"):
        m = pat.search(p.name)
        if m:
            mx = max(mx, int(m.group(1)))
    return mx + 1


def _latest_version(root: Path, stem: str) -> int:
    return max(0, _next_version(root, stem) - 1)


def _version_path(root: Path, stem: str, ver: int) -> Path:
    return _rev_dir(root) / f"{stem}_v{ver}.md"


def _read_version(root: Path, stem: str, ver: int) -> str:
    if ver <= 0:
        return ""
    p = _version_path(root, stem, ver)
    return p.read_text(encoding="utf-8") if p.exists() else ""


def _write_changelog(root: Path, which: str, ver: int, note: str) -> str:
    rev_dir = _rev_dir(root)
    rev_dir.mkdir(parents=True, exist_ok=True)
    changelog = rev_dir / "CHANGELOG.md"
    stamp = datetime.utcnow().isoformat() + "Z"
    if not changelog.exists():
        changelog.write_text("# Revision / Master changelog\n\n", encoding="utf-8")
    with open(changelog, "a", encoding="utf-8") as f:
        f.write(f"- **{which} v{ver}** ({stamp}): {note or 'snapshot'}\n")
    return stamp


def _write_version_pointer(root: Path, which: str, ver: int) -> None:
    vf = root / "VERSION"
    existing = {}
    if vf.exists():
        for line in vf.read_text(encoding="utf-8").splitlines():
            if "=" in line:
                k, v = line.split("=", 1)
                existing[k.strip()] = v.strip()
    existing[which] = str(ver)
    vf.write_text("\n".join(f"{k}={v}" for k, v in existing.items()) + "\n", encoding="utf-8")


def _repoint_live(root: Path, which: str, ver: int) -> Path:
    """Point the live `<stem>.md` at `revisions/<stem>_v<ver>.md` as a symlink."""
    live, stem = _live(root, which)
    target = f"revisions/{stem}_v{ver}.md"
    live.parent.mkdir(parents=True, exist_ok=True)
    if live.is_symlink() or live.exists():
        live.unlink()
    live.symlink_to(target)
    return live


def start_revision(root: Path, which="revision", note="", force=False) -> dict:
    """Create a NEW immutable version `_v<next>.md` as a copy of the latest, point the
    live link at it, and record VERSION + CHANGELOG.

    This is the ONLY operation that advances the version number, so a distinct version
    file is created for every revision and no earlier version is ever overwritten.
    If `force` is False and the live link already points at a version that differs from
    the latest *and* is already the top version, we still create a new one (a revision
    always gets its own file). Consumers wanting a no-op guard set `force=True` to skip
    when the content is unchanged since the previous version."""
    live, stem = _live(root, which)
    _rev_dir(root).mkdir(parents=True, exist_ok=True)
    ver = _next_version(root, stem)
    latest = _latest_version(root, stem)
    if not force:
        # If live already targets a version and content matches the latest, do not churn.
        if live.is_symlink() and _read_version(root, stem, latest) and \
                live.read_text(encoding="utf-8") == _read_version(root, stem, latest) and ver == latest + 1:
            return {"ok": True, "which": which, "version": latest,
                    "path": str(_version_path(root, stem, latest)), "skipped": True,
                    "reason": "live already points at the latest version"}
    dst = _version_path(root, stem, ver)
    seed = _read_version(root, stem, latest) or (live.read_text(encoding="utf-8") if live.exists() and not live.is_symlink() else "")
    dst.write_text(seed, encoding="utf-8")
    _write_changelog(root, which, ver, note or "new revision")
    _write_version_pointer(root, which, ver)
    _repoint_live(root, which, ver)
    return {"ok": True, "which": which, "version": ver, "path": str(dst), "skipped": False}


def snapshot(root: Path, which="revision", note="") -> dict:
    """Forward-compat alias for `start_revision` (a new version is always created)."""
    return start_revision(root, which, note, force=False)


def log_release(root: Path, sig: dict) -> None:
    rev_dir = _rev_dir(root)
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
