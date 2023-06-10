

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('Base_donnee.csv',index_col=0,delimiter=';',decimal=',',thousands=' ')
data.columns = ['Modele','Constructeur','Type','Nbre passager','Nbre equipage','Modele moteur','conso cruise','surface alaire','Alt cruise','Vcruise','Range','Ma cruise','Wing span','WTO','WLA','Wf','We']


Cd0 = 0.015

class Aircraft:
    def __init__(self):
        self.name = str(input('Entrez le modèle de votre avion : ')) # Surface de l'aire en m^2
        avion = data[data['Modele'] == self.name ]         
        self.constructeur = avion['Constructeur']
        self.type=avion['Type']
        self.passager:avion['Nbre passager']
        self.equipage= avion['Nbre equipage']
        self.moteur = avion['Modele moteur']
        self.conso_cruise = avion['conso cruise']
        self.surface_alaire = avion['surface alaire']
        self.alt_cruise = avion['Alt cruise']
        self.v_cruise = avion['Vcruise']
        self.range = avion ['Range']
        self.mach_cruise = avion ['Ma cruise']
        self.envergure = avion ['Wing span']
        self.wto = avion ['WTO']
        self.wla = avion ['WLA']
        self.wf = avion ['Wf']
        self.we = avion ['We']
        print(self.we)


#        
#    def recherche_avion(self):
#         avion = data[data['Modele'] == self.name ]
#         
#         self.constructeur = avion['Constructeur']
#         print(self.constructeur)
#         
#         return avion
        
        
        
avion=Aircraft()
#avion.recherche_avion()      
        
#        self.S 
#        self.wing_span = wing_span  # Envergure de l'aile en m
#        self.Range = Range
#    
        


