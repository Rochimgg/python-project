import matplotlib.pyplot as plt
import numpy as np

import dispositivos_semiconductores.fisica_semiconductores.diccionario_constantes as cte
from dispositivos_semiconductores.fisica_semiconductores.funciones_calculos_guia_1 import concentration_int

# Dado un bloque de silicio cristalino intrínseco, considerando equilibrio térmico, temperatura ambiente,
# 12 µm de largo y 4 (µm)2 de seccion, se pide:
# a) Calcule la resistencia entre los extremos de la barra de silicio.
# b) Hallar la expresión de la corriente si se aplica una diferencia de potencial V_EXT entre los extremos
# del bloque. Indicar esquemáticamente el sentido del movimiento de los portadores.


def main():
    L = 12e-4  # cm
    A = 4e-8  # cm^2
    T = 300
    mn = 1.1 * cte.electron_mass
    mp = 0.56 * cte.electron_mass
    Eg = 1.12
    mu_n = 1450
    mu_p = 500

    ni = concentration_int(mn, mp, T, Eg)
    sigma = cte.q*(mu_n + mu_p) * ni
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
