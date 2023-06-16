class Temps:

    def __init__(self,d_mont,d_cruise,d_desc,vto,v_vol):
        self.d_mont = d_mont
        self.d_cruise = d_cruise
        self.d_desc = d_desc
        self.vto = vto
        self.v_vol=v_vol

    def temps_mont(self):
        tps_mont=self.d_mont/self.vto
        return tps_mont

    def temps_cruise(self):
        tps_cruise=self.d_cruise/self.v_vol
        return tps_cruise

    def temps_desc(self, gamma_des):
