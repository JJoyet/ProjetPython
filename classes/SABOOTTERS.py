import numpy as np
import random

from .deck import Deck
from .menu import Menu
from .player import Player
from .hand import Hand
from .card import Carte
from .board import Plateau
from .human import Human


class SABOOTERS(object):
    """Class containing the whole game"""
    def __init__(self):
        self.__menu = Menu()
        self.__deck = Deck()
        self.__pioche = []
        self.__defausse = []
        self.__joueurs = []
        self.__plateau = Plateau()

    def __initpartie(self):
        """ Initialization of a game"""

        self.__menu.start_game()
        for i in range(0, self.__menu.number):
            self.__joueurs.append(Human(self.__menu.players_name[i], self.__menu.roles[i], self.__menu.number))

    def __initmanche(self):
        """Initialization of a round"""
        self.__menu.change_role()
        i = 0
        for joueur in self.__joueurs:
            joueur.role = self.__menu.roles[i]
            i += 1

        self.__deck.random_cartes()     # Shuffle the cards

        set_pos_gold = random.sample([[0, 2], [2, 2], [4, 2]], 3)   # Define the positions of the "END" cards

        # Card distribution
        k = 0
        for carte in self.__deck.cartes:
            # Place the arrival/departure cards on the board
            if carte.typ == 3 or carte.typ == 4 or carte.typ == 5:
                if carte.typ == 3:
                    self.__plateau.add_carte(carte, [2, 0], 1)
                else:
                    self.__plateau.add_carte(carte, set_pos_gold[k], 1)
                    k = k + 1
            # Create the deck with the action and path cards
            else:
                self.__pioche.append(carte)
        print(len(self.__pioche))
        # Players draw their cards
        for i in range(self.__menu.number):
            for j in range(self.__joueurs[i].hand.hand_size):
                self.__joueurs[i].piocher_carte(self.__pioche)

    def __manche(self):
        """How a round unfolds"""

        # Initialization of a game
        self.__initmanche()

        # Variable to determine if players have any cards left in their hand
        nb_card_player = 0

        # Variable to determine if gold has been found
        gold_found = 0

        # Card counter
        nb_card_player = 1

        state = 0
        # As long as gold is not found and there are still cards in hand
        while nb_card_player != 0 and gold_found == 0:
            nb_card_player = 0
            # Variable to know who to play
            current_indice = 0
            for joueur in self.__joueurs:
                joueur.tourjoueur(self.__plateau, self.__pioche, self.__defausse, self.__joueurs)
                nb_card_player = nb_card_player + len(joueur.hand.cards)
                gold_found = self.__plateau.gold_found
                # If gold has been found it is the end of the round, the diggers win
                if gold_found == 1:
                    state = 2
                    self.__menu.fin_de_manche(state, current_indice)
                    break
                current_indice += 1

        # If the gold has not been found the saboteurs win
        if gold_found == 0:
            state = 1
            self.__menu.fin_de_manche(state, current_indice)
            pass

        # Empty the pick and drop
        self.__pioche = []
        self.__defausse = []

        # Remove the cards from the board
        self.__plateau.reset_plateau()

    # How a game is played
    def start_game(self):
        """How a game is played"""
        # Initialization of the game
        self.__initpartie()
        # The game is played in three rounds
        for i in range(3):
            # We display on the board which round we are at
            self.__plateau.no_manche = i + 1
            # A round is going on
            self.__manche()
        self.__menu.fin_de_partie()

