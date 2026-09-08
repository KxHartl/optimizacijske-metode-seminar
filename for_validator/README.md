# Independent verification package

> **Course:** Optimization Methods in System Development and Control (OMRiUS)
>
> **Student:** Krešimir Hartl
>
> **Supervisor:** Prof. Andrej Jokić, PhD
>
> **Institution:** University of Zagreb, Faculty of Mechanical Engineering and Naval Architecture
>
> **Report version:** v1.6, 30 physical PDF pages

The PDF consists of the title page, two pages of the original assignment scan,
the table of contents, and 26 numbered seminar pages. The assignment scan is the
only document appended to the seminar.

## Package contents

```text
for_validator/
├── 01_TASK/                              original assignment and transcription
├── 02_REPORT_PDF/                        submission-ready v1.6 PDF
├── 03_LATEX_SOURCE/                      synchronized LaTeX source and figures
├── 04_SOURCE_CODE/matlab/                MATLAB source of all numerical results
├── 05_VERIFICATION_AND_BENCHMARKS/
│   ├── BENCHMARK_RESULTS.md              numerical cross-checks
│   ├── DEFENSE_QA_PACKAGE.md             concise oral-defense questions and answers
│   └── matlab_output/                    literal output of all four MATLAB tasks
└── omrius_recenzija_*.md                 historical independent reviews of v1.0
```

## Reproduction

The scripts were verified with MATLAB R2025b and Optimization Toolbox. Task 4
also requires YALMIP and SDPT3 to be available on the MATLAB path.

```matlab
addpath(genpath('path/to/YALMIP'));
cd 04_SOURCE_CODE/matlab
run_all
```

`run_all.m` stops if a solver fails. When run from this package, it writes the
literal console output to `05_VERIFICATION_AND_BENCHMARKS/matlab_output/` and
exports the seven vector figures to `03_LATEX_SOURCE/figures/`. The same sources
in the repository write to `docs/code/` and `docs/figures/`.

## v1.6 review closure

- All requested subproblems are answered in the same order as the assignment.
- Claims about LMI objective selection, mesh refinement, local sensitivity,
  coefficient intervals, switched-system growth, and the off-diagonal product
  were corrected and narrowed to what is proved.
- The robust-QP figure now shows representative boundary realizations and one
  clearly marked robust feasible intersection, without shading all 100 samples.
- The road-leveling result distinguishes cross-sectional area
  `J [m²]` from volume `V = wJ [m³]` and reports the second divided difference
  in `m⁻¹`.
- Citations are limited to four locally available course PDFs. No inaccessible
  book citation remains.
- MATLAB R2025b reproduced the recorded values with `rng(42)`, including the
  robust solution, Monte Carlo counts, controller, and certified decay rate.
- The source, figures, console output, verification notes, and report PDF in
  this package are synchronized with v1.6.

Historical review files remain unchanged and refer to v1.0; they are not a
source of seminar content.
