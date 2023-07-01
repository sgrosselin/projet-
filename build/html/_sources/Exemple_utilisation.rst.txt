==================
Exemple d'utilisation
==================

Nous allons vous présenter ici un exemple d'utilisation.

Tout d'abord, l'utilisateur est invité à choisir un avion parmi la base de données suivantes

*Choix avion*
-------------
.. csv-table::
   :file: data/Base_donnee_avions.csv
   :delim: ;

*Choix aéroport de destination*
-------------
.. csv-table::
   :file: data/Base_donnee_aeroports.csv
   :delim: ;

*Résultats du programme*
-------------
Considérons un vol sur Boeing 777 pour un vol CDG-YUL,
Nous obtenons dès lors :

- Distance aéroports : 5541,12 Km
- H_t_min :  5,04 Km (Altitude pour un temps de vol minimal)
- H_c_min : 12,94 km (Altitude pour une consommation minimale)
- Temps de trajet minimal : 6h 6 min
- Temps de trajet pour une consommation minimale : 7 h 49 min
- Consommation minimale de carburant : 85375 lbs

Nous obtenons aussi les courbes suivantes:

.. image:: Images/Affichage_1.png

.. image:: Images/Affichage_3D.png





