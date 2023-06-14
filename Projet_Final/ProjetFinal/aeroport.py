
import pandas as pd
from math import sin, cos, acos, radians


data = pd.read_csv('Base_donnee_aeroports.csv' ,index_col=0 ,delimiter=';' ,decimal=',' ,thousands=' ')
#import pdb;pdb.set_trace()
data.columns = ['Latitude (Nord)' ,'Longitude (Est)' ,'Altitude']


class Aeroports:
    def __init__(self):
        self.name = str(input('Entrez le sigle IATA de l\' aéroport d\'arrivée : '))
        aeroport = data.loc[[self.name]]
        self.latitude_arr = aeroport['Latitude (Nord)']
        self.longitude_arr =aeroport['Longitude (Est)']
        self.altitude = aeroport['Altitude']

    def distance_aeroports(self):
        self.aeroport_depart='CDG'
        self.latitude_dep = 49.008014499166165
        self.longitude_dep= 2.550717852775395

        # Altitude + RT en mètres (sphère IAG-GRS80)
        RT = 6378137
        H = 12192
        # angle en radians entre les 2 points
        S = acos(sin(radians(float(self.latitude_dep))) * sin(radians(float(self.latitude_arr))) + cos(radians(float(self.latitude_dep))) * cos(radians(float(self.latitude_arr))) * cos(abs(radians(float(self.longitude_arr)) - radians(float(self.longitude_dep)))))
        # distance entre les 2 points, comptée sur un arc de grand cercle
        dist_aeroports = S * (RT)
        print(dist_aeroports/1000)
        return dist_aeroports

aeroport = Aeroports()
aeroport.distance_aeroports()

