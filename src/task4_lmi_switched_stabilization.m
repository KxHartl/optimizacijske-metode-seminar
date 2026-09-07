%% Zadatak 4 - Sklopni linearni sustav: analiza i LMI stabilizacija
%  xdot = A(t)x + Bu,  A(t) = A_parno za floor(t) paran, A_neparno inace
%  Sve brojke koje se pojavljuju u poglavlju 5 seminara ispisuje ova skripta.

clear; close all; clc;
warning('off', 'MATLAB:print:ContentTypeImageSuggested');
addpath(fullfile(pwd, 'common'));   % skripte se pokrecu iz mape src
config_plot();

if isempty(which('sdpvar'))
    error(['YALMIP nije na MATLAB path-u. Instalirati ga u fullfile(userpath,''YALMIP'') ' ...
           'i dodati addpath(genpath(...)) u startup.m.']);
end

A_par = [-1, -pi/6;   3*pi/2, -1];
A_nep = [-1, -3*pi/2; pi/6,   -1];
B     = [1; 0];
x0    = [1; 0];
T     = 20;

fprintf('=== ZADATAK 4 ===\n');

%% (a) Svojstvene vrijednosti pojedinih modova
ep = eig(A_par);  en = eig(A_nep);
fprintf('\n--- (a) Stabilnost modova ---\n');
fprintf('eig(A_parno)   = %.6f %+.6fi,  %.6f %+.6fi\n', real(ep(1)), imag(ep(1)), real(ep(2)), imag(ep(2)));
fprintf('eig(A_neparno) = %.6f %+.6fi,  %.6f %+.6fi\n', real(en(1)), imag(en(1)), real(en(2)), imag(en(2)));
fprintf('pi/2 = %.6f -> obje matrice su Hurwitzove (Re = -1 < 0)\n', pi/2);

%% (b) Monodromijska matrica
Phi_p = expm(A_par);  Phi_n = expm(A_nep);  Phi_c = Phi_n*Phi_p;
ec    = eig(Phi_c);   rho = max(abs(ec));
fprintf('\n--- (b) Monodromijska matrica ---\n');
fprintf('Phi_parno   = [%9.6f %9.6f; %9.6f %9.6f]   (e^-1/3 = %.6f, 3e^-1 = %.6f)\n', ...
        Phi_p(1,1), Phi_p(1,2), Phi_p(2,1), Phi_p(2,2), exp(-1)/3, 3*exp(-1));
fprintf('Phi_neparno = [%9.6f %9.6f; %9.6f %9.6f]\n', Phi_n(1,1), Phi_n(1,2), Phi_n(2,1), Phi_n(2,2));
fprintf('Phi_cycle   = [%9.6f %9.6f; %9.6f %9.6f]   (-9e^-2 = %.6f, -e^-2/9 = %.6f)\n', ...
        Phi_c(1,1), Phi_c(1,2), Phi_c(2,1), Phi_c(2,2), -9*exp(-2), -exp(-2)/9);
fprintf('det(Phi_cycle) = %.6f   (e^-4 = %.6f)\n', det(Phi_c), exp(-4));
fprintf('rho(Phi_cycle) = %.6f  > 1  -> sklopni sustav NIJE stabilan\n', rho);

