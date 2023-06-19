#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:57:05 2023

@author: salome
"""



from Modules import Aircraft, Utilisateur, Distance, Aeroports, Temps, Vitesse, Conso, Affichage, Affichage_dist, Carburant



avion = Aircraft()
# Choix de l'avion de départ
aeroport= Aeroports()
# Choix de l'aéroport d'arrivée
vit=Vitesse(avion)
# Création de la classe vitesse utilisant la classe avion
conso=Conso(avion,vit)
# Création de la classe conso

Vto=vit.vitesse_decollage(conso)
V_desc=vit.vitesse_descente()
Vmax,V_cruise, T=vit.calcul_vitesse()
s=aeroport.distance_aeroports()
Dist = Distance(vit, s)


tps = Temps(Dist,Vto,V_desc)
b=Affichage(conso, vit, tps, aeroport)
a=Affichage_dist(conso, vit, Dist, aeroport)
c=Carburant(avion, tps, vit, conso)
utilisateur = Utilisateur (a,b, c)



