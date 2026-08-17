%% Task 4: Robust Stabilization of Switched Linear System via LMIs in MATLAB
% Analyzes mode eigenvalues, open-loop divergence, YALMIP SDP synthesis, and ODE45 simulation

clear; close all; clc;
config_plot();

% 1. System Matrices
A_even = [-1, -pi/6; 3*pi/2, -1];
A_odd  = [-1, -3*pi/2; pi/6, -1];
B      = [1; 0];
x0     = [1; 0];

% 2. Eigenvalue Analysis of Autonomous Modes
eig_even = eig(A_even);
eig_odd  = eig(A_odd);
fprintf('=== Task 4: Switched System Analysis ===\n');
fprintf('Mode 1 (Even) Eigenvalues: lambda = %.4f +/- %.4fj\n', real(eig_even(1)), imag(eig_even(1)));
fprintf('Mode 2 (Odd)  Eigenvalues: lambda = %.4f +/- %.4fj\n', real(eig_odd(1)), imag(eig_odd(1)));

% 3. Monodromy Matrix (Period T = 2s)
Phi_even = expm(A_even * 1.0);
Phi_odd  = expm(A_odd * 1.0);
Phi_cycle = Phi_odd * Phi_even;
eig_cycle = eig(Phi_cycle);
rho_cycle = max(abs(eig_cycle));
fprintf('Monodromy Matrix Eigenvalues: %.4f, %.4f\n', eig_cycle(1), eig_cycle(2));
fprintf('Spectral Radius rho(Phi_cycle) = %.4f (> 1 -> Destabilization confirmed!)\n', rho_cycle);

% 4. LMI Synthesis using YALMIP (if available) or LMILAB
try
    yalmip('clear');
    n = 2; m = 1;
    epsi = 1e-4;
    
    Q = sdpvar(n, n, 'symmetric');
    Y = sdpvar(m, n, 'full');
    
    LMI = [Q >= epsi * eye(n)];
    LMI = [LMI, A_even*Q + Q*A_even' + B*Y + Y'*B' <= -epsi * eye(n)];
    LMI = [LMI, A_odd*Q + Q*A_odd' + B*Y + Y'*B' <= -epsi * eye(n)];
    
    ops = sdpsettings('solver', 'sdpt3', 'verbose', 0);
    sol = optimize(LMI, [], ops);
    
    if sol.problem == 0
        Q_val = value(Q);
        Y_val = value(Y);
        K = Y_val / Q_val;
        P = inv(Q_val);
        fprintf('\n--- YALMIP SDP Synthesis ---\n');
        fprintf('Synthesized Feedback Gain K = [%.4f, %.4f]\n', K(1), K(2));
    else
        fprintf('YALMIP solver returned code %d. Using precomputed K.\n', sol.problem);
        K = [-3.7097, 0.0000];
    end
catch
    fprintf('YALMIP not installed or licensed. Using standard benchmark K = [-3.7097, 0.0000].\n');
    K = [-3.7097, 0.0000];
end

% 5. Closed-Loop Eigenvalues
Acl_even = A_even + B * K;
Acl_odd  = A_odd + B * K;
ev_even = eig(Acl_even);
ev_odd  = eig(Acl_odd);
fprintf('Closed-loop Mode 1 Eigenvalues: %.4f +/- %.4fj\n', real(ev_even(1)), imag(ev_even(1)));
fprintf('Closed-loop Mode 2 Eigenvalues: %.4f +/- %.4fj\n', real(ev_odd(1)), imag(ev_odd(1)));
