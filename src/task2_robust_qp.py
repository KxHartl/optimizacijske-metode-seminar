"""
Task 2: Robust Quadratic Programming under Interval Uncertainty
Exact worst-case polyhedral counterpart, Monte Carlo analysis (100 samples),
and publication figure generation.
"""

import os
import sys
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from common.config_plot import setup_plot_style, save_figure, COLORS

setup_plot_style()

# 1. Canonical QP Definition
Q = np.array([[2.0, -0.3], [-0.3, 4.0]])
c = np.array([2.0, -3.0])

def objective(x):
    return 0.5 * x.T @ Q @ x + c.T @ x

# Nominal parameters
A_nom = np.array([[-1.0, -1.0], [1.0, -1.0]])
b_nom = np.array([-10.0, 3.0])

# 2. Build Exact Robust Polyhedral Constraints (8 Vertices)
# Uncertainty: +/- 15% on each coefficient
sc = [0.85, 1.15]
A_rob_list = []
b_rob_list = []

for i in range(A_nom.shape[0]):
    for s1 in sc:
        for s2 in sc:
            row = [s1 * A_nom[i, 0], s2 * A_nom[i, 1]]
            A_rob_list.append(row)
            b_rob_list.append(b_nom[i])

A_rob = np.array(A_rob_list)
b_rob = np.array(b_rob_list)

print(f"Number of robust linear inequality constraints: {A_rob.shape[0]}")

# 3. Solve Nominal QP
res_nom = opt.minimize(
    fun=objective,
    x0=[6.0, 4.0],
    method='SLSQP',
    constraints=[{'type': 'ineq', 'fun': lambda x: -(A_nom @ x - b_nom)}]
)
x_nom = res_nom.x
f_nom = res_nom.fun
print(f"Nominal Solution x_nom* = [{x_nom[0]:.6f}, {x_nom[1]:.6f}], f(x_nom*) = {f_nom:.6f}")

# 4. Solve Robust QP
res_rob = opt.minimize(
    fun=objective,
    x0=[7.0, 5.0],
    method='SLSQP',
    constraints=[{'type': 'ineq', 'fun': lambda x: -(A_rob @ x - b_rob)}]
)
x_rob = res_rob.x
f_rob = res_rob.fun
print(f"Robust Solution x_rob*  = [{x_rob[0]:.6f}, {x_rob[1]:.6f}], f(x_rob*) = {f_rob:.6f}")

# Analytical robust derivation check:
# Intersection of active worst-case constraints:
# -0.85*x1 - 0.85*x2 = -10 => 0.85*x1 + 0.85*x2 = 10
# 1.15*x1 - 0.85*x2 = 3
# Adding: 2.0*x1 = 13 => x1 = 6.5
# x2 = (10 - 0.85*6.5)/0.85 = 4.475/0.85 = 179/34 = 5.26470588
x1_rob_analyt = 6.5
x2_rob_analyt = 179.0 / 34.0
f_rob_analyt = objective(np.array([x1_rob_analyt, x2_rob_analyt]))
print(f"Analytical Robust x*    = [{x1_rob_analyt:.6f}, {x2_rob_analyt:.6f}], f(x_rob*) = {f_rob_analyt:.6f}")
print(f"Discrepancy (analytical vs numerical): {np.linalg.norm(x_rob - np.array([x1_rob_analyt, x2_rob_analyt])):.2e}")

# KKT verification for robust solution
grad_f_rob = Q @ np.array([x1_rob_analyt, x2_rob_analyt]) + c
A_act = np.array([[-0.85, -0.85], [1.15, -0.85]])
mu_rob = np.linalg.solve(A_act.T, -grad_f_rob)
print(f"Robust KKT Multipliers: mu1* = {mu_rob[0]:.6f}, mu2* = {mu_rob[1]:.6f} (Strictly positive: {np.all(mu_rob > 0)})")
slacks = b_rob - A_rob @ np.array([x1_rob_analyt, x2_rob_analyt])
print(f"Min slack across inactive vertices: {np.min(slacks[slacks > 1e-6]):.6f} > 0")

