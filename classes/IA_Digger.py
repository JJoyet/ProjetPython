import numpy as np
import random
import os
from .hand import Hand
from .card import Carte
from .board import Plateau
from .player import Player
from .action_card import Action_card
from .path_card import Path_card
import sys


class IA_Digger(Player):
    """ Using this class the players (digger) can make their choices"""

    def __init__(self, name, role, nb_players):
        super().__init__(name, role, nb_players)


        # Display the board: plateau.affiche()
        print(plateau)
        print("It is {0} turn, your role is: {1}".format(self.name, self.role))

        # Displays the player's hand
        print(self.hand)

        # Displays the status of its tools
        self.hand.affiche_tools()

    # Method to ask the player what action he wants to take
    def __choix_action(self, plateau):  # Pas fait

        if not isinstance(plateau, Plateau):
            print("Error: The player needs the board to take a decision")
            sys.exit()

        # Display of the board and the hand of the player whose turn it is
        self.__print_game_state_player(plateau)

        # The player chooses an action
        print("What action do you want to take?")
        print("1) Use a card")
        print("2) Passing your turn and throw away a card")
        choix_action = 1

        return choix_action

    def __change_action(self, plateau):     # Pas fait
        """Define another action if an action could not be performed """
        change = np.random.randint(0, 2)  # Choice between 0 and 1
        return change

    # Method to ask the player which card he wants to play
    def __choix_carte(self, plateau, choix_action): # Pas fait

        # We make sure that a board has been set up
        if not isinstance(plateau, Plateau):
            print("Error: The player needs the board to take a decision")
            sys.exit()

        # We make sure that the choice value given as input is correct
        if choix_action != 1 and choix_action != 2:
            print("Error: the action choice entered in parameter does not correspond to any possible action")
            sys.exit()

        # We make sure that the player chooses one of his cards
        state = False
        change = 0
        while state == False and change == 0:
            self.__print_game_state_player(plateau)
            print("What card would you like to chose (1 to {0})?".format(len(self.hand.cards)))
            no_carte = input()
            if no_carte.isdecimal() == True:
                no_carte = int(no_carte)
                if (no_carte > 0 and no_carte <= len(self.hand.cards)):
                    if choix_action == 2 or (
                            choix_action == 1 and self.hand.tools[0] == 1 and self.hand.tools[1] == 1 and
                            self.hand.tools[2] == 1) or isinstance(self.hand.cards[no_carte - 1], Action_card):
                        state = True
                        no_carte = no_carte - 1
                    else:
                        self.__print_game_state_player(plateau)
                        print("One of the tools is broken, this card cannot be used.")
                        change = self.__change_action(plateau)
                else:
                    self.__print_game_state_player(plateau)
                    print("Please, do not steal a card from your neighbour!")
                    change = self.__change_action(plateau)
            else:
                self.__print_game_state_player(plateau)
                print("Please, do not steal a card from your neighbour!")
                change = self.__change_action(plateau)

        if change == 0:
            # We get the card that the player has chosen
            choix_carte = self.hand.cards[no_carte]
        else:
            # We create a card that will not be used
            choix_carte = Action_card(1)

        # The value change allows the player to change the action
        return change, choix_carte

    def choix_sens_carte(self, plateau, choix_carte):   # Pas fait
        """Method that allows the player to choose the direction of the card"""

        # Check the nature of the parameters
        if not isinstance(plateau, Plateau):
            print("Error: The player needs the board to make a decision")
            sys.exit()

        if not isinstance(choix_carte, Path_card):
            print("Error: Player needs a card to make a decision")
            sys.exit()

        # Make sure the player chooses sens = 0 or sens = 1
        state = False
        change = 0
        while (state == False and change == 0):
            self.__print_game_state_player(plateau)
            print("Which way do you want to orient the card (0 or 1)?")
            choix_carte.sens = 0
            print("0 for the direct direction")
            print(choix_carte, end="\n\n")
            choix_carte.sens = 1
            print("")
            print("1 for the indirect direction")
            print(choix_carte)
            sens = np.randint(0, 2)
        choix_carte.sens = sens
        return change

    # Method to choose a position where to place the map
    def __choix_pos(self, plateau, card):   # Pas fait
        """Check  if the placed path cards meet the conditions"""
        # We check the input parameters
        if not isinstance(plateau, Plateau):
            print("Error: The player needs the board to make a decision")
            sys.exit()
        if not isinstance(card, Carte):
            print("Error: The player needs the board to make a decision")
            sys.exit()

        pos = []
        x = 0
        y = 0
        self.__print_game_state_player(plateau)
        print(card)
        print("Where do you want to place your card ?")

        # We make sure that the player places the card on the board, that he does not overlap the cards and
        # that the card he places is compatible with the other cards
        state = False
        change = 0
        while state == False and change == 0:
            i = input("Choose the line where you want to put the card: ")
            j = input("Choose the column where you want to put the card: ")
            try:
                i = int(i)
                j = int(j)
                if (i >= -10 and j <= 10 and i >= -10 and j <= 10):
                    if plateau.pathmap[i + 15][j + 15][0] == 0:
                        if ((card.path[card.sens][1] == plateau.pathmap[i + 14][j + 15][4] or
                             plateau.pathmap[i + 14][j + 15][0] == 0) and (
                                    card.path[card.sens][2] == plateau.pathmap[i + 15][j + 14][3] or
                                    plateau.pathmap[i + 15][j + 14][0] == 0) and (
                                    card.path[card.sens][3] == plateau.pathmap[i + 15][j + 16][2] or
                                    plateau.pathmap[i + 15][j + 16][0] == 0) and (
                                    card.path[card.sens][4] == plateau.pathmap[i + 16][j + 15][1] or
                                    plateau.pathmap[i + 16][j + 15][0] == 0)) and (
                                plateau.pathmap[i + 14][j + 15][0] == 1 or plateau.pathmap[i + 16][j + 15][0] == 1 or
                                plateau.pathmap[i + 15][j + 14][0] == 1 or plateau.pathmap[i + 15][j + 16][0] == 1):
                            state = True
                            pos = [i, j]
                        else:
                            self.__print_game_state_player(plateau)
                            print(card)
                            print("The card does not fit with the other cards")
                            change = self.__change_action(plateau)
                            if change == 0:
                                self.__print_game_state_player(plateau)
                                print(card)
                                print("Where do you want to place your card ?")
                    else:
                        self.__print_game_state_player(plateau)
                        print(card)
                        print("A card is already positioned at the desired location, choose another position")
                        print("Where do you want to place your card ?")
                else:
                    self.__print_game_state_player(plateau)
                    print(card)
                    print("Please place the card on the board (-10<=i<=10) (-10<=j<=10)")
                    print("Where do you want to place your card ?")
            except ValueError:
                self.__print_game_state_player(plateau)
                print(card)
                print("Please place the card on the board (-10<=i<=10) (-10<=j<=10)")
                print("Where do you want to place your card ?")

        # The value change allows the player to change the action
        return change, pos

    # Method to use an action_tools card
    def __use_tools_card(self, players, choix_carte):   # Fait
        """Allow a player to use a tool card"""
        # Erase the content of the console, we check if we are on Windows
        os.system('cls' if os.name == 'nt' else 'clear')
        # On affiche les outils des joueurs
        for player in players:
            print(f"{player.name}'s tools:")
            player.hand.affiche_tools()

        # The player is asked on which player he wants to apply the card
        change = 0
        choix_player = np.randint(0, len(players)+1)
        if change == 0:
            # The tools of the chosen player are repaired
            if choix_carte.vectapparence[0] == 2:
                if choix_carte.vectapparence[2] != 0:
                    players[choix_player].hand.tools[choix_carte.vectapparence[2] - 4] = 1

                # The tools of the chosen player are destroyed
                if choix_carte.vectapparence[0] == 3:
                    players[choix_player].hand.tools[choix_carte.vectapparence[1] - 4] = 0
                if choix_carte.vectapparence[2] != 0:
                    players[choix_player].hand.tools[choix_carte.vectapparence[2] - 4] = 0

        # The value change allows the player to change the action
        return change

    def tourjoueur(self, plateau, pioche, defausse, players):   # Pas fait
        """Allow a player to play for one turn"""
        change = 1
        while change == 1:
            # The player chooses an action
            choix_action = self.__choix_action(plateau)

            if choix_action == 1:
                # The player is asked which card he wants to play
                change, choix_carte = self.__choix_carte(plateau, choix_action)

                if change == 1:
                    pass

                else:
                    # The map is a path
                    if choix_carte.typ == 0:
                        # The player is asked which direction he wants to put his card
                        change = self.choix_sens_carte(plateau, choix_carte)

                        if change == 0:
                            # The player is asked where he wants to put his card
                            change, pos = self.__choix_pos(plateau, choix_carte)

                            if change == 0:
                                # The card is placed on the board
                                plateau.add_carte(choix_carte, pos)

                    # The card is a tool action card
                    if choix_carte.typ == 1:
                        self.__use_tools_card(players, choix_carte)

                    # The card is a secret plan
                    if choix_carte.typ == 2:
                        print("Which card do you want to reveal? ")
                        state = False
                        while state == False:
                            i = input("Choose the line where you want to put the card: ")
                            j = input("Choose the column where you want to put the card: ")
                            try:
                                i = int(i)
                                j = int(j)
                                state = True
                                pos = [i, j]
                            except ValueError:
                                self.__print_game_state_player(plateau)
                                print("Please choose a position on the board")
                                print("Which card do you want to reveal? ")

                        if pos == plateau.pos_gold:
                            print(
                                "The ancient scroll tells you that there is more gold here than you could spend on a night of drinking at the tavern.")
                            a = input("Press any button to continue.")

                        else:
                            print(
                                "The old scroll tells you that there is absolutely nothing at this location and that it really sucks.")
                            a = input("Press any button to continue.")

                    if choix_carte.typ == 6:  # The map is a crumbling map
                        state = False
                        while (state == False and change == 0):
                            self.__print_game_state_player(plateau)
                            print("Which path do you want to collapse?")
                            i = input("Choose the line where you want to put the card: ")
                            j = input("Choose the column where you want to put the card: ")
                            try:
                                i = int(i)
                                j = int(j)
                                pos = [i, j]
                                state = plateau.collapse(pos)
                                if state == False:
                                    self.__print_game_state_player(plateau)
                                    print("The position does not correspond to any card.")
                                    change = self.__change_action(plateau)
                            except ValueError:
                                self.__print_game_state_player(plateau)
                                print("Please choose a position on the board")
            elif choix_action == 2:  # The player is asked which card he wants to discard
                change, choix_carte = self.__choix_carte(plateau, choix_action)
                if change == 0:
                    # The card is placed in the discard pile
                    defausse.append(choix_carte)
        # The card is removed from the player's hand
        self.hand.remove_card(choix_carte)
        # Player draws a new card if there are any cards left
        if len(pioche) > 0:
            self.piocher_carte(pioche)


"""
• 3 players : 1 Saboteur and 3 Diggers
• 4 players : 1 Saboteur and 4 Diggers
• 5 players : 2 Saboteurs and 4 Diggers
• 6 players : 2 Saboteurs and 5 Diggers
• 7 players : 3 Saboteurs and 5 Diggers
• 8 players : 3 Saboteurs and 6 Diggers
• 9 players : 3 Saboteurs and 7 Diggers
• 10 players : all Role cards (4 Saboteurs and 7 Diggers)
"""
