#!/usr/bin/env python3
"""
Render the lecture/exercise slide pages that the textbook quotes verbatim.

The manifest (docs/udzbenik/slides/manifest.tsv) is the source of truth and is
committed; the PNGs are derived and can always be regenerated:

    python src/extract_slides.py

Manifest columns (tab separated, '#' starts a comment):

    id      pdf_basename        page    crop
    p03-kkt 03_Uvjeti_optimalnosti  59  -
    v3-tbl  Vjezbe 3            24      0,0.12,1,0.75

`page` is the PDF page number, NOT the slide number printed on the slide —
beamer overlays make the two differ. `crop` is x,y,w,h as fractions of the
page, or '-' for the whole page.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LECTURES = ROOT / "data" / "sources" / "lectures"
SLIDES = ROOT / "docs" / "udzbenik" / "slides"
SCAN = ROOT / "docs" / "udzbenik" / "zadatak"
JOBS = [SLIDES / "manifest.tsv", SCAN / "manifest.tsv"]
DPI = 200


def page_size_px(pdf: Path, page: int) -> tuple[int, int]:
    out = subprocess.run(
        ["pdfinfo", "-f", str(page), "-l", str(page), str(pdf)],
        capture_output=True, text=True, check=True).stdout
    # "Page size: 596 x 841 pts (A4)" or, with -f/-l, "Page  1 size: 596 x 841 pts".
    m = re.search(r"size:\s+([\d.]+)\s+x\s+([\d.]+)\s+pts", out)
    if not m:
        raise RuntimeError(f"cannot read page size of {pdf} p{page}")
    w_pt, h_pt = float(m.group(1)), float(m.group(2))
    return round(w_pt * DPI / 72), round(h_pt * DPI / 72)


def resolve_pdf(pdf_name: str) -> Path:
    """A name with a slash is a path from the repo root; otherwise a lecture."""
    return (ROOT / pdf_name) if "/" in pdf_name else (LECTURES / f"{pdf_name}.pdf")


def render(out_dir: Path, entry_id: str, pdf_name: str, page: int, crop: str) -> Path:
    pdf = resolve_pdf(pdf_name)
    if not pdf.exists():
        raise FileNotFoundError(pdf)
    out_root = out_dir / entry_id
    cmd = ["pdftocairo", "-png", "-r", str(DPI), "-f", str(page), "-l", str(page)]
    if crop and crop != "-":
        fx, fy, fw, fh = (float(v) for v in crop.split(","))
        pw, ph = page_size_px(pdf, page)
        cmd += ["-x", str(round(fx * pw)), "-y", str(round(fy * ph)),
                "-W", str(round(fw * pw)), "-H", str(round(fh * ph))]
    cmd += ["-singlefile", str(pdf), str(out_root)]
    subprocess.run(cmd, check=True)
    return out_root.with_suffix(".png")


def run_manifest(manifest: Path) -> int:
    if not manifest.exists():
        print(f"  (no manifest at {manifest}, skipped)")
        return 0
    out_dir = manifest.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    n = 0
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        cols = [c.strip() for c in line.split("\t") if c.strip()]
        if len(cols) < 3:
            print(f"skipping malformed line: {raw}", file=sys.stderr)
            continue
        entry_id, pdf_name, page = cols[0], cols[1], int(cols[2])
        crop = cols[3] if len(cols) > 3 else "-"
        png = render(out_dir, entry_id, pdf_name, page, crop)
        print(f"  {entry_id:<24} <- {pdf_name} p{page:<4} -> {png.name}")
        n += 1
    print(f"  {n} page(s) rendered into {out_dir}")
    return n


def main() -> int:
    for manifest in JOBS:
        print(f"[{manifest.parent.name}]")
        run_manifest(manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
