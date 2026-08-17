%% Task 2: Robust Quadratic Programming in MATLAB
% Solves worst-case counterpart for interval uncertainty and performs Monte Carlo evaluation

clear; close all; clc;
config_plot();

% 1. Objective and nominal constraints
Q = [2.0, -0.3; -0.3, 4.0];
c = [2.0; -3.0];
A_nom = [-1.0, -1.0; 1.0, -1.0];
b_nom = [-10.0; 3.0];

% 2. Robust worst-case formulation over 8 vertices
sc = [0.85, 1.15];
A_rob = [];
b_rob = [];

for i = 1:size(A_nom, 1)
    for s1 = sc
        for s2 = sc
            A_rob = [A_rob; s1 * A_nom(i, 1), s2 * A_nom(i, 2)]; %#ok<AGROW>
            b_rob = [b_rob; b_nom(i)]; %#ok<AGROW>
        end
    end
end

fprintf('Number of robust constraints: %d\n', size(A_rob, 1));

% 3. Solve nominal and robust QP
options = optimoptions('quadprog', 'Display', 'none', 'Algorithm', 'interior-point-convex');
[x_nom, f_nom] = quadprog(Q, c, A_nom, b_nom, [], [], [], [], [], options);
[x_rob, f_rob] = quadprog(Q, c, A_rob, b_rob, [], [], [], [], [], options);

fprintf('Nominal Solution x_nom* = [%.6f; %.6f], f = %.6f\n', x_nom(1), x_nom(2), f_nom);
fprintf('Robust Solution x_rob*  = [%.6f; %.6f], f = %.6f\n', x_rob(1), x_rob(2), f_rob);

% Analytical solution:
% x1_rob = 6.5, x2_rob = 179/34 = 5.264706
x_rob_analyt = [6.5; 179/34];
f_rob_analyt = 0.5 * x_rob_analyt' * Q * x_rob_analyt + c' * x_rob_analyt;
fprintf('Analytical Robust x*    = [%.6f; %.6f], f = %.6f\n', x_rob_analyt(1), x_rob_analyt(2), f_rob_analyt);
fprintf('Discrepancy (norm)      = %.2e\n', norm(x_rob - x_rob_analyt));

% KKT multiplier verification
grad_f_rob = Q * x_rob_analyt + c;
A_act = [-0.85, -0.85; 1.15, -0.85];
mu_rob = A_act' \ (-grad_f_rob);
fprintf('Robust KKT Multipliers: mu1* = %.6f, mu2* = %.6f\n', mu_rob(1), mu_rob(2));

% 4. Monte Carlo Evaluation
rng(42);
num_samples = 100;
violations_nom = 0;
violations_rob = 0;

for k = 1:num_samples
    s11 = (0.85 + 0.30 * rand()) * A_nom(1, 1);
    s12 = (0.85 + 0.30 * rand()) * A_nom(1, 2);
    s21 = (0.85 + 0.30 * rand()) * A_nom(2, 1);
    s22 = (0.85 + 0.30 * rand()) * A_nom(2, 2);
    A_k = [s11, s12; s21, s22];
    
    if any(A_k * x_nom - b_nom > 1e-7)
        violations_nom = violations_nom + 1;
    end
    if any(A_k * x_rob - b_nom > 1e-7)
        violations_rob = violations_rob + 1;
    end
end

fprintf('\n--- Monte Carlo Results (N=%d) ---\n', num_samples);
fprintf('Nominal failure rate: %d/%d (%.1f%%)\n', violations_nom, num_samples, (violations_nom/num_samples)*100);
fprintf('Robust failure rate:  %d/%d (%.1f%%)\n', violations_rob, num_samples, (violations_rob/num_samples)*100);
