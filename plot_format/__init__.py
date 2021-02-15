"""
===========
Plot Format
===========

Global plot formatting options.  Goal is to produce IEEE journal compatible
figures easily.  Each plot format setting set in this file can be overriden in
individual plots, or by setting the respective rcParams again.

Reference:
https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html

Initially written by Okko Järvinen, okko.jarvinen@aalto.fi, 2020.

How to use
----------

Import the file in the beginning of the main module as::

    import plot_format
    plot_format.set_style()

The style can be further specified or changed by passing style identifier as
parameter::

    import plot_format
    plot_format.set_style('ieeetran')

Default style is 'ieeetran'. Feel free to add your own styles. The purpose is
to make common styles that can be used in many contexts -- very specific
styling should be done in the plot itself.

"""

import os
import sys
import pdb
if not (os.path.abspath('../../thesdk') in sys.path):
    sys.path.append(os.path.abspath('../../thesdk'))

from thesdk import *
import numpy as np

import matplotlib.pyplot as plt
from cycler import cycler

def set_style(style='ieeetran'):
    # Common settings
    plt.rcParams['savefig.bbox'] = 'tight'
    plt.rcParams['savefig.pad_inches'] = 0
    plt.rcParams['savefig.format'] = 'pdf'
    plt.rcParams['figure.dpi'] = 150
    plt.rcParams['figure.constrained_layout.use'] = True
    if style == 'ieeetran':
        # This cycles first through linestyles with black ('0') color, then 40% gray, etc. 
        monochrome = (cycler('color', ['0.0','0.5','0.7'])*cycler('linestyle', ['-', '--', ':', '-.']))
        plt.rcParams['font.weight'] = 'normal'
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
        plt.rcParams['mathtext.fontset'] = 'dejavuserif'
        # This should give fitting font style, might not work if ghostscript is not in path
        plt.rcParams['text.usetex'] = True
        plt.rcParams['text.latex.preamble'] = r'\usepackage{mathptmx} \usepackage{amsmath}'
        # 10 or 8?
        plt.rcParams['axes.labelsize'] = 10
        plt.rcParams['axes.labelweight'] = 'normal'
        plt.rcParams['axes.titleweight'] = 'normal'
        plt.rcParams['axes.axisbelow'] = True
        plt.rcParams['axes.grid'] = True
        plt.rcParams['axes.grid.axis'] = 'both'
        plt.rcParams['axes.prop_cycle'] = monochrome
        plt.rcParams['axes.xmargin'] = 0
        plt.rcParams['grid.color'] = '0.8'
        plt.rcParams['lines.linewidth'] = 1
        plt.rcParams['lines.markersize'] = 4
        plt.rcParams['legend.fontsize'] = 8
        plt.rcParams['legend.fancybox'] = False
        plt.rcParams['legend.frameon'] = True
        plt.rcParams['legend.framealpha'] = 1
        plt.rcParams['legend.edgecolor'] = '0'
        plt.rcParams['legend.borderpad'] = 0.3
        #plt.rcParams['legend.handlelength'] = 1.5
        plt.rcParams['legend.handletextpad'] = 0.5
        plt.rcParams['legend.labelspacing'] = 0.4
        plt.rcParams['patch.linewidth'] = '0.5'
        plt.rcParams['xtick.labelsize'] = 9
        plt.rcParams['ytick.labelsize'] = 9
        plt.rcParams['axes.titlesize'] = 10
        # This should be the width of one column
        plt.rcParams['figure.figsize'] = (3.5,2.0)
        plt.rcParams['image.cmap'] = 'gray'
    elif style == 'isscc':
        monochrome = (cycler('linestyle', ['-', '--', ':', '-.'])*cycler('color', ['b','r','g','m','k']))
        plt.rcParams['font.weight'] = 'normal'
        plt.rcParams['font.family'] = 'sans'
        plt.rcParams['text.usetex'] = False
        plt.rcParams['axes.labelsize'] = 10
        plt.rcParams['axes.labelweight'] = 'normal'
        plt.rcParams['axes.titleweight'] = 'normal'
        plt.rcParams['axes.axisbelow'] = True
        plt.rcParams['axes.grid'] = True
        plt.rcParams['axes.grid.axis'] = 'both'
        plt.rcParams['axes.prop_cycle'] = monochrome
        plt.rcParams['axes.xmargin'] = 0
        plt.rcParams['grid.color'] = '0.75'
        plt.rcParams['lines.linewidth'] = 1.2
        plt.rcParams['lines.markersize'] = 5
        plt.rcParams['legend.fontsize'] = 8
        plt.rcParams['legend.fancybox'] = False
        plt.rcParams['legend.frameon'] = True
        plt.rcParams['legend.framealpha'] = 1
        plt.rcParams['legend.edgecolor'] = '0.6'
        plt.rcParams['xtick.labelsize'] = 9
        plt.rcParams['ytick.labelsize'] = 9
        plt.rcParams['figure.titlesize'] = 10
        plt.rcParams['figure.figsize'] = (3.2,2.3)
        plt.rcParams['image.cmap'] = 'jet'
    elif style == 'isscc_bw':
        monochrome = (cycler('color', ['0.0','0.4','0.6'])*cycler('linestyle', ['-', '--', ':', '-.']))
        plt.rcParams['font.weight'] = 'normal'
        plt.rcParams['font.family'] = 'sans'
        plt.rcParams['text.usetex'] = False
        plt.rcParams['axes.labelsize'] = 10
        plt.rcParams['axes.labelweight'] = 'normal'
        plt.rcParams['axes.titleweight'] = 'normal'
        plt.rcParams['axes.axisbelow'] = True
        plt.rcParams['axes.grid'] = True
        plt.rcParams['axes.grid.axis'] = 'both'
        plt.rcParams['axes.prop_cycle'] = monochrome
        plt.rcParams['axes.xmargin'] = 0
        plt.rcParams['grid.color'] = '0.75'
        plt.rcParams['lines.linewidth'] = 1.2
        plt.rcParams['lines.markersize'] = 5
        plt.rcParams['legend.fontsize'] = 8
        plt.rcParams['legend.fancybox'] = False
        plt.rcParams['legend.frameon'] = True
        plt.rcParams['legend.framealpha'] = 1
        plt.rcParams['legend.edgecolor'] = '0.6'
        plt.rcParams['xtick.labelsize'] = 9
        plt.rcParams['ytick.labelsize'] = 9
        plt.rcParams['figure.titlesize'] = 10
        plt.rcParams['figure.figsize'] = (3.2,2.3)
        plt.rcParams['image.cmap'] = 'gray'
    else:
        pass
    return
