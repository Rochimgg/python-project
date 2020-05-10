import dispositivos_semiconductores.fisica_semiconductores.diccionario_constantes as cte
from dispositivos_semiconductores.fisica_semiconductores.funciones_calculos_guia_1 import concentration_int

# Calcular la conductividad de los siguientes materiales semiconductores intrínseco a temperatura ambiente.
# a) Silicio (Si):
# m∗n = 1.1 m0; m∗p = 0.56 m0;
# Eg = 1.12 eV;
# µn = 1450 cm2/Vs; µp = 500 cm2/Vs.
# b) Germanio (Ge):
# m∗n = 0.56 m0; m∗p = 0.29 m0;
# Eg = 0.66 eV;
# µn = 3900 cm2/Vs; µp = 2300 cm2/Vs.
# c) Arseniuro de Galio (GaAs):
# m∗n = 0.068 m0; m∗p = 0.47 m0;
# Eg = 1.42 eV;
# µn = 8500 cm2/Vs; µp = 400 cm2/Vs.


def main():

    # conductividad intrinseca en equilibrio
    # sigma = q(n0*mu_n + p0*mu_p) = q(mu_n + mu_p)*ni

    # Silicio
    mn = 1.1 * cte.electron_mass
    mp = 0.56 * cte.electron_mass
    Eg = 1.12
    mu_n = 1450
    mu_p = 500
    ni = concentration_int(mn, mp, 300, Eg)
    sigma_Si = cte.q*(mu_n + mu_p)*ni
    rho_si = 1/sigma_Si

    # Germanio
    mn = 0.56 * cte.electron_mass
    mp = 0.29 * cte.electron_mass
    Eg = 0.66
    mu_n = 3900
    mu_p = 400
    ni = concentration_int(mn, mp, 300, Eg)
    sigma_Ge = cte.q*(mu_n + mu_p)*ni
    rho_Ge = 1/sigma_Ge

    # Arseniuro de Galio
    mn = 8500 * cte.electron_mass
    mp = 400 * cte.electron_mass
    Eg = 1.42
    mu_n = 8500
    mu_p = 400
    ni = concentration_int(mn, mp, 300, Eg)
    sigma_GaAs = cte.q*(mu_n + mu_p)*ni
    rho_GaAs = 1/sigma_GaAs



if __name__ == '__main__':
    main()
