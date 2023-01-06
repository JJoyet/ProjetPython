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

    def __str__(self):
        """ Function ToString that displays the player's hand """
        st = ""
        for x in range(0,3):
            for i in range(2*len(self.__cards)):
                if x == 1 and i % 2 == 0:
                    st += f"{(i//2)+1}: "
                elif i % 2 == 0:
                    st += "   "
                elif i % 2 != 0 and x == 1:
                    st += self.__cards[(i-1)//2].part_st(x)+", "
                elif i % 2 != 0:
                    st += self.__cards[(i-1)//2].part_st(x)+"  "
            st += "\n"
        return st

    def affiche_tools(self):
        """Function that displays the player's tools"""
        print("")
        for x in range(0, 3):
            for i in range(6):
                if x == 1 and i % 2 == 0:
                    if i == 0:
                        print("P:  ", end="")
                    if i == 2:
                        print("L:  ", end="")
                    if i == 4:
                        print("W:  ", end="")
                elif i % 2 == 0:
                    print("    ", end="")
                elif i % 2 != 0:
                    if self.tools[(i-1)//2] == 0:
                        print(Hand.table_tools[Hand.mat_tools[(i-1)//2][0][x]], end="")
                        print("   ", end="")
                    if self.tools[(i-1)//2] == 1:
                        print(Hand.table_tools[Hand.mat_tools[(i-1)//2][1][x]], end="")
                        print("   ", end="")
            print("")
        print("")
    
    def add_card(self, card):
        """Method for adding a map"""
        if not isinstance(card, Carte):
            print("Error: only cards can be added to a player's hand")
            sys.exit()
        if len(self.__cards)==self.__hand_size:
            return
        card.face = 1
        self.__cards.append(card)

    def remove_card(self, card):
        """Method to remove a card"""
        if not isinstance(card, Carte):
            print("Error: only cards can be removed from a player's hand")
            sys.exit()
        self.__cards.remove(card)
    

    @property
    def hand_size(self):
        return self.__hand_size

    @property
    def cards(self):
        return self.__cards

 