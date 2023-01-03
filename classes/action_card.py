import numpy as np
import random
import os
from .card import Carte
import sys


class Action_card(Carte):
    """Cartes action du jeu SABOOTERS
    • Type 1 : Carte action
    • Type 2 : Carte map
    • Type 6 : Carte éboulement """

    def __init__(self,typ):
        super().__init__(typ)

        #On tire au hasard une apparence a la carte selon son type
        if typ == 1 :
            #Carte action_tools
            self.__vectapparence=Carte.mataction[np.random.choice(np.array([1,2,3,4,5,6,7,8,9,10,11,12]))]
            self.__vectrecto=Carte.matrecto[0]
        elif typ == 2:
            #Carte map
            self.__vectapparence=Carte.mataction[13]
            self.__vectrecto=Carte.matrecto[0]
        elif typ == 6:
            #Carte éboulement
            self.__vectapparence=Carte.mataction[0]
            self.__vectrecto=Carte.matrecto[0]
        else:
            print("Erreur: la valeur du type de carte est incorrecte, initialisation par default d'une carte action_tools")
            a=input("press any bouton to continue")
            #Carte action_tools
            self.__vectapparence=Carte.mataction[np.random.choice(np.array([1,2,3,4,5,6,7,8,9,10,11,12]))]
            self.__vectrecto=Carte.matrecto[0]
        
    #Methode qui permet d'afficher une partie de la carte
    def part_st(self,x): #Le parametre x détermine quel partie de la carte on affiche
        #On affiche la partie de la carte que l'on souhaite afficher
        if self.face==1:
            if x==0:
                return Carte.tableaction[self.__vectapparence[0]]
            elif x==1:
                return Carte.tableaction[self.__vectapparence[1]]
            elif x==2:
                return Carte.tableaction[self.__vectapparence[2]]
            else:
                print("Erreur: la valeur d'affichage de la carte est incorrecte, veuilliez choisir une valeur entre 0 et 2")
                sys.exit()
        if self.face==0:
            if x==0:
                return Carte.tablerecto[self.__vectrecto[0]]
            elif x==1:
                return Carte.tablerecto[self.__vectrecto[1]]
            elif x==2:
                return Carte.tablerecto[self.__vectrecto[2]]
            else:
                print("Erreur: la valeur d'affichage de la carte est incorrecte, veuilliez choisir une valeur entre 0 et 2")
                sys.exit()

    #Methode qui permet d'afficher une partie de la carte
    def affiche(self,x): #Le parametre x détermine quel partie de la carte on affiche
        #On affiche la partie de la carte que l'on souhaite afficher
        if self.face==1:
            if x==0:
                print(Carte.tableaction[self.__vectapparence[0]],end = "")
            elif x==1:
                print(Carte.tableaction[self.__vectapparence[1]],end = "")
            elif x==2:
                print(Carte.tableaction[self.__vectapparence[2]],end = "")
            else:
                print("Erreur: la valeur d'affichage de la carte est incorrecte, veuilliez choisir une valeur entre 0 et 2")
                sys.exit()
        if self.face==0:
            if x==0:
                print(Carte.tablerecto[self.__vectrecto[0]],end = "")
            elif x==1:
                print(Carte.tablerecto[self.__vectrecto[1]],end = "")
            elif x==2:
                print(Carte.tablerecto[self.__vectrecto[2]],end = "")
            else:
                print("Erreur: la valeur d'affichage de la carte est incorrecte, veuilliez choisir une valeur entre 0 et 2")
                sys.exit()

    #Fonction tostring
    def __str__(self):
        st=Carte.tableaction[self.__vectapparence[0]]+"\n"+Carte.tableaction[self.__vectapparence[1]]+"\n"+Carte.tableaction[self.__vectapparence[2]]
        return st

    #Fonction de comparaison
    def __eq__(self,other):

        if not isinstance ( other , Action_card ) :
            return False

        if ( self is other ) :
            return True

        if self.typ != other.typ or self.__vectapparence != other.vectapparence: #Les autres attributs ne sont pas testé car non déterminant sur la nature de la carte
            return False

        return True


    @property
    def vectapparence(self) : return self.__vectapparence
    @property
    def vectrecto(self) : return self.__vectrecto
        
