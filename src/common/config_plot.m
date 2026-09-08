function colors = config_plot()
% CONFIG_PLOT  Global MATLAB figure defaults used by all task scripts.
%
%   Napomena: MATLAB R2025b u sesiji bez radne povrsine (-batch) crta osi,
%   legende i tekst prema tamnoj temi bez obzira na Figure.Color, pa se sve
%   boje ovdje postavljaju eksplicitno kako bi izvezeni PDF bio dosljedan.
%   TeX (a ne LaTeX) interpreter koristi se zbog hrvatskih znakova u oznakama.

    % Standard professional seminar palette, chosen to remain distinguishable
    % for readers with color-vision deficiencies. Scripts obtain it as the
    % return value, while ColorOrder keeps future plots consistent.
    colors.blue       = [0.000 0.447 0.698];
    colors.red        = [0.835 0.369 0.000];
    colors.green      = [0.000 0.620 0.451];
    colors.amber      = [0.902 0.624 0.000];
    colors.sky        = [0.337 0.706 0.914];
    colors.purple     = [0.800 0.475 0.655];
    colors.dark       = [0.180 0.200 0.220];
    colors.gray       = [0.500 0.520 0.540];
    colors.lightGray  = [0.900 0.910 0.920];
    colors.lightBlue  = [0.855 0.925 0.965];

    set(groot, 'defaultTextInterpreter',          'tex');
    set(groot, 'defaultAxesTickLabelInterpreter', 'tex');
    set(groot, 'defaultLegendInterpreter',        'tex');

    set(groot, 'defaultAxesFontName',  'Times New Roman');
    set(groot, 'defaultTextFontName',  'Times New Roman');
    set(groot, 'defaultAxesFontSize',  11);
    set(groot, 'defaultLineLineWidth', 1.6);

    % --- boje: svijetla podloga i standardni redoslijed serija ---
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
    set(groot, 'defaultAxesColorOrder', [colors.blue; colors.red; colors.green; ...
                                         colors.amber; colors.sky; colors.purple]);

    % --- mreza ---
    set(groot, 'defaultAxesXGrid',         'on');
    set(groot, 'defaultAxesYGrid',         'on');
    set(groot, 'defaultAxesGridLineStyle', '--');
    set(groot, 'defaultAxesGridAlpha',     0.30);
    set(groot, 'defaultAxesBox',           'on');
end