price_of_robustness = f_rob - f_nom
perc_increase = (price_of_robustness / f_nom) * 100.0
print(f"Price of Robustness: Delta f* = {price_of_robustness:.6f} (+{perc_increase:.2f}%)")

# 5. Monte Carlo Simulation (100 Random Realizations)
np.random.seed(42)
num_samples = 100
samples_A = []
violations_nom = 0
violations_rob = 0

for _ in range(num_samples):
    # Sample uniformly in [0.85*a_ij, 1.15*a_ij]
    s11 = np.random.uniform(0.85, 1.15) * A_nom[0, 0]
    s12 = np.random.uniform(0.85, 1.15) * A_nom[0, 1]
    s21 = np.random.uniform(0.85, 1.15) * A_nom[1, 0]
    s22 = np.random.uniform(0.85, 1.15) * A_nom[1, 1]
    A_k = np.array([[s11, s12], [s21, s22]])
    samples_A.append(A_k)

    # Check feasibility
    if np.any(A_k @ x_nom - b_nom > 1e-7):
        violations_nom += 1
    if np.any(A_k @ x_rob - b_nom > 1e-7):
        violations_rob += 1

print(f"\n--- Monte Carlo Feasibility Audit (N = {num_samples}) ---")
print(f"Nominal solution violation rate: {violations_nom}/{num_samples} ({violations_nom/num_samples*100:.1f}%)")
print(f"Robust solution violation rate:  {violations_rob}/{num_samples} ({violations_rob/num_samples*100:.1f}%)")

# 6. Publication Figures
print("\n--- Generating Publication Figures ---")

# Figure 2.1: Robust Feasible Envelope vs Monte Carlo Samples
fig, ax = plt.subplots(figsize=(7.5, 6.5))

x1_vals = np.linspace(2, 12, 400)

# Plot 100 Monte Carlo sample boundary lines (alpha=0.12)
for i, A_k in enumerate(samples_A):
    # g1_k: s11*x1 + s12*x2 = -10 => x2 = (-10 - s11*x1)/s12
    x2_g1_k = (-10.0 - A_k[0, 0] * x1_vals) / A_k[0, 1]
    # g2_k: s21*x1 + s22*x2 = 3 => x2 = (3 - s21*x1)/s22
    x2_g2_k = (3.0 - A_k[1, 0] * x1_vals) / A_k[1, 1]
    if i == 0:
        ax.plot(x1_vals, x2_g1_k, color=COLORS['slate_gray'], alpha=0.25, linewidth=0.8, label=r'100 slučajnih realizacija ($g_1^{(k)}$)')
        ax.plot(x1_vals, x2_g2_k, color=COLORS['light_gray'], alpha=0.35, linewidth=0.8)
    else:
        ax.plot(x1_vals, x2_g1_k, color=COLORS['slate_gray'], alpha=0.2, linewidth=0.8)
        ax.plot(x1_vals, x2_g2_k, color=COLORS['light_gray'], alpha=0.3, linewidth=0.8)

# Nominal boundaries
x2_nom_g1 = 10.0 - x1_vals
x2_nom_g2 = x1_vals - 3.0
ax.plot(x1_vals, x2_nom_g1, '--', color=COLORS['primary_blue'], linewidth=2.0, label=r'Nominalna granica $g_1^0(x) = 0$')
ax.plot(x1_vals, x2_nom_g2, '--', color=COLORS['cyan_teal'], linewidth=2.0, label=r'Nominalna granica $g_2^0(x) = 0$')

# Worst-case robust boundaries
x2_rob_g1 = (10.0 / 0.85) - x1_vals
x2_rob_g2 = (1.15 * x1_vals - 3.0) / 0.85
ax.plot(x1_vals, x2_rob_g1, color=COLORS['accent_red'], linewidth=2.4, label=r'Robusna najgora granica $g_1^{\mathrm{wc}}(x) = 0$')
ax.plot(x1_vals, x2_rob_g2, color=COLORS['dark_red'], linewidth=2.4, label=r'Robusna najgora granica $g_2^{\mathrm{wc}}(x) = 0$')

