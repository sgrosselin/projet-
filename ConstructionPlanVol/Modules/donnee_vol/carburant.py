
class Carburant:
    def __init__(self, avion, temps,vitesse, consommation):
        self.Avion =avion
        self.t = temps
        self.v = vitesse
        self.c=consommation



    def carburant_consommee_minimal(self):
        Poussee = self.Avion.Poussee
        Dvol = self.t.temps_total(self.c.v_conso, self.v.hcruise)/3600
        Q = self.c.C_min * Poussee * Dvol
        return Q

