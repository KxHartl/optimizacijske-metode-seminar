%% Pokrece sve cetiri skripte i sprema konzolni ispis u docs/code/.
%  Pokrenuti iz mape src:   >> cd src;  run_all
%  Svaka brojka koja se pojavljuje u seminaru mora postojati u tim datotekama.

clear; close all; clc;
scriptDir = fileparts(mfilename('fullpath'));
addpath(fullfile(scriptDir, 'common'));

packageOutDir = fullfile(scriptDir, '..', '..', ...
    '05_VERIFICATION_AND_BENCHMARKS', 'matlab_output');
if exist(fileparts(packageOutDir), 'dir')
    outDir = packageOutDir;
else
    outDir = fullfile(scriptDir, '..', 'docs', 'code');
end
if ~exist(outDir, 'dir'), mkdir(outDir); end

tasks = {'task1_qp_analysis', 'task2_robust_qp', ...
         'task3_road_leveling', 'task4_lmi_switched_stabilization'};

for k = 1:numel(tasks)
    logFile = fullfile(outDir, sprintf('task%d_output.txt', k));
    if exist(logFile, 'file'), delete(logFile); end
    diary(logFile); diary on;
    runOne(tasks{k});
    diary off;
    fprintf('[run_all] %s -> %s\n', tasks{k}, logFile);
end
fprintf('\n[run_all] Sve skripte izvrsene bez greske.\n');

function runOne(scriptName)
    % Vlastiti radni prostor da 'clear' u skripti ne obrise varijable pozivatelja.
    scriptDir = fileparts(mfilename('fullpath'));
    run(fullfile(scriptDir, scriptName));
end
