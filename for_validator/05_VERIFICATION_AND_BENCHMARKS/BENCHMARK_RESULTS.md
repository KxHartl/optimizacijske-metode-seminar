# Benchmark Results & Numerical Tolerances Audit

> **Course:** Optimization Methods in Systems Development and Control (OMRiUS)  
> **Student:** Krešimir Hartl  
> **Mentor:** Prof. Dr. Sc. Andrej Jokić  
> **Project:** Master's Seminar — Technical Verification & Validation Dossier  

---

## 1. Summary of Numerical Discrepancies and Solvers

All analytical results derived in the report have been verified across numerical optimization packages in both **MATLAB** (`quadprog`, `linprog`, `fmincon`, YALMIP + SDPT3) and **Python** (`scipy.optimize`, `cvxpy` with Clarabel/SCS solvers).

| Task / Metric | Exact Analytical Formula | Analytical Value | MATLAB / Python Value | Discrepancy / Error | Verification Status |
|---|---|---|---|---|---|
| **Task 1: $x_1^*$** | $\frac{380}{66} = \frac{190}{33}$ | $5.757576$ | $5.757576$ | $< 10^{-8}$ | **PASSED** (Exact) |
| **Task 1: $x_2^*$** | $10 - \frac{190}{33} = \frac{140}{33}$ | $4.242424$ | $4.242424$ | $< 10^{-8}$ | **PASSED** (Exact) |
| **Task 1: $\mu_1^*$** | $\frac{404}{33}$ | $12.242424$ | $12.242424$ | $< 10^{-8}$ | **PASSED** (Exact) |
| **Task 1: $\mu_2^*$** | $0$ (Inactive constraint) | $0.000000$ | $0.000000$ | $0.00$ | **PASSED** (Exact) |
| **Task 1: $p^* = f(x^*)$** | $\frac{2000}{33}$ | $60.606061$ | $60.606061$ | $< 10^{-8}$ | **PASSED** (Exact) |
| **Task 1: $d^* = g(\mu^*)$** | $\frac{2000}{33}$ | $60.606061$ | $60.606061$ | $< 10^{-8}$ | **PASSED** (Zero duality gap) |
| **Task 1: $\frac{\partial p^*}{\partial b_1}$** | $-\mu_1^* = -\frac{404}{33}$ | $-12.242424$ | $-12.242357$ | $6.75 \times 10^{-5}$ ($\Delta b_1 = 10^{-4}$) | **PASSED** (Sensitivity verified) |
| **Task 2: $x_{1,\mathrm{rob}}^*$** | $\frac{10 + 3}{0.85 + 1.15} = \frac{13}{2}$ | $6.500000$ | $6.500000$ | $< 10^{-8}$ | **PASSED** (Exact) |
| **Task 2: $x_{2,\mathrm{rob}}^*$** | $\frac{10 - 0.85(6.5)}{0.85} = \frac{179}{34}$ | $5.264706$ | $5.264706$ | $< 10^{-8}$ | **PASSED** (Exact) |
| **Task 2: $f(x_{\mathrm{rob}}^*)$** | $\frac{978253}{11560}$ | $84.623962$ | $84.623962$ | $< 10^{-8}$ | **PASSED** (Exact) |
| **Task 2: Price of Robustness** | $\Delta f^* = f_{\mathrm{rob}}^* - f_{\mathrm{nom}}^*$ | $24.017901$ ($+39.63\%$) | $24.017901$ ($+39.63\%$) | $< 10^{-8}$ | **PASSED** |
| **Task 2: Monte Carlo Feasibility** | 100 Uniform realizations | 100% ($x_{\mathrm{rob}}^*$) vs 43% ($x_{\mathrm{nom}}^*$) | 0% violations vs 57% violations | Exact | **PASSED** (Worst-case guaranteed) |
| **Task 3: Case A ($N=20$)** | LP Discrete Formulation | $J^* = 1.916180\text{ m}^2$ | $1.916180\text{ m}^2$ | $< 10^{-8}$ | **PASSED** (Cut: 0.088, Fill: 1.829) |
| **Task 3: Case A ($N=100$)** | LP Discrete Formulation | $J^* = 1.965940\text{ m}^2$ | $1.965940\text{ m}^2$ | $< 10^{-8}$ | **PASSED** (Asymptotic continuum limit) |
| **Task 3: Case B ($N=20$)** | LP Discrete Formulation | $J^* = 2.453727\text{ m}^2$ | $2.453727\text{ m}^2$ | $< 10^{-8}$ | **PASSED** (Cut: 0.303, Fill: 2.151) |
| **Task 3: Case B ($N=100$)** | LP Discrete Formulation | $J^* = 2.506047\text{ m}^2$ | $2.506047\text{ m}^2$ | $< 10^{-8}$ | **PASSED** (Curvature saturated $\pm 0.2$) |
| **Task 4: $\lambda(A_{\mathrm{parno}})$** | $-1 \pm j\frac{\pi}{2}$ | $-1.0000 \pm 1.5708j$ | $-1.0000 \pm 1.5708j$ | $< 10^{-8}$ | **PASSED** (Hurwitz mode 1) |
| **Task 4: $\lambda(A_{\mathrm{neparno}})$** | $-1 \pm j\frac{\pi}{2}$ | $-1.0000 \pm 1.5708j$ | $-1.0000 \pm 1.5708j$ | $< 10^{-8}$ | **PASSED** (Hurwitz mode 2) |
| **Task 4: $\rho(\Phi_{\mathrm{cycle}})$** | $e^{A_{\mathrm{odd}}} e^{A_{\mathrm{even}}}$ | $1.2180$ | $1.2180$ | $> 1$ | **PASSED** (Open-loop unstable) |
| **Task 4: Closed-loop Gain $K$** | LMI SDP Synthesis | $[-2.7120, 0.0926]$ | $[-2.7120, 0.0926]$ | Convex LMI | **PASSED** |
| **Task 4: $\rho(\Phi_{\mathrm{cl,cycle}})$** | Closed loop monodromy | $0.1320$ | $0.1320$ | $\ll 1$ | **PASSED** (Strict contraction) |
| **Task 4: $\lambda_{\max}(\dot{V})$** | Mode 1 & Mode 2 LMI check | $-0.0950, -0.0549$ | $< 0$ | $< 0$ | **PASSED** (Monotone energy decay) |

