#!/usr/local/bin/python3
from dispositivos_semiconductores.diccionario_constantes import *
from dispositivos_semiconductores.funciones_calculos import xd0, E_max, phi_b, xn0, xp0


# TODO: corregir este ejercicio
def main():
    Na = 1e16
    Nd = 1e15
    ni = Si["ni"]
    e = Si["e"]
    V = -5

    _phi_b = phi_b(Na, Nd, ni)
    print(_phi_b)
    print(xd0(Na=Na, Nd=Nd, e=e, phi_b=_phi_b, ni=ni, V=V))
    _xn0 = xn0(Na=Na, Nd=Nd, e=e, phi_b=_phi_b, V=V)
    print(E_max(Nd, _xn0, e))

    V = 5
    print(xd0(Na=Na, Nd=Nd, e=e, phi_b=_phi_b, ni=ni, V=V))
    _xp0 = xp0(Na=Na, Nd=Nd, e=e, phi_b=_phi_b, V=V)
   # print(E_max(Na, _xp0, e))


if __name__ == '__main__':
    main()