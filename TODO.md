# OMRiUS Master Seminar Project Execution Roadmap & Task Registry

> **Course:** Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)  
> **Institution:** Faculty of Mechanical Engineering and Naval Architecture (FSB), University of Zagreb  
> **Student:** Krešimir Hartl  
> **Academic Supervisor:** Prof. dr. sc. Andrej Jokić  
> **Repository Format:** `fsb-seminar` (Tectonic / MiKTeX / pdflatex)  
> **Status:** Completed & Ready for Defense  

---

## Executive Blueprint & Governance

### 1. Architectural Principles & Quality Standards
- **Zero Mathematical Ambiguity**: Every proof, derivation, active-set branch, dual formulation, and LMI congruence transformation is analytically complete and self-contained.
- **RAG & Course Grounding**: All theoretical frameworks map deterministically to lecture slides (`data/sources/lectures/01`–`08`) and auditorne vježbe (`Vjezbe 1`–`5`).
- **Machine-Precision Consistency**: Analytical predictions ($x^*$, $\mu^*$, $p^*$, $K$) match numerical solver solutions (`quadprog`, `linprog`, `fmincon`, YALMIP, CVXPY) to $\le 10^{-8}$ relative tolerance.
- **Autonomous Proactive Git**: Every completed logical milestone is checkpointed with `🤖 [AI]` tag.
- **Publication-Grade Visual Assets**: All 12 plots exported as vector graphics (`.pdf`) and raster (`.png` $\ge 300\text{ DPI}$) to `docs/figures/`.
- **Formal Academic Croatian Register**: Report chapters in `docs/chapters/` strictly adhere to Croatian academic optimization terminology.

---

## Specialist Agent Workflow & Orchestration Matrix

| Phase / Role | Specialized Subagent | Primary Directory | Scope & Responsibilities | Status |
|---|---|---|---|---|
| **Phase 1: Derivations** | `writer` / `research` | `TASK/`, `docs/chapters/` | Analytical proofs, KKT resolution, dual functions, worst-case robust counterpart, LMI congruence. | **COMPLETE** |
| **Phase 2: Code & Simulations** | `self` (Engineering) | `src/`, `docs/figures/`, `tests/` | MATLAB (`.m`) & Python (`.py`) numerical scripts, solver benchmarks, Monte Carlo loops, ODE simulation. | **COMPLETE** |
| **Phase 3: LaTeX Drafting** | `writer` | `docs/chapters/`, `docs/tables/` | High-fidelity Croatian academic text, equation typesetting, table formatting, figure inclusion. | **COMPLETE** |
| **Phase 4: Verification & QA** | `qa_reviewer` | `docs/REVIEW.md`, `tests/` | End-to-end numerical-analytical validation, build sanity checks, defense package preparation. | **COMPLETE** |
| **Phase 5: Release Build** | `latex_architect` | `dist/v1.0/` | PDF compilation via `build-docs.ps1`, layout verification, page limit constraint ($\le 45$ pages). | **COMPLETE** |

---

## Phase 1 — Mathematical Derivations & Analytical Solution Packages

### Task 1: Quadratic Programming (QP), Convexity, KKT, Duality & Sensitivity
- [x] **1.1 Matrix Formulation & Strict Convexity Proof**
  - [x] Express $f(x) = x_1^2 + 2x_2^2 - 0.3x_1 x_2 + 2x_1 - 3x_2$ in symmetric canonical form: $f(x) = \frac{1}{2} x^T Q x + c^T x$.
  - [x] Derive analytical Hessian matrix:
    $$Q = \nabla^2 f(x) = \begin{bmatrix} 2 & -0.3 \\ -0.3 & 4 \end{bmatrix}, \quad c = \begin{bmatrix} 2 \\ -3 \end{bmatrix}$$
  - [x] Compute eigenvalues of $Q$: $\det(\lambda I - Q) = \lambda^2 - 6\lambda + 7.91 = 0 \implies \lambda_{1} \approx 1.9560, \lambda_{2} \approx 4.0440$.
  - [x] Formulate formal proof: $\lambda_i > 0 \implies Q \succ 0$ (positive definite) on $\mathbb{R}^2$, confirming $f(x)$ is strictly convex.
  - [x] Prove constraint set convexity: $g_1(x) = -x_1 - x_2 + 10 \le 0$ and $g_2(x) = x_1 - x_2 - 3 \le 0$ are affine half-spaces; intersection of convex sets is convex.
  - [x] Conclude global optimality: strictly convex objective over non-empty convex polyhedral domain guarantees a unique global minimum $x^*$.
