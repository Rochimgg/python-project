#!/usr/local/bin/python3

import math

from numpy import log as ln

from dispositivos_semiconductores.diccionario_constantes import *


def ni(mef_n, mef_p, T, Eg):
    if T == 0 and Eg > 0:
        ret = - math.inf
    else:
        # py2tex(f'2 * ({np.pi} * sqrt({mef_n} * {mef_p}) * {dic.k} / {dic.h}) * exp({Eg} / (2 * {dic.k} * {T}))')
        EgJ = Eg * q * unit['joule']  # J
        masa = math.sqrt(mef_n * mef_p) * unit['kilogram']  # Kg
        dospi = 2 * math.pi
        kT = k * T * unit['joule']  # J/K * T = J
        planck_cuadrado = h ** 2 * unit['joule**2 * second**2']  # (J s)^2
        ret = 2 * math.pow(dospi * masa * kT / planck_cuadrado, 1.5) * math.exp(-EgJ / (2 * kT)) / 1e6
    return ret


def phi_b(ni, Na, Nd, T=T_amb):
    return (k * T / q) * ln(Na * Nd / (ni ** 2))


def xn0(Na, Nd, e, ni=0, V=0, phi_b=None, T=T_amb):
    if phi_b is None:
        _phi_b = (k * T / q) * ln(Na * Nd / (ni ** 2)) * unit['volt']
        return math.sqrt(2 * e * (_phi_b - V) * Na / (q * (Na + Nd) * Nd))
    else:
        return math.sqrt(2 * e * (phi_b - V) * Na / (q * (Na + Nd) * Nd))


def xp0(Na, Nd, e, ni=0, V=0, phi_b=None, T=T_amb):
    if phi_b is None:
        _phi_b = (k * T / q) * ln(Na * Nd / (ni ** 2)) * unit['volt']
        return math.sqrt(2 * e * (_phi_b - V) * Nd / (q * (Na + Nd) * Na))
    else:
        return math.sqrt(2 * e * (phi_b - V) * Nd / (q * (Na + Nd) * Na))


def xd0(Na, Nd, e, ni=0, V=0, phi_b=None, T=T_amb):
    if phi_b is None:
        _phi_b = (k * T / q) * ln(Na * Nd / (ni ** 2)) * unit['volt']
        return math.sqrt(2 * e * (_phi_b-V) * (Na + Nd) / (q * Na * Nd))
    else:
        return math.sqrt(2 * e * (phi_b-V) * (Na + Nd) / (q * Na * Nd))


def E_max(Nd_Na, xn_xp, e):
    return q * Nd_Na * xn_xp / e
