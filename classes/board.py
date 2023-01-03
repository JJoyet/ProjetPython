import numpy as np
import random
import os
import sys
from .card import Carte
from .path_card import Path_card

class Plateau(object):
    """Plateau du jeu SABOOTERS"""
    def __init__(self):
        #tableau binaire qui determine si une carte a ete posee et contien le chemin de la mine
        self.__pathmap=np.ones((30,30,5),int)
        for pathmap_i in self.__pathmap:
            for pathmap_ij in pathmap_i:
                pathmap_ij[0]=0

        #liste composé des cartes présent sur le plateau
        self.__cartes_posees=[]

        #Tableau des dimensions du plateau que l'on affiche, permet de rendre le plateau dynamique
        self.__dimensions=[[0,0],[0,0]]

        #attribut qui permet de garder en memoire la position de la carte gold
        self.__pos_gold=[]

        #attribut qui permet de garder en memoire la position de la carte start
        self.__pos_start=[]

        #attribut qui permet de garder en memoire les positions des cartes pierres
        self.__pos_stone=[]

        #attribut qui permet de determiner si la carte gold a été trouvé 
        self.__gold_found=0

        #Variable qui permet d'afficher à quelle manche le jeu est
        self.no_manche=0 #L'attribut est publique car il doit pouvoir être modifié depuis l'extérieur 

#Méthode qui permet d'ajouter une carte sur le plateau, on met en parametre la carte et la position à laquelle on souhaite poser le carte
    def add_carte(self,carte,pos,init_game=0): #Le paramètre init_game permet de dire si on initialise la partie
        #On verifie si la carte posée est bien une carte
        if not isinstance ( carte , Path_card ) :
            print("Erreur: uniquement des cartes peuvent être posee sur le plateau")
            sys.exit()

        #On limite la zone où la carte peut être posée
        if pos[0]<-10 or pos[0]>10 or pos[1]<-10 or pos[1]>10:
            print("Erreur: La position de la carte va au dela de la taille maximale du plateau")
            sys.exit()

        #On verifie si il y a déja une carte positionné à l'endroit désiré
        if self.__pathmap[pos[0]+15][pos[1]+15][0]==1 :
            print("Erreur: une carte est déja positionnée à l'emplacement désiré")
            sys.exit()

        #On verifie si la valeur entrée pour init_game est correct
        if init_game!=0 and init_game!=1:
            print("Erreur: valeur incorrecte entrée pour init_game")
            sys.exit()

        #Les cartes d'arrivée sont placée face cachée
        if carte.typ != 4 and carte.typ != 5:
            carte.face=1
        else:
            carte.face=0

        #Le plateau garde en mémoire la position de la carte gold
        if carte.typ == 4 :
            self.__pos_gold=pos
        
        #Le plateau garde en memoire la position des cartes stone
        if carte.typ == 5 :
            self.__pos_stone.append(pos)

        #Le plateau garde en memoire la position de la carte start
        if carte.typ == 3 :
            self.__pos_start=pos

        #On modifie la position de la carte
        carte.pos=pos

        #On ajoute la carte aux cartes du plateau
        self.__cartes_posees.append(carte)

        #On réajuste la dimention du plateau par rapport à la position de la nouvelle carte posée
        if pos[0] < self.__dimensions[0][0]:
            self.__dimensions[0][0]=pos[0]

        if pos[0]+1 > self.__dimensions[0][1]:
            self.__dimensions[0][1]=pos[0]+1

        if pos[1] < self.__dimensions[1][0]:
            self.__dimensions[1][0]=pos[1]

        if pos[1]+1 > self.__dimensions[1][1]:
            self.__dimensions[1][1]=pos[1]+1

        #On indique qu'une carte est posée à la position de la carte
        self.__pathmap[carte.pos[0]+15][carte.pos[1]+15]=carte.path

        if init_game==0:
            #On verifie si la carte a été posé à coté d'une carte END
            if ((pos[0]==self.__pos_gold[0]+1 or pos[0]==self.__pos_gold[0]-1) and pos[1]==self.__pos_gold[1]) or ((pos[1]==self.__pos_gold[1]+1 or pos[1]==self.__pos_gold[1]-1) and pos[0]==self.__pos_gold[0]):
                for i in range(len(self.__cartes_posees)):
                    if self.__cartes_posees[i].pos==self.__pos_gold:
                        self.__cartes_posees[i].face=1
                        self.__gold_found=1
                        
            #On verifie si la carte a été posé à coté d'une carte pierre
            for pos_stone in self.__pos_stone:
                if ((pos[0]==pos_stone[0]+1 or pos[0]==pos_stone[0]-1) and pos[1]==pos_stone[1]) or ((pos[1]==pos_stone[1]+1 or pos[1]==pos_stone[1]-1) and pos[0]==pos_stone[0]):
                    for carte in self.__cartes_posees:
                        if carte.pos==pos_stone:
                            carte.face=1

