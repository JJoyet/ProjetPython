import numpy as np
import random
import os
from .hand import Hand
from .card import Card
from .board import Board
from .player import Player
from .action_card import Action_card
from .path_card import Path_card
import sys


class IA_Digger(Player):
    """ Using this class the players (digger) can make their choices"""

    def __init__(self, name, role, nb_players):
        super().__init__(name, role, nb_players)

    def __print_game_state_player(self, board):
        if not isinstance(board, Board):
            print("Error: The player needs the board to take a decision")
            sys.exit()
        # Display of the board and the hand of the player whose turn it is
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the content of the console, we check if we are on
        # window

        # Displays which round we are on
        print("+-----------+")
        print("| ROUND : {0} |".format(board.nb_round))
        print("+-----------+")

        # Display the board: board.affiche()
        print(board)
        print("It is {0} turn, your role is: {1}".format(self.name, self.role))
        # Displays the player's hand
        print(self.hand)

        # Displays the status of its tools
        self.hand.print_tools()
    # Method to ask the player what action he wants to take
    def __choice_action(self, board):

        if not isinstance(board, Board):
            print("Error: The player needs the board to take a decision")
            sys.exit()



        # The player chooses an action
        print("What action do you want to take?")
        print("1) Use a card")
        print("2) Passing your turn and throw away a card")
        choice_action = 0
        nb_good_cards: int = 0
        #for k in range(len(self.hand.cards)):
        #    if self.hand.cards[k].typ == 0:
        #        nb_good_cards += 1
         #   elif self.hand.cards[k].typ == 1 and self.hand.cards[k].vectapparence[0] == 2:
          #      nb_good_cards += 1
        #if nb_good_cards >= 4:
         #   choix_action = 1
        #else :
         #   choix_action = 2
        choice_action = np.random.randint(1,3)
        return choice_action

    def __change_action(self, board):     # Fait
        """Define another action if an action could not be performed """
        change = np.random.randint(0, 2)  # Choice between 0 and 1
        return change

    # Method to ask the player which card he wants to play
    def __choice_card(self, board, choice_action):
        # We make sure that a board has been set up
        if not isinstance(board, Board):
            print("Error: The player needs the board to take a decision")
            sys.exit()

        # We make sure that the choice value given as input is correct
        if choice_action != 1 and choice_action != 2:
            print("Error: the action choice entered in parameter does not correspond to any possible action")
            sys.exit()

        self.__print_game_state_player(board)

        # We make sure that the player chooses one of his cards
        state = False
        change = 0
        nb_card = 0
        # for k in range(len(self.hand.cards)):
           # if self.hand.cards[k].typ == 0:
            #    if card.path[card.sens][k] == [1, 0, 1, 1, 0] or card.path[card.sens][k] == [1, 1, 1, 1, 0] or card.path[card.sens][k] == [1, 0, 1, 1, 1] or card.path[card.sens][k] == [1, 1, 1, 1, 1,]:
            #        no_carte = k
            #elif self.hand.cards[k].typ == 1 and self.hand.cards[k].vectapparence[0] == 2:
        #        no_carte = k
        if len(self.hand.cards) == 1:
            nb_card = 1
        else:
            nb_card = np.random.randint(1, len(self.hand.cards))

        if change == 0:
            # We get the card that the player has chosen
            choice_card = self.hand.cards[nb_card -1]
        else:
            # We create a card that will not be used
            choice_card = Action_card(1)

        # The value change allows the player to change the action
        return change, choice_card

    def choice_direction_card(self, board, choice_card):
        """Method that allows the player to choose the direction of the card"""

        # Check the nature of the parameters
        if not isinstance(board, Board):
            print("Error: The player needs the board to make a decision")
            sys.exit()

        if not isinstance(choice_card, Path_card):
            print("Error: Player needs a card to make a decision")
            sys.exit()

        # Make sure the player chooses sens = 0 or sens = 1
        state = False
        change = 0
        while (state == False and change == 0):
            sens = np.random.randint(1, 2)
            state = True
        choice_card.sens = sens
        return change

    # Method to choose a position where to place the map
    def __choice_pos(self, board, card):
        """Check  if the placed path cards meet the conditions"""
        # We check the input parameters
        if not isinstance(board, Board):
            print("Error: The player needs the board to make a decision")
            sys.exit()
        if not isinstance(card, Card):
            print("Error: The player needs the board to make a decision")
            sys.exit()

        pos = []
        x = 0
        y = 0
        self.__print_game_state_player(board)
        print(card)
        print("Where do you want to place your card ?")

        # We make sure that the player places the card on the board, that he does not overlap the cards and
        # that the card he places is compatible with the other cards
        state = False
        change = 0
        i = 2
        j = 10
        case = 1
        while state == False and change == 0:
            if (i >= -10 and j <= 10 and i >= -10 and j <= 10):
                if board.pathmap[i + 15][j + 15][0] == 0:
                    if ((card.path[card.sens][1] == board.pathmap[i + 14][j + 15][4] or
                         board.pathmap[i + 14][j + 15][0] == 0) and (
                                card.path[card.sens][2] == board.pathmap[i + 15][j + 14][3] or
                                board.pathmap[i + 15][j + 14][0] == 0) and (
                                card.path[card.sens][3] == board.pathmap[i + 15][j + 16][2] or
                                board.pathmap[i + 15][j + 16][0] == 0) and (
                                card.path[card.sens][4] == board.pathmap[i + 16][j + 15][1] or
                                board.pathmap[i + 16][j + 15][0] == 0)) and (
                            board.pathmap[i + 14][j + 15][0] == 1 or board.pathmap[i + 16][j + 15][0] == 1 or
                            board.pathmap[i + 15][j + 14][0] == 1 or board.pathmap[i + 15][j + 16][0] == 1):
                        state = True
                        pos = [i, j]
                    else:
                        self.__print_game_state_player(board)
                        print(card)
                        print("The card does not fit with the other cards")
                        change = self.__change_action(board)
                        if change == 0:
                            self.__print_game_state_player(board)
                            print(card)
                            print("Where do you want to place your card ?")
                else:
                    self.__print_game_state_player(board)
                    print(card)
                    print("A card is already positioned at the desired location, choose another position")
                    print("Where do you want to place your card ?")
            else:
                self.__print_game_state_player(board)
                print(card)
                print("Please place the card on the board (-10<=i<=10) (-10<=j<=10)")
                print("Where do you want to place your card ?")
            j -= 1
            if j == 0:
                if case == 1:
                    j = 10
                    i += 1  # A revoir si on change la taille du tableau
                    if i == 11:
                        i == 2
                        case = 2
                elif case == 2:
                    j = 10
                    i -= 10
                    if i == -1:
                        i = 2
                        case = 1

        # The value change allows the player to change the action
        return change, pos

    # Method to use an action_tools card
    def __use_tools_card(self, players, choice_card):   # Fait
        """Allow a player to use a tool card"""
        # Erase the content of the console, we check if we are on Windows
        os.system('cls' if os.name == 'nt' else 'clear')
        # On affiche les outils des joueurs
        for player in players:
            print(f"{player.name}'s tools:")
            player.hand.print_tools()

        # The player is asked on which player he wants to apply the card
        change = 0
        choice_player = np.random.randint(1, len(players))
        if change == 0:
            # The tools of the chosen player are repaired
            if choice_card.vectlook[0] == 2:
                players[choice_player].hand.tools[choice_card.vectlook[1] - 4] = 1
                if choice_card.vectlook[2] != 0:
                    players[choice_player].hand.tools[choice_card.vectlook[2] - 4] = 1
            # The tools of the chosen player are destroyed
            if choice_card.vectlook[0] == 3:
                players[choice_player].hand.tools[choice_card.vectlook[1] - 4] = 0
                if choice_card.vectlook[2] != 0:
                    players[choice_player].hand.tools[choice_card.vectlook[2] - 4] = 0
        # The value change allows the player to change the action
        # The value change allows the player to change the action
        return change

    def player_turn(self, board, unplayed_deck, played_deck, players):
        """Allow a player to play for one turn"""
        change = 1
        while change == 1:
            # The player chooses an action
            choice_action = self.__choice_action(board)

            if choice_action == 1:
                # The player is asked which card he wants to play
                change, choice_card = self.__choice_card(board, choice_action)

                if change == 1:
                    pass

                else:
                    # The map is a path
                    if choice_card.typ == 0:
                        # The player is asked which direction he wants to put his card
                        change = self.choice_direction_card(board, choice_card)

                        if change == 0:
                            # The player is asked where he wants to put his card
                            change, pos = self.__choice_pos(board, choice_card)

                            if change == 0:
                                # The card is placed on the board
                                board.add_card(choice_card, pos)

                    # The card is a tool action card
                    if choice_card.typ == 1:
                        self.__use_tools_card(players, choice_card)

                    # The card is a secret plan
                    if choice_card.typ == 2:
                        choice = np.random.randint(0, 3)
                        pos = [2,2]
                        if pos == board.pos_gold:
                            a = 1

                        else:
                            a = 1

                    if choice_card.typ == 6:  # The map is a crumbling map
                        state = False
                        while (state == False and change == 0):
                            self.__print_game_state_player(board)
                            print("Which path do you want to collapse?")
                            try:
                                i = 10
                                j = 10
                                pos = [i, j]
                                state = board.collapse(pos)
                                if state == False:
                                    self.__print_game_state_player(board)
                                    print("The position does not correspond to any card.")
                                    change = self.__change_action(board)
                                    i = i -1
                                    if i == 0:   # Change column
                                        i = 10
                                        j -= 1
                                    else:
                                        i = i - 1

                            except ValueError:
                                self.__print_game_state_player(board)
                                print("Please choose a position on the board")
            elif choice_action == 2:  # The player is asked which card he wants to discard
                change, choice_card = self.__choice_card(board, choice_action)
                if change == 0:
                    # The card is placed in the discard pile
                    unplayed_deck.append(choice_card)
        # The card is removed from the player's hand
        self.hand.remove_card(choice_card)
        # Player draws a new card if there are any cards left
        if len(unplayed_deck) > 0:
            self.pick_card(unplayed_deck)
        print("IA finished to play")


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
