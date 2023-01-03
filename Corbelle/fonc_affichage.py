import classes.map as sb
import numpy as np

#Fonction qui affiche le message de bienvenue
def aff_wel():
    print("+--------------------------------------------------------------------+")
    print("| Welcome to SabOOtters, where dwarf otters look for gold in a mine! |")
    print("+--------------------------------------------------------------------+")


#Fonction qui affiche le plateau de jeu
def affichePlateau(deck):
    #creation du plateau
    plateau=[[sb.Casevide for x in range(9)] for x in range(5)]
    for i in range(0,len(deck)):
        plateau[deck[i].pos[0]][deck[i].pos[1]]=deck[i]
    
    #affiche de la premiere ligne
    for i in range(0,10):
        if i==0 :
            print(" |",end = "")
        else:
            print(" ",i-1," ",end = "")
    print("")

        #affichege de la deuxieme ligne
    for i in range(0,10):
        if i==0 :
            print("-+",end = "")
        else:
            print("-----",end = "")
    print("")

    for i in range(0,len(plateau)):
        for x in range(0,3):
            if x==1:
                print(i,end = "")
                print("|",end = "")
            else:
                print(" |",end = "")
            for j in range(0,len(plateau[0])):
                plateau[i][j].affiche(x)
            print("")

    #affichege de la derniere ligne
    for i in range(0,10):
        if i==0 :
            print("-+",end = "")
        else:
            print("-----",end = "")
    print("")