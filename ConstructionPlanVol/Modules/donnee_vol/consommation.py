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
        self.v_max,self.v_cruise,temp=self.v.calcul_vitesse() #m/s
        self.Rapport_poids_cruise= 0.975*0.975*0.995*self.Avion.Wto/self.Avion.Wla # On calcule d'abord de poids nécéssaire
        self.k=1/m.pi*0.8*self.Avion.allongement #Calcul du coefficient d'Oswald
        self.finesse_max= m.sqrt(1/(4*self.k*0.015)) #Calcul de la finesse maximale
   

    def consommation_mont(self,v):
        """
        Fonction qui calcule la consommation durant la phase de montée

        :param v:
            (float) :Vitesse de l'avion

        :return:

            - (float) : Consommation durant la phase de montée

        """
        v_montee = self.v.vitesse_montee(v)
        self.conso_montee = []
        for i in range(len(v_montee)) :
            conso=[]
            for j in v_montee[i]:
                conso.append((j*1.9438/self.Avion.range)*self.finesse_max*m.log(self.Rapport_poids_cruise))
                self.conso_montee.append(sum(conso)/len(conso))
        print()
        return self.conso_montee
     
    def consommation_cruise_min(self):
        """
        Calcul la consommation en carburant de l'avion choisit par l'utilisateur en fonction du trajet

        :return:

            - float : C : la consommation optimale en lb/lb/h

        """
    # Nous allons calculer la consommation spécifique à l'aide de la formule de Breguet
        self.conso_min = []     
        for i, vkts in enumerate(self.v_cruise):

            self.conso_min.append((vkts*1.9438/self.Avion.range)*self.finesse_max*m.log(self.Rapport_poids_cruise))          
             # la vitesse est en kts pour la formule de Breguet

        return self.conso_min


    def consommation_cruise_max(self):
        """
        Fonction qui calcule la consommation maximale durant la phase de croisière

        :return:

            - (float) : conso_max : Consommation maximale durant la phase de croisière

        """
    # Nous allons calculer la consommation spécifique à l'aide de la formule de Breguet   
        self.conso_max = []     
        for i, vkts in enumerate(self.v_max):

            self.conso_max.append((vkts*1.9438/self.Avion.range)*self.finesse_max*m.log(self.Rapport_poids_cruise))          
             # la vitesse est en kts pour la formule de Breguet

        return self.conso_max
        


