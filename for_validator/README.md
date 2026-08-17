# Independent Validator & Reviewer Package

> **Course:** Optimization Methods in Systems Development and Control (OMRiUS)  
> **Student:** Krešimir Hartl  
> **Mentor:** Prof. Dr. Sc. Andrej Jokić  
> **Institution:** Faculty of Mechanical Engineering and Naval Architecture (FSB), University of Zagreb  
> **Project:** Master's Seminar — Optimization Methods & Control Systems  

---

## Overview

This standalone `/for_validator` folder contains all materials required for an independent academic, technical, and numerical audit of the seminar work. Every analytical derivation, numerical simulation, and graphical artifact is completely self-contained and reproducible.

---

## Directory Structure

```
for_validator/
├── 01_TASK/                                 # Original assignment specifications
│   ├── zadatak_omrius.md                   # Full markdown transcription with mathematical steps
│   └── Zadatak_OMRiUS_Kresimir_Hartl.pdf   # Original signed PDF task specification from professor
├── 02_REPORT_PDF/                           # Final compiled publication PDF
│   └── OMRiUS_seminar_Kresimir_Hartl.pdf   # 38-page complete academic report (FSB LaTeX format)
├── 03_LATEX_SOURCE/                         # Complete LaTeX source code and vector figures
│   ├── main.tex                            # Main document entry point
│   ├── references.bib                      # Bibliography (7 academic citations)
│   ├── chapters/                           # Individual chapter TeX sources (00 to 04 + conclusion)
│   └── figures/                            # 12 high-resolution vector PDF figures
├── 04_SOURCE_CODE/                          # Complete simulation & optimization code
│   ├── python/                             # Python implementation (scipy, cvxpy, matplotlib)
│   │   ├── run_all.py                      # Master batch runner (executes all 4 tasks)
│   │   ├── task1_qp_analysis.py            # Task 1: Convexity, KKT 4-case solver, Dual, Sensitivity
│   │   ├── task2_robust_qp.py              # Task 2: Robust QP, 8-vertex equivalent, Monte Carlo (100 runs)
│   │   ├── task3_road_leveling.py          # Task 3: Road leveling LP, Epigraph slacks, Cases A & B (N=20, 100)
│   │   ├── task4_lmi_switched_stabilization.py # Task 4: Switched system, Monodromy, LMI SDP synthesis
│   │   └── common/config_plot.py           # Publication plotting style and color schemes
│   └── matlab/                             # MATLAB implementation (quadprog, linprog, YALMIP)
│       ├── run_all.m                       # MATLAB master runner
│       ├── task1_qp_analysis.m             # Task 1 MATLAB solver
│       ├── task2_robust_qp.m               # Task 2 MATLAB solver
│       ├── task3_road_leveling.m           # Task 3 MATLAB solver
│       └── task4_lmi_switched_stabilization.m # Task 4 MATLAB solver
├── 05_VERIFICATION_AND_BENCHMARKS/          # Validation audits & defense resources
│   ├── BENCHMARK_RESULTS.md                # Numerical comparison table across analytical and solvers
│   └── DEFENSE_QA_PACKAGE.md               # 4 in-depth defense questions & theoretical justifications
├── requirements.txt                         # Python dependencies
└── README.md                               # This documentation file
```

---

## Quickstart: Running Numerical Verification

### Option A: Python (Recommended)

1. Ensure Python $\ge 3.10$ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the complete automated test and figure generation suite:
   ```bash
   python 04_SOURCE_CODE/python/run_all.py
   ```
   *(All 4 tasks will execute, verify tolerances $< 10^{-8}$, and regenerate publication figures)*.

### Option B: MATLAB / YALMIP

1. Open MATLAB.
2. Navigate to `04_SOURCE_CODE/matlab/`.
3. Run:
   ```matlab
   run_all
   ```

---

## Technical Summary of Solved Tasks

