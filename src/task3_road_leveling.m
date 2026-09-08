%% Zadatak 3 - Optimalna nivelacija uzduznog profila ceste (LP)
%  min dx*sum(z)  uz  -z <= y - h <= z, |D1*y| <= b1, |D2*y| <= b2, y0 = a, yN = b
%  Sve brojke koje se pojavljuju u poglavlju 4 seminara ispisuje ova skripta.

clear; close all; clc;
warning('off', 'MATLAB:print:ContentTypeImageSuggested');
addpath(fullfile(pwd, 'common'));   % skripte se pokrecu iz mape src
colors = config_plot();

L    = 10;
hfun = @(x) 0.0053*x.^4 - 0.095*x.^3 + 0.48*x.^2 - 0.3*x + 1;
cases = struct('name', {'A','A','B','B'}, 'b1', {0.5,0.5,0.5,0.5}, ...
               'b2', {0.5,0.5,0.2,0.2}, 'N', {20,100,20,100});

opts = optimoptions('linprog', 'Algorithm', 'dual-simplex', 'Display', 'none');
res  = struct([]);

fprintf('=== ZADATAK 3 ===\n');
fprintf('h(0) = %.4f,  h(L) = %.4f\n', hfun(0), hfun(L));
fprintf('\n Slucaj |   N |   dx  |   J* [m^2] | max|Dy| [-] | max|D2y| [m^-1] | var | nejed. | exitflag\n');

for k = 1:numel(cases)
    N  = cases(k).N;  b1 = cases(k).b1;  b2 = cases(k).b2;
    dx = L/N;  x = linspace(0, L, N+1)';  hv = hfun(x);  n = N+1;

    % Varijable: v = [y; z],  dim = 2*(N+1)
    f = [zeros(n,1); dx*ones(n,1)];

    I  = eye(n);
    D1 = (diag(-ones(n,1)) + diag(ones(n-1,1), 1));  D1 = D1(1:N, :)/dx;
    D2 = zeros(N-1, n);
    for i = 1:N-1
        D2(i, i) = 1;  D2(i, i+1) = -2;  D2(i, i+2) = 1;
    end
    D2 = D2/dx^2;
    Zn = zeros(size(D1,1), n);  Zc = zeros(size(D2,1), n);

    A = [ I, -I;  -I, -I;  D1, Zn;  -D1, Zn;  D2, Zc;  -D2, Zc];
    b = [hv;      -hv;     b1*ones(N,1); b1*ones(N,1); b2*ones(N-1,1); b2*ones(N-1,1)];

    Aeq = zeros(2, 2*n);  Aeq(1,1) = 1;  Aeq(2,N+1) = 1;
    beq = [hv(1); hv(end)];
    lb  = [-inf(n,1); zeros(n,1)];

    [v, J, ef] = linprog(f, A, b, Aeq, beq, lb, [], opts);
    assert(ef == 1, 'linprog nije konvergirao (slucaj %d, exitflag = %d).', k, ef);

    y = v(1:n);
    res(k).name = cases(k).name;  res(k).N = N;  res(k).dx = dx;
    res(k).x = x;  res(k).h = hv;  res(k).y = y;  res(k).J = J;
    res(k).b1 = b1; res(k).b2 = b2;
    res(k).mD1 = max(abs(D1*y));  res(k).mD2 = max(abs(D2*y));
    res(k).nvar = 2*n;  res(k).nineq = size(A,1);  res(k).ef = ef;

    fprintf('   %s    | %3d | %5.2f | %10.6f | %7.4f | %8.4f | %3d | %6d | %d\n', ...
        cases(k).name, N, dx, J, res(k).mD1, res(k).mD2, 2*n, size(A,1), ef);
end

fprintf('\nUtjecaj mreze  (A): %.6f -> %.6f  (%+.2f %%)\n', res(1).J, res(2).J, 100*(res(2).J/res(1).J - 1));
fprintf('Utjecaj mreze  (B): %.6f -> %.6f  (%+.2f %%)\n', res(3).J, res(4).J, 100*(res(4).J/res(3).J - 1));
fprintf('Utjecaj b2 (N=100): %.6f -> %.6f  (%+.2f %%)\n', res(2).J, res(4).J, 100*(res(4).J/res(2).J - 1));

