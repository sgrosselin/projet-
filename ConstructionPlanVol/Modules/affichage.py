import matplotlib.pyplot as plt
import math as m
gamma_montee=3
gamma_desc = 3.5


class Affichage:
    def __init__(self, conso, vitesse, temps):
        self.c=conso
        self.v=vitesse
        self.t=temps

    def graphique_altitude_t_min(self):
        i_max, H_max = self.v.valeur_vitesse_max()
        i=0
        y_t_min=[0]
        x_t_min=[0]
        i_cruise=0
        #while i< self.t.temps_total(self.v.vmax):
        while y_t_min[i] >= 0:
            if i < self.t.temps_mont(self.v.vmax):
                y_t_min.append(self.v.vmax*m.tan(m.radians(gamma_montee)) * i)
            elif self.t.temps_mont(self.v.vmax)<i<self.t.temps_mont(self.v.vmax)+self.t.temps_cruise(self.v.vmax):
                y_t_min.append(H_max)
                i_cruise = i
            else :
                y_t_min.append(H_max-m.tan(m.radians(gamma_desc)) * (i-i_cruise))
            x_t_min.append(i)
            i+=1
        print(f" valeur de x, valeur de y_t_min :", x_t_min, y_t_min)
        return x_t_min, y_t_min


    def graphique_altitude_C_min(self):
        H_conso=self.v.hcruise
        i=0
        y_conso_min=[0]
        x_c_min=[0]
        i_cruise=0
        while y_conso_min[i] >= 0:
            if i < self.t.temps_mont(self.c.v_conso):
                y_conso_min.append(m.tan(m.radians(gamma_montee)) * i)
            elif self.t.temps_mont(self.c.v_conso)<i<self.t.temps_mont(self.v.vmax)+self.t.temps_cruise(self.c.v_conso):
                y_conso_min.append(H_conso)
                i_cruise = i
            else :
                y_conso_min.append(H_conso-m.tan(m.radians(gamma_desc)) * (i-i_cruise))
            x_c_min.append(i)
            i+=1
        print(f" valeur y_conso_min :", y_conso_min)
        return x_c_min, y_conso_min

    def plan_de_vol(self):
        x_t_min, y_t_min = self.graphique_altitude_t_min()
        x_c_min, y_conso_min = self.graphique_altitude_C_min()
        plt.plot(x_t_min, y_t_min, label='Trajet avec un temps minimum')
        plt.plot(x_c_min, y_conso_min, label='Trajet avec une consommation minimum')
        plt.xlabel('Temps en s')
        plt.ylabel('Altitude en km')
        plt.title(' Proposition de plan de vol')
        plt.grid()
        plt.legend()
        return plt.show()



