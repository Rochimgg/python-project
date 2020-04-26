#!/usr/local/bin/python3

from funciones_calculos_guia_1 import concentration_int
import diccionario_constantes as cte


# Determinar la concentración intrínseca de portadores (ni) de los siguientes semiconductores
# a temperatura ambiente (T = 27◦C)

def main():
    # Germanio a temperatura ambiente
    mef_n = 0.56 * cte.m0
    mef_p = 0.29 * cte.m0
    T = 273 + 27
    Eg = 1.12
    print(cte.RESULT_FORMAT.format(concentration_int(mef_n, mef_p, T, Eg)))
    # Arseniuro de Galio a temperatura ambiente
    mef_n = 0.068 * cte.m0
    mef_p = 0.47 * cte.m0
    T = 273 + 27
    Eg = 1.12
    print(cte.RESULT_FORMAT.format(concentration_int(mef_n, mef_p, T, Eg)))


if __name__ == '__main__':
    main()
