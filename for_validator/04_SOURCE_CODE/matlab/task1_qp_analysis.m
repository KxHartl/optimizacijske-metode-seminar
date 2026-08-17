%% Task 1: Quadratic Programming (QP) Analysis in MATLAB
% Solves primal QP, 4-case KKT resolution, Lagrange dual, sensitivity analysis, and generates plots

clear; close all; clc;
config_plot();

% 1. Problem matrices (f(x) = 0.5*x'*Q*x + c'*x)
Q = [2.0, -0.3; -0.3, 4.0];
c = [2.0; -3.0];
A = [-1.0, -1.0; 1.0, -1.0];
b = [-10.0; 3.0];

% 2. Strict convexity verification
lambda = eig(Q);
fprintf('Hessian Q eigenvalues: lambda_1 = %.6f, lambda_2 = %.6f\n', lambda(1), lambda(2));
if all(lambda > 0)
    fprintf('Matrix Q is strictly positive definite (Q > 0) -> f(x) is strictly convex.\n');
end

% 3. Numerical solution with quadprog
options = optimoptions('quadprog', 'Display', 'none', 'Algorithm', 'interior-point-convex');
[x_opt, f_opt, exitflag, output, lambda_qp] = quadprog(Q, c, A, b, [], [], [], [], [], options);

fprintf('\n--- Numerical quadprog Results ---\n');
fprintf('Optimal x* = [%.6f; %.6f]\n', x_opt(1), x_opt(2));
fprintf('Optimal cost p* = %.6f\n', f_opt);
fprintf('Lagrange multipliers mu* = [%.6f; %.6f]\n', lambda_qp.ineqlin(1), lambda_qp.ineqlin(2));

% 4. Analytical KKT Solution (Case 2: g1 active, g2 inactive)
M_kkt = [2.0, -0.3, -1.0; -0.3, 4.0, -1.0; -1.0, -1.0, 0.0];
rhs_kkt = [-2.0; 3.0; -10.0];
sol_kkt = M_kkt \ rhs_kkt;
x_analytical = sol_kkt(1:2);
mu1_analytical = sol_kkt(3);
p_analytical = 0.5 * x_analytical' * Q * x_analytical + c' * x_analytical;

fprintf('\n--- Analytical KKT Results ---\n');
fprintf('Analytical x* = [%.6f; %.6f]\n', x_analytical(1), x_analytical(2));
fprintf('Analytical mu1* = %.6f\n', mu1_analytical);
fprintf('Analytical p* = %.6f\n', p_analytical);

% 5. Dual Problem Maximization
Q_inv = inv(Q);
dual_obj = @(mu) -(-0.5 * (c + A'*mu)' * Q_inv * (c + A'*mu) - b'*mu);
mu0 = [1.0; 1.0];
opts_fmincon = optimoptions('fmincon', 'Display', 'none', 'Algorithm', 'interior-point');
[mu_dual_opt, neg_d_opt] = fmincon(dual_obj, mu0, [], [], [], [], [0; 0], [Inf; Inf], [], opts_fmincon);
d_opt = -neg_d_opt;

fprintf('\n--- Dual Optimization Results ---\n');
fprintf('Dual optimal mu* = [%.6f; %.6f]\n', mu_dual_opt(1), mu_dual_opt(2));
fprintf('Dual optimal d* = %.6f\n', d_opt);
fprintf('Duality gap |p* - d*| = %.2e\n', abs(f_opt - d_opt));

% 6. Sensitivity Analysis
delta = 1e-4;
b_pert = [-10.0 + delta; 3.0];
[x_pert, f_pert] = quadprog(Q, c, A, b_pert, [], [], [], [], [], options);
dp_db1_num = (f_pert - f_opt) / delta;
fprintf('\n--- Sensitivity Results ---\n');
fprintf('Numerical dp*/db1 = %.6f\n', dp_db1_num);
fprintf('Analytical -mu1*  = %.6f\n', -mu1_analytical);
fprintf('Absolute difference = %.2e\n', abs(dp_db1_num - (-mu1_analytical)));

% 7. MATLAB Plotting & Figure Export
fig_dir = fullfile('docs', 'figures');
if ~exist(fig_dir, 'dir'), mkdir(fig_dir); end

% Fig 1.1: Primal Geometry
figure('Position', [100, 100, 700, 600], 'Visible', 'off');
[X1, X2] = meshgrid(linspace(0, 10, 300), linspace(0, 10, 300));
Z = 0.5*(Q(1,1)*X1.^2 + 2*Q(1,2)*X1.*X2 + Q(2,2)*X2.^2) + c(1)*X1 + c(2)*X2;
contour(X1, X2, Z, 25, 'LineWidth', 1.2); hold on;

% Boundaries
x1_v = linspace(0, 10, 300);
plot(x1_v, 10 - x1_v, 'r-', 'LineWidth', 2.0, 'DisplayName', 'g_1(x) = 0');
plot(x1_v, x1_v - 3, 'g-', 'LineWidth', 2.0, 'DisplayName', 'g_2(x) = 0');
plot(x_opt(1), x_opt(2), 'rp', 'MarkerSize', 14, 'MarkerFaceColor', 'r', 'DisplayName', 'x^*');

% Gradients
grad_f = Q * x_opt + c;
quiver(x_opt(1), x_opt(2), 0.25*grad_f(1), 0.25*grad_f(2), 0, 'b', 'LineWidth', 2, 'DisplayName', '\nabla f(x^*)');
quiver(x_opt(1), x_opt(2), -1.8, -1.8, 0, 'r', 'LineWidth', 2, 'DisplayName', '\nabla g_1(x^*) (\mu_1^* = 12.242)');
quiver(x_opt(1), x_opt(2), 1.8, -1.8, 0, 'g--', 'LineWidth', 2, 'DisplayName', '\nabla g_2(x^*) (\mu_2^* = 0)');

xlim([0, 10]); ylim([0, 10]);
xlabel('x_1'); ylabel('x_2');
title('Zadatak 1: Geometrija QP problema i KKT ravnoteža gradijenata (MATLAB)');
legend('Location', 'northeast'); grid on;
exportgraphics(gcf, fullfile(fig_dir, 'fig1_1_qp_primal_geometry_matlab.png'), 'Resolution', 300);
close(gcf);
