import numpy as np
import random
from abc import ABC, abstractmethod
import os
from hand import Hand
from card import Carte
from board import Plateau
import sys



class Player(ABC):
    def __init__(self,name,role,nb_players):
        self.__name = name
        self.__role = role    #le role c'est de la classe menu.personnage[i]
        self.hand = nb_players   #pour afficher la main: player.hand.display_hand()

    #Methode qui permet de faire piocher une carte au joueur
    def piocher_carte(self,pioche):
        if len(pioche)<=0:
            print("Erreur: la pioche est vide")
            sys.exit()
        
        self.hand.add_card(pioche[0])
        pioche.remove(pioche[0])

    #Methode qui permet d'enlever une carte au joueur
    def defausse_carte(self,card,defausse):
        defausse.append(card)
        self.hand.remove_card(card)

    #Methode abstraite qui permet à un humain ou à une IA de jouer pendant un tour 
    #@abstractmethod
    #def tourjoueur(self,plateau,pioche,defausse): pass



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


    def hand(self):
        return self.hand

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
