import numpy as np
import random
from abc import ABC, abstractmethod
import os
from .hand import Hand
from .card import Carte
from .board import Plateau
import sys



class Player(ABC):
    def __init__(self,name,role,nb_players):
        self.__name = name
        self.__role = role    #le role c'est de la classe menu.personnage[i]
        self.__hand = Hand(nb_players)   #pour afficher la main: player.hand.display_hand()

    #Methode qui permet de faire piocher une carte au joueur
    def piocher_carte(self,pioche):
        if len(pioche)<=0:
            print("Erreur: la pioche est vide")
            sys.exit()
        
        self.__hand.add_card(pioche[0])
        pioche.remove(pioche[0])

    #Methode qui permet d'enlever une carte au joueur
    def defausse_carte(self,card,defausse):
        defausse.append(card)
        self.__hand.remove_card(card)

    #Methode abstraite qui permet à un humain ou à une IA de jouer pendant un tour 
    @abstractmethod
    def tourjoueur(self,plateau,pioche,defausse): pass


<<<<<<< HEAD
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
        
=======

>>>>>>> origin/BrancheJulienLaurent3

    @property
    def name(self):
        return self.__name

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self,role):
        if role == "S":
            self.__role=role
        #On defini par default "C" comme role
        else:
            self.__role="C"


    @property
    def hand(self):
        return self.__hand

<<<<<<< HEAD
    @hand.setter
    def hand(self,hand):
        self.__hand=hand
=======
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
>>>>>>> origin/BrancheJulienLaurent3
