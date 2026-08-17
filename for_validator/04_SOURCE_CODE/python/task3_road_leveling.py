"""
Task 3: Road Profile Optimization via Linear Programming (LP)
Discretization, Epigraph Slack Formulation, linprog Solver,
and Publication Figures for Cases A & B with N=20 and N=100.
"""

import os
import sys
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from common.config_plot import setup_plot_style, save_figure, COLORS

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

setup_plot_style()

# 1. Terrain Function
L = 10.0
def terrain(x):
    return 0.0053 * x**4 - 0.095 * x**3 + 0.48 * x**2 - 0.3 * x + 1.0

# 2. Solver Function for Arbitrary (b1, b2, N)
def solve_road_leveling(b1, b2, N, case_name=""):
    dx = L / N
    x = np.linspace(0, L, N + 1)
    h = terrain(x)
    
    num_y = N + 1
    num_z = N + 1
    num_vars = num_y + num_z
    
    # Cost vector: min sum(z_i * dx)
    # theta = [y_0 ... y_N, z_0 ... z_N]^T
    c = np.zeros(num_vars)
    c[num_y:] = dx  # objective is sum(z_i * dx) = total volume
    
    A_ineq_list = []
    b_ineq_list = []
    
    # 1. Absolute value constraints: y_i - z_i <= h_i and -y_i - z_i <= -h_i
    for i in range(num_y):
        # y_i - z_i <= h_i
        row1 = np.zeros(num_vars)
        row1[i] = 1.0
        row1[num_y + i] = -1.0
        A_ineq_list.append(row1)
        b_ineq_list.append(h[i])
        
        # -y_i - z_i <= -h_i
        row2 = np.zeros(num_vars)
        row2[i] = -1.0
        row2[num_y + i] = -1.0
        A_ineq_list.append(row2)
        b_ineq_list.append(-h[i])
        
    # 2. Slope constraints: |(y_i - y_{i-1})/dx| <= b1
    #  y_i - y_{i-1} <= b1*dx
    # -y_i + y_{i-1} <= b1*dx
    for i in range(1, num_y):
        row1 = np.zeros(num_vars)
        row1[i] = 1.0 / dx
        row1[i - 1] = -1.0 / dx
        A_ineq_list.append(row1)
        b_ineq_list.append(b1)
        
        row2 = np.zeros(num_vars)
        row2[i] = -1.0 / dx
        row2[i - 1] = 1.0 / dx
        A_ineq_list.append(row2)
        b_ineq_list.append(b1)
        
    # 3. Curvature constraints: |(y_i - 2y_{i-1} + y_{i-2})/dx^2| <= b2
    for i in range(2, num_y):
        row1 = np.zeros(num_vars)
        row1[i] = 1.0 / (dx**2)
        row1[i - 1] = -2.0 / (dx**2)
        row1[i - 2] = 1.0 / (dx**2)
        A_ineq_list.append(row1)
        b_ineq_list.append(b2)
        
        row2 = np.zeros(num_vars)
        row2[i] = -1.0 / (dx**2)
        row2[i - 1] = 2.0 / (dx**2)
        row2[i - 2] = -1.0 / (dx**2)
        A_ineq_list.append(row2)
        b_ineq_list.append(b2)
        
    A_ub = np.array(A_ineq_list)
    b_ub = np.array(b_ineq_list)
    
    # 4. Boundary equality constraints: y(0) = 1, y(L) = 4
    A_eq = np.zeros((2, num_vars))
    b_eq = np.array([1.0, 4.0])
    A_eq[0, 0] = 1.0
    A_eq[1, num_y - 1] = 1.0
    
    # Bounds: y free, z >= 0
    bounds = [(None, None)] * num_y + [(0, None)] * num_z
    
    # Solve via Highs dual simplex / interior point
    res = opt.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    
    if not res.success:
        raise RuntimeError(f"Optimization failed for Case {case_name}, N={N}: {res.message}")
        
    y_opt = res.x[:num_y]
    z_opt = res.x[num_y:]
    cost_integral = res.fun
    raw_sum = np.sum(z_opt)
    
    # Compute slopes and curvatures
    slopes = np.diff(y_opt) / dx
    curvatures = np.diff(slopes) / dx
    
    # Cut and fill volumes
    diff = y_opt - h
    cut_vol = np.sum(np.maximum(0, -diff)) * dx
    fill_vol = np.sum(np.maximum(0, diff)) * dx
    
    return {
        'x': x,
        'h': h,
        'y': y_opt,
        'z': z_opt,
        'cost': cost_integral,
        'raw_sum': raw_sum,
        'slopes': slopes,
        'x_slopes': x[1:],
        'curvatures': curvatures,
        'x_curv': x[2:],
        'cut_vol': cut_vol,
        'fill_vol': fill_vol,
        'b1': b1,
        'b2': b2,
        'N': N
    }

