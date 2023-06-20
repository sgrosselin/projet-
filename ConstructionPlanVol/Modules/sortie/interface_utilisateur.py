
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:18:12 2023

@author: salome
"""

# Cette classe permet d'afficher à l'utilisateur les différents résultats obtenus
class Utilisateur:
    def __init__(self,aff_dist, aff_tps, conso):
        self.aff_dist = aff_dist
        self.aff_tps = aff_tps
        self.c = conso


      

        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("Voici les deux propositions en fonction du temps :\n")
        print(self.aff_tps.plan_de_vol())

        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("Voici les deux proposition en fonction de la distance :\n")
        print(self.aff_dist.plan_de_vol_dist())

        print(f"Pour le vol avec une consommation minimale, ",round(self.c.carburant_consommee_minimal(),3),"lbs de carburant ont été consommé" )
