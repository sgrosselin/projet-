class Temps:

    def __init__(self,dist,vto,v_desc):
        self.d=dist
        self.vto = vto
        self.v_desc=v_desc

    def temps_mont(self,alt):
        self.d_montee_sol, self.d_mont = self.d.distance_montee(alt)
        self.tps_mont=self.d_mont*1000/(self.vto)
        #print(f"le temps de montée ", self.tps_mont)
        return self.tps_mont

    def temps_cruise(self,v_vol,alt):
        self.d_desc_sol, self.d_desc= self.d.distance_descente(alt)
        self.tps_cruise=self.d.distance_croisiere(self.d_desc_sol,self.d_montee_sol)*1000/(v_vol)
        #print(self.tps_cruise)
        return self.tps_cruise

    def temps_desc(self):
        self.tps_desc=self.d_desc*1000/(self.v_desc)
        return self.tps_desc

    def temps_total(self, v_vol,alt):
        self.tps_total =  self.temps_mont(alt) + self.temps_cruise(v_vol,alt) + self.temps_desc()
        return self.tps_total
    