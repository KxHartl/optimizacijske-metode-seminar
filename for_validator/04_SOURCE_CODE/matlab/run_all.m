%% Pokrece sve cetiri skripte i sprema konzolni ispis u docs/code/.
%  Pokrenuti iz mape src:   >> cd src;  run_all
%  Svaka brojka koja se pojavljuje u seminaru mora postojati u tim datotekama.

clear; close all; clc;
addpath(fullfile(pwd, 'common'));
outDir = fullfile(pwd, '..', 'docs', 'code');
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
    run(scriptName);
end