- [x] **1.2 Complete KKT System & 4-Branch Active-Set Matrix Derivation**
  - [x] Formulate Lagrangian function:
    $$\mathcal{L}(x, \mu) = f(x) + \mu_1(-x_1 - x_2 + 10) + \mu_2(x_1 - x_2 - 3)$$
  - [x] State explicit KKT conditions (Stationarity, Primal Feasibility, Dual Feasibility, Complementary Slackness).
  - [x] **Exhaustive 4-Case Evaluation Table**:
    - [x] **Case 1: Both Inactive ($\mu_1 = 0, \mu_2 = 0$)**: $x_0 = [-0.8976, 0.6827]^T \implies g_1(x_0) = 10.215 > 0 \implies$ REJECTED.
    - [x] **Case 2: Only $g_1$ Active ($\mu_1 > 0, \mu_2 = 0$)**: $x^* = \left(\frac{190}{33}, \frac{140}{33}\right) \approx (5.7576, 4.2424)$, $\mu_1^* = \frac{404}{33} \approx 12.2424$, $p^* = \frac{2000}{33} \approx 60.6061 \implies$ ACCEPTED (Unique Global Optimum).
    - [x] **Case 3: Only $g_2$ Active ($\mu_1 = 0, \mu_2 > 0$)**: Yields $\mu_2 = -6.709 < 0$ and $g_1(x) = 8.519 > 0 \implies$ REJECTED.
    - [x] **Case 4: Both Active ($\mu_1 > 0, \mu_2 > 0$)**: Intersection $x = (6.5, 3.5) \implies \mu_2 = -2.45 < 0 \implies$ REJECTED.
- [x] **1.3 Analytical Lagrange Dual Function Derivation & Strong Duality**
  - [x] Derive unconstrained minimum $x^*(\mu) = -Q^{-1}(c + A^T \mu)$.
  - [x] Substitute $x^*(\mu)$ into $\mathcal{L}(x, \mu)$ to obtain explicit dual function $g(\mu) = -\frac{1}{2} (c + A^T \mu)^T Q^{-1} (c + A^T \mu) - b^T \mu$.
  - [x] Verify concavity of $g(\mu)$.
  - [x] Maximize $g(\mu)$ subject to $\mu \ge 0 \implies \mu^* = [12.2424, 0]^T$, $d^* = 60.6061$.
  - [x] Verify Slater's condition ($x = [7, 6]^T \implies g_1 = -3 < 0, g_2 = -2 < 0$) $\implies$ Strong duality holds ($p^* = d^*$, gap $\gamma = 0$).
- [x] **1.4 Sensitivity Theorem & Perturbational Analysis**
  - [x] Prove sensitivity relation: $\frac{\partial p^*}{\partial b_1} = -\mu_1^* = -12.2424$, $\frac{\partial p^*}{\partial b_2} = -\mu_2^* = 0$.
  - [x] Economic / shadow price interpretation.
  - [x] Numerical perturbation verification with $\Delta b_1 = 10^{-4} \implies \Delta p^* / \Delta b_1 = -12.242357$.

---

### Task 2: Robust Quadratic Programming under Interval Uncertainty
- [x] **2.1 Theoretical Framework of Robust Counterparts (Lecture 8 Grounding)**
  - [x] Define uncertain parameter sets for $\pm 15\%$ interval variation: $\mathcal{U}_1, \mathcal{U}_2$.
  - [x] Formulate robust semi-infinite QP.
