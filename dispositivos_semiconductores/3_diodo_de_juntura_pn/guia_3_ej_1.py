#!/usr/local/bin/python3
import dispositivos_semiconductores.diccionario_constantes as cte
from dispositivos_semiconductores.funciones_calculos import *


def main():
    phi_b = 0.9 * unit.volt  # V
    print(phi_b)
    R = 3 * unit["ohm"]
    Na = 1e16 * unit['1/centimeter**3']
    Nd = 1e15 * unit['1/centimeter**3']
    current = phi_b/R
    print(current)


if __name__ == '__main__':
    main()
