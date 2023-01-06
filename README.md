# ProjetPython
SABOOTERS
Version non terminé de l'interface graphique:
Après avoir récupéré les images des différents types de cartes : j'ai utilisé pygames pour créer  une interface graphique.
Les méthodes du jeu initial dans la console n'étant pas adapté à une interface graphique, l'interface graphique ne permet d'efféctuer qu'un déroulement partiel du jeu.
Elle permet : de lancer le jeu dans une fenêtre, demander le nombre de joueur, et vérifier que c'est bien un nombre entre 3 et 10, entrer les noms des joueurs et les 
enregistrer, lancer une partie avec le nombre de joueurs inscrit au début et leurs noms affichés, poser des cartes n'importe où sur le terrain. Quelques spécificités
sur les actions, pour rentrer un caractère dans une inputbox, il faut cliquer dessus rentrer le nombre et si on veut déclencher l'action suivante appuyer sur entrée. 
Ensuite, pour déplacer une carte lorsqu'on est dans le jeu, on clique uns seule fois sur les cartes du joueurs courant en haut  à gauche (carte cliqué, carte joué, pas 
de retour en arrière) puis sur le terrain. Jouer une carte est actuellement la seule manière de finir un tour, une fois la carte posé sur le terrain, le tour switch
instantanément.
