#!/usr/local/bin/python3


def main():
    # Una oblea de Silicio a temperatura ambiente está dopada con átomos aceptores con una concentración
    # de ND = 10^14 cm−3
    NA = 10e14
    T = 273 + 27
    ni = 10e9

    print("NA = " + str(NA))

    # ¿Cuál es la concentración de electrones n0 (cm−3) a temperatura ambiente?
    n0 = ni**2/NA
    print("n0 = " + str(n0))

    # ¿Cuál es la concentración de huecos p0 (cm−3) a temperatura ambiente?
    # 10^14  >>  10^9
    #  NA    >>   ni -> p0 = NA
    p0 = NA
    print("p0 = " + str(p0))

    # ¿Cómo cambian las concentraciones de portadores de carga n0 y p0 si el dopaje tiene una concentración
    # NA = 10e5 cm−3?
    # Si las concentraciones de NA cambian a 10e5, ahora son comparables con las concentraciones intrinsecas,
    # por lo que no se puede asegurar que p0 = NA


if __name__ == '__main__':
    main()
