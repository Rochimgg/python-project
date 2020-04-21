#!/usr/local/bin/python3
import scipy as sc
from scipy.constants import electron_mass
from scipy.constants import Boltzmann
from scipy.constants import Planck

RESULT_FORMAT = "{:.4e}"
#k = sc.constants.value('Boltzmann constant in eV/K')
k = Boltzmann
k = sc.constants.value('Boltzmann constant in eV/K')
h = Planck
h = sc.constants.value('reduced Planck constant in eV s')
m_0 = electron_mass
#m_0m = sc.constants.value('electron mass energy equivalent in MeV')/1e6
'''h = sc.constants.value('Planck constant in eV/Hz')
h = sc.constants.value('reduced Planck constant in eV s')
m_0 = sc.constants.value('electron mass')
m_0u = sc.constants.value('electron mass in u')
m_0m = sc.constants.value('electron molar mass')'''