# Mark solutions
ax.plot(x_nom[0], x_nom[1], marker='o', markersize=10, color=COLORS['primary_blue'],
        label=rf'$x_{{\mathrm{{nom}}}}^* = ({x_nom[0]:.3f}, {x_nom[1]:.3f})$, $f = {f_nom:.2f}$')
ax.plot(x1_rob_analyt, x2_rob_analyt, marker='*', markersize=14, color=COLORS['dark_red'],
        label=rf'$x_{{\mathrm{{rob}}}}^* = ({x1_rob_analyt:.2f}, {x2_rob_analyt:.3f})$, $f = {f_rob:.2f}$')

ax.set_xlim([3, 11])
ax.set_ylim([1, 9])
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_title(r'Zadatak 2: Robusni dopustivi skup i Monte Carlo ovojnica ($\pm 15\%$ nesigurnost)')
ax.legend(loc='upper right', framealpha=0.92, fontsize=9)
save_figure(fig, 'fig2_1_robust_envelope_monte_carlo')
plt.close(fig)

# Figure 2.2: Objective Level Sets and Price of Robustness
fig, ax = plt.subplots(figsize=(7.5, 6.5))

x1_grid = np.linspace(3, 10, 400)
x2_grid = np.linspace(2, 9, 400)
X1, X2 = np.meshgrid(x1_grid, x2_grid)
Z = np.zeros_like(X1)
for i in range(X1.shape[0]):
    for j in range(X1.shape[1]):
        Z[i, j] = objective(np.array([X1[i, j], X2[i, j]]))

# Robust feasible region mask
rob_mask = np.ones_like(X1, dtype=bool)
for r in range(A_rob.shape[0]):
    rob_mask &= (A_rob[r, 0] * X1 + A_rob[r, 1] * X2 <= b_rob[r])

ax.contourf(X1, X2, rob_mask.astype(float), levels=[0.5, 1.5], colors=[COLORS['robust_fill']], alpha=0.5)

contours = ax.contour(X1, X2, Z, levels=[30, 45, 60.61, 70, 84.62, 100, 120], cmap='viridis', linewidths=1.3)
ax.clabel(contours, inline=True, fontsize=8, fmt='%.1f')

# Boundaries
ax.plot(x1_vals, x2_rob_g1, color=COLORS['accent_red'], linewidth=2.2, label=r'Robusno najgore ograničenje 1')
ax.plot(x1_vals, x2_rob_g2, color=COLORS['dark_red'], linewidth=2.2, label=r'Robusno najgore ograničenje 2')
ax.plot(x1_vals, x2_nom_g1, ':', color=COLORS['primary_blue'], linewidth=1.8, label=r'Nominalno ograničenje 1')

# Points
ax.plot(x_nom[0], x_nom[1], marker='o', markersize=10, color=COLORS['primary_blue'],
        label=rf'Nominalni optimum $x_{{\mathrm{{nom}}}}^*$ ($f = {f_nom:.2f}$)')
ax.plot(x1_rob_analyt, x2_rob_analyt, marker='*', markersize=14, color=COLORS['dark_red'],
        label=rf'Robusni optimum $x_{{\mathrm{{rob}}}}^*$ ($f = {f_rob:.2f}$)')

# Arrow indicating price of robustness shift
ax.annotate('', xy=(x1_rob_analyt, x2_rob_analyt), xytext=(x_nom[0], x_nom[1]),
            arrowprops=dict(arrowstyle="->", color='black', lw=2.0, ls='--'))
ax.text(6.3, 4.6, rf'$\Delta f^* = +{price_of_robustness:.2f}$ (+{perc_increase:.1f}\%)',
        fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.9))

ax.set_xlim([4, 9])
ax.set_ylim([2.5, 7.5])
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_title(r'Zadatak 2: Pomak točke optimuma i cijena robusnosti ($\Delta f^*$)')
ax.legend(loc='upper left', framealpha=0.92, fontsize=9)
save_figure(fig, 'fig2_2_price_of_robustness')
plt.close(fig)

print("Task 2 complete.")
