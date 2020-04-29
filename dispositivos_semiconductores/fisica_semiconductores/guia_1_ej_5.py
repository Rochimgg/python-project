#!/usr/local/bin/python3


def main():
    # Una oblea de Silicio a temperatura ambiente está dopada con átomos donores con una concentración
    # de ND = 10^15 cm−3
    ND = 10e15
    T = 273 + 27
    ni = 10e9

    print("ND = " + str(ND))

    # ¿Cuál es la concentración de electrones n0 (cm−3) a temperatura ambiente?
    # 10^15  >>  10^9
    #  ND    >>   ni -> n0 = ND
    n0 = ND
    print("n0 = " + str(n0))

    # ¿Cuál es la concentración de huecos p0 (cm−3) a temperatura ambiente?
    p0 = ni ** 2 / ND
    print("p0 = " + str(p0))

    # ¿Cómo cambian las concentraciones de portadores de carga n0 y p0 si el dopaje tiene una concentración
    # ND = 10e8 cm−3?
    # Si las concentraciones de ND cambian a 10e8, ahora son comparables con las concentraciones intrinsecas,
    # por lo que no se puede asegurar que n0 = ND
    # TODO: plantear las ecuaciones para esto


if __name__ == '__main__':
    main()
