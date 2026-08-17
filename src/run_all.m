%% Master Runner Script for OMRiUS Seminar MATLAB Simulations
clear; close all; clc;

fprintf('==========================================\n');
fprintf('Executing Task 1: QP Analysis\n');
fprintf('==========================================\n');
task1_qp_analysis;

fprintf('\n==========================================\n');
fprintf('Executing Task 2: Robust QP\n');
fprintf('==========================================\n');
task2_robust_qp;

fprintf('\n==========================================\n');
fprintf('Executing Task 3: Road Leveling LP\n');
fprintf('==========================================\n');
task3_road_leveling;

fprintf('\n==========================================\n');
fprintf('Executing Task 4: Switched LMI Stabilization\n');
fprintf('==========================================\n');
task4_lmi_switched_stabilization;

fprintf('\nAll MATLAB simulations executed successfully.\n');
