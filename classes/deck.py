import numpy as np
import random
from .card import Carte
from .action_card import Action_card
from .path_card import Path_card




class Deck(object):
    """Create the cards of the deck"""
    def __init__(self):
        self.__cartes = []
        self.__cartes.append(Path_card(3))
        self.__cartes.append(Path_card(4))
        for i in range(2):
            self.__cartes.append(Path_card(5))
        for i in range(40):
            self.__cartes.append(Path_card(0))
        for i in range(26):
            actiontyp = np.random.choice(np.array([0,1,2,3,4]))
            if actiontyp == 0:
                self.__cartes.append(Action_card(6))
            else :
                self.__cartes.append(Action_card(1))
        self.__cartes.append(Action_card(2))

    def random_cartes(self):
        """Method that allows you to mix cards"""
        self.__cartes = random.sample(self.__cartes, len(self.__cartes))


    @property
    def cartes(self) : return self.__cartes