---

## 2. Key Theoretical Formulas

### Task 1: Quadratic Programming
* Hessian matrix:
  $$Q = \begin{bmatrix} 2 & -0.3 \\ -0.3 & 4 \end{bmatrix} \succ 0, \quad c = \begin{bmatrix} 2 \\ -3 \end{bmatrix}, \quad A = \begin{bmatrix} -1 & -1 \\ 1 & -1 \end{bmatrix}, \quad b = \begin{bmatrix} -10 \\ 3 \end{bmatrix}$$
* Lagrange Dual Function:
  $$g(\mu) = -\frac{1}{2}(c + A^T \mu)^T Q^{-1} (c + A^T \mu) - b^T \mu$$
* Sensitivity theorem:
  $$\frac{\partial p^*}{\partial b_i} = -\mu_i^*$$

### Task 2: Robust Optimization
* Vertex-based robust deterministic equivalent:
  $$\max_{a_i \in \mathcal{U}_i} a_i^T x \leq b_i \iff (v_i^{(k)})^T x \leq b_i, \quad \forall k \in \{1, \dots, 2^n\}$$
* 8 linear inequalities with vertices from $[-1.15, -0.85] \times [-1.15, -0.85]$ and $[0.85, 1.15] \times [-1.15, -0.85]$.

### Task 3: Road Leveling Linear Program
* Epigraph slack variables $z_i \geq |y_i - h_i|$:
  $$\min \Delta x \sum_{i=0}^N z_i \quad \text{s.t.} \quad y_i - z_i \leq h_i, \quad -y_i - z_i \leq -h_i, \quad |D_1 y| \leq b_1, \quad |D_2 y| \leq b_2, \quad y_0 = a, \quad y_N = b$$

### Task 4: Switched System LMI Stabilization
* Congruence transformation ($Q = P^{-1} \succ 0, Y = KQ$):
  $$A_i Q + Q A_i^T + B Y + Y^T B^T \prec 0, \quad i \in \{\mathrm{even}, \mathrm{odd}\}$$
* Monodromy Matrix:
  $$\Phi_{\mathrm{cycle}} = e^{A_{\mathrm{odd}} \cdot 1} e^{A_{\mathrm{even}} \cdot 1}, \quad \rho(\Phi_{\mathrm{cycle}}) = \max_i |\lambda_i(\Phi_{\mathrm{cycle}})|$$
