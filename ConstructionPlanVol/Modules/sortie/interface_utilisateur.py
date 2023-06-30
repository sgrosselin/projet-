#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Cette classe permet d'afficher à l'utilisateur les différents résultats obtenus
class Utilisateur:
    """
    Classe Utilisateur qui va permettre de faire l'interface utilisateur et d'afficher les plans de vol

    Attributs :
        - aff_dist (Classe) : Classe Affichage_dist créee dans le fichier affichage_distance.py
        - aff_tps (Classe) : Classe Affichage créee dans le fichier affichage_temps.py
        - conso (Classe) : La classe conso de l'avion choisi dans le fichier consommation.py
    """
    def __init__(self,aff_dist, aff_tps, conso, lat, long):
        """
            Initialise la classe Utilisateur

            Arguments:
                - aff_dist (Classe) : Classe Affichage_dist créee dans le fichier affichage_distance.py
                - aff_tps (Classe) : Classe Affichage créee dans le fichier affichage_temps.py
                - conso (Classe) : La classe conso de l'avion choisi dans le fichier consommation.py
            """
        self.aff_dist = aff_dist
        self.aff_tps = aff_tps
        self.c = conso
        self.lat = lat
        self.long = long



      

        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("Voici les deux propositions en fonction du temps :\n")
        print(self.aff_tps.plan_de_vol())

        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("Voici les deux proposition en fonction de la distance :\n")
        print(self.aff_dist.plan_de_vol_dist(lat,long))

        print(f"Pour le vol avec une consommation minimale, ",round(self.c.carburant_consommee_minimal(),3),"lbs de carburant ont été consommé" )
