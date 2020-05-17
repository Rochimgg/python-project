#!/usr/local/bin/python3
import dispositivos_semiconductores.diccionario_constantes as cte
from dispositivos_semiconductores.funciones_calculos import potencial_juntura


def main():
    Na = 1e18
    Nd = 1e15
    phi_b_1 = potencial_juntura(Na, Nd, cte.Si["ni"])
    print(phi_b_1)

    Na = 1e16
    Nd = 1e15
    phi_b_2 = potencial_juntura(Na, Nd, cte.Si["ni"])
    print(phi_b_2)

    print(phi_b_2/phi_b_1*100)


if __name__ == '__main__':
    main()