%% Slike 4.1 i 4.2 - profil ceste za slucaj A i B
for pair = {[1 2 'A'], [3 4 'B']}
    ii = pair{1};  k20 = ii(1);  k100 = ii(2);  nm = char(ii(3));
    fg = figure('Position', [100 100 780 420], 'Visible', 'off', 'Color', 'w');
    hold on;
    xf = [res(k100).x; flipud(res(k100).x)];
    yf = [res(k100).y; flipud(res(k100).h)];
    fill(xf, yf, colors.lightGray, 'EdgeColor', 'none', 'FaceAlpha', 0.82);
    % A subtle color band emphasizes the local difference between the grids.
    y20i = interp1(res(k20).x, res(k20).y, res(k100).x, 'linear');
    for jj = 1:numel(res(k100).x)-1
        xb = res(k100).x(jj:jj+1);
        yb20 = y20i(jj:jj+1); yb100 = res(k100).y(jj:jj+1);
        if mean(yb20 - yb100) >= 0, bandColor = colors.blue; else, bandColor = colors.red; end
        patch([xb; flipud(xb)], [yb20; flipud(yb100)], bandColor, ...
              'EdgeColor', 'none', 'FaceAlpha', 0.18, 'HandleVisibility', 'off');
    end
    plot(res(k100).x, res(k100).h, '-', 'Color', colors.dark, 'LineWidth', 1.7);
    plot(res(k20).x,  res(k20).y,  '-', 'Color', colors.blue, 'LineWidth', 1.15);
    plot(res(k100).x, res(k100).y, '-', 'Color', colors.red,  'LineWidth', 1.15);
    xlabel('x [m]'); ylabel('visina [m]');
    legend({'iskop / nasip', 'teren h(x)', ...
            sprintf('niveleta y(x), N = 20  (J^* = %.4f m^2)',  res(k20).J), ...
            sprintf('niveleta y(x), N = 100 (J^* = %.4f m^2)', res(k100).J)}, ...
           'Location', 'northwest', 'FontSize', 9);
    xlim([0 L]);
    fn = sprintf('fig3_%d_road_case_%s.pdf', 1 + (nm == 'B'), nm);
    exportgraphics(fg, fullfile(fig_dir(), fn), 'ContentType', 'vector');
    exportgraphics(fg, fullfile(fig_dir(), strrep(fn, '.pdf', '.png')), 'Resolution', 220);
    close(fg);
end

%% Slika 4.3 - provjera ogranicenja prve i druge podijeljene razlike (N = 100)
fg = figure('Position', [100 100 780 620], 'Visible', 'off', 'Color', 'w');
for sp = 1:2
    subplot(2,1,sp); hold on;
    for k = [2 4]
        N = res(k).N;  dx = res(k).dx;  y = res(k).y;
        D1 = (diag(-ones(N+1,1)) + diag(ones(N,1),1));  D1 = D1(1:N,:)/dx;
        if sp == 1
            d = D1*y;  xs = res(k).x(2:end);
        else
            D2 = zeros(N-1, N+1);
            for i = 1:N-1, D2(i,i) = 1; D2(i,i+1) = -2; D2(i,i+2) = 1; end
            D2 = D2/dx^2;  d = D2*y;  xs = res(k).x(3:end);
        end
        st = {'k-', 'k--'};  ii = 1 + (k == 4);
        plot(xs, d, st{ii}, 'LineWidth', 1.8);
    end
    if sp == 1
        yline( 0.5, 'k:', 'LineWidth', 1.4);  yline(-0.5, 'k:', 'LineWidth', 1.4);
        ylabel('\nabla y_i  [m/m]');  ylim([-0.65 0.65]);
        legend({'slucaj A', 'slucaj B', '\pm b_1 = \pm 0.5'}, 'Location', 'southeast', 'FontSize', 9);
    else
        yline( 0.5, 'k:', 'LineWidth', 1.4);  yline(-0.5, 'k:', 'LineWidth', 1.4);
        yline( 0.2, 'k-.', 'LineWidth', 1.2); yline(-0.2, 'k-.', 'LineWidth', 1.2);
        ylabel('\nabla^2 y_i  [m^{-1}]');  ylim([-0.65 0.65]);
        legend({'slucaj A', 'slucaj B', '\pm b_2 = \pm 0.5 (A)', '', '\pm b_2 = \pm 0.2 (B)'}, ...
               'Location', 'southeast', 'FontSize', 9);
    end
    xlabel('x [m]');  xlim([0 L]);
end
exportgraphics(fg, fullfile(fig_dir(), 'fig3_3_road_constraint_check.pdf'), 'ContentType', 'vector');
close(fg);
fprintf('\nSlike 4.1-4.3 izvezene.\n');
