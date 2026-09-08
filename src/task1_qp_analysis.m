%% Zadatak 1 - QP, konveksnost, KKT uvjeti, Lagrangeova dualnost, osjetljivost
%  min 1/2*x'*Q*x + c'*x   uz   G*x - h <= 0
%  Sve brojke koje se pojavljuju u poglavlju 2 seminara ispisuje ova skripta.

clear; close all; clc;
warning('off', 'MATLAB:print:ContentTypeImageSuggested');
addpath(fullfile(pwd, 'common'));   % skripte se pokrecu iz mape src
colors = config_plot();

%% 1. Podaci problema
Q = [ 2.0, -0.3;
     -0.3,  4.0];
c = [ 2.0; -3.0];
G = [-1.0, -1.0;
      1.0, -1.0];
h = [-10.0; 3.0];

fprintf('=== ZADATAK 1 ===\n');

%% (a) Konveksnost: svojstvene vrijednosti Hesseove matrice
lam = eig(Q);
fprintf('\n--- (a) Konveksnost ---\n');
fprintf('eig(Q) = %.6f, %.6f\n', lam(1), lam(2));
fprintf('det(Q) = %.6f,  Q > 0 : %d\n', det(Q), all(lam > 0));

%% (b) KKT: sve 4 kombinacije aktivnosti ogranicenja
fprintf('\n--- (b) KKT, 4 kombinacije aktivnosti ---\n');

% Slucaj 1: oba neaktivna  (mu = 0)
x0 = -Q\c;
fprintf('Slucaj 1 (0,0): x = [%.6f, %.6f], g1 = %.6f  -> %s\n', ...
    x0(1), x0(2), G(1,:)*x0 - h(1), 'odbacen (g1 > 0)');

