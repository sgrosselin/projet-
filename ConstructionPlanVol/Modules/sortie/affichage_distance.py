#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:19:25 2023

@author: salome
"""
import matplotlib.pyplot as plt



class Affichage_dist:
    def __init__(self,conso,vitesse,distance, aeroport):
        self.c = conso
        self.v = vitesse
        self.d = distance
        self.a=aeroport
        
    def graphique_t_min(self):
        i_max,self.H_max = self.v.valeur_vitesse_max()
        dist_mont_max, dist_mont_sol_max = self.d.distance_montee(self.H_max)
        dist_desc_max, dist_desc_sol_max = self.d.distance_descente(self.H_max)
        
        i=0
        x_t_min=[0]
        y_t_min=[392/3281] #On part de l'altiude de notre aeroport de départ qui est CDG. Mais c'est en ft donc on le mets en km.
        while  y_t_min[-1]>= self.a.altitude/3281: #Tant que notre avion n'a pas atteint l'altitude de notre aeroport d'arrivée, on continue d'implémenter
            if i < dist_mont_sol_max :
                y_t_min.append((i*(self.H_max/dist_mont_sol_max) + y_t_min[0]))
                
            elif dist_mont_sol_max <i<dist_mont_sol_max +self.d.distance_croisiere(dist_mont_sol_max, dist_desc_sol_max):
                y_t_min.append(self.H_max)
                i_cruise = i
            else :
                y_t_min.append(self.H_max-((i-i_cruise)*(self.H_max/dist_desc_sol_max) + y_t_min[0]))
            x_t_min.append(i)
            i+=1
        y_t_min.pop(-1)
        x_t_min.pop(-1)
        
        return x_t_min,y_t_min
    
    def graphique_c_min(self):
        self.H_conso = self.v.hcruise
        dist_mont_conso, dist_mont_sol_conso = self.d.distance_montee(self.H_conso)
        dist_desc_conso, dist_desc_sol_conso = self.d.distance_descente(self.H_conso)
        
        i=0
        x_c_min=[0]
        y_c_min=[392/3281] #On part de l'altiude de notre aeroport de départ qui est CDG. Mais c'est en ft donc on le mets en km.
        while  y_c_min[-1]>= self.a.altitude/3281: #Tant que notre avion n'a pas atteint l'altitude de notre aeroport d'arrivée, on continue d'implémenter
            if i < dist_mont_sol_conso :
                y_c_min.append(i*(self.H_conso/dist_mont_sol_conso) + y_c_min[0])
                
            elif dist_mont_sol_conso <i<dist_mont_sol_conso +self.d.distance_croisiere(dist_mont_sol_conso, dist_desc_sol_conso):
                y_c_min.append(self.H_conso)
                i_cruise = i
            else :
                y_c_min.append(self.H_conso-((i-i_cruise)*(self.H_conso/dist_desc_sol_conso) + y_c_min[0]))
            x_c_min.append(i)
            i+=1
        y_c_min.pop(-1)
        x_c_min.pop(-1)
        
        return x_c_min,y_c_min
    
    
    def plan_de_vol_dist(self):
        x_t_min, y_t_min = self.graphique_t_min()
        x_c_min, y_conso_min = self.graphique_c_min()
        plt.figure(2)
        plt.plot(x_t_min, y_t_min, label='Trajet avec un temps minimum')
        plt.plot(x_c_min, y_conso_min, label='Trajet avec une consommation minimum')
        plt.xlabel('Distance en km')
        plt.ylabel('Altitude en km')
        plt.title(' Proposition de plan de vol en fonction de la distance')
        plt.grid()
        plt.legend()
        print(f"l'altitude pour un temps minimum est de " , self.H_max,"km") 
        print(f"l'altitude pour une consommation minimum est de " , self.H_conso,"km")
        return plt.show()

    
    
    
    
    
    
    
    
    
    
    
    
    
    