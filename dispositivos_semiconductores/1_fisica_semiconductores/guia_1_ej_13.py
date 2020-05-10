
import numpy as np

import dispositivos_semiconductores.fisica_semiconductores.diccionario_constantes as cte
from dispositivos_semiconductores.fisica_semiconductores.funciones_calculos_guia_1 import concentration_int


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
    T = 300
    mn = cte.electron_mass
    mp = 0.5 * cte.electron_mass
    Eg = 0.6
    mu_n = 2000
    mu_p = 1500

    ni = concentration_int(mn, mp, T, Eg)
    sigma = cte.q*(mu_n + mu_p) * ni
    rho = 1/sigma
    R = L*rho/A
    print(R)


if __name__ == '__main__':
    main()
