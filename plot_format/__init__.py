"""
===========
plot_format
===========

Global plot formatting options.
Goal is to produce IEEE journal compatible figures easily.
Each plot format setting set in this file can be
overriden in individual plots, or by setting the respective
rcParams again.

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
plt.rcParams['text.usetex'] = False
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'normal'
plt.rcParams['axes.titleweight'] = 'normal'
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.grid.axis'] = 'both'
plt.rcParams['axes.prop_cycle'] = monochrome
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['lines.markersize'] = 6
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['figure.titlesize'] = 10
plt.rcParams['figure.figsize'] = (4.774,2.95)
plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['image.cmap'] = 'gray'
