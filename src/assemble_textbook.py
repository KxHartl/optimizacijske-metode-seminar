#!/usr/bin/env python3
"""
Assemble Master Textbook: docs/UDZBENIK_OMRIUS_PRIPREMA_OBRANE.md
Concatenates README preface and Chapters 00 to 10 from docs/textbook/
with appropriate image path resolution and formatting.
"""

import os

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    textbook_dir = os.path.join(root_dir, "docs", "textbook")
    output_md = os.path.join(root_dir, "docs", "UDZBENIK_OMRIUS_PRIPREMA_OBRANE.md")

    readme_file = os.path.join(textbook_dir, "README.md")
    with open(readme_file, "r", encoding="utf-8") as f:
        readme_content = f.read()

    chapter_files = [
        "00_matematicki_rjecnik_i_govorni_vodic.md",
        "01_temelji_i_konveksnost.md",
        "02_uvjeti_optimalnosti_i_kkt.md",
        "03_dualnost_i_osjetljivost.md",
        "04_robusna_optimizacija.md",
        "05_modeliranje_ceste_i_diskretizacija.md",
        "06_lp_i_l1_aproksimacija.md",
        "07_stabilnost_i_sklopni_sustavi.md",
        "08_lmi_robusna_stabilizacija.md",
        "09_konicno_programiranje_i_schur.md",
        "10_vodic_za_usmenu_obranu.md",
    ]

    parts = [readme_content]

    for fname in chapter_files:
        fpath = os.path.join(textbook_dir, fname)
        if not os.path.exists(fpath):
            print(f"Warning: {fpath} does not exist!")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        # In docs/UDZBENIK_OMRIUS_PRIPREMA_OBRANE.md, path to figures is figures/...
        content = content.replace("../figures/", "figures/")
        parts.append("\n\n\\newpage\n\n---\n\n" + content)

    full_content = "\n".join(parts)

    with open(output_md, "w", encoding="utf-8") as f:
        f.write(full_content)

    file_size_kb = len(full_content.encode("utf-8")) / 1024.0
    print(f"Successfully assembled {output_md}")
    print(f"Total size: {len(full_content)} characters ({file_size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
