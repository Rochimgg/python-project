#!/usr/local/bin/python3
import scipy as sc
from scipy.constants import electron_mass
from scipy.constants import Boltzmann
from scipy.constants import Planck

RESULT_FORMAT = "{:.4e}"
k = sc.constants.value('Boltzmann constant in eV/K')
h = sc.constants.value('Planck constant in eV/Hz')
m_0 = sc.constants.value('electron mass')