% Slucaj 2: samo g1 aktivno
M2   = [Q, G(1,:)'; G(1,:), 0];
s2   = M2 \ [-c; h(1)];
x2   = s2(1:2); mu1 = s2(3);
g2v  = G(2,:)*x2 - h(2);
p2   = 0.5*x2'*Q*x2 + c'*x2;
fprintf('Slucaj 2 (1,0): x = [%.6f, %.6f], mu1 = %.6f, g2 = %.6f -> KKT OK\n', ...
    x2(1), x2(2), mu1, g2v);
fprintf('                p* = f(x*) = %.6f   (= 2000/33 = %.6f)\n', p2, 2000/33);

% Slucaj 3: samo g2 aktivno
M3  = [Q, G(2,:)'; G(2,:), 0];
s3  = M3 \ [-c; h(2)];
x3  = s3(1:2); mu2_3 = s3(3);
fprintf('Slucaj 3 (0,1): x = [%.6f, %.6f], mu2 = %.6f, g1 = %.6f -> odbacen\n', ...
    x3(1), x3(2), mu2_3, G(1,:)*x3 - h(1));

% Slucaj 4: oba aktivna
x4  = G \ h;
mu4 = -G' \ (Q*x4 + c);
fprintf('Slucaj 4 (1,1): x = [%.6f, %.6f], mu = [%.6f, %.6f] -> odbacen (mu2 < 0)\n', ...
    x4(1), x4(2), mu4(1), mu4(2));

% Gradijenti u optimumu
gradf = Q*x2 + c;
fprintf('grad f(x*) = [%.6f, %.6f];  -mu1*grad g1 = [%.6f, %.6f]\n', ...
    gradf(1), gradf(2), -mu1*G(1,1), -mu1*G(1,2));

%% (d) Numericko rjesenje - quadprog
fprintf('\n--- (d) MATLAB quadprog ---\n');
opts = optimoptions('quadprog', 'Display', 'none', 'Algorithm', 'interior-point-convex');
[x_qp, f_qp, ef_qp, ~, lam_qp] = quadprog(Q, c, G, h, [], [], [], [], [], opts);
assert(ef_qp == 1, 'quadprog nije konvergirao (exitflag = %d).', ef_qp);
fprintf('exitflag        = %d\n', ef_qp);
fprintf('x_opt           = [%.6f; %.6f]\n', x_qp(1), x_qp(2));
fprintf('p*  = fval      = %.6f\n', f_qp);
fprintf('lambda.ineqlin  = [%.6f; %.6f]\n', lam_qp.ineqlin(1), lam_qp.ineqlin(2));
fprintf('|x_qp - x_analiticki| = %.3e\n', norm(x_qp - x2));

%% (e) Dualni problem
%  theta(mu) = -1/2*mu'*G*Q^-1*G'*mu + (-c'*Q^-1*G' - h')*mu - 1/2*c'*Q^-1*c
%  max theta(mu) uz mu >= 0 je opet QP, pa se rjesava istom funkcijom quadprog.
fprintf('\n--- (e) Dualni problem (quadprog na -theta(mu), uz mu >= 0) ---\n');
Qi = inv(Q);
Hd = G*Qi*G';  Hd = 0.5*(Hd + Hd');   % numericka simetrizacija
fd = (c'*Qi*G' + h')';
kd = 0.5*(c'*Qi*c);
[mu_d, negd, ef_d] = quadprog(Hd, fd, [], [], [], [], [0;0], [], [], opts);
assert(ef_d == 1, 'quadprog (dual) nije konvergirao (exitflag = %d).', ef_d);
d_opt = -(negd + kd);
fprintf('exitflag        = %d\n', ef_d);
fprintf('mu*             = [%.6f; %.6f]\n', mu_d(1), mu_d(2));
fprintf('d*  = theta(mu*)= %.6f\n', d_opt);
fprintf('dualni procjep p* - d* = %.3e\n', f_qp - d_opt);

% Slaterova tocka
xs = [7; 6];
fprintf('Slaterova tocka x = [7; 6]: g1 = %.4f, g2 = %.4f\n', G(1,:)*xs - h(1), G(2,:)*xs - h(2));

%% (f) Osjetljivost: G*x - h <= v
fprintf('\n--- (f) Osjetljivost ---\n');
dlt = 1e-4;
[~, f_v1] = quadprog(Q, c, G, h + [dlt; 0], [], [], [], [], [], opts);
[~, f_v2] = quadprog(Q, c, G, h + [0; dlt], [], [], [], [], [], opts);
dp1 = (f_v1 - f_qp)/dlt;
dp2 = (f_v2 - f_qp)/dlt;
fprintf('dp*/dv1 numericki = %.6f,  -mu1* = %.6f,  odstupanje = %.2e\n', dp1, -mu1,   abs(dp1 + mu1));
fprintf('dp*/dv2 numericki = %.6f,  -mu2* = %.6f,  odstupanje = %.2e\n', dp2, 0.0,    abs(dp2));

%% (c) Slika 2.1 - dopustivi skup, nivo-krivulje, gradijenti u KKT tocki
fg = figure('Position', [100 100 720 600], 'Visible', 'off', 'Color', 'w');
[X1, X2] = meshgrid(linspace(-2, 11, 400), linspace(-2, 11, 400));
Z = 0.5*(Q(1,1)*X1.^2 + 2*Q(1,2)*X1.*X2 + Q(2,2)*X2.^2) + c(1)*X1 + c(2)*X2;

hold on;
% dopustivi skup F (neomedjen; ovdje odrezan na prikazani okvir)
Fx = [-1, 6.5, 11, 11, -1];
Fy = [11, 3.5,  8, 11, 11];
fill(Fx, Fy, colors.lightGray, 'EdgeColor', 'none', 'FaceAlpha', 0.72);
% nivo-krivulje funkcije cilja
contour(X1, X2, Z, 16, 'LineWidth', 0.75, 'LineColor', colors.gray);
% granice ogranicenja
t = linspace(-2, 11, 200);
plot(t, 10 - t,  '-',  'Color', colors.blue, 'LineWidth', 2.0);
plot(t, t - 3,   '-',  'Color', colors.red,  'LineWidth', 2.0);
% tocke
plot(x0(1), x0(2), 'o', 'Color', colors.dark, 'MarkerSize', 7, 'MarkerFaceColor', 'w', 'LineWidth', 1.2);
plot(x2(1), x2(2), 'p', 'Color', colors.green, 'MarkerSize', 15, 'MarkerFaceColor', colors.green);
% gradijenti (duljine su graficki skalirane)
sf = 0.22;
quiver(x2(1), x2(2), sf*gradf(1), sf*gradf(2), 0, 'Color', colors.dark, 'LineWidth', 2.2, 'MaxHeadSize', 0.5);
quiver(x2(1), x2(2), sf*mu1*G(1,1), sf*mu1*G(1,2), 0, 'LineWidth', 2.2, ...
       'LineStyle', '-', 'MaxHeadSize', 0.5, 'Color', colors.sky);
quiver(x2(1), x2(2), 1.7*G(2,1), 1.7*G(2,2), 0, 'LineWidth', 2.2, ...
       'LineStyle', '-', 'MaxHeadSize', 0.6, 'Color', colors.coral);
text(x2(1)+0.15, x2(2)+2.3,  '\nabla f(x^*)',                 'FontSize', 11, 'Color', colors.dark);
text(x2(1)-4.6,  x2(2)-3.6,  '\mu_1^*\nabla g_1(x^*)',        'FontSize', 11, 'Color', colors.sky);
text(x2(1)+1.1,  x2(2)-1.9,  '\nabla g_2(x^*),  \mu_2^* = 0', 'FontSize', 11, 'Color', colors.coral);
text(x0(1)+0.2,  x0(2)+0.35, 'x^0',                           'FontSize', 11);
text(x2(1)+0.25, x2(2)+0.35, 'x^*',                           'FontSize', 11);
xlim([-2 11]); ylim([-2 11]); axis square;
xlabel('x_1'); ylabel('x_2');
legend({'dopustivi skup F', 'nivo-krivulje f(x)', 'g_1(x) = 0', 'g_2(x) = 0', ...
        'x^0 (min. bez ogranicenja)', 'x^* (KKT tocka)'}, ...
       'Location', 'northeast', 'FontSize', 9);
exportgraphics(fg, fullfile(fig_dir(), 'fig1_1_qp_primal_geometry.pdf'), 'ContentType', 'vector');
exportgraphics(fg, fullfile(fig_dir(), 'fig1_1_qp_primal_geometry.png'), 'Resolution', 220);
close(fg);
fprintf('\nSlika 2.1 izvezena.\n');
