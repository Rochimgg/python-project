
import numpy as np

from dispositivos_semiconductores.diccionario_constantes import *
from dispositivos_semiconductores.funciones_calculos import ni


# Una muestra semiconductora intrínseca de forma de cilindro de radio R = 0.2 mm y largo L = 2 mm se
# encuentra a T = 300 K y tiene las siguientes características:
# Eg = 0.6 eV;
# m∗n = m0; m∗p = 0.5 × m0;
# µn = 2000 cm2/Vs; µp = 1500 cm2/Vs.
# Calcular el valor de resistencia de la muestra.


def main():
    L = 0.2  # cm
    R = 0.02  # cm
    A = np.pi * R ** 2
    T = T_amb
    mn = m0
    mp = 0.5 * m0
    Eg = 0.6
    mu_n = 2000
    mu_p = 1500

    _ni = ni(mn, mp, T, Eg)
    sigma = q*(mu_n + mu_p) * _ni
    rho = 1/sigma
    R = L*rho/A
    print(R)


if __name__ == '__main__':
    main()
