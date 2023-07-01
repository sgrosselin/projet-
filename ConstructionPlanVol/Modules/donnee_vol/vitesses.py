import math as m

## Constantes universelles
T11km= 216.66           # Température au niveau de la limite troposphère-stratosphère
TSL = 288.15        # Température en K au niveau de la mer
rhoSL = 1.225  # densite de reference en kg/m^3 au niveau de la mer
g0 = 9.81  # attraction gravitationnelle, en m/s^2
a0 = -0.0065  # constante d'evolution de temperature, en Kelvin/m
R = 287  # constante des gaz pour l'air, J / (kg K)
gamma_desc = 3.5
Cd0 = 0.015
e=0.8

#♣Cette classe calcule les vitesses en fonctions des différentes phases. On commence par calculer la "vitesse", la "vitesse max" et la "vitesse de descente", puis on calcule la "vitesse de décrochage" et la "vitesse de decollage" qui vont dépendre de la classe consommation
class Vitesse :
    """
        Classe Vitesse qui permet de calculer la vitesse de l'avion sur différentes phases de vol

        Attributs :
            - avion (Classe) : La classe avion relative à l'avion choisi par l'utilisateur

        """
    def __init__(self,avion,aero):
        """
        Initialise la classe Vitesse
        :param - avion (Classe) : La classe avion relative à l'avion choisi par l'utilisateur
        """
        self.Avion= avion
        self.aeroport = aero
        
    def calcul_vitesse(self):
        """
        Fonction qui calcule la vitesse maximale de l'avion
        :return:
            - list : Liste des vitesses maximales de l'avion
            - list : Liste des vitesses de croisière de l'avion
            - list : Liste des températures
        """
    #Cette fonction va nous ressortir une liste de vitesse max et une liste de vitesse de croisière ainsi que la liste de température
        self.vitesse_max=[]
        self.vitesse_cruise = []
        self.altitude=[]
        self.Tliste=[]
        #On va créer une boucle for, qui va parcourir une liste d'altitude
        for i in range(5000, 13000, 100):   # i en m
        #Il y a différentes température en fonction de l'altitude
            if (i/1000) < 11:  # Troposphère       # en Km
                T = TSL - 6.5 * (i/1000)    # en km
            else:
                T = T11km  # Stratosphère
            self.altitude.append(i/1000)    #altitude en km
            self.Tliste.append(T)
            self.a= m.sqrt(1.4*287*T) #On calcule la vitesse du son
            self.vitesse_cruise.append(round((self.Avion.M_cruise * self.a),2))  # en m/s
            #On calcule la vitesse de croisière avec le Mach de croisière
            self.vitesse_max.append(round((self.Avion.M_max*self.a),2))  # en m/s
            #On calcule la vitesse maximale avec le Mach max
        return self.vitesse_max, self.vitesse_cruise, self.Tliste

    def valeur_vitesse_max(self):
        """
        Permet de calculer la vitesse maximale
        :return:
            - int : Position de la vitesse maximale dans la liste des vitesses
            - float : Altitude pour laquelle on a une vitesse maximale
        """
    #Cette fonction nous permet de ressortir la vitesse maximale de la liste de vitesse maximale. Suite à cela nous ressortirons la position dans la liste et l'altitude correspondante
        i_max=0
        self.v_max=max(self.vitesse_max)
        for i in range(len(self.vitesse_max)):
            #Cette boulce for nous permet de trouver à qu'elle position se situe la vitesse maximale
            if self.vitesse_max[i] == self.v_max :
                i_max = i
        self.H_max = self.altitude[i_max]
        return i_max, self.H_max, self.v_max        #en km

    def vitesse_montee (self,vitesse):
        v_montee = []
        for i in range(len(self.vitesse_cruise)):
            coeff_directeur = (vitesse[i] - self.Avion.V_decollage*0.514)/(self.altitude[i]*1000 - self.aeroport.altitude*0.305)
            alt_aeroport = int(self.aeroport.altitude*0.305)
            v=[]
            for x in range(alt_aeroport,int(self.altitude[i]*1000),100):               
                v.append(coeff_directeur*x + self.Avion.V_decollage*0.514)
            v_montee.append(v)
        #print(v_montee[0])
        return v_montee


    def vitesse_descente(self):
        """
        Calcume la vitesse pour la phase de descente de l'avion

        :return:
            float : Vitesse de descente de l'avion
        """
        k=1/(m.pi*self.Avion.allongement*e) #Calcul du coefficient d'Oswald
        Cl = m.sqrt(Cd0/k) #Calcul du coefficient de trainée
        V_desc = m.sqrt((2*m.cos(m.degrees(gamma_desc))*self.Avion.Wla*0.4535*9.81)/(rhoSL*Cl*self.Avion.s_alaire*0.0929)) #Calcul de la vitesse de descente
        return V_desc









