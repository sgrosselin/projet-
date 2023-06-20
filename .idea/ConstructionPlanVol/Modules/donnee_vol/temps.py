
#Cette classe nous permet de calculer les temps lors des différentes phases
class Temps:

    def __init__(self,dist,vit,conso):
        self.d=dist
        self.v = vit
        self.c = conso

    def temps_mont(self,alt):
        self.d_montee_sol, self.d_mont = self.d.distance_montee(alt)
        self.tps_mont=self.d_mont*1000/(self.v.vitesse_decollage(self.c))# Notre vitesse est en metres par secondes, donc on multiplie par 1000 notre distance pour avoir des metres.
        return self.tps_mont

    def temps_cruise(self,v_vol,alt):
        self.d_desc_sol, self.d_desc= self.d.distance_descente(alt)

        self.tps_cruise=self.d.distance_croisiere(self.d_desc_sol,self.d_montee_sol)*1000/(v_vol) #Pour calculer le temps de croisière on utilise la distance de descente au sol et de montée au sol

        self.tps_cruise=self.d.distance_croisiere(self.d_desc_sol,self.d_montee_sol)*1000/v_vol
        #print(self.tps_cruise)

        return self.tps_cruise

    def temps_desc(self):
        self.tps_desc=self.d_desc*1000/(self.v.vitesse_descente())
        return self.tps_desc

    def temps_total(self, v_vol,alt):
    #On crée une fonction qui calcule le temps total
        self.tps_total =  self.temps_mont(alt) + self.temps_cruise(v_vol,alt) + self.temps_desc()
        return self.tps_total
