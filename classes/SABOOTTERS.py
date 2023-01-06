import numpy as np
import random

from .deck import Deck
from .menu import Menu
from .player import Player
from .hand import Hand
from .card import Card
from .board import Board
from .human import Human
from .IA_Digger import IA_Digger


class SABOOTERS(object):
    """Class containing the whole game"""

    def __init__(self):
        self.__menu = Menu()
        self.__deck = Deck()
        self.__unplayed_deck = []
        self.__played_deck = []
        self.__players = []
        self.__board = Board()

    def __initgame(self):
        """ Initialization of a game"""

        self.__menu.start_game()
        for i in range(0, self.__menu.number):
            if self.__menu.bot[i] == "Human":
                self.__players.append(Human(self.__menu.players_name[i], self.__menu.roles[i], self.__menu.number))
            elif self.__menu.bot[i] == "AI":
                self.__players.append(IA_Digger(self.__menu.players_name[i], self.__menu.roles[i], self.__menu.number))
            self.__players.append(Human(self.__menu.players_name[i], self.__menu.roles[i], self.__menu.number))

    def __initround(self):
        """Initialization of a round"""
        self.__menu.change_role()
        i = 0
        for player in self.__players:
            player.role = self.__menu.roles[i]
            i += 1


        self.__deck.random_cards()     # Shuffle the cards

        set_pos_gold = random.sample([[-1, 5], [2, 5], [5, 5]], 3)   # Define the positions of the "END" cards

        # Card distribution
        k = 0
        for card in self.__deck.cards:
            # Place the arrival/departure cards on the board
            if card.typ == 3 or card.typ == 4 or card.typ == 5:
                if card.typ == 3:
                    self.__board.add_card(card, [2, 0], 1)
                else:
                    self.__board.add_card(card, set_pos_gold[k], 1)
                    k = k + 1
            # Create the deck with the action and path cards
            else:
                self.__unplayed_deck.append(card)
        # Players draw their cards
        for i in range(self.__menu.number):
            for j in range(self.__players[i].hand.hand_size):
                self.__players[i].pick_card(self.__unplayed_deck)


    def __round(self, nb_player_turn):
        """How a round unfolds"""

        # Initialization of a game
        self.__initround()
        self.nb_player_turn = nb_player_turn
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

            for k in range(len(self.__players)):
                self.__players[self.nb_player_turn].player_turn(self.__board, self.__unplayed_deck, self.__played_deck, self.__players)
                nb_card_player = nb_card_player + len(self.__players[self.nb_player_turn].hand.cards)
                gold_found = self.__board.gold_found
                self.nb_player_turn += 1
                # Re-loop to allow every player to play
                if self.nb_player_turn > len(self.__players) - 1:
                    self.nb_player_turn = 0
                # If gold has been found it is the end of the round, the diggers win
                if gold_found == 1:
                    state = 2
                    self.__menu.end_round(state, current_indice)
                    break
                current_indice += 1

        # If the gold has not been found the saboteurs win
        if gold_found == 0:
            state = 1
            self.__menu.end_round(state, current_indice)
            pass

        # Empty the pick and drop
        self.__unplayed_deck = []
        self.__played_deck = []

        # Remove the cards from the board
        self.__board.reset_board()

    def start_game(self):
        """How a game is played"""
        # Initialization of the game

        self.__initgame()
        # The game is played in three rounds
        print("Write the name of the youngest person")
        state = False
        k = 0
        while state == False:
            name = input()
            for i in range(len(self.__menu.players_name)):
                if name == str(self.__menu.players_name[i]):
                    nb_player_turn = i
                    state = True
            else:
                print('Please write a correct name')
        self.__board.nb_round = 1
        # A round is going on
        self.__round(nb_player_turn)
        for i in range(2):
            # We display on the board which round we are at
            self.__board.nb_round = i + 1
            # A round is going on

            self.__round(nb_player_turn)
            nb_player_turn += 1
        self.__menu.end_game()

