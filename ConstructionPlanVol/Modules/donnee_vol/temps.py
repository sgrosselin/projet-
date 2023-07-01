# -*- coding: utf-8 -*-

#Cette classe nous permet de calculer les temps lors des diffÃ©rentes phases
class Temps:
    """
        ReprÃ©sente la classe temps pour calculer le temps de vol sur chacune des trois phases de vol

        Attributs :
            - dist (Classe) : La classe distance relative Ã  la distance parcourue par l'avion dans le fichier distance.py            - Vitesse (Classe) : la classe vitesse relative au trajet et Ã  l'avion crÃ©e dans le fichier vitesses.py
            - dist (Classe) : La classe distance relative Ã  la distance parcourue par l'avion dans le fichier distance.py            - Vitesse (Classe) : la classe vitesse relative au trajet et Ã  l'avion crÃ©e dans le fichier vitesses.py
            - vit (classe) : la classe vitesse relative au trajet et Ã  l'avion crÃ©e dans le fichier vitesses.py
            - conso (Classe) : la classe Conso relative dans le fichier consommation.py
        """
    def __init__(self,dist,vit,aero,avion):
        """
                Initialise la classe Temps

                Attributs :
                    - dist (Classe) : La classe distance relative Ã  la distance parcourue par l'avion dans le fichier distance.py            - Vitesse (Classe) : la classe vitesse relative au trajet et Ã  l'avion crÃ©e dans le fichier vitesses.py
                    - vit (classe) : la classe vitesse relative au trajet et Ã  l'avion crÃ©e dans le fichier vitesses.py
                    - conso (Classe) : la classe Conso relative dans le fichier consommation.py
                """
        self.d=dist
        self.v = vit
        self.aeroport = aero
        self.avion = avion

    def temps_mont(self,v):
        """
        Calcule le temps de montÃ©e
        :param alt: (float) : Altitude de la phase de croisiÃ¨re

        :return:
            - float : temps de montÃ©e en s
        """
        t_montee=[]
        v_montee = self.v.vitesse_montee(v)
        
        for i in range(len(v_montee)):
            t=[]
            
            for j in v_montee[i]:
                t.append(1147/j)
            t_montee.append(sum(t))
            
        return t_montee

    def temps_cruise(self,v_vol,alt):
        """
        Calcul le temps de vol durant la phase de croisiÃ¨re
        :param v_vol: (float) : Vitesse de croisiÃ¨re de l'avion
        :param alt: (float) Altitude de croisiÃ¨re de l'avion

        :return:
            float : Temps de vol durant la phase de croisiÃ¨re
        """
        self.d_desc_sol, self.d_desc= self.d.distance_descente(alt)
        self.d_montee_sol, self.d_mont = self.d.distance_montee(alt)
        self.tps_cruise=self.d.distance_croisiere(self.d_desc_sol,self.d_montee_sol)*1000/(v_vol) #Pour calculer le temps de croisiÃ¨re on utilise la distance de descente au sol et de montÃ©e au sol

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

