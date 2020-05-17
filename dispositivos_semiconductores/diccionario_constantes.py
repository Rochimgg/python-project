#!/usr/local/bin/python3
import scipy as sc
from scipy.constants import electron_mass
from pint import UnitRegistry

unit = UnitRegistry()

RESULT_FORMAT = "{:.4e}"
k = sc.constants.value('Boltzmann constant') * unit['joule/kelvin']
h = sc.constants.value('Planck constant') * unit['joule*second']
m0 = sc.constants.value('electron mass') * unit['kilogram']
q = sc.constants.value('elementary charge') * unit['coulomb']
T_amb = 300 * unit['kelvin']
e0 = sc.constants.value('vacuum electric permittivity') * unit['farad/centimeter']

Si = {
    "mef_n":  1.1 * m0,  # Kg
    "mef_p": 0.56 * m0,  # Kg
    "mu_n": 1450 * unit['centimeter**2/(volt*second)'],  # cm^2/Vs
    "mu_p": 500,  # cm^2/Vs
    "Eg": 1.12,  # eV
    "er": 11.7,   # adim
    "e": 11.7 * e0,   # adim
    "ni": 1e10  # cm^-3
}

Ge = {
    "mef_n":  0.56 * m0,  # Kg
    "mef_p": 0.29 * m0,  # Kg
    "mu_n": 3900,  # cm^2/Vs
    "mu_p": 2300,  # cm^2/Vs
    "Eg": 0.66,  # eV
    "er": 0,   # adim
    "ni": 2.36e13  # cm^-3
}

GaAs = {
    "mef_n":  0.068 * m0,  # Kg
    "mef_p": 0.47 * m0,  # Kg
    "mu_n": 8500,  # cm^2/Vs
    "mu_p": 400,  # cm^2/Vs
    "Eg": 1.42,  # eV
    "er": 3.9,   # adim
    "e": 3.9 * e0,
    "ni": 1.8e6  # cm^-3
}



