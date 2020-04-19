#!/usr/local/bin/python3

import funciones_calculos_guia_1 as fun
import diccionario_constantes as dic


# a) Determinar la concentración intrínseca de portadores (ni) del silicio a temperatura ambiente (T =27◦C)
# b) Repetir para T = 0◦C y T = 100◦C

def main():
    # Germanio a temperatura ambiente
    mef_n = 0.56 * dic.m_0
    mef_p = 0.29 * dic.m_0
    T = 273 + 27
    Eg = 1.12
    fun.concentration_int(mef_n, mef_p, T, Eg)
    # Arseniuro de Galio a temperatura ambiente
    mef_n = 0.068 * dic.m_0
    mef_p = 0.47 * dic.m_0
    T = 273 + 27
    Eg = 1.12
    fun.concentration_int(mef_n, mef_p, T, Eg)


if __name__ == '__main__':
    main()