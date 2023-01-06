import numpy as np
import random
from abc import ABC, abstractmethod
import os
from .hand import Hand
from .card import Carte
from .board import Plateau
import sys



class Player(ABC):
    def __init__(self,name, role, nb_players):
        self.__name = name
        self.__role = role    # the role is of the class menu.character[i]
        self.__hand = Hand(nb_players)   # to display the hand: player.hand.display_hand()
    def piocher_carte(self, pioche):
        """Method that allows the player to draw a card"""
        if len(pioche) <= 0:
            print("Error: the deck is empty")
            sys.exit()
        
        self.__hand.add_card(pioche[0])
        pioche.remove(pioche[0])

    def defausse_carte(self, card, defausse):
        """Method to remove a card from the player"""
        defausse.append(card)
        self.__hand.remove_card(card)

    # Abstract method that allows a human or an AI to play during a round
    @abstractmethod
    def tourjoueur(self, plateau, pioche, defausse): pass


    @property
    def name(self):
        return self.__name

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self,role):
        if role == "S":
            self.__role = role
        # Define by default "C" as a role
        else:
            self.__role = "C"


    @property
    def hand(self):
        return self.__hand

    # @hand.setter
    # def hand(self,hand):
    #     self.__hand=hand




"""
• à 3 joueurs : 1 Saboteur et 3 Chercheurs
• à 4 joueurs : 1 Saboteur et 4 Chercheurs
• à 5 joueurs : 2 Saboteurs et 4 Chercheurs
• à 6 joueurs : 2 Saboteurs et 5 Chercheurs
• à 7 joueurs : 3 Saboteurs et 5 Chercheurs
• à 8 joueurs : 3 Saboteurs et 6 Chercheurs
• à 9 joueurs : 3 Saboteurs et 7 Chercheurs
• à 10 joueurs : toutes les cartes Rôle (4 Saboteurs et 7 Chercheurs)
"""
