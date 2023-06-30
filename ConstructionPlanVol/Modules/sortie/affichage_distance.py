#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

#Cette classe permet d'afficher l'altitude de l'avion en fonction de la distance

class Affichage_dist:
    """
    Classe qui va permettre d'afficher les courbes correspondant aux plans de vol

    Attributs:
        - conso (classe) : la classe conso correspondant à la consommation de l'avion choisi par l'utilisateur
        - vitesse (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
        - distance (classe) : la classe distance créee dans le fichier distance.py
        - aeroport (classe) : La classe aeroport créee dans le fichier aeroports.py

    """
    def __init__(self,conso,vitesse,distance, aeroport):
        """
            Initialise la classe Affichage_dist
            Arguments:
                - conso (classe) : la classe conso correspondant à la consommation de l'avion choisi par l'utilisateur
                - vitesse (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
                - distance (classe) : la classe distance créee dans le fichier distance.py
                - aeroport (classe) : La classe aeroport créee dans le fichier aeroports.py
        """
        self.c = conso
        self.v = vitesse
        self.d = distance
        self.a = aeroport
        
    #Cette fonction ressort les valeurs de x et y pour un plan de vol avec un temps minimum
    def graphique_t_min(self):
        """
        Fonction qui va calculer le plan de vol pour un vol à vitesse maximale

        :return:
            -list : Liste des distances pour l'ordonnée (qui va correspondre à la distance entre les aéroports)
            -list des altitudes de notre avion
        """
        i_max,self.H_max = self.v.valeur_vitesse_max()
        dist_mont_max, dist_mont_sol_max = self.d.distance_montee(self.H_max)
        dist_desc_max, dist_desc_sol_max = self.d.distance_descente(self.H_max)
        
        i=1
        x_t_min=[0]
        y_t_min=[392/3281] #On part de l'altiude de notre aeroport de départ qui est CDG. Mais c'est en ft donc on le mets en km.
        self.arrivee=self.a.altitude/3281
        while  y_t_min[-1]>= self.arrivee: #Tant que notre avion n'a pas atteint l'altitude de notre aeroport d'arrivée, on continue d'implémenter
            if i < dist_mont_sol_max :
            #Si i est plus petit que le temps de montée que l'on a calculé, alors on ajoute à y la valeur de la fonction affine qui dépend du coefficient directeur pour la montée
                y_t_min.append((i*((self.H_max- y_t_min[0])/dist_mont_sol_max) + y_t_min[0]))
                
            elif dist_mont_sol_max <i<dist_mont_sol_max +self.d.distance_croisiere(dist_mont_sol_max, dist_desc_sol_max):
            #si i est dans le temps de la croisière, alors on ajoute à y l'altitude de notre croisière
                y_t_min.append(self.H_max+ y_t_min[0])
                i_cruise = i+1
            else :
            # si i est dans le temps de descente, on ajoute à y la valeur de la fonction affine qui dépaend du coefficient directeur pour la descente
                y_t_min.append((self.H_max+ y_t_min[0])-((i-i_cruise)*((self.H_max-self.arrivee)/dist_desc_sol_max)))
            x_t_min.append(i)
            i+=1 #On incrémente i afin de continuer la boucle while
        y_t_min.pop(-1)
        x_t_min.pop(-1)
        
        return x_t_min,y_t_min
    
    #Cette fonction ressort les valeurs de x et y pour un plan de vol avec une consommation minimum
    def graphique_c_min(self):
        """
            Fonction qui va calculer le plan de vol pour un vol à consommation minimale

            :return:
                -list : Liste de la distance pour l'ordonnée (qui va correspondre à la distance entre les aéroports)
                -list des altitudes de notre avion

        """
        self.H_conso = self.v.hcruise
        dist_mont_conso, dist_mont_sol_conso = self.d.distance_montee(self.H_conso)
        dist_desc_conso, dist_desc_sol_conso = self.d.distance_descente(self.H_conso)
        i=1
        x_c_min=[0]
        y_c_min=[392/3281] #On part de l'altiude de notre aeroport de départ qui est CDG. Mais c'est en ft donc on le mets en km.
        
        while  y_c_min[-1]>= self.arrivee: #Tant que notre avion n'a pas atteint l'altitude de notre aeroport d'arrivée, on continue d'implémenter
            if i < dist_mont_sol_conso :
            #Si i est plus petit que le temps de montée que l'on a calculé, alors on ajoute à y la valeur de la fonction affine qui dépend du coefficient directeur pour la montée
                y_c_min.append(i*((self.H_conso-y_c_min[0])/dist_mont_sol_conso) + y_c_min[0])
                
            elif dist_mont_sol_conso <i<dist_mont_sol_conso +self.d.distance_croisiere(dist_mont_sol_conso, dist_desc_sol_conso):
            #si i est dans le temps de la croisière, alors on ajoute à y l'altitude de notre croisière
                y_c_min.append(self.H_conso+y_c_min[0])
                i_cruise = i+1
            else :
            # si i est dans le temps de descente, on ajoute à y la valeur de la fonction affine qui dépaend du coefficient directeur pour la descente
                y_c_min.append((self.H_conso+y_c_min[0])-((i-i_cruise)*((self.H_conso-self.arrivee)/dist_desc_sol_conso)))
            x_c_min.append(i)
            i+=1 #On incrémente i afin de continuer la boucle while
        y_c_min.pop(-1)
        x_c_min.pop(-1)
        
        return x_c_min,y_c_min


    def plan_de_vol_dist(self):
        """
        Fonction qui va tracer le plan de vol pour un vol à consommation minimale et pour un temps minimal en fonction de la distance

        :return: Le tracé réalisé

        """
    # Cette fonction affiche un graphique avec deux courbes, une pour le temps minimum et une pour la consommation minimum, le tout en fonction de la distance
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
        print(f"l'altitude pour un temps minimum est de " , round((self.H_max+self.arrivee),2),"km")
        print(f"l'altitude pour une consommation minimum est de " ,round( (self.H_conso+self.arrivee),2),"km")
        return plt.show()

    
    
    
    
    
    
    
    
    
    
    
    
    
    