function d = fig_dir()
% FIG_DIR  Absolute path of the directory all figures are exported to.
    here = fileparts(mfilename('fullpath'));         % <repo>/src/common
    packageFigures = fullfile(here, '..', '..', '..', ...
        '03_LATEX_SOURCE', 'figures');
    if exist(fileparts(packageFigures), 'dir')
        d = packageFigures;
    else
        d = fullfile(here, '..', '..', 'docs', 'figures');
    end
    if ~exist(d, 'dir'), mkdir(d); end
end