%% (c) LMI sinteza regulatora (YALMIP + SDPT3)
% LMI je homogen u (Q, Y): ako je (Q, Y) dopustiv, dopustiv je i (tQ, tY), t > 0,
% uz isti K = Y*Q^-1. Zato se stroge nejednakosti normiraju parom Q >= I,
% M_i <= -I, a medju dopustivim parovima bira se onaj s najmanjim ||Y|| (najmanje pojacanje).
n = 2;  m = 1;
Qv = sdpvar(n, n, 'symmetric');
Yv = sdpvar(m, n, 'full');
F  = [Qv >= eye(n), ...
      A_par*Qv + Qv*A_par' + B*Yv + Yv'*B' <= -eye(n), ...
      A_nep*Qv + Qv*A_nep' + B*Yv + Yv'*B' <= -eye(n)];
sol = optimize(F, norm(Yv, 2), sdpsettings('solver', 'sdpt3', 'verbose', 0));
assert(sol.problem == 0, 'SDP nije rijesen: %s', sol.info);

Qs = value(Qv);  Ys = value(Yv);
P  = inv(Qs);    K  = Ys*P;

fprintf('\n--- (c) LMI sinteza (YALMIP + SDPT3) ---\n');
fprintf('status : %s\n', sol.info);
fprintf('Q = [%9.6f %9.6f; %9.6f %9.6f]\n', Qs(1,1), Qs(1,2), Qs(2,1), Qs(2,2));
fprintf('Y = [%9.6f %9.6f]\n', Ys(1), Ys(2));
fprintf('P = [%9.6f %9.6f; %9.6f %9.6f],  eig(P) = %.6f, %.6f\n', ...
        P(1,1), P(1,2), P(2,1), P(2,2), min(eig(P)), max(eig(P)));
fprintf('K = [%9.6f %9.6f]\n', K(1), K(2));

Acl_p = A_par + B*K;  Acl_n = A_nep + B*K;
evp = eig(Acl_p);  evn = eig(Acl_n);
fprintf('A_cl,parno   = [%9.6f %9.6f; %9.6f %9.6f]\n', Acl_p(1,1), Acl_p(1,2), Acl_p(2,1), Acl_p(2,2));
fprintf('A_cl,neparno = [%9.6f %9.6f; %9.6f %9.6f]\n', Acl_n(1,1), Acl_n(1,2), Acl_n(2,1), Acl_n(2,2));
fprintf('eig(A_cl,parno)   = %.6f %+.6fi ,  %.6f %+.6fi\n', ...
        real(evp(1)), imag(evp(1)), real(evp(2)), imag(evp(2)));
fprintf('eig(A_cl,neparno) = %.6f %+.6fi ,  %.6f %+.6fi\n', ...
        real(evn(1)), imag(evn(1)), real(evn(2)), imag(evn(2)));

Mp = Acl_p'*P + P*Acl_p;  Mn = Acl_n'*P + P*Acl_n;
fprintf('lambda_max(A_cl,parno''P + P A_cl,parno)     = %.6f  < 0\n', max(eig(Mp)));
fprintf('lambda_max(A_cl,neparno''P + P A_cl,neparno) = %.6f  < 0\n', max(eig(Mn)));
rho_cl = max(abs(eig(expm(Acl_n)*expm(Acl_p))));
fprintf('rho(Phi_cl,cycle) = %.6f  << 1\n', rho_cl);

% Zajamcena eksponencijalna stopa iz Vdot <= -2*alpha*V  (poopcena svojstvena vrijednost)
alpha = 0.5*min(-max(eig(Mp, P)), -max(eig(Mn, P)));
fprintf('alpha = %.6f 1/s  ->  V(x(t)) <= V(x(0))*exp(-2*alpha*t)\n', alpha);
fprintf('sqrt(cond(P)) = %.6f  ->  ||x(t)|| <= %.4f*exp(-%.4f*t)*||x(0)||\n', sqrt(cond(P)), sqrt(cond(P)), alpha);

%% Simulacija sklopnog sustava (ode45 po segmentima od 1 s)
    function [tt, xx] = sim_switched(Amat_p, Amat_n, x_init, Tend)
        tt = [];  xx = [];  xc = x_init;
        for kseg = 0:Tend-1
            if mod(kseg, 2) == 0, Aa = Amat_p; else, Aa = Amat_n; end
            o = odeset('RelTol', 1e-9, 'AbsTol', 1e-11);
            [ts, xs] = ode45(@(t, x) Aa*x, [kseg, kseg+1], xc, o);
            tt = [tt; ts];  xx = [xx; xs];  xc = xs(end,:)';   %#ok<AGROW>
        end
    end

[t_ol, x_ol] = sim_switched(A_par, A_nep, x0, T);
[t_cl, x_cl] = sim_switched(Acl_p, Acl_n, x0, T);
fprintf('\n--- Simulacija (x(0) = [1; 0], ode45, RelTol 1e-9) ---\n');
fprintf('otvoreni krug : ||x(20)|| = %.4e\n', norm(x_ol(end,:)));
fprintf('zatvoreni krug: ||x(5)||  = %.4e,  ||x(20)|| = %.4e\n', ...
        norm(x_cl(find(t_cl >= 5, 1),:)), norm(x_cl(end,:)));

%% Slika 5.1 - otvoreni krug
fg = figure('Position', [100 100 900 380], 'Visible', 'off', 'Color', 'w');
subplot(1,2,1); hold on;
plot(t_ol, x_ol(:,1), 'k-',  'LineWidth', 1.6);
plot(t_ol, x_ol(:,2), 'k--', 'LineWidth', 1.6);
xlabel('t [s]'); ylabel('x_1(t),  x_2(t)'); xlim([0 T]);
legend({'x_1(t)', 'x_2(t)'}, 'Location', 'northwest', 'FontSize', 9);
subplot(1,2,2); hold on;
plot(x_ol(:,1), x_ol(:,2), 'k-', 'LineWidth', 1.2);
plot(x0(1), x0(2), 'ko', 'MarkerSize', 7, 'MarkerFaceColor', 'k');
xlabel('x_1'); ylabel('x_2'); axis square;
exportgraphics(fg, fullfile(fig_dir(), 'fig4_1_open_loop_divergence.pdf'), 'ContentType', 'vector');
close(fg);

%% Slika 5.2 - zatvoreni krug
Tc = 8;
sel = t_cl <= Tc;
fg = figure('Position', [100 100 900 380], 'Visible', 'off', 'Color', 'w');
subplot(1,2,1); hold on;
plot(t_cl(sel), x_cl(sel,1), 'k-',  'LineWidth', 1.6);
plot(t_cl(sel), x_cl(sel,2), 'k--', 'LineWidth', 1.6);
xlabel('t [s]'); ylabel('x_1(t),  x_2(t)'); xlim([0 Tc]);
legend({'x_1(t)', 'x_2(t)'}, 'Location', 'northeast', 'FontSize', 9);
subplot(1,2,2); hold on;
th = linspace(0, 2*pi, 300);
for lev = [x0'*P*x0, 0.25*x0'*P*x0, 0.05*x0'*P*x0]
    Rc = chol(P/lev);  E = Rc\[cos(th); sin(th)];
    plot(E(1,:), E(2,:), ':', 'Color', [0.55 0.55 0.55], 'LineWidth', 1.0);
end
plot(x_cl(sel,1), x_cl(sel,2), 'k-', 'LineWidth', 1.4);
plot(x0(1), x0(2), 'ko', 'MarkerSize', 7, 'MarkerFaceColor', 'k');
xlabel('x_1'); ylabel('x_2'); axis square;
legend({'x^{T}Px = c', '', '', 'trajektorija'}, 'Location', 'southwest', 'FontSize', 9);
exportgraphics(fg, fullfile(fig_dir(), 'fig4_2_closed_loop_stabilization.pdf'), 'ContentType', 'vector');
close(fg);
fprintf('\nSlike 5.1-5.2 izvezene.\n');
