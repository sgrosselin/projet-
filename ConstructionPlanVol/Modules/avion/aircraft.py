

import pandas as pd

data = pd.read_csv('Base_donnee_avions.csv',index_col=0,delimiter=';',decimal='.',thousands=' ')
data.columns = ['Modele','Constructeur','Type','Conso','s_alaire','envergure','allongement','range','Mach_cruise','Mach_max','WTO','WLA','Wf','We']



class Aircraft:
    def __init__(self):
        self.name = str(input('Entrez le modèle de votre avion : ')) # Surface de l'aire en m^2
        avion = data[data['Modele'] == self.name ]         
        self.constructeur = avion['Constructeur'].values[0]
        self.type=avion['Type'].values[0]
        self.conso_cruise = avion['Conso'].astype('float').values[0]
        self.s_alaire = avion['s_alaire'].astype('float').values[0]
        self.envergure = avion['envergure'].astype('float').values[0]
        self.allongement = avion['allongement'].astype('float').values[0]
        self.range = avion ['range'].astype('float').values[0]
        self.M_cruise = avion ['Mach_cruise'].astype('float').values[0]
        self.M_max = avion ['Mach_max'].astype('float').values[0]
        self.Wto = avion ['WTO'].astype('float').values[0]
        self.Wla = avion ['WLA'].astype('float').values[0]
        self.Wf = avion ['Wf'].astype('float').values[0]
        self.We = avion ['We'].astype('float').values[0]
  
        
        


        



