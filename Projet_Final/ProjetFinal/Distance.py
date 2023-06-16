import math as m

class Distance:

    def __init__(self, angle_montee,angle_descente, altitude_croisiere, dist_aeroports):
        self.angle_montee = angle_montee
        self.altitude_croisiere = altitude_croisiere
        self.angle_descente = angle_descente
        self.dist_aeroports = dist_aeroports

    def distance_montee(self):
        d_mont = self.altitude_croisiere/m.tan(m.pi/180*3)
        return d_mont

    def distance_descente(self):
        d_desc = self.altitude_croisiere / m.tan(m.pi/180*3.5)
        return d_desc

    def distance_croisiere(self, d_desc, d_mont):
        d_cruise = self.dist_aeroports - (d_desc + d_mont)
        return d_cruise


d_desc= Distance.distance_descente()
d_mont= Distance.distance_montee()
print(Distance.distance_croisiere(d_desc, d_mont))