- [x] **2.2 Analytical Derivation of Exact Deterministic Counterpart**
  - [x] Prove vertex extreme theorem for linear functions over polyhedra.
  - [x] Formulate full deterministic QP with all 8 vertex inequalities.
  - [x] Compute analytical closed-form solution: $x_{\text{rob}}^* = \left(6.5, \frac{179}{34}\right) = (6.5000, 5.2647)$, $f(x_{\text{rob}}^*) = 84.6240$.
- [x] **2.3 Price of Robustness & Monte Carlo Verification**
  - [x] Price of robustness: $\Delta f^* = 84.6240 - 60.6061 = 24.0179$ (+39.63%).
  - [x] Run 100-sample Monte Carlo simulation: nominal failure rate $57\%$, robust failure rate $0\%$.

---

### Task 3: Optimization Formulation & Approximation — Road Profile Leveling (LP)
- [x] **3.1 Continuous Variational Problem Formulation**
  - [x] Objective: $\min \int_0^L |y(x) - h(x)| dx$.
  - [x] Slope constraint: $|y'(x)| \le b_1$.
  - [x] Curvature constraint: $|y''(x)| \le b_2$.
  - [x] Boundary conditions: $y(0) = 1$, $y(L) = 4$.
- [x] **3.2 Discrete Finite Difference Discretization Scheme**
  - [x] Discretization grid: $N$ intervals, $N+1$ nodes, $\Delta x = L/N$.
  - [x] First difference operator matrix $D_1 \in \mathbb{R}^{N \times (N+1)}$.
  - [x] Second difference operator matrix $D_2 \in \mathbb{R}^{(N-1) \times (N+1)}$.
- [x] **3.3 Linear Programming Reformulation via Epigraph Slack Variables**
  - [x] Slack variables $z_i \ge |y_i - h_i|$.
  - [x] Decision vector $\theta = [y^T, z^T]^T \in \mathbb{R}^{2N+2}$.
  - [x] Linear objective $f_{\text{LP}}^T \theta = \Delta x \sum z_i$.
  - [x] Full inequality constraint matrix $A \theta \le b$ with $6N$ rows.
  - [x] Solve 4 benchmark cases ($N=20, 100$, Cases A and B).

---

### Task 4: Robust Stabilization of Switched Linear System via LMIs
- [x] **4.1 Open-Loop Autonomous Mode Analysis & Hurwitz Characterization**
  - [x] Eigenvalue derivation: $\lambda_{1,2}(A_{\text{parno}}) = -1 \pm j \frac{\pi}{2}$, $\lambda_{1,2}(A_{\text{neparno}}) = -1 \pm j \frac{\pi}{2}$.
  - [x] Proof that individual modes are Hurwitz stable ($\text{Re}(\lambda) = -1 < 0$).
- [x] **4.2 Theoretical Destabilization Mechanism under Periodic Switching**
  - [x] State transition matrices $\Phi_{\text{parno}}, \Phi_{\text{neparno}}$.
  - [x] Full period monodromy matrix: $\Phi_{\text{cycle}} = \Phi_{\text{neparno}} \Phi_{\text{parno}}$.
  - [x] Spectral radius $\rho(\Phi_{\text{cycle}}) = 1.2180 > 1$, proving open-loop instability.
- [x] **4.3 Common Quadratic Lyapunov Function & LMI Linearization**
  - [x] Candidate CQLF $V(x) = x^T P x$, $P \succ 0$.
  - [x] Closed-loop Lyapunov derivative $(A_i + BK)^T P + P(A_i + BK) \prec 0$.
  - [x] Congruence transformation ($Q = P^{-1} \succ 0$) and variable substitution ($Y = KQ$).
  - [x] Exact LMI formulation in $Q$ and $Y$.
  - [x] State feedback gain recovery: $K = Y Q^{-1}$.
  - [x] ODE simulation confirming exponential stabilization and energy dissipation.

