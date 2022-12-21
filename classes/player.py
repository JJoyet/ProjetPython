import numpy as np
import random
import os
from hand import Hand



class Player(object):
    def __init__(self,name,role,nb_players):
        self.__name = name
        self.__role = role    #le role c'est de la classe menu.personnage[i]
        self.__hand = Hand(nb_players) #pour afficher la main: player.hand.display_hand()

    def piocher_carte(self,pioche):
        pioche[0].face=1
        self.__hand.cards.append(pioche[0])
        pioche.remove(pioche[0])

    def choix_action(self,plateau):
        #Le joueur choisi une action
        print("What action do you want to take?")
        print("1) Use a card")
        print("2) Passing your turn and throw away a card")
        choix_action=int(input())

        #On s'assure que le joueur choisi une action parmis les actions possibles
        while choix_action !=1 and choix_action !=2:
            print("Please, don't do anything else and just play!")
            print("1) Use a card")
            print("2) Passing your turn and throw away a card")
            choix_action=int(input())
        return choix_action

    def choix_carte_act(self,plateau):

        #On demande au joueur quel carte il veut jouer
        no_carte=int(input("What card would you like to play (1 to {0})?".format(self.__hand.hand_size)))-1

        #On s'assure que le joueur choisisse une de ses cartes
        while no_carte < 0 or no_carte > self.__hand.hand_size-1:
            print("Please, do not steal a card from your neighbour!")
            no_carte=int(input("What card would you like to play (1 to {0})?".format(self.__hand.hand_size)))-1

        #On recupere la carte que le joueur a choisi
        choix_carte=self.__hand.cards[no_carte]

        return choix_carte

    def choix_carte_rem(self,plateau):
        #On demande au joueur quelle carte il veut se defausser
        no_carte=int(input("Which card do you want to throw away (1 to {0})?".format(self.__hand.hand_size)))-1

        #On s'assure que le joueur choisisse une de ses cartes
        while no_carte < 0 or no_carte > self.__hand.hand_size-1:
            print("Please, don't steal a card from your neighbour!")
            no_carte=int(input("What card would you like to play (1 to {0})?".format(self.__hand.hand_size)))-1
                
        choix_carte=self.__hand.cards[no_carte]

        return choix_carte
    
    def choix_pos(self,plateau):
        pos=[]
        pos.append(int(input("Where do you want to place your card (x value)?")))
        pos.append(int(input("(y value)?")))
            
        #On s'assure que le joueur pose bien la carte sur le plateau
        while pos[0] < 0 or pos[0] > 4 or pos[1] < 0 or pos[1] >8 :
            print("Please place the card on the board (0<=x<=4) (0<=y<=8)")
            pos=[]
            pos.append(int(input("Where do you want to place your card (x value)?")))
            pos.append(int(input("(y value)?")))
        return pos
    def your_turn_to_play(self, x)
        

    @property
    def name(self):
        return self.__name

    @property
    def role(self):
        return self.__role

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self,hand):
        self.__hand=hand