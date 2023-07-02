import math as m

#On initialise les angles de montée et de descente
angle_montee = 5    # En degrée
angle_descente = 5 # En degrée

#Cette classe nous permet de calculer les distances dans les différentes phases de vol. On va calculer les distances parcourues par l'avion mais aussi les distances au sol qui ne sont pas les mêmes
class Distance:
    """
    Représente la classe distance pour calculer la distance parcourue sur chacune des trois phases de vol

    Attributs :
        - Vitesse (Classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
        - dist_aeroports (flaot) : Utilise la fonction distance_aeroports de la classe Aeroports pour déterminer la distance entre l'aéroport de départ et d'arrivée
    """

    def __init__(self, vitesse, aeroports):
        """
            Initialise la classe distance

            Arguments :
                - Vitesse (Classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
                - dist_aeroports (flaot) : Utilise la fonction distance_aeroports de la classe Aeroports pour déterminer la distance entre l'aéroport de départ et d'arrivée
            """
        self.aeroports = aeroports
        self.v = vitesse
        self.dist_aero = self.aeroports.distance_aeroports()

    def distance_montee(self,alt):
        """
        Calcule la distance de montée réelle et la distance de montée au sol

        :param alt: (float) : Altitude de la phase de croisière

        :return:
            - float : Distance de montée en km
            - float : Distance au sol de parcourue pendant la phase de montée en km
        """
    #Pour la distance de montée, on se sert de l'angle de montée
        d_mont = alt/ m.sin(m.radians(angle_montee)) #km
        d_mon_sol = d_mont*m.cos(m.radians(angle_montee)) #distance au sol en km
        return d_mon_sol, d_mont

    def distance_descente(self,alt):
        """

        Calcule la distance de montée réelle et la distance de montée au sol

        :param alt: (float) : Altitude de la phase de croisière

        :return:
            - float : Distance de descente en km
            - float : Distance au sol de parcourue pendant la phase de descente en km
        """
    #Pour la distance de descente, on se sert de l'angle de descente
        d_desc = alt / m.sin(m.radians(angle_descente))
        d_desc_sol = d_desc*m.cos(m.radians(angle_descente)) # en km
        return d_desc_sol, d_desc   # km

    def distance_croisiere(self, d_desc_sol, d_mont_sol):
        """
        Calcule la distance de montée réelle et la distance de montée au sol

        :param d_desc_sol: (float) : Distance au sol parcourue pendant la phase de descente
        :param d_mont_sol: (float) : Distance au sol parcourue pendant la phase de montée

        :return:
            float : Distance parcourue durant la phase de croisière

        """
    #La distance de croisière est calculée en soustrayant les 2 distances précédentes à la distance totale
        d_cruise = self.dist_aero - (d_desc_sol + d_mont_sol)  # km
        return d_cruise # km


