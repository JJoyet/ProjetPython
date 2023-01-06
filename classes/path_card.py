import numpy as np
import random
import os
from .card import Card
import sys


class Path_card(Card):
    """SABOOTERS Path cards
    • Type 0 : path card
    • Type 3 : start card 
    • Type 4 : gold card 
    • Type 5 : stone card """

    def __init__(self, typ):
        super().__init__(typ)

        #We define a default direction for the card
        self.__direction=0 #The attribute is private because we want to control its modification

        # Appearance is randomly drawn on the card according to its type
        if typ == 0:  # Path card
            chemin = np.random.choice(np.array([0, 1, 2, 3, 4, 5, 6, 7]))
            self.__vectlook = Card.matchemin[chemin]
            self.__vectrecto = Card.matrecto[0]
            self.__path = Card.matpath[chemin]
        elif typ == 3:
            # start card
            self.__vectlook = Card.matchemin[8]
            self.__vectrecto = Card.matrecto[0]
            self.__path = Card.matpath[8]
        elif typ == 4:
            # Gold card
            self.__vectlook = Card.matchemin[9]
            self.__vectrecto = Card.matrecto[1]
            self.__path = Card.matpath[9]
        elif typ == 5:
            # Stone card
            self.__vectlook = Card.matchemin[10]
            self.__vectrecto = Card.matrecto[1]
            self.__path = Card.matpath[10]
        else:
            print("Error: the value of the card type is incorrect, initialization by default of a path card")
            a = input("press any bouton to continue")
            # Path card
            chemin = np.random.choice(np.array([0, 1, 2, 3, 4, 5, 6, 7]))
            self.__vectlook = Card.matchemin[chemin]
            self.__vectrecto = Card.matrecto[0]
            self.__path = Card.matpath[chemin]

    def part_st(self, x):
        """Method to display a part of the map"""
        # Display the part of the map you want to see
        if self.face == 1:
            if x == 0:
                return Card.tablechemin[self.__vectlook[self.__direction][0]]
            elif x == 1:
                return Card.tablechemin[self.__vectlook[self.__direction][1]]
            elif x == 2:
                return Card.tablechemin[self.__vectlook[self.__direction][2]]
            else:
                print("Error: the display value of the card is incorrect, please choose a value between 0 and 2")
                sys.exit()

        if self.face == 0:
            if x == 0:
                return Card.tablerecto[self.__vectrecto[0]]
            elif x == 1:
                return Card.tablerecto[self.__vectrecto[1]]
            elif x == 2:
                return Card.tablerecto[self.__vectrecto[2]]
            else:
                print("Error: the display value of the card is incorrect, please choose a value between 0 and 2")
                sys.exit()

    def __str__(self):
        """Function toString"""
        st = Card.tablechemin[self.__vectlook[self.__direction][0]] + "\n" + Card.tablechemin[self.__vectlook[self.__direction][1]] + "\n" + \
             Card.tablechemin[self.__vectlook[self.__direction][2]]
        return st

    # Equals
    def __eq__(self, other):

        if not isinstance(other, Path_card):
            return False

        if self is other:
            return True

        if self.typ != other.typ or self.__vectlook != other.vectlook:
            # The other attributes are not tested because they do not determine the nature of the card
            return False

        return True

    @property
    def vectlook(self):
        return self.__vectlook

    @property
    def direction(self) : return self.__direction
    
    @direction.setter
    def direction(self,direction):
        if direction == 1:
            self.__direction=direction
        #We define a default direction for the card
        else:
            self.__direction=0

    @property
    def vectrecto(self):
        return self.__vectrecto

    @property
    def path(self):
        return self.__path
