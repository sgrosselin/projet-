
class Carburant:
    """
    Représente la classe Carburant

    Attributs:
        - avion (classe) : la classe avion correspondant à l'avion choisit par l'utilisateur
        - temps (classe) : la classe temps crée dans le fichier temps.py
        - vitesse (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
        - consommation (classe) : La classe concommation crée dans le fichier consommation.py

    """

    def __init__(self, avion, temps,vitesse, consommation):
        """ Initialisation de la classe carburant
        Arguments:
        - avion (classe) : la classe avion correspondant à l'avion choisit par l'utilisateur
        - temps (classe) : la classe temps crée dans le fichier temps.py
        - vitesse (classe) : la classe vitesse relative au trajet et à l'avion crée dans le fichier vitesses.py
        - consommation (classe) : La classe concommation crée dans le fichier consommation.py
        """
        self.Avion =avion
        self.t = temps
        self.v = vitesse
        self.c=consommation



    def carburant_consommee_minimal(self):
        """
        Fonction qui calcule la quantité de carburant consommée pendant le vol


        :return:
            int : Quantité de carburant consommée en lb
        """
        Poussee = self.Avion.Poussee
        Dvol = self.t.temps_total(self.c.v_conso, self.v.hcruise)/3600
        Q = self.c.C_min * Poussee * Dvol
        return Q

