#!/usr/local/bin/python3
from dispositivos_semiconductores.diccionario_constantes import *
from dispositivos_semiconductores.funciones_calculos import xd0, E_max, phi_b, xn0


def main():
    Na = 1e16
    Nd = 1e15
    ni = Si["ni"]
    e = Si["e"]

    _phi_b = phi_b(Na, Nd, ni)
    print(xd0(Na=Na, Nd=Nd, e=e, phi_b=_phi_b))
    _xn0 = xn0(Na=Na, Nd=Nd, e=e, phi_b=_phi_b)
    print(E_max(Nd_Na=Nd, xn_xp=_xn0, e=e))



if __name__ == '__main__':
    main()
