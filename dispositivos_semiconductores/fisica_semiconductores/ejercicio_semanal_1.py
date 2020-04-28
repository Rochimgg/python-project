#!/usr/local/bin/python3
import numpy as np

import dispositivos_semiconductores.fisica_semiconductores.diccionario_constantes as cte
from dispositivos_semiconductores.fisica_semiconductores.funciones_calculos_guia_1 import concentration_int


# n0 y p0 son las concentraciones volumétricas de electrones y huecos libres
# Nc, Nv:  densidad de estados efectivos en las bandas de conducción y valencia
# Ec, Ev: energía del nivel inferior de la banda de conducción y del superior en la de valencia.
# EF: energía del nivel de Fermi: EF = (Ec + Ev)/2, para semiconductores intrínsecos.


def main():
    L = 3e-3  # cm
    r = 5e-4  # cm
    S = np.pi * r ** 2  # cm^2
    T = 300  # K
    kT = cte.k * T

    # datos para Germanio
    Eg = 0.66  # eV
    mef_n = 0.56 * cte.m0  # kg
    mef_p = 0.29 * cte.m0  # kg
    mu_n = 3900  # cm^2V^-1s^-1  movilidad electrones
    mu_p = 2300  # cm^2V^-1s^-1  movilidad huecos

    # calcular la concentración de electrones y huecos libres
    # en regimen intrínseco ni = n0 = p0
    ni_Ge = concentration_int(mef_n, mef_p, T, Eg)  # cm^-3

    # calcular la conductividad del material

    # conductividad intrinseca en equilibrio
    # sigma = q(n0*mu_n + p0*mu_p) = q(mu_n + mu_p)*ni
    # densidad de carga volumetrica C/cm^3
    # rho = q(Nd - n0) = sigma^-1
    sigma = cte.q * (mu_n + mu_p) * ni_Ge  # S cm^-1

    print(cte.RESULT_FORMAT.format(ni_Ge))
    print(cte.RESULT_FORMAT.format(sigma))

    # Si el material fuese Silicio (Si) dopado uniformememnte con fósforo (P)
    # P es un elemento del grupo V (donores) Deberia buscar la concentracion de
    # atomos donores para obtener la misma conductividad

    # datos para Silicio

    ni_Si = 1.5e10  # cm^-3
    mu_n = 1350  # cm^2V^-1s^-1  movilidad electrones
    mu_p = 500  # cm^2V^-1s^-1  movilidad huecos
    Nd_Si = sigma / cte.q / mu_n  # cm^-3

    print(cte.RESULT_FORMAT.format(Nd_Si))

    # Calcular el valor de resistencia (R) para la geometria del problema.

    rho = sigma ** (-1)  # Ω cm
    R = rho * L / S  # Ω

    print(cte.RESULT_FORMAT.format(R))

    # Calcular la corriente que circula al aplicar una tensión de 3V entre las caras del cilindro.
    # ¿Cuánto es la contribución de corriente de electrones y corriente de huecos?
    I = 3 / R  # A Por Ohm
    print(cte.RESULT_FORMAT.format(I))

    # Considero el Silicio dopado uniformemente, por lo que las corrientes de difusion
    # son despreciables en este caso, solo tomare en cuenta las corrientes de arrastre
    # El campo electrico tiene direccion correspondiente con la longitud del alambre

    E = 3 / L  # V / long
    dndx = 0
    dpdx = 0
    p = ni_Si ** 2 / Nd_Si
    n = Nd_Si
    Dn = kT * mu_n / cte.q
    Dp = kT * mu_p / cte.q
    Jna = cte.q * mu_n * n * E
    Jnd = cte.q * Dn * dndx
    Jn = Jna + Jnd
    Jpa = cte.q * mu_p * p * E
    Jpd = - cte.q * Dp * dpdx
    Jp = Jpa + Jpd
    J = Jn + Jp  # A/cm^2
    In = Jn * S
    Ip = Jp * S
    I = J * S

    print(cte.RESULT_FORMAT.format(Jn))
    print(cte.RESULT_FORMAT.format(Jp))
    print(cte.RESULT_FORMAT.format(J))
    print(cte.RESULT_FORMAT.format(In))
    print(cte.RESULT_FORMAT.format(Ip))
    print(cte.RESULT_FORMAT.format(I))


if __name__ == '__main__':
    main()
