#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
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


    def plan_de_vol_dist(self, lat, long):
        """
        Fonction qui va tracer le plan de vol pour un vol à consommation minimale et pour un temps minimal en fonction de la distance

         :return: Le tracé réalisé

        """
        x_t_min, y_t_min = self.graphique_t_min()
        x_c_min, y_conso_min = self.graphique_c_min()

        # Coordonnées des aéroports
        paris_longitude = np.deg2rad(2.3522)
        paris_latitude = np.deg2rad(48.8566)
        arrive_longitude = np.deg2rad(long)
        arrive_latitude = np.deg2rad(lat)

        # Listes des altitudes correspondantes à la trajectoire des avions
        y_avion1 = y_t_min
        y_avion2 = y_conso_min

        # Création de la figure et des axes 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Coordonnées sphériques de la Terre
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 50)
        earth_radius = 6371

        # Tracé de la sphère creuse représentant la Terre
        x = earth_radius * np.outer(np.cos(u), np.sin(v))
        y = earth_radius * np.outer(np.sin(u), np.sin(v))
        z = earth_radius * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x, y, z, alpha=0.3, edgecolor='none')

        # Tracé des aéroports
        ax.scatter([earth_radius * np.cos(paris_longitude) * np.sin(paris_latitude)],
                   [earth_radius * np.sin(paris_longitude) * np.sin(paris_latitude)],
                   [earth_radius * np.cos(paris_latitude)],
                   marker='o', s=50, color='red', label='Paris')
        ax.scatter([earth_radius * np.cos(arrive_longitude) * np.sin(arrive_latitude)],
                   [earth_radius * np.sin(arrive_longitude) * np.sin(arrive_latitude)],
                   [earth_radius * np.cos(arrive_latitude)],
                   marker='o', s=50, color='blue', label="Arrivée")

        # Initialisation des avions
        plane1 = ax.plot([], [], [], marker='o', markersize=5, color='green', label='Trajet avec un temps minimal')[0]
        trajectory1 = ax.plot([], [], [], color='green', linewidth=1, zorder=2)[0]
        plane2 = \
        ax.plot([], [], [], marker='o', markersize=5, color='orange', label='Trajet avec un consommation minimale')[0]
        trajectory2 = ax.plot([], [], [], color='orange', linewidth=1, zorder=2)[0]

        # Fonctions pour calculer les coordonnées des avions à un temps donné
        def calculate_plane_position_avion1(t):
            # Calcul de l'arc géodésique depuis Paris pour le premier avion
            arc_longitude = paris_longitude + t * (arrive_longitude - paris_longitude)
            arc_latitude = paris_latitude + t * (arrive_latitude - paris_latitude)
            altitude1 = y_avion1[int(t * (len(y_avion1) - 1))] * 100
            x_plane = (earth_radius + altitude1) * np.cos(arc_longitude) * np.sin(arc_latitude)
            y_plane = (earth_radius + altitude1) * np.sin(arc_longitude) * np.sin(arc_latitude)
            z_plane = (earth_radius + altitude1) * np.cos(arc_latitude)
            return x_plane, y_plane, z_plane

        def calculate_plane_position_avion2(i):
            # Calcul de l'arc géodésique depuis Paris pour le deuxième avion
            arc_longitude = paris_longitude + t * (arrive_longitude - paris_longitude)
            arc_latitude = paris_latitude + t * (arrive_latitude - paris_latitude)
            altitude2 = y_avion2[int(t * (len(y_avion2) - 1))] * 100
            x_plane = (earth_radius + altitude2) * np.cos(arc_longitude) * np.sin(arc_latitude)
            y_plane = (earth_radius + altitude2) * np.sin(arc_longitude) * np.sin(arc_latitude)
            z_plane = (earth_radius + altitude2) * np.cos(arc_latitude)
            return x_plane, y_plane, z_plane

        # Animation du mouvement des avions
        t_values = np.linspace(0, 1, len(y_avion1))

        t_values2 = np.linspace(0, 1, len(y_avion2))

        x_trajectory1, y_trajectory1, z_trajectory1 = [], [], []  # Trajectoire du premier avion
        x_trajectory2, y_trajectory2, z_trajectory2 = [], [], []  # Trajectoire du deuxième avion

        for t, i in zip(t_values, t_values2):
            # Effacer le graphique précédent des avions et des trajectoires
            plane1.set_data([], [])
            plane1.set_3d_properties([])
            trajectory1.set_data([], [])
            trajectory1.set_3d_properties([])
            plane2.set_data([], [])
            plane2.set_3d_properties([])
            trajectory2.set_data([], [])
            trajectory2.set_3d_properties([])

            # Calcul des nouvelles coordonnées des avions
            x_plane1, y_plane1, z_plane1 = calculate_plane_position_avion1(t)
            x_plane2, y_plane2, z_plane2 = calculate_plane_position_avion2(i)

            # Mise à jour des coordonnées des avions et des trajectoires
            plane1.set_data(x_plane1, y_plane1)
            plane1.set_3d_properties(z_plane1)
            x_trajectory1.append(x_plane1)
            y_trajectory1.append(y_plane1)
            z_trajectory1.append(z_plane1)
            trajectory1.set_data(x_trajectory1, y_trajectory1)
            trajectory1.set_3d_properties(z_trajectory1)
            plane2.set_data(x_plane2, y_plane2)
            plane2.set_3d_properties(z_plane2)
            x_trajectory2.append(x_plane2)
            y_trajectory2.append(y_plane2)
            z_trajectory2.append(z_plane2)
            trajectory2.set_data(x_trajectory2, y_trajectory2)
            trajectory2.set_3d_properties(z_trajectory2)

            # Affichage de la figure
            plt.pause(0.001)

            # Configuration des axes
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title('Visualisation des plans de vol')
            ax.legend()

            # Affichage de la figure finale
        plt.show()

    
    
    
    
    
    
    
    
    
    
    
    
    
    