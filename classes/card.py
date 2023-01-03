import numpy as np
import random
import os
from abc import ABC , abstractmethod

class Carte(ABC):
    """Carte du jeu SABOOTERS
    • Type 0 : Carte chemin
    • Type 1 : Carte action
    • Type 2 : Carte map
    • Type 3 : Carte start
    • Type 4 : Carte gold
    • Type 5 : Carte pierre 
    • Type 6 : Carte éboulement """
    #Tables contenant le contenu des cartes
                #   0          1         2         3         4         5         6         7         8         9         10        11
    tablechemin=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)'),('(-+-)'),('(-S-)'),('($$$)'),('(-N-)')]
    tableaction=[('(   )'),('(XXX)'),('(REP)'),('(BRK)'),('( P )'),('( L )'),('( W )'),('( M )'),('(MAP)')]
    tablerecto=[('(   )'),('(+++)'),('(+S+)'),('(END)')]
    
    #Matrices contenant contenant les vecteurs permettant d'atribuer une apparence a chaques types de cartes
                #0        1       2       3       4       5       6       7       8       9       10      11      12      13      14       15        16         
    matchemin=[[1,1,1],[0,2,0],[1,3,0],[0,3,1],[0,4,0],[0,5,0],[1,8,1],[1,6,1],[0,6,1],[1,6,0],[1,7,1],[0,7,1],[1,7,0],[1,8,1],[1,9,1],[10,10,10],[1,11,1]]
    mataction=[[1,1,1],[2,4,0],[2,5,0],[2,6,0],[2,4,5],[2,4,6],[2,5,6],[3,4,0],[3,5,0],[3,6,0],[3,4,5],[3,4,6],[3,5,6],[7,8,4]]
    matrecto=[[1,2,1],[0,3,0]]

    #Matrices contenant les vecteurs de chemin attribué aux cartes chemin [valeur indiquant la présence d'une carte, haut, gauche, droite, bas]
                # 0           1           2            3          4           5           6           7           8           9           10          11          12          13          14          15          16
    matpath=[[1,1,0,0,1],[1,0,1,1,0],[1,1,0,0,0],[1,0,0,0,1],[1,0,1,0,0],[1,0,0,1,0],[1,1,1,1,1],[1,1,1,0,1],[1,0,1,0,1],[1,1,1,0,0],[1,1,0,1,1],[1,0,0,1,1],[1,1,0,1,0],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

    def __init__(self,typ):
        #On defini une position par default 
        self.pos = [0,0] #La position de la carte n'est pas un attribut privé car une carte peut se trouvé à priori n'importe où

        #On defini le type de carte
        self.__typ=typ

        #On defini par default que le carte est face cachee
        self.face=0 #La face détermine si la carte est posé coté recto ou verso, cet attribut est privé car on souhaite controler sa modification

    @abstractmethod
    def affiche(self,x): pass

    @abstractmethod
    def part_st(self,x): pass

    @property
    def typ(self) : return self.__typ
    @property
    def face(self) : return self.__face

    @face.setter
    def face(self,face):
        self.__face=0
        if face>=0 and face<=1:
            self.__face=face


