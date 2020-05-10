# Tres obleas, cada una de un material semiconductor distinto (Si, Ge y GaAs) son dopadas con átomos
# donores con una concentracion ND = 5e9 cm−3
# ¿Cuál es la concentración de electrones y huecos
# en cada uno de los materiales a temperatura ambiente? ¿Cuánto cambian en cada caso respecto de las
# concentraciones para los materiales intrínsecos?



def main():
    Na = 5e9
    ni_Si = 1.5e10  # cm^-3
    ni_Ge = 2.36e13  # cm^-3
    ni_GaAs = 1.8e6  # cm^-3

    #Si
    # n0 - ni^2/n0 = Nd - Na
    n0_Si = -Na/2 + math.sqrt((-Na/2)**2+ ni_Si**2)
    p0_Si = ni_Si**2/n0_Si

    #Ge
    # Na >> ni
    n0_Ge = (ni_Ge**2)/Na
    p0_Ge = ni_Ge

    #GaAs
    # n0 - ni^2/n0 = Nd - Na
    n0_GaAs = Na/2 + math.sqrt((-Na/2)**2+ ni_GaAs**2)
    p0_GaAs = ni_GaAs**2/n0_GaAs


if __name__ == '__main__':
    main()