

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('Base_donnee.csv',index_col=0,delimiter=';',decimal=',',thousands=' ')
data.columns = ['Modele','Constructeur','Type','Nbre passager','Nbr equipage','Modele moteur','conso cruise','surface alaire','Alt cruise','Vcruise','Range','Ma Cruise','Wing span','WTO','WLA','Wf','We']


Cd0 = 0.015

class Aircraft:
    def __init__(self):
        self.name = str(input('Entrez le modèle de votre avion : ')) # Surface de l'aire en m^2
        print(self.name)
        
        
    def recherche_avion(self):
         avion = data[data['Modele'] == self.name ]
         print(avion)
         self.constructeur= avion['Constructeur']
         #print(self.constructeur)
         
         return avion
        
        
        
        
        
#        self.S 
#        self.wing_span = wing_span  # Envergure de l'aile en m
#        self.Range = Range
#    
        