### 1. Task 1: Quadratic Programming, KKT Conditions, Dual & Sensitivity
* **Convexity:** Hessian $Q = \begin{bmatrix} 2 & -0.3 \\ -0.3 & 4 \end{bmatrix} \succ 0$ with $\lambda_1 \approx 1.956, \lambda_2 \approx 4.044 > 0 \implies$ Strictly convex.
* **KKT 4-Case Analysis:** Exhaustively checks all $2^2=4$ combinations.
  * **Optimum:** $x^* = \left(\frac{190}{33}, \frac{140}{33}\right) \approx (5.757576, 4.242424)$, $\mu_1^* = \frac{404}{33} \approx 12.242424$, $\mu_2^* = 0$, $p^* = \frac{2000}{33} \approx 60.606061$.
* **Lagrange Dual:** $g(\mu) = -\frac{1}{2}(c+A^T\mu)^T Q^{-1}(c+A^T\mu) - b^T\mu \implies$ Zero duality gap ($p^* = d^*$).
* **Sensitivity:** Verified $\frac{\partial p^*}{\partial b_1} = -\mu_1^* = -12.242424$ with numerical finite differences ($6.75 \times 10^{-5}$ error).

### 2. Task 2: Robust QP Under Interval Uncertainty ($\pm 15\%$)
* **Exact Worst-Case Formulation:** Semi-infinite constraints mapped to $2^2 \times 2 = 8$ extreme vertices of the rectangular uncertainty set.
* **Closed-Form Solution:** Active worst-case intersection:
  $$x_{\mathrm{rob}}^* = \left( \frac{13}{2}, \frac{179}{34} \right) = (6.500000, 5.264706), \quad f(x_{\mathrm{rob}}^*) = \frac{978253}{11560} \approx 84.623962.$$
* **Monte Carlo Feasibility Audit:** 100 random uniform realizations show nominal solution violates constraints in $57\%$ of cases, while robust solution achieves **100% feasibility** (0 violations).
* **Price of Robustness:** $\Delta f^* = +24.017901\ (+39.63\%)$.

### 3. Task 3: Road Profile Optimization via Linear Programming
* **Variational Formulation:** $\min \int_0^L |y(x) - h(x)| dx$ subject to $|y'| \leq b_1$, $|y''| \leq b_2$, $y(0)=1, y(L)=4$.
* **LP Reformulation:** Epigraph slack variables $z_i \ge |y_i - h_i|$ with $6N$ inequality constraints.
* **4 Benchmark Cases:**
  * Case A ($b_1=0.5, b_2=0.5$): $J^*(N=20) = 1.9162\text{ m}^2$, $J^*(N=100) = 1.9659\text{ m}^2$.
  * Case B ($b_1=0.5, b_2=0.2$): $J^*(N=20) = 2.4537\text{ m}^2$, $J^*(N=100) = 2.5060\text{ m}^2$ (Curvature saturates at $\pm 0.2\text{ m}^{-1}$).

### 4. Task 4: Switched System Analysis & Robust LMI Stabilization
* **Modes Stability:** Both modes are Hurwitz ($\lambda = -1 \pm j\frac{\pi}{2}$).
* **Open-Loop Instability:** Monodromy matrix across 1 period ($T=2\text{ s}$) has spectral radius $\rho(\Phi_{\mathrm{cycle}}) = 1.2180 > 1 \implies$ Periodic switching pumps energy into system causing spiral divergence.
* **LMI SDP Synthesis:** Nonconvex BMI $(A_i+BK)^TP + P(A_i+BK) \prec 0$ linearized via congruence transformation ($Q=P^{-1} \succ 0, Y=KQ$):
  $$A_i Q + Q A_i^T + B Y + Y^T B^T \prec 0.$$
* **Closed-Loop Verification:** Closed-loop monodromy spectral radius $\rho(\Phi_{\mathrm{cl,cycle}}) = 0.1320 \ll 1$, $\lambda_{\max}(\dot{V}) < 0$, strictly decaying energy $V(t) \le V_0 e^{-\alpha t}$.

---

## Publication PDF Attributes

* **File:** `02_REPORT_PDF/OMRiUS_seminar_Kresimir_Hartl.pdf`
* **Page Count:** 38 pages (strictly complies with the $\le 45$ pages requirement)
* **LaTeX Engine:** Tectonic (XeTeX) with `fontspec` and OpenType TeX Gyre Termes
* **Language:** Croatian technical academic standard (passive voice, standard terminology)
