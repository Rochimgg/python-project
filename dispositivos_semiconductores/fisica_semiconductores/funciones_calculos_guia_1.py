#!/usr/local/bin/python3

import math
import numpy as np
from pytexit import py2tex
import diccionario_constantes as cte


def concentration_int(mef_n, mef_p, T, Eg):
    if T == 0 and Eg > 0:
        return - math.inf

    # py2tex(f'2 * ({np.pi} * sqrt({mef_n} * {mef_p}) * {dic.k} / {dic.h}) * exp({Eg} / (2 * {dic.k} * {T}))')
    EgJ = Eg * cte.q
    masa = math.sqrt(mef_n * mef_p)
    dospi = 2 * math.pi
    kT = cte.k * T
    planck_cuadrado = cte.h ** 2
    ni = 2 * math.pow(dospi * masa * kT / planck_cuadrado, 1.5) * math.exp(-EgJ/(2*kT))/1e6
    return ni
