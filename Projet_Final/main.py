#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:57:05 2023

@author: salome
"""

import ProjetFinal

Avion = Aircraft()
Speed = Vitesse(Avion)
v_cruise=Speed.vitesse_cruise()
c = Conso(Avion, Speed)

print(v_cruise)