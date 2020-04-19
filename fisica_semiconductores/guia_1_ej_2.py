#!/usr/local/bin/python3

import funciones_calculos_guia_1 as fun


# a) Determinar la concentración intrínseca de portadores (ni) del silicio a temperatura ambiente (T =27◦C)
# b) Repetir para T = 0◦C y T = 100◦C

def main():

    mef_p = 0.56 * m_0
    mef_n = 1.1 * m_0
    T = 273 + 27
    Eg = 1.12
    fun.concentration_int(mef_n, mef_p, T, Eg)
    T = 0
    fun.concentration_int(mef_n, mef_p, T, Eg)
    T = 273
    fun.concentration_int(mef_n, mef_p, T, Eg)


if __name__ == '__main__':
    main()
