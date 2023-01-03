import numpy as np
import random
import os
from .hand import Hand
from .card import Carte
from .board import Plateau
from .player import Player
from .action_card import Action_card
import sys



class Human(Player):
    def __init__(self,name,role,nb_players):
        super ( ) . __init__ (name,role,nb_players)

#Fonction qui affiche l'état du jeu pour le joueur humain
    def __print_game_state_player(self,plateau):
        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()
        #affichage du plateau et de la main du joueur dont c'est la tour
        os.system('cls' if os.name == 'nt' else 'clear')  #efface le contenue de la console, on verifie si on est sur windows ou pas

        #Affiche à quelle manche on est
        print("+-----------+")
        print("| ROUND : {0} |".format(plateau.no_manche))
        print("+-----------+")

        #Affiche le plateau
        #plateau.affiche()
        print(plateau)
        print("It is {0} turn, your role is: {1}".format(self.name,self.role))

        #Affiche la main du joueur
        self.hand.affiche()

        #Affiche l'état de ses outils
        self.hand.affiche_tools()

    #Methode qui permet de demander au joueur quelle action il veut prendre
    def __choix_action(self,plateau):

        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()


        #affichage du plateau et de la main du joueur dont c'est la tour
        self.__print_game_state_player(plateau)


        #Le joueur choisi une action
        print("What action do you want to take?")
        print("1) Use a card")
        print("2) Passing your turn and throw away a card")
        

        etat = False
        while (etat == False):
            choix_action=input()
            if (choix_action.isdecimal()==True):
                choix_action=int(choix_action)
                if (choix_action == 1 or choix_action == 2):
                    etat = True
                else:
                    self.__print_game_state_player(plateau)
                    print("Please, don't do anything else and just play!")
                    print("1) Use a card")
                    print("2) Passing your turn and throw away a card")
            else:
                self.__print_game_state_player(plateau)
                print("Please, don't do anything else and just play!")
                print("1) Use a card")
                print("2) Passing your turn and throw away a card")


        return choix_action

    #Methode qui permet de changer d'action si une action n'a pas pu être effectué
    def __change_action(self,plateau):
        etat1 = False
        while (etat1 == False):
            print("Do you want to take another action?")
            print("1: yes 0: no")
            change=input()
            if (change.isdecimal()==True):
                change=int(change)
                if (change == 1 or change == 0):
                    etat1 = True
                else:
                    self.__print_game_state_player(plateau)
                    print("Please, don't do anything else and just play!")

            else:
                self.__print_game_state_player(plateau)
                print("Please, don't do anything else and just play!")

        return change

    #Methode qui permet de demander au joueur quelle carte il veut jouer
    def __choix_carte(self,plateau,choix_action):
        #On s'assure qu'un plateau a bien été mis en parametre
        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()

        #On s'assure que la valeur de choix donné en entrée est correct
        if choix_action !=1 and choix_action !=2:
            print("Erreur: le choix d'action entrée en paramètre ne correspond à aucune action possible")
            sys.exit()


        #On s'assure que le joueur choisisse une de ses cartes
        etat = False
        change = 0
        while (etat == False and change == 0):
            self.__print_game_state_player(plateau)
            print("What card would you like to chose (1 to {0})?".format(len(self.hand.cards)))

            no_carte=input()
            if (no_carte.isdecimal()==True):
                no_carte=int(no_carte)
                if (no_carte > 0 and no_carte <= len(self.hand.cards)):
                    if choix_action == 2 or (choix_action == 1 and self.hand.tools[0]==1 and self.hand.tools[1]==1 and self.hand.tools[2]==1) or isinstance ( self.hand.cards[no_carte-1] , Action_card ):
                        etat = True
                        no_carte=no_carte-1
                    else:
                        self.__print_game_state_player(plateau)
                        print("One of the tools is broken, this card cannot be used.")
                        change=self.__change_action(plateau)
                else:
                    self.__print_game_state_player(plateau)
                    print("Please, do not steal a card from your neighbour!")
                    change=self.__change_action(plateau)
            else:
                self.__print_game_state_player(plateau)
                print("Please, do not steal a card from your neighbour!")
                change=self.__change_action(plateau)

        if change==0:
            #On recupere la carte que le joueur a choisi
            choix_carte=self.hand.cards[no_carte]
        else:
            #On crée une carte qui ne sera pas utilisé
            choix_carte=Action_card(1)

        #La valeur change permet au joueur de changer d'action
        return change,choix_carte

    #Methode qui permet de choisir une position où placer la carte
    def __choix_pos(self,plateau,card):
        #On verifie les parametres d'entrée
        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()
        if not isinstance ( card , Carte ) :
            print("Erreur: Le joueur a besoin d'une carte pour prendre une decision")
            sys.exit()

        pos=[]
        x=0
        y=0

        self.__print_game_state_player(plateau)
        print("Where do you want to place your card ?")

        #On s'assure que le joueur pose bien la carte sur le plateau, qu'il ne superpose pas les cartes et que la carte qu'il pose est compatible avec les autres cartes
        etat = False
        change=0
        while (etat == False and change==0):
            i=input("(i value)")
            j=input("(j value)")
            try:
                i = int(i)
                j = int(j)
                if (i >= -10 and j <= 10 and i >= -10 and j <= 10):
                    if plateau.pathmap[i+15][j+15][0]==0  :
                        if ((card.path[1]==plateau.pathmap[i+14][j+15][4] or plateau.pathmap[i+14][j+15][0]==0)  and (card.path[2]==plateau.pathmap[i+15][j+14][3] or plateau.pathmap[i+15][j+14][0]==0) and (card.path[3]==plateau.pathmap[i+15][j+16][2] or plateau.pathmap[i+15][j+16][0]==0) and (card.path[4]==plateau.pathmap[i+16][j+15][1] or plateau.pathmap[i+16][j+15][0]==0)) and (plateau.pathmap[i+14][j+15][0]==1 or plateau.pathmap[i+16][j+15][0]==1 or plateau.pathmap[i+15][j+14][0]==1 or plateau.pathmap[i+15][j+16][0]==1):
                            etat = True
                            pos=[i,j]
                        else:
                            self.__print_game_state_player(plateau)
                            print("The card does not fit with the other cards")
                            change=self.__change_action(plateau)
                            if change == 0:
                                self.__print_game_state_player(plateau)
                                print("Where do you want to place your card ?")
                    else:
                        self.__print_game_state_player(plateau)
                        print("A card is already positioned at the desired location, choose another position")
                        print("Where do you want to place your card ?")
                else:
                    self.__print_game_state_player(plateau)
                    print("Please place the card on the board (-10<=i<=10) (-10<=j<=10)")
                    print("Where do you want to place your card ?")
            except ValueError:
                self.__print_game_state_player(plateau)
                print("Please place the card on the board (-10<=i<=10) (-10<=j<=10)")
                print("Where do you want to place your card ?")

        #La valeur change permet au joueur de changer d'action
        return change, pos

    #Methode qui permet d'utiliser une carte action_tools
    def __use_tools_card(self,players,choix_carte):
        #Revoir cette fonction, augmenter solidité
        #Fonction qui applique une carte d'action d'outils
        os.system('cls' if os.name == 'nt' else 'clear')  #efface le contenue de la console, on verifie si on est sur windows ou pas

        #On affiche les outils des joueurs
        for player in players:
            print("{1}'s tools:".format(player.name))
            player.hand.affiche_tools()

        #On demande au joueur sur quel joueur il veut appliquer la carte
        change=0
        etat=0
        while etat == 0 and change == 0:
            choix_player=input("On which player do you want to apply this card? (0 to {0})".format(len(players)-1))
            try:
                choix_player=int(choix_player)
                if choix_player>=0 and choix_player<=len(players)-1:
                    etat = True
                else:
                    print("The value entered is not correct")
                    change=self.__change_action(plateau)
                    if change == 0:
                        os.system('cls' if os.name == 'nt' else 'clear')  #efface le contenue de la console, on verifie si on est sur windows ou pas
                        #On affiche les outils des joueurs
                        for player in players:
                            print("{1}'s tools:".format(player.name))
                            player.hand.affiche_tools()
                
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')  #efface le contenue de la console, on verifie si on est sur windows ou pas
                #On affiche les outils des joueurs
                for player in players:
                    print("{1}'s tools:".format(players.name))
                    player.hand.affiche_tools()
                    print("Please, don't do anything else and just play!")

        os.system('cls' if os.name == 'nt' else 'clear')  #efface le contenue de la console, on verifie si on est sur windows ou pas

        if change==0:
            #Les outils du joueur choisi sont réparé
            if choix_carte.vectapparence[0]==2:
                players[choix_player].hand.tools[choix_carte.vectapparence[1]-4]=1
                if choix_carte.vectapparence[2] != 0 :
                    players[choix_player].hand.tools[choix_carte.vectapparence[2]-4]=1

            #Les outils du joueur choisi sont détruit
            if choix_carte.vectapparence[0]==3:
                players[choix_player].hand.tools[choix_carte.vectapparence[1]-4]=0
                if choix_carte.vectapparence[2] != 0 :
                    players[choix_player].hand.tools[choix_carte.vectapparence[2]-4]=0

        #La valeur change permet au joueur de changer d'action
        return change
        

    
    #Methode qui fait jouer le joueur pendant un tour
    def tourjoueur(self,plateau,pioche,defausse,players):

        change = 1
        while change==1:
            #Le joueur choisi une action
            choix_action=self.__choix_action(plateau)

            if choix_action == 1:
                #On demande au joueur quel carte il veut jouer
                change, choix_carte=self.__choix_carte(plateau,choix_action)
            
                if change==1 :pass

                else:
                    #La carte est un chemin
                    if choix_carte.typ==0:
                        #On demande au joueur où il veut poser sa carte
                        change, pos=self.__choix_pos(plateau,choix_carte)

                        if change==0:
                            #La carte est placee sur le plateau 
                            plateau.add_carte(choix_carte,pos)


                    #La carte est une carte action d'outils
                    if choix_carte.typ==1:
                        self.__use_tools_card(players,choix_carte)
                

                    #La carte est un plan secret 
                    if choix_carte.typ==2: 
                        print("Which card do you want to reveal? ")
                        etat = False
                        while (etat == False):
                            i=input("(i value)")
                            j=input("(j value)")
                            try:
                                i = int(i)
                                j = int(j)
                                etat = True
                                pos=[i,j]
                            except ValueError:
                                self.__print_game_state_player(plateau)
                                print("Please choose a position on the board")
                                print("Which card do you want to reveal? ")

                        if pos == plateau.pos_gold:
                            print("The ancient scroll tells you that there is more gold here than you could spend on a night of drinking at the tavern.")
                            a=input("Press any button to continue.")

                        else : 
                            print("The old scroll tells you that there is absolutely nothing at this location and that it really sucks.")
                            a=input("Press any button to continue.")

                    #La carte est une carte éboulement
                    if choix_carte.typ==6: 
                        
                        etat = False
                        while (etat == False and change==0):
                            self.__print_game_state_player(plateau)
                            print("Which path do you want to collapse?")
                            i=input("(i value)")
                            j=input("(j value)")
                            try:
                                i = int(i)
                                j = int(j)
                                pos=[i,j]
                                etat = plateau.collapse(pos)
                                if etat == False:
                                    self.__print_game_state_player(plateau)
                                    print("The position does not correspond to any card.")
                                    change=self.__change_action(plateau)
                            except ValueError:
                                self.__print_game_state_player(plateau)
                                print("Please choose a position on the board")


            if choix_action == 2:

                #On demande au joueur quelle carte il veut se defausser
                change, choix_carte=self.__choix_carte(plateau,choix_action)

                if change ==0:
                    #La carte est placé dans la defausse 
                    defausse.append(choix_carte)

        #La carte est retire de la main du joueur
        self.hand.remove_card(choix_carte)
        #Le joueur pioche une nouvelle carte si il reste des cartes
        if len(pioche)>0:
            self.piocher_carte(pioche)


    # @property
    # def name(self):
    #     return self.name

    # @property
    # def role(self):
    #     return self.role

    # @property
    # def hand(self):
    #     return self.hand

    # @hand.setter
    # def hand(self,hand):
    #     self.hand=hand




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
