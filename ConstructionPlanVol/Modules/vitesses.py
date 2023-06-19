import math as m
#from aircraft import Aircraft
#from consommation import Conso

## Constantes universelles
T11km= 216.66           # Température au niveau de la limite troposphère-stratosphère
TSL = 288.15        # Température en K au niveau de la mer
rhoSL = 1.225  # densite de reference en kg/m^3 au niveau de la mer
g0 = 9.81  # attraction gravitationnelle, en m/s^2
a = -0.0065  # constante d'evolution de temperature, en Kelvin/m
R = 287  # constante des gaz pour l'air, J / (kg K)
gamma_desc = 3.5
Cd0 = 0.015
e=0.8


class Vitesse :
    def __init__(self,avion):
        self.Avion= avion
        
    def calcul_vitesse(self):
        self.vitesse_max=[]
        vitesse_cruise = []
        self.altitude=[]
        self.Tliste=[]
        for i in range(5000, 13000, 100):   # i en m
            if (i/1000) < 11:  # Troposphère       # en Km
                T = TSL - 6.5 * (i/1000)    # en km
            else:
                T = T11km  # Stratosphère  
            self.altitude.append(i/1000)    #altitude en km
            self.Tliste.append(T)
            self.a= m.sqrt(1.4*287*T)
            vitesse_cruise.append(round((self.Avion.M_cruise * self.a),2))  # en m/s
            self.vitesse_max.append(round((self.Avion.M_max*self.a),2))  # en m/s
            #print(self.vitesse_max)
        #print("La température est de", T, "K")
        return self.vitesse_max, vitesse_cruise, self.Tliste
        
    def valeur_vitesse_max(self):
        i_max=0
        self.vmax=max(self.vitesse_max)
        for i in range(len(self.vitesse_max)):
            if self.vitesse_max[i] == self.vmax :
                i_max = i
        self.H_max = self.altitude[i_max]
        return i_max, self.H_max        #en km


    def vitesse_decrochage(self,consommation):
        self.conso=consommation
        Cltomax=1.8
        c,v,i_min=self.conso.consommation()
        Temp = self.Tliste[i_min]
        if Temp > T11km:
            self.rho = rhoSL * (Temp / TSL) ** (-g0 / (a * R) - 1)  # kg/m^3
        else:
            self.hcruise = self.altitude[i_min]
            rho11km = rhoSL * (T11km / TSL) ** (-g0 / (a * R) - 1)  # densite 11 km
            self.rho = rho11km * m.exp(-(g0 / (R * Temp)) * (self.hcruise - 11))  # densite apres 11 km
        print("La densité est de", self.rho, "kg/m^3")
        #print(m.sqrt(self.Avion.Wto*0.4535/(0.5*self.rho*Cltomax*self.Avion.s_alaire*0.0929))) #conversion ft^2 en m^2
        return m.sqrt(self.Avion.Wto*0.4535/(0.5*self.rho*Cltomax*self.Avion.s_alaire*0.0929)) #conversion ft^2 en m^2
    

    def vitesse_decollage(self,conso):
        print(1.1*self.vitesse_decrochage(conso))
        return 1.1*self.vitesse_decrochage(conso)

    def vitesse_descente(self):
        k=1/(m.pi*self.Avion.allongement*e)
        Cl = m.sqrt(Cd0/k)
        V_desc = m.sqrt((2*m.cos(m.degrees(gamma_desc))*self.Avion.Wla*0.4535)/(rhoSL*Cl*self.Avion.s_alaire*0.0929))
        return V_desc





#v=Vitesse()
#v.vitesse_decollage() 
    
    
    
    

