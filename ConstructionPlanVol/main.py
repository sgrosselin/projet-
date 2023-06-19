#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:57:05 2023

@author: salome
"""

from Modules import Aircraft,Vitesse,Conso

from Modules import Distance, Aeroports, Temps, Vitesse, Conso, Affichage


avion = Aircraft()
aeroport= Aeroports()
vit=Vitesse(avion)
conso=Conso(avion,vit)
#c=conso.consommation()
Vto=vit.vitesse_decollage(conso)
V_desc=vit.vitesse_descente()
Vmax,V_cruise, T=vit.calcul_vitesse()
s=aeroport.distance_aeroports()
Dist = Distance(vit, s)

#D_montee_sol, D_montee=Dist.distance_montee(alt)
#D_desc_sol,D_desc=Dist.distance_descente()
#D_cruise=Dist.distance_croisiere(D_desc_sol,D_montee_sol)




"""v=Vitesse(avion)
conso=Conso(avion,v)
v.vitesse_decollage(conso) """
#v.vitesse_max()

tps = Temps(Dist,Vto,V_desc)
a=Affichage(conso, vit, tps)

a.plan_de_vol()
#tps = Temps(D_montee,D_cruise,D_desc,Vto,Vmax,V_desc)
#tps_mont, tps_cruise, tps_desc = tps.temps_mont(), tps.temps_cruise(), tps.temps_desc()
#print(tps.temps_total(tps_mont, tps_cruise, tps_desc)/3600)

