import classes.map as sb
import numpy as np

#Creation de 9 cartes chemin
deck=[]
up=0
mi=0
do=0
for i in range(0,3):
    for j in range(0,3):
        pos=sb.Pos(i,j)
        up=0
        mi=0
        do=0

        mi=np.random.choice(np.array([1,2,3,4,5,6,7]))
        
        #Chemin direct vertical
        if mi == 1:
            up=1
            do=1

        #cul de sac haut/bas
        elif mi == 3:
            up=np.random.choice(np.array([0,1]))
            if up == 0:
                do=1
        
        elif mi==6 or mi==7:
            up=np.random.choice(np.array([0,1]))
            if up == 0:
                do=1
            else:
                do=np.random.choice(np.array([0,1]))

        carte=sb.Chemin(pos,0,up,mi,do)
        deck.append(carte)

#affichage des 9 cartes  
for i in range(0,9):
    for j in range(0,3):
        deck[3*(i//3)+j].affiche(i%3)
    print("")



      
    