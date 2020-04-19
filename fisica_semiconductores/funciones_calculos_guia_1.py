#!/usr/local/bin/python3

import numpy as np
import math as mt
import diccionario_constantes as dic


def concentration_int(mef_n, mef_p, T, Eg):
    if T == 0 and Eg > 0:
        if Eg > 0:
            ni = mt.inf
        else:
            ni = - mt.inf
    else:
        ni = dic.RESULT_FORMAT.format(2 * (np.pi * np.sqrt(mef_n * mef_p) * dic.k / dic.h) * mt.exp(Eg / (2 * dic.k * T)))
    print(ni)