"""
===========
plot_format
===========

Global plot formatting options.
Goal is to produce IEEE journal compatible figures easily.
Each plot format setting set in this file can be
overriden in individual plots, or by setting the respective
rcParams again.

Reference:
https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html

Initially written by Okko Järvinen, okko.jarvinen@aalto.fi, 2020.

"""

import os
import sys
if not (os.path.abspath('../../thesdk') in sys.path):
    sys.path.append(os.path.abspath('../../thesdk'))

from thesdk import *
import numpy as np

import matplotlib.pyplot as plt
from cycler import cycler
# This cycles first through linestyles with black ('0') color, then 40% gray, etc. 
monochrome = (cycler('color', ['0.0','0.4','0.6'])*cycler('linestyle', ['-', '--', ':', '-.']))

plt.rcParams['font.weight'] = 'normal'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
# This should give fitting font style, might not work if ghostscript is not in path
plt.rcParams['text.usetex'] = True
# 10 or 8?
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'normal'
plt.rcParams['axes.titleweight'] = 'normal'
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.grid.axis'] = 'both'
plt.rcParams['axes.prop_cycle'] = monochrome
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['lines.markersize'] = 6
plt.rcParams['legend.fontsize'] = 8
plt.rcParams['legend.fancybox'] = False
plt.rcParams['legend.frameon'] = True
plt.rcParams['legend.framealpha'] = 1
plt.rcParams['legend.edgecolor'] = '0.6'
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['figure.titlesize'] = 10
# This was somewhere online
#plt.rcParams['figure.figsize'] = (4.774,2.95)
# This should be the width of one column
plt.rcParams['figure.figsize'] = (3.5,2.3)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['image.cmap'] = 'gray'
