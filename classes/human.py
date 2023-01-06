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


class Human(Player):
    """ Using this class the (human) players can make their choices"""
    def __init__(self, name, role, nb_players):
        super().__init__(name, role, nb_players)

    # Function that displays the game status to the human player
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
        self.hand.affiche_tools()

    # Method to ask the player what action he wants to take
    def __choix_action(self, board):

        if not isinstance(board, Board):
            print("Error: The player needs the board to take a decision")
            sys.exit()

        # Display of the board and the hand of the player whose turn it is
        self.__print_game_state_player(board)

        # The player chooses an action
        print("What action do you want to take?")
        print("1) Use a card")
        print("2) Passing your turn and throw away a card")

        etat = False
        while (etat == False):
            choix_action = input()
            if choix_action.isdecimal() == True:
                choix_action = int(choix_action)
                if choix_action == 1 or choix_action == 2:
                    etat = True
                else:
                    self.__print_game_state_player(board)
                    print("Please, don't do anything else and just play!")
                    print("1) Use a card")
                    print("2) Passing your turn and throw away a card")
            else:
                self.__print_game_state_player(board)
                print("Please, don't do anything else and just play!")
                print("1) Use a card")
                print("2) Passing your turn and throw away a card")

        return choix_action

    def __change_action(self, board):
        """Define another action if an action could not be performed """
        etat = False
        while etat == False:
            print("Do you want to take another action?")
            print("1: yes 0: no")
            change = input()
            if change.isdecimal() == True:
                change = int(change)
                if change == 1 or change == 0:
                    etat = True
                else:
                    self.__print_game_state_player(board)
                    print("Please, don't do anything else and just play!")

            else:
                self.__print_game_state_player(board)
                print("Please, don't do anything else and just play!")

        return change

    # Method to ask the player which card he wants to play
    def __choix_card(self, board, choix_action):

        # We make sure that a board has been set up
        if not isinstance(board, Board):
            print("Error: The player needs the board to take a decision")
            sys.exit()

        # We make sure that the choice value given as input is correct
        if choix_action != 1 and choix_action != 2:
            print("Error: the action choice entered in parameter does not correspond to any possible action")
            sys.exit()

        # We make sure that the player chooses one of his cards
        etat = False
        change = 0
        while etat == False and change == 0:
            self.__print_game_state_player(board)
            print("What card would you like to chose (1 to {0})?".format(len(self.hand.cards)))

            no_card = input()
            if no_card.isdecimal() == True:
                no_card = int(no_card)
                if (no_card > 0 and no_card <= len(self.hand.cards)):
                    if choix_action == 2 or (
                            choix_action == 1 and self.hand.tools[0] == 1 and self.hand.tools[1] == 1 and
                            self.hand.tools[2] == 1) or isinstance(self.hand.cards[no_card - 1], Action_card):
                        etat = True
                        no_card = no_card - 1
                    else:
                        self.__print_game_state_player(board)
                        print("One of the tools is broken, this card cannot be used.")
                        change = self.__change_action(board)
                else:
                    self.__print_game_state_player(board)
                    print("Please, do not steal a card from your neighbour!")
                    change = self.__change_action(board)
            else:
                self.__print_game_state_player(board)
                print("Please, do not steal a card from your neighbour!")
                change = self.__change_action(board)

        if change == 0:
            # We get the card that the player has chosen
            choix_card = self.hand.cards[no_card]
        else:
            # We create a card that will not be used
            choix_card = Action_card(1)

        # The value change allows the player to change the action
        return change, choix_card

    def choix_sens_card(self,board,choix_card):
        """Method that allows the player to choose the direction of the card"""

        #We check the nature of the parameters
        if not isinstance ( board , Board ) :
            print("Erreur: Le joueur a besoin du board pour prendre une decision")
            sys.exit()

        if not isinstance (choix_card , Path_card ) :
            print("Erreur: Le joueur a besoin d'une card pour prendre une decision")
            sys.exit()

        #Make sure the player chooses sens=0 or sens=1
        etat = False
        change = 0
        while (etat == False and change == 0):
            self.__print_game_state_player(board)
            print("Which way do you want to orient the card (0 or 1)?")
            choix_card.sens=0
            print(choix_card,end="\n\n")
            choix_card.sens=1
            print(choix_card)
            sens=input()
            if (sens.isdecimal()==True):
                sens=int(sens)
                if sens == 0 or sens ==1:
                        etat = True
                else:
                    self.__print_game_state_player(board)
                    print("It's a card, there are only two possibilities...")
                    change=self.__change_action(board)
            else:
                self.__print_game_state_player(board)
                print("It's a card, there are only two possibilities...")
                change=self.__change_action(board)
        choix_card.sens=sens
        return change
        
    # Method to choose a position where to place the map
    def __choix_pos(self, board, card):
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
        etat = False
        change = 0
        while etat == False and change == 0:
            i = input("(i value)")
            j = input("(j value)")
            try:
                i = int(i)
                j = int(j)
                if (i >= -10 and j <= 10 and i >= -10 and j <= 10):
                    if board.pathmap[i+15][j+15][0]==0  :
                        if ((card.path[card.sens][1]==board.pathmap[i+14][j+15][4] or board.pathmap[i+14][j+15][0]==0)  and (card.path[card.sens][2]==board.pathmap[i+15][j+14][3] or board.pathmap[i+15][j+14][0]==0) and (card.path[card.sens][3]==board.pathmap[i+15][j+16][2] or board.pathmap[i+15][j+16][0]==0) and (card.path[card.sens][4]==board.pathmap[i+16][j+15][1] or board.pathmap[i+16][j+15][0]==0)) and (board.pathmap[i+14][j+15][0]==1 or board.pathmap[i+16][j+15][0]==1 or board.pathmap[i+15][j+14][0]==1 or board.pathmap[i+15][j+16][0]==1):
                            etat = True
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
            except ValueError:
                self.__print_game_state_player(board)
                print(card)
                print("Please place the card on the board (-10<=i<=10) (-10<=j<=10)")
                print("Where do you want to place your card ?")

        # The value change allows the player to change the action
        return change, pos

    # Method to use an action_tools card
    def __use_tools_card(self, players, choix_card):
        """Allow a player to use a tool card"""
        # Erase the content of the console, we check if we are on Windows
        os.system('cls' if os.name == 'nt' else 'clear')

        # Players' tools are displayed
        for player in players:
            print(f"{player.name}'s tools:")
            player.hand.affiche_tools()

        # The player is asked on which player he wants to apply the card
        change = 0
        etat = 0
        while etat == 0 and change == 0:
            choix_player = input("On which player do you want to apply this card? (0 to {0})".format(len(players) - 1))
            try:
                choix_player = int(choix_player)
                if choix_player >= 0 and choix_player <= len(players) - 1:
                    etat = True
                else:
                    print("The value entered is not correct")
                    change = self.__change_action(board)
                    if change == 0:
                        # Erase the content of the console, we check if we are on Windows
                        os.system('cls' if os.name == 'nt' else 'clear')
                        # Players' tools are displayed
                        for player in players:
                            print(f"{players.name}'s tools:")
                            player.hand.affiche_tools()

            except ValueError:
                # Erase the content of the console, we check if we are on Windows
                os.system('cls' if os.name == 'nt' else 'clear')
                # On affiche les outils des joueurs
                for player in players:
                    print(f"{players.name}'s tools:")
                    player.hand.affiche_tools()
                    print("Please, don't do anything else and just play!")
        # Erase the content of the console, we check if we are on Windows
        os.system('cls' if os.name == 'nt' else 'clear')

        if change == 0:
            # The tools of the chosen player are repaired
            if choix_card.vectapparence[0] == 2:
                players[choix_player].hand.tools[choix_card.vectapparence[1] - 4] = 1
                if choix_card.vectapparence[2] != 0:
                    players[choix_player].hand.tools[choix_card.vectapparence[2] - 4] = 1

            # The tools of the chosen player are destroyed
            if choix_card.vectapparence[0] == 3:
                players[choix_player].hand.tools[choix_card.vectapparence[1] - 4] = 0
                if choix_card.vectapparence[2] != 0:
                    players[choix_player].hand.tools[choix_card.vectapparence[2] - 4] = 0

        # The value change allows the player to change the action
        return change

    def tourjoueur(self, board, pioche, defausse, players):
        """Allow a player to play for one turn"""
        change = 1
        while change==1:
            #The player chooses an action
            choix_action=self.__choix_action(board)

            if choix_action == 1:
                #The player is asked which card he wants to play
                change, choix_card=self.__choix_card(board,choix_action)
            
                if change==1 :pass

                else:
                    #The map is a path
                    if choix_card.typ==0:
                        #The player is asked which direction he wants to put his card
                        change=self.choix_sens_card(board, choix_card)

                        if change==0:
                            #The player is asked where he wants to put his card
                            change, pos=self.__choix_pos(board,choix_card)

                            if change==0:
                                #The card is placed on the board
                                board.add_card(choix_card,pos)


                    #The card is a tool action card
                    if choix_card.typ==1:
                        self.__use_tools_card(players,choix_card)
                

                    #The card is a secret plan 
                    if choix_card.typ==2: 
                        print("Which card do you want to reveal? ")
                        etat = False
                        while etat == False:
                            i = input("(i value)")
                            j = input("(j value)")
                            try:
                                i = int(i)
                                j = int(j)
                                etat = True
                                pos = [i, j]
                            except ValueError:
                                self.__print_game_state_player(board)
                                print("Please choose a position on the board")
                                print("Which card do you want to reveal? ")

                        if pos == board.pos_gold:
                            print("The ancient scroll tells you that there is more gold here than you could spend on a night of drinking at the tavern.")
                            a = input("Press any button to continue.")

                        else:
                            print("The old scroll tells you that there is absolutely nothing at this location and that it really sucks.")
                            a = input("Press any button to continue.")

                    if choix_card.typ == 6:                        # The map is a crumbling map
                        etat = False
                        while (etat == False and change == 0):
                            self.__print_game_state_player(board)
                            print("Which path do you want to collapse?")
                            i = input("(i value)")
                            j = input("(j value)")
                            try:
                                i = int(i)
                                j = int(j)
                                pos = [i, j]
                                etat = board.collapse(pos)
                                if etat == False:
                                    self.__print_game_state_player(board)
                                    print("The position does not correspond to any card.")
                                    change = self.__change_action(board)
                            except ValueError:
                                self.__print_game_state_player(board)
                                print("Please choose a position on the board")
            elif choix_action == 2:   #  The player is asked which card he wants to discard
                change, choix_card = self.__choix_card(board, choix_action)
                if change == 0:
                    # The card is placed in the discard pile
                    defausse.append(choix_card)
        # The card is removed from the player's hand
        self.hand.remove_card(choix_card)
        # Player draws a new card if there are any cards left
        if len(pioche) > 0:
            self.piocher_card(pioche)


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
