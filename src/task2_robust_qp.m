%% Zadatak 2 - Robusni QP uz intervalnu nesigurnost koeficijenata (+-15 %)
%  Nominalni problem iz Zadatka 1; koeficijenti matrice G nesigurni.
%  Sve brojke koje se pojavljuju u poglavlju 3 seminara ispisuje ova skripta.

clear; close all; clc;
warning('off', 'MATLAB:print:ContentTypeImageSuggested');
addpath(fullfile(pwd, 'common'));   % skripte se pokrecu iz mape src
config_plot();

%% 1. Nominalni podaci
Q = [2.0, -0.3; -0.3, 4.0];
c = [2.0; -3.0];
G = [-1.0, -1.0; 1.0, -1.0];
h = [-10.0; 3.0];
sc = [0.85, 1.15];

fprintf('=== ZADATAK 2 ===\n');

%% 2. Vrhovi skupova nesigurnosti -> 8 determinsitickih nejednakosti
G_rob = []; h_rob = [];
for i = 1:2
    for s1 = sc
        for s2 = sc
            G_rob(end+1, :) = [s1*G(i,1), s2*G(i,2)];  %#ok<SAGROW>
            h_rob(end+1, 1) = h(i);                    %#ok<SAGROW>
        end
    end
end
fprintf('\n--- Vrhovi skupa nesigurnosti (%d nejednakosti) ---\n', size(G_rob,1));
for k = 1:size(G_rob,1)
    fprintf('  %6.2f*x1 %+6.2f*x2 <= %6.2f\n', G_rob(k,1), G_rob(k,2), h_rob(k));
end

%% 3. Robusni QP
opts = optimoptions('quadprog', 'Display', 'none', 'Algorithm', 'interior-point-convex');
[x_rob, f_rob_q, ef, ~, lam_rob] = quadprog(Q, c, G_rob, h_rob, [], [], [], [], [], opts);
assert(ef == 1, 'quadprog nije konvergirao (exitflag = %d).', ef);
f_rob = 0.5*x_rob'*Q*x_rob + c'*x_rob;
fprintf('\n--- Robusni QP (quadprog) ---\n');
fprintf('exitflag  = %d\n', ef);
fprintf('x_rob*    = [%.6f; %.6f]   (analiticki [13/2; 179/34] = [%.6f; %.6f])\n', ...
        x_rob(1), x_rob(2), 13/2, 179/34);
fprintf('f(x_rob*) = %.6f            (analiticki 978253/11560 = %.6f)\n', f_rob, 978253/11560);
fprintf('max(G_rob*x - h_rob) = %.3e\n', max(G_rob*x_rob - h_rob));

%% 4. Provjera: je li dovoljno samo najgore g1?
G1w = [-0.85, -0.85];
[x_g1, ~, ef1] = quadprog(Q, c, G1w, h(1), [], [], [], [], [], opts);
fprintf('\n--- Provjera aktivnosti ---\n');
fprintf('Samo g1^wc aktivno: x = [%.4f, %.4f], g2^wc(x) = %+.4f -> %s\n', ...
        x_g1(1), x_g1(2), [1.15 -0.85]*x_g1 - 3, 'nedopustivo');

