% Configures global MATLAB plotting defaults for publication-ready figures
function config_plot()
    set(groot, 'defaulttextinterpreter', 'latex');
    set(groot, 'defaultAxesTickLabelInterpreter', 'latex');
    set(groot, 'defaultLegendInterpreter', 'latex');
    set(groot, 'defaultAxesFontSize', 11);
    set(groot, 'defaultAxesFontName', 'Times');
    set(groot, 'defaultLineLineWidth', 1.8);
    set(groot, 'defaultAxesXGrid', 'on');
    set(groot, 'defaultAxesYGrid', 'on');
    set(groot, 'defaultAxesGridLineStyle', '--');
    set(groot, 'defaultAxesGridAlpha', 0.35);
end
