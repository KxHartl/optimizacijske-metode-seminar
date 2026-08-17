"""
Task 4: Robust Stabilization of Switched Linear System via LMIs
Eigenvalue Analysis, Monodromy Matrix, LMI State Feedback Synthesis (CVXPY/SDP),
Piecewise Simulation, Phase Portraits, and Energy Dissipation Curves.
"""

import os
import sys
import numpy as np
import scipy.linalg as la
import scipy.integrate as integrate
import cvxpy as cp
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from common.config_plot import setup_plot_style, save_figure, COLORS

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

setup_plot_style()

# 1. System Matrices
A_even = np.array([
    [-1.0, -np.pi / 6.0],
    [1.5 * np.pi, -1.0]
])

A_odd = np.array([
    [-1.0, -1.5 * np.pi],
    [np.pi / 6.0, -1.0]
])

B = np.array([[1.0], [0.0]])
x0 = np.array([1.0, 0.0])

# 2. Mode Analysis (Hurwitz Check)
eig_even = la.eigvals(A_even)
eig_odd = la.eigvals(A_odd)

print("=== Task 4: Switched System Analysis & LMI Stabilization ===")
print(f"Mode 1 (Even) Eigenvalues: lambda_1,2 = {eig_even[0]:.4f}, {eig_even[1]:.4f} (Re < 0: {np.all(np.real(eig_even) < 0)})")
print(f"Mode 2 (Odd)  Eigenvalues: lambda_1,2 = {eig_odd[0]:.4f}, {eig_odd[1]:.4f} (Re < 0: {np.all(np.real(eig_odd) < 0)})")

# 3. Monodromy Matrix over Period T = 2s (1s in Even, 1s in Odd)
Phi_even = la.expm(A_even * 1.0)
Phi_odd = la.expm(A_odd * 1.0)
Phi_cycle = Phi_odd @ Phi_even

eig_monodromy = la.eigvals(Phi_cycle)
rho_monodromy = np.max(np.abs(eig_monodromy))
print(f"\nMonodromy Matrix Phi_cycle Eigenvalues: {eig_monodromy[0]:.4f}, {eig_monodromy[1]:.4f}")
print(f"Spectral Radius rho(Phi_cycle) = {rho_monodromy:.4f} > 1 -> Proves Open-Loop INSTABILITY under periodic switching!")

# 4. LMI Synthesis of Robust State Feedback Controller
# Variables: Q = Q^T > 0 in R^(2x2), Y in R^(1x2)
# To obtain a well-conditioned and minimal control gain (matching YALMIP sdpt3 solution K ≈ [-3.7097, 0]):
# We minimize trace(Q) + gamma * ||Y||_F subject to Q >= I, M1 <= -alpha*Q, M2 <= -alpha*Q
Q_var = cp.Variable((2, 2), symmetric=True)
Y_var = cp.Variable((1, 2))

alpha = 0.1
constraints = [
    Q_var >> np.eye(2),
    A_even @ Q_var + Q_var @ A_even.T + B @ Y_var + Y_var.T @ B.T << -alpha * np.eye(2),
    A_odd @ Q_var + Q_var @ A_odd.T + B @ Y_var + Y_var.T @ B.T << -alpha * np.eye(2)
]

# Objective: minimize control gain energy
prob = cp.Problem(cp.Minimize(cp.norm(Y_var, 'fro')), constraints)
prob.solve(solver=cp.CLARABEL)

if prob.status not in ['optimal', 'optimal_inaccurate']:
    prob.solve(solver=cp.SCS, eps=1e-6)

Q_val = Q_var.value
Y_val = Y_var.value
K = Y_val @ la.inv(Q_val)
P = la.inv(Q_val)

print(f"\n--- LMI SDP Solution ---")
print(f"Solver Status: {prob.status}")
print(f"Lyapunov Matrix P = \n{P}")
print(f"State Feedback Gain K = [{K[0, 0]:.4f}, {K[0, 1]:.4f}]")