%% 5. KKT provjera u x_rob*: svih 8 nejednakosti + mnozitelji
gradf = Q*x_rob + c;
act   = find(abs(G_rob*x_rob - h_rob) < 1e-6);
mu_a  = -G_rob(act,:)' \ gradf;
fprintf('grad f(x_rob*) = [%.6f, %.6f]\n', gradf(1), gradf(2));
fprintf('aktivni vrhovi : %s\n', mat2str(act'));
fprintf('mu aktivnih    = [%.6f, %.6f]  (> 0)\n', mu_a(1), mu_a(2));
fprintf('\n  k |   G_rob(k,:)*x_rob   |  h  |  slack  | status\n');
for k = 1:size(G_rob,1)
    sl = h_rob(k) - G_rob(k,:)*x_rob;
    if abs(sl) < 1e-6, st = 'aktivno'; else, st = 'slack'; end
    fprintf(' %2d |       %9.4f     | %4.0f | %7.4f | %s\n', k, G_rob(k,:)*x_rob, h_rob(k), sl, st);
end

%% 6. Usporedba s nominalnim rjesenjem
[x_nom, ~] = quadprog(Q, c, G, h, [], [], [], [], [], opts);
f_nom = 0.5*x_nom'*Q*x_nom + c'*x_nom;
fprintf('\n--- Usporedba s nominalnim rjesenjem ---\n');
fprintf('x_nom* = [%.6f; %.6f], f = %.6f\n', x_nom(1), x_nom(2), f_nom);
fprintf('x_rob* = [%.6f; %.6f], f = %.6f\n', x_rob(1), x_rob(2), f_rob);
fprintf('porast f = %.6f  (%.2f %%)\n', f_rob - f_nom, 100*(f_rob - f_nom)/f_nom);

%% 7. Monte Carlo provjera dopustivosti
rng(42);
Nmc  = 100;
viol_nom = 0; viol_rob = 0;
Gs = zeros(2,2,Nmc);
for k = 1:Nmc
    S = 0.85 + 0.30*rand(2,2);          % skalari s ~ U(0.85, 1.15)
    Gk = G .* S;
    Gs(:,:,k) = Gk;
    if any(Gk*x_nom - h > 1e-12), viol_nom = viol_nom + 1; end
    if any(Gk*x_rob - h > 1e-12), viol_rob = viol_rob + 1; end
end
fprintf('\n--- Monte Carlo (N = %d, rng(42)) ---\n', Nmc);
fprintf('krsenja za x_nom* : %d / %d\n', viol_nom, Nmc);
fprintf('krsenja za x_rob* : %d / %d\n', viol_rob, Nmc);

%% 8. Slika 3.1 - realizacije, robusne granice, oba optimuma
fg = figure('Position', [100 100 720 600], 'Visible', 'off', 'Color', 'w');
hold on;
t = linspace(0, 14, 200);
hMC = [];
for k = 1:Nmc
    Gk = Gs(:,:,k);
    y1 = (h(1) - Gk(1,1)*t)/Gk(1,2);
    y2 = (h(2) - Gk(2,1)*t)/Gk(2,2);
    p1 = plot(t, y1, '-', 'Color', [0.78 0.78 0.78], 'LineWidth', 0.5);
    plot(t, y2, '-', 'Color', [0.78 0.78 0.78], 'LineWidth', 0.5);
    if k == 1, hMC = p1; end
end
hNomB = plot(t, 10 - t, 'k--', 'LineWidth', 1.6);
plot(t, t - 3, 'k--', 'LineWidth', 1.6);
hRobB = plot(t, 10/0.85 - t, 'k-', 'LineWidth', 2.2);
plot(t, (1.15*t - 3)/0.85, 'k-', 'LineWidth', 2.2);
hNom  = plot(x_nom(1), x_nom(2), 'ko', 'MarkerSize', 9, 'MarkerFaceColor', 'w', 'LineWidth', 1.6);
hRob  = plot(x_rob(1), x_rob(2), 'kp', 'MarkerSize', 16, 'MarkerFaceColor', 'k');
text(x_nom(1)-1.7, x_nom(2)-0.5, 'x^*_{nom}', 'FontSize', 11);
text(x_rob(1)+0.3, x_rob(2)+0.4, 'x^*_{rob}', 'FontSize', 11);
xlim([0 12]); ylim([0 12]); axis square;
xlabel('x_1'); ylabel('x_2');
legend([hMC hNomB hRobB hNom hRob], ...
       {'100 slucajnih realizacija', 'nominalne granice', 'granice najgoreg slucaja', ...
        'nominalni optimum', 'robusni optimum'}, 'Location', 'northeast', 'FontSize', 9);
exportgraphics(fg, fullfile(fig_dir(), 'fig2_1_robust_envelope_monte_carlo.pdf'), 'ContentType', 'vector');
close(fg);
fprintf('\nSlika 3.1 izvezena.\n');
