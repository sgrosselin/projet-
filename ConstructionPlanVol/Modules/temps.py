class Temps:

    def __init__(self,d_mont,d_cruise,d_desc,vto,v_vol,v_desc):
        self.d_mont = d_mont
        self.d_cruise = d_cruise
        self.d_desc = d_desc
        self.vto = vto
        self.v_vol=v_vol
        self.v_desc=v_desc

    def temps_mont(self):
        tps_mont=self.d_mont/self.vto
        return tps_mont

    def temps_cruise(self):
        tps_cruise=self.d_cruise/self.v_vol
        return tps_cruise

    def temps_desc(self):
        tps_desc=self.d_desc/self.v_desc
        return tps_desc

