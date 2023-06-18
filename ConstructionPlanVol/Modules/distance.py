import math as m
angle_montee = 3    # En degrée
angle_descente = 3.5 # En degrée
class Distance:


    def __init__(self, altitude_croisiere, dist_aeroports):
        self.altitude_croisiere = altitude_croisiere
        self.aeroports = dist_aeroports

    def distance_montee(self):
        #d_mont = self.altitude_croisiere/m.tan(m.radians(angle_montee))
        d_mont = self.altitude_croisiere / m.sin(m.radians(angle_montee))
        d_mon_sol = d_mont*m.cos(m.radians(angle_montee)) #km
        print(f"La distance de montée est de :", d_mont, "km")
        return d_mon_sol, d_mont

    def distance_descente(self):
        d_desc = self.altitude_croisiere / m.sin(m.radians(angle_descente))
        d_desc_sol = d_desc*m.cos(m.radians(angle_descente)) # en km
        print(f"La distance de descente est de :", d_desc, "Km")
        return d_desc_sol, d_desc   # km

    def distance_croisiere(self, d_desc_sol, d_mont_sol):
        d_cruise = self.aeroports - (d_desc_sol + d_mont_sol)  # km
        print(f"La distance de croisière est de :", d_cruise, "Km")
        return d_cruise # km


