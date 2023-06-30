# projet_final_MGA802

**TITRE : SIMULATION ET OPTIMISATION DE TRAJECTOIRES DE VOL**

**Plan du README :**

I - INTRODUCTION

II - EXPLICATION DU CODE

III - EXEMPLE D'UTILISATION




**I - INTRODUCTION**


Les pilotes d'avions ont de nombreuses tâches à réaliser avant de pouvoir finalement pouvoir embarquer et l'une d'elle se trouve être la création de leur plans de vol.
C'est pourquoi, nous avons décidé de créer un programme qui permet au pilote de les aider à réaliser cette trajectoire de vol. Celle-ci sera apr la suite optimisée, puisque nous proposerons au pilote 2 trajectoires :
- La première sera la trajectoire la plus rapide, en utilisant donc une vitesse maximale pendant la phase de croisière en fonction de l'avion.
- La seconde sera celle qui utilisera le moins de carburant, c'est à dire qui aura une consommation spécifique minimale.

Des courbes lui seront finalement proposées afin de mieux l'aider à visualiser les trajectoires. Il pourra étudier une courbe de l'altitude en fonction du temps et une courbe de l'altitude en fonction de la distance.

Nous avons choisi de fixer l'aéroport de départ. Dans notre code, il s'agit de l'aéroport Paris Charles De Gaulle.
Par la suite, le pilote va pouvoir choisir quel avion il souhaite utiliser, parmis ceux proposés dans notre base de donnée, mais il va aussi pouvoir choisir l'aéroport d'arrivée dans une autre base de donnée.
Ci-dessous, nous allons vous expliquer comment bien utiliser ntore code pour réaliser ce que vous souhaitez.

**II - EXPLICATION DU CODE**

Notre code est composé de 3 modules ainsi que d'un fichier "main.py" qui permet de lancer le programme et d'appeler toutes les classes nécéssaires. Les 3 modules sont les suivants: 
- Donnée de vol 
- Entrée 
- Sortie
Chacun de ses modules contient un fichier "__init__".
Nous allons maintenant vous expliquer ce que chacun de ces modules contient. Tout d'abord, comme son nom l'indique, le module "Entrée" va contenir les différentes classes qui vont permettre à l'utilisateur d'aller récupérer les bases de données.
C'est à dire que nous avons les classes "Aéroport" et "Aircraft" qui appellent chacunes leur base de donnée qui leur est propre. La base de données Aéroport contient 5 choix d'aéroport avec la position de ceux-ci, tandis que la classe Aircraft contient 15 choix d'avions, ainsi que leurs différentes caractéristiques.
Ces 2 classes vont lire les différents fichiers csv et vont attribuer chacune de slignes et des colonnes à des noms que nosu pourront réutiliser dans les différentes classes et fonctions.


Le module "Donnée de vol" va permettre au programme de calculer toutes les valeurs et variables nécéssaires pour obtenir le plan de vol. Il est constitué des classes consommation, carburant, temps, distance et vitesses.
Nous allons expliquer ce que réalise chacunes de ces classes et nous commencons avec la classe vitesse :  
Tout d'abord, la classe vitesse permet de calculer les vitesses des différentes phases de vols, mais aussi de la trajectoire que l'on souhaite optimiser (temps le plus rapide ou consommation minimum).
Elle va prendre en attribut la classe "Aircraft" que nous avons expliqué ci-dessus et elle contient 5 fonctions. La première fonction "calcul_vitesse" va calculer et retourner une liste de vitesses pour la phase de vol de croisière. Cela signifie qu'elle va calculer des vitesses à la fois à Mach maximal et à Mach de croisière. Elle utilisera pour cela une boucle "for" qui va parcourir une liste d'altitude et elle va utiliser 2 formules en focntions de si l'on se trouve en troposphère ou en stratosphère.
- La fonction "valeur_vitesse_max" permet de retourner la valeur maximale dans la liste des vitesses maximales.
- La fonction "vitesse_decrochage" utilise les valeurs retournées dans la classe consommation afin d'obtenir la position dans la liste voulue et de l'utiliser pour retrouver la valeur de température à la même position. On va ainsi calculer la vitesse de décrochage.
- La fonction "vitesse_decollage" permet d'obtenir la vitesse pendant la phase de décollage de l'avion. Pour cela elle utilise la valeur calculée dans la fonction "vitesse_decrochage".
- Finalement, la fonction "vitesse_descente" permet, à l'aide du coefficient de trainée et du coefficient d'oswald, de caculer la vitesse pendant la phase de descente de l'avion.

