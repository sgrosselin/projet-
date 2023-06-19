#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:18:12 2023

@author: salome
"""

class Utilisateur:
    def __init__(self,aff_dist, aff_tps):
        self.aff_dist = aff_dist
        self.aff_tps = aff_tps
        
        print("Nous allons vous proposer deux trajet: un plus rapide et l'autre moins gourmand en carburant" )
        print("Voici les deuc proposition en fonction de la distance")        
        print(self.aff_dist.plan_de_vol_dist())
        print("Voici les deuc proposition en fonction du temps")
        print(self.aff_tps.plan_de_vol())
        