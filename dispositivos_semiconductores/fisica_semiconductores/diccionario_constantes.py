#!/usr/local/bin/python3
import scipy as sc
from scipy.constants import electron_mass
from scipy.constants import Boltzmann
from scipy.constants import Planck

RESULT_FORMAT = "{:.4e}"
k = sc.constants.value('Boltzmann constant')
h = sc.constants.value('Planck constant')
m0 = sc.constants.value('electron mass')
q = sc.constants.value('elementary charge')
