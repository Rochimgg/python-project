#!/usr/local/bin/python3

from dispositivos_semiconductores.diccionario_constantes import *
from dispositivos_semiconductores.funciones_calculos import ni


# Determinar la concentración intrínseca de portadores (ni) de los siguientes semiconductores
# a temperatura ambiente (T = 27◦C)

def main():
    # Germanio a temperatura ambiente
    mef_n = Ge["mef_n"]
    mef_p = Ge["mef_p"]
    T = T_amb
    Eg = Ge["Eg"]
    print(RESULT_FORMAT.format(ni(mef_n, mef_p, T, Eg)))

    # Arseniuro de Galio a temperatura ambiente
    mef_n = GaAs["mef_n"]
    mef_p = GaAs["mef_p"]
    T = T_amb
    Eg = GaAs["Eg"]
    print(RESULT_FORMAT.format(ni(mef_n, mef_p, T, Eg)))


if __name__ == '__main__':
    main()
