"""
Task 1: QP Analysis, KKT 4-Case Resolution, Duality, Sensitivity, and Plotting
"""

import os
import sys
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))
from common.config_plot import setup_plot_style, save_figure, COLORS

setup_plot_style()

# 1. Canonical Problem Definition
# f(x) = x1^2 + 2*x2^2 - 0.3*x1*x2 + 2*x1 - 3*x2
# f(x) = 0.5 * x^T Q x + c^T x
Q = np.array([[2.0, -0.3], [-0.3, 4.0]])
c = np.array([2.0, -3.0])
A = np.array([[-1.0, -1.0], [1.0, -1.0]])
b = np.array([-10.0, 3.0])

def objective(x):
    return 0.5 * x.T @ Q @ x + c.T @ x

def grad_f(x):
    return Q @ x + c

# 2. Eigenvalue Analysis for Strict Convexity
eigvals, eigvecs = np.linalg.eigh(Q)
print(f"Hessian Q eigenvalues: lambda_1 = {eigvals[0]:.6f}, lambda_2 = {eigvals[1]:.6f}")
print(f"Is Q positive definite: {np.all(eigvals > 0)}")

# 3. Exhaustive 4-Case KKT Analysis
print("\n--- Exhaustive 4-Case KKT Analysis ---")

# Case 1: Both inactive (mu1 = 0, mu2 = 0)
x_case1 = np.linalg.solve(Q, -c)
g1_case1 = -x_case1[0] - x_case1[1] + 10
g2_case1 = x_case1[0] - x_case1[1] - 3
print(f"Case 1 (mu1=0, mu2=0): x = [{x_case1[0]:.6f}, {x_case1[1]:.6f}]")
print(f"  g1(x) = {g1_case1:.6f} (needs <= 0) -> {'Feasible' if g1_case1 <= 0 else 'INFEASIBLE (REJECTED)'}")

# Case 2: Only g1 active (mu1 > 0, mu2 = 0)
# [ 2   -0.3  -1 ] [ x1 ]   [ -2 ]
# [ -0.3   4  -1 ] [ x2 ] = [  3 ]
# [ -1    -1   0 ] [ mu1]   [ -10]
M_case2 = np.array([
    [2.0, -0.3, -1.0],
    [-0.3, 4.0, -1.0],
    [-1.0, -1.0, 0.0]
])
rhs_case2 = np.array([-2.0, 3.0, -10.0])
sol_case2 = np.linalg.solve(M_case2, rhs_case2)
x_case2 = sol_case2[:2]
mu1_case2 = sol_case2[2]
g2_case2 = x_case2[0] - x_case2[1] - 3
print(f"Case 2 (g1 active): x = [{x_case2[0]:.6f}, {x_case2[1]:.6f}], mu1 = {mu1_case2:.6f}")
print(f"  g2(x) = {g2_case2:.6f}, mu1 = {mu1_case2:.6f} -> {'ACCEPTED (OPTIMUM)' if (g2_case2 <= 0 and mu1_case2 >= 0) else 'REJECTED'}")

# Case 3: Only g2 active (mu1 = 0, mu2 > 0)
# [ 2   -0.3   1 ] [ x1 ]   [ -2 ]
# [ -0.3   4  -1 ] [ x2 ] = [  3 ]
# [ 1    -1   0 ] [ mu2]   [  3 ]
M_case3 = np.array([
    [2.0, -0.3, 1.0],
    [-0.3, 4.0, -1.0],
    [1.0, -1.0, 0.0]
])
rhs_case3 = np.array([-2.0, 3.0, 3.0])
sol_case3 = np.linalg.solve(M_case3, rhs_case3)
x_case3 = sol_case3[:2]
mu2_case3 = sol_case3[2]
g1_case3 = -x_case3[0] - x_case3[1] + 10
print(f"Case 3 (g2 active): x = [{x_case3[0]:.6f}, {x_case3[1]:.6f}], mu2 = {mu2_case3:.6f}")
print(f"  g1(x) = {g1_case3:.6f}, mu2 = {mu2_case3:.6f} -> {'ACCEPTED' if (g1_case3 <= 0 and mu2_case3 >= 0) else 'REJECTED'}")

# Case 4: Both active (g1=0, g2=0)
# -x1 - x2 = -10, x1 - x2 = 3 => x1 = 6.5, x2 = 3.5
x_case4 = np.array([6.5, 3.5])
# Q x + c + A^T mu = 0 => A^T mu = -(Q x + c)
grad_f_case4 = Q @ x_case4 + c
# A^T = [[-1, 1], [-1, -1]]
mu_case4 = np.linalg.solve(A.T, -grad_f_case4)
print(f"Case 4 (both active): x = [{x_case4[0]:.6f}, {x_case4[1]:.6f}], mu = [{mu_case4[0]:.6f}, {mu_case4[1]:.6f}]")
print(f"  mu >= 0 check: {'ACCEPTED' if np.all(mu_case4 >= 0) else 'REJECTED (mu2 < 0)'}")

