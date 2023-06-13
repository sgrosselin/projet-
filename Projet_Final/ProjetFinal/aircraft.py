

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('Base_donnee_avions.csv',index_col=0,delimiter=';',decimal=',',thousands=' ')
data.columns = ['Modele','Constructeur','Type','Conso','s_alaire','envergure','allongement','range','Mach_cruise','Mach_max','WTO','WLA','Wf','We']


Cd0 = 0.015

class Aircraft:
    def __init__(self):
        self.name = str(input('Entrez le modèle de votre avion : ')) # Surface de l'aire en m^2
        avion = data[data['Modele'] == self.name ]         
        self.constructeur = avion['Constructeur']
        self.type=avion['Type']
        self.conso_cruise = avion['Conso']
        self.s_alaire = avion['s_alaire']
        self.envergure = avion['envergure']
        self.allongement = avion['allongement']
        self.range = avion ['range']
        self.M_cruise = avion ['Mach_cruise']
        self.M_max = avion ['Mach_max']
        self.wto = avion ['WTO']
        self.wla = avion ['WLA']
        self.wf = avion ['Wf']
        self.we = avion ['We']
        


        
        
avion=Aircraft()