# 3. Run All 4 Benchmark Cases
cases = [
    {'name': 'A_N20', 'label': 'Slučaj A (b1=0.5, b2=0.5, N=20)', 'b1': 0.5, 'b2': 0.5, 'N': 20},
    {'name': 'A_N100', 'label': 'Slučaj A (b1=0.5, b2=0.5, N=100)', 'b1': 0.5, 'b2': 0.5, 'N': 100},
    {'name': 'B_N20', 'label': 'Slučaj B (b1=0.5, b2=0.2, N=20)', 'b1': 0.5, 'b2': 0.2, 'N': 20},
    {'name': 'B_N100', 'label': 'Slučaj B (b1=0.5, b2=0.2, N=100)', 'b1': 0.5, 'b2': 0.2, 'N': 100},
]

results = {}
print("=== Task 3: Road Leveling LP Benchmark Results ===")
for c in cases:
    res = solve_road_leveling(c['b1'], c['b2'], c['N'], c['name'])
    results[c['name']] = res
    print(f"[{c['label']}]")
    print(f"  Total Earthwork Volume J* = {res['cost']:.6f} m^2 (Raw discrete sum = {res['raw_sum']:.4f})")
    print(f"  Iskop (Cut) = {res['cut_vol']:.4f} m^2, Nasip (Fill) = {res['fill_vol']:.4f} m^2")
    print(f"  Max Slope |y'| = {np.max(np.abs(res['slopes'])):.4f} (limit = {c['b1']})")
    print(f"  Max Curvature |y''| = {np.max(np.abs(res['curvatures'])):.4f} (limit = {c['b2']})\n")

# 4. Publication Figures
print("--- Generating Publication Figures ---")

# Figure 3.1: Case A Comparison (N=20 vs N=100)
fig, ax = plt.subplots(figsize=(8, 5))
x_dense = np.linspace(0, L, 500)
h_dense = terrain(x_dense)
ax.plot(x_dense, h_dense, color=COLORS['dark_blue'], linewidth=2.2, label=r'Prirodni profil terena $h(x)$')

res_a20 = results['A_N20']
res_a100 = results['A_N100']
ax.plot(res_a20['x'], res_a20['y'], 's--', color=COLORS['amber_orange'], markersize=5,
        label=rf'Nivelacija $y(x)$, Slučaj A ($N=20$, $J^* = {res_a20["cost"]:.2f}$)')
ax.plot(res_a100['x'], res_a100['y'], '-', color=COLORS['accent_red'], linewidth=2.0,
        label=rf'Nivelacija $y(x)$, Slučaj A ($N=100$, $J^* = {res_a100["cost"]:.2f}$)')

# Fill cut and fill area for N=100
ax.fill_between(res_a100['x'], res_a100['h'], res_a100['y'],
                where=(res_a100['y'] < res_a100['h']),
                color=COLORS['amber_orange'], alpha=0.25, label='Iskop (Cut)')
ax.fill_between(res_a100['x'], res_a100['h'], res_a100['y'],
                where=(res_a100['y'] >= res_a100['h']),
                color=COLORS['forest_green'], alpha=0.25, label='Nasip (Fill)')

ax.set_xlim([0, 10])
ax.set_xlabel(r'Udaljenost $x$ [m]')
ax.set_ylabel(r'Nadmorska visina $y, h$ [m]')
ax.set_title(r'Zadatak 3: Optimalni uzdužni profil ceste — Slučaj A ($b_1 = 0.5, b_2 = 0.5$)')
ax.legend(loc='upper left', framealpha=0.92)
save_figure(fig, 'fig3_1_road_case_A')
plt.close(fig)

# Figure 3.2: Case B Comparison (N=20 vs N=100)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_dense, h_dense, color=COLORS['dark_blue'], linewidth=2.2, label=r'Prirodni profil terena $h(x)$')

