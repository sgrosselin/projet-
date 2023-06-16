import math as m
angle_montee = 3    # En degrée
angle_descente = 3.5 # En degrée
class Distance:


    def __init__(self, altitude_croisiere, dist_aeroports):
        self.altitude_croisiere = altitude_croisiere
        self.dist_aeroports = dist_aeroports

    def distance_montee(self):
        d_mont = self.altitude_croisiere/m.tan(m.radians(angle_montee))
        print(f"La distance de montée est de :", d_mont, "ft")
        return d_mont

    def distance_descente(self):
        d_desc = self.altitude_croisiere / m.tan(m.radians(angle_descente))
        print(f"La distance de descente est de :", d_desc, "ft")
        return d_desc   # ft

    def distance_croisiere(self, d_desc, d_mont):
        d_cruise = self.dist_aeroports - (d_desc + d_mont)
        print(f"La distance de croisière est de :", d_cruise, "ft")
        return d_cruise # ft


