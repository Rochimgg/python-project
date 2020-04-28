#!/usr/local/bin/python3

import dispositivos_semiconductores.fisica_semiconductores.diccionario_constantes as cte
from dispositivos_semiconductores.fisica_semiconductores.funciones_calculos_guia_1 import concentration_int


# a) Determinar la concentración intrínseca de portadores (ni) del silicio a temperatura ambiente (T = 27◦C)
# b) Repetir para T = 0◦C y T = 100◦C

def main():
    mef_p = 0.56 * cte.m0
    mef_n = 1.1 * cte.m0
    T = 273 + 27
    Eg = 1.12
    print(cte.RESULT_FORMAT.format((concentration_int(mef_n, mef_p, T, Eg))))
    T = 0
    print(cte.RESULT_FORMAT.format(concentration_int(mef_n, mef_p, T, Eg)))
    T = 273
    print(cte.RESULT_FORMAT.format(concentration_int(mef_n, mef_p, T, Eg)))


if __name__ == '__main__':
    main()