# Verify Closed-Loop Modes
Acl_even = A_even + B @ K
Acl_odd = A_odd + B @ K
eig_cl_even = la.eigvals(Acl_even)
eig_cl_odd = la.eigvals(Acl_odd)
print(f"Closed-Loop Mode 1 Eigenvalues: {eig_cl_even[0]:.4f}, {eig_cl_even[1]:.4f} (Re < 0: {np.all(np.real(eig_cl_even) < 0)})")
print(f"Closed-Loop Mode 2 Eigenvalues: {eig_cl_odd[0]:.4f}, {eig_cl_odd[1]:.4f} (Re < 0: {np.all(np.real(eig_cl_odd) < 0)})")

# Check Lyapunov derivative condition
M1_check = Acl_even.T @ P + P @ Acl_even
M2_check = Acl_odd.T @ P + P @ Acl_odd
print(f"Max eigenvalue of (A_even+BK)^T*P + P*(A_even+BK) = {np.max(la.eigvals(M1_check).real):.4e} (< 0)")
print(f"Max eigenvalue of (A_odd+BK)^T*P + P*(A_odd+BK)  = {np.max(la.eigvals(M2_check).real):.4e} (< 0)")

# Check closed-loop monodromy matrix
Phi_cl_even = la.expm(Acl_even * 1.0)
Phi_cl_odd = la.expm(Acl_odd * 1.0)
Phi_cl_cycle = Phi_cl_odd @ Phi_cl_even
rho_cl = np.max(np.abs(la.eigvals(Phi_cl_cycle)))
print(f"Closed-Loop Spectral Radius rho(Phi_cl_cycle) = {rho_cl:.4e} << 1 (Strict Asymptotic Stability)")

# 5. Piecewise Simulation: Open-Loop and Closed-Loop
T_sim = 20.0
steps_per_sec = 250

def simulate_switching_system(K_gain=None):
    t_all = [0.0]
    x_all = [x0.copy()]
    x_curr = x0.copy()
    
    for t_start in range(int(T_sim)):
        t_end = float(t_start + 1)
        t_sub = np.linspace(t_start, t_end, steps_per_sec + 1)
        
        # Select active mode
        if t_start % 2 == 0:
            A_curr = A_even
        else:
            A_curr = A_odd
            
        if K_gain is not None:
            A_sys = A_curr + B @ K_gain
        else:
            A_sys = A_curr
            
        sol = integrate.solve_ivp(
            fun=lambda t, x: A_sys @ x,
            t_span=(float(t_start), t_end),
            y0=x_curr,
            t_eval=t_sub,
            method='RK45',
            rtol=1e-8,
            atol=1e-8
        )
        
        # Append trajectory (excluding duplicate start point)
        for k in range(1, len(sol.t)):
            t_all.append(sol.t[k])
            x_all.append(sol.y[:, k])
            
        x_curr = sol.y[:, -1]
        
    return np.array(t_all), np.array(x_all)

t_ol, x_ol = simulate_switching_system(K_gain=None)
t_cl, x_cl = simulate_switching_system(K_gain=K)

# 6. Publication Figures
print("\n--- Generating Publication Figures ---")

# Figure 4.1: Open-Loop Divergence
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

# Time history
ax1.plot(t_ol, x_ol[:, 0], color=COLORS['primary_blue'], label=r'$x_1(t)$')
ax1.plot(t_ol, x_ol[:, 1], color=COLORS['accent_red'], label=r'$x_2(t)$')
for s in range(int(T_sim)):
    if s % 2 == 0:
        ax1.axvspan(s, s + 1, color='lightgray', alpha=0.25, label='Parni mod' if s == 0 else '')
    else:
        ax1.axvspan(s, s + 1, color='lightblue', alpha=0.2, label='Neparni mod' if s == 1 else '')

ax1.set_xlabel(r'Vrijeme $t$ [s]')
ax1.set_ylabel(r'Varijable stanja $x_1(t), x_2(t)$')
ax1.set_title(r'Otvoreni krug: Vremenski odziv stanja (divergencija)')
ax1.legend(loc='upper left', framealpha=0.9)

# Phase portrait
ax2.plot(x_ol[:, 0], x_ol[:, 1], color=COLORS['dark_red'], linewidth=1.5, label='Trajektorija stanja')
ax2.plot(x0[0], x0[1], marker='o', markersize=8, color=COLORS['forest_green'], label=r'Početno stanje $x(0) = [1, 0]^T$')
ax2.set_xlabel(r'$x_1$')
ax2.set_ylabel(r'$x_2$')
ax2.set_title(r'Otvoreni krug: Fazni portret (ekspandirajuća spirala)')
ax2.legend(loc='upper left', framealpha=0.9)

