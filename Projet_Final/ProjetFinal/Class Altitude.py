import math as m

class Conso():
    def __init__(self, Avion, Vitesse):
        self.Vitesse=Vitesse
        self.Avion=Avion
    def conso(self):
        Rapport_poids_cruise= 0.975*0.975*0.995*self.Avion.Wto/self.Avion.Wla
        k=1/m.pi*0.8*self.Avion.A
        finesse_max= m.sqrt(1/(4*k*0.015))
        for i in self.Vitesse.vitesse_cruise:
            C_min=1
            i_min=0
            C=(i/self.range)*finesse_max*m.log(Rapport_poids_cruise)
            if C<C_min:
                C_min = C
                i_min=i
            else:
                C_min=C_min

        return (C_min, self.Vitesse.vitesse_cruise[i_min], i_min)
