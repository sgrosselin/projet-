import math as m
#from aircraft import Aircraft
#from consommation import Conso

## Constantes universelles
T11km= 216.66           # Température au niveau de la limite troposphère-stratosphère
TSL = 288.15        # Température en K au niveau de la mer
rhoSL = 0.00237  # densite de reference en slug/ft^3 au niveau de la mer
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
        vitesse_max=[]
        vitesse_cruise = []
        self.altitude=[]
        self.Tliste=[]
        for i in range(10000, 41000, 1000):
            if i < 11e3:  # Troposphère
                T = TSL - 6.5e-3 * i
            else:
                T = T11km  # Stratosphère  
            self.altitude.append(i)
            self.Tliste.append(T)
            self.a= m.sqrt(1.4*1716*T)
            vitesse_cruise.append(round((self.Avion.M_cruise * self.a),2))
            vitesse_max.append(round((self.Avion.M_max*self.a),2))
        print("La température est de", T, "K")
        return vitesse_max, vitesse_cruise, self.Tliste
        

    def vitesse_decrochage(self,consommation):
        self.conso=consommation
        Cltomax=1.8
        c,v,i_min=self.conso.consommation()
        Temp = self.Tliste[i_min]
        if Temp > T11km:
            rho = rhoSL * (Temp / TSL) ** (-g0 / (a * R) - 1)
        else:
            hm = self.altitude[i_min]
            rho11km = rhoSL * (T11km / TSL) ** (-g0 / (a * R) - 1)  # densite 11 km
            self.rho = rho11km * m.exp(-(g0 / (R * Temp)) * (hm - 11e3))  # densite apres 11 km
        print("La densité est de", rho, "slug/ft^3")
        print(m.sqrt(self.Avion.Wto/(0.5*rho*Cltomax*self.Avion.s_alaire)))
        return m.sqrt(self.Avion.Wto/(0.5*rho*Cltomax*self.Avion.s_alaire))
    

    def vitesse_decollage(self,conso):
        print(1.1*self.vitesse_decrochage(conso))
        return 1.1*self.vitesse_decrochage(conso)

    def vitesse_descente(self):
        k=1/(m.pi*self.Avion.allongement*e)
        Cl = m.sqrt(Cd0/k)
        V_desc = m.sqrt((2*m.cos(m.degrees(gamma_desc))*self.Avion.Wla)/(rhoSL*Cl*self.Avion.s_alaire))
        return V_desc





#v=Vitesse()
#v.vitesse_decollage() 
    
    
    
    

