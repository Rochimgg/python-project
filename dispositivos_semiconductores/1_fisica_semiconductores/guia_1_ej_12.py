import matplotlib.pyplot as plt
import numpy as np

from dispositivos_semiconductores.diccionario_constantes import *
from dispositivos_semiconductores.funciones_calculos import ni


# Para los tres materiales del ejercicio anterior, calcular la conductividad de cada uno de los materiales a
# distintas temperaturas dentro del rango T ∈ {−50◦C; 125◦C}. Realizar un gráfico con los datos obtenidos.
# (Suponer que es válido considerar unicamente la variación térmica de la movilidad debido a la dispersión
# de los portadores por oscilaciones de la red cirstalina.)


def main():

    T = np.arange(223., 398, 1)

    # Silicio
    mn = 1.1 * m0
    mp = 0.56 * m0
    Eg = 1.12
    mu_n = 1450
    mu_p = 500
    arr_rho = np.empty(len(T))
    for i in range(len(T)):
        arr_rho[i] = 1/(q*(mu_n + mu_p)*ni(mn, mp, T[i], Eg))
    plt.plot(T, arr_rho)
    plt.ylabel('rho Si (cm.ohm)')
    plt.xlabel('temperatura K')
    plt.show()

    # Germanio
    mn = 0.56 * m0
    mp = 0.29 * m0
    Eg = 0.66
    mu_n = 3900
    mu_p = 400
    arr_rho = np.empty(len(T))
    for i in range(len(T)):
        arr_rho[i] = 1/(q*(mu_n + mu_p)*ni(mn, mp, T[i], Eg))
    plt.plot(T, arr_rho)
    plt.ylabel('rho Ge (cm.ohm)')
    plt.xlabel('temperatura K')
    plt.show()

    # Arseniuro de Galio
    mn = 8500 * m0
    mp = 400 * m0
    Eg = 1.42
    mu_n = 8500
    mu_p = 400
    arr_rho = np.empty(len(T))
    for i in range(len(T)):
        arr_rho[i] = 1/(q*(mu_n + mu_p)*ni(mn, mp, T[i], Eg))
    plt.plot(T, arr_rho)
    plt.ylabel('rho GaAs (cm.ohm)')
    plt.xlabel('temperatura K')
    plt.show()


if __name__ == '__main__':
    main()

