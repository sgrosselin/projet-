import math as m
#from aircraft import Aircraft
#from vitesses import Vitesse

class Conso:
    def __init__(self, Aircraft,V):
        
        self.Avion=Aircraft
        self.V=V
        
    def consommation(self):
        Rapport_poids_cruise= 0.975*0.975*0.995*self.Avion.Wto/self.Avion.Wla
        k=1/m.pi*0.8*self.Avion.allongement
        finesse_max= m.sqrt(1/(4*k*0.015))
        vit,temp=self.V.vitesse_cruise()
        
        for i in range(len(vit)):
            C_min=1
            i_min=0
            C=(i/self.Avion.range)*finesse_max*m.log(Rapport_poids_cruise)
            if C<C_min:
                C_min = C
                i_min=i
            else:
                C_min=C_min
        
        print(round(C_min,5))
        return (round(C_min,5),vit[i_min], i_min)

#c= Conso()
#c.consommation()
