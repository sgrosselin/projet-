import math as m
#from aircraft import Aircraft
#from vitesses import Vitesse


#Cette classe nous permet de calculer la consommation spécifique de notre vol
class Conso:
    """
    Représente la classe Conso

    Attributs :
        - avion (classe) : la classe avion correspondant à l'avion choisit par l'utilisateur
        - V (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
    """
    def __init__(self, avion,V):
        """
           Initialise la consommation

           Arguments :
               - avion (classe) : la classe avion correspondant à l'avion choisit par l'utilisateur
               - V (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py

           """
    #On a besoin pour cela des informations sur l'avion et sur les différentes vitesses calculées

        self.Avion=avion
        self.v = V
        v_max,self.v_cruise,temp=self.v.calcul_vitesse() #m/s

    def consommation(self):
        """
        Calcul la consommation en carburant de l'avion choisit par l'utilisateur en fonction du trajet

        :return:
            - float : C, la consommation optimale en lb/lb/h
            - float : V, La vitesse de croisière pour la valeur de la consommation optimale calculée
            - int : i, La position de la consommation minimale dans la liste des consommations
        """
    # Nous allons calculer la consommation spécifique à l'aide de la formule de Breguet
        Rapport_poids_cruise= 0.975*0.975*0.995*self.Avion.Wto/self.Avion.Wla # On calcule d'abord de poids nécéssaire
        k=1/m.pi*0.8*self.Avion.allongement #Calcul du coefficient d'Oswald
        finesse_max= m.sqrt(1/(4*k*0.015)) #Calcul de la finesse maximale
        
        for i, vkts_cruise in enumerate(self.v_cruise):
        #Nous allons comparer chaque valeurs de C_min que nous aurons calculé afin de ne retenir que la plus petite
            self.C_min=1
            i_min=0
            C=(vkts_cruise*1.9438/self.Avion.range)*finesse_max*m.log(Rapport_poids_cruise)
             # la vitesse est en kts pour la formule de Breguet
            if C<self.C_min:
                self.C_min = C #C est en lb/lb.h
                i_min=i #On a besoin de garder la position de C_min dans la liste, afin de pouvoir réutilsier directement cette position dans nos calculs de vitesse, choix d'altitude ...
            else:
                self.C_min=self.C_min     #C est en lb/lb.h
        self.v_conso=self.v_cruise[i_min]

        return (round(self.C_min,5),self.v_conso, i_min)





