#!/usr/bin/env python3
"""
Build script for OMRiUS University Textbook & Oral Defense Guide PDF.
Converts docs/UDZBENIK_OMRIUS_PRIPREMA_OBRANE.md into a high-quality PDF
using pandoc and tectonic with academic typographic styling.
"""

import os
import re
import subprocess
import sys

def sanitize_markdown(content: str) -> str:
    """Replace emojis and non-standard unicode characters with clean LaTeX/Markdown equivalents."""
    replacements = [
        ("❓", "**[Ispitno pitanje]** "),
        ("⚠️", "**[PAŽNJA / ZAMKA]** "),
        ("💡", "**[Inženjerski uvid]** "),
        ("🔴", "**[KLJUČNI ISPITNI NALAZ]** "),
        ("👑", "**[Krunski teorem]** "),
        ("📚", ""),
        ("🧭", ""),
        ("🛠️", ""),
        ("🎯", ""),
        ("📖", ""),
        ("🗺️", ""),
        ("❌", "[NEISPRAVNO] "),
        ("✅", "[TOČNO] "),
        ("👉", ""),
        ("⧵", "\\setminus "),
    ]
    for orig, repl in replacements:
        content = content.replace(orig, repl)
    
    # Remove any remaining lone surrogates or stray emoji codes if any
    content = re.sub(r'[\U00010000-\U0010ffff]', '', content)
    return content

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root_dir)

    md_source = os.path.join(root_dir, "docs", "UDZBENIK_OMRIUS_PRIPREMA_OBRANE.md")
    build_dir = os.path.join(root_dir, "docs", "build")
    os.makedirs(build_dir, exist_ok=True)
    
    dist_dir = os.path.join(root_dir, "dist", "v1.2")
    os.makedirs(dist_dir, exist_ok=True)

    print(f"Reading {md_source}...")
    with open(md_source, "r", encoding="utf-8") as f:
        raw_md = f.read()

    sanitized_md = sanitize_markdown(raw_md)
    temp_md = os.path.join(build_dir, "udzbenik_sanitized.md")
    with open(temp_md, "w", encoding="utf-8") as f:
        f.write(sanitized_md)

    header_tex = os.path.join(build_dir, "udzbenik_header.tex")
    header_content = r"""
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{booktabs}
\usepackage{microtype}
\usepackage{xcolor}

\definecolor{fsbblue}{RGB}{0, 51, 102}
\definecolor{linkblue}{RGB}{0, 80, 160}

\pagestyle{fancy}
\fancyhf{}
\setlength{\headheight}{14pt}
\fancyhead[L]{\small\itshape Krešimir Hartl}
\fancyhead[R]{\small\itshape OMRiUS — Sveučilišni udžbenik i ispitni vodič}
\fancyfoot[L]{\small\itshape Fakultet strojarstva i brodogradnje, Sveučilište u Zagrebu}
\fancyfoot[R]{\small\bfseries\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{fsbblue}}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{fsbblue}}{\thesection.}{0.5em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries}{\thesubsection.}{0.5em}{}
\titleformat{\subsubsection}
  {\normalfont\normalsize\bfseries\itshape}{\thesubsubsection.}{0.5em}{}

\titlespacing*{\section}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
\titlespacing*{\subsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
"""
    with open(header_tex, "w", encoding="utf-8") as f:
        f.write(header_content)

    tex_out = os.path.join(build_dir, "udzbenik_final.tex")
    print(f"Running pandoc to create {tex_out}...")
    pandoc_cmd = [
        "pandoc",
        temp_md,
        "-s",
        "-o", tex_out,
        "--toc",
        "--toc-depth=3",
        "--include-in-header=" + header_tex,
        "-V", "geometry:margin=2.5cm",
        "-V", "documentclass=report",
        "-V", "lang=hr",
        "-V", "title=OPTIMIZACIJSKE METODE U RAZVOJU I UPRAVLJANJU SUSTAVA",
        "-V", "subtitle=Sveučilišni udžbenik, teorijski vodič i priručnik za pripremu usmene obrane i ispita",
        "-V", "author=Krešimir Hartl (mentor: Prof. dr. sc. Andrej Jokić)",
        "-V", "date=Rujan 2026. | Verzija v1.2"
    ]
    
    res = subprocess.run(pandoc_cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if res.returncode != 0:
        print("Pandoc failed:", res.stderr)
        sys.exit(1)
    print("Pandoc generated tex successfully.")

    print("Running tectonic compilation...")
    tectonic_cmd = [
        "tectonic",
        "-X", "compile",
        tex_out,
        "--outdir", build_dir,
        "--keep-logs"
    ]
    res_tec = subprocess.run(tectonic_cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if res_tec.returncode != 0:
        print("Tectonic compilation error:", res_tec.stderr)
        print("Output:", res_tec.stdout)
        sys.exit(1)

    generated_pdf = os.path.join(build_dir, "udzbenik_final.pdf")
    if not os.path.exists(generated_pdf):
        print("Error: generated PDF not found at", generated_pdf)
        sys.exit(1)

    dist_pdf = os.path.join(dist_dir, "OMRiUS_udzbenik_priprema_obrane.pdf")
    docs_pdf = os.path.join(root_dir, "docs", "UDZBENIK_OMRIUS_PRIPREMA_OBRANE.pdf")

    import shutil
    shutil.copy2(generated_pdf, dist_pdf)
    shutil.copy2(generated_pdf, docs_pdf)

    file_size_kb = os.path.getsize(dist_pdf) / 1024.0
    print(f"SUCCESS! Output PDF generated:")
    print(f"  -> {dist_pdf} ({file_size_kb:.1f} KB)")
    print(f"  -> {docs_pdf}")

if __name__ == "__main__":
    main()
