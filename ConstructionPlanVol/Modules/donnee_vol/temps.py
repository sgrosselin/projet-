
#Cette classe nous permet de calculer les temps lors des différentes phases
class Temps:
    """
        Représente la classe temps pour calculer le temps de vol sur chacune des trois phases de vol

        Attributs :
            - dist (Classe) : La classe distance relative à la distance parcourue par l'avion dans le fichier distance.py            - Vitesse (Classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
            - vit (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
            - conso (Classe) : la classe Conso relative dans le fichier consommation.py
        """
    def __init__(self,dist,vit,conso):
        """
                Initialise la classe Temps

                Attributs :
                    - dist (Classe) : La classe distance relative à la distance parcourue par l'avion dans le fichier distance.py            - Vitesse (Classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
                    - vit (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
                    - conso (Classe) : la classe Conso relative dans le fichier consommation.py
                """
        self.d=dist
        self.v = vit
        self.c = conso

    def temps_mont(self,alt):
        """
        Calcule le temps de montée
        :param alt: (float) : Altitude de la phase de croisière

        :return:
            - float : temps de montée en s
        """
        self.d_montee_sol, self.d_mont = self.d.distance_montee(alt)
        self.tps_mont=self.d_mont*1000/(self.v.vitesse_decollage(self.c))# Notre vitesse est en km/s, donc on multiplie par 1000 notre distance pour avoir des metres.
        return self.tps_mont

    def temps_cruise(self,v_vol,alt):
        """
        Calcul le temps de vol durant la phase de croisière
        :param v_vol: (float) : Vitesse de croisière de l'avion
        :param alt: (float) Altitude de croisière de l'avion

        :return:
            float : Temps de vol durant la phase de croisière
        """
        self.d_desc_sol, self.d_desc= self.d.distance_descente(alt)

        self.tps_cruise=self.d.distance_croisiere(self.d_desc_sol,self.d_montee_sol)*1000/(v_vol) #Pour calculer le temps de croisière on utilise la distance de descente au sol et de montée au sol

        self.tps_cruise=self.d.distance_croisiere(self.d_desc_sol,self.d_montee_sol)*1000/v_vol
        #print(self.tps_cruise)

        return self.tps_cruise

    def temps_desc(self):
        """
            Calcule le temps de descente

            :return:
                - float : temps de descente en s
        """
        self.tps_desc=self.d_desc*1000/(self.v.vitesse_descente())
        return self.tps_desc

    def temps_total(self, v_vol,alt):
        """
        Calcule le temps de vol total (toutes phases comprises) pour l'avion et l'aéroport de destination choisis
        :param v_vol: Vitesse de croisière
        :param alt: (float) : Altitude de croisière

        :return:
            - float : temps total de vol en s
        """
    #On crée une fonction qui calcule le temps total
        self.tps_total =  self.temps_mont(alt) + self.temps_cruise(v_vol,alt) + self.temps_desc()
        return self.tps_total
