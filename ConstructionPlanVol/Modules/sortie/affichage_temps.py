import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Cette classe permet d'afficher l'altitude de l'avion en fonction du temps

class Affichage:
    """
        Classe qui va permettre d'afficher les courbes correspondant aux plans de vol en fonction du temps

        Attributs:
            - conso (classe) : la classe conso correspondant à la consommation de l'avion choisi par l'utilisateur
            - vitesse (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
            - temps (classe) : la classe temps créee dans le fichier temps.py
            - aeroport (classe) : La classe aeroport créee dans le fichier aeroports.py*

        """
    def __init__(self, conso, vitesse, temps, aeroport):
        """
            Initialise la classe Affichage

            Arguments:
                - conso (classe) : la classe conso correspondant à la consommation de l'avion choisi par l'utilisateur
                - vitesse (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
                - temps (classe) : la classe temps créee dans le fichier temps.py
                - aeroport (classe) : La classe aeroport créee dans le fichier aeroports.py

        """
        self.c=conso
        self.v=vitesse
        self.t=temps
        self.a=aeroport

    #Cette fonction ressort les valeurs de x et y pour un plan de vol avec un temps minimum
    def graphique_altitude_t_min(self):
        """
            Fonction qui va calculer le plan de vol pour un vol à vitesse maximale

            :return:
                -list : Liste des temps pour l'ordonnée (qui va correspondre au temps de vol)
                -list des altitudes de notre avion pour un temps de vol minimal

        """
        i_max, self.H_max = self.v.valeur_vitesse_max()
        i=1
        y_t_min=[392/3281] #On part de l'altiude de notre aeroport de départ qui est CDG. Mais c'est en ft donc on le mets en km.
        x_t_min=[0]
        i_cruise=0
        while  y_t_min[-1]>= self.a.altitude/3281:
        #Tant que notre avion n'a pas atteint l'altitude de notre aeroport d'arrivée, on continue d'implémenter
            if i < self.t.temps_mont(self.H_max):
            #Si i est plus petit que le temps de montée que l'on a calculé, alors on ajoute à y la valeur de la fonction affine qui dépend du coefficient directeur pour la montée
                y_t_min.append((((self.H_max-y_t_min[0])/self.t.temps_mont(self.H_max)) * i) + y_t_min[0])

            elif self.t.temps_mont(self.H_max)<i<self.t.temps_mont(self.H_max)+self.t.temps_cruise(self.v.vmax,self.H_max):
            #si i est dans le temps de la croisière, alors on ajoute à y l'altitude de notre croisière
                y_t_min.append(self.H_max+ y_t_min[0])
                i_cruise = i+1
            else :
            # si i est dans le temps de descente, on ajoute à y la valeur de la fonction affine qui dépaend du coefficient directeur pour la descente
                y_t_min.append((self.H_max+ y_t_min[0])-(((self.H_max-(self.a.altitude/3281))/self.t.temps_desc() * (i-i_cruise))))

            x_t_min.append(i)
            i+=1 #On incrémente i afin de continuer la boucle while
        y_t_min.pop(-1)
        x_t_min.pop(-1)
        return x_t_min, y_t_min, self.H_max

    #Cette fonction ressort les valeurs de x et y pour un plan de vol avec une consommation minimum
    def graphique_altitude_C_min(self):
        """
            Fonction qui va calculer le plan de vol pour un vol à consommation minimale

            :return:
                -list : Liste des temps pour l'ordonnée (qui va correspondre au temps de vol)
                -list des altitudes de notre avion pour une consommation minimale*

        """
        H_conso=self.v.hcruise
        i=1
        y_conso_min=[392/3281] #On part de l'altiude de notre aeroport de départ qui est CDG. Mais c'est en ft donc on le mets en km.
        x_c_min=[0]
        i_cruise=0
        while y_conso_min[-1]>= self.a.altitude/3281:
        #Tant que notre avion n'a pas atteint l'altitude de notre aeroport d'arrivée, on continue d'implémenter
            if i < self.t.temps_mont(H_conso):
            #Si i est plus petit que le temps de montée que l'on a calculé, alors on ajoute à y la valeur de la fonction affine qui dépend du coefficient directeur pour la montée
                y_conso_min.append(((H_conso-y_conso_min[0])/self.t.temps_mont(H_conso)) * i + y_conso_min[0])

            elif self.t.temps_mont(H_conso)<i<self.t.temps_mont(H_conso)+self.t.temps_cruise(self.c.v_conso,H_conso):
            #si i est dans le temps de la croisière, alors on ajoute à y l'altitude de notre croisière
                y_conso_min.append(H_conso+ y_conso_min[0])
                i_cruise = i+1
            else :
            # si i est dans le temps de descente, on ajoute à y la valeur de la fonction affine qui dépaend du coefficient directeur pour la descente
                y_conso_min.append((H_conso+ y_conso_min[0])-((i-i_cruise)*((H_conso-(self.a.altitude/3281))/self.t.temps_desc())))
            x_c_min.append(i)
            i+=1  #On incrémente i afin de continuer la boucle while
        x_c_min.pop(-1)
        y_conso_min.pop(-1)
        return x_c_min, y_conso_min

    def plan_de_vol(self):
        """
        Fonction qui va tracer le plan de vol pour un vol à consommation minimale et pour un temps minimal en fonction du temps

        :return: Le tracé réalisé
        """
    # Cette fonction affiche un graphique avec deux courbes, une pour le temps minimum et une pour la consommation minimum, le tout en fonction du temps
        x_t_min, y_t_min,H_max = self.graphique_altitude_t_min()

        x_t_min, y_t_min, H_max = self.graphique_altitude_t_min()

        x_c_min, y_conso_min = self.graphique_altitude_C_min()

        fig, ax = plt.subplots()
        line_t_min, = ax.plot(x_t_min, y_t_min, label='Trajet avec un temps minimum')
        line_c_min, = ax.plot(x_c_min, y_conso_min, label='Trajet avec une consommation minimum')


        position_avion1 = 0  # Position initiale de l'avion 1
        position_avion2 = 0  # Position initiale de l'avion 2
        last_frame = len(x_t_min) - 2  # Indice de l'avant-dernière position

        def update(frame):
            """
            Fonction qui réalise l'animation des avions sur le plan de vol

            :param frame: Paramètre pour mettre à jour la figure à chaque itération

            :return: La figure et l'animation
            """
            nonlocal position_avion1, position_avion2

            position_avion1 += self.c.v_conso / 2
            position_avion2 += max(self.v.vitesse_max) / 2.5

            if frame > self.t.temps_mont(H_max):
                position_avion1 += self.v.vitesse_descente() / 5
                position_avion2 += self.v.vitesse_descente() / 5

            ax.clear()
            ax.plot(x_t_min, y_t_min, label='Trajet avec un temps minimum')
            ax.plot(x_c_min, y_conso_min, label='Trajet avec une consommation minimum')

            if frame == last_frame:  # Dernière frame avant l'avant-dernière position
                if int(position_avion1) < len(x_t_min) - 1:
                    ax.scatter(x_t_min[int(position_avion1)], y_t_min[int(position_avion1)], color='red',
                               label='Avion 1')
                if int(position_avion2) < len(x_c_min) - 1:
                    ax.scatter(x_c_min[int(position_avion2)], y_conso_min[int(position_avion2)], color='green',
                               label='Avion 2')
            elif frame == len(x_t_min) - 1:  # Dernière frame, affichage final
                ax.scatter(x_t_min[-1], y_t_min[-1], color='red', label='Avion 1')
                ax.scatter(x_c_min[-1], y_conso_min[-1], color='green', label='Avion 2')
            else:
                if int(position_avion1) < len(x_t_min) - 1:
                    ax.scatter(x_t_min[int(position_avion1)], y_t_min[int(position_avion1)], color='red',
                               label='Avion 1')
                if int(position_avion2) < len(x_c_min) - 1:
                    ax.scatter(x_c_min[int(position_avion2)], y_conso_min[int(position_avion2)], color='green',
                               label='Avion 2')

            ax.set_xlabel('Temps en s')
            ax.set_ylabel('Altitude en km')
            ax.set_title('Proposition de plan de vol')
            ax.grid()
            ax.legend()

            if frame >= len(x_t_min) - 1:
                anim.event_source.stop()

        anim = FuncAnimation(fig, update, frames=len(x_t_min), interval=1, repeat=False)
        print(f"Le temps de trajet minimum est de", round(self.t.temps_total(self.v.vmax,self.H_max)/3600,2),'heures')
        print(f"Le temps de trajet pour une consommation minimum est de", round(self.t.temps_total(self.c.v_conso,self.v.hcruise)/3600,2),'heures')
        print(f"Le gain de temps est de",round((self.t.temps_total(self.c.v_conso,self.v.hcruise)- self.t.temps_total(self.v.vmax,self.H_max))/3600,2),'heures')
        plt.show()