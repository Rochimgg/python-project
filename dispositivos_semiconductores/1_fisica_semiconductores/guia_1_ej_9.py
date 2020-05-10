#  Una oblea de Germanio en equilibrio térmico a temperatura ambiente está dopada con átomos aceptores
# con una concentracion de NA = 10^14 cm−3.
# a) Calcule la densidad de electrones y huecos en las bandas de conduccion y valencia, respectivamente.
# b) ¿Cómo cambian estas concentraciones si el equilibrio térmico es a una temperatura de 50◦C ¿Y si T = 150◦C?


def main():
    Na = 1e14  # cm^-3
    Nd = 0  # cm^-3
    ni_Ge = 2.36e13  # cm^-3

    # n0 - ni^2/n0 = Nd - Na
    n0_Ge = (Nd-Na)/2 + math.sqrt(((Nd-Na)/2)**2 + ni_Ge**2)
    p0_Ge = ni_Ge**2/n0_Ge

    # si T = (50 + 273)K

    # si T = (150 + 273)K


if __name__ == '__main__':
    main()