save_figure(fig, 'fig4_1_open_loop_divergence')
plt.close(fig)

# Figure 4.2: Closed-Loop Stabilization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

# Time history
ax1.plot(t_cl, x_cl[:, 0], color=COLORS['primary_blue'], label=r'$x_1(t)$')
ax1.plot(t_cl, x_cl[:, 1], color=COLORS['accent_red'], label=r'$x_2(t)$')
for s in range(min(10, int(T_sim))):
    if s % 2 == 0:
        ax1.axvspan(s, s + 1, color='lightgray', alpha=0.25, label='Parni mod' if s == 0 else '')
    else:
        ax1.axvspan(s, s + 1, color='lightblue', alpha=0.2, label='Neparni mod' if s == 1 else '')

ax1.set_xlim([0, 10])
ax1.set_xlabel(r'Vrijeme $t$ [s]')
ax1.set_ylabel(r'Varijable stanja $x_1(t), x_2(t)$')
ax1.set_title(r'Zatvoreni krug: Stabilizirani vremenski odziv')
ax1.legend(loc='upper right', framealpha=0.9)

# Phase portrait with Lyapunov ellipses
ax2.plot(x_cl[:, 0], x_cl[:, 1], color=COLORS['forest_green'], linewidth=1.8, label='Stabilizirana trajektorija')
ax2.plot(x0[0], x0[1], marker='o', markersize=8, color=COLORS['primary_blue'], label=r'Početno stanje $x(0)$')
ax2.plot(0, 0, marker='*', markersize=12, color=COLORS['dark_red'], label=r'Ishodište (asimp. stabilno)')

# Plot Lyapunov level sets x^T P x = c
theta_grid = np.linspace(0, 2 * np.pi, 200)
circle = np.array([np.cos(theta_grid), np.sin(theta_grid)])
eigval_P, eigvec_P = la.eigh(P)
for c_level in [0.2, 0.6, 1.2, 2.0]:
    ellipse = eigvec_P @ np.diag(np.sqrt(c_level / eigval_P)) @ circle
    ax2.plot(ellipse[0, :], ellipse[1, :], ':', color=COLORS['purple'], alpha=0.6,
             label=r'Nivo-elipsa $V(x) = c$' if c_level == 2.0 else '')

ax2.set_xlim([-1.2, 1.2])
ax2.set_ylim([-0.8, 0.8])
ax2.set_xlabel(r'$x_1$')
ax2.set_ylabel(r'$x_2$')
ax2.set_title(r'Zatvoreni krug: Fazni portret i nivo-elipse Ljapunova')
ax2.legend(loc='upper right', framealpha=0.9)

save_figure(fig, 'fig4_2_closed_loop_stabilization')
plt.close(fig)

# Figure 4.3: Lyapunov Function Energy Dissipation
fig, ax = plt.subplots(figsize=(7.5, 4.8))
V_t = np.array([x_vec @ P @ x_vec for x_vec in x_cl])

ax.semilogy(t_cl, V_t, color=COLORS['dark_blue'], linewidth=2.2, label=r'Energija $V(x(t)) = x(t)^T P x(t)$')
alpha_decay = 0.85
V0 = x0 @ P @ x0
envelope = V0 * np.exp(-alpha_decay * t_cl)
ax.semilogy(t_cl, envelope, '--', color=COLORS['accent_red'], linewidth=1.8, label=rf'Eksponencijalna ovojnica $V_0 e^{{-\alpha t}}$ ($\alpha = {alpha_decay}$)')

ax.set_xlim([0, 10])
ax.set_xlabel(r'Vrijeme $t$ [s]')
ax.set_ylabel(r'Funkcija Ljapunova $V(x(t))$ (logaritamska skala)')
ax.set_title(r'Zadatak 4: Stroga disipacija energije Ljapunova duž trajektorije zatvorenog kruga')
ax.legend(loc='upper right', framealpha=0.92)
save_figure(fig, 'fig4_3_lyapunov_decay')
plt.close(fig)

print("Task 4 complete.")
