class Temps:

    def __init__(self,dist,vto,v_desc):
        self.d=dist
        self.vto = vto
        self.v_desc=v_desc

    def temps_mont(self,v_vol):
        self.d_montee_sol, self.d_mont = self.d.distance_montee()
        self.tps_mont=self.d_mont/(v_vol*1000)
        print(f"le temps de montée ", self.tps_mont)
        return self.tps_mont

    def temps_cruise(self,v_vol):
        self.d_desc_sol, self.d_desc= self.d.distance_descente()
        self.tps_cruise=self.d.distance_croisiere(self.d_desc,self.d_mont)/(v_vol*1000)
        return self.tps_cruise

    def temps_desc(self):
        self.tps_desc=self.d_desc/(self.v_desc*1000)
        return self.tps_desc

    def temps_total(self, v_vol):
        self.tps_total = self.temps_desc() + self.temps_mont(v_vol) + self.temps_cruise(v_vol)
        return self.tps_total
    