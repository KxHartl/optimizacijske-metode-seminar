function d = fig_dir()
% FIG_DIR  Absolute path of the directory all figures are exported to.
    here = fileparts(mfilename('fullpath'));         % <repo>/src/common
    d    = fullfile(here, '..', '..', 'docs', 'figures');
    if ~exist(d, 'dir'), mkdir(d); end
end
