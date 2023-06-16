#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:57:05 2023

@author: salome
"""

from Modules import Aircraft,Vitesse,Conso

from Modules import Distance, Aeroports


avion = Aircraft()
#aeroport= Aeroports()
#s=aeroport.distance_aeroports()
#Dist = Distance(40000, s)
#print(Dist.distance_montee())

v=Vitesse(avion)
conso=Conso(avion,v)
v.vitesse_decollage(conso) 
#v.vitesse_max()
