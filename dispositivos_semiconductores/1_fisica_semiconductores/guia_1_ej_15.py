import matplotlib.pyplot as plt
import numpy as np

from dispositivos_semiconductores.diccionario_constantes import *
from dispositivos_semiconductores.funciones_calculos import ni

# Dado un bloque de silicio cristalino intrínseco, considerando equilibrio térmico, temperatura ambiente,
# 12 µm de largo y 4 (µm)2 de seccion, se pide:
# a) Calcule la resistencia entre los extremos de la barra de silicio.
# b) Hallar la expresión de la corriente si se aplica una diferencia de potencial V_EXT entre los extremos
# del bloque. Indicar esquemáticamente el sentido del movimiento de los portadores.


def main():
    L = 12e-4  # cm
    A = 4e-8  # cm^2
    T = 300
    mn = 1.1 * m0
    mp = 0.56 * m0
    Eg = 1.12
    mu_n = 1450
    mu_p = 500

    _ni = ni(mn, mp, T, Eg)
    sigma = q*(mu_n + mu_p) * _ni
    rho = 1/sigma
    R = L*rho/A
    print(R)
    V_EXT = np.arange(-10., 10, 1)

    arr_I = np.empty(len(V_EXT))
    for i in range(len(V_EXT)):
        arr_I[i] = V_EXT[i]/R
    plt.plot(V_EXT, arr_I)
    plt.ylabel('corriente (A)')
    plt.xlabel('tension (V)')
    plt.show()


if __name__ == '__main__':
    main()