La classe temps permet de calculer les temps pour les différentes phases de vols. Elle contient 4 fonctions, une pour chaques phase de vol et une qui calcule el temps total. C'est calcul seront réalisés à l'aide de la formule : V= D/T et nous utiliserons les vitesses appropriées et calculées dans la classe précédentes.

La classe distance permet de calculer les distances pour les différentes phases de vols. Elle contient 3 fonctions, une pour chaque phases de vol. Chaque focntions va calculer à la fois la distance aprcourue par l'avion, mais uassi la distance parcourue par rapport au sol.

La classe consommation contient en attribut les classes "Aircraft" et "vitesses" et elel va eprmettre au programme de calculer la consomamtion spécifique de l'avion pendant la phase de croisière. Pour cela, elle va utilsier la formule de breguet ainsi qu ela liste de vitesse à Mach Croisière, retournées dans la classe "vitesse".
Elle va parcourir la liste de vitesse, calculer la consommation spécifique et comparer avec la valeur calculée précédemment pour savoir laquelle est la plus petite. Elle ne va ainsi retenir que la valeur de la consommation spécifique la plus petite. A ce moement là, la fonction va return la valeur de cette consomamtion spécifique, sa position dans la liste ainsi que la valeur de la viesse utilisée pour cette consommation là.

Finalement, la classe carburant permet de calculer le carburant consommé pendant toute la durée du vol.


Le module "sortie" permet à l'utilisateur de pouvoir observer les différentes courbes et trajectoire proposées. De ce fait, il contient les classes affichage_distance, affichage_temps et interface_utilisateur.
La classe interface_utilisateur, peremt d'afficher les différents graphiques ainsi que d'afficher les valeurs du temsp pour les 2 propositions, des altitudes ainsi que des consommations spécifique et de carburants.
Les classes affichage_temps et affichage temps fonctionne de la même façons. Elles permettent de créer et plot les graphiques en fonctions du temps et de la distance. Elles vont pour cela parcourir une boucle while, qui ne s'arrete que lorsque l'avion a atteint l'altitude de l'aéroport d'arrivée. Puis elles vont rencontrer trois possibilités de calcul: soit nous sommes pendant la phase de montée, soit de crosiire, soit de descente. 
Elle va ainsi calculer la pente de la courbe en fonction de ces différentes phases. Puis, la focntion "plan_de_vol" va afficher le graphe qui contient les courbes de consommation minimum et de temps minimum en fonction de la distance et du temps. La focntion "update" va permettre à l'utilisateur de mieux visualiser la vitesse utilisées pendant les phases, car il pourra observer 2 avions parcourir ces différents graphes.


**III - EXEMPLE D'UTILISATION**

Nous allons maintenant réaliser un exemple d'utilisation. Il faut commencer par lancer la fichier "main.py" qui se trouve sur la github. Ce programme va vous demander d'entrer l'avion que vous souhaitez. Vous pouvez aller observer la base de données proposées ou entrer un de ces avions ci-dessous :

A321

B737

A320neo

A321neoXLR

A320

A220

A330

A350-900

A350-1000

ACJ220

B777

ACJ319neo

ACJ320neo

ACJ330

B747

Une fois l'avion choisi, le programme va vous demander d'entrer l'aéroport de destination voulu. Vous pouvez chosir parmis les sigles de ces aéroports: 

JFK

YUL

LIS

CAI

HEL

Le programme va ainsi vous afficher les propositions de plan de vols en fonction de l'avion et de l'aéroport d'arrivée choisi. Il vous indiquera aussi le temps que vous allez mettre et la consommation de votre avion pendant ce vol.
 Ainsi, si vous choississez l'avion "B777" et l'aéroport d'arrivée "YUL", vous obtiendrez une trajectoire de vol pour un temps minimal de 6 h 6 min à une altitude de 5.04 km ainsi qu'une trajectoire de vol pour une consommation minimale de 7 h 49 min , à une altitude de 12.94 km pour une consommation de 85375 lbs.
 







