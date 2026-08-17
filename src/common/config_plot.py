"""
Common Plot Configuration for OMRiUS Seminar Figures
Ensures consistent publication styling, high DPI (>=300), LaTeX font styling,
and standardized color palettes across all generated figures.
"""

import os
import matplotlib.pyplot as plt

def setup_plot_style():
    """Configure matplotlib global parameters for publication quality."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 13,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.titlesize': 14,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'lines.linewidth': 1.8,
        'lines.markersize': 6,
        'grid.alpha': 0.35,
        'grid.linestyle': '--',
        'axes.grid': True,
        'mathtext.fontset': 'cm',
        'figure.autolayout': True
    })

# Standardized Color Palette
COLORS = {
    'primary_blue': '#1f77b4',
    'dark_blue': '#003366',
    'accent_red': '#d62728',
    'dark_red': '#8b0000',
    'forest_green': '#2ca02c',
    'emerald': '#008040',
    'amber_orange': '#ff7f0e',
    'purple': '#9467bd',
    'cyan_teal': '#17becf',
    'slate_gray': '#7f7f7f',
    'light_gray': '#e0e0e0',
    'feasible_fill': '#d0e1fd',
    'robust_fill': '#fed7d7'
}

def save_figure(fig, filename, fig_dir='docs/figures'):
    """Save figure in both PDF (vector) and PNG (high-DPI raster) formats."""
    os.makedirs(fig_dir, exist_ok=True)
    base_path = os.path.join(fig_dir, filename)
    fig.savefig(f"{base_path}.pdf", bbox_inches='tight', dpi=300)
    fig.savefig(f"{base_path}.png", bbox_inches='tight', dpi=300)
    print(f"Saved figure: {base_path}.pdf and {base_path}.png")
