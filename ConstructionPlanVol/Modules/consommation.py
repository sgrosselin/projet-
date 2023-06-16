import math as m
#from aircraft import Aircraft
#from vitesses import Vitesse

class Conso:
    def __init__(self, avion,V):
        
        self.Avion=avion
        self.V=V
        
    def consommation(self):
        Rapport_poids_cruise= 0.975*0.975*0.995*self.Avion.Wto/self.Avion.Wla
        k=1/m.pi*0.8*self.Avion.allongement
        finesse_max= m.sqrt(1/(4*k*0.015))
        v_max,v_cruise,temp=self.V.calcul_vitesse()
        
        for i in range(len(v_cruise)):
            C_min=1
            i_min=0
            C=(i/self.Avion.range)*finesse_max*m.log(Rapport_poids_cruise)
            if C<C_min:
                C_min = C
                i_min=i
            else:
                C_min=C_min

        return (round(C_min,5),v_cruise[i_min], i_min)

#c= Conso()
#c.consommation()
