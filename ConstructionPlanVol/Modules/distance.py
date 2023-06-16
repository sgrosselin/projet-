import math as m
angle_montee = 3    # En degrée
angle_descente = 3.5 # En degrée
class Distance:

    angle_montee = 3    # En degrée
    angle_descente = 3.5 # En degrée
    def __init__(self, altitude_croisiere, dist_aeroports):
        self.altitude_croisiere = altitude_croisiere
        self.dist_aeroports = dist_aeroports

    def distance_montee(self):
        d_mont = self.altitude_croisiere/m.tan(m.pi/180*angle_montee)
        return d_mont

    def distance_descente(self):
        d_desc = self.altitude_croisiere / m.tan(m.pi/180*angle_descente)
        return d_desc

    def distance_croisiere(self, d_desc, d_mont):
        d_cruise = self.dist_aeroports - (d_desc + d_mont)
        return d_cruise


