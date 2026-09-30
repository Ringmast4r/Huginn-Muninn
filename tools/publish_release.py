#!/usr/bin/env python3
"""Publish the Huginn-Muninn master database as a GitHub Release asset.

The master (1.5 GB, refreshed daily on CT 152) cannot live in git - GitHub refuses files over
100 MB - so it is published as a release asset instead: releases allow 2 GB per file, are served
from a CDN with no bandwidth quota, and do not grow the repository history.

  data-latest          rolling release; its asset is replaced on every run
  data-YYYY-MM-DD      dated release, created on the first of each month (or with --tag)

Runs on the workstation, where gh is signed in (unset GH_TOKEN first; the keyring token is the
good one). Needs ssh access to the Proxmox host to pull the file out of CT 152.

Usage: py -3.13 tools/publish_release.py [--dated] [--keep]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = "Ringmast4r/Huginn-Muninn"
PVE = "root@10.0.0.245"
CT = "152"
MASTER_ON_CT = "/opt/huginn-muninn/database/huginn_muninn_master.db"
ASSET = "huginn_muninn_master.db"


def sh(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    env = {k: v for k, v in os.environ.items() if k not in ("GH_TOKEN", "GITHUB_TOKEN")}
    return subprocess.run(list(args), check=check, text=True, capture_output=True, env=env)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dated", action="store_true", help="also create the dated data-YYYY-MM-DD release")
    ap.add_argument("--keep", action="store_true", help="keep the downloaded copy in the temp dir")
    args = ap.parse_args()

    work = Path(tempfile.gettempdir()) / "huginn-release"
    work.mkdir(parents=True, exist_ok=True)
    local = work / ASSET
    print("pulling the master from CT 152 ...")
    sh("ssh", "-n", PVE, f"pct pull {CT} {MASTER_ON_CT} /root/{ASSET}")
    sh("scp", "-q", f"{PVE}:/root/{ASSET}", str(local))

    con = sqlite3.connect(f"file:{local}?mode=ro", uri=True)
    built = con.execute("SELECT * FROM generated_on").fetchone()[0]
    counts = {t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
              for t in ("dhcp_fingerprint", "dhcp_vendor", "dhcp6_fingerprint", "dhcp6_enterprise", "mac_vendor", "device")}
    con.close()
    built_iso = datetime.fromtimestamp(int(built), timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    digest = sha256(local)
    size_gb = local.stat().st_size / 1e9
    notes = (
        f"Fingerbank master database, upstream build {built_iso}.\n\n"
        f"Size {size_gb:.2f} GB, SHA-256 `{digest}`.\n\n"
        "Rows: " + ", ".join(f"{t} {n:,}" for t, n in counts.items()) + ".\n\n"
        "The per-table exports in the repository are cut from exactly this file; "
        "MANIFEST.json there carries the same build stamp."
    )
    (work / "RELEASE_NOTES.md").write_text(notes, encoding="utf-8")
    print(f"master: build {built_iso}, {size_gb:.2f} GB, sha256 {digest[:12]}...")

    today = datetime.now(timezone.utc)
    dated = args.dated or today.day == 1  # the scheduled daily run keeps one dated release per month
    tags = ["data-latest"] + ([f"data-{today:%Y-%m-%d}"] if dated else [])
    for tag in tags:
        exists = sh("gh", "release", "view", tag, "-R", REPO, check=False).returncode == 0
        if not exists:
            title = "Latest master database" if tag == "data-latest" else f"Master database {tag[5:]}"
            sh("gh", "release", "create", tag, "-R", REPO, "--title", title, "--notes-file", str(work / "RELEASE_NOTES.md"),
               "--latest=false" if tag != "data-latest" else "--latest")
            print(f"created release {tag}")
        else:
            sh("gh", "release", "edit", tag, "-R", REPO, "--notes-file", str(work / "RELEASE_NOTES.md"))
        print(f"uploading to {tag} ...")
        sh("gh", "release", "upload", tag, str(local), "-R", REPO, "--clobber")
        print(f"published {ASSET} to {tag}")
    if not args.keep:
        local.unlink(missing_ok=True)
    print(json.dumps({"build": built_iso, "sha256": digest, "tags": tags}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
