import math as m

## Constantes universelles
T11km= 216.66           # Température au niveau de la limite troposphère-stratosphère
TSL = 288.15        # Température en K au niveau de la mer
rhoSL = 1.225  # densite de reference en kg/m^3 au niveau de la mer
g0 = 9.81  # attraction gravitationnelle, en m/s^2
a0 = -0.0065  # constante d'evolution de temperature, en Kelvin/m
R = 287  # constante des gaz pour l'air, J / (kg K)
gamma_desc = 5
Cd0 = 0.015
e=0.8

#♣Cette classe calcule les vitesses en fonctions des différentes phases. On commence par calculer la "vitesse", la "vitesse max" et la "vitesse de descente", puis on calcule la "vitesse de décrochage" et la "vitesse de decollage" qui vont dépendre de la classe consommation
class Vitesse :
    def __init__(self,avion):
        self.Avion= avion

    def calcul_vitesse(self):
    #Cette fonction va nous ressortir une liste de vitesse max et une liste de vitesse de croisière ainsi que la liste de température
        self.vitesse_max=[]
        vitesse_cruise = []
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
            vitesse_cruise.append(round((self.Avion.M_cruise * self.a),2))  # en m/s
            #On calcule la vitesse de croisière avec le Mach de croisière
            self.vitesse_max.append(round((self.Avion.M_max*self.a),2))  # en m/s
            #On calcule la vitesse maximale avec le Mach max
        return self.vitesse_max, vitesse_cruise, self.Tliste

    def valeur_vitesse_max(self):
    #Cette fonction nous permet de ressortir la vitesse maximale de la liste de vitesse maximale. Suite à cela nous ressortirons la position dans la liste et l'altitude correspondante
        i_max=0
        self.vmax=max(self.vitesse_max)
        for i in range(len(self.vitesse_max)):
            #Cette boulce for nous permet de trouver à qu'elle position se situe la vitesse maximale
            if self.vitesse_max[i] == self.vmax :
                i_max = i
        self.H_max = self.altitude[i_max]
        return i_max, self.H_max        #en km


    def vitesse_decrochage(self,consommation):
        self.conso=consommation
        Cltomax=1.8 #Valeur de Cltomax prise pour une moyenne d'avion
        c,v,i_min=self.conso.consommation()
        Temp = self.Tliste[i_min] #On utilise la position return dans la classe consommation, afin d'avoir la position de C_min et donc d'utiliser la bonne température
        if Temp > T11km:
        #Il y a différents rho en fonction de la température
            self.rho = rhoSL * (Temp / TSL) ** (-g0 / (a0 * R) - 1)  # kg/m^3
        else:
            self.hcruise = self.altitude[i_min]
            rho11km = rhoSL * (T11km / TSL) ** (-g0 / (a0 * R) - 1)  # densite 11 km
            self.rho = rho11km * m.exp(-(g0 / (R * Temp)) * (self.hcruise - 11))  # densite apres 11 km
        return m.sqrt(self.Avion.Wto*0.4535/(0.5*self.rho*Cltomax*self.Avion.s_alaire*0.0929)) #conversion ft^2 en m^2
        #Formule qui nous permet de calculer la vitesse de décrochage


    def vitesse_decollage(self,conso):
    #La vitesse de décollage dépend de la vitesse de décrochage
        return 1.1*self.vitesse_decrochage(conso)

    def vitesse_descente(self):
        k=1/(m.pi*self.Avion.allongement*e) #Calcul du coefficient d'Oswald
        Cl = m.sqrt(Cd0/k) #Calcul du coefficient de trainée
        V_desc = m.sqrt((2*m.cos(m.degrees(gamma_desc))*self.Avion.Wla*0.4535)/(rhoSL*Cl*self.Avion.s_alaire*0.0929)) #Calcul de la vitesse de descente
        return V_desc









