#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:57:05 2023

@author: salome
"""

from Modules import Aircraft,Vitesse,Conso

from Modules import Distance, Aeroports, Temps, Vitesse, Conso


avion = Aircraft()
aeroport= Aeroports()
vit=Vitesse(avion)
conso=Conso(avion,vit)
c,v,i=conso.consommation()
Vto=vit.vitesse_decollage(c)
V_desc=vit.vitesse_descente()
Vmax,V_cruise=vit.calcul_vitesse()
s=aeroport.distance_aeroports()
Dist = Distance(40000, s)
D_montee=Dist.distance_montee()
D_desc=Dist.distance_descente()
D_cruise=Dist.distance_croisiere(D_desc,D_montee)



"""v=Vitesse(avion)
conso=Conso(avion,v)
v.vitesse_decollage(conso) """
#v.vitesse_max()

tps = Temps(D_montee,D_cruise,D_desc,Vto,V_cruise,V_desc)
tps.temps_cruise()

