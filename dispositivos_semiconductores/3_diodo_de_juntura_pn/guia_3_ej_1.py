#!/usr/local/bin/python3
import dispositivos_semiconductores.diccionario_constantes as cte
from dispositivos_semiconductores.funciones_calculos import *


def main():
    phi_b = 0.9 * unit.volt  # V
    print(phi_b)
    Na = 1e16 * unit['1/centimeter**3']
    Nd = 1e15 * unit['1/centimeter**3']
    Cj0_a = 0 * unit['farad']


if __name__ == '__main__':
    main()