# 4. Numerical Verification using SciPy
res = opt.minimize(
    fun=objective,
    x0=[6.0, 4.0],
    method='SLSQP',
    bounds=None,
    constraints=[
        {'type': 'ineq', 'fun': lambda x: -(A @ x - b)[0]},
        {'type': 'ineq', 'fun': lambda x: -(A @ x - b)[1]}
    ],
    options={'ftol': 1e-12, 'disp': False}
)
x_opt = res.x
f_opt = res.fun
print("\n--- Numerical Verification (SLSQP / quadprog equivalent) ---")
print(f"Optimal x* = [{x_opt[0]:.6f}, {x_opt[1]:.6f}]")
print(f"Optimal f(x*) = {f_opt:.6f}")

# 5. Dual Function g(mu) and Numerical Dual Optimization
# g(mu) = inf_x L(x, mu) = -0.5 * (c + A^T mu)^T Q^-1 (c + A^T mu) - b^T mu
Q_inv = np.linalg.inv(Q)
def dual_function(mu):
    v = c + A.T @ mu
    return -0.5 * v.T @ Q_inv @ v - b.T @ mu

res_dual = opt.minimize(
    fun=lambda mu: -dual_function(mu),
    x0=[1.0, 1.0],
    bounds=[(0, None), (0, None)],
    method='L-BFGS-B'
)
mu_opt = res_dual.x
d_opt = -res_dual.fun
print("\n--- Dual Problem Verification ---")
print(f"Optimal dual mu* = [{mu_opt[0]:.6f}, {mu_opt[1]:.6f}]")
print(f"Optimal dual value d* = {d_opt:.6f}")
print(f"Duality Gap (p* - d*) = {abs(f_opt - d_opt):.2e}")

# 6. Sensitivity Analysis
print("\n--- Sensitivity Analysis ---")
delta = 1e-4
# Perturb b1
b_pert_plus = np.array([-10.0 + delta, 3.0])
res_b1_plus = opt.minimize(
    fun=objective, x0=x_opt, method='SLSQP',
    constraints=[{'type': 'ineq', 'fun': lambda x: -(A @ x - b_pert_plus)[0]},
                 {'type': 'ineq', 'fun': lambda x: -(A @ x - b_pert_plus)[1]}]
)
# Note: constraint is A x <= b, so -x1 - x2 <= -10 + delta.
# Perturbing b1 by +delta relaxes/tightens:
# dp*/db1 = (p*(b1+delta) - p*(b1)) / delta
dp_db1_num = (res_b1_plus.fun - f_opt) / delta
print(f"dp*/db1 (numerical)  = {dp_db1_num:.6f}")
print(f"-mu1* (analytical)   = {-mu1_case2:.6f}")
print(f"Sensitivity Error    = {abs(dp_db1_num - (-mu1_case2)):.2e}")

# 7. Figure Generation
print("\n--- Generating Publication Figures ---")

# Figure 1.1: Primal Feasible Region, Objective Contours, and Gradients
fig, ax = plt.subplots(figsize=(7, 6))

x1_grid = np.linspace(0, 10, 400)
x2_grid = np.linspace(0, 10, 400)
X1, X2 = np.meshgrid(x1_grid, x2_grid)
Z = np.zeros_like(X1)
for i in range(X1.shape[0]):
    for j in range(X1.shape[1]):
        x_vec = np.array([X1[i, j], X2[i, j]])
        Z[i, j] = objective(x_vec)

# Constraint boundaries
# g1: -x1 - x2 + 10 = 0 => x2 = 10 - x1
# g2: x1 - x2 - 3 = 0 => x2 = x1 - 3
x1_line = np.linspace(0, 10, 400)
x2_g1 = 10.0 - x1_line
x2_g2 = x1_line - 3.0

# Feasible region fill
# Intersection: x1+x2 >= 10 and x2 >= x1 - 3
feasible_mask = (-X1 - X2 + 10 <= 0) & (X1 - X2 - 3 <= 0)
ax.contourf(X1, X2, feasible_mask.astype(float), levels=[0.5, 1.5], colors=[COLORS['feasible_fill']], alpha=0.6)

# Contour lines of objective
contours = ax.contour(X1, X2, Z, levels=25, cmap='viridis', linewidths=1.2)
ax.clabel(contours, inline=True, fontsize=8, fmt='%.1f')

# Plot boundary lines
ax.plot(x1_line, x2_g1, color=COLORS['accent_red'], linewidth=2.0, label=r'$g_1(x): -x_1 - x_2 + 10 \leq 0$')
ax.plot(x1_line, x2_g2, color=COLORS['forest_green'], linewidth=2.0, label=r'$g_2(x): x_1 - x_2 - 3 \leq 0$')

# Optimal point and unconstrained minimum
ax.plot(x_case2[0], x_case2[1], marker='*', markersize=14, color=COLORS['dark_red'],
        label=rf'$x^* = ({x_case2[0]:.3f}, {x_case2[1]:.3f})$')