#Methode qui permet de créer un éboulement
    def collapse(self,pos):
        etat=False
        for carte in self.__cartes_posees:
            #On cherche parmis les cartes posée si il y en a une qui correspond à la position de l'éboulemetn et si elle ne correspond pas à une carte départ ou arrivée
            if carte.pos==pos and carte.typ != 3 and carte.typ != 4 and carte.typ != 5:
                etat=True
                self.__cartes_posees.remove(carte)
                break
        if etat==True:
            self.__pathmap[pos[0]][pos[1]]=[0,1,1,1]
        #La methode retourne un booléen qui indique si l'opération est un succès
        return etat

    #Fonction qui réinitialise le plateau
    def reset_plateau(self):
        self.__pathmap=np.ones((30,30,5),int)
        for pathmap_i in self.__pathmap:
            for pathmap_ij in pathmap_i:
                pathmap_ij[0]=0
        self.__cartes_posees=[]
        self.__dimensions=[[0,0],[0,0]]
        self.__pos_gold=[]
        self.__pos_stone=[]
        self.__gold_found = 0

    #Fonction ToString
    def __str__(self):
        st=""
        #Fonction qui affiche le plateau de jeu 
        #affichage de la première ligne
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                st+="  |"
            else:
                #On gére le cas où le numéro de colonne comporte 2 caractères
                if (j-1)<0 or (j-1)>=10:
                    st+=f" {j-1}  "
                else:
                    st+=f"  {j-1}  "
        st+="|"+"\n"

        #affichage de la deuxieme ligne, partie supérieur du cadre
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                st+="--+"
            else:
                st+="-----"
        st+="+--"+"\n"

        for i in range(self.__dimensions[0][0],self.__dimensions[0][1]):
            for x in range(0,3):
                if x==1:
                    #On gére le cas où le numéro de ligne comporte 2 caractères
                    if i<0 or i>=10:
                        st+=f"{i}|"
                    else:
                        st+=f" {i}|"
                else:
                    st+="  |"
                for j in range(self.__dimensions[1][0],self.__dimensions[1][1]):
                    if self.__pathmap[i+15][j+15][0]==0:
                        st+="     "
                    else:
                        for k in range(len(self.__cartes_posees)):
                            if self.__cartes_posees[k].pos == [i,j]:
                                st+=self.__cartes_posees[k].part_st(x)
                st+="|"+"\n"

        #affichage de la derniere ligne, partie inférieur du cadre
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                st+="--+"
            else:
               st+="-----"
        st+="+--"+"\n"
        return st

    #Fonction qui affiche le plateau
    def affiche(self):
        #Fonction qui affiche le plateau de jeu 
        #affichage de la première ligne
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                print("  |",end = "")
            else:
                #On gére le cas où le numéro de colonne comporte 2 caractères
                if (j-1)<0 or (j-1)>=10:
                    print(f" {j-1}  ",end = "")
                else:
                    print(f"  {j-1}  ",end = "")
        print("|")

        #affichage de la deuxieme ligne, partie supérieur du cadre
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                print("--+",end = "")
            else:
                print("-----",end = "")
        print("+--")

        for i in range(self.__dimensions[0][0],self.__dimensions[0][1]):
            for x in range(0,3):
                if x==1:
                    #On gére le cas où le numéro de ligne comporte 2 caractères
                    if i<0 or i>=10:
                        print(i,end = "|")
                    else:
                        print(f" {i}",end = "|")
                else:
                    print("  |",end = "")
                for j in range(self.__dimensions[1][0],self.__dimensions[1][1]):
                    if self.__pathmap[i+15][j+15][0]==0:
                        print("     ",end = "")
                    else:
                        for k in range(len(self.__cartes_posees)):
                            if self.__cartes_posees[k].pos == [i,j]:
                                self.__cartes_posees[k].affiche(x)
                print("|")

        #affichage de la derniere ligne, partie inférieur du cadre
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                print("--+",end = "")
            else:
               print("-----",end = "")
        print("+--")

    @property
    def cartes_posees(self) : return self.__cartes_posees

    @property
    def pathmap(self) : return self.__pathmap

    @property
    def gold_found(self) : return self.__gold_found

    @property
    def pos_gold(self) : return self.__pos_gold

