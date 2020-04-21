#!/usr/local/bin/python3

import math
from pytexit import py2tex
import diccionario_constantes as cte


def concentration_int(mef_n, mef_p, T, Eg):
    if T == 0 and Eg > 0:
        ni = - math.inf
    else:
        # py2tex(f'2 * ({np.pi} * sqrt({mef_n} * {mef_p}) * {dic.k} / {dic.h}) * exp({Eg} / (2 * {dic.k} * {T}))')
        ni = cte.RESULT_FORMAT.format((2 * ((2 * math.pi * math.sqrt(mef_n * mef_p) * cte.k * T) / cte.h ** 2) ** (3 / 2) * math.exp(Eg / (2 * cte.k * T))))
    print(ni)
