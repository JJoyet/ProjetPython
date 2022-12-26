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

    def __print_game_state_player(self,plateau):
        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()
        #affichage du plateau et de la main du joueur dont c'est la tour
        os.system("cls")  #efface le contenue de la console, valable que sur windows
        print("+-----------+")
        print("| ROUND : {0} |".format(plateau.no_manche))
        print("+-----------+")
        plateau.affiche()
        print("It is {0} turn:".format(self.name))
        self.hand.affiche()
        self.hand.affiche_tools()

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

    def __change_action(self):

        etat1 = False
        while (etat1 == False):
            print("Do you want to take another action?")
            print("1: yes 0: no")
            change=input()
            print(change)
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

    def __choix_carte(self,plateau,choix_action):
    #On demande au joueur quel carte il veut jouer
        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()

        #On s'assure que le joueur choisisse une de ses cartes
        etat = False
        change = 0

        self.__print_game_state_player(plateau)
        print("What card would you like to chose (1 to {0})?".format(len(self.hand.cards)))

        while (etat == False and change == 0):

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
                        change=self.__change_action()
                        if change == 0:
                            self.__print_game_state_player(plateau)
                            print("What card would you like to chose (1 to {0})?".format(len(self.hand.cards)))

                else:
                    self.__print_game_state_player(plateau)
                    print("Please, do not steal a card from your neighbour!")
                    print("What card would you like to play (1 to {0})?".format(len(self.hand.cards)))
            else:
                self.__print_game_state_player(plateau)
                print("Please, do not steal a card from your neighbour!")
                print("What card would you like to play (1 to {0})?".format(len(self.hand.cards)))


        #On recupere la carte que le joueur a choisi
        choix_carte=self.hand.cards[no_carte]

        return choix_carte, change

    
    def __choix_pos(self,plateau,card):
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
        while (etat == False):
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


        return pos

    def __use_tools_card(self,players,choix_carte):
        #Revoir cette fonction, augmenter solidité
        #Fonction qui applique une carte d'action d'outils
        os.system("cls")  #efface le contenue de la console, valable que sur windows

        #On affiche les outils des joueurs
        for i in range(len(players)):
            print("{0}:{1}'s tools:".format(i,players[i].name))
            players[i].hand.affiche_tools()

        #On demande au joueur sur quel joueur il veut appliquer la carte
        etat=0
        while etat == 0:
            choix_player=input("On which player do you want to apply this card? (0 to {0})".format(len(players)-1))
            try:
                choix_player=int(choix_player)
                if choix_player>=0 and choix_player<=len(players)-1:
                    etat = True
                else:
                    os.system("cls")  #efface le contenue de la console, valable que sur windows
                    #On affiche les outils des joueurs
                    for i in range(len(players)):
                        print("{0}:{1}'s tools:".format(i,players[i].name))
                        players[i].hand.affiche_tools()
                        print("Please, don't do anything else and just play!")
                
            except ValueError:
                os.system("cls")  #efface le contenue de la console, valable que sur windows
                #On affiche les outils des joueurs
                for i in range(len(players)):
                    print("{0}:{1}'s tools:".format(i,players[i].name))
                    players[i].hand.affiche_tools()
                    print("Please, don't do anything else and just play!")

        os.system("cls")  #efface le contenue de la console, valable que sur windows

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
    

    def tourjoueur(self,plateau,pioche,defausse,players):

        change = 1
        while change==1:
            #Le joueur choisi une action
            choix_action=self.__choix_action(plateau)

            if choix_action == 1:
                #On demande au joueur quel carte il veut jouer
                choix_carte, change=self.__choix_carte(plateau,choix_action)
            
                if change==1 :pass

                else:
                    #La carte est un chemin
                    if choix_carte.typ==0:
                        #On demande au joueur où il veut poser sa carte
                        pos=self.__choix_pos(plateau,choix_carte)
              
                        #La carte est placee sur le plateau 
                        plateau.add_carte(choix_carte,pos)


                    #La carte est une carte action d'outils
                    if choix_carte.typ==1:
                        self.__use_tools_card(players,choix_carte)
                

                    #La carte est un plan secret 
                    if choix_carte.typ==2: 
                        print("Which end card do you want to see? (1 to 3)")


                    #La carte est un chemin
                    if choix_carte.typ==6: pass

            

            if choix_action == 2:

                #On demande au joueur quelle carte il veut se defausser
                choix_carte,change=self.__choix_carte(plateau,choix_action)

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