res_b20 = results['B_N20']
res_b100 = results['B_N100']
ax.plot(res_b20['x'], res_b20['y'], 'd--', color=COLORS['purple'], markersize=5,
        label=rf'Nivelacija $y(x)$, Slučaj B ($N=20$, $J^* = {res_b20["cost"]:.2f}$)')
ax.plot(res_b100['x'], res_b100['y'], '-', color=COLORS['accent_red'], linewidth=2.0,
        label=rf'Nivelacija $y(x)$, Slučaj B ($N=100$, $J^* = {res_b100["cost"]:.2f}$)')

ax.fill_between(res_b100['x'], res_b100['h'], res_b100['y'],
                where=(res_b100['y'] < res_b100['h']),
                color=COLORS['amber_orange'], alpha=0.25, label='Iskop (Cut)')
ax.fill_between(res_b100['x'], res_b100['h'], res_b100['y'],
                where=(res_b100['y'] >= res_b100['h']),
                color=COLORS['forest_green'], alpha=0.25, label='Nasip (Fill)')

ax.set_xlim([0, 10])
ax.set_xlabel(r'Udaljenost $x$ [m]')
ax.set_ylabel(r'Nadmorska visina $y, h$ [m]')
ax.set_title(r'Zadatak 3: Optimalni uzdužni profil ceste — Slučaj B ($b_1 = 0.5, b_2 = 0.2$)')
ax.legend(loc='upper left', framealpha=0.92)
save_figure(fig, 'fig3_2_road_case_B')
plt.close(fig)

# Figure 3.3: Slope Profile |y'(x)| vs Limit b1
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(res_a100['x_slopes'], res_a100['slopes'], color=COLORS['primary_blue'], linewidth=1.8, label=r'Nagib $y^\prime(x)$ (Slučaj A, $N=100$)')
ax.plot(res_b100['x_slopes'], res_b100['slopes'], color=COLORS['accent_red'], linewidth=1.8, label=r'Nagib $y^\prime(x)$ (Slučaj B, $N=100$)')
ax.axhline(0.5, color='black', linestyle='--', linewidth=1.5, label=r'Maksimalni dozvoljeni nagib $\pm b_1 = \pm 0.5$')
ax.axhline(-0.5, color='black', linestyle='--', linewidth=1.5)

ax.set_xlim([0, 10])
ax.set_ylim([-0.65, 0.65])
ax.set_xlabel(r'Udaljenost $x$ [m]')
ax.set_ylabel(r'Nagib ceste $y^\prime(x)$ [m/m]')
ax.set_title(r'Zadatak 3: Provjera ograničenja prvog reda (nagib ceste)')
ax.legend(loc='lower left', framealpha=0.92)
save_figure(fig, 'fig3_3_road_slope_profile')
plt.close(fig)

# Figure 3.4: Curvature Profile |y''(x)| vs Limit b2
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(res_a100['x_curv'], res_a100['curvatures'], color=COLORS['primary_blue'], linewidth=1.6, label=r'Zakrivljenost $y^{\prime\prime}(x)$ (Slučaj A)')
ax.plot(res_b100['x_curv'], res_b100['curvatures'], color=COLORS['accent_red'], linewidth=1.6, label=r'Zakrivljenost $y^{\prime\prime}(x)$ (Slučaj B)')
ax.axhline(0.5, color=COLORS['primary_blue'], linestyle=':', linewidth=1.4, label=r'Granica $b_2 = 0.5$ (Slučaj A)')
ax.axhline(-0.5, color=COLORS['primary_blue'], linestyle=':', linewidth=1.4)
ax.axhline(0.2, color=COLORS['accent_red'], linestyle='--', linewidth=1.4, label=r'Granica $b_2 = 0.2$ (Slučaj B)')
ax.axhline(-0.2, color=COLORS['accent_red'], linestyle='--', linewidth=1.4)

ax.set_xlim([0, 10])
ax.set_ylim([-0.6, 0.6])
ax.set_xlabel(r'Udaljenost $x$ [m]')
ax.set_ylabel(r'Zakrivljenost ceste $y^{\prime\prime}(x)$ [1/m]')
ax.set_title(r'Zadatak 3: Provjera ograničenja drugog reda (zakrivljenost / udobnost vožnje)')
ax.legend(loc='lower left', framealpha=0.92)
save_figure(fig, 'fig3_4_road_curvature_profile')
plt.close(fig)

print("Task 3 complete.")
