#!/usr/bin/env python3
"""
Build docs/udzbenik/udzbenik.tex into a PDF with Tectonic (XeTeX).

    python src/build_udzbenik.py

Output: docs/udzbenik/build/udzbenik.pdf, copied to
        dist/<version>/OMRiUS_udzbenik_v2.pdf

Deliberately separate from .ai/scripts/helpers/build-docs.ps1: that script
compiles every top-level docs/*.tex and warns above project.yaml's max_pages
(30), a limit that applies to the seminar, not to a textbook.
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "udzbenik"
TEX = SRC / "udzbenik.tex"
BUILD = SRC / "build"
VERSION = "v1.2"
DIST_NAME = "OMRiUS_udzbenik_v2.pdf"

# LaTeX warnings that matter for this document.
NOISE = re.compile(r"Missing character|Undefined control sequence|"
                   r"LaTeX Error|Emergency stop|File .* not found")


def ensure_images() -> None:
    """Slide and scan PNGs are derived and gitignored; render whatever is
    missing before the LaTeX run so a fresh clone builds in one command."""
    import extract_slides
    for manifest in extract_slides.JOBS:
        if not manifest.exists():
            continue
        for raw in manifest.read_text(encoding="utf-8").splitlines():
            line = raw.split("#", 1)[0].strip()
            if not line:
                continue
            entry_id = line.split("	")[0].strip()
            if not (manifest.parent / f"{entry_id}.png").exists():
                print("rendering missing images ...")
                extract_slides.main()
                return


def main() -> int:
    if not TEX.exists():
        print(f"missing {TEX}", file=sys.stderr)
        return 1
    BUILD.mkdir(parents=True, exist_ok=True)
    ensure_images()

    cmd = ["tectonic", "-X", "compile", str(TEX),
           "--outdir", str(BUILD), "--keep-logs"]
    print(" ".join(cmd))
    res = subprocess.run(cmd, cwd=SRC, capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    sys.stdout.write(res.stdout)
    if res.returncode != 0:
        sys.stderr.write(res.stderr)
        return res.returncode
    # Tectonic reports warnings on stderr even on success.
    for line in res.stderr.splitlines():
        if "warning" in line.lower():
            print(line)

    pdf = BUILD / "udzbenik.pdf"
    if not pdf.exists():
        print("tectonic reported success but produced no PDF", file=sys.stderr)
        return 1

    log = BUILD / "udzbenik.log"
    if log.exists():
        hits = [l for l in log.read_text(encoding="utf-8", errors="replace").splitlines()
                if NOISE.search(l)]
        if hits:
            print(f"\n{len(hits)} log line(s) worth checking:")
            for h in hits[:25]:
                print("  " + h.strip())

    pages = "?"
    try:
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                              text=True, check=True).stdout
        pages = next(l.split()[1] for l in info.splitlines() if l.startswith("Pages"))
    except Exception:
        pass

    dist = ROOT / "dist" / VERSION
    dist.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(pdf, dist / DIST_NAME)
        dest = dist / DIST_NAME
    except PermissionError:          # PDF open in a viewer
        dest = dist / DIST_NAME.replace(".pdf", "_latest.pdf")
        shutil.copy2(pdf, dest)

    print(f"\nOK — {pages} pages -> {pdf.relative_to(ROOT)} and {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
