import math

## Constantes universelles
T11km= 216.66           # Température au niveau de la limite troposphère-stratosphère
TSL = 288.15        # Température en K au niveau de la mer
rhoSL = 0.00237  # densite de reference en slug/ft^3 au niveau de la mer
g0 = 9.81  # attraction gravitationnelle, en m/s^2
a = -0.0065  # constante d'evolution de temperature, en Kelvin/m
R = 287  # constante des gaz pour l'air, J / (kg K)

class Atmosphere:
    def __init__(self, altitude):       # Altitude donnée en ft
        self.altitude = altitude

    def Temperature(self):
        # evaluation de l'altitude en m : hm
        hm = self.altitude * 0.3048
        #T11km= 216.66           # Température au niveau de la limite troposphère-stratosphère
        #TSL = 288.15        # Température en K au niveau de la mer
        if hm < 11e3:                   # Troposphère
            T = TSL - 6.5e-3 * hm
        else:
            T = T11km                  # Stratosphère
        print("La température est de", T, "K")
        return T


    def density(self):
        T=self.Temperature()
        if T > T11km:
            rho = rhoSL * (T / TSL) ** (-g0 / (a * R) - 1)
        else:
            hm = self.altitude*0.3048  # conversion des pieds en metre
            rho11km = rhoSL * (T11km / TSL) ** (-g0 / (a * R) - 1)  # densite 11 km
            rho = rho11km * math.exp(-(g0 / (R * T)) * (hm - 11e3))  # densite apres 11 km
        print("La densité est de", rho, "slug/ft^3")
        return rho



