

import pandas as pd

data = pd.read_csv('Base_donnee_avions.csv',index_col=0,delimiter=';',decimal='.',thousands=' ')
data.columns = ['Modele','Constructeur','Type','Conso','s_alaire','envergure','allongement','range','Mach_cruise','Mach_max','WTO','WLA','Wf','We','Poussee']


#Cette classe permet de récupérer les informations de différents avions et de pouvoir les réutiliser par la suite

class Aircraft:
    def __init__(self):
    #Dans cette fonction, on appelle toutes les colonnes de notre fichier, et donc ainsi toutes les valeurs afin de pouvoir les réutiliser
        print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("\nLe but de ce programme est de vous permettre de choisir l'avion que vous souhaitez, puis un aéroport d'arrivée. ")
        print("Suite à cela, nous allons vous proposer deux plans de vols : un avec le trajet le plus rapide pour arriver")
        print("à votre destination et le second avec la consommation la plus minime pour arriver à votre destination.")
        print("\nNous vous indiquerons tout cela à l'aide de deux graphiques, l'un qui vous montre le plan de vol en fonction")
        print("de la distance au sol et l'autre en fonction du temps")

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
        self.Poussee = avion['Poussee'].astype('float').values[0]
    # 'values[0]' nous eprmet de ne ressortir que la valeur de We pour un avion spécifique
    # Nous avons du mettre toutes nos valeurs en types float










