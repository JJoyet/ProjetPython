import numpy as np
import random
from .card import Card
from .action_card import Action_card
from .path_card import Path_card




class Deck(object):
    """Create the cards of the deck"""
    def __init__(self):
        self.__cards = []
        self.__cards.append(Path_card(3))
        self.__cards.append(Path_card(4))
        for i in range(2):
            self.__cards.append(Path_card(5))
        for i in range(40):
            self.__cards.append(Path_card(0))
        for i in range(26):
            actiontyp = np.random.choice(np.array([0, 1, 2, 3, 4]))
            if actiontyp == 0:

                self.__cards.append(Action_card(6))
            else:
                self.__cards.append(Action_card(1))
        self.__cards.append(Action_card(2))

    def random_cards(self):
        """Method that allows you to mix cards"""
        self.__cards = random.sample(self.__cards, len(self.__cards))


    @property
    def cards(self) : return self.__cards
