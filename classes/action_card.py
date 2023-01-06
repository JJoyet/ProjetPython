import numpy as np
import random
import os
from .card import Card
import sys


class Action_card(Card):
    """SABOOTERS action cards
    • Type 1 : action_tools card
    • Type 2 : map card
    • Type 6 : collapse card """

    def __init__(self,typ):
        super().__init__(typ)
        # Appearance is drawn at random from the card according to its type

        if typ == 1:
            # Action_tools card
            self.__vectlook = Card.mataction[np.random.choice(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))]
            self.__vectrecto = Card.matrecto[0]
        elif typ == 2:
            # Map Card
            self.__vectlook = Card.mataction[13]
            self.__vectrecto = Card.matrecto[0]
        elif typ == 6:
            # Crumbling card
            self.__vectlook = Card.mataction[0]
            self.__vectrecto = Card.matrecto[0]
        else:
            print("Error: the value of the card type is incorrect, initialization by default of an action_tools card")
            a=input("press any bouton to continue")
            # Action_tools card
            self.__vectlook = Card.mataction[np.random.choice(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))]
            self.__vectrecto = Card.matrecto[0]
        
    def part_st(self,x):    # The x parameter determines which part of the card is displayed
        """ Method to display a part of the card"""
        # Display the part of the card you want to see
        if self.face == 1:
            if x == 0:
                return Card.tableaction[self.__vectlook[0]]
            elif x == 1:
                return Card.tableaction[self.__vectlook[1]]
            elif x == 2:
                return Card.tableaction[self.__vectlook[2]]
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
        """toString function"""

        st = Card.tableaction[self.__vectlook[0]]+"\n"+Card.tableaction[self.__vectlook[1]]+"\n"+Card.tableaction[self.__vectlook[2]]
        return st

    def __eq__(self,other):

        if not isinstance(other, Action_card):
            return False

        if self is other:
            return True

        # The other attributes are not tested because they do not determine the nature of the card
        if self.typ != other.typ or self.__vectlook != other.vectlook:
            return False

        return True


    @property
    def vectlook(self): return self.__vectlook
    @property
    def vectrecto(self): return self.__vectrecto
        