ax.plot(x_case1[0], x_case1[1], marker='o', markersize=8, color=COLORS['slate_gray'],
        label=rf'$x_0 = ({x_case1[0]:.2f}, {x_case1[1]:.2f})$ (nesputano)')

# Gradients at x*
grad_f_val = grad_f(x_case2)
grad_g1_val = np.array([-1.0, -1.0])
grad_g2_val = np.array([1.0, -1.0])
scale_g = 1.8
scale_f = 0.25

ax.quiver(x_case2[0], x_case2[1], grad_f_val[0]*scale_f, grad_f_val[1]*scale_f,
          angles='xy', scale_units='xy', scale=1, color=COLORS['dark_blue'],
          width=0.008, label=r'$\nabla f(x^*)$')
ax.quiver(x_case2[0], x_case2[1], grad_g1_val[0]*scale_g, grad_g1_val[1]*scale_g,
          angles='xy', scale_units='xy', scale=1, color=COLORS['accent_red'],
          width=0.008, label=r'$\nabla g_1(x^*)$ (aktivno, $\mu_1^* = 12.242$)')
ax.quiver(x_case2[0], x_case2[1], grad_g2_val[0]*scale_g, grad_g2_val[1]*scale_g,
          angles='xy', scale_units='xy', scale=1, color=COLORS['forest_green'],
          width=0.008, label=r'$\nabla g_2(x^*)$ (neaktivno, $\mu_2^* = 0$)')

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_title(r'Zadatak 1: Geometrija QP problema, nivo-krivulje i KKT ravnoteža gradijenata')
ax.legend(loc='upper right', framealpha=0.9)
save_figure(fig, 'fig1_1_qp_primal_geometry')
plt.close(fig)

# Figure 1.2: Dual Function Surface g(mu1, mu2)
fig, ax = plt.subplots(figsize=(7, 6))
mu1_vals = np.linspace(0, 20, 200)
mu2_vals = np.linspace(0, 10, 200)
M1, M2 = np.meshgrid(mu1_vals, mu2_vals)
G = np.zeros_like(M1)
for i in range(M1.shape[0]):
    for j in range(M1.shape[1]):
        G[i, j] = dual_function(np.array([M1[i, j], M2[i, j]]))

cont_dual = ax.contour(M1, M2, G, levels=30, cmap='plasma', linewidths=1.2)
ax.clabel(cont_dual, inline=True, fontsize=8, fmt='%.1f')
ax.plot(mu1_case2, 0.0, marker='*', markersize=14, color=COLORS['dark_red'],
        label=rf'$\mu^* = ({mu1_case2:.3f}, 0.000)$, $d^* = {d_opt:.3f}$')

ax.set_xlim([0, 20])
ax.set_ylim([0, 10])
ax.set_xlabel(r'$\mu_1$')
ax.set_ylabel(r'$\mu_2$')
ax.set_title(r'Zadatak 1: Nivo-krivulje konkavne dualne funkcije $g(\mu_1, \mu_2)$')
ax.legend(loc='upper right', framealpha=0.9)
save_figure(fig, 'fig1_2_qp_dual_surface')
plt.close(fig)

# Figure 1.3: Sensitivity Curve p*(b1) vs Tangent
fig, ax = plt.subplots(figsize=(7, 5))
delta_range = np.linspace(-0.5, 0.5, 50)
p_pert = []
for d in delta_range:
    b_test = np.array([-10.0 + d, 3.0])
    res_t = opt.minimize(
        fun=objective, x0=x_opt, method='SLSQP',
        constraints=[{'type': 'ineq', 'fun': lambda x, b_curr=b_test: -(A @ x - b_curr)[0]},
                     {'type': 'ineq', 'fun': lambda x, b_curr=b_test: -(A @ x - b_curr)[1]}]
    )
    p_pert.append(res_t.fun)

ax.plot(delta_range, p_pert, 'o-', color=COLORS['primary_blue'], label=r'Točna funkcija optimalne vrijednosti $p^*(b_1 + \Delta b_1)$')
tangent = f_opt - mu1_case2 * delta_range
ax.plot(delta_range, tangent, '--', color=COLORS['accent_red'], linewidth=2.2,
        label=rf'Linearna aproksimacija nagiba $-\mu_1^* = -{mu1_case2:.4f}$')
ax.plot(0, f_opt, marker='*', markersize=12, color=COLORS['dark_red'], label=rf'$p^* = {f_opt:.4f}$')

ax.set_xlabel(r'Perturbacija desne strane $\Delta b_1$')
ax.set_ylabel(r'Optimalna vrijednost $p^*$')
ax.set_title(r'Zadatak 1: Analiza osjetljivosti i verifikacija teorema osjetljivosti')
ax.legend(loc='best', framealpha=0.9)
save_figure(fig, 'fig1_3_qp_sensitivity')
plt.close(fig)

print("Task 1 complete.")
