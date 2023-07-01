#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:57:05 2023

@author: salome
"""
from modules import *


avion = Aircraft()
# Choix de l'avion de départ
aeroport= Aeroports()
# Choix de l'aéroport d'arrivée
vit=Vitesse(avion, aeroport)
# Création de la classe vitesse utilisant la classe avion
conso=Conso(avion,vit)
# Création de la classe conso pour l'avion et la vitesse calculée


s=aeroport.distance_aeroports()
lat_arrive,long_arrive=aeroport.coordonnees_arrive()

Dist = Distance(vit, s)


tps = Temps(Dist,vit, aeroport, avion)
c=Carburant(avion, tps, vit, conso)
b=Affichage(c, vit, tps, aeroport)
a=Affichage_dist(c, vit, Dist, aeroport)

utilisateur = Utilisateur (a,b, c, lat_arrive, long_arrive)



