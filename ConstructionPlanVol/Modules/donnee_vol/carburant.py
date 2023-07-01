
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




    def carburant_conso_min (self,v):
        """
        Fonction qui calcule la quantité de carburant consommée pour un vol avec une consommation de carburant minimale


        :return:
            int : Quantité de carburant consommée en lb
        """       
        poussee = self.Avion.Poussee
        conso_min = self.c.consommation_cruise_min()
        conso_montee= self.c.consommation_mont(v)
        self.liste_v_max, self.liste_v_conso , T= self.v.calcul_vitesse()
        tps_mont=self.t.temps_mont(self.liste_v_conso)
        c=[]  
        for k in range (len(self.c.v_cruise)) :
                              
            c.append(conso_min[k]*(self.t.temps_cruise(self.c.v_cruise[k],self.v.altitude[k])/3600) + conso_montee[k] *(tps_mont[k]/3600))
            
        c_min = min(c)
        
        for i in range(len(c)) :
            if c[i] == c_min :
                i_minim=i  
                H_conso = self.v.altitude[i_minim]
                v_conso = self.c.v_cruise[i_minim]
                self.Q_min=c_min*poussee
           
        return self.Q_min, i_minim , H_conso, v_conso
            
            
            
    def carburant_temps_min (self):
        """
        Fonction qui calcule la quantité de carburant consommée pour un vol avec un temps de trajet minimun


        :return:
            int : Quantité de carburant consommée en lb
        """  
        conso_max = self.c.consommation_cruise_max()
        conso_montee= self.c.consommation_mont(self.liste_v_max)
        i,H,v_max =self.v.valeur_vitesse_max()           
        tps_mont =self.t.temps_mont(self.liste_v_max)   
        poussee = self.Avion.Poussee
     
        Q_max = (conso_max[i]*(self.t.temps_cruise(v_max,H)/3600)+ conso_montee[i]* (tps_mont[i]/3600))*poussee
        return Q_max    
    
    
    