function config_plot()
% CONFIG_PLOT  Global MATLAB figure defaults used by all task scripts.
%
%   Napomena: MATLAB R2025b u sesiji bez radne povrsine (-batch) crta osi,
%   legende i tekst prema tamnoj temi bez obzira na Figure.Color, pa se sve
%   boje ovdje postavljaju eksplicitno kako bi izvezeni PDF bio crno-bijel.
%   TeX (a ne LaTeX) interpreter koristi se zbog hrvatskih znakova u oznakama.

    set(groot, 'defaultTextInterpreter',          'tex');
    set(groot, 'defaultAxesTickLabelInterpreter', 'tex');
    set(groot, 'defaultLegendInterpreter',        'tex');

    set(groot, 'defaultAxesFontName',  'Times New Roman');
    set(groot, 'defaultTextFontName',  'Times New Roman');
    set(groot, 'defaultAxesFontSize',  11);
    set(groot, 'defaultLineLineWidth', 1.6);

    % --- boje: svijetla podloga, tamne linije ---
    set(groot, 'defaultFigureColor',    'w');
    set(groot, 'defaultAxesColor',      'none');   % bijela podloga figure prolazi kroz osi
    set(groot, 'defaultAxesXColor',     'k');
    set(groot, 'defaultAxesYColor',     'k');
    set(groot, 'defaultAxesZColor',     'k');
    set(groot, 'defaultAxesGridColor',  [0.15 0.15 0.15]);
    set(groot, 'defaultTextColor',      'k');
    set(groot, 'defaultLegendColor',     'w');
    set(groot, 'defaultLegendTextColor', 'k');
    set(groot, 'defaultLegendEdgeColor', 'k');
    set(groot, 'defaultColorbarColor',   'k');

    % --- mreza ---
    set(groot, 'defaultAxesXGrid',         'on');
    set(groot, 'defaultAxesYGrid',         'on');
    set(groot, 'defaultAxesGridLineStyle', '--');
    set(groot, 'defaultAxesGridAlpha',     0.30);
    set(groot, 'defaultAxesBox',           'on');
end
