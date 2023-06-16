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
class Vitesse :
    def __init__(self, toto):
        self.Avion=toto
        

    def vitesse_max(self):
        vitesse_max=[]
        for i in range(10000, 41000, 1000):
            hm = i * 0.3048
            T11km= 216.66           # Température au niveau de la limite troposphère-stratosphère
            TSL = 288.15        # Température en K au niveau de la mer
            if hm < 11e3:  # Troposphère
                T = TSL - 6.5e-3 * hm
            else:
                T = T11km  # Stratosphère       
            self.a= m.sqrt(1.4*1716*T)
            vitesse_max.append(round((self.Avion.M_max*self.a),2))
        print("La température est de", T, "K")
        print(vitesse_max)
        return vitesse_max

    def vitesse_cruise(self):
        vitesse_cruise = []
        Tliste=[]
        for i in range(10000, 41000, 1000):
            hm = i * 0.3048
            T11km= 216.66           # Température au niveau de la limite troposphère-stratosphère
            TSL = 288.15        # Température en K au niveau de la mer
            if hm < 11e3:  # Troposphère
                T = TSL - 6.5e-3 * hm
            else:
                T = T11km  # Stratosphère
            Tliste.append(T)            
            self.a = m.sqrt(1.4 * 1716 * T)
            vitesse_cruise.append(round((self.Avion.M_cruise * self.a),2))
        print("La température est de", T, "K")
        return (vitesse_cruise, Tliste)
#v=Vitesse()
#v.vitesse_cruise()

    

    def vitesse_decrochage(self, Conso):
        
        vitesse_cruise, Tliste = self.vitesse_cruise()
        Cltomax=1.8
        T11km = 216.66  # Température au niveau de la limite troposphère-stratosphère
        TSL = 288.15
        c,v,i=self.conso.consommation()
        T = Tliste[self.c.i_min]
        if T > T11km:
            rho = rhoSL * (T / TSL) ** (-g0 / (a * R) - 1)
        else:
            hm = self.altitude * 0.3048  # conversion des pieds en metre
            rho11km = rhoSL * (T11km / TSL) ** (-g0 / (a * R) - 1)  # densite 11 km
            rho = rho11km * m.exp(-(g0 / (R * T)) * (hm - 11e3))  # densite apres 11 km
        print("La densité est de", rho, "slug/ft^3")
        
        return round(m.sqrt(self.Avion.Wto/(0.5*rho*Cltomax*self.Avion.s_alaire)),2)
    

    def vitesse_decollage(self):
        print(1.1*self.vitesse_decrochage)
        return 1.1*self.vitesse_decrochage
    
#v=Vitesse()
#v.vitesse_decollage() 
    
    
    
    