---

## Phase 2 — MATLAB / Python Implementation, Simulation & Plotting Suite

- [x] **2.1 Task 1 Simulation Suite (`src/task1_qp_analysis.py` & `.m`)**
  - [x] Export Fig 1.1: Primal feasible polygon, contours, gradients, KKT balance.
  - [x] Export Fig 1.2: Dual function surface $g(\mu_1, \mu_2)$.
  - [x] Export Fig 1.3: Perturbation curve $p^*(b_1)$ vs tangent.
- [x] **2.2 Task 2 Robust Optimization Suite (`src/task2_robust_qp.py` & `.m`)**
  - [x] Export Fig 2.1: Robust envelope vs 100 Monte Carlo sample polytopes.
  - [x] Export Fig 2.2: Objective level sets and price of robustness shift.
- [x] **2.3 Task 3 Road Profile LP Suite (`src/task3_road_leveling.py` & `.m`)**
  - [x] Export Fig 3.1: Case A road profile $y(x)$ vs terrain $h(x)$ ($N=20, 100$).
  - [x] Export Fig 3.2: Case B road profile $y(x)$ vs terrain $h(x)$ ($N=20, 100$).
  - [x] Export Fig 3.3: Slope profile $y'(x)$ vs $\pm b_1$.
  - [x] Export Fig 3.4: Curvature profile $y''(x)$ vs $\pm b_2$.
- [x] **2.4 Task 4 Switched System & LMI Suite (`src/task4_lmi_switched_stabilization.py` & `.m`)**
  - [x] Export Fig 4.1: Open-loop divergence (time history & phase portrait).
  - [x] Export Fig 4.2: Closed-loop stabilization & Lyapunov level ellipses.
  - [x] Export Fig 4.3: Lyapunov energy dissipation $V(x(t))$ on logarithmic scale.
- [x] **2.5 Master Runner Suite (`src/run_all.py` & `src/run_all.m`)**

---

## Phase 3 — LaTeX Documentation & Chapter Drafting

- [x] **3.0 Master Document Configuration (`docs/main.tex`)**
- [x] **3.1 Chapter 0: Uvod (`docs/chapters/00-uvod.tex`)**
- [x] **3.2 Chapter 1: Zadatak 1 QP (`docs/chapters/01-zadatak1-qp.tex`)**
- [x] **3.3 Chapter 2: Zadatak 2 Robust QP (`docs/chapters/02-zadatak2-rob-qp.tex`)**
- [x] **3.4 Chapter 3: Zadatak 3 Cesta LP (`docs/chapters/03-zadatak3-cesta-lp.tex`)**
- [x] **3.5 Chapter 4: Zadatak 4 LMI Stabilizacija (`docs/chapters/04-zadatak4-lmi-stabilizacija.tex`)**
- [x] **3.6 Chapter 5: Zaključak (`docs/chapters/zakljucak.tex`)**
- [x] **3.7 Bibliography Database (`docs/references.bib`)**

---

## Phase 4 — Quality Assurance, Verification & Defense Preparation

- [x] **4.1 Numerical & Textual QA Checklist (`docs/REVIEW.md`)**
  - [x] Machine-precision table populated with all tolerances $< 10^{-8}$.
- [x] **4.2 Academic Defense Q&A Preparation Package (`docs/REVIEW.md`)**
  - [x] Defense questions 1–4 answered with complete mathematical rigor.

---

## Phase 5 — Build & Distribution Packaging

- [x] **5.1 Compilation & Page Budget Check**
  - [x] Run `build-docs.ps1` with Tectonic XeTeX engine.
  - [x] Page count verified: **38 / 45 pages** (0 errors).
- [x] **5.2 Distribution Artifact Generation**
  - [x] Copy compiled PDF to `dist/v1.0/OMRiUS_seminar_Kresimir_Hartl.pdf`.
  - [x] Final git porcelain status verified clean.
