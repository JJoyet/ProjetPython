import numpy as np
import random
import os
from abc import ABC, abstractmethod


class Card(ABC):
    """SABOOTERS Game Card
    • Type 0 : path card
    • Type 1 : action_tools card
    • Type 2 : map card
    • Type 3 : start card 
    • Type 4 : gold card 
    • Type 5 : stone card
    • Type 6 : collapse card"""

    # Table containing the content of the cards
                #   0          1         2         3         4         5         6         7         8         9         10        11
    tablechemin=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)'),('(-+-)'),('(-S-)'),('($$$)'),('(STO)')]
    tableaction=[('(   )'),('(XXX)'),('(REP)'),('(BRK)'),('( P )'),('( L )'),('( W )'),('( M )'),('(MAP)')]
    tablerecto=[('(   )'),('(+++)'),('(+S+)'),('(END)')]
    
    # Matrices containing vectors to assign an appearance to each type of card
    matchemin=[[[1,1,1],[1,1,1]], #0
               [[0,2,0],[0,2,0]], #1
               [[1,3,0],[0,3,1]], #2 
               [[0,4,0],[0,5,0]], #3
               [[1,8,1],[1,8,1]], #4
               [[1,6,1],[1,7,1]], #5
               [[0,6,1],[1,7,0]], #6
               [[1,6,0],[0,7,1]], #7
               [[1,9,1],[1,9,1]], #8
               [[10,10,10],[10,10,10]], #9
               [[1,11,1],[1,11,1]]] #10

    mataction=[[1,1,1],
               [2,4,0],
               [2,5,0],
               [2,6,0],
               [2,4,5],
               [2,4,6],
               [2,5,6],
               [3,4,0],
               [3,5,0],
               [3,6,0],
               [3,4,5],
               [3,4,6],
               [3,5,6],
               [7,8,4]]

    matrecto=[[1,2,1],[0,3,0]]

    # Matrices containing path vectors assigned to path cards [value indicating the presence of a card, top, left, right, bottom].
    matpath=[[[1,1,0,0,1],[1,1,0,0,1]], #0 
             [[1,0,1,1,0],[1,0,1,1,0]], #1
             [[1,1,0,0,0],[1,0,0,0,1]], #2 
             [[1,0,1,0,0],[1,0,0,1,0]], #3
             [[1,1,1,1,1],[1,1,1,1,1]], #4
             [[1,1,1,0,1],[1,1,0,1,1]], #5
             [[1,0,1,0,1],[1,1,0,1,0]], #6
             [[1,1,1,0,0],[1,0,0,1,1]], #7
             [[1,1,1,1,1],[1,1,1,1,1]], #8
             [[1,1,1,1,1],[1,1,1,1,1]], #9
             [[1,1,1,1,1],[1,1,1,1,1]],]#10

    def __init__(self, typ):
        # Define a position by default
        self.pos = [0, 0]
        # Define the type of card
        self.__typ = typ

        # Define by default that the card is face down
        self.__face = 0

    @abstractmethod
    def part_st(self, x): pass

    @abstractmethod
    def __str__(self): pass

    @property
    def typ(self): return self.__typ

    @property
    def face(self): return self.__face

    @face.setter
    def face(self, face):
        self.__face = 0
        if 0 <= face <= 1:
            self.__face = face
