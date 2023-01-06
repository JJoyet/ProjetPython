import numpy as np
import random
import os
import sys
from .card import Carte
from .path_card import Path_card


class Plateau(object):
    """Plateau du jeu SABOOTERS"""

    def __init__(self):
        # Binary array that determines if a map has been placed and contains the path to the mine
        self.__pathmap = np.ones((30, 30, 5), int)
        for pathmap_i in self.__pathmap:
            for pathmap_ij in pathmap_i:
                pathmap_ij[0] = 0

        # List composed of the cards present on the board
        self.__cartes_posees = []

        # Table of dimensions of the tray that we display, allows to make the tray dynamic
        self.__dimensions = [[0, 0], [0, 0]]

        # Attribute that allows to keep in memory the position of the gold card
        self.__pos_gold = []

        # Attribute that allows to keep in memory the position of the start card
        self.__pos_start = []

        # Attribute that allows to keep in memory the positions of the stone cards
        self.__pos_stone = []

        # Attribute that determines if the gold card has been found
        self.__gold_found = 0

        # Variable that displays which round the game is in
        self.no_manche = 0  # The attribute is public because it must be able to be modified from the outside

    def add_carte(self, carte, pos, init_game=0):  # The parameter init_game allows to say if we initialize the game
        """#Method to add a card on the board,
         we set the parameters of the card
         and the position where we want to put the card"""

        # Check if the card is a card
        if not isinstance(carte, Path_card):
            print("Error: only cards can be placed on the board")
            sys.exit()

        # Limit the area where the card can be placed
        if pos[0] < -10 or pos[0] > 10 or pos[1] < -10 or pos[1] > 10:
            print("Error: The position of the card goes beyond the maximum size of the tray")
            sys.exit()

        # Check if there is already a card positioned at the desired location
        if self.__pathmap[pos[0] + 15][pos[1] + 15][0] == 1:
            print("Error: a card is already positioned at the desired location")
            sys.exit()

        # Check if the value entered for init_game is correct
        if init_game != 0 and init_game != 1:
            print("Error: incorrect value entered for init_game")
            sys.exit()

        # Arrival cards are placed face down
        if carte.typ != 4 and carte.typ != 5:
            carte.face = 1
        else:
            carte.face = 0

        # The tray keeps track of the position of the gold card
        if carte.typ == 4:
            self.__pos_gold = pos

        # The board keeps track of the position of the stone cards
        if carte.typ == 5:
            self.__pos_stone.append(pos)

        # The board remembers the position of the start card
        if carte.typ == 3:
            self.__pos_start = pos

        # Changing the position of the map
        carte.pos = pos

        # Add the card to the cards on the board
        self.__cartes_posees.append(carte)

        # The size of the board is readjusted to the position of the new card placed on it
        if pos[0] < self.__dimensions[0][0]:
            self.__dimensions[0][0] = pos[0]

        if pos[0] + 1 > self.__dimensions[0][1]:
            self.__dimensions[0][1] = pos[0] + 1

        if pos[1] < self.__dimensions[1][0]:
            self.__dimensions[1][0] = pos[1]

        if pos[1] + 1 > self.__dimensions[1][1]:
            self.__dimensions[1][1] = pos[1] + 1

        # Indicates that a card is placed at the card's position
        self.__pathmap[carte.pos[0] + 15][carte.pos[1] + 15] = carte.path[carte.sens]

        if init_game == 0:
            # Check if the card has been placed next to an END card
            if ((pos[0] == self.__pos_gold[0] + 1 or pos[0] == self.__pos_gold[0] - 1) and pos[1] == self.__pos_gold[1]) or ((pos[1] == self.__pos_gold[1] + 1 or pos[1] == self.__pos_gold[1] - 1) and pos[0] == self.__pos_gold[0]):
                for i in range(len(self.__cartes_posees)):
                    if self.__cartes_posees[i].pos == self.__pos_gold:
                        self.__cartes_posees[i].face = 1
                        self.__gold_found = 1

            # Check if the card has been placed next to a stone card
            for pos_stone in self.__pos_stone:
                if ((pos[0] == pos_stone[0] + 1 or pos[0] == pos_stone[0] - 1) and pos[1] == pos_stone[1]) or (
                        (pos[1] == pos_stone[1] + 1 or pos[1] == pos_stone[1] - 1) and pos[0] == pos_stone[0]):
                    for carte in self.__cartes_posees:
                        if carte.pos == pos_stone:
                            carte.face = 1

    def collapse(self, pos):
        """Method to create a crumbling"""

        etat = False
        for carte in self.__cartes_posees:
            # Look among the cards placed if there is one that corresponds
            # to the position of the crumbling and if it does not correspond to a start or finish card
            if carte.pos == pos and carte.typ != 3 and carte.typ != 4 and carte.typ != 5:
                etat = True
                self.__cartes_posees.remove(carte)
                break
        if etat == True:
            self.__pathmap[pos[0]][pos[1]] = [0, 1, 1, 1]
        # The method returns a boolean which indicates if the operation is successful
        return etat

    def reset_plateau(self):
        """Function that resets the board"""

        self.__pathmap = np.ones((30, 30, 5), int)
        for pathmap_i in self.__pathmap:
            for pathmap_ij in pathmap_i:
                pathmap_ij[0] = 0
        self.__cartes_posees = []
        self.__dimensions = [[0, 0], [0, 0]]
        self.__pos_gold = []
        self.__pos_stone = []
        self.__gold_found = 0

    def __str__(self):
        """toString function"""
        st = ""
        # Function that displays the game board
        # Display of the first line
        for j in range(self.__dimensions[1][0], self.__dimensions[1][1] + 1):
            if j == self.__dimensions[1][0]:
                st += "  |"
            else:
                # Manage the case where the column number has 2 characters
                if (j - 1) < 0 or (j - 1) >= 10:
                    st += f" {j - 1}  "
                else:
                    st += f"  {j - 1}  "
        st += "|" + "\n"

        # Display of the second line, upper part of the frame
        for j in range(self.__dimensions[1][0], self.__dimensions[1][1] + 1):
            if j == self.__dimensions[1][0]:
                st += "--+"
            else:
                st += "-----"
        st += "+--" + "\n"

        for i in range(self.__dimensions[0][0], self.__dimensions[0][1]):
            for x in range(0, 3):
                if x == 1:
                    # Manage the case where the line number has 2 characters
                    if i < 0 or i >= 10:
                        st += f"{i}|"
                    else:
                        st += f" {i}|"
                else:
                    st += "  |"
                for j in range(self.__dimensions[1][0], self.__dimensions[1][1]):
                    if self.__pathmap[i + 15][j + 15][0] == 0:
                        st += "     "
                    else:
                        for k in range(len(self.__cartes_posees)):
                            if self.__cartes_posees[k].pos == [i, j]:
                                st += self.__cartes_posees[k].part_st(x)
                st += "|" + "\n"

        # Display of the last line, bottom part of the frame
        for j in range(self.__dimensions[1][0], self.__dimensions[1][1] + 1):
            if j == self.__dimensions[1][0]:
                st += "--+"
            else:
                st += "-----"
        st += "+--" + "\n"
        return st

    @property
    def cartes_posees(self):
        return self.__cartes_posees

    @property
    def pathmap(self):
        return self.__pathmap

    @property
    def gold_found(self):
        return self.__gold_found

    @property
    def pos_gold(self):
        return self.__pos_gold
