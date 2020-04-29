
#  Se tiene una oblea de Silicio a temperatura ambiente dopada con una concentración de átomos aceptores
#  de NA = 1014 cm−3. Se agregan átomos donores con una concentración de ND = 7.5 × 1015 cm−3 en una región de la oblea.

# a) Esta región de la oblea, ¿es tipo n o tipo p?
# b) ¿Cuál es la concentración de electrones n0 (cm−3) a temperatura ambiente en esta región?
# c) ¿Cuál es la concentración de huecos p0 (cm−3) a temperatura ambiente en esta región?

def main():
    Na = 1e14  # cm^-3
    Nd = 7.5e15  # cm^-3
    ni_Si = 1.5e10  # cm^-3

    # n0 - ni^2/n0 = Nd - Na
    n0_Si = (Nd-Na)/2 + math.sqrt(((Nd-Na)/2)**2 + ni_Si**2)
    p0_Si = ni_Si**2/n0_Si


if __name__ == '__main__':
    main()