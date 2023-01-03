import numpy as np
import random
import sys
from .card import Carte



class Hand(object):#0       1       2       3       4       5       6       7       8       9       10
    table_tools=[('   '),(' | '),('-°-'),('| |'),('---'),(' -o'),('\_/'),(' _ '),('|§|'),('o-o'),('   '),('/|\u005C')]
    mat_tools=[[[0,1,1],[7,11,1]],[[2,3,4],[2,8,4]],[[10,6,5],[10,6,9]]]


    def __init__(self, nb_players):
        self.__cards = []
        self.tools = [1,1,1]
        if nb_players <= 5:
            self.__hand_size = 6
        elif nb_players <= 7:
            self.__hand_size = 5
        else:
            self.__hand_size = 4

    #Fonction qui affiche les outils du joueur
    def affiche_tools(self):
        print("")
        for x in range(0,3):
            for i in range(6):
                if x==1 and i%2==0:
                    if i == 0:
                        print("P:  ",end = "")
                    if i == 2:
                        print("L:  ",end = "")
                    if i == 4:
                        print("W:  ",end = "")
                elif i%2==0:
                    print("    ",end = "")
                elif i%2 != 0:
                    if self.tools[(i-1)//2] == 0:
                        print(Hand.table_tools[Hand.mat_tools[(i-1)//2][0][x]],end = "")
                        print("   ",end = "")
                    if self.tools[(i-1)//2] == 1:
                        print(Hand.table_tools[Hand.mat_tools[(i-1)//2][1][x]],end = "")
                        print("   ",end = "")
            print("")
        print("")

    #Fonction qui affiche la main du joueur 
    def affiche(self):
        
        for x in range(0,3):
            for i in range(2*len(self.__cards)):
                if x==1 and i%2==0:
                    print((i//2)+1,end = "")
                    print(": ",end = "")
                elif i%2==0:
                    print("   ",end = "")
                elif i%2 != 0 and x==1:
                    self.__cards[(i-1)//2].affiche(x)
                    print(", ",end = "")
                elif i%2 != 0:
                    self.__cards[(i-1)//2].affiche(x)
                    print("  ",end = "")
            print("")


    
    def add_card(self, card): #ajouter une carte
        if not isinstance ( card , Carte ) :
            print("Erreur: uniquement des cartes peuvent être ajouté à la main d'un joueur")
            sys.exit()
        if len(self.__cards)==self.__hand_size:
            return
        card.face=1
        self.__cards.append(card)

    def remove_card(self, card): #enlever une carte
        if not isinstance ( card , Carte ) :
            print("Erreur: uniquement des cartes peuvent être retiré de la main d'un joueur")
            sys.exit()
        self.__cards.remove(card)
    

    @property
    def hand_size(self):
        return self.__hand_size

    @property
    def cards(self):
        return self.__cards

 