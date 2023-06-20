<<<<<<< HEAD
import math as m

#On initialise les angles de montée et de descente
angle_montee = 5    # En degrée
angle_descente = 5 # En degrée

#Cette classe nous permet de calculer les distances dans les différentes phases de vol. On va calculer les distances parcourues par l'avion mais aussi les distances au sol qui ne sont pas les mêmes
class Distance:


    def __init__(self, vitesse, dist_aeroports):

        self.aeroports = dist_aeroports
        self.v = vitesse

    def distance_montee(self,alt):
    #Pour la distance de montée, on se sert de l'angle de montée
        d_mont = alt/ m.sin(m.radians(angle_montee)) #km
        d_mon_sol = d_mont*m.cos(m.radians(angle_montee)) #distance au sol en km
        return d_mon_sol, d_mont

    def distance_descente(self,alt):
    #Pour la distance de descente, on se sert de l'angle de descente
        d_desc = alt / m.sin(m.radians(angle_descente))
        d_desc_sol = d_desc*m.cos(m.radians(angle_descente)) # en km
        return d_desc_sol, d_desc   # km

    def distance_croisiere(self, d_desc_sol, d_mont_sol):
    #La distance de croisière est calculée en soustrayant les 2 distances précédentes à la distance totale
        d_cruise = self.aeroports - (d_desc_sol + d_mont_sol)  # km
        return d_cruise # km


=======
import math as m

#On initialise les angles de montée et de descente
angle_montee = 5    # En degrée
angle_descente = 5 # En degrée

#Cette classe nous permet de calculer les distances dans les différentes phases de vol. On va calculer les distances parcourues par l'avion mais aussi les distances au sol qui ne sont pas les mêmes
class Distance:


    def __init__(self, vitesse, dist_aeroports):

        self.aeroports = dist_aeroports
        self.v = vitesse

    def distance_montee(self,alt):
    #Pour la distance de montée, on se sert de l'angle de montée
        d_mont = alt/ m.sin(m.radians(angle_montee)) #km
        d_mon_sol = d_mont*m.cos(m.radians(angle_montee)) #distance au sol en km
        return d_mon_sol, d_mont

    def distance_descente(self,alt):
    #Pour la distance de descente, on se sert de l'angle de descente
        d_desc = alt / m.sin(m.radians(angle_descente))
        d_desc_sol = d_desc*m.cos(m.radians(angle_descente)) # en km
        return d_desc_sol, d_desc   # km

    def distance_croisiere(self, d_desc_sol, d_mont_sol):
    #La distance de croisière est calculée en soustrayant les 2 distances précédentes à la distance totale
        d_cruise = self.aeroports - (d_desc_sol + d_mont_sol)  # km
        return d_cruise # km


>>>>>>> 5d1d4fc568ab7f04cc92cdeb69293e35d9747d1f
