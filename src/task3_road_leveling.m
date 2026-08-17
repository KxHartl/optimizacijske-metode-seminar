%% Task 3: Optimization Formulation - Road Profile Leveling (LP) in MATLAB
% Formulates and solves the terrain leveling problem using sparse linprog for Cases A & B

clear; close all; clc;
config_plot();

L = 10;
hfun = @(x) 0.0053*x.^4 - 0.095*x.^3 + 0.48*x.^2 - 0.3*x + 1;

cases = { ...
    struct('name',"A",'b1',0.5,'b2',0.5,'N',20); ...
    struct('name',"A",'b1',0.5,'b2',0.5,'N',100); ...
    struct('name',"B",'b1',0.5,'b2',0.2,'N',20); ...
    struct('name',"B",'b1',0.5,'b2',0.2,'N',100) ...
};

opts = optimoptions('linprog','Algorithm','dual-simplex','Display','none');

fprintf('=== Task 3: MATLAB linprog Benchmark ===\n');

for k = 1:numel(cases)
    name = cases{k}.name;
    b1 = cases{k}.b1;
    b2 = cases{k}.b2;
    N  = cases{k}.N;
    dx = L/N;
    x  = linspace(0,L,N+1).';
    h  = hfun(x);
    a  = h(1);
    b  = h(end);

    % Variables: theta = [y_0...y_N, z_0...z_N]^T (dim: 2*(N+1))
    ny = N+1; nz = N+1; n = ny + nz;
    
    % Cost: min sum(z_i * dx)
    f = zeros(n,1);
    f(ny+1:end) = dx;

    % Inequalities A * theta <= bineq
    % 1. Epigraph absolute value bounds: (y_i - h_i <= z_i) and (-y_i + h_i <= z_i)
    % 2. Slope bounds: -b1 <= (y_i - y_{i-1})/dx <= b1
    % 3. Curvature bounds: -b2 <= (y_i - 2*y_{i-1} + y_{i-2})/dx^2 <= b2
    A_ineq = [];
    bineq = [];

    % 1. Epigraph bounds
    I_y = eye(ny);
    I_z = eye(nz);
    A_ineq = [A_ineq; [I_y, -I_z]; [-I_y, -I_z]];
    bineq  = [bineq; h; -h];

    % 2. Slope bounds
    D1 = zeros(N, ny);
    for i = 1:N
        D1(i, i+1) = 1/dx;
        D1(i, i)   = -1/dx;
    end
    A_ineq = [A_ineq; [D1, zeros(N, nz)]; [-D1, zeros(N, nz)]];
    bineq  = [bineq; b1*ones(N,1); b1*ones(N,1)];

    % 3. Curvature bounds
    D2 = zeros(N-1, ny);
    for i = 1:N-1
        D2(i, i+2) = 1/(dx^2);
        D2(i, i+1) = -2/(dx^2);
        D2(i, i)   = 1/(dx^2);
    end
    A_ineq = [A_ineq; [D2, zeros(N-1, nz)]; [-D2, zeros(N-1, nz)]];
    bineq  = [bineq; b2*ones(N-1,1); b2*ones(N-1,1)];

    % Boundary equality constraints: y(0)=1, y(L)=4
    Aeq = zeros(2, n);
    beq = [a; b];
    Aeq(1, 1)  = 1;
    Aeq(2, ny) = 1;

    % Lower bounds for z >= 0, y free
    lb = [-Inf*ones(ny,1); zeros(nz,1)];
    ub = Inf*ones(n,1);

    % Solve LP
    [sol, cost_integral, exitflag] = linprog(f, A_ineq, bineq, Aeq, beq, lb, ub, opts);
    
    y_opt = sol(1:ny);
    z_opt = sol(ny+1:end);
    raw_sum = sum(z_opt);

    fprintf('Slučaj %s (b1=%.1f, b2=%.1f, N=%d):\n', name, b1, b2, N);
    fprintf('  Total Cost J* = %.6f m^2 (Raw discrete sum = %.4f)\n', cost_integral, raw_sum);
end
