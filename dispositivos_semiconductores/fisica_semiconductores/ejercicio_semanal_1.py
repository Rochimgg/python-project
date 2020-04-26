#!/usr/local/bin/python3
import numpy as np
import math
import diccionario_constantes as cte
from funciones_calculos_guia_1 import concentration_int


def main():
    L = 3  # mm
    r = 0.5  # mm
    vol = np.pi ** 2 * L  # mm^3
    T = 300  # K

    # datos para Germanio
    Eg = 0.66  # eV
    mef_n = 0.56 * cte.m0  # kg
    mef_p = 0.29 * cte.m0  # kg
    mu_n = 3900  # cm^2V^-1s^-1  movilidad electrones
    mu_p = 2300  # cm^2V^-1s^-1  movilidad huecos
    ni_Ge = 2.36e13  # cm^-3

    print(cte.RESULT_FORMAT.format(concentration_int(mef_n, mef_p, T, Eg)))

    # n0 y p0 son las concentraciones volumétricas de electrones y huecos libres
    # Nc, Nv:  densidad de estados efectivos en las bandas de conducción y valencia
    # Ec, Ev: energía del nivel inferior de la banda de conducción y del superior en la de valencia.
    # EF: energía del nivel de Fermi: EF = (Ec + Ev)/2, para semiconductores intrínsecos.

    # densidad de carga volumetrica C/cm^3
    # rho = q(Nd - n0)

    # np = ni^2
    # en regimen intrínseco ni = n0 = p0

    # calcular la concentración de electrones y huecos libres


    # calcular la conductividad del material


    # datos para Silicio
    ni_Si = 1.5e10  # cm^-3
    Nv = 1.04e19  # cm^-3
    Nc = 2.8e19  # cm^-3
    mu_n = 1350  # cm^2V^-1s^-1  movilidad electrones
    mu_p = 500  # cm^2V^-1s^-1  movilidad huecos
    kT = cte.k * T
    mef_n = 1.1 * cte.m0  # kg
    mef_p = 0.59 * cte.m0  # kg

    Eg = 1.1 * cte.q # eV
    masa = math.sqrt(mef_n * mef_p)
    dospi = 2 * math.pi
    kT = cte.k * T
    planck_cuadrado = cte.h ** 2

    ni = math.sqrt(Nc*Nv*math.exp(-Eg/(2*kT)))

    print(cte.RESULT_FORMAT.format(concentration_int(mef_n, mef_p, T, Eg)))
#GaAS
    mef_n = 0.068 * cte.m0  # kg
    mef_p = 0.5 * cte.m0  # kg
    concentration_int(mef_n, mef_p, T, 1.43)

if __name__ == '__main__':
    main()
