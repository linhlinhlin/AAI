"""Fetch pinned ITSP dataset and attribution using Git partial clone, not APR toolchains."""

import argparse
import hashlib
import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path

COMMIT = "0553f683f99403efb5ef440af826c1d229a52376"
REPOSITORY = "https://github.com/jyi/ITSP"


def git(repository, *args):
    return subprocess.run(
        ["git", "-c", "core.autocrlf=false", "-C", str(repository), *args],
        check=True,
        capture_output=True,
    ).stdout


def download(destination: Path):
    destination.mkdir(parents=True, exist_ok=True)
    cache = destination / "repository"
    if not cache.exists():
        subprocess.run(
            [
                "git",
                "-c",
                "core.autocrlf=false",
                "clone",
                "--filter=blob:none",
                "--no-checkout",
                "--depth",
                "1",
                REPOSITORY + ".git",
                str(cache),
            ],
            check=True,
        )
    try:
        git(cache, "cat-file", "-e", COMMIT)
    except subprocess.CalledProcessError:
        git(cache, "fetch", "--depth", "1", "origin", COMMIT)
    git(cache, "sparse-checkout", "set", "--no-cone", "/dataset/", "/README.md", "/LICENSE")
    git(cache, "checkout", COMMIT)
    entries = git(cache, "ls-tree", "-r", COMMIT, "--", "dataset", "README.md", "LICENSE")
    records = []
    # Read Git blobs, not checkout bytes: Windows autocrlf must not change provenance.
    paths = []
    for line in entries.decode().splitlines():
        meta, path = line.split("\t", 1)
        _, kind, oid = meta.split()
        if kind != "blob":
            raise ValueError(f"Unexpected tree entry: {line}")
        paths.append((path, oid))
    process = subprocess.run(
        ["git", "-C", str(cache), "cat-file", "--batch"],
        input=("\n".join(oid for _, oid in paths) + "\n").encode(),
        capture_output=True,
        check=True,
    )
    position = 0
    for path, oid in paths:
        end = process.stdout.index(b"\n", position)
        header = process.stdout[position:end].decode().split()
        size = int(header[2])
        data = process.stdout[end + 1 : end + 1 + size]
        position = end + size + 2
        digest = hashlib.sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest()
        if digest != oid:
            raise ValueError(f"Git blob hash mismatch: {path}")
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        records.append(
            {
                "path": path,
                "bytes": size,
                "git_blob_sha1": oid,
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    provenance = {
        "repository": REPOSITORY,
        "commit": COMMIT,
        "retrieved_at_utc": datetime.now(UTC).isoformat(),
        "scope": "dataset/**, README.md, LICENSE; no APR toolchains",
        "files": records,
    }
    (destination / "provenance.json").write_text(json.dumps(provenance, indent=2), encoding="utf-8")
    print(f"Verified {len(records)} files; {sum(x['bytes'] for x in records)} bytes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("data/raw/itsp"))
    download(parser.parse_args().